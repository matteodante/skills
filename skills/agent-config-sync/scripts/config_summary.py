#!/usr/bin/env python3
"""Summarize and compare Claude Code, Codex and T3 Code configuration across machines.

Usage:
  python3 config_summary.py summary [--home DIR] > this-machine.json
  python3 config_summary.py compare a.json b.json

`summary` only reads files and prints one JSON document. Secrets are never printed:
MCP servers and plugins are reported by name, instruction files by hash.
`compare` exits 0 when both summaries match and 1 when they differ.
"""

import argparse
import hashlib
import json
import os
import platform
import sys
from pathlib import Path

try:
    import tomllib
except ImportError:  # Python 3.10
    tomllib = None

INSTRUCTION_FILES = [".claude/CLAUDE.md", ".codex/AGENTS.md"]
SKILL_DIRS = {
    "skills: shared (~/.agents/skills)": ".agents/skills",
    "skills: claude (~/.claude/skills)": ".claude/skills",
    "skills: codex only (~/.codex/skills)": ".codex/skills",
}
# Values that are paths, project-specific or machine state; compare them by hand if needed.
CLAUDE_SKIPPED_KEYS = {"hooks", "statusLine", "autoMode", "env", "enabledPlugins", "extraKnownMarketplaces"}
CODEX_SCALAR_SKIPPED_KEYS = {"notify", "sqlite_home", "log_dir"}
T3_CLIENT_SKIPPED_KEYS = {"onboardingCompletedAt", "mainWindowBounds"}


def read_json(path):
    if not path.is_file():
        return None
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def read_toml(path):
    if not path.is_file():
        return None
    if tomllib is None:
        return {"_error": "reading config.toml needs Python 3.11 or later"}
    with open(path, "rb") as handle:
        return tomllib.load(handle)


def file_hash(path):
    if not path.is_file():
        return None
    normalized = path.read_bytes().replace(b"\r\n", b"\n").strip()
    return hashlib.sha256(normalized).hexdigest()[:12]


def list_skills(path):
    if not path.is_dir():
        return None
    return sorted(entry.name for entry in path.iterdir() if not entry.name.startswith("."))


def enabled_names(table):
    return sorted(name for name, value in (table or {}).items() if value is True or (isinstance(value, dict) and value.get("enabled")))


def summarize_claude(home):
    settings = read_json(home / ".claude/settings.json") or {}
    user_state = read_json(home / ".claude.json") or {}
    return {
        "claude: plugins": enabled_names(settings.get("enabledPlugins")),
        "claude: marketplaces": sorted((settings.get("extraKnownMarketplaces") or {}).keys()),
        "claude: mcp servers": sorted((user_state.get("mcpServers") or {}).keys()),
        "claude: settings": {k: v for k, v in settings.items() if k not in CLAUDE_SKIPPED_KEYS},
        "claude: hook events": sorted((settings.get("hooks") or {}).keys()),
    }


def summarize_codex(home):
    config = read_toml(home / ".codex/config.toml")
    if config is None:
        return {"codex": None}
    if "_error" in config:
        return {"codex": config["_error"]}
    scalars = {k: v for k, v in config.items() if not isinstance(v, dict) and k not in CODEX_SCALAR_SKIPPED_KEYS}
    return {
        "codex: mcp servers": sorted((config.get("mcp_servers") or {}).keys()),
        "codex: plugins": enabled_names(config.get("plugins")),
        "codex: marketplaces": sorted((config.get("marketplaces") or {}).keys()),
        "codex: settings": scalars,
        "codex: features": config.get("features"),
        "codex: hooks.json events": sorted(((read_json(home / ".codex/hooks.json") or {}).get("hooks") or {}).keys()),
    }


def summarize_t3(home):
    userdata = home / ".t3/userdata"
    settings = read_json(userdata / "settings.json")
    client = read_json(userdata / "client-settings.json")
    if client is not None:
        client = {k: v for k, v in client.items() if k not in T3_CLIENT_SKIPPED_KEYS}
    return {"t3: settings": settings, "t3: client settings": client}


def summarize(home):
    summary = {"_machine": {"os": platform.system(), "home": str(home)}}
    summary["instructions"] = {name: file_hash(home / name) for name in INSTRUCTION_FILES}
    for label, relative in SKILL_DIRS.items():
        summary[label] = list_skills(home / relative)
    summary.update(summarize_claude(home))
    summary.update(summarize_codex(home))
    summary.update(summarize_t3(home))
    return summary


def describe_difference(left, right):
    if isinstance(left, list) and isinstance(right, list):
        return [f"only in A: {sorted(set(left) - set(right))}", f"only in B: {sorted(set(right) - set(left))}"]
    if isinstance(left, dict) and isinstance(right, dict):
        lines = []
        for key in sorted(set(left) | set(right)):
            if left.get(key) != right.get(key):
                lines.append(f"{key}: A={json.dumps(left.get(key))[:160]} B={json.dumps(right.get(key))[:160]}")
        return lines
    return [f"A={json.dumps(left)[:160]}", f"B={json.dumps(right)[:160]}"]


def compare(path_a, path_b):
    with open(path_a, encoding="utf-8") as handle:
        a = json.load(handle)
    with open(path_b, encoding="utf-8") as handle:
        b = json.load(handle)
    print(f"A: {a.get('_machine')}\nB: {b.get('_machine')}\n")
    differences = 0
    for key in sorted((set(a) | set(b)) - {"_machine"}):
        if a.get(key) == b.get(key):
            print(f"same       {key}")
            continue
        differences += 1
        print(f"DIFFERENT  {key}")
        for line in describe_difference(a.get(key), b.get(key)):
            print(f"    {line}")
    return 1 if differences else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    summary_parser = commands.add_parser("summary", help="print this machine's configuration summary as JSON")
    summary_parser.add_argument("--home", default=os.path.expanduser("~"), help="home directory to read (default: current user)")
    compare_parser = commands.add_parser("compare", help="compare two summary files")
    compare_parser.add_argument("a")
    compare_parser.add_argument("b")
    args = parser.parse_args()

    if args.command == "summary":
        print(json.dumps(summarize(Path(args.home)), indent=1, sort_keys=True, ensure_ascii=False))
        return 0
    return compare(args.a, args.b)


if __name__ == "__main__":
    sys.exit(main())
