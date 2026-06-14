# Apple Product Blueprint

Use this reference when turning a raw product idea into an iOS app.

## App Quality Bar

The v1 app should be small, but production-minded:

- one clear primary workflow
- native Apple navigation and controls
- persistent data where the user expects it
- realistic seed/demo data when the app would otherwise be empty
- empty, loading, error, offline, permission, and success states where relevant
- Dynamic Type, dark mode, accessibility labels, and tappable controls sized for touch
- repeatable build/test commands
- secrets excluded from source control

Avoid broad feature lists. Build the smallest coherent app a real target user could try.

## Product Brief Questions

Ask the smallest useful set:

- Who is the target user and when do they open the app?
- What painful job should the app handle first?
- What does success look like after one session?
- What should be stored locally, synced with iCloud, shared, or server-side?
- Does the idea require external LLMs, paid APIs, long jobs, webhooks, or private integrations?
- What visual tone fits the niche?
- What should be intentionally out of scope for v1?

## Apple Stack Decisions

| Need | Prefer | Use backend when |
| --- | --- | --- |
| Native UI | SwiftUI | never for normal app UI |
| Local app state | SwiftData | data must be shared with non-Apple clients |
| iCloud sync | SwiftData + CloudKit or CloudKit records | conflicts need custom server resolution |
| AI assistance | Foundation Models / Apple Intelligence when available | external models, paid APIs, private prompts, or keys are required |
| Reminders | UserNotifications | reminders are coordinated across many users |
| System actions | App Intents | action needs private integrations or server auth |
| Background work | BackgroundTasks where appropriate | work is long-running or must run while device is offline |
| Auth | Sign in with Apple, iCloud account, local-only mode | accounts must work outside Apple ecosystem |

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

## Screen Patterns

Choose the pattern that matches the target workflow.

### Tracker / Personal System

- dashboard
- capture form
- item detail
- history/insights
- settings/privacy

### Learning / Coaching

- path dashboard
- lesson/task detail
- review/tutor
- library/glossary
- learning records

### Generator / Assistant

- brief builder
- generation settings
- draft/output
- revisions/history
- export/share

### Operations / Professional Tool

- status overview
- work queue
- guarded action sheet
- logs/history
- reference/runbook

## Design Rules

- Use native Apple controls first.
- Use SF Symbols for recognizable actions.
- Use cards only for repeated objects, not every section.
- Keep typography matched to context: large only for true page-level hierarchy.
- Keep forms dense, readable, and predictable for operational apps.
- Use color semantically and sparingly.
- Confirm layout on at least one simulator screenshot for substantial UI work.
- Fix text overlap, truncation, and awkward wrapping before final response.

## Backend Boundary

Use a backend only after naming the reason:

- keep secrets out of the app
- call external LLMs or paid APIs
- coordinate multi-user jobs
- process webhooks
- schedule durable server work
- perform billing or server validation

Document:

- what runs on device
- what runs server-side
- what data crosses the boundary
- where secrets live
- offline behavior
- failure states shown in the app

## Validation Checklist

Before final response:

- official Apple docs were consulted for every used Apple framework
- project opens or generates successfully
- build passes on a concrete iOS Simulator destination when possible
- tests pass or failures are reported honestly
- simulator launch/screenshot is checked for substantial UI work when feasible
- no `.env`, private keys, `.p8`, API keys, or provisioning secrets are committed
- final answer names the backend/cloud boundary, if any
