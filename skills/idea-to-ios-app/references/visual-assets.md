# Visual Assets And Image Generation

Read when the requested design includes imagery, generated assets, or media integration. Establish the visual direction first, using `impeccable` when available. Preserve the approved product contract when initializing another skill's context.

## Contents

1. Media decision
2. Capability and provider gate
3. Asset plan
4. Generation workflow
5. App guidance
6. Website guidance
7. Iconography
8. Integration and QA
9. Safety and truthfulness

## 1. Media Decision

Decide whether authored media improves comprehension, trust, emotion, differentiation, or product demonstration. Use image generation when the approved composition benefits from:

- editorial or lifestyle imagery that establishes the user's world;
- illustration, collage, 3D form, texture, or atmospheric background;
- mascots, characters, onboarding scenes, empty-state art, or educational visuals;
- product-specific decorative iconography or category objects at display size;
- app-icon concepts and marketing artwork;
- compositional mockups used to select a visual direction before implementation.

Skip generated media when the surface works better with real product UI, real photography, data visualization, typography, SF Symbols, existing brand assets, CSS/SwiftUI materials, or deterministic vector/code output.

Every asset needs a job. Do not add a stock-looking hero image, random gradient orb, decorative illustration, or icon tile because the layout feels empty.

## 2. Capability And Provider Gate

Inspect the active agent's available skills and tools immediately before visual work.

- When `imagegen` and a native image-generation tool are available, read and follow the installed `imagegen` instructions. Recommend its built-in generation path because it avoids separate provider credentials and setup, unless the user already chose another provider.
- Claude Code and Codex may expose different image tools. Keep the asset brief tool-neutral.
- If the active host has no native generator and bespoke raster media is needed, reuse an approved provider choice or ask one decision question: use a configured provider, choose Replicate, or proceed without generated media. Include the cost/privacy/setup tradeoff. If no generated asset is needed, continue without a provider question.
- If multiple providers are available and the choice changes cost, data handling, fidelity, licensing, or reproducibility, let the user choose. Reuse a provider decision already approved in `PRODUCT.md` unless its terms or suitability changed.
- Do not assume that a skill file proves the current session can call an image tool.
- Do not install a paid API, request credentials, or switch to a CLI/API fallback without the authorization required by the loaded image-generation workflow.
- If no supported generator is available, use code-native/system assets or verified licensed media. Report bespoke assets that remain blocked.

Image generation is a conditional creative capability rather than a hard prerequisite for compiling the app. It becomes blocking only when the approved design contract depends on bespoke raster media.

### Replicate path

Use Replicate only within the user's provider, data, and spend authorization. Reuse existing authority instead of requesting it for every call. At execution time:

1. Fetch current official [Node.js/client guidance](https://replicate.com/docs/get-started/nodejs), [prediction lifecycle](https://replicate.com/docs/topics/predictions/create-a-prediction), [output-file handling](https://replicate.com/docs/topics/predictions/output-files), [data retention](https://replicate.com/docs/topics/predictions/data-retention), [API-token guidance](https://replicate.com/docs/topics/security/api-tokens), security terms, and [pricing](https://replicate.com/pricing).
2. Recommend a current model from live Replicate documentation/catalog evidence for the asset type. Present model owner/name, version behavior, relevant price basis, strengths, limitations, and data implications. Do not preserve a default model name or version in this skill.
3. Ask the user to set `REPLICATE_API_TOKEN` in their local environment. Never ask them to paste the token in chat, write it into source files, or commit it.
4. Use the official client or HTTP API according to the project language and current docs. Prefer a small project-local script with explicit inputs, output directory, bounded polling/timeouts, errors, and sanitized logs over an undocumented one-off request.
5. Establish a prediction count or spend boundary before multi-candidate generation when none is already agreed. Stop at that boundary; a request for one asset does not authorize an unbounded variation loop.
6. Download selected outputs into the project before provider URLs expire or retention rules remove them. Record prediction ID, provider, model/version, prompt, parameters, date, output path, and cost/metrics when returned; never record the token.
7. Remove rejected remote predictions or inputs when the current API and the user's retention decision support deletion. Do not upload private, personal, licensed, or client-confidential media without explicit authorization.

## 3. Asset Plan

For a set of generated assets, record the plan in `Docs/decisions/visual-assets.md`. For a single asset, a short entry in existing design notes is enough. Keep fields relevant to the asset:

- stable ID and purpose;
- app screen, website section, App Store surface, or icon slot that consumes it;
- audience message and relationship to the product thesis;
- asset type: photo, illustration, texture, 3D, background, character, decorative icon, app icon, or concept comp;
- dimensions, aspect ratio, crop-safe area, focal point, and required variants;
- approved palette, materials, mood, and references from `DESIGN.md`;
- whether text is forbidden or must be exact;
- light/dark, phone/tablet, desktop/mobile, locale, and accessibility behavior;
- format, performance/memory budget, repository destination, and owner;
- source, prompt, generation/edit method, date, and review status;
- chosen provider, model/version, prediction/job ID, external-data decision, and cost/metrics when available.

Design the containing layout first. Generate for a known composition with real negative-space and crop requirements rather than forcing an arbitrary image into the layout later.

## 4. Generation Workflow

For each approved asset:

1. Write one provider-neutral production brief that names intended use, subject, scene, medium, composition, focal placement, palette, lighting, materials, constraints, and avoid list. Adapt parameters to the chosen provider without changing the approved art direction.
2. Use the exact consuming aspect ratio or a source ratio that supports all approved crops.
3. Keep UI labels and marketing copy outside raster images unless the asset requires inseparable lettering. Localizable interface text belongs in code.
4. Generate a small set of materially different candidates when composition remains open; do not keep requesting near-identical variants.
5. Inspect candidates at full size and inside the real surface. Check anatomy, hands/faces, object geometry, text, brand drift, artifacts, crop, contrast, and false implications.
6. Select one direction, iterate with one targeted change when needed, and reject the rest.
7. Move final project-bound assets from generator storage into the repository. Never reference a temporary or agent-global path from product code.
8. Record the final prompt, provider/model/version, selected file, provenance, edits, cost when available, and reason for selection.

Never replace an existing approved asset without explicit replacement scope. Use stable, descriptive, versioned filenames during iteration.

## 5. App Guidance

Use generated raster media in native app UI when it supports the user's task or product character:

- onboarding/education that explains a concept faster than copy;
- empty states whose artwork reinforces recovery or the next action;
- content covers, category art, backgrounds, textures, or display illustrations;
- custom branded moments that do not imitate controls;
- app-icon exploration, followed by manual selection, refinement, and current Apple asset validation.

Keep operating surfaces legible and native. Generated media must not impersonate controls, encode required information only in pixels, interfere with Dynamic Type, or reduce contrast. Provide accessibility labels when informative and hide purely decorative assets from assistive technologies.

Store production assets through the project's asset catalog or established resource pipeline with appropriate scale and appearance variants. Verify memory, decoding, scrolling, and launch cost on supported devices.

## 6. Website Guidance

Use generated imagery when the showcase needs a memorable visual thesis, real atmosphere, or narrative media unavailable from product captures. Strong candidates include a full-bleed hero scene, editorial illustration, product-world collage, section transitions, texture systems, and focused supporting art.

- Match the approved website purpose and `DESIGN.md`; compose imagery around the actual product story.
- Reserve copy-safe negative space from the prompt and validate real responsive crops.
- Prefer product captures for proof. Generated media can frame or dramatize the product but cannot replace evidence.
- Export responsive sizes and modern formats through the website's image pipeline. Preserve a high-quality source when future crops are likely.
- Write accurate alt text for informative media; use empty alt/decorative semantics when it carries no information.
- Avoid embedding essential claims, CTAs, prices, or legal text inside an image.

## 7. Iconography

Use SF Symbols for standard iOS actions and states. Use the website's established vector icon family for functional web controls.

Generate custom icons only when they are decorative, illustrative, product-specific, and large enough to benefit from raster craft. Define the whole family first: perspective, silhouette, material, lighting, palette, padding, background, and output size. Generate and review it as one coherent system.

Do not mix generated bitmap icons with SF Symbols in the same functional control language. Do not use image generation to approximate another company's icons or logo. Prefer SVG/vector authoring when icons must scale sharply, inherit color, animate, or match an existing line system.

## 8. Integration And QA

Validate final media in context:

- app phone/tablet layouts, light/dark appearance, Dynamic Type, Reduce Motion, and relevant accessibility modes;
- website desktop/mobile breakpoints, high-density screens, slow network, no-image fallback, and content reflow;
- crop/focal point, contrast with overlaid text, compression artifacts, color profile, file size, decoding/memory, and loading priority;
- localization and right-to-left behavior when composition depends on direction;
- consistency with `DESIGN.md`, nearby components, real product captures, and App Store artwork;
- licensing/provenance record and absence of watermarks or unintended marks.

Delete unused drafts from production bundles. Keep only approved source files and outputs required for reproducibility or future editing.

## 9. Safety And Truthfulness

- Do not generate a real person's likeness, customer story, testimonial, endorsement, award, rating, press logo, or usage evidence without authorization and a truthful source.
- Follow the active generator's content rules and use brand/reference material within the user's rights and authorized scope. Do not pass copied assets off as original work.
- Label synthetic examples when users could mistake them for collected customer data or real events.
- Do not use generated UI as an App Store screenshot. Capture the implemented app with deterministic fictional data.
- Do not let generated art imply a capability, integration, device, result, or regulated outcome the app does not provide.
- Re-check current App Store icon, screenshot, and marketing requirements before export or submission.
