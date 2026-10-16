# Matteo Dante Skills

A small collection of portable agent skills for Codex and Claude Code.

## Available Skills

| Skill | Purpose |
| --- | --- |
| [idea-to-ios-app](skills/idea-to-ios-app/SKILL.md) | Research an iPhone app idea, build an approved native product, or prepare an App Store release. |
| [deeper](skills/deeper/SKILL.md) | Do a task at an expert's depth: name what an expert would add, the raw sources, the methods and the outside verification, then do it that way. |
| [project-launch](skills/project-launch/SKILL.md) | Take a finished project public: release and license, a fact-checked article, blog, portfolio and CV, a demo video and short posts, each published only with approval. |

The iOS skill has three modes: **Define**, **Build**, and **Ship**. It keeps country-specific demand evidence separate from assumptions, reuses approved product decisions, and creates only the app, website, backend, and release components the requested scope needs.

Companion skills improve specialized work but are not mandatory for every stage. The package includes research, design, native development, media, and release protocols with documented fallbacks.

## Install and Use

Install for Codex with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add matteodante/skills -g -a codex -s idea-to-ios-app -y
```

To use the same source with both agents:

```bash
npx skills add matteodante/skills -g -a codex claude-code -s idea-to-ios-app -y
```

Install `deeper` the same way with `-s deeper`, then invoke it as `/deeper` in Claude Code or `$deeper` in Codex.

Install `project-launch` the same way with `-s project-launch`. Its stages are **Release**, **Write-up**, **Publish** and **Announce**; ask for the one you need, for example "Use project-launch to write up this project and update my blog and CV".

From a local checkout, substitute `.` for `matteodante/skills`. Inspect the skill and scripts before installing. Invoke it by name in your agent, for example:

- “Use idea-to-ios-app in Define mode to evaluate this app idea for the UK market. Save the research report.”
- “Use idea-to-ios-app to build the approved PRODUCT.md as a local SwiftUI app.”
- “Use idea-to-ios-app to prepare screenshots and TestFlight for this existing app.”

Native builds and simulator checks need macOS and Xcode. Current market and policy research needs web access. Paid generation, signing changes, deployment, uploads, and submission require authority for the specific action.

The [companion checker](skills/idea-to-ios-app/scripts/check-companion-skills.sh) takes an explicit agent, checks only that installation, and offers a read-only preview of missing setup commands:

```bash
sh skills/idea-to-ios-app/scripts/check-companion-skills.sh --check discovery --agent codex
sh skills/idea-to-ios-app/scripts/check-companion-skills.sh --print-install build --agent claude-code
```

Run the installed checker's absolute path from the target app repository to include its project-local skills. File checks do not establish active-session tool availability. See [tooling and fallbacks](skills/idea-to-ios-app/references/tooling-and-docs.md) for scopes, exit codes, installation behavior, and optional media capabilities.

## Repository

```text
skills/
  deeper/
    SKILL.md
  idea-to-ios-app/
    SKILL.md
    agents/openai.yaml
    references/
    scripts/
docs/
  SKILL_FORMAT.md
  IOS_SKILL_RESEARCH.md
  SKILL_EVALUATION.md
templates/skill/SKILL.md.template
scripts/
  validate-skills.sh
  validate_skills.py
tests/
requirements-dev.txt
.github/workflows/validate.yml
```

Keep skill-specific resources inside the skill so installed copies remain self-contained. Repository documentation and validation tools are for maintainers.

## Development

Use Python 3.10 or later. The validator's only external dependency is PyYAML; skill consumers do not need the repository's development dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
./scripts/validate-skills.sh
python -m unittest discover -s tests -v
```

The validator checks real YAML frontmatter, naming, required fields, unfinished scaffolds, optional Codex UI fields, and local Markdown file links. It reports errors with paths and exits nonzero. It does not check remote URLs, Markdown anchors, runtime tools, or the quality of the workflow.

Tests use temporary repositories and fake installers/agent CLIs. They do not install companions, contact providers, or alter your agent configuration. GitHub Actions runs validation and tests on Linux and macOS, plus ShellCheck on Linux. With ShellCheck installed, run it locally:

```bash
shellcheck scripts/validate-skills.sh skills/idea-to-ios-app/scripts/check-companion-skills.sh
```

## Add or Update a Skill

1. Create `skills/<skill-name>/SKILL.md` from the [template](templates/skill/SKILL.md.template).
2. Replace every placeholder with a precise trigger, useful workflow, and verifiable outcome.
3. Link substantial conditional guidance from `references/`; add scripts only for concrete repeatable work.
4. Follow [the format guide](docs/SKILL_FORMAT.md), update the catalog above, and run the checks.
5. Evaluate realistic requests using [the behavior checklist](docs/SKILL_EVALUATION.md). Syntax checks alone cannot establish instruction quality.

Keep credentials, private project details, customer data, and unlicensed third-party content out of the repository. Sources and refresh guidance for the iOS workflow are in [the research notes](docs/IOS_SKILL_RESEARCH.md).

## License

[MIT](LICENSE). Publish only material you own or are allowed to redistribute.
