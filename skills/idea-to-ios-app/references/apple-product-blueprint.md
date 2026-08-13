# Apple Product Blueprint

Use this reference after discovery and before architecture or app code. Transfer Maestro's delivery discipline: separate product lanes, explicit session ownership, deterministic fixtures, and release automation. Create the product from the user's brief.

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
- locales, phone/iPad expectations, and accessibility constraints;
- risks that must be prototyped before broad implementation.

The result must describe a product a user can finish a job with, not a feature list. If the approved record is missing or conflicts with the requested build, return to the Product Approval Gate.

## 2. Account Decision

Decide authentication before drawing the welcome screen.

### Prefer guest or local-first use when

- the app has no significant account-based capability;
- all important data can remain on device or use the user's iCloud container;
- an account would only collect identity or gate a trial unnecessarily.

### Use an account when justified by

- cross-platform identity or server-owned data;
- collaboration, shared workspaces, durable server jobs, or private integrations;
- subscriptions/entitlements that must be reconciled server-side;
- abuse prevention or regulated access that genuinely requires identity.

When accounts exist, design the whole lifecycle:

- official Sign in with Apple presentation and HIG-compliant copy;
- nonce/state handling and server validation of the identity token when a backend participates;
- stable opaque Apple user identifier in Keychain, never email as identity;
- first-authorization handling because name/email may not be returned later;
- credential-state check at launch and revocation handling;
- recoverable signed-out/session-expired states;
- in-app account deletion, fresh reauthentication when appropriate, backend deletion/token revocation, and local wipe;
- review/demo access that does not expose real personal data.

Use Sosumi immediately before implementation to fetch the current AuthenticationServices docs, HIG, configuration steps, account-deletion technote, and App Review rules.

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

Use `NavigationStack` with typed lightweight route values for phone flows. Use `TabView` only for stable peer destinations users switch between frequently. Consider `NavigationSplitView` when iPad information hierarchy benefits. Fetch current APIs with Sosumi before choosing syntax.

## 4. App Composition

The app entry owns long-lived dependencies and injects them; feature views do not construct production services ad hoc.

```text
App entry
  ├─ configuration and persistence container
  ├─ session/account state
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
  Config/
  Tests/Unit/
  Tests/UI/
  scripts/
backend/                  # only when justified
website/
  src or equivalent
  public/
aso/
  metadata/<locale>/
  screenshots-source/
  strategy.json
  scripts/
Docs/
  competitive-landscape.md
  decisions/
  release/
```

Keep shared agent instructions in `AGENTS.md`. A minimal `CLAUDE.md` may import or point to them for Claude Code; Codex reads `AGENTS.md`. Do not duplicate evolving rules in two long files.

Set up the full shape for Build and Ship even when the first implementation targets only one vertical slice. `backend/` is the exception: create it only when the approved boundary requires it. Connect root commands and CI to the real subprojects; avoid empty decorative packages.

## 6. Native Architecture

- SwiftUI for native UI; Observation for app/feature state when compatible.
- SwiftData for local domain persistence when it fits; plan and test migrations.
- CloudKit only when sync/sharing is a product requirement, not as a reflex.
- Protocol boundaries for network, auth, storage, clocks, notifications, purchases, and expensive transformations.
- Feature/domain code independent of concrete persistence and HTTP clients.
- Actors or isolated services for shared mutable asynchronous state.
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
- Deterministic fixtures serve previews, UI tests, review/demo mode, and marketing capture without changing production semantics.
- Build, unit tests, UI tests, and a simulator walkthrough are repeatable from documented commands.
- No speculative framework or backend remains in the project.
