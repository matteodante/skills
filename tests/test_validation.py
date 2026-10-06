"""Exercise validation through its public command using temporary repositories."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_skills.py"


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="skills validation ")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.skill = self.root / "skills" / "sample-skill"
        self.skill.mkdir(parents=True)
        self.write_skill()

    def write_skill(self, frontmatter=None, body="# Sample\n\nDo the requested work.\n"):
        if frontmatter is None:
            frontmatter = "name: sample-skill\ndescription: Help with a specific recurring task."
        (self.skill / "SKILL.md").write_text(
            f"---\n{frontmatter}\n---\n\n{body}", encoding="utf-8"
        )

    def validate(self):
        return subprocess.run(
            [sys.executable, str(VALIDATOR), "--root", str(self.root)],
            cwd=self.root, capture_output=True, text=True, check=False,
        )

    def assert_invalid(self, message):
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(message, result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_valid_folded_yaml_and_optional_fields(self):
        self.write_skill(
            "name: sample-skill\ndescription: >-\n  Help with a recurring task\n"
            "  that needs this workflow.\nlicense: MIT\ncompatibility: Python 3\n"
            "metadata:\n  version: '1.0'\nallowed-tools: Read"
        )
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_empty_repository_fails(self):
        (self.skill / "SKILL.md").unlink()
        self.skill.rmdir()
        self.assert_invalid("no skill directories")

    def test_missing_manifest_fails(self):
        (self.skill / "SKILL.md").unlink()
        self.assert_invalid("missing SKILL.md")

    def test_fields_in_body_are_not_frontmatter(self):
        (self.skill / "SKILL.md").write_text(
            "# Example\nname: sample-skill\ndescription: Looks valid to grep.\n",
            encoding="utf-8",
        )
        self.assert_invalid("must start with YAML frontmatter")

    def test_malformed_duplicate_and_nonmapping_yaml_fail(self):
        for value in (
            "name: [unfinished", "- name\n- description",
            "name: sample-skill\nname: other\ndescription: Duplicate.",
        ):
            with self.subTest(value=value):
                self.write_skill(value)
                self.assert_invalid("invalid frontmatter")

    def test_name_format_and_directory_match(self):
        for name in ("Bad-Name", "-name", "name--name", "different-name", "a" * 65):
            with self.subTest(name=name):
                self.write_skill(f"name: {name}\ndescription: Useful description.")
                self.assert_invalid("name must")

    def test_description_must_be_a_bounded_nonempty_string(self):
        for value in ("''", "'   '", "false", "[]", "x" * 1025, "'x" + " " * 1024 + "'"):
            with self.subTest(value=value[:30]):
                self.write_skill(f"name: sample-skill\ndescription: {value}")
                self.assert_invalid("description must")

    def test_unknown_fields_and_nonstring_metadata_fail(self):
        self.write_skill("name: sample-skill\ndescription: Example.\nunknown: true")
        self.assert_invalid("unsupported frontmatter field")
        self.write_skill("name: sample-skill\ndescription: Example.\nmetadata:\n  version: 1")
        self.assert_invalid("metadata must map strings")

    def test_empty_instructions_and_template_placeholders_fail(self):
        self.write_skill(body="")
        self.assert_invalid("instructions must not be empty")
        self.write_skill(body="# Sample\n\n[TODO: describe the actual workflow]\n")
        self.assert_invalid("unfinished scaffold")

    def test_links_in_references_are_checked_relative_to_the_document(self):
        references = self.skill / "references"
        references.mkdir()
        self.write_skill(body="Read [the guide](references/guide.md).")
        guide = references / "guide.md"
        guide.write_text("Read [missing details](missing.md).", encoding="utf-8")
        self.assert_invalid("broken local link: missing.md")
        (references / "missing.md").write_text("Details.", encoding="utf-8")
        self.assertEqual(self.validate().returncode, 0)

    def test_links_cannot_depend_on_files_outside_an_installed_skill(self):
        (self.root / "README.md").write_text("Repository guide.", encoding="utf-8")
        self.write_skill(body="Read [repository guide](../../README.md).")
        self.assert_invalid("local link leaves package")

    def test_code_examples_and_remote_urls_are_not_checked_as_local_files(self):
        self.write_skill(body=(
            "# Sample\n[web](https://example.com/a) [anchor](#sample)\n"
            "```md\n[example](missing.md)\n[TODO: sample placeholder]\n```\n"
            "~~~~md\n[another example](missing.md)\n~~~\n~~~~\n"
        ))
        self.assertEqual(self.validate().returncode, 0)

    def test_reference_links_and_paths_with_spaces(self):
        self.write_skill(body="[Guide][guide]\n\n[guide]: <guide with spaces.md>\n")
        self.assert_invalid("broken local link")
        (self.skill / "guide with spaces.md").write_text("Guide.", encoding="utf-8")
        self.assertEqual(self.validate().returncode, 0)

    def test_ui_yaml_fields_and_invocation_policy(self):
        agents = self.skill / "agents"
        agents.mkdir()
        metadata = agents / "openai.yaml"
        metadata.write_text("interface: []\n", encoding="utf-8")
        self.assert_invalid("interface must be a mapping")
        metadata.write_text(
            "interface:\n  default_prompt: Use $sample-skill-extra.\n"
            "policy:\n  allow_implicit_invocation: 'false'\n", encoding="utf-8",
        )
        self.assert_invalid("default_prompt must mention $sample-skill")
        self.assert_invalid("allow_implicit_invocation must be a boolean")
        metadata.write_text(
            "interface:\n  default_prompt: Use $sample-skill to complete the task.\n"
            "  short_description: Complete a specific recurring task\n"
            "policy:\n  allow_implicit_invocation: false\n", encoding="utf-8",
        )
        self.assertEqual(self.validate().returncode, 0)

    def test_root_document_links_are_checked(self):
        (self.root / "README.md").write_text("Read [guide](docs/missing.md).", encoding="utf-8")
        self.assert_invalid("README.md: broken local link")

    def test_wrapper_works_outside_the_repository(self):
        result = subprocess.run(
            ["bash", str(ROOT / "scripts" / "validate-skills.sh")],
            cwd=self.root, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
