#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
missing=0

while IFS= read -r -d '' dir; do
  skill_md="$dir/SKILL.md"
  if [[ ! -f "$skill_md" ]]; then
    echo "Missing SKILL.md: ${dir#$root/}"
    missing=1
    continue
  fi

  if ! grep -q '^name:' "$skill_md"; then
    echo "Missing frontmatter name: ${skill_md#$root/}"
    missing=1
  fi

  if ! grep -q '^description:' "$skill_md"; then
    echo "Missing frontmatter description: ${skill_md#$root/}"
    missing=1
  fi
done < <(find "$root/skills" -mindepth 1 -maxdepth 1 -type d -not -name '_template' -print0)

if [[ "$missing" -ne 0 ]]; then
  exit 1
fi

echo "Skills structure OK"
