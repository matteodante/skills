# Repository Guidance

Prefer the simplest working solution and readable, explicit code. Implement only what the current workflow needs; avoid speculative abstractions, compatibility layers, or mandatory dependencies without a concrete reason.

## Scope

- Installable packages live in `skills/<name>/`; keep their resources self-contained.
- Put triggers in concise frontmatter and conditional detail in linked references.
- Preserve user intent, existing approval, and the requested delivery stage.
- Check current primary sources before changing tool commands or platform requirements.
- Do not change global skill installations or agent configuration merely to develop this repository.

## Checks

After installing `requirements-dev.txt` in a virtual environment, run:

```bash
./scripts/validate-skills.sh
python -m unittest discover -s tests -v
shellcheck scripts/validate-skills.sh skills/idea-to-ios-app/scripts/check-companion-skills.sh
```

Use temporary fixtures and fake CLIs for installer tests. Review changed instructions against `docs/SKILL_EVALUATION.md`; structural tests do not prove good workflow decisions. Update the README and format documentation when public commands or package behavior change.
