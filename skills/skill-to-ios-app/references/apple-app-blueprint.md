# Apple App Blueprint

Use this reference when turning a skill into an iOS app architecture.

## App Quality Bar

The v1 app should be small, but production-minded:

- one clear primary workflow adapted from the source skill
- native Apple navigation and controls
- persistent data where the user expects it
- realistic seed/demo data when the app would otherwise be empty
- empty, loading, error, offline, permission, and success states where relevant
- Dynamic Type, dark mode, accessibility labels, and tappable controls sized for touch
- repeatable build/test commands
- secrets excluded from source control

Avoid broad feature lists. Build the smallest coherent app a real target user could try.

## Decision Table

| Need | Prefer | Use backend when |
| --- | --- | --- |
| Local app state | SwiftData | data must be shared with non-Apple clients |
| iCloud sync | SwiftData + CloudKit or CloudKit records | workflows need server-side conflict resolution |
| AI assistance | Foundation Models / Apple Intelligence when available | external models, paid APIs, private prompts, long jobs, or keys are required |
| Reminders | UserNotifications | reminders are coordinated across many users |
| System actions | App Intents | action needs private integrations or server auth |
| Files/templates | Files app, document picker, app bundle assets | files must be generated asynchronously or collaboratively |
| Background work | BackgroundTasks where appropriate | work is long-running, scheduled server-side, or unreliable on device |
| Auth | Sign in with Apple, iCloud account, local-only mode | app needs account systems outside Apple ecosystem |

## Project Shape

Prefer this shape for generated Swift projects:

```text
Sources/
  App/
  Domain/
  Features/
  Services/
Tests/
  AppTests/
Docs/
Config/
```

Common files:

- `Sources/App/<AppName>App.swift`
- `Sources/App/RootView.swift`
- `Sources/Domain/Models.swift`
- `Sources/Services/SeedData.swift`
- `Sources/Services/<Capability>Service.swift`
- `Sources/Features/<Workflow>View.swift`
- `Tests/<AppName>Tests/*Tests.swift`
- `Makefile`
- `project.yml` when using XcodeGen
- `Config/*.example` for local config, never real secrets

## Product Brief Questions

Ask the smallest useful set:

- Who uses this app and in what situation?
- What is the one action the first screen must make obvious?
- What should the app remember after each session?
- Does anything need sync, collaboration, server-side jobs, or external LLMs?
- Should the app feel utilitarian, premium, playful, clinical, educational, or operational?
- What must never leave the device?
- What should be intentionally out of scope for v1?

## Feature Mapping Patterns

### Teaching or Learning Skill

Screens:

- dashboard with current path
- lesson/detail view
- review/tutor view
- library/glossary
- learning records

Models:

- path/course
- lesson/step/block
- quiz/check
- record/glossary item

### Audit or Review Skill

Screens:

- intake form
- findings list
- finding detail with evidence
- export/share

Models:

- audit
- finding
- severity
- evidence
- recommendation

### Generator Skill

Screens:

- brief builder
- generation settings
- draft/output view
- revision history

Models:

- brief
- template
- draft
- revision

### Operations Skill

Screens:

- status overview
- guarded action form
- logs/history
- runbook/reference

Models:

- resource
- action
- event
- runbook step

## Backend Boundary

Use a backend only after naming the reason. Good reasons:

- keep secrets out of the app
- call external LLMs
- coordinate multi-user jobs
- process webhooks
- schedule work that must run even if the phone is offline
- perform paid/billing/server validation

Document:

- what runs on device
- what runs server-side
- what data crosses the boundary
- where secrets live
- failure modes and offline behavior

## Design Rules

- Use native Apple controls first.
- Use SF Symbols for recognizable actions.
- Use cards only for repeated objects, not every section.
- Keep typography matched to context: large only for true page-level hierarchy.
- Keep forms dense, readable, and predictable for operational apps.
- Use color semantically and sparingly.
- Confirm layout on at least one simulator screenshot for substantial UI work.
- Fix text overlap, truncation, and awkward wrapping before final response.

## Validation Checklist

Before final response:

- official Apple docs were consulted for every used Apple framework
- project opens or generates successfully
- build passes on a concrete iOS Simulator destination when possible
- tests pass or failures are reported honestly
- simulator launch/screenshot is checked for substantial UI work when feasible
- no `.env`, private keys, `.p8`, API keys, or provisioning secrets are committed
- final answer names the backend/cloud boundary, if any
