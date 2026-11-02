---
name: article-evidence-opinions
description: "Use when: benchmark evidence patterns are understood and you need to gather facts, validate upstream claims, and shape verified evidence into expert opinions with a mandatory handoff to /article-skeleton."
argument-hint: '[content-workspace/project-slug] [article-slug]'
user-invocable: true
allowed-tools:
  - Bash
  - Read
  - Edit
  - Write
  - WebSearch
  - WebFetch
  - Agent
  - mcp__you__*
  - mcp__tavily__*
  - mcp__exa__*
  - mcp__crawl4ai__*
  - mcp__firecrawl__*
  - mcp__plugin_playwright_playwright__*
  - mcp__apify__*
  - mcp__agent-reach__*
  - mcp__douyin__*
  - mcp__linkedin__*
  - mcp__mcp-server-chart__*
---

# /article-evidence-opinions

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Before any evidence work, verify:
- `project-profile.md` exists and `state.json` indicates `lockedProfile: true`
- `benchmark-success-formula.md` exists with user-approved Structural Blueprint and Reader Advancement Mechanism
- `topic-card.md` exists for this article
- If the Locked Profile Gate fails, stop and route to `/profile-discover`, `/profile-answer`, `/profile-research-deep`, or `/profile-lock`

### Handoff Read (MANDATORY — complete before Phase 0 Plan Preview)

| Upstream File | Extract | Used For |
|---|---|---|
| `benchmark-success-formula.md` Dimension 13 (Proof Strategy) | Per-benchmark proof mechanisms and evidence rhythm | Evidence deployment TARGET |
| `benchmark-success-formula.md` Dimension 14 (Human Texture) | Voice patterns, texture mechanisms, judgment density | Voice lens and opinion calibration |
| `benchmark-success-formula.md` Dimensions 2, 3, 4, 5, 12 | Reader state, tension, angle, question ladder, rhythm | Cognitive path facts must serve |
| `topic-card.md` | Core keyword, intent, promised angle, differentiator | Claims requiring validation |
| `intent-research.md` (Optional) | User question clusters and candidate H2s | Aligning opinions with what users actually ask |
| `project-profile.md` §2 + §5 + §10 | Product scope, methods, materials, certifications, red lines | Tier 1 sources and guardrails |
| `knowledge/fact-library.json` (Optional) | Verified claims and cases from prior articles with `used_in_articles` / `usage_count` tracking | Reusing verified Tier 1 facts while avoiding cross-article repetition (run `python3 scripts/sync_draft_born_claims.py content-workspace/<project-slug> --recommend` to surface least-used facts first) |

## Purpose

This skill is a dual-purpose Evidence & Validation Engine:

1. **Evidence gatherer & GEO Citation Triple Engine (Princeton/Georgia Tech KDD 2024 GEO Standard)**: study how benchmarks deploy proof and opinion, then map those patterns to Tier 1/2/3 sources — engineering every decision-critical H2 around the three empirically proven LLM-citation boosters:
   - **Condition-Bounded Statistics Addition (`+37% GEO visibility`)**: pair every claim with a concrete tolerance, duration, cost delta, or test-standard threshold (`±0.15 mm kerf`, `≥1,000 hrs ASTM B117`, `$4,000–$8,000 retrofit penalty`).
   - **Named-Expert & Primary-Standard Quotation Addition (`+40% GEO visibility`)**: prepare direct, attributable field-engineering quotes from the Named Technical Author / QC Reviewer (`project-profile.md`) and exact clause references from primary standards (`ASTM A240`, `ISO 9013`, `UL 1741 SB`).
   - **Physical Cause-and-Effect Failure Chains (`+30% GEO visibility`)**: document the shop-floor/chemical/structural mechanism behind why cheap shortcuts fail (`Cl⁻ pitting of Cr₂O₃ film`, `thermal HAZ bowing on unframed >2.4m panels`) plus **Anti-Sell Disqualification Proof** (honestly stating 2–3 conditions where our high-spec option is overkill).
2. **SERP Consensus Counter-Engine (Ryan Law / Animalz *Antithesis → Forensic Teardown → Synthesis*)**: take the `SERP Consensus Target` from `intent-research.md` and pair each competitor platitude with a forensic counter-proof and a conditional decision rule (`If [Condition A] → [Path X]; if [Condition B] → [Path Y]`).
3. **Outline validator**: scan upstream artifacts for claims, specs, numbers, comparisons, and regulatory assertions before `/article-skeleton`.
4. **Correction generator**: when upstream artifacts contain errors, produce `upstream-revision-suggestions.md` and pause for Peer Co-Research deliberation.

Every claim entering `/article-skeleton` must pass through this engine first. Unverified claims must be weakened, removed, or documented as user overrides.

---

## Phase 0 — Plan Preview (output first, do NOT execute)

Before evidence work, present a structured plan for approval:

1. **Upstream Consumption Report**: Dim 13 proof strategy per benchmark, Dim 14 voice texture per benchmark, Dim 2/3/4/5/12 cognitive path
2. **Knowledge Gap Preview**: estimated flag count and priority distribution from `topic-card.md` and `benchmark-success-formula.md`
3. **Benchmark Evidence Patterns**: how benchmarks deploy proof and opinion
4. **Evidence Mapping**: per-stage Tier 1/2/3 sources mapped to benchmark patterns
5. **External Verification Plan**: the four required searches with tools and fallbacks
6. **Subagent Plan**: parallel bounded units and main-context synthesis method
7. **Deliverable List**: files to be generated

Output the plan, then show:

```
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，按计划推进
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
```

Wait for approval before Phase 1.

---

## Phase 1 — Knowledge Gap Flag Extraction

Scan upstream artifacts for anything that will become a claim. For each item, create a flag with a unique ID, priority, and owning section/H2.

### Flag ID format

- `P1-001`, `P1-002` for Priority 1
- `P2-001`, `P2-002` for Priority 2
- `P3-001`, `P3-002` for Priority 3

### Priority rules

| Priority | Scope | Source requirement |
|---|---|---|
| P1 | Decision-critical, safety, compliance, major cost claims | 2+ independent sources |
| P2 | Technical specs, market data, performance claims | 2+ authoritative sources |
| P3 | Background, guidance, generic context | 1+ authoritative source |

### What to flag

- Material property claims
- Numerical specs (capacity, lead time, MOQ, dimensions)
- Comparative claims ("highest", "fastest", "best for")
- Certification and regulatory claims
- Cost or pricing claims
- Market or trend claims
- Any unsourced statement presented as fact

Assign each flag an initial status of `NEEDS CLARIFICATION` and record: Flag ID, Section/H2, Original Claim, Priority, Source Needed.

Output a draft `knowledge-gap-register.md` from `templates/knowledge-gap-register.md` after this phase.

---

## Phase 2 — Benchmark Evidence Study

Read `benchmark-success-formula.md` Dimensions 13 and 14 before touching project sources. For each benchmark, answer:

1. **What counts as proof?** Case study, named practitioner, real numbers, photography, certification, side-by-side test?
2. **Where does evidence appear vs. opinion appear?** What is the section-level rhythm?
3. **How dense are the judgments?** Count opinions per major section.
4. **What human texture mechanisms signal "a real person wrote this"?** Field language, specific failures, direct address, scene setting?

Record the resulting **Benchmark Evidence Model** in `evidence-opinion-pack.md` §1.

---

## Phase 3 — Fact Gathering & External Verification

### Phase 3a — Source Library Collection

For each stage of the Structural Blueprint and Reader Advancement Mechanism, extract facts from `project-profile.md` §2/§5/§10, source-library CSVs, and `knowledge/fact-library.json` (if it exists).

Classify every fact:

| Tier | Definition | Verification expectation |
|---|---|---|
| Tier 1 | Proprietary / owned evidence | source-library-verified |
| Tier 2 | Independent / industry evidence | externally verified |
| Tier 3 | Generic background | minimally sourced |

Mark each fact as:
- `source-library-verified` — origin in owned data or fact library
- `assumption-needs-flag` — inferred, must be transparently labeled
- `needs-external-verification` — must be validated by Phase 3b search

### Phase 3b — External Verification

Run the four required searches every time. Use subagents in parallel, one per bounded search category or per product/model. Main context synthesizes.

**Required searches:**

1. **Technical claim verification**: material properties, engineering specs, performance claims — engineering databases, spec guides, materials handbooks, manufacturer datasheets
2. **Buyer voice**: Reddit, Quora, architecture/design forums, LinkedIn, and relevant Chinese platforms for real questions, fears, misconceptions, wishes
3. **SERP refresh**: confirm current top-ranking content matches topic-cluster research; note ranking shifts and new content
4. **Certification / regulatory scope**: what cited certifications (ISO, ASTM, EN, UL, etc.) guarantee vs. exclude, in plain language

Use the `search-toolbox` skill for tool selection and fallbacks. Cross-reference at least two independent sources for any technical claim.

### Verification rules

- Verified facts: update to `VERIFIED`, record sources, source count, confidence
- Contradicted claims: classify `INCORRECT`, `FALSE CLAIM`, or `FALSE COMPARATIVE CLAIM`; specify correction action
- Unverifiable claims: classify `BLOCKED`; specify removal or weakening
- Partially verified: keep `NEEDS CLARIFICATION` with an owner

### Error taxonomy

Classify every flag using exactly one status:

- `VERIFIED` — claim matches source
- `INCORRECT` — claim contradicts source; must be corrected
- `FALSE CLAIM` — factually wrong or misleading
- `FALSE COMPARATIVE CLAIM` — comparison is wrong
- `MATH ERROR` — arithmetic is wrong
- `UNITS ERROR` — units are wrong or mismatched
- `NEEDS CLARIFICATION` — partially verified; requires confirmation
- `BLOCKED` — cannot be verified; must be removed or weakened

---

## Phase 4 — Calculation & Units Audit

Audit every number in upstream artifacts or derived for the draft:

- Recalculate percentages, ratios, and conversions
- Verify unit consistency (metric vs. imperial, weight vs. mass, pressure vs. force)
- Confirm decimal precision matches source precision
- Flag extrapolations and estimations as `assumption-needs-flag`
- Check comparative baselines ("20% faster than what?")

Record results in `knowledge-gap-register.md` `## Calculation & Units Audit`. Any `MATH ERROR` or `UNITS ERROR` must have a correction action before `/article-skeleton`.

---

## Phase 5 — Opinion Processing

Process verified Tier 1 and Tier 2 facts into expert opinions using the 4-lens voice system and four opinion emergence methods.

### Numeric controls

Choose concrete values before generating opinions:

| Control | Normal Range | Push Higher When | Push Lower When |
|---|---|---|---|
| Technical trap count | 2-10 | high-risk spec topic, many failure modes, strong proprietary evidence | topic simple, evidence thin, benchmark restrained |
| Expert stance count | 2-10 | benchmark strongly opinionated or buyer needs clear trade-off calls | topic informational, low-risk, weak evidence |
| Opinion intensity | 3-9 / 10 | must change buyer behavior or challenge a common shortcut | mainly explains options; stay calmer |

The numbers must be supported by real facts. Lower them instead of inventing stronger opinions.

### Opinion emergence methods

Use `voice-and-humanization`:

1. **Conditional judgment** — "X is the right call when..."
2. **Trade-off framing** — "You gain A but lose B"
3. **Counterexample** — "Most suppliers say X; what actually happens is Y"
4. **Field language** — workshop-floor terminology signaling real experience

### Voice lens allocation

Assign a primary lens per section type, grounded in benchmark voice patterns. Every opinion must pass the competitor test, judgment test, trade-off test, and supplier test.

---

## Phase 6 — Generate Deliverables

Create these files in `content-workspace/<project-slug>/articles/<article-slug>/`:

1. **`knowledge-gap-register.md`** (from `templates/knowledge-gap-register.md`)
   - Complete flag inventory with IDs, priorities, statuses, sources, source counts, confidence, correction actions
   - Layman Translation Library for every technical term/spec
   - Calculation & Units Audit
   - User Overrides / Editorial Decisions
   - Blocked Claims disposition
   - Quality Assurance Checklist

2. **`evidence-opinion-pack.md`** (from `templates/evidence-opinion-pack.md`)
   - Benchmark Evidence Model
   - Knowledge Gap Register status
   - Tier 1 / Tier 2 / Tier 3 fact inventory
   - External verification summary (technical, buyer voice, SERP, regulatory)
   - Opinion strategy and numeric controls
   - Voice lens allocation and opinion emergence methods
   - Industry controversies and expert stances
   - Differentiation opportunities
   - Internal link plan
   - External citation plan
   - Complexity warnings
   - Suggested analogies
   - Upstream revision status
   - Output handoff checklist

3. **`evidence-handoff-summary.md`** (from `templates/evidence-handoff-summary.md`) — MANDATORY
   - Top 10 critical facts for author attention
   - Complexity warnings
   - Suggested analogies
   - Voice & tone guidance
   - Section-specific writing guidance per H2
   - Visual placeholder recommendations
   - Mandatory red lines
   - Optional editorial decisions / user overrides
   - Pre-writing checklist for `/article-skeleton`

4. **`upstream-revision-suggestions.md`** (from `templates/upstream-revision-suggestions.md`) — CONDITIONAL
   - Generate only if upstream artifacts contain errors
   - Identify upstream artifact, exact location, original claim, suggested correction, priority, rationale, source
   - Implementation status table
   - Critical corrections must be resolved before `/article-skeleton`

---

## Layman Translation Requirement

For every technical term or spec entering the draft, provide a 5-step translation in `knowledge-gap-register.md`:

1. **Technical Term**: exact term
2. **Layman Definition**: one-sentence plain English
3. **Real Impact**: what it means for the reader's project or decision
4. **Comparison**: how it compares to alternatives
5. **Usage Recommendation**: when to choose or avoid

Do not skip this for abbreviations, material grades, finishes, standards, or engineering parameters.

---

## Upstream Revision Loop

If errors are found in upstream artifacts:

1. Generate `upstream-revision-suggestions.md`
2. Update `evidence-opinion-pack.md` §12 to indicate the file was generated
3. Update `knowledge-gap-register.md` with user override rows for rejected suggestions
4. Pause for approval using the PAUSE block
5. Do NOT proceed to `/article-skeleton` until critical and high-priority items are resolved

If no upstream errors exist, explicitly state "No upstream revision suggestions generated" in `evidence-opinion-pack.md` §12.

---

## Subagent-First Execution

Use subagents for parallel search and verification. Bound each subagent to one unit of work:

| Subagent | Bounded Unit | Output |
|---|---|---|
| Technical verifier | One product, material, or spec family | Verified/corrected claims with sources |
| Buyer voice researcher | One platform or forum type | Real questions, fears, misconceptions |
| SERP refresher | One target keyword cluster | Ranking shifts and content changes |
| Regulatory verifier | One standard or certification | Scope, guarantees, exclusions |

Main context synthesizes subagent outputs, resolves conflicts, assigns final confidence scores, and writes deliverables. Subagents do not write final artifacts directly.

---

## Skills to Load

- `evidence-policy` — Tier 1/2/3 classification and evidence labels
- `voice-and-humanization` — lens selection, opinion emergence, intensity
- `search-toolbox` — tool inventory and fallback order
- `agent-reach` — Reddit, LinkedIn, Chinese platforms, forums

---

## Examples

### Example 1: Compiling Evidence Opinion Pack

Input: `/article-evidence-opinions content-workspace/steel-screen`

Output:
- `knowledge-gap-register.md` with 24 flags (6 P1, 10 P2, 8 P3)
- `evidence-opinion-pack.md` with 18 Tier 1 facts, 12 Tier 2 facts, 5 traps, 4 stances
- `evidence-handoff-summary.md` as writer-facing handoff
- `upstream-revision-suggestions.md` because `topic-card.md` contained an unverified comparative claim

---

## PAUSE

```
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，按计划推进
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
```

Present the deliverables. Ask:
- Are opinions landing as insights?
- Any fact needing deeper verification?
- Any section where lens choice or opinion density feels wrong?
- If `upstream-revision-suggestions.md` exists, are the suggested corrections acceptable?

---

## Output

Create these files in `content-workspace/<project-slug>/articles/<article-slug>/`:

| File | Required | Purpose |
|---|---|---|
| `knowledge-gap-register.md` | Yes | Central validation ledger |
| `evidence-opinion-pack.md` | Yes | Full evidence and opinion package |
| `evidence-handoff-summary.md` | Yes | Writer-facing handoff summary |
| `upstream-revision-suggestions.md` | Conditional | Corrections for upstream artifacts |

Update `content-workspace/<project-slug>/articles/<article-slug>/state.json`:

```json
{
  "currentStage": "article-evidence-opinions",
  "nextCommand": "/article-skeleton"
}
```

Proceed to `/article-skeleton` only after approval and after all critical/high-priority upstream revisions are resolved.
