# Skill Format

A skill is a folder that teaches an agent how to do one specific kind of work.

Minimum shape:

```text
skills/<skill-name>/
  SKILL.md
```

Recommended shape when useful:

```text
skills/<skill-name>/
  SKILL.md
  scripts/
  examples/
  templates/
```

## `SKILL.md`

Use frontmatter first:

```md
---
name: skill-name
description: Use when...
---
```

Then write practical operating instructions:

- when to use the skill
- what context to gather first
- step-by-step workflow
- safety rules
- expected final output

Keep it specific. A good skill changes behavior for a narrow recurring task.

## Rules

- Do not commit secrets, tokens, customer data or private repo details.
- Do not copy third-party skill content unless its license allows redistribution.
- Prefer small examples over long generic explanations.
- Put helper scripts inside the skill folder when they are specific to that skill.
