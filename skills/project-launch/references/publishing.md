# Publishing and Surfaces

## Blog

- Push the article to the folder the blog reads. Find the blog's cache (ISR revalidate, CDN max-age). When the author edits articles after publishing, a short revalidation (minutes, not hours) lets fixes reach readers before the posts spread.
- Check the live page with an HTTP client, not a cached browser tab: the `<title>`, `meta name="description"`, the `og:` tags, a sentence from the new text, and that removed phrases return no match. Check the blog index too, because it may refresh on another schedule.
- When an article is renamed, keep the URL slug. Posts already shared point to it.

## Link previews

- LinkedIn caches previews. After any change to the title, description or image, open the Post Inspector for the URL. Its scrape refreshes the card for new and existing posts.
- X refreshes cards on its own schedule. Do not delete and repost to force it.

## Profile, portfolio and assistant context

- Profile README: one line each for the project (demo link while the repository is private) and the article, with the article's current title.
- Portfolio: project cards in every language the site has, links to the demo and article, the AI assistant's context and `llms.txt` if the site has them. Run the site's checks (lint, types, tests) before pushing. A push to the deploy branch usually deploys production, so treat it as publishing.
- Search all repositories for the old wording after any change of status or claim: repository URL, license, "open source", withdrawn numbers.

## CV

- Keep the public and the full (private) CV consistent. Private versions are often encrypted in the repository: get the key from the local environment file the project documents, never print it, and use the project's own encryption command.
- Rebuild the PDFs from source (LaTeX or similar). Before editing a source you rebuilt from a PDF, compare its output page by page with the published file.
- Check the live files: the public CV downloads, and the gated CV answers 401 without access.

## Links both ways

Article → project or demo → portfolio → CV → profile, and back. After publishing, open each link once from the live pages.
