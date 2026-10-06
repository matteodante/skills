# Skill Format

Each `skills/<skill-name>/` directory is an installable package. Its required `SKILL.md` starts with YAML frontmatter and contains the instructions an agent needs for one recurring workflow.

## Entrypoint

```yaml
---
name: example-skill
description: Explain what this skill does and the requests that should activate it.
---
```

Follow the [Agent Skills specification](https://agentskills.io/specification). Use a lowercase name with single internal hyphens, matching the directory, within 64 characters. Descriptions must be nonempty and within 1024 characters; keep them much shorter when possible. Put the key capability first.

Optional portable fields include `license`, `compatibility`, `metadata`, and `allowed-tools`. Use them only when useful. `metadata` maps strings to strings; quote version numbers. `compatibility` is limited to 500 characters. Host-specific permissions belong in the appropriate host configuration, not invented frontmatter keys.

The body should cover the task's real decisions, prerequisites, workflow, and completion evidence. Avoid generic agent advice or lists of unrelated triggers. Existing user instructions and authorization remain authoritative.

## Supporting Files

```text
skills/example-skill/
  SKILL.md
  agents/openai.yaml       # optional Codex UI and invocation metadata
  references/             # conditional guidance
  scripts/                # tested helpers
  assets/                 # files used in generated output
```

Create only directories that have a concrete use. Link references from the entrypoint and explain when to read them. Keep paths relative to the document containing the link, within the installed package. For example, an entrypoint can link to `references/build.md`; that reference can link to `../scripts/build.sh`.

Keep substantial detail in one place. A reference should not repeat the entrypoint's entire workflow. Do not copy third-party manuals or depend on a private repository.

For shell examples, quote paths. Scripts should have clear help and exit codes, report unavailable prerequisites, and keep inspection separate from mutation. Test observable behavior when scripts install tools, write files, or make external changes.

## Codex UI Metadata

Optional `agents/openai.yaml` can include:

```yaml
interface:
  display_name: "Example Skill"
  short_description: "Complete a specific recurring workflow"
  default_prompt: "Use $example-skill to complete this task."
```

Keep the short description within 25–64 characters and mention the exact `$skill-name` in the default prompt. Leave implicit invocation at its default unless the user requests explicit-only behavior. Preserve unrelated policy and dependency fields when editing. See [Codex skills metadata](https://developers.openai.com/codex/skills/) for the host format.

## Validation

From the repository root, after installing `requirements-dev.txt`:

```bash
./scripts/validate-skills.sh
python -m unittest discover -s tests -v
```

You can also validate another checkout:

```bash
python scripts/validate_skills.py --root "/path/to/skills repository"
```

The repository validator checks frontmatter delimiters and YAML types, duplicate keys, field limits, directory names, unfinished scaffold markers, selected UI fields, and local Markdown link targets. It checks inline links and reference-link definitions outside fenced examples. Skills cannot link outside their own package; root documentation can link within the repository. The reserved `skills/_template/` directory is excluded.

Remote URL availability, section anchors, plain code paths, and runtime behavior are outside this static check. Review the [behavior scenarios](SKILL_EVALUATION.md) for changed instructions and execute new or changed helpers with safe fixtures.
