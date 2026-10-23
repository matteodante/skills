---
name: project-launch
description: Take a finished technical project public, or refresh what is already out. Decide what to open and under which license, write and fact-check a technical article, publish it on the blog, update the profile README, portfolio and CV, record a demo video, and write short LinkedIn and X posts. Use when the user wants to publish, announce, write up or showcase a project.
---

# Project Launch

Make a project's public surfaces tell one consistent, verified story: the repository or demo, a technical article, the blog that hosts it, the profile, portfolio and CV that point to it, and short posts that bring readers in. Nothing goes public without the user's approval for that action.

## Choose the Work

| Stage | Outcome |
| --- | --- |
| **Release** | The code's public status is decided (open, closed but ready to open, or demo only), with a license, a clean repository, a reviewed change and builds on every target. |
| **Write-up** | An article in which every claim traces to a measurement or a project document, framed safely around third-party rights. |
| **Publish** | The article is live on the blog. Profile, portfolio, CV and assistant context link to it, link previews are refreshed, and everything is checked live. |
| **Announce** | Short posts for each platform and an optional demo video, each published only after the user approves it. |

Enter at the stage the user asks for. Reuse decisions already made in the conversation or the repositories (license, wording, platforms, what stays unnamed) instead of asking again. When a decision changes, for example the code goes private or a claim is withdrawn, carry it through every surface that repeats it.

## Readiness

1. Map the surfaces before writing. Find where articles live and how the blog renders them, including its cache time. Find the portfolio and CV sources, how private parts are encrypted and where the key is kept (never print a key), and the profile README. Check which social accounts are logged in in a browser you may drive. Read each repository's own instructions.
2. Settle third-party rights early. These are products, names, source code, assets or servers that belong to someone else. Agree with the user on what must never appear: names, possession of source code, distribution, official services. Say plainly that you are not giving legal advice, and that a recognizable screenshot can identify what the text leaves unnamed.
3. Before any step that runs for minutes (builds, reviews, recordings), tell the user what is running and how long it takes. Run it in the background and report when it ends.
4. Commit, push, deploy and post only within the user's authorization for that action. A request to prepare is not a request to publish.

## Release

Read [release](references/release.md) for license choices, the closed-but-ready option, repository hygiene, clean-room rules and the review loop.

- Recommend a license by what the user wants to protect. Add the license file and a per-file header, and state the license in the README.
- Run an independent adversarial review after each large change. Check every finding against the cited code, or against the reference implementation's observable behaviour, before you accept it. Record the finding, the check and the outcome, then fix what holds.
- Build and test every supported target. Treat a demo as part of the release: host it where it stays reachable even if the repository goes private.

## Write-up

Read [article](references/article.md) for the structure, the claim discipline and the wording around third-party rights.

- Lead with the question, answer it, then show the evidence: starting point, approach comparison, architecture, hard problems with before and after numbers, testing, how it was built, what's next.
- Take every number from a measurement or a document in the project. Prefer accurate qualifiers to absolutes ("essentially unchanged").
- Have a second model fact-check the changed parts against the project's documents before publishing. Verify its findings the same way as in Release.
- Humanize and measure before publishing: no AI tells, short paragraphs, one visual element per section, a subtitle consistent with the body (see the voice section of [article](references/article.md)).

## Publish

Read [publishing](references/publishing.md) for the blog, link previews, profile, portfolio, CV and assistant context.

- Push the article where the blog reads it, wait for the cache, and check the live page: title, description, Open Graph tags, the new text, and that removed phrases are gone.
- Update every surface that names the project, in every language the site has, and link them both ways: article, project or demo, portfolio, CV.
- Refresh LinkedIn's cache of the page with its Post Inspector after any change to the title, description or image.

## Announce

Read [social](references/social.md) for post shapes and the approval flow. For a recorded demo, read [demo video](references/demo-video.md).

- Write for the stated audience (recruiters and non-technical readers by default): a short hook, what it is in plain words, one twist, the link.
- Keep drafts in a local file, never in a public repository. Show the exact text and media before each post, and publish only after an approval that covers that post.
- Publish from the user's logged-in browser. Then open the post's URL, add the link reply if the platform calls for one, and report the URLs.

## Verification and Handoff

Report:
- what is live, with links, and the checks behind each claim: HTTP status, the live title and description, the preview inspector, CI;
- what stays local, what is waiting for approval, and which pushes are needed and in which order (a library before the project that pins it);
- the risks the user accepted, for example a recognizable demo or claims that imply access to someone else's code.

When a check was not possible, say so instead of implying success.
