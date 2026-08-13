# Product Discovery And Approval

Use this reference before any design, repository scaffolding, architecture, or implementation.

## Contents

1. Normalize the input
2. Competitor research protocol
3. Design tree discussion
4. Global search demand and keyword validation
5. Proposed product contract
6. Approval

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

## 4. Global Search Demand And Keyword Validation

Run this protocol after the user, job, first outcome, and differentiation are specific enough to produce realistic searches, and before proposing the product contract. Invoke `keyword-research` when installed; otherwise follow this protocol directly. In either case, treat the evidence rules below as authoritative when a keyword tool requests metrics that are unavailable.

### Market Scope

Do not equate “global” with the user's country or with the US alone.

- For an English-first global hypothesis, use the US as the anchor and compare at least the UK, Canada, and Australia.
- Add one or more category-relevant non-English storefronts when language, regulation, culture, purchasing power, or local incumbents could change the opportunity.
- For an explicitly local product, analyze the target storefront and at least one benchmark market; do not generalize local demand globally.
- Record storefront country code, query language, locale, currency, and access date. Explain why the selected markets represent the hypothesis.

### Keyword Universe

Generate a working set broad enough to challenge the positioning, normally 20–50 queries, across:

- category and solution terms;
- user problem and desired-outcome language;
- core action and object combinations;
- audience or profession modifiers;
- incumbent, substitute, and workaround language;
- high-intent long tails, synonyms, abbreviations, and locally natural translations.

Keep separate clusters for the proposed wedge, a broader category, and a narrower job. Use autocomplete and live results to replace invented phrases with language people actually use. Do not force a global English keyword into every locale.

### Evidence Hierarchy

Prefer current evidence in this order:

1. **Apple Ads**: read-only keyword suggestions, Search Popularity, recommendation data, or forecast data that the authorized interface exposes. Record the displayed scale and its current documented meaning. Treat popularity as a relative demand signal unless Apple explicitly exposes a volume estimate.
2. **Attributed keyword providers**: use monthly-volume or difficulty estimates only when the provider, country, date, and metric semantics are visible. Do not silently merge incompatible providers or scales.
3. **Apple's public Search API, App Store autocomplete, and live search results**: use them to discover phrasing, exact-title matches, result relevance, competitor density, and storefront differences. They do not expose search volume.
4. **App Store listings and review feeds**: use ratings/reviews, pricing, monetization, update cadence, and recurring review themes as traction and competition evidence, not query demand.
5. **Current trend or web-search sources**: use them for direction, seasonality, or broader problem awareness. Label them as non-App-Store signals.

Account access does not authorize mutations. Never create a campaign, accept suggested keywords, alter bids or budgets, add billing, or spend money without separate user approval.

### Evidence Matrix

For every serious keyword candidate capture:

| Field | Requirement |
| --- | --- |
| Keyword and cluster | Exact query and its problem/category/audience/long-tail role |
| Market | Storefront, language, and locale |
| Relevance and intent | Evidence-backed fit with the approved job; manual judgments must be labeled |
| Demand | Exact volume, estimate, relative popularity, or `unverified`, with provider and scale |
| Competition | Relevant top results, exact-title matches, dominant brands, and top-result rating/review distribution |
| Commercial signal | Visible pricing, subscriptions/IAP, and paid alternatives |
| Freshness | Access date and material recent entrants or updates |
| Confidence | High, medium, or low with the missing evidence stated |
| Implication | Proceed, test, reposition, stop, or deprioritize |

Do not:

- call result counts, ratings, review counts, rankings, or autocomplete order “monthly searches”;
- turn Apple Ads popularity into an exact volume unless the active interface and documentation define it that way;
- map a 1–5 or qualitative signal to 1–100 and then present a precise opportunity score;
- calculate a composite score when volume or difficulty is missing, incomparable, or inferred;
- select the least competitive niche without checking whether the low competition may reflect weak demand;
- select the highest-volume term without checking whether a new app has a plausible ranking and conversion wedge.

When comparable sourced inputs exist, a transparent score may help sort candidates, but always show the underlying metrics and assumptions. The decision must survive without the score.

### Decision And Validation

Conclude with exactly one current verdict:

- **Proceed**: demand is supported across the intended market and the product has a credible acquisition and conversion wedge.
- **Test**: the wedge is plausible but the demand signal is missing, mixed, seasonal, or too provider-dependent.
- **Reposition**: demand exists, but users search for a different job, audience, or promise than the proposed product.
- **Stop**: evidence is weak and there is no credible non-search acquisition path, or competition makes the proposed wedge implausible.

Show the ranked keyword clusters, cross-market differences, strongest counterevidence, confidence, and what would change the verdict. If reliable demand data is unavailable, write `unverified` rather than estimating it from competitors. Propose the smallest next validation, such as a read-only Apple Ads planner check or a separately authorized exact-match discovery campaign, including budget cap, duration, success metric, and kill criterion.

The final product contract must preserve this evidence and cannot describe the product as globally validated when only one storefront was checked.

## 5. Proposed Product Contract

Present the contract in the conversation before writing project files:

```text
Product thesis
Target user and usage moment
Problem, evidence, workaround, why now
Competitive landscape and category gap
Differentiation, disadvantages, and positioning
Target markets, keyword clusters, demand signals, competitive density, evidence confidence, and verdict
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

## 6. Approval

End with a direct request:

> Questa è la definizione di prodotto che userò come vincolo. Vuoi modificarla oppure la approvi e mi autorizzi a impostare la repository e iniziare l'esecuzione?

Wait for an explicit approval. A partial answer, silence, or approval of one section does not authorize implementation. Apply revisions, show the updated contract, and request approval again.

After approval, write:

- `PRODUCT.md`: approved contract and version/date;
- `Docs/competitive-landscape.md`: evidence matrix, sources, access dates, and synthesis;
- `Docs/market-demand.md`: markets, keyword clusters, source semantics, evidence matrix, verdict, and validation plan;
- `Docs/decisions/product-approval.md`: approval statement, date, approved scope, unresolved accepted risks;
- `Docs/decisions/*.md`: later architecture/product decisions that preserve traceability.

Any later request that changes target user, core outcome, monetization, account model, data boundary, or v1 scope returns to this approval gate before implementation continues.
