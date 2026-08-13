# iOS Skill Research Notes

Research snapshot: 2026-08-13. `idea-to-ios-app` must re-fetch market evidence, Apple documentation, and store requirements because products, pricing, SDK APIs, review policy, metadata limits, and asset specifications change.

## Product Discovery

- Competitive research must include direct products, adjacent substitutes, and manual or “do nothing” alternatives. Product/listing/pricing claims require current first-party evidence; public reviews help identify patterns but cannot prove market-wide conclusions.
- The companion `competitors` workflow contributes honest strengths/weaknesses, use-case comparisons, centralized evidence, and current research practices. The iOS skill uses these methods for product strategy, not for generating SEO comparison pages.
- The companion `grilling` workflow models product discussion as a decision tree. It asks the current decision frontier in rounds, gives recommendations, waits for the user's decisions, and forbids execution until both sides confirm shared understanding.
- The consolidated skill accepts ideas, briefs, existing agent skills, and workflows. It extracts domain behavior from a source skill while removing agent-only orchestration from the app experience.

## Portability

- The package uses the open Agent Skills structure: a directory named for the skill, a `SKILL.md`, required `name` and `description` frontmatter, and optional `scripts/`, `references/`, and `assets/`. Source: [Agent Skills specification](https://agentskills.io/specification).
- Claude Code discovers the same `SKILL.md` format from its personal and project skill directories. Source: [Claude Code skills documentation](https://code.claude.com/docs/en/skills).
- Codex uses Agent Skills and can load shared installations from `.agents/skills`; `agents/openai.yaml` adds Codex-specific presentation and MCP metadata without changing portable instructions. Source: [Codex skills documentation](https://developers.openai.com/codex/skills/).
- `npx skills` supports installing one source for multiple agents. The bootstrap checks each agent's real project/global skill paths and avoids large CLI JSON listings that can truncate.

## Apple Documentation And Tooling

- Sosumi exposes Apple Developer documentation as Markdown through a remote MCP endpoint. The skill requires both MCP configuration and usable tools in the active session. Source: [Sosumi](https://sosumi.ai/).
- Apple documents connecting external coding agents to Xcode through `xcrun mcpbridge`, with command examples for Claude Code and Codex. The skill treats this bridge as optional and retains `xcodebuild`/`simctl` fallbacks. Source: [Giving external agents access to Xcode](https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode).
- The deployment target cannot be a fixed “latest iOS” value. Each run must inspect the installed stable Xcode/SDK, fetch current framework availability, and record availability guards or user-approved beta dependencies.

## Authentication And App Structure

- Apple provides the native Sign in with Apple control and implementation flow through AuthenticationServices. Sources: [`SignInWithAppleButton`](https://developer.apple.com/documentation/authenticationservices/signinwithapplebutton), [Implementing user authentication with Sign in with Apple](https://developer.apple.com/documentation/authenticationservices/implementing-user-authentication-with-sign-in-with-apple), and [Sign in with Apple HIG](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple).
- App Review Guideline 5.1.1 requires apps that support account creation to offer account deletion in the app, while apps without significant account-based features should allow use without login. Authentication therefore remains a product decision. Source: [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/).
- Apple publishes a technote for account deletion and token revocation in Sign in with Apple systems. Source: [TN3194](https://developer.apple.com/documentation/technotes/tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple).
- SwiftUI navigation supports data-driven stacks and destinations; `TabView` represents peer destinations and should follow the approved information architecture. Sources: [`NavigationStack`](https://developer.apple.com/documentation/swiftui/navigationstack) and [`TabView`](https://developer.apple.com/documentation/swiftui/tabview).

## Testing And Release

- Apple documents Swift Testing for unit/domain coverage while XCUITest remains the UI automation boundary. Sources: [Testing](https://developer.apple.com/documentation/testing), [`XCUIApplication`](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication), and [`XCUIScreenshot`](https://developer.apple.com/documentation/xcuiautomation/xcuiscreenshot).
- App Store screenshots should show the app in use and must follow current device/locale specifications. The skill fetches requirements before capture/export instead of storing numeric limits. Sources: [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) and [Upload app previews and screenshots](https://developer.apple.com/help/app-store-connect/manage-app-information/upload-app-previews-and-screenshots/).
- A privacy-policy URL is part of App Store Connect app privacy configuration. The release workflow builds and verifies live privacy and support pages before submission. Source: [Manage app privacy](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy/).
- App Store Connect supports API-based asset upload. The generated operator must follow the current create/upload/commit lifecycle, remain read-only by default, and require confirmation for mutations. Source: [Uploading assets to App Store Connect](https://developer.apple.com/documentation/appstoreconnectapi/uploading-assets-to-app-store-connect).

## Generated Visual Media

- The skill treats generated imagery as authored product material for approved app and website compositions, while preserving SF Symbols and vector/code icon systems for functional controls.
- Codex may use its host-native `imagegen` workflow. If Claude Code or another host exposes no native generator, the skill asks the user to choose Replicate, another configured provider, or no AI-generated media.
- Replicate uses API tokens for authenticated requests and supports client/HTTP prediction workflows. The skill requires `REPLICATE_API_TOKEN` through the local environment, current model/pricing verification, explicit paid-call authorization, bounded generation, and local download/provenance records. Sources: [Replicate Node.js guide](https://replicate.com/docs/get-started/nodejs), [prediction lifecycle](https://replicate.com/docs/topics/predictions/create-a-prediction), [output files](https://replicate.com/docs/topics/predictions/output-files), [data retention](https://replicate.com/docs/topics/predictions/data-retention), [API tokens](https://replicate.com/docs/topics/security/api-tokens), and [pricing](https://replicate.com/pricing).
- Generated concept comps do not count as implemented app screens or App Store screenshots. Release assets must show the real app with deterministic fictional data.

## Maestro Patterns Retained

The local Maestro project supplied by the user was used only as a process reference. The consolidated skill retains:

- a product approval gate before repository or code execution;
- separate app, optional backend, website, and ASO/release lanes;
- one app entry that owns persistence, session, and long-lived services;
- a root session gate plus a complete account lifecycle when identity is justified;
- deterministic seeded modes for previews, UI tests, review, and marketing capture;
- distinct offline/default tests and opt-in live, paid, or destructive E2E suites;
- versioned listing sources, policy/support pages, screenshot automation, and a dry-run-first App Store Connect operator.

The skill excludes Maestro's domain models, feature names, copy, branding, and screen designs.
