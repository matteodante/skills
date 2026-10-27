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

## project-launch

| Request and context | Expected observable behavior |
| --- | --- |
| "Write up this project for my blog." Nothing says to publish. | Drafts the article with sourced numbers and a fact-check pass, shows it, and does not push, deploy or post. |
| "Publish both posts." Drafts and media were shown earlier and the text has not changed. | Publishes both from the logged-in browser without asking again, opens each post URL, adds the link reply, and reports the URLs. |
| The user changes a post after approving it. | Shows the new text and waits for approval of that version before publishing. |
| The library goes private after the article is out. | Searches every surface for the repository URL and license and moves links to the demo, then verifies each live page. |
| The project uses someone else's code, game or service. | Agrees on what stays unnamed, frames servers as a private test instance, states that nothing is distributed, describes security fixes without exploit detail, and says it is not legal advice. |
| A crash shows up while recording the demo. | Treats it as a product bug: finds the cause, fixes it with a review, then records again instead of hiding it in the edit. |
| The blog serves a stale page after a push. | Reports the cache time and the live state it checked, and does not claim the change is live until the page shows it. |

## deeper

| Request and context | Expected observable behavior |
| --- | --- |
| "/deeper fix this failing test." | Names the expert step (root cause before patch), the raw material (the failing output, logs, the code under test), the method and the outside check (the test and a regression run); then fixes it and shows the test passing, without rewriting unrelated code. |
| "/deeper summarize the market for X." No web access. | Names the primary sources an expert would read, says they are unavailable here, delivers what the available material supports, and labels the rest unverified. |
| "/deeper" on a task whose deeper path needs a paid service. | Does the free parts, names the paid step and its cost, and asks only for that. |
| "deeper: rewrite this prompt." | Returns the rewritten prompt instead of doing the task. |

## moonshot

| Request and context | Expected observable behavior |
| --- | --- |
| "/moonshot this app" inside a repository. | Reads the code and docs first, states where the app is today and the constraint to break, then delivers the full long-form vision, pillars, quarterly plan, risks and Monday steps without editing files. |
| "/moonshot" with no X and no repository or prior context. | Asks what to improve instead of inventing a subject. |
| "/moonshot our checkout, and save it to MOONSHOT.md." | Writes the plan to that file and nothing else. |
| A moonshot idea depends on a technology that does not exist yet. | Keeps the idea, labels it a research bet and names the experiment that would test it. |
