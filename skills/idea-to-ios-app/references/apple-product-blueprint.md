# Apple Product Blueprint

Use this reference for the approved implementation scope. Keep the project runnable, dependency ownership clear, and verification repeatable. Extend an existing app in place; create additional product and release components only when requested.

## Contents

1. Approved product contract
2. Account decision
3. Experience map
4. App composition
5. Repository shape
6. Native architecture
7. Backend boundary
8. Definition of a coherent v1

## 1. Approved Product Contract

Implement only the approved contract persisted in `PRODUCT.md`. Confirm it contains:

- target user and usage moment;
- painful job and current workaround;
- first-session outcome and repeated-use loop;
- one measurable success signal;
- core workflow, supporting capabilities, and v1 non-goals;
- local, synced, shared, server, and never-collected data;
- monetization and account implications;
- approved visual direction, media inventory, generator/provider decision, external-processing boundary, and spend limit;
- locales, phone/iPad expectations, and accessibility constraints;
- risks that must be prototyped before broad implementation.

The result must describe a product a user can finish a job with, not a feature list. If approval exists in the conversation or brief, persist it without asking again. Clarify a material conflict or missing product decision before implementing the affected behavior.

## 2. Account Decision

Decide authentication before drawing the welcome screen.

### Prefer guest or local-first use when

- the app has no significant account-based capability;
- all important data can remain on device or use the user's iCloud container;
- an account would only collect identity or gate a trial unnecessarily.

### Use an account when justified by

- cross-platform identity or server-owned data;
- collaboration, shared workspaces, durable server jobs, or private integrations;
- entitlements that must be shared across the product's own accounts or platforms;
- abuse prevention or regulated access that genuinely requires identity.

An App Store purchase alone does not justify a separate product account. Verify the current App Review login rules against the actual account model. When accounts exist, cover session restoration, credential protection, recovery, revocation, deletion, and review access for the chosen provider.

When Sign in with Apple is selected or required, design its whole lifecycle:

- official Sign in with Apple presentation and HIG-compliant copy;
- nonce/state handling and server validation of the identity token when a backend participates;
- stable opaque Apple user identifier in Keychain, never email as identity;
- first-authorization handling because name/email may not be returned later;
- credential-state check at launch and revocation handling;
- recoverable signed-out/session-expired states;
- in-app account deletion, fresh reauthentication when appropriate, backend deletion/token revocation, and local wipe;
- review/demo access that does not expose real personal data.

Fetch current AuthenticationServices docs, HIG, configuration steps, account-deletion technote, and App Review rules using callable Sosumi tools or direct Apple documentation before implementation.

## 3. Experience Map

Start from the core job. A typical product may need these roles, but include only justified screens:

1. **Launch/session gate**: restores local state and routes without flashing the wrong screen.
2. **Welcome/sign-in**: only when the account decision requires it; explain value before identity.
3. **Primary surface**: exposes the first action and current work.
4. **Create/run flow**: focused input, permissions, confirmation, progress, success, and recovery.
5. **Detail/result**: evidence, next action, edit/retry/share as appropriate.
6. **History/library**: only if past work has future value.
7. **Settings/account**: preferences, sync state, support, privacy, terms, export/reset/delete, and sign out.

Specify for each screen:

- user intent and primary action;
- data read/written;
- loading, empty, error, offline, permission, success, and destructive states;
- navigation entry/exit and restoration/deep-link needs;
- analytics event only if measurement is authorized and privacy-compatible.

Choose `NavigationStack` and lightweight route values when a phone flow needs a navigation stack. Use `TabView` for stable peer destinations users switch between frequently. Consider `NavigationSplitView` when the supported iPad layout benefits. Verify current APIs before choosing syntax.

## 4. App Composition

The app entry owns long-lived dependencies and injects them; feature views do not construct production services ad hoc.

```text
App entry
  ├─ configuration and persistence container
  ├─ session/account state when needed
  ├─ entitlement/store state when needed
  └─ RootView
       ├─ deterministic debug/capture hosts (DEBUG only)
       ├─ welcome/sign-in when justified
       └─ primary app shell
```

Keep the root decision small and testable. Avoid duplicated containers, network work during view initialization, and hidden global state.

## 5. Repository Shape

Follow an existing repository first. For a new ship-oriented product, prefer:

```text
AGENTS.md
CLAUDE.md
PRODUCT.md
DESIGN.md
app/
  project.yml or existing Xcode project
  Sources/
    App/
    Domain/
    Features/
    Services/
    DesignSystem/
    Debug/
  Resources/ or Assets.xcassets/
  Config/
  Tests/Unit/
  Tests/UI/
  scripts/
backend/                  # only when justified
website/
  src or equivalent
  public/media/
aso/
  metadata/<locale>/
  screenshots-source/
  strategy.json
  scripts/
Docs/
  competitive-landscape.md
  market-demand.md
  decisions/
    visual-assets.md
  release/
```

Keep shared agent instructions in `AGENTS.md`. A minimal `CLAUDE.md` may import or point to them for Claude Code; Codex reads `AGENTS.md`. Do not duplicate evolving rules in two long files.

This is a full release example, not a mandatory scaffold. For a Build vertical slice, create only the app, applicable tests, and useful documentation/tooling. Add `website/`, `aso/`, and release automation when delivery scope needs them, and `backend/` only when the approved boundary requires it. Preserve existing folders and project generation choices. Connect commands and CI to real subprojects; avoid empty packages.

## 6. Native Architecture

- SwiftUI for native UI; Observation for app/feature state when compatible.
- SwiftData for local domain persistence when it fits; plan and test migrations.
- CloudKit only when sync/sharing is a product requirement, not as a reflex.
- Small concrete types first; introduce protocols where a real integration or deterministic test needs substitution.
- Keep business rules testable without building storage/network abstractions for every feature.
- Follow Swift concurrency isolation for actual shared asynchronous state; avoid speculative service layers.
- App Intents, widgets, notifications, background work, StoreKit, or AI only when the product contract proves their value.

Choose the minimum deployment target from audience and capability requirements. Prefer the latest stable APIs available at that target, with explicit availability paths when necessary. Do not opt into beta-only frameworks by accident.

## 7. Backend Boundary

A backend is allowed only after naming why the device cannot own the work:

- external paid APIs or private keys;
- durable or scheduled jobs;
- webhooks and server-to-server callbacks;
- cross-platform identity/data or collaboration;
- App Store server validation and shared entitlement state;
- moderation, abuse controls, or regulated policy enforcement.

Document request/response contracts, authentication, data minimization, retention/deletion, retries/idempotency, offline behavior, observability, and user-facing failures. Keep `.p8`, API keys, signing material, and environment secrets outside source control and outside the app bundle.

## 8. Definition Of A Coherent V1

- The first outcome works with realistic data.
- Persistence and account behavior match the product contract.
- All reachable production states are intentional.
- Native navigation, controls, Dynamic Type, VoiceOver, dark mode, Reduce Motion, and supported layouts are verified.
- Deterministic fixtures serve the previews, tests, and capture flows in scope without changing production semantics. Test/capture shortcuts stay compile-gated; reviewer access must work in the submitted configuration.
- Approved generated media is stored in the repository, documented with provider/model/prompt provenance, optimized for its consuming surface, and verified in context.
- Build, unit tests, UI tests, and a simulator walkthrough are repeatable from documented commands.
- No speculative framework or backend remains in the project.
