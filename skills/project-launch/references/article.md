# Technical Article

## Shape

1. **The question** in one sentence, and the answer ("It can.").
2. **Starting point**: what the system was, with numbers (lines of code, APIs, sizes).
3. **Choosing the approach**: a table of the alternatives, how each works, and why not. Include the respected tools you did not pick, and say when they are the better choice.
4. **Architecture**: one diagram (Mermaid when the blog renders it) and a short list of components.
5. **Hard problems**: short war stories, each with the cause, the fix and a before and after number.
6. **Testing**: how correctness was checked on the real system, not on toys.
7. **How it was built**: people, AI agents, process, and what went wrong.
8. **What's next**, and a closing line that returns to the question.

The title uses the words the audience searches and shares: the genre or product category, the hook ("multiplayer included"). Avoid internal jargon. The subtitle becomes the page description and the preview text, so it must hold up alone.

## Claims

- Take every number from a measurement, a log or a project document, and keep the source at hand for the fact check.
- Prefer accurate qualifiers to absolutes: "essentially unchanged" when a few hundred call sites changed, "measured on" with the hardware.
- Drop a claim that has no public source, or publish the source (a demo page with the measurement).
- After editing, have a second model compare the changed parts with the documents they come from, then verify its findings before you fix anything.

## Voice and readability

- Write in the first person, plainly, with the writer's opinions and asides. Apply the humanizer rules before publishing: no em or en dashes, no "not X but Y" contrasts, no one-line closers that restate the paragraph, no forced triads, no bold labels on list items, sentence-case headings that say what the section holds, no filler words such as delve, crucial, robust, showcase, testament.
- Measure readability instead of guessing: paragraphs of at most about 70 words, sentences of at most about 40, no run of more than four plain paragraphs. A small script over the Markdown (code blocks excluded) gives the numbers.
- Give every section something the eye can hold: a short real code block, a small table, a blockquote with a real line from the product or its tests, a diagram or a screenshot. Open with a concrete hook (a quote, a response payload, three lines of code), not with an introduction.
- Keep the article's subtitle self-contained and consistent with the body: it is the page description and the link preview, so a number that differs from the body is the first thing a reader sees.

## Images and provenance

- One provenance manifest per article (`images/<slug>.origin.json`): file, type, source, licence, processing and SHA-256, for covers and screenshots alike. Generated covers record tool and prompt; screenshots record URL, viewport, date and state.
- Without an image generator, compose the cover from the product's own rights-cleared media (a before/after of a real output, for example) and say so in the manifest. Never show as a result anything that is not a real output.
- Check the product's own rights register before using footage, and record the new use there.

## History

- One commit per article in the articles repository: the article, its images, its manifest and its README line. Fold later edits into that commit with fixup commits and an autosquash rebase, and push with `--force-with-lease`; this only applies to a repository the author alone works on.

## Third-party rights

Discuss these with the user before drafting, and again before publishing. This is not legal advice; say so.

- **Names**: leave unnamed what the user wants unnamed. Warn that screenshots, videos and descriptions can still identify it.
- **Possession**: some methods imply access to someone else's source, for example "compiled from source, without rewriting". Show the user which sentences state it outright, so the user can decide whether to keep them.
- **Services**: when the work talks to someone else's service, describe it as a private test instance on the user's machine, with test accounts only, not the official service, not connected to it and not open to the public.
- **Distribution**: say explicitly what is not distributed: source code, builds, assets, installers.
- **Affiliation**: no affiliation with the owner; all rights belong to their owners.
- Put these points in a short "About this project" box near the top and repeat the distribution point in the closing.
- **Security work on legacy code**: describe the fix (lengths validated before copying, sender checks that now run) and leave out how to exploit the original (buffer sizes, reachable paths, what an attacker could send).

## Format for a Markdown blog

- Frontmatter as the blog expects, typically `title`, `subtitle`, `date`, `cover`, `coverAlt`, `draft`. Check the blog's parser for required fields and how it drops a leading H1.
- The cover is an original image without logos or trademarks, with descriptive alt text. Generated images are fine when the user agrees.
- Use relative image paths inside the articles repository, and anchors that match the heading slugs the renderer generates.
- Read the rendered page, not only the Markdown: diagrams on a phone, tables, code blocks.
