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
    SKILL.md
scripts/
  validate-skills.sh
```

## Add a Skill

1. Copy `templates/skill` to `skills/<skill-name>`.
2. Fill in `SKILL.md`.
3. Add any supporting examples, scripts or templates inside that skill folder.
4. Run:

```bash
./scripts/validate-skills.sh
```

## License

MIT. Only commit content you own or are allowed to publish.
