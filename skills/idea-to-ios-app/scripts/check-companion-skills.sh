#!/bin/sh
set -eu

usage() {
  printf '%s\n' 'Usage: check-companion-skills.sh [--check|--print-install|--install] [discovery|build|ship|all] --agent codex|claude-code|all
  discovery      competitor-profiling and grilling (default stage)
  build          discovery plus design, Apple docs, SwiftUI, and testing
  ship, all      build plus review, ASO, and marketing captures
  --check        read-only check of local companion files and MCP configuration
  --print-install  print commands for missing companions; perform no writes
  --install      install missing companions globally for the selected agent(s)

Exit codes: 0 = selected checks passed, 1 = missing companions, 2 = invalid
arguments. Installer failures propagate. File presence does not prove session availability.
Only use --install when the user has authorized installation and MCP setup.'
}

mode=${1:---check}
if [ "$#" -gt 0 ]; then shift; fi
case "$mode" in
  --check|--print-install|--install) ;;
  -h|--help) usage; exit 0 ;;
  *) usage >&2; exit 2 ;;
esac

stage=discovery
case "${1:-}" in
  discovery|build|ship|all) stage=$1; shift ;;
esac

agent=''
if [ "$#" -eq 2 ] && [ "$1" = "--agent" ]; then
  agent=$2
else
  usage >&2
  exit 2
fi
case "$agent" in
  codex|claude-code) selected_agents=$agent ;;
  all) selected_agents='codex claude-code' ;;
  *) usage >&2; exit 2 ;;
esac
case "$stage" in
  discovery) stage_level=1 ;;
  build) stage_level=2 ;;
  ship|all) stage_level=3 ;;
esac

# Each row is used by checking, command previews, and installation.
companions='1|competitor-profiling|coreyhaines31/marketingskills
1|grilling|mattpocock/skills
2|impeccable|pbakaus/impeccable
2|sosumi|https://sosumi.ai
2|swiftui-pro|twostraws/swiftui-agent-skill
2|swift-testing|dpearson2699/swift-ios-skills
3|app-store-review|dpearson2699/swift-ios-skills
3|app-store-optimization|dpearson2699/swift-ios-skills
3|aso|coreyhaines31/marketingskills
3|ios-marketing-capture|ParthJadhav/ios-marketing-capture
3|app-store-screenshots|parthjadhav/app-store-screenshots'

has_skill() (
  target_agent=$1
  target_skill=$2
  search_dir=$(pwd -P)
  project_root=$(git rev-parse --show-toplevel 2>/dev/null) || project_root=$search_dir
  project_root=$(cd "$project_root" && pwd -P)

  while :; do
    case "$target_agent" in
      codex) skill_path="$search_dir/.agents/skills/$target_skill/SKILL.md" ;;
      claude-code) skill_path="$search_dir/.claude/skills/$target_skill/SKILL.md" ;;
    esac
    [ -f "$skill_path" ] && exit 0
    [ "$search_dir" = "$project_root" ] && break
    [ "$search_dir" = / ] && break
    search_dir=$(dirname "$search_dir")
  done

  case "$target_agent" in
    codex)
      codex_root=${CODEX_HOME:-${HOME:?HOME is required}/.codex}
      [ -f "$HOME/.agents/skills/$target_skill/SKILL.md" ] ||
        [ -f "$codex_root/skills/$target_skill/SKILL.md" ] ||
        [ -f "$codex_root/skills/.system/$target_skill/SKILL.md" ]
      ;;
    claude-code)
      [ -f "${HOME:?HOME is required}/.claude/skills/$target_skill/SKILL.md" ]
      ;;
  esac
)

has_sosumi() {
  case "$1" in
    codex) codex mcp get sosumi --json >/dev/null 2>&1 ;;
    claude-code) claude mcp get sosumi >/dev/null 2>&1 ;;
  esac
}

configure_sosumi() {
  case "$1" in
    codex) codex mcp add sosumi --url https://sosumi.ai/mcp ;;
    claude-code) claude mcp add --transport http --scope user sosumi https://sosumi.ai/mcp ;;
  esac
}

failed=0
for target_agent in $selected_agents; do
  for companion in $companions; do
    level=${companion%%|*}
    package=${companion#*|}
    skill=${package%%|*}
    source=${package#*|}
    [ "$level" -le "$stage_level" ] || continue
    if has_skill "$target_agent" "$skill"; then
      if [ "$mode" = "--check" ]; then
        printf 'FOUND: %s (%s)\n' "$skill" "$target_agent"
      fi
      continue
    fi

    case "$mode" in
      --check)
        printf 'MISSING: %s (%s)\n' "$skill" "$target_agent"
        failed=1
        ;;
      --print-install)
        printf 'npx --yes skills add %s -g -a %s -s %s -y\n' "$source" "$target_agent" "$skill"
        ;;
      --install)
        if ! command -v npx >/dev/null 2>&1; then
          printf '%s\n' 'ERROR: Node.js with npx is required for installation.' >&2
          exit 1
        fi
        npx --yes skills add "$source" -g -a "$target_agent" -s "$skill" -y
        if ! has_skill "$target_agent" "$skill"; then
          printf 'ERROR: installer completed but %s is not visible for %s. Inspect its output.\n' "$skill" "$target_agent" >&2
          exit 1
        fi
        ;;
    esac
  done

  if [ "$stage_level" -ge 2 ]; then
    if [ "$mode" = "--check" ]; then
      if has_skill "$target_agent" imagegen; then
        printf 'OPTIONAL: imagegen guidance found (%s); verify the session tool.\n' "$target_agent"
      else
        printf 'OPTIONAL: imagegen guidance not found (%s); use the approved media plan.\n' "$target_agent"
      fi
    fi
    case "$target_agent" in
      codex) agent_cli=codex ;;
      claude-code) agent_cli=claude ;;
    esac
    if ! command -v "$agent_cli" >/dev/null 2>&1; then
      printf '# UNVERIFIED: %s CLI unavailable; check Sosumi in the active session.\n' "$target_agent"
    elif has_sosumi "$target_agent"; then
      if [ "$mode" = "--check" ]; then
        printf 'CONFIGURED: Sosumi (%s); active tools still need verification.\n' "$target_agent"
      fi
    else
      case "$mode" in
        --check)
          printf 'MISSING: Sosumi MCP configuration (%s); direct Apple docs are a fallback.\n' "$target_agent"
          failed=1
          ;;
        --print-install)
          case "$target_agent" in
            codex) printf '%s\n' 'codex mcp add sosumi --url https://sosumi.ai/mcp' ;;
            claude-code) printf '%s\n' 'claude mcp add --transport http --scope user sosumi https://sosumi.ai/mcp' ;;
          esac
          ;;
        --install)
          configure_sosumi "$target_agent"
          if ! has_sosumi "$target_agent"; then
            printf 'ERROR: Sosumi configuration could not be verified (%s).\n' "$target_agent" >&2
            exit 1
          fi
          ;;
      esac
    fi
  fi
done

if [ "$failed" -ne 0 ]; then
  printf '\nInspect --print-install %s --agent %s, or use the documented fallbacks.\n' "$stage" "$agent"
  exit 1
fi
if [ "$mode" != "--print-install" ]; then
  printf 'Selected local checks passed (%s, %s). Verify active-session capabilities separately.\n' "$stage" "$agent"
fi
