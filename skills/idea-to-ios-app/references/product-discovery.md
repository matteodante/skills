# Product Discovery And Approval

Use this reference before any design, repository scaffolding, architecture, or implementation.

## Contents

1. Normalize the input
2. Competitor research protocol
3. Design tree discussion
4. Proposed product contract
5. Approval

## 1. Normalize The Input

Accept an idea, problem statement, niche, brief, existing product, agent skill, or workflow. Extract a provisional model:

- target user and usage moment;
- painful job and current workaround;
- promised first-session outcome;
- repeated-use loop and expected frequency;
- known features, constraints, business model, and evidence;
- unclear assumptions and contradictions;
- reason this should be a native iOS app instead of a website, automation, or existing tool.

When the input is an agent skill, map domain inputs, decisions, outputs, scripts, records, safety boundaries, and validation evidence into product behavior. Remove agent orchestration and host-specific tooling from the user experience.

## 2. Competitor Research Protocol

Research current evidence because products, pricing, positioning, listings, and reviews change.

### Landscape

Find:

- at least three direct competitors when the category supports them;
- at least two adjacent competitors or substitutes;
- the dominant manual, spreadsheet, notes, messaging, search, or “do nothing” workaround.

If fewer credible products exist, document the search space and evidence instead of padding the list.

### Source Priority

Prefer:

1. current App Store listing and in-product experience;
2. official product, pricing, support, privacy, changelog, and documentation pages;
3. first-party launch material and public demos;
4. recent user reviews and credible community discussions for recurring experience themes;
5. third-party analysis only for context that primary sources cannot provide.

Record source URL and access date. Ratings, review counts, pricing, features, and policies require live verification. Never turn a single review into a market conclusion.

### Comparison Record

For each competitor capture:

- target audience, category, promise, and primary job;
- onboarding and whether login blocks first value;
- first-use path, main action, repeated loop, navigation, and major states;
- pricing/monetization and material limitations;
- data, privacy, integrations, and platform/ecosystem choices visible from public evidence;
- App Store name/subtitle, screenshot narrative, positioning, and review themes;
- strengths, weaknesses, best-fit user, and who should avoid it;
- relevant update cadence or abandoned-product risk;
- source-backed facts versus inference.

Compare reasons and outcomes, not only feature checkboxes. Explain where each product wins and why a user would stay with their current workaround.

### Synthesis

Produce:

- category map: direct, adjacent, substitute, workaround;
- evidence matrix by decision-relevant dimension;
- underserved jobs or segments;
- table-stakes features versus differentiators;
- acquisition and App Store discoverability implications;
- credible wedge and defensibility hypothesis;
- strongest reasons the proposed idea may fail;
- questions the research cannot answer without primary customer evidence.

Invoke `competitors` for its honesty, research depth, use-case comparison, and centralized evidence principles. Do not create SEO comparison pages during discovery.

## 3. Design Tree Discussion

Invoke `grilling`. Ask questions in dependency-aware rounds and wait after each round.

Suggested branches:

1. **User/problem**: exact user, triggering moment, severity, frequency, workaround, evidence.
2. **Market**: why existing options fail this user, honest difference, timing, acquisition path.
3. **Value loop**: first outcome, repeated action, stored value, retention mechanism, failure/recovery.
4. **Scope**: must-have workflow, supporting states, non-goals, native advantage, supported devices/locales.
5. **Business**: willingness to pay, pricing model, unit-cost drivers, trial/paywall timing, ASO hypothesis.
6. **Trust**: data ownership, permissions, account need, deletion/export, AI disclosure, safety/regulated risks.
7. **Delivery**: validation experiment, metrics, kill criteria, delivery mode, path, identity/signing constraints.

For every question:

- state the decision and why it matters;
- include a recommended answer based on evidence;
- expose the tradeoff and downstream decisions;
- ask only questions whose prerequisites are settled;
- update the unresolved list after the answer.

Challenge weak assumptions. Ask what result would disprove the idea, why the user cannot get the outcome from the strongest competitor, what brings them back, and how the first users will discover the app.

## 4. Proposed Product Contract

Present the contract in the conversation before writing project files:

```text
Product thesis
Target user and usage moment
Problem, evidence, workaround, why now
Competitive landscape and category gap
Differentiation, disadvantages, and positioning
First-session outcome and repeated-use loop
Prioritized v1 scope and non-goals
Screen/state map and navigation rationale
Visual direction, media plan, provider preference, acceptable external processing, and spend boundary
Domain data, ownership, sync, privacy, permissions
Guest/account decision and deletion/export lifecycle
Monetization and cost model
Backend boundary and external services
Acquisition/ASO hypothesis
Success metrics, validation experiment, kill criteria
Risks and mitigations
Delivery mode, repository path, identity/signing, devices/locales
Resolved decisions, assumptions, unresolved items
```

The contract must be specific enough that two capable implementers would build the same product shape. Replace adjectives such as “simple,” “premium,” or “AI-powered” with observable behavior and constraints.

## 5. Approval

End with a direct request:

> Questa è la definizione di prodotto che userò come vincolo. Vuoi modificarla oppure la approvi e mi autorizzi a impostare la repository e iniziare l'esecuzione?

Wait for an explicit approval. A partial answer, silence, or approval of one section does not authorize implementation. Apply revisions, show the updated contract, and request approval again.

After approval, write:

- `PRODUCT.md`: approved contract and version/date;
- `Docs/competitive-landscape.md`: evidence matrix, sources, access dates, and synthesis;
- `Docs/decisions/product-approval.md`: approval statement, date, approved scope, unresolved accepted risks;
- `Docs/decisions/*.md`: later architecture/product decisions that preserve traceability.

Any later request that changes target user, core outcome, monetization, account model, data boundary, or v1 scope returns to this approval gate before implementation continues.
