"""Exercise the agent-config-sync summary script through its command line with fake home directories."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "agent-config-sync" / "scripts" / "config_summary.py"


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="")


class ConfigSummaryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="config summary ")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def make_home(self, name, instructions="- rule\n", skills=("alpha",), token="secret-token"):
        home = self.root / name
        write(home / ".claude/CLAUDE.md", instructions)
        write(home / ".codex/AGENTS.md", instructions)
        for skill in skills:
            write(home / ".agents/skills" / skill / "SKILL.md", "---\nname: x\n---\n")
        write(home / ".claude/settings.json", json.dumps({
            "language": "Italian",
            "enabledPlugins": {"one@market": True, "off@market": False},
            "env": {"API_KEY": token},
        }))
        write(home / ".claude.json", json.dumps({"mcpServers": {"docs": {"url": f"https://example.test/?t={token}"}}}))
        write(home / ".codex/config.toml", f'model = "m"\n\n[mcp_servers.docs]\nurl = "https://example.test/?t={token}"\n\n[plugins."p@market"]\nenabled = true\n')
        return home

    def summary(self, home):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "summary", "--home", str(home)],
            capture_output=True, text=True, check=True,
        )
        return result.stdout

    def compare(self, a, b):
        path_a = self.root / "a.json"
        path_b = self.root / "b.json"
        path_a.write_text(self.summary(a), encoding="utf-8")
        path_b.write_text(self.summary(b), encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(SCRIPT), "compare", str(path_a), str(path_b)],
            capture_output=True, text=True,
        )

    def test_summary_reports_names_and_never_secrets(self):
        output = self.summary(self.make_home("mac"))
        data = json.loads(output)
        self.assertEqual(data["claude: plugins"], ["one@market"])
        self.assertEqual(data["claude: mcp servers"], ["docs"])
        self.assertEqual(data["skills: shared (~/.agents/skills)"], ["alpha"])
        if sys.version_info >= (3, 11):
            self.assertEqual(data["codex: plugins"], ["p@market"])
        self.assertNotIn("secret-token", output)

    def test_identical_machines_compare_equal_despite_line_endings(self):
        result = self.compare(self.make_home("mac"), self.make_home("win", instructions="- rule\r\n"))
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertNotIn("DIFFERENT", result.stdout)

    def test_differences_are_reported_with_both_sides(self):
        result = self.compare(self.make_home("mac", skills=("alpha", "beta")), self.make_home("win", instructions="- other\n"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("DIFFERENT  instructions", result.stdout)
        self.assertIn("only in A: ['beta']", result.stdout)

    def test_missing_configuration_is_not_an_error(self):
        empty = self.root / "empty"
        empty.mkdir()
        data = json.loads(self.summary(empty))
        self.assertIsNone(data["skills: shared (~/.agents/skills)"])
        self.assertEqual(data["claude: plugins"], [])


if __name__ == "__main__":
    unittest.main()
