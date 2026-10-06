# Release Blueprint

Use this reference for Ship mode or the specific release work requested. Reuse approved product decisions and existing release tools. Prepare and inspect the concrete result before any external action that still needs authorization; do not ask again for actions already authorized.

## Contents

1. Release repository
2. Test lanes
3. Privacy and review
4. Showcase, policy, and support website
5. ASO source of truth
6. Deterministic marketing capture
7. Marketing screenshot composition
8. App Store Connect operator
9. TestFlight and submission

## 1. Release Repository

Adapt to the existing stack. A complete shape usually includes:

```text
app/
  Config/
  Tests/Unit/
  Tests/UI/
  scripts/capture-marketing.sh
  scripts/capture-app-preview.sh       # optional
  scripts/archive-testflight.sh
website/
  src or pages/
  public/
aso/
  metadata/<locale>/
  screenshots-source/<locale>/
  strategy.json
  scripts/asc.mjs
  scripts/upload-screenshots.sh
Docs/release/
  checklist.md
  review-notes.md
  privacy-inventory.md
```

Generated outputs, archives, videos, screenshots, tokens, `.p8` keys, and local environment files stay ignored unless the project versions approved safe source assets.

## 2. Test Lanes

Maintain distinct lanes:

1. **Unit/domain**: deterministic tests for models, rules, migrations, formatting, and real integration boundaries. Preserve the existing framework; prefer Swift Testing for new suites where supported.
2. **UI smoke**: deterministic XCUITest flows using seeded local data and disabled cloud/network dependencies where possible.
3. **Integration**: opt-in tests against owned backend/sandbox services.
4. **Live/paid/destructive**: explicit environment flag, isolated test account, cost/risk warning, and never part of the default scheme.
5. **Manual release**: VoiceOver, Dynamic Type, appearance, localization, permissions, poor network, account revocation/deletion, StoreKit sandbox, device-specific behavior.

The default CI/simulator suite must be repeatable offline. Do not turn production services into mocks globally; inject deterministic implementations only in previews, tests, demo/review, and capture configurations.

Record the exact project generation, build, test, archive, export, and simulator commands. Fail the release gate on test failures, runtime crashes, unresolved P0/P1 native audit findings, missing privacy declarations, or invalid signing. Unverified visual taste does not fail this gate.

## 3. Privacy And Review Gate

Before metadata or upload:

- inventory every collected data category, purpose, linkage/tracking behavior, retention, processor, and deletion path;
- reconcile code/SDK behavior with `PrivacyInfo.xcprivacy`, required-reason APIs, permission usage strings, ATT choice, privacy labels, and the live privacy policy;
- verify every entitlement and background mode is used and explained;
- ensure login is justified; if account creation exists, verify in-app deletion end to end;
- prepare a review account or disclosed demo path reachable in the submitted Release configuration when review cannot reach the feature otherwise; a DEBUG-only capture host cannot provide reviewer access;
- ensure backend services are live and review notes explain non-obvious hardware, permissions, subscriptions, or flows;
- use fictional data in review and marketing assets.

Use `app-store-review` when available and resolve verified blockers. Otherwise follow the checks above using current Apple guidance. Fetch App Review and App Store Connect privacy guidance through Sosumi or direct Apple documentation before the audit.

## 4. Showcase, Policy, And Support Website

Provide the required public information on stable HTTPS URLs before submission. Reuse an existing product website or suitable hosted pages; a new website application is not mandatory. Include:

- a product page with accurate value proposition, real app imagery, App Store link when available, and no unsupported claims;
- `/privacy/` with app-specific collection, processing, retention, deletion, third parties, contact, and effective date;
- terms matched to accounts, user content, subscriptions, and other applicable product behavior when needed;
- `/support/` or `/contact/` with a working support channel and expected response path;
- optional account-deletion instructions, accessibility statement, FAQ, and status links when useful.

Keep product name, support email, legal entity, URLs, and App Store ID in shared site configuration. Verify production URLs, mobile layout, accessibility, metadata, canonical/social cards, error pages, and contact delivery. Legal text must reflect the real data inventory; do not present generated text as legal advice.

## 5. ASO Source Of Truth

Use `aso` and `app-store-optimization` when available and relevant; otherwise use this protocol with current Apple requirements. Store approved source by locale under the existing release structure or `aso/metadata/<locale>/`. Keep positioning, keywords, evidence, screenshot narrative, locale decisions, and freshness in a strategy record; use a machine-readable file only when scripts consume it.

Generate or review:

- name, subtitle, keyword field, promotional text, description, release notes;
- support, marketing, and privacy URLs;
- category, age-rating, pricing/availability, review notes, and localizations;
- screenshot/app-preview captions and ordering;
- optional Custom Product Pages, in-app events, or product-page tests only when justified.

Research live competitors and current store results; separate observed facts from inference. Never overwrite live metadata merely because a draft scores better. Validate every field against current App Store Connect limits immediately before upload.

## 6. Deterministic Marketing Capture

Use `ios-marketing-capture` when available. Keep an existing reliable capture flow, or implement a DEBUG-only capture mode with:

- stable seeded fictional data and deterministic dates/statuses;
- explicit launch arguments/environment for capture, locale, appearance, and scenario;
- production-sized navigation and layouts, with cloud/network/auth replaced only through injected debug dependencies;
- no real accounts, notifications, personal data, unstable clocks, animations, or remote content;
- one manifest mapping ordered marketing moments to screen, state, locale, appearance, and expected filename;
- a script that builds once where practical, installs/launches per scenario, waits for readiness, captures, and validates dimensions/files.

Keep capture hosts compile-gated and unreachable in release builds. Exercise the same visual components as production; do not create fake marketing-only UI.

If an App Preview is useful, use a separate deterministic XCUITest-driven recording flow and validate the current duration, dimensions, codec, frame rate, audio, and device-class requirements before export.

## 7. Marketing Screenshot Composition

Use `app-store-screenshots` after raw captures exist when it fits the requested output. Prefer its shipped editor/template or the repository's existing composition tool. A focused export does not require creating an editor application.

Create a narrative led by the primary outcome, one claim per slide, real in-app captures, legible thumbnail copy, deliberate layout rhythm, localized copy, and current required export sizes. Each individual image must make sense outside the full carousel.

QA every locale/device export for accurate UI, safe claims, clipping, contrast, source-file existence, filenames/order, and current App Store requirements. Screenshots should primarily show the app in use, not splash/login screens. Keep editor state and approved source copy versioned; keep regenerable output policy explicit.

## 8. App Store Connect Operator

Prefer an existing maintained App Store Connect integration. For a manual release, document the dashboard steps and validation. Generate `aso/scripts/asc.mjs` or an equivalent operator only when recurring authorized work needs custom automation. Verify current API documentation for commands actually being implemented, such as:

```text
validate-local
inspect-live
diff-listing
apply-listing --version <version> --confirm
upload-screenshots --locale <locale> --device <device> --confirm
build-status --version <version>
testflight-status --build <build>
review-status --version <version>
```

Requirements:

- default to read-only inspection, validation, or diff;
- require explicit version/app identifiers and an explicit mutation flag such as `--confirm`; passing it executes an already-authorized action rather than creating another conversational approval gate;
- read issuer ID, key ID, app ID, and `.p8` path from environment; keep the private key outside the repository;
- use short-lived JWTs, redact secrets, apply bounded retries, and print actionable API errors;
- validate local metadata, locales, URLs, asset inventory, and current limits before network writes;
- inspect current remote state and make updates idempotent;
- implement the documented asset create/upload-operation/commit lifecycle and verify processing state;
- never select a build, submit for review, release a version, change pricing, or delete remote data as a side effect of another command;
- write sanitized operation reports locally for audit and handoff.

Provide `.env.example` with names only and a dry-run fixture/test for request construction. Use official current API docs and release notes rather than copied endpoints or remembered schemas.

## 9. TestFlight And Submission

The archive/TestFlight script must select the explicit workspace/project, scheme, configuration, team/export options, version/build number, and destination. Validate the archive before upload. Upload only with authorization, then poll/report processing without silently continuing to submission.

Before declaring readiness, confirm:

- clean release build and archive;
- unit/UI suites and required manual checks pass;
- version/build numbers and signing are correct;
- website URLs are live;
- privacy/review audit passes;
- localized metadata and assets are complete;
- screenshot/app-preview files meet current specifications;
- export compliance, content rights, age rating, pricing/availability, review contact, and review notes are complete;
- account deletion and reviewer access work against production-like services;
- remaining blockers, owner, and next action are recorded.

“Ready” means evidence is present. “Uploaded” and “submitted” are separate authorized states and must be reported separately.
