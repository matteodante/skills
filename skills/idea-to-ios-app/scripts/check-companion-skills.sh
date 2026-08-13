#!/bin/sh
set -eu

mode=${1:---check}
stage=${2:-all}

usage() {
  printf '%s\n' \
    'Usage: check-companion-skills.sh [--check|--print-install|--install] [discovery|build|ship|all]' \
    '  discovery  competitors, grilling, and impeccable' \
    '  build      discovery plus Sosumi, SwiftUI, authentication, testing, and visual-capability reporting' \
    '  ship       build plus review, ASO, capture, and screenshot skills' \
    '  all        same cumulative set as ship'
}

case "$mode" in
  --check|--print-install|--install) ;;
  -h|--help)
    usage
    exit 0
    ;;
  *)
    usage >&2
    exit 2
    ;;
esac

case "$stage" in
  discovery|build|ship|all) ;;
  *)
    usage >&2
    exit 2
    ;;
esac

discovery_skills='competitors grilling impeccable'
build_skills='sosumi swiftui-pro authentication swift-testing'
ship_skills='app-store-review app-store-optimization aso ios-marketing-capture app-store-screenshots'

case "$stage" in
  discovery) required_skills=$discovery_skills ;;
  build) required_skills="$discovery_skills $build_skills" ;;
  ship|all) required_skills="$discovery_skills $build_skills $ship_skills" ;;
esac

include_build=0
include_ship=0
case "$stage" in
  build) include_build=1 ;;
  ship|all) include_build=1; include_ship=1 ;;
esac

print_discovery_install() {
  printf '%s\n' \
    'npx --yes skills add coreyhaines31/marketingskills -g -a codex claude-code -s competitors -y' \
    'npx --yes skills add mattpocock/skills -g -a codex claude-code -s grilling -y' \
    'npx --yes skills add pbakaus/impeccable -g -a codex claude-code -s impeccable -y'
}

print_build_install() {
  printf '%s\n' \
    'npx --yes skills add https://sosumi.ai -g -a codex claude-code -s sosumi -y' \
    'npx --yes skills add twostraws/swiftui-agent-skill -g -a codex claude-code -s swiftui-pro -y' \
    'npx --yes skills add dpearson2699/swift-ios-skills -g -a codex claude-code -s authentication swift-testing -y' \
    'codex mcp add sosumi --url https://sosumi.ai/mcp' \
    'claude mcp add --transport http --scope user sosumi https://sosumi.ai/mcp'
}

print_ship_install() {
  printf '%s\n' \
    'npx --yes skills add dpearson2699/swift-ios-skills -g -a codex claude-code -s app-store-review app-store-optimization -y' \
    'npx --yes skills add coreyhaines31/marketingskills -g -a codex claude-code -s aso -y' \
    'npx --yes skills add ParthJadhav/ios-marketing-capture -g -a codex claude-code -s ios-marketing-capture -y' \
    'npx --yes skills add parthjadhav/app-store-screenshots -g -a codex claude-code -s app-store-screenshots -y'
}

print_install() {
  print_discovery_install
  if [ "$include_build" -eq 1 ]; then
    print_build_install
  fi
  if [ "$include_ship" -eq 1 ]; then
    print_ship_install
  fi
}

if [ "$mode" = "--print-install" ]; then
  print_install
  exit 0
fi

if [ "$mode" = "--install" ]; then
  if ! command -v npx >/dev/null 2>&1; then
    printf '%s\n' 'ERROR: Node.js with npx is required for installation.' >&2
    exit 1
  fi

  npx --yes skills add coreyhaines31/marketingskills -g -a codex claude-code -s competitors -y
  npx --yes skills add mattpocock/skills -g -a codex claude-code -s grilling -y
  npx --yes skills add pbakaus/impeccable -g -a codex claude-code -s impeccable -y

  if [ "$include_build" -eq 1 ]; then
    npx --yes skills add https://sosumi.ai -g -a codex claude-code -s sosumi -y
    npx --yes skills add twostraws/swiftui-agent-skill -g -a codex claude-code -s swiftui-pro -y
    npx --yes skills add dpearson2699/swift-ios-skills -g -a codex claude-code -s authentication swift-testing -y

    if command -v codex >/dev/null 2>&1 && ! codex mcp get sosumi --json >/dev/null 2>&1; then
      codex mcp add sosumi --url https://sosumi.ai/mcp
    fi
    if command -v claude >/dev/null 2>&1 && ! claude mcp get sosumi >/dev/null 2>&1; then
      claude mcp add --transport http --scope user sosumi https://sosumi.ai/mcp
    fi
  fi

  if [ "$include_ship" -eq 1 ]; then
    npx --yes skills add dpearson2699/swift-ios-skills -g -a codex claude-code -s app-store-review app-store-optimization -y
    npx --yes skills add coreyhaines31/marketingskills -g -a codex claude-code -s aso -y
    npx --yes skills add ParthJadhav/ios-marketing-capture -g -a codex claude-code -s ios-marketing-capture -y
    npx --yes skills add parthjadhav/app-store-screenshots -g -a codex claude-code -s app-store-screenshots -y
  fi
fi

project_has_skill() {
  agent_name=$1
  skill_name=$2
  search_dir=${PWD}

  while :; do
    case "$agent_name" in
      codex)
        [ -f "$search_dir/.agents/skills/$skill_name/SKILL.md" ] && return 0
        [ -f "$search_dir/.codex/skills/$skill_name/SKILL.md" ] && return 0
        ;;
      claude-code)
        [ -f "$search_dir/.claude/skills/$skill_name/SKILL.md" ] && return 0
        ;;
    esac

    [ "$search_dir" = "/" ] && break
    parent_dir=$(dirname -- "$search_dir")
    [ "$parent_dir" = "$search_dir" ] && break
    search_dir=$parent_dir
  done

  return 1
}

global_has_skill() {
  agent_name=$1
  skill_name=$2
  user_home=${HOME:?HOME is required}

  case "$agent_name" in
    codex)
      codex_root=${CODEX_HOME:-$user_home/.codex}
      [ -f "$user_home/.agents/skills/$skill_name/SKILL.md" ] ||
        [ -f "$codex_root/skills/$skill_name/SKILL.md" ]
      ;;
    claude-code)
      [ -f "$user_home/.claude/skills/$skill_name/SKILL.md" ]
      ;;
  esac
}

has_skill() {
  agent_name=$1
  skill_name=$2
  project_has_skill "$agent_name" "$skill_name" || global_has_skill "$agent_name" "$skill_name"
}

has_imagegen_guidance() {
  agent_name=$1
  user_home=${HOME:?HOME is required}

  if has_skill "$agent_name" imagegen; then
    return 0
  fi

  if [ "$agent_name" = "codex" ]; then
    codex_root=${CODEX_HOME:-$user_home/.codex}
    [ -f "$codex_root/skills/.system/imagegen/SKILL.md" ] && return 0
  fi

  return 1
}

failed=0

for skill_name in $required_skills; do
  missing_for=''

  if ! has_skill codex "$skill_name"; then
    missing_for='Codex'
  fi
  if ! has_skill claude-code "$skill_name"; then
    if [ -n "$missing_for" ]; then
      missing_for="$missing_for, Claude Code"
    else
      missing_for='Claude Code'
    fi
  fi

  if [ -n "$missing_for" ]; then
    printf 'MISSING: %s (%s)\n' "$skill_name" "$missing_for"
    failed=1
  else
    printf 'OK: %s (Codex, Claude Code)\n' "$skill_name"
  fi
done

if [ "$include_build" -eq 1 ]; then
  if has_imagegen_guidance codex; then
    printf '%s\n' 'AVAILABLE: imagegen guidance found for Codex; verify the active session exposes an image-generation tool.'
  else
    printf '%s\n' 'OPTIONAL: no imagegen guidance found on disk for Codex; select a provider at visual-design time.'
  fi

  if has_imagegen_guidance claude-code; then
    printf '%s\n' 'AVAILABLE: imagegen guidance found for Claude Code; verify the active session exposes an image-generation tool.'
  else
    printf '%s\n' 'OPTIONAL: no imagegen guidance found on disk for Claude Code; ask the user to choose Replicate, another provider, or no AI media.'
  fi

  if command -v codex >/dev/null 2>&1; then
    if codex mcp get sosumi --json >/dev/null 2>&1; then
      printf '%s\n' 'OK: Sosumi MCP configured for Codex'
    else
      printf '%s\n' 'MISSING: Sosumi MCP configuration for Codex'
      failed=1
    fi
  else
    printf '%s\n' 'SKIP: Codex CLI is not installed; Codex skill files were still checked.'
  fi

  if command -v claude >/dev/null 2>&1; then
    if claude mcp get sosumi >/dev/null 2>&1; then
      printf '%s\n' 'OK: Sosumi MCP configured for Claude Code'
    else
      printf '%s\n' 'MISSING: Sosumi MCP configuration for Claude Code'
      failed=1
    fi
  else
    printf '%s\n' 'SKIP: Claude Code CLI is not installed; Claude skill files were still checked.'
  fi
fi

if [ "$failed" -ne 0 ]; then
  printf '\nRun with --print-install %s for exact commands, or --install %s after authorization.\n' "$stage" "$stage"
  exit 1
fi

printf 'Companion skills are ready for the %s stage in Codex and Claude Code.\n' "$stage"
