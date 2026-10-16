# Release

## Decide what opens

| Option | When it fits | What goes public |
| --- | --- | --- |
| Open source now | Demand is known, the code is clean of third-party material, and the user wants contributors. | Repository, license, issues. |
| Closed but ready to open | Demand is unknown, or the surrounding context is sensitive. The user wants to keep options open. | A live demo, the write-up, and a contact link. The repository stays private with license headers and docs already in place, so opening it is one setting. |
| Demo only | The code cannot be released (third-party code, unclear rights). | A demo built from material the user owns, plus the write-up. |

When the status changes, search every surface for the repository URL and the license name, and update them: README, article, portfolio cards in every language, CV, assistant context, llms.txt. A link to a repository that turned private returns 404 to everyone else.

## Choose a license

- **MIT or Apache-2.0**: permissive. Anyone may use, modify and close their changes. Apache-2.0 adds a patent grant.
- **MPL-2.0**: file-level copyleft. Changes to the library's own files must stay open, while programs that only link it may stay closed. It is the usual answer to "I want to protect it a bit without scaring users away".
- **GPL-3.0 or AGPL-3.0**: strong copyleft. Linked programs, or network services under the AGPL, must be released too. This limits commercial adoption.

Add the license file, an SPDX header to every source file (`SPDX-License-Identifier: MPL-2.0` plus the notice the license asks for), and a License section in the README. List bundled third-party code in a notices file.

## Clean room

Code derived from a source without a license cannot be released. Rewrite it from public documentation and standard mathematics or algorithms, and say so in the file header. To match a reference implementation, compare observable behaviour only: call the reference with the same inputs, then record its answers as test expectations. Never copy or decompile its code. Run reference binaries only when they are installed system components or official redistributables, never binaries from archives of unclear origin.

## Repository hygiene

- README: what it is, a demo link, the build for each target, status and limits.
- CHANGELOG with an Unreleased section; CONTRIBUTING and SECURITY when outside contributions are possible.
- No local absolute paths, secrets, internal code names or names the user wants withheld. Search before every push.

## Review loop

1. Give a second model the change range and a review-only brief: what changed, what must not change, what to look for. Run it on a throwaway clone. On Windows, use a short path and `git -c core.longpaths=true clone`.
2. For each finding, read the cited lines, or reproduce the case, or compare with the reference implementation. Mark it as holding, partly holding or rejected.
3. Fix what holds, re-run the tests on every target, and record a table with the finding, the check and the outcome, in the place the project keeps reviews.
4. The reviewer's claim is not evidence. Its reproduction is.

## Builds and tests

Build and test each supported target: native, browser/WebAssembly, other operating systems. The release is not done while one of them is unverified. When the project is consumed as a submodule or package, push the library before the project that pins its commit, then check that a fresh clone can initialize it.
