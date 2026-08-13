# Matteo Dante Skills

Open source collection of personal agent skills.

This repository is intentionally small and boring:

- one skill per folder under `skills/`
- each skill starts from a `SKILL.md`
- examples, scripts and templates stay close to the skill that uses them
- no private project details, credentials, customer data or copied third-party skill content

## Structure

```text
skills/
  skill-name/
    SKILL.md
    scripts/
    examples/
    assets/
docs/
  SKILL_FORMAT.md
templates/
  skill/
    SKILL.md.template
scripts/
  validate-skills.sh
```

## Add a Skill

1. Create `skills/<skill-name>/`.
2. Copy `templates/skill/SKILL.md.template` to `skills/<skill-name>/SKILL.md`.
3. Fill in `SKILL.md`.
4. Add any supporting examples, scripts, references or assets inside that skill folder.
5. Run:

```bash
./scripts/validate-skills.sh
```

## Skills

- `idea-to-ios-app`: researches and challenges an idea, gets the product contract approved, then turns an idea, brief, skill, or workflow into a complete tested iOS product repository and optional App Store release.

The skill uses the portable Agent Skills format and can be installed for Codex and Claude Code together:

```bash
npx skills add matteodante/skills -g -a codex claude-code \
  -s idea-to-ios-app -y
```

Its staged `scripts/check-companion-skills.sh` gate checks discovery, Apple development, testing, ASO, and screenshot companion skills for both agents and verifies Sosumi MCP configuration before the stage that needs them.

## License

MIT. Only commit content you own or are allowed to publish.
