#!/usr/bin/env python3
"""Validate portable skill metadata and the repository's local references."""

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ModuleNotFoundError:
    sys.exit("PyYAML is required. Install requirements-dev.txt in a virtual environment.")


FRONTMATTER_FIELDS = {
    "name", "description", "license", "compatibility", "metadata", "allowed-tools"
}
SKILL_NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
LINK_TARGET = re.compile(
    r"\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)(?:\s+\"[^\"\n]*\")?\s*\)"
    r"|^\s{0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)",
    re.MULTILINE,
)


class UniqueKeyLoader(yaml.SafeLoader):
    """Catch accidental duplicate keys instead of silently keeping the last."""

    def construct_mapping(self, node, deep=False):
        mapping = super().construct_mapping(node, deep=deep)
        if len(mapping) != len(node.value):
            raise yaml.constructor.ConstructorError(
                None, None, "duplicate YAML key", node.start_mark
            )
        return mapping


def load_mapping(text):
    value = yaml.load(text, Loader=UniqueKeyLoader)
    if not isinstance(value, dict):
        raise ValueError("YAML must be a mapping")
    return value


def prose_only(text):
    """Leave fenced examples out of link and unfinished-scaffold checks."""
    lines = []
    marker = None
    for line in text.splitlines():
        fence = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            run, suffix = fence.groups()
            if marker is None:
                marker = run
            elif run[0] == marker[0] and len(run) >= len(marker) and not suffix.strip():
                marker = None
            continue
        if marker is None:
            lines.append(line)
    return "\n".join(lines)


def validate_frontmatter(skill_dir):
    path = skill_dir / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.DOTALL)
    if not match:
        return ["must start with YAML frontmatter between --- lines"]

    try:
        metadata = load_mapping(match.group(1))
    except (yaml.YAMLError, ValueError) as error:
        return [f"invalid frontmatter: {error}"]

    errors = []
    for key in metadata:
        if key not in FRONTMATTER_FIELDS:
            errors.append(f"unsupported frontmatter field: {key}")

    name = metadata.get("name")
    if not isinstance(name, str) or not SKILL_NAME.fullmatch(name) or len(name) > 64:
        errors.append("name must be 1–64 lowercase letters/digits with single internal hyphens")
    elif name != skill_dir.name:
        errors.append(f"name must match directory '{skill_dir.name}'")

    description = metadata.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        errors.append("description must be a non-empty string of at most 1024 characters")
    elif "[TODO:" in description:
        errors.append("description contains an unfinished placeholder")

    for field in ("license", "compatibility", "allowed-tools"):
        if field in metadata:
            value = metadata[field]
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{field} must be a non-empty string")
            elif field == "compatibility" and len(value) > 500:
                errors.append("compatibility must be at most 500 characters")

    if "metadata" in metadata:
        values = metadata["metadata"]
        if not isinstance(values, dict) or any(
            not isinstance(key, str) or not isinstance(value, str)
            for key, value in values.items()
        ):
            errors.append("metadata must map strings to strings")

    body = text[match.end():].strip()
    if not body:
        errors.append("skill instructions must not be empty")
    if "[TODO:" in prose_only(body) or name == "replace-with-skill-name":
        errors.append("skill contains an unfinished scaffold placeholder")
    return errors


def validate_interface(skill_dir):
    path = skill_dir / "agents" / "openai.yaml"
    if not path.exists():
        return []
    try:
        metadata = load_mapping(path.read_text(encoding="utf-8"))
    except (yaml.YAMLError, ValueError) as error:
        return [f"invalid YAML: {error}"]

    interface = metadata.get("interface", {})
    if not isinstance(interface, dict):
        return ["interface must be a mapping"]

    errors = []
    for field in ("display_name", "short_description", "default_prompt"):
        if field not in interface:
            continue
        value = interface[field]
        if not isinstance(value, str) or not value.strip():
            errors.append(f"interface.{field} must be a non-empty string")
            continue
        if field == "short_description" and not 25 <= len(value) <= 64:
            errors.append("interface.short_description must be 25–64 characters")
        if field == "default_prompt" and not re.search(
            rf"\${re.escape(skill_dir.name)}(?![a-z0-9-])", value
        ):
            errors.append(f"interface.default_prompt must mention ${skill_dir.name}")

    policy = metadata.get("policy", {})
    if not isinstance(policy, dict):
        errors.append("policy must be a mapping")
    elif "allow_implicit_invocation" in policy and not isinstance(
        policy["allow_implicit_invocation"], bool
    ):
        errors.append("policy.allow_implicit_invocation must be a boolean")
    return errors


def validate_links(path, boundary):
    errors = []
    text = prose_only(path.read_text(encoding="utf-8"))
    for match in LINK_TARGET.finditer(text):
        target = (match.group(1) or match.group(2)).strip("<>")
        url = urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            continue
        resolved = (path.parent / unquote(url.path)).resolve()
        if not resolved.is_relative_to(boundary.resolve()):
            errors.append(f"local link leaves package: {target}")
        elif not resolved.exists():
            errors.append(f"broken local link: {target}")
    return errors


def validate_repository(root):
    skills_root = root / "skills"
    if not skills_root.is_dir():
        return ["skills/ directory is missing"], 0
    skill_dirs = sorted(
        path for path in skills_root.iterdir()
        if path.is_dir() and not path.name.startswith(".") and path.name != "_template"
    )
    if not skill_dirs:
        return ["skills/ contains no skill directories"], 0

    errors = []
    for skill_dir in skill_dirs:
        path = skill_dir / "SKILL.md"
        if not path.is_file():
            errors.append(f"{path.relative_to(root)}: missing SKILL.md")
            continue
        errors.extend(f"{path.relative_to(root)}: {error}" for error in validate_frontmatter(skill_dir))
        interface_path = skill_dir / "agents" / "openai.yaml"
        errors.extend(
            f"{interface_path.relative_to(root)}: {error}"
            for error in validate_interface(skill_dir)
        )
        for markdown in sorted(skill_dir.rglob("*.md")):
            errors.extend(
                f"{markdown.relative_to(root)}: {error}"
                for error in validate_links(markdown, skill_dir)
            )

    documents = sorted(root.glob("*.md")) + sorted((root / "docs").rglob("*.md"))
    for path in documents:
        errors.extend(f"{path.relative_to(root)}: {error}" for error in validate_links(path, root))
    return errors, len(skill_dirs)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parent.parent,
        help="repository to validate (defaults to this script's repository)",
    )
    args = parser.parse_args()
    try:
        errors, count = validate_repository(args.root.resolve())
    except (OSError, UnicodeError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Validated {count} skill(s): metadata, UI fields, and local file links OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
