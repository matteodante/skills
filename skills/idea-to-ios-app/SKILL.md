---
name: idea-to-ios-app
description: Validate an iPhone app idea or turn an approved product brief, agent skill, or workflow into a native SwiftUI app and optional App Store release. Use for iOS product discovery, market and keyword evidence, product definition, implementation, or launch preparation. For an existing approved app, work only on the requested stage.
---

# Idea to iOS App

Turn a specific user problem into an evidence-backed product decision, a working native app, or a prepared release. Keep the user's scope and existing repository conventions authoritative.

## Choose the Work

| Mode | Outcome |
| --- | --- |
| **Define** | Research, demand evidence, product contract, and open decisions. No app implementation. |
| **Build** | An approved native vertical slice, runnable project, meaningful tests, and documented commands. |
| **Ship** | Release assets, policy/support surfaces, validation, and the last authorized release action. |

For a new idea, define the product before scaffolding or implementation. A matching approved brief, existing product contract, or explicit user instruction to proceed supplies authority: reuse it instead of restarting discovery or requesting the same approval. For an existing app, inspect what exists and enter at the requested stage. Refresh research when a changed assumption affects the work.

Build only the deliverables the user requested. A vertical slice does not imply a backend, marketing website, full ASO system, or release automation. Add those when the approved contract or Ship mode needs them.

## Readiness

1. Inspect the brief, conversation, repository instructions, product/design records, and current worktree before editing.
2. If the input is a skill or workflow, read the resources that define its behavior. Extract domain inputs, decisions, outputs, and validation; leave agent orchestration out of the app experience.
3. Read [tooling and current documentation](references/tooling-and-docs.md) for the active stage. Resolve `<skill-dir>` to this skill's directory and select the active agent:
   ```bash
   sh "<skill-dir>/scripts/check-companion-skills.sh" --check discovery --agent codex
   ```
   Select `build` or `ship` for those stages. Substitute `claude-code` when appropriate; use `all` as the agent only when both installations are in scope.
4. Treat filesystem checks as hints. The active skill catalog and callable tools determine what can run. Use the bundled protocols or current primary documentation when a companion is unavailable. Report the limitation and stop only work that truly needs the missing capability.
5. Install tools, configure MCP, or use paid services only within existing user authorization. Otherwise finish useful work and show exact proposed commands before seeking the missing authority.

## Define: Evidence and Product Decisions

Read [product discovery and approval](references/product-discovery.md).

- State the target user, triggering moment, painful job, current workaround, first outcome, repeat-use loop, and native advantage.
- Research direct competitors, adjacent substitutes, and manual workarounds. Use `competitor-profiling` when available. Find public facts yourself, date sources, separate observations from inference, and explain where competitors win.
- Use `grilling` when available to resolve consequential decisions in short rounds. Ask only questions that affect the next step; reuse answers already given.
- Validate query demand for the intended storefronts after the job and positioning become specific. For a global hypothesis, compare multiple relevant markets; never infer scope from the user's location.
- Label keyword metrics by provider, country, language, access date, scale, and meaning. Apple Ads popularity is relative; listings, result counts, ratings, and reviews do not measure search volume.
- Record unavailable demand as `unverified`. Give a **proceed**, **test**, **reposition**, or **stop** verdict, counterevidence, confidence, and a next validation with success and stop criteria. Do not run a paid experiment without authority.

Present the proposed contract with scope, non-goals, screen/state map, data/account/backend decisions, visual direction, monetization, demand evidence, risks, and delivery constraints. Ask for approval only when it is still missing. Accepted uncertainty stays visible; approval does not turn a hypothesis into evidence.

Persist approved decisions in `PRODUCT.md`, with research and the approval record under `Docs/` using the reference's format. In Define mode, deliver the requested research or contract without starting a build. A request for a written discovery report authorizes writing that report before product approval.

## Build: Working Native Product

Read [the Apple product blueprint](references/apple-product-blueprint.md).

1. Check Build companions for the active agent. Inspect installed Xcode, stable SDKs, schemes, and simulator runtimes before selecting a deployment target. If macOS/Xcode is unavailable, complete portable work and report native verification as blocked.
2. Fetch current Apple guidance for the selected APIs, HIG patterns, entitlements, privacy behavior, and review implications. Prefer callable Sosumi tools; direct Apple documentation is the fallback. Record decision-relevant sources and dates.
3. Extend the existing project or create the smallest complete app structure. Keep long-lived dependencies owned by the app entry; add seams where tests or real integrations need them.
4. Define the visual direction using `impeccable` when available. Preserve an approved `PRODUCT.md` when another skill initializes design context. Read [visual assets](references/visual-assets.md) only when imagery or asset work is needed.
5. Implement the primary workflow, persistence where needed, and reachable loading, empty, error, offline, permission, and success states. Add supporting screens only when they help complete the approved job.
6. Keep guest/local use when identity adds no significant value. If accounts are required, verify the applicable sign-in rules and implement session recovery, secure credentials, revocation, and in-app deletion. Use Sign in with Apple when selected or required; it is not an automatic consequence of having any account.
7. Add a backend only for approved responsibilities the device cannot own, such as private keys, durable jobs, webhooks, or collaboration.

Do not default to subscriptions, CloudKit, AI, tabs, widgets, authentication, or protocol layers. Choose native frameworks and navigation from the product's actual requirements.

## Verify the Product

- Use the existing test framework; for new Swift unit/domain suites, prefer Swift Testing where supported. Use XCUITest for UI automation.
- Test domain rules, persistence/migrations, risky transformations, and the first outcome. Keep seeded UI checks deterministic; make live, paid, and destructive tests opt-in.
- Build and launch the representative path. Inspect supported layouts, Dynamic Type, VoiceOver, Reduce Motion, appearances, localization, and permission/error recovery.
- Review media in its real layout for crop, legibility, accessibility, loading, and memory cost.
- Use native audit/polish guidance when available, fix verified blockers, and repeat checks affected by the fix. Record commands and results; label manual or unavailable checks accurately.

A green build does not establish visual correctness. Debug fixtures and capture hosts must remain isolated from production behavior.

## Ship: Prepare, Verify, Then Act

Read [the release blueprint](references/release-blueprint.md) and check Ship companions for the active agent.

1. Reconcile code/SDK behavior, permissions, entitlements, privacy declarations, account deletion, and reviewer access with current Apple requirements.
2. Prepare accurate product, privacy, and support surfaces; include terms where the product needs them. Reuse existing hosting and release tooling.
3. Refresh ASO evidence and version localized metadata. Validate current field and asset limits before export or upload.
4. Capture the implemented app with deterministic fictional data; compose marketing screenshots from those captures. Generated concept images are not App Store screenshots.
5. Prepare a local validation, remote inspection, and diff path before App Store Connect writes. Keep listing updates, uploads, build selection, submission, pricing, deletion, and release as distinct actions.
6. Build, test, archive, and report readiness with evidence. Execute only authorized external actions, then verify their actual status.

An authorized request to upload or submit does not require repeated confirmation of the same action. When authority is missing, complete the reviewable package first and identify the exact remaining action.

## Handoff

Report the requested outcome, changed files/artifacts, material decisions, validation evidence, and remaining blockers. For discovery, include dated sources, market coverage, metric limitations, and the verdict. For implementation, include runnable commands and checks actually performed. For release, distinguish **prepared**, **uploaded**, **submitted**, and **released**.

Never claim missing research, native tests, live URLs, provider access, or release actions succeeded. Keep credentials and real personal data out of source control, fixtures, and captures.
