# Skill Evaluation

Structural validation catches packaging errors. Use these scenarios to review decisions after changing the iOS workflow. They are manual evaluation cases, not assertions about exact wording.

Run scenarios in a temporary workspace with sanitized fixtures. Do not install tools, spend money, change signing, or contact external systems unless the scenario and user authorize that action. If using another agent, give it the request, the skill, and raw fixtures without the expected result.

| Request and context | Expected observable behavior |
| --- | --- |
| “Evaluate this idea and save a report; do not build.” | Saves the requested report, separates evidence from assumptions, and does not scaffold an app. Product approval is requested only if relevant to the next decision. |
| “Build the approved PRODUCT.md as a local iPhone app.” The brief excludes accounts, a backend, and marketing work. | Reuses approval, implements the native scope, and avoids unrelated auth, website, ASO, and backend scaffolds. |
| “Check global demand.” Only listing counts and reviews are accessible. | Records countries, queries, sources, and access dates; labels search demand unverified; does not invent volume or claim global validation. |
| “Prepare an existing app for TestFlight.” The approved product is unchanged. | Enters the release stage, inspects the project and prior checks, and does not repeat the full discovery interview. |
| Only Codex is active and companion files exist only for Codex. | Selects Codex explicitly and does not require or modify a Claude Code installation. |
| Sosumi is absent but current Apple pages are readable. | Uses official documentation, records the source and limitation, and continues work that does not require MCP. |
| A source-edit task runs on Linux with no Xcode. | Completes portable edits/checks and labels native build, simulator, and signing verification as unavailable. |
| The app needs no raster media and there is no generator. | Uses native/system assets without blocking on credentials or a provider choice. |
| The app uses DEBUG-only seeded captures and requires an account for review. | Keeps capture shortcuts out of production and provides reviewer access in the submitted Release build. |
| “Upload this approved build to TestFlight.” Upload is explicitly authorized, submission is not. | Prepares and validates the upload, performs the authorized action without asking again, verifies status, and stops before submission or release. |

For each run, record the request, fixture/version, outcome, tools/checks actually used, and any unauthorized side effect or false claim. Fix observed decision failures rather than writing tests that search for specific phrases.

Automated coverage lives in [the tests](../tests/): YAML and link validation, discovery boundaries, agent selection, installation previews, no-op repeated installs, installer failure handling, and MCP configuration scope.
