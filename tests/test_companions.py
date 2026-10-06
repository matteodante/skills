"""Check discovery and install side effects with isolated homes and fake CLIs."""

import json
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "skills" / "idea-to-ios-app" / "scripts" / "check-companion-skills.sh"
DISCOVERY = ("competitor-profiling", "grilling")
BUILD = DISCOVERY + ("impeccable", "sosumi", "swiftui-pro", "swift-testing")
SHIP = BUILD + ("app-store-review", "app-store-optimization", "aso",
                "ios-marketing-capture", "app-store-screenshots")


class CompanionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="skill companions ")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.home = self.root / "user home"
        self.project = self.root / "project"
        self.bin = self.root / "bin"
        for path in (self.home, self.project, self.bin):
            path.mkdir()
        self.log = self.root / "calls.jsonl"
        # Only child processes see these temporary directories. The user's
        # environment and installed skills are never changed by this suite.
        self.environment = {
            **os.environ,
            "HOME": str(self.home),
            "CODEX_HOME": str(self.home / ".codex"),
            "PATH": f"{self.bin}:/usr/bin:/bin",
            "SKILLS_TEST_LOG": str(self.log),
        }
        subprocess.run(["git", "init", "--quiet", str(self.project)], check=True)
        self.fake_cli("npx", """
            import json
            import os
            import sys
            from pathlib import Path
            args = sys.argv[1:]
            with open(os.environ['SKILLS_TEST_LOG'], 'a') as log:
                log.write(json.dumps(['npx', *args]) + '\\n')
            if os.environ.get('SKILLS_TEST_INSTALL_FAIL'):
                sys.exit(9)
            if os.environ.get('SKILLS_TEST_INSTALL_NOOP'):
                sys.exit(0)
            agent = args[args.index('-a') + 1]
            skill = args[args.index('-s') + 1]
            directory = '.codex' if agent == 'codex' else '.claude'
            path = Path(os.environ['HOME']) / directory / 'skills' / skill / 'SKILL.md'
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('Installed fixture.')
        """)
        for cli in ("codex", "claude"):
            self.fake_cli(cli, """
                import json
                import os
                import sys
                from pathlib import Path
                name = Path(sys.argv[0]).name
                with open(os.environ['SKILLS_TEST_LOG'], 'a') as log:
                    log.write(json.dumps([name, *sys.argv[1:]]) + '\\n')
                state = Path(os.environ['HOME']) / (name + '-sosumi')
                if sys.argv[2] == 'add':
                    state.touch()
                sys.exit(0 if state.exists() else 1)
            """)

    def fake_cli(self, name, source):
        path = self.bin / name
        path.write_text(f"#!{sys.executable}\n" + textwrap.dedent(source), encoding="utf-8")
        path.chmod(0o755)

    def install_files(self, skills, agent="codex", base=None):
        if base is None:
            directory = ".codex" if agent == "codex" else ".claude"
            base = self.home / directory / "skills"
        for skill in skills:
            path = base / skill / "SKILL.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("Fixture skill.", encoding="utf-8")

    def run_checker(self, mode="--check", stage="discovery", agent="codex", cwd=None):
        return subprocess.run(
            ["/bin/sh", str(CHECKER), mode, stage, "--agent", agent],
            cwd=cwd or self.project, env=self.environment,
            capture_output=True, text=True, check=False,
        )

    def calls(self):
        if not self.log.exists():
            return []
        return [json.loads(line) for line in self.log.read_text().splitlines()]

    def test_only_selected_agent_is_required(self):
        self.install_files(DISCOVERY)
        self.assertEqual(self.run_checker().returncode, 0)
        self.assertEqual(self.run_checker(agent="all").returncode, 1)
        self.assertEqual(self.calls(), [])

    def test_claude_project_and_codex_shared_directories(self):
        self.install_files(DISCOVERY, base=self.project / ".claude" / "skills")
        self.assertEqual(self.run_checker(agent="claude-code").returncode, 0)
        self.assertEqual(self.run_checker().returncode, 1)
        self.install_files(DISCOVERY, base=self.home / ".agents" / "skills")
        self.assertEqual(self.run_checker().returncode, 0)

    def test_project_lookup_stops_at_repository_boundary(self):
        self.install_files(DISCOVERY, base=self.root / ".agents" / "skills")
        nested = self.project / "nested"
        nested.mkdir()
        self.assertEqual(self.run_checker(cwd=nested).returncode, 1)
        self.install_files(DISCOVERY, base=self.project / ".agents" / "skills")
        self.assertEqual(self.run_checker(cwd=nested).returncode, 0)

    def test_custom_codex_home_and_symlinked_skills(self):
        custom = self.root / "custom codex"
        self.environment["CODEX_HOME"] = str(custom)
        source = self.root / "shared skills"
        self.install_files(DISCOVERY, base=source)
        (custom / "skills").mkdir(parents=True)
        for skill in DISCOVERY:
            (custom / "skills" / skill).symlink_to(source / skill, target_is_directory=True)
        self.assertEqual(self.run_checker().returncode, 0)

    def test_print_install_only_lists_missing_companions_and_never_mutates(self):
        self.install_files(("grilling",))
        result = self.run_checker(mode="--print-install")
        self.assertEqual(result.returncode, 0)
        self.assertIn("-a codex -s competitor-profiling", result.stdout)
        self.assertNotIn("-s grilling", result.stdout)
        self.assertEqual(self.calls(), [])
        self.assertEqual(self.run_checker().returncode, 1)

    def test_install_only_missing_skills_and_repeat_is_a_noop(self):
        self.install_files(("grilling",))
        result = self.run_checker(mode="--install")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(self.calls()), 1)
        self.assertIn("competitor-profiling", self.calls()[0])
        self.assertEqual(self.run_checker(mode="--install").returncode, 0)
        self.assertEqual(len(self.calls()), 1)

    def test_install_failure_stops_before_later_mutations(self):
        self.environment["SKILLS_TEST_INSTALL_FAIL"] = "1"
        result = self.run_checker(mode="--install", stage="ship")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(len(self.calls()), 1)
        self.assertFalse((self.home / "codex-sosumi").exists())

    def test_successful_installer_without_files_is_not_reported_ready(self):
        self.environment["SKILLS_TEST_INSTALL_NOOP"] = "1"
        result = self.run_checker(mode="--install")
        self.assertEqual(result.returncode, 1)
        self.assertIn("not visible", result.stderr)
        self.assertEqual(len(self.calls()), 1)

    def test_build_does_not_require_authentication_or_image_generation(self):
        self.install_files(BUILD)
        (self.home / "codex-sosumi").touch()
        result = self.run_checker(stage="build")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertNotIn("MISSING: authentication", result.stdout)
        self.assertNotIn("MISSING: imagegen", result.stdout)
        self.assertTrue(all(call[0] == "codex" and call[2] == "get" for call in self.calls()))

    def test_missing_mcp_is_reported_without_configuring_it(self):
        self.install_files(BUILD)
        result = self.run_checker(stage="build")
        self.assertEqual(result.returncode, 1)
        self.assertFalse((self.home / "codex-sosumi").exists())
        self.assertFalse(any(call[2] == "add" for call in self.calls()))

    def test_install_configures_only_selected_cli(self):
        self.install_files(BUILD, agent="claude-code")
        result = self.run_checker(mode="--install", stage="build", agent="claude-code")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.home / "claude-sosumi").exists())
        self.assertFalse((self.home / "codex-sosumi").exists())
        self.assertTrue(all(call[0] == "claude" for call in self.calls()))

    def test_no_cli_reports_unverified_configuration(self):
        self.install_files(BUILD)
        (self.bin / "codex").unlink()
        result = self.run_checker(stage="build")
        self.assertEqual(result.returncode, 0)
        self.assertIn("UNVERIFIED", result.stdout)
        self.assertEqual(self.calls(), [])

    def test_ship_is_cumulative_and_all_matches_ship(self):
        self.install_files(BUILD)
        (self.home / "codex-sosumi").touch()
        self.assertEqual(self.run_checker(stage="ship").returncode, 1)
        self.install_files(SHIP)
        self.assertEqual(self.run_checker(stage="ship").returncode, 0)
        self.assertEqual(self.run_checker(stage="all").returncode, 0)

    def test_invalid_arguments_fail_before_any_cli_calls(self):
        for args in (
            [], ["--check", "discovery"], ["--check", "build", "--agent", "unknown"],
            ["--check", "unknown", "--agent", "codex"],
            ["--install", "discovery", "--agent", "codex", "extra"],
        ):
            with self.subTest(args=args):
                result = subprocess.run(
                    ["/bin/sh", str(CHECKER), *args], cwd=self.project,
                    env=self.environment, capture_output=True, text=True, check=False,
                )
                self.assertEqual(result.returncode, 2)
        self.assertEqual(self.calls(), [])


if __name__ == "__main__":
    unittest.main()
