# Tooling And Current Documentation

Use this reference at the start of every run and whenever an Apple capability or release requirement enters scope.

## Contents

1. Portability contract
2. Staged companion skills
3. Sosumi MCP
4. Documentation method
5. Framework skill routing
6. Xcode automation
7. Version rule

## Portability Contract

This skill follows the Agent Skills open format:

- `SKILL.md` frontmatter contains only portable `name` and `description` fields.
- Paths are relative to the skill directory; no Claude-only or Codex-only skill variables are required.
- `agents/openai.yaml` is optional Codex UI/tool metadata. Claude Code can ignore it.
- Project guidance belongs in `AGENTS.md`; a short `CLAUDE.md` may import or point to it.

Install this skill for both agents with `npx skills` and keep the same source folder or symlinked installation. Do not maintain divergent Codex and Claude copies.

## Staged Companion Skills

Run the gate for the current stage. It verifies project or global visibility through each agent's actual skill directories instead of parsing a potentially truncated CLI listing.

```bash
sh "<skill-dir>/scripts/check-companion-skills.sh" --check discovery
sh "<skill-dir>/scripts/check-companion-skills.sh" --check build
sh "<skill-dir>/scripts/check-companion-skills.sh" --check ship
```

| Skill | Source | Purpose |
| --- | --- | --- |
| `competitors` | `coreyhaines31/marketingskills` | current competitive research and honest comparison |
| `grilling` | `mattpocock/skills` | dependency-aware product decision rounds |
| `sosumi` | `https://sosumi.ai` | Apple documentation workflow |
| `impeccable` | `pbakaus/impeccable` | product context, native audit, polish |
| `swiftui-pro` | `twostraws/swiftui-agent-skill` | current SwiftUI implementation/review |
| `authentication` | `dpearson2699/swift-ios-skills` | Sign in with Apple and credential lifecycle |
| `swift-testing` | `dpearson2699/swift-ios-skills` | Swift Testing and XCTest boundaries |
| `app-store-review` | `dpearson2699/swift-ios-skills` | review, privacy, entitlement audit |
| `app-store-optimization` | `dpearson2699/swift-ios-skills` | Apple-specific listing conversion |
| `aso` | `coreyhaines31/marketingskills` | ASO research and listing workflow |
| `ios-marketing-capture` | `ParthJadhav/ios-marketing-capture` | deterministic localized in-app captures |
| `app-store-screenshots` | `parthjadhav/app-store-screenshots` | marketing composition and export |
| `imagegen` or equivalent | host-provided capability | optional raster generation/editing for app and website media |

Stages are cumulative:

- **discovery**: `competitors`, `grilling`, `impeccable`;
- **build**: discovery plus `sosumi`, `swiftui-pro`, `authentication`, `swift-testing`, and Sosumi MCP;
- **ship**: build plus review, ASO, capture, and screenshot skills.

`--check` never installs. `--print-install <stage>` prints commands. `--install <stage>` installs that cumulative set globally for both agents and configures Sosumi for installed CLIs; run it only with authorization.

The checker reports local `imagegen` guidance when found but does not fail when it is absent. Image generation is host-dependent and cannot be made portable through an assumed `npx skills` source. At visual-design time, inspect the active session; if no native generator exists, ask the user to choose Replicate, another configured provider, or no AI media. Replicate requires separate authorization, current-doc verification, an environment token, and spend/data decisions.

After installation, invoke each skill at the stage that owns its work. Do not paraphrase a companion skill's workflow from memory. If a required skill cannot be installed or loaded, stop that stage and report the exact dependency rather than silently substituting a weaker process.

## Sosumi MCP

Remote endpoint: `https://sosumi.ai/mcp`

```bash
# Codex
codex mcp add sosumi --url https://sosumi.ai/mcp
codex mcp get sosumi --json

# Claude Code
claude mcp add --transport http --scope user sosumi https://sosumi.ai/mcp
claude mcp get sosumi
```

Restart the agent session if newly configured tools are not exposed. Configuration output does not prove the current session can call the tools.

## Documentation Method

For each selected capability:

1. Search Apple documentation with Sosumi using the framework, symbol, task, and policy terms.
2. Fetch exact pages for the symbol/task, HIG pattern, relevant technote, entitlement/configuration, testing API, release note, and App Review rule.
3. Prefer current primary Apple sources. Use a companion skill as operational guidance, not as a substitute for policy or availability verification.
4. Record URL, access date, deployment-target implication, entitlement/privacy implication, and decision.
5. Re-run the lookup when Xcode, SDK, App Review guidance, App Store Connect requirements, or the selected capability changes.

For Sign in with Apple, the minimum live lookup includes AuthenticationServices implementation, `SignInWithAppleButton`, configuration, HIG, credential revocation/state, token validation, account deletion/revocation, and the current App Review login/deletion rules.

For navigation, fetch the current `NavigationStack`, `NavigationSplitView`, and `TabView` guidance that matches the chosen information architecture.

For release, fetch the current App Review Guidelines, privacy details, screenshot/app-preview specifications, metadata/localization limits, App Store Connect API asset-upload docs, and API release notes immediately before generation or upload. Never preserve numeric limits in this skill.

## Framework Skill Routing

Install additional skills from `dpearson2699/swift-ios-skills` when their capability is selected:

- data: `swiftdata`, `cloudkit`, `core-data`, `swift-codable`;
- app structure: `swift-architecture`, `swift-concurrency`, `swiftui-navigation`, `swiftui-patterns`, `swiftui-layout-components`, `swiftui-performance`;
- system surfaces: `app-intents`, `widgetkit`, `push-notifications`, `background-processing`, `tipkit`, `app-clips`;
- commerce/security: `storekit`, `swift-security`, `cryptokit`;
- intelligence/media: `apple-on-device-ai`, `coreml`, `vision-framework`, `speech-recognition`;
- quality: `ios-accessibility`, `ios-localization`, `debugging-instruments`.

Install only selected capabilities for both agents, for example:

```bash
npx --yes skills add dpearson2699/swift-ios-skills -g \
  -a codex claude-code -s swiftdata cloudkit -y
```

Verify the requested names with the source package's `--list` output before installation.

## Xcode Automation

When the installed Xcode exposes its MCP bridge and the host supports MCP, prefer it for Xcode-specific inspection and automation. Verify the current Apple instructions first. Known command shape:

```bash
codex mcp add xcode -- xcrun mcpbridge
claude mcp add --transport stdio xcode -- xcrun mcpbridge
```

Fall back to explicit `xcodebuild`, `xcrun simctl`, and project-generator commands when the bridge is unavailable. Always report the concrete scheme, configuration, destination, and result.

## Version Rule

Never say a skill “uses the latest iOS” without evidence. Report:

- installed Xcode and Swift versions;
- available stable SDK/runtime;
- chosen minimum deployment target and why;
- capabilities that require availability guards;
- any beta dependency accepted by the user.
