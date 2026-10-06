# Tooling and Current Documentation

Read for environment setup, companion selection, or current Apple documentation. Check only capabilities needed by the requested stage.

## Portability

The entrypoint uses portable `name` and `description` fields. Resources travel with the skill; `agents/openai.yaml` adds optional Codex presentation and MCP metadata. Keep shared project guidance in `AGENTS.md`; a short `CLAUDE.md` may point to it.

Install for the agents actually in use. A shared source or symlink avoids divergent copies:

```bash
npx skills add matteodante/skills -g -a codex -s idea-to-ios-app -y
# Select both only when both are wanted:
npx skills add matteodante/skills -g -a codex claude-code -s idea-to-ios-app -y
```

## Companion Checks

Run the [companion checker](../scripts/check-companion-skills.sh) from the target project, using its installed skill path:

```bash
sh "<skill-dir>/scripts/check-companion-skills.sh" --check discovery --agent codex
sh "<skill-dir>/scripts/check-companion-skills.sh" --check build --agent claude-code
sh "<skill-dir>/scripts/check-companion-skills.sh" --check ship --agent all
```

The agent argument is required. Stages are cumulative; the default stage is discovery, and `all` as a stage means ship.

| Stage | Companions | Source |
| --- | --- | --- |
| Discovery | `competitor-profiling` | [marketingskills](https://github.com/coreyhaines31/marketingskills) |
| Discovery | `grilling` | [mattpocock/skills](https://github.com/mattpocock/skills) |
| Build | `impeccable` | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| Build | `sosumi` | [Sosumi](https://sosumi.ai/) |
| Build | `swiftui-pro` | [SwiftUI agent skill](https://github.com/twostraws/swiftui-agent-skill) |
| Build | `swift-testing` | [swift-ios-skills](https://github.com/dpearson2699/swift-ios-skills) |
| Ship | `app-store-review`, `app-store-optimization` | [swift-ios-skills](https://github.com/dpearson2699/swift-ios-skills) |
| Ship | `aso` | [marketingskills](https://github.com/coreyhaines31/marketingskills) |
| Ship | `ios-marketing-capture` | [ios-marketing-capture](https://github.com/ParthJadhav/ios-marketing-capture) |
| Ship | `app-store-screenshots` | [app-store-screenshots](https://github.com/parthjadhav/app-store-screenshots) |

These are companion recommendations, not prerequisites for every task. Use their installed instructions when relevant. The bundled discovery, product, visual, and release references provide fallback workflows. Missing companions do not justify stopping a task that available tools can complete.

`authentication` applies only when the approved product needs it. An available keyword specialist may supplement the bundled evidence protocol, but do not assume a package contains a skill named `keyword-research`. Inspect a source's current catalog before adding optional skills. `competitors` in marketingskills serves SEO comparison pages; use `competitor-profiling` for product research.

### What the checker establishes

- Codex project checks examine `.agents/skills` from the working directory through the repository root. Global checks include `~/.agents/skills`, `$CODEX_HOME/skills` (default `~/.codex/skills`), and its `.system` directory.
- Claude Code checks examine project `.claude/skills` through the repository root and personal `~/.claude/skills`.
- Outside Git, project checks examine only the working directory.
- Symlinked skill folders are accepted. The checker does not inspect plugin caches, admin locations, disabled-skill settings, custom Claude configuration directories, or remote hosts.
- Build/Ship checks query Sosumi configuration only for selected, installed CLIs. An absent CLI is reported as `UNVERIFIED`; configuration does not establish connectivity, enabled state, or active-session availability.

Treat the session's actual catalog and callable tools as authoritative. A file check can miss a usable plugin or find a disabled skill.

### Installation behavior

`--check` is read-only. Exit 0 means the selected local checks passed, 1 reports missing companions/configuration, and 2 reports invalid arguments. CLI failures during installation propagate a nonzero status. Neither exit 0 nor file presence proves runtime readiness.

`--print-install <stage> --agent <agent>` prints only missing installation/configuration commands after read-only checks. `--install` executes those actions globally for selected agents, skips existing files/configurations, and stops on an installation failure. It does not update already installed skills.

Use installation only when the user has authorized its scope. Show the commands and explain which missing capability matters if authority is absent. Do not install another agent's companions as a side effect.

## Apple Documentation

Prefer Sosumi when its tools are callable. The remote endpoint is `https://sosumi.ai/mcp`. When needed and authorized:

```bash
codex mcp add sosumi --url https://sosumi.ai/mcp
codex mcp get sosumi --json

claude mcp add --transport http --scope user sosumi https://sosumi.ai/mcp
claude mcp get sosumi
```

Refresh or restart the session if new tools are not exposed. If Sosumi is unavailable, read current official Apple pages directly. Continue independent work when a particular document is inaccessible, and label decisions that remain unverified.

For each selected capability, fetch the relevant symbol/task, availability, configuration, HIG, privacy, and testing guidance. Record the URL, access date, and decision it supports. Recheck when the capability, SDK, or release requirement changes; do not collect unrelated API pages.

For Sign in with Apple, check AuthenticationServices, the native control, credential lifecycle, token validation, revocation, and account deletion. For release, recheck App Review, privacy disclosures, metadata/localization limits, screenshot/app-preview specifications, and any API upload lifecycle being implemented.

## Conditional Framework Skills

Consult the current [swift-ios-skills catalog](https://github.com/dpearson2699/swift-ios-skills) for the capability selected by the product. Typical areas include persistence/sync, navigation, concurrency, accessibility/localization, authentication/security, StoreKit, system integrations, and on-device intelligence.

Verify names before installation, then select only what is needed:

```bash
npx skills add dpearson2699/swift-ios-skills --list
npx skills add dpearson2699/swift-ios-skills -g -a codex -s authentication -y
```

Do not let a framework skill's defaults override the approved deployment target, architecture, or scope.

## Native Build Environment

Inspect the actual environment:

```bash
xcode-select -p
xcodebuild -version
xcodebuild -showsdks
xcrun simctl list devices available
```

Select a scheme, configuration, and available simulator destination from project/tool output. Document the chosen minimum deployment target and availability guards. A beta dependency needs user opt-in; do not silently switch Xcode or signing.

When Xcode exposes its MCP bridge, consult [Apple's setup instructions](https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode) and use it if configured. Explicit `xcodebuild`, `xcrun simctl`, and existing project commands remain valid alternatives.

On a host without Xcode, complete research, source edits, and portable checks within scope. Do not report native builds, simulator walkthroughs, signing, or archives as verified.

## Sources

Format, discovery paths, and installation syntax were checked on 2026-10-06 against the [Agent Skills specification](https://agentskills.io/specification), [Codex skills documentation](https://developers.openai.com/codex/skills/), [Claude Code skills documentation](https://code.claude.com/docs/en/skills), and [skills CLI](https://github.com/vercel-labs/skills). Companion catalogs can change; verify the requested package before a new installation.
