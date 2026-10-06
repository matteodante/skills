# iOS Skill Research Notes

Maintenance review: 2026-10-06. These notes explain source choices and workflow decisions; they are not a cache of current API limits, market demand, or deployment requirements. Fetch the relevant primary pages again for each product or release.

## Skills and Tooling

- The [Agent Skills specification](https://agentskills.io/specification) defines portable metadata and the package structure. The repository validator now parses YAML, checks package-local references, and validates optional UI fields rather than searching for field names anywhere in the file.
- [Codex skill discovery](https://developers.openai.com/codex/skills/) and [Claude Code skills](https://code.claude.com/docs/en/skills) use different local locations. The companion checker selects an explicit agent and bounds project searches to the Git root. Its disk/configuration checks are incomplete by design: the active catalog and exposed tools remain authoritative.
- The [skills CLI](https://github.com/vercel-labs/skills) supports selecting skills and agents. The checker shares one companion inventory across check, preview, and install modes, installs only missing companions, and never interprets configuration presence as a successful runtime call.
- [Sosumi](https://sosumi.ai/) provides an Apple documentation interface. It is preferred when callable; direct Apple documentation remains a valid fallback. [Xcode agent access](https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode) is an optional automation path, not a prerequisite for explicit build commands.

## Product Discovery and Demand

- [competitor-profiling](https://github.com/coreyhaines31/marketingskills/tree/main/skills/competitor-profiling) is the relevant companion for competitor research. The same package's `competitors` skill targets comparison/alternative pages. Review the live catalog before choosing an optional keyword specialist.
- [grilling](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling) can help resolve product decisions. The bundled protocol still works without it. Reuse existing answers and approval; scale discussion to consequential unknowns.
- [Apple Ads reporting definitions](https://ads.apple.com/app-store/help/reporting/0023-reporting-options-and-definitions) distinguish Search Popularity from campaign metrics. Record the scale exposed by the actual interface; do not convert a relative indicator into monthly searches.
- [Apple Ads recommendations](https://ads.apple.com/app-store/help/recommendations/0055-review-recommendations) include suggestions and forecast-style estimates. Viewing them does not authorize applying them, changing a budget, or running an experiment.
- Store listings, pricing, reviews, and updates describe products and traction. They do not establish query volume. The discovery reference requires country/language/source/date context, explicit missing evidence, counterarguments, and a proceed/test/reposition/stop verdict.

## Native Product and Review

- [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) tie login obligations to actual account behavior and require reviewer access to account-based features. Apply current rules to the approved product; do not add an account just because authentication guidance is installed.
- Reviewer access must exist in the submitted build. A DEBUG-only capture host can generate marketing assets but cannot serve as release reviewer access. This is an implementation consequence of the review-access requirement, not a separate Apple feature.
- Keep [AuthenticationServices](https://developer.apple.com/documentation/authenticationservices/implementing-user-authentication-with-sign-in-with-apple), [Sign in with Apple HIG](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple), and [account deletion/token revocation](https://developer.apple.com/documentation/technotes/tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple) as live lookups when the chosen account model needs them.
- Choose the deployment target from the installed stable Xcode/SDK, required capability availability, and audience. Preserve existing project conventions and test frameworks. Native build/simulator evidence requires an actual supported host.

## Release and Media

- [Manage app privacy](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy/) is the source for App Store privacy configuration. Public policy/support information must match implemented data behavior; an existing website or hosted pages can provide it.
- Apple's current [Manage your App Store assets](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-your-app-store-assets) covers Asset Library and screenshot/preview management. The former upload-page URL returned a not-found page during this review. Recheck current [screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications) and [app preview specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications) before export.
- Use the current [asset upload API guidance](https://developer.apple.com/documentation/appstoreconnectapi/uploading-assets-to-app-store-connect) when custom automation is justified. Prefer existing tooling; keep inspection, metadata writes, asset upload, build selection, submission, and release separate.
- Generated artwork supports an approved visual direction. It does not establish implemented UI, customer evidence, or App Store screenshots. Capture the real app with fictional data for marketing.
- Native image tooling is conditional. If an approved plan needs external generation, verify the chosen provider's current documentation, data handling, price, and spend boundary. The [visual-assets reference](../skills/idea-to-ios-app/references/visual-assets.md) includes the optional Replicate path.

## Maintenance Boundaries

The workflow is self-contained and does not require access to a private example app. It retains product decisions, native dependency ownership, deterministic test/capture fixtures, and release evidence without prescribing one product's screens or a mandatory multi-package architecture.

This review checked format/discovery documentation, companion catalogs, Apple review/privacy guidance, Apple Ads metric definitions, and the current App Store asset-management page. Framework APIs, generator models/pricing, and authenticated Apple tools were not exercised as part of repository maintenance. They must be verified when a concrete task selects them.
