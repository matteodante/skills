---
name: skill-to-ios-app
description: Transform an existing agent skill, SKILL.md, workflow, or inferred skill idea into a native iPhone app using the Apple ecosystem. Use when the user asks to turn a skill into an iOS app, build an Apple-native app from agent instructions, convert a workflow into SwiftUI/SwiftData/CloudKit/App Intents/Foundation Models architecture, or create an iPhone project with optional Apple-first cloud/backend support.
---

# Skill To iOS App

Convert a skill or agent workflow into a native iPhone app. Start by understanding the product, then generate a real Apple-native project instead of a wrapper around the skill text. Keep the first version simple, but make it production-minded, polished, and suitable for the target audience.

## Source Skill Discovery

1. Identify the source skill from the user's path, repo, installed skill name, conversation context, or workspace files.
2. If the source is ambiguous, choose the most likely candidate and ask for confirmation.
3. Read the source `SKILL.md` completely. Read referenced files only when they affect product behavior, domain logic, assets, or validation.
4. Extract:
   - core job the skill performs
   - user inputs and outputs
   - repeated workflow steps
   - domain records worth storing
   - scripts, templates, references, and assets worth turning into app features
   - risky operations that require confirmation, auth, cloud, or backend isolation

## Required Questions

Ask concise questions before implementation unless the user already answered them in the current conversation. Prefer 4-6 questions, not a long interview.

Cover:

1. Target user and niche.
2. The main job the app must do on the first screen.
3. Native Apple-only vs cloud/backend needs, especially for LLM jobs, secrets, long jobs, webhooks, or shared data.
4. Visual style and product tone.
5. Data that must persist locally, sync through iCloud, or stay server-side.
6. Output location, app name, bundle id, Apple team id, and signing constraints when needed.

If the user wants speed, proceed with explicit assumptions and list them before editing.

## Product Mapping

Turn the skill into app behavior:

- Skill instructions -> guided flows, checklists, local rules, and app actions.
- References -> in-app library, glossary, templates, examples, or contextual help.
- Scripts -> native Swift services when practical; backend jobs only when needed.
- Learning/procedure skills -> paths, steps, progress, review, records.
- Review/audit skills -> intake form, findings list, severity, evidence, export.
- Creator/generator skills -> brief builder, draft output, iteration history, export/share.
- Ops/infrastructure skills -> dashboards, runbooks, status, guarded actions, logs.

Design the app around the user's actual workflow, not around a generic landing page.

## Product And Design Standard

The generated app must be simple at first, but not rough:

- target a concrete public and usage context
- make the first screen's primary action obvious
- use native Apple navigation, tab bars, lists, forms, sheets, toolbars, context menus, and SF Symbols where appropriate
- support Dynamic Type, dark mode, accessible labels, sensible hit targets, and predictable gestures
- include empty, loading, error, offline, permission-denied, and success states where relevant
- use restrained visual styling tailored to the niche, not generic cards or marketing composition
- avoid placeholder-only flows; include realistic seed/demo data derived from the source skill when useful

Design around repeated use by the final audience.

## Apple-First Architecture

Use native Apple technologies by default:

- SwiftUI for UI.
- SwiftData for local persistence.
- CloudKit/iCloud when sync, shared state, or lightweight cloud storage is needed.
- App Intents for shortcuts and system actions.
- Local Notifications for reminders and spaced review.
- Foundation Models / Apple Intelligence when available for local AI features.
- Swift Testing or XCTest for core logic.

Allow backend/cloud only when the product needs capabilities the client should not own:

- external LLM API keys or paid model access
- long-running jobs
- scheduled server work
- webhooks
- multi-user admin workflows
- private integrations
- server-side validation, billing, or App Store Server logic

When backend is required, design the smallest backend boundary and explain why it cannot stay client-only. Never put API keys or private signing keys in the iOS app.

Read `references/apple-app-blueprint.md` before planning architecture or writing app code.

## Documentation Gate

Before creating or editing iOS app code, consult current official Apple documentation for every framework or capability used. At minimum, verify the relevant pages for SwiftUI, SwiftData, CloudKit, App Intents, Apple Intelligence/Foundation Models, notifications, entitlements, signing, and testing.

Use official docs for external backend/cloud providers too. Cite the docs used in the final answer.

## Implementation Workflow

1. Inspect the source skill and summarize the product opportunity.
2. Ask the required questions or state assumptions already available.
3. Choose the app architecture and data model.
4. Create a native iOS project. Prefer the repo's existing project-generation pattern; otherwise use a simple Xcode project or `project.yml` with XcodeGen when available.
5. Implement the first useful version: first screen, core workflow, persistence, production states, and at least one realistic seed/example derived from the skill.
6. Add entitlements only when required. Use examples for local config and keep secrets ignored.
7. Add focused tests for seed data, workflow logic, and risky transformations.
8. Validate with the most relevant local checks: project generation, `xcodebuild build`, `xcodebuild test`, and simulator launch/screenshot for UI work when feasible.

## Guardrails

- Do not build an HTML/WebView wrapper unless the user explicitly asks.
- Do not create a marketing landing page as the app's first screen.
- Do not silently add a backend. Ask or explain a concrete necessity first.
- Do not copy secrets from existing projects into the generated app.
- Do not overfit to the original skill file structure; build the user's product workflow.
- Do not ship UI with overlapping text, unstable layout, missing states, or placeholder-only screens.
- Keep generated projects boring and maintainable: clear folders, small models, simple services, repeatable CLI validation.

## Final Output

Report:

- app/project path
- source skill used
- key app screens and data model
- Apple frameworks and any backend/cloud boundary
- validation commands and results
- docs consulted
