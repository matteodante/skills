---
name: idea-to-ios-app
description: Turn an app idea, rough concept, niche, user problem, product brief, existing agent skill, or workflow into a clearly defined, competitively researched, user-approved, native iOS product and complete repository. Use when validating or challenging an iPhone app idea, analyzing its market and competitors, discussing product decisions before implementation, translating a skill into app behavior, designing screens and architecture, building with SwiftUI and Apple frameworks, or preparing tests, ASO, marketing screenshots, a policy/support website, App Store Connect automation, TestFlight, and App Store delivery.
---

# Idea To iOS App

Own the path from uncertain idea to shipped iOS product. Derive the delivery discipline from Maestro: clear product decisions, separated app/release lanes, explicit dependency ownership, deterministic fixtures, tests, and release automation. Never copy Maestro's domain, features, copy, models, branding, or screens.

## Operating Contract

Choose the requested delivery mode:

- **Define**: research, challenge, discuss, and approve the product contract.
- **Build**: complete Define, set up the full repository, and deliver a tested native vertical slice.
- **Ship**: complete Build and the App Store release system through the last authorized external action.

For every mode, complete the Product Approval Gate. Do not scaffold a project, create app code, design screens, or choose architecture until the user approves the product contract. Read-only inspection and research are allowed before approval.

External mutations remain separate approvals: installing global tools, buying services, changing signing, deploying, editing live App Store Connect data, uploading a build, and submitting for review.

## 0. Resolve Inputs And Readiness

Resolve `<skill-dir>` as the directory containing this `SKILL.md`.

1. Read `<skill-dir>/references/tooling-and-docs.md`.
2. Run `sh "<skill-dir>/scripts/check-companion-skills.sh" --check discovery`.
3. If discovery dependencies are missing, use `--install discovery` only with installation authority. Otherwise print the commands with `--print-install discovery` and pause.
4. Inspect the user's brief, conversation, repository instructions, existing product/design documents, and relevant workspace files.
5. If the input is a source skill or workflow, read it completely and inspect referenced scripts, templates, assets, safety boundaries, and validation rules that determine product behavior. Extract domain value; do not build a SKILL.md viewer or generic chat wrapper.

Keep the workflow compatible with both Codex and Claude Code. Do not use host-specific skill syntax without a documented fallback.

## 1. Research The Problem And Market

Read `<skill-dir>/references/product-discovery.md` and follow its evidence protocol.

1. Write a provisional problem statement, target user, usage moment, current workaround, first outcome, and reason for a native iOS app.
2. Find market facts yourself. Do not ask the user to research information available through the workspace, web, App Store, product sites, documentation, pricing pages, changelogs, or public reviews.
3. Invoke `competitors`. Analyze direct competitors, adjacent products, and non-product workarounds. Use current sources and record access dates.
4. Compare audience, job, promise, onboarding/account gate, first-use flow, repeated loop, information architecture, pricing, review themes, App Store messaging/screenshots, strengths, weaknesses, and underserved opportunities.
5. Separate source-backed facts, user claims, and inference. Acknowledge where competitors are better. Do not invent feature gaps or differentiation.
6. Produce an opportunity thesis and the strongest case against building the idea.

Research informs the discussion; it does not settle product decisions for the user.

## 2. Discuss And Stress-Test The Idea

Invoke `grilling` and work through a design tree in rounds.

- Ask the complete current decision frontier, number each question, include a recommended answer with rationale, then wait.
- Recompute the frontier after every response. Do not ask downstream questions before their prerequisites are settled.
- Challenge target, urgency, existing alternatives, differentiation, acquisition, retention, monetization, native advantage, scope, data, account need, risk, and success criteria.
- Resolve contradictions with evidence and explicit tradeoffs. Avoid agreeable summaries that leave decisions implicit.
- Ask the user only for decisions, preferences, private context, and inaccessible evidence. Find public and repository facts yourself.
- Keep an unresolved-decisions list. Do not convert silence into approval.

Finish only when both sides share the same product model and the decision frontier is empty.

## 3. Product Approval Gate

Create a proposed product contract in the conversation using the format in `product-discovery.md`. It must include:

- one-sentence thesis, target user, painful job, current workaround, and why now;
- competitor landscape, category gap, differentiation, and honest disadvantages;
- first-session outcome, repeated-use loop, prioritized scope, and non-goals;
- screen/state map and navigation rationale;
- data ownership, privacy, permissions, account decision, monetization, and backend boundary;
- acquisition/ASO hypothesis, success metrics, kill criteria, key risks, and validation plan;
- delivery mode, repository path, app identity, locales/devices, signing constraints, and unresolved items.

Ask the user to approve or revise this contract. Start execution only after an explicit approval such as “approvo, procedi”. A build request accompanied by an existing approved `PRODUCT.md` counts only after checking that the current request still matches it and surfacing material conflicts.

After approval:

1. persist `PRODUCT.md`, `Docs/competitive-landscape.md`, and `Docs/decisions/product-approval.md` in the repository;
2. invoke `impeccable` initialization/shape using the approved product contract, asking only for missing visual decisions;
3. preserve the approved scope. Return to the user before implementing any material product change.

## 4. Current Apple Documentation Gate

Before architecture, run `sh "<skill-dir>/scripts/check-companion-skills.sh" --check build`. Install missing build dependencies only with authority.

Confirm Sosumi tools are exposed in the active session. Then, for each selected Apple capability:

1. search with Sosumi for the exact task and symbols;
2. fetch current API pages, HIG guidance, technotes, release notes, configuration/entitlement instructions, testing guidance, and applicable App Review rules;
3. invoke the relevant installed framework skill;
4. record sources and decisions in `Docs/decisions/`;
5. resolve the deployment target from the installed stable Xcode SDK, required APIs, and audience. A beta requires user opt-in.

Never hardcode remembered OS versions, store limits, entitlements, or review rules.

## 5. Set Up The Complete Repository

Read `<skill-dir>/references/apple-product-blueprint.md`. For Build or Ship, initialize the entire repository immediately after approval, following existing conventions when present.

Create and connect:

- root `AGENTS.md`, a concise Claude Code bridge in `CLAUDE.md`, `PRODUCT.md`, and decision/release documentation;
- `app/` with project generation/configuration, native sources, unit/UI tests, deterministic debug fixtures, and build/capture/archive scripts;
- `website/` for the showcase, privacy, terms, support/contact, and shared product/legal configuration;
- `aso/` for versioned localized metadata, research/strategy, raw captures, marketing compositions, and App Store Connect scripts;
- `backend/` only when the approved product contract proves that the device cannot own a responsibility;
- CI and documented local commands appropriate to the repository.

Build mode must create the release lanes even when it only implements the first native vertical slice. Do not scatter website, metadata, screenshots, and release scripts across the app project.

## 6. Build The Native Product

Implement the approved vertical slice:

1. app entry and long-lived dependency ownership;
2. guest/session/auth gate according to the approved account decision;
3. primary workflow and persisted domain model;
4. justified detail, history, library, and settings/account/legal surfaces;
5. realistic deterministic demo data;
6. loading, empty, error, offline, permission, success, revocation, and deletion states that can occur in production.

Prefer native Apple frameworks where they fit the verified target. Choose `NavigationStack`, `NavigationSplitView`, sheets, or `TabView` from the approved information architecture. Keep routes typed and lightweight, and keep feature UI independent from storage/network implementations.

Do not require login without significant account-based value. When accounts are justified, implement the complete Sign in with Apple lifecycle, including credential state, revocation, server validation when applicable, Keychain identity, reauthentication, in-app deletion, backend/token deletion, and local wipe.

Use a backend only for approved client-inappropriate work such as secrets, paid external APIs, durable jobs, webhooks, cross-platform identity, collaboration, or server validation.

## 7. Quality And Test Loop

Invoke `swiftui-pro` and selected framework skills during implementation. Then:

1. add Swift Testing coverage for domain rules, persistence/migrations, and risky transformations;
2. add deterministic XCUITest coverage for launch, first outcome, persistence, settings, and account flows that exist;
3. separate offline seeded UI tests from opt-in live, paid, destructive, or backend E2E suites;
4. verify Dynamic Type, VoiceOver, Reduce Motion, appearances, localization expansion, keyboard, phone, and supported iPad layouts;
5. generate/build, test, launch the simulator, and inspect the whole representative path;
6. invoke `impeccable` for native audit and polish, resolve verified P0/P1 findings, and re-run the audit.

A green build does not prove product or visual correctness.

## 8. Ship Pipeline

For Ship mode, read `<skill-dir>/references/release-blueprint.md` and run `sh "<skill-dir>/scripts/check-companion-skills.sh" --check ship` before release work.

Complete, in order:

1. privacy manifest, permissions, entitlements, review access, account deletion, and App Store review audit;
2. production website and live privacy, terms, and support URLs;
3. ASO research, localization, and versioned listing source using `aso` and `app-store-optimization`;
4. deterministic raw captures using `ios-marketing-capture`;
5. marketing compositions and current-size exports using `app-store-screenshots`;
6. dry-run-first App Store Connect operator, screenshot upload path, TestFlight/build/review status, and separate confirmed mutation commands;
7. archive, tests, audit evidence, and unresolved release blockers.

Use fictional data in marketing/review assets. Show the real app in use rather than login, splash, personal data, or invented UI.

## Guardrails

- Do not execute before product approval.
- Do not copy Maestro-specific product details.
- Do not make auth, CloudKit, AI, subscriptions, tabs, widgets, or backend defaults.
- Do not silently install tools, change signing, deploy, upload, edit live metadata, or submit.
- Do not commit `.p8`, provisioning profiles, tokens, `.env`, personal data, or unsafe captures.
- Keep deterministic capture/test paths compile-gated and isolated from release behavior.

## Final Handoff

Report research sources, competitors and opportunity, approved product contract and approval record, repository paths, product/auth/backend decisions, screen map, Apple docs and companion skills used, build/test/audit evidence, website/ASO/assets status, App Store Connect actions, and remaining blockers. Label assumptions and distinguish ready, uploaded, and submitted states.
