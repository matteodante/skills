# Where each agent keeps its configuration and how to change it

Paths are relative to the user's home directory: `~` on macOS and Linux, `%USERPROFILE%` on Windows. Before you edit anything, check which home the app really reads. If a variable such as `CLAUDE_CONFIG_DIR` or `CODEX_HOME` exists in only one shell profile, apps launched outside that shell, like desktop apps and T3 Code, keep using the defaults, and the configuration splits in two.

## Claude Code

| What | Where | Change it with |
| --- | --- | --- |
| Global instructions | `.claude/CLAUDE.md` | Edit the file |
| Settings, permissions, hooks, enabled plugins, marketplaces | `.claude/settings.json` | Edit the JSON and validate it. Plugins: `claude plugin marketplace add OWNER/REPO`, `claude plugin install NAME@MARKETPLACE --scope user` |
| User-scope MCP servers | `mcpServers` in `.claude.json` (the file sits in the home directory, not inside `.claude/`) | `claude mcp add --scope user …`, `claude mcp list` to check health and auth |
| Skills | `.claude/skills/` | Usually links into `.agents/skills/`, see Skills below |
| Subagents | `.claude/agents/` | Copy the files |

The file `.claude/.claude.json` is a stray copy. Claude Code creates it when something launches it with `CLAUDE_CONFIG_DIR=~/.claude`. Check that nothing points there before you delete it.

## Codex

| What | Where | Change it with |
| --- | --- | --- |
| Global instructions | `.codex/AGENTS.md` | Edit the file |
| Model, effort, sandbox, features, MCP servers, plugins, marketplaces | `.codex/config.toml` | Edit, then parse it with `tomllib` before saving. The desktop app rewrites this file, so make the edits with the app closed or restart the app afterwards |
| Hooks | `.codex/hooks.json` | Edit the JSON. On Windows each hook may also need a `commandWindows` |
| Skills | `.agents/skills/` (shared), `.codex/skills/` (Codex only, plus the app's `.system`) | See Skills below |

Machine-specific tables that you should not copy: `notify`, `[mcp_servers.node_repl]` and `computer-use` (the app generates them), `[projects.*]` trust entries, `[hooks.state]` hashes, `[windows]`, and absolute paths such as `sqlite_home`, `log_dir` and `git-worktree-root`. On Windows, `codex` may be missing from PATH. The app keeps the CLI under `%LOCALAPPDATA%\OpenAI\Codex\bin\…\codex.exe`.

## T3 Code

| What | Where |
| --- | --- |
| Server settings: default model, storage cleanup, background activity, provider instances | `.t3/userdata/settings.json` |
| Client UI settings: follow-up behavior, sidebar, fonts, browser | `.t3/userdata/client-settings.json` |
| Keybindings | `.t3/userdata/keybindings.json` |

Do not copy `desktop-settings.json` (window bounds, exposure mode), `environment-id`, `secrets/`, tokens or databases. Restart T3 Code after editing these files. When the T3 MCP tools are available, prefer `t3_environment_preferences_update` for the environment-wide preferences.

## Skills

The `skills` CLI (`npx skills add SOURCE -g -a claude-code -a codex -s NAME… -y`) keeps one copy of each skill in `.agents/skills/`. Codex reads that folder directly. Claude Code sees the skill through a link in `.claude/skills/`: a symlink on macOS and Linux, a junction on Windows. The source of every installed skill is recorded in `.agents/.skill-lock.json`.

- Reinstall a skill on the other machine from its lock entry rather than copying files, so later `npx skills update` runs keep working.
- Copy only the skills that have no lock entry. Put them in `.agents/skills/`, then link them into `.claude/skills/`. On Windows: `New-Item -ItemType Junction -Path … -Target …`.
- If a Claude plugin already ships a skill (hyperframes, runpod, unreal…), install that skill for Codex only (`-a codex`). Otherwise Claude loads it twice.
- Skills with their own installer, such as impeccable, are managed with that installer, never with `npx skills`.

## What to treat as OS-specific

Language servers for one platform (`swift-lsp`), MCP servers that wrap a local app that is not installed on that machine (Blender, Unreal), absolute paths, app-generated entries, and status line or hook commands, which need each OS's path syntax. Port these by hand, or leave them out and say so.
