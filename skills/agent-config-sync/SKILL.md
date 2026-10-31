---
name: agent-config-sync
description: Compare and synchronize Claude Code, Codex and T3 Code configuration across machines (macOS, Windows, Linux) — instructions, skills, plugins, MCP servers, settings and logins. Sets up SSH access when the other machine is unreachable, lets the user choose how to resolve each difference, applies the changes with each tool's own CLI and verifies the result. Use when the user wants the same agent setup on several computers, asks why two machines behave differently, or moves to a new machine.
---

# Agent config sync

The goal: the same Claude Code, Codex and T3 Code setup on every machine the user names. Every difference is resolved the way the user chooses, every change is verified, and every login still needed is listed at the end.

## 1. Reach every machine

Find out where your tools actually run. A desktop client attached to another machine's server, or a remote-control session, still runs everything on the server. For each machine you cannot read directly, follow [connect.md](references/connect.md). Ask the user only for the steps that need them: an elevated prompt, a password or a UI toggle. Give them commands that can be pasted as they are.

## 2. Take inventory

On every machine, run [config_summary.py](scripts/config_summary.py). Over SSH, copy the script first. On Windows, use `python` or `py`.

```bash
python3 scripts/config_summary.py summary > machine-a.json
python3 scripts/config_summary.py compare machine-a.json machine-b.json
```

The summary reads files only. It reports skills, plugins and MCP servers by name and instruction files by hash. It may still contain setting values, so keep summaries out of repositories. Then read the files behind each difference: [locations.md](references/locations.md) says which file holds what and what is machine-specific. While you read, look for leftovers of past migrations: a config-dir variable set in only one shell profile, stray copies such as `.claude/.claude.json`, old backups, and instruction files that contradict each other or describe a setup that no longer exists.

## 3. Let the user decide

Group the differences and ask with a multiple-choice question when the host supports one. Use one question per group: instructions, skills, Claude plugins, MCP servers, Codex app plugins, and setting values. For each group, name the actual items and offer:

- **Union on every machine (recommended for skills, plugins and MCP servers).** Leave out items that only work on one OS and say which ones.
- **One machine is the reference.** This usually fits setting values; recommend the machine the user configured most recently.
- **Choose item by item.**

For instruction files that contradict each other, quote both versions and ask which one is true, after checking the facts yourself. Example: does the variable the file mentions exist at all? Ask before you delete anything, and before you copy secrets such as API tokens embedded in MCP URLs or env blocks to another machine. If the user already gave a rule ("tokens may be copied", "the Mac is the reference"), apply it without asking again.

## 4. Apply

- Back up every file before you change it, next to the original (`FILE.before-sync`). If the user asks for cleanup, delete these backups once the final verification passes.
- Use each tool's own commands: `npx skills add` from the source in `.skill-lock.json`, `claude plugin install`, `claude mcp add`. Edit JSON and TOML with a parser and validate before writing. Never edit files by string search on one line.
- Keep one copy of each skill in `.agents/skills/`, linked into `.claude/skills/`. Remove duplicates that a plugin already provides.
- Install missing CLIs that a configured MCP server needs, for example the Railway CLI for the `railway` MCP. Use the machine's normal package manager and respect the user's rules about where tools live.
- When the user asked for it, remove what the sync made redundant: old copies, abandoned temp files, stray config files. Look at each target before deleting it.

## 5. Verify and hand off

Run `summary` again on every machine and `compare` again. Every remaining difference must be one the user chose or one that is OS-specific. Check authentication with `claude mcp list`, `codex login status`, `codex mcp list` and each CLI's `whoami`. Then report:

- what changed on each machine, and where the backups are;
- the differences that remain, and why;
- the logins the user must do on each machine, with the exact command or UI path. Examples: `/mcp` inside Claude Code, the MCP settings page of the Codex app, `railway login`;
- the apps to restart so they reload their configuration.

Never claim a login worked, or that a setting is live, until you have seen it.
