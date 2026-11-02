# Workflow Architecture

## 1. Artifact Graph, Not Loose Stages

The workflow is still deep and stop-gated, but the control surface is an artifact graph:

```text
Discover -> Answer -> Cluster -> Research -> Lock ->
Benchmark -> Extract -> Evidence ->
Skeleton -> Arc -> Draft ->
Truth QA -> Info Gain QA -> Benchmark QA -> Reader QA ->
Repair -> Enrich -> Publish -> Review
```

Each command creates durable files that downstream commands must read. Agents should not recreate project context or invent missing background.

Use `/workflow-status` to recover context, inspect blockers, check article queue progress, or decide the next safe command.

## 2. Discovery First

The system starts from weak input. A user may only say:

```text
我做金属屏风外贸，想做 SEO。
```

`/profile-discover` performs light research and creates `project-profile.draft.md` with defaults, gaps, and high-value questions. `/profile-answer` updates the draft after user replies and collects keyword data when available. `/article-cluster` consumes the keyword data to generate Deep SEO Cards and a topic pool, then pauses for the user to select the first article. `/profile-research-deep` researches the selected topic in depth. `/profile-lock` creates the locked profile and state gate, including the selected first article.

Profile-lock gate: article production commands must verify `project-profile.md`, `project-profile.json`, and `state.json` indicate `lockedProfile: true` before running. If not, stop and route to `/profile-discover`, `/profile-answer`, `/article-cluster`, `/profile-research-deep`, or `/profile-lock`.

Draft profile sections:

- Business Snapshot
- Product Hypotheses
- Buyer Hypotheses
- Market Hypotheses
- Content Strategy Defaults
- Evidence Needs
- Questions for User

Locked profile sections:

- Confirmed Business Model
- Product / Service Scope
- Target Buyers
- Target Markets and Languages
- Brand Voice and Red Lines
- Source Library
- Competitor Set
- Content Pillars
- Internal Link Inventory
- Publishing Platform Rules
- Default Article SOP Settings

## 3. Video SOP as Production Assets

The video SOP has been translated into the current v3 artifact graph:

- Topic roadmap -> `topic-cluster.md`
- Selected benchmark set -> `benchmark-candidates.md`
- Benchmark structure and success logic -> `benchmark-success-formula.md`
- Borrowed/transformed benchmark assets -> `benchmark-asset-ledger.md`
- Evidence and expert judgment -> `evidence-opinion-pack.md`
- Section contracts and numeric controls -> `skeleton.md`
- Narrative progression -> `article-arc.md`
- Article draft and draft-born claim ledger -> `draft.md`
- QA gates -> `truth-qa.md`, `information-gain-qa.md`, `benchmark-drift-audit.md`, `reader-qa.md`
- Enrichment assets -> `enriched-draft.md`, `image-plan.md`, optional `html-visual-plan.md`, optional `visual-render-check.md`
- Publishing package -> `publish-package.md`, `schema.json`, and platform-ready metadata

## 4. Benchmark-Led Transmutation

Benchmark imitation remains the highest writing constraint. Borrowed viewpoints, case patterns, data, and brand stance are allowed, but must be transformed through `benchmark-asset-ledger.md`.

Do not fake ownership. A borrowed public case can become an industry scenario or common buyer pattern, but not a claimed client story.

Read the **full benchmark article**, not a sample, before drafting. Use the Numeric Control Vector in `skeleton.md` and `draft.md` to choose exact imitation / injection / differentiation numbers for the article, then diagnose drift qualitatively instead of pretending one fixed ratio fits every benchmark.

## 5. Benchmark-Led Answerability

Answerability supports benchmark imitation. It must not dominate the article.

- No forced FAQ when the benchmark is not FAQ-like.
- No forced per-section takeaway when the benchmark does not use that rhythm.
- Machine-facing material can live in publish pack, schema, or FAQ candidates.
- Human reading flow and benchmark fidelity outrank visible answer blocks.

## 6. Section Contracts, QA, and Repair

`section-contracts.md` turns each H2 into a controllable execution unit. Drafting must follow these contracts.

After drafting, run all four QA gates:

- `truth-qa.md` verifies claims, data, source use, and red lines.
- `information-gain-qa.md` verifies unique business insights, factory experience, and red-line originality.
- `benchmark-drift-audit.md` verifies the article still follows the benchmark success formula.
- `reader-qa.md` verifies natural reading flow and removes mechanical SEO tone.

If a QA gate fails, create `repair-plan.md` and run `/article-repair`. Only after all gates pass may `/article-enrich` and `/article-publish-pack` run. After publishing, run `/article-review` (30/60/90 days) to close the feedback loop.

Stop-language: if any required artifact is missing, the profile is not locked, or the previous stage is incomplete, stop immediately and tell the user exactly what is missing and which command to run next.
