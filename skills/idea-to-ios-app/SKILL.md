---
name: idea-to-ios-app
description: Turn a product idea, rough concept, niche, user problem, or app brief into a native iPhone app using the Apple ecosystem. Use when the user asks to create an iOS app from an idea, validate an app concept, define target audience and UX, or scaffold a SwiftUI/SwiftData/CloudKit/App Intents/Foundation Models project with optional Apple-first backend/cloud support.
---

# Idea To iOS App

Convert an idea into a focused native iPhone app. Start with product clarity, then build a simple first version that still feels production-ready and Apple-native.

## Product Discovery

Ask concise questions before implementation unless the user already answered them. Prefer 5-7 questions.

Cover:

1. Target user, niche, and usage moment.
2. Pain point and promise: what problem the app solves better than the current workaround.
3. First-screen action: what the user should do immediately after opening the app.
4. Data and privacy: what is local, iCloud-synced, shared, or server-side.
5. AI/backend needs: external LLMs, long-running jobs, webhooks, secrets, or collaboration.
6. Visual style: utilitarian, premium, playful, clinical, educational, operational, or another concrete direction.
7. App name, output path, bundle id, Apple team id, and signing constraints when relevant.

If the user wants speed, proceed with explicit assumptions and list them before editing.

## Product Shape

Turn the idea into a first useful app, not a marketing page.

Define:

- core user persona
- top workflow
- smallest useful data model
- first screen and primary action
- 3-5 supporting screens or states
- what is intentionally out of scope for v1
- what makes the app feel credible to its target audience

Keep v1 simple, but not throwaway. A simple production-ready app has fewer features, not weaker craft.

## Apple-First Architecture

Use native Apple technologies by default:

- SwiftUI for UI.
- SwiftData for local persistence.
- CloudKit/iCloud for sync, shared Apple-device data, or lightweight cloud storage.
- App Intents for Shortcuts, Spotlight, Siri, or system actions.
- Local Notifications for reminders and timed user value.
- Foundation Models / Apple Intelligence when available for local AI features.
- Swift Testing or XCTest for core logic.

Allow backend/cloud only when required by the product:

- external LLM API keys or paid model access
- long-running jobs
- scheduled server work
- webhooks
- multi-user admin workflows
- private integrations
- server-side validation, billing, or App Store Server logic

When backend is required, design the smallest boundary and name why it cannot stay on device. Never put API keys, private keys, or signing secrets in the iOS app.

Read `references/apple-product-blueprint.md` before planning architecture or writing app code.

## Design Standard

The first version must feel like a real iPhone app for the target audience:

- use standard Apple navigation, tab bars, lists, forms, sheets, toolbars, context menus, and SF Symbols where appropriate
- support Dynamic Type, dark mode, accessible labels, sensible hit targets, and predictable gestures
- include empty, loading, error, offline, permission-denied, and success states where relevant
- make the main action obvious without visible tutorial text
- use restrained visual styling tailored to the niche, not generic cards or marketing composition
- avoid WebViews and HTML wrappers unless explicitly requested

Design around repeated use, not first-impression decoration.

## Documentation Gate

Before creating or editing iOS app code, consult current official Apple documentation for every Apple framework or capability used. At minimum, verify relevant docs for SwiftUI, SwiftData, CloudKit, App Intents, Apple Intelligence/Foundation Models, notifications, entitlements, signing, accessibility, and testing.

Use official docs for any backend/cloud provider too. Cite the docs used in the final answer.

## Implementation Workflow

1. Clarify the idea with the product discovery questions or state assumptions.
2. Produce a short product decision: target, first workflow, data model, Apple stack, and backend boundary.
3. Create a native iOS project. Prefer the repo's existing project-generation pattern; otherwise use a simple Xcode project or `project.yml` with XcodeGen when available.
4. Implement the first useful version: first screen, core workflow, persistence, seed/demo data, and production states.
5. Add only necessary entitlements and keep local config examples separate from secrets.
6. Add focused tests for seed data, workflow logic, and risky transformations.
7. Validate with project generation, `xcodebuild build`, `xcodebuild test`, and simulator launch/screenshot for UI work when feasible.

## Guardrails

- Do not build a landing page as the app.
- Do not add backend just because the app has AI language in the idea.
- Do not hide product uncertainty behind code volume. Ask or state assumptions.
- Do not ship UI with overlapping text, unstable layout, missing empty states, or placeholder-only flows.
- Do not copy secrets from existing projects.
- Keep the architecture boring, testable, and ready to grow.

## Final Output

Report:

- app/project path
- target audience and first workflow
- key screens and data model
- Apple frameworks and backend/cloud boundary
- validation commands and results
- docs consulted
