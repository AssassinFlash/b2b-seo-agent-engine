---
name: article-skeleton
description: "Use when: the evidence-opinion pack, content-type library, and search-intent candidate pool are ready and you need to convert those upstream inputs into a 7:3 H2 heading strategy and differentiated skeleton with section contracts."
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

# /article-skeleton

## Purpose

Convert the pre-built **search-intent candidate pool** and **content-type library** into a differentiated article skeleton. This skill performs **no live research** — PAA, Autocomplete, Reddit, and competitor-H2 extraction belong to `/article-intent-research`.

The skeleton is the crossover point between:
- **What users ask** (`intent-research.md`)
- **How great content answers** (`content-type-library.md`, `benchmark-success-formula.md`)
- **What the business can prove** (`evidence-opinion-pack.md`)

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Before building the skeleton, verify:
- `project-profile.md` exists and `state.json` indicates `lockedProfile: true`.
- `topic-card.md` exists with an approved Outline Sketch.
- `intent-research.md` exists with a consolidated candidate pool.
- `content-type-library.md` exists with selected primary exemplars.
- `benchmark-candidates.md` and the selected `benchmarks/<source>-raw-observations.md` files exist.
- `benchmark-success-formula.md` exists with user-approved Structural Blueprint and Dimensions.
- `evidence-opinion-pack.md` exists with user-approved facts, opinions, and voice lenses.

### Handoff Read (MANDATORY — complete before Phase 0 Plan Preview)

| Upstream File | Extract | Used For |
|---|---|---|
| `project-profile.md` | Locked profile flag, target buyers, red lines, product scope, approved voice | Gating the skeleton and validating every H2 |
| `state.json` | `lockedProfile`, `currentStage`, approved upstream artifacts | Confirming workflow state safety |
| `topic-card.md` (Outline Sketch) | Seed H2s, primary keyword, search intent, angle | Seeding the raw candidate pool |
| `intent-research.md` | Consolidated candidate pool, intent mapping, extraction evidence | Selecting search-facing H2s |
| `content-type-library.md` | Library categories, structural patterns, selected exemplar models | Borrowing cross-format / cross-industry structures |
| `benchmark-candidates.md` | Selected primary exemplars and cognitive models | Choosing which benchmark patterns to imitate |
| `benchmarks/<source>-raw-observations.md` | Per-benchmark raw structural and heading observations | Direct structural borrowing and rhythm imitation |
| `benchmark-success-formula.md` §2.15 + §3 | Question ladder, decision framework, section rhythm, section function | Imitating benchmark success patterns |
| `evidence-opinion-pack.md` | Voice lenses, technical traps, expert stances, Tier 1 evidence | Assigning voice lens, evidence role, and forbidden-claim boundaries |
| `templates/h2-heading-strategy.md` | 7:3 H2 format template | Producing the H2 Heading Strategy artifact |
| `templates/section-contracts.md` | Section contract table template | Producing `skeleton.md` |

If any required file is missing or `lockedProfile` is not `true`, stop and route to the appropriate upstream skill.

## Skills to Load

- `structure-variation` — format mapping, rhythm audit.
- `evidence-policy` — dynamic evidence placement.
- `benchmark-transmutation` — imitate → inject → differentiate rules.
- `voice-and-humanization` — lens selection and AI-pattern removal.

## Instructions

**Main context**: build the section structure, design H2s with a 7:3 SEO/CTR ratio, assign formats and voice lenses, audit rhythm.

**Philosophy**: Follow the Imitate → Inject → Differentiate stack. Start from the Structural Blueprint of the selected benchmarks, inject the project's data, and differentiate through `structure-variation` and `voice-and-humanization`.

---

### Phase 0 — Plan Preview

Before proposing H2s or section contracts, present:

1. **Upstream Consumption Report**: confirm what was read from `intent-research.md`, `content-type-library.md`, `topic-card.md`, `benchmark-candidates.md`, `benchmark-success-formula.md`, and `evidence-opinion-pack.md`.
2. **Intent & Entity Coverage Check**: map each major search-intent cluster AND verify all `table-stakes` entities + `SERP Consensus Targets` from `intent-research.md` are accounted for.
3. **Above-the-Fold Viewport Contract (Navboost 防跳出首屏设计)**: specify the first 180 words (direct answer + contrarian reframe + path preview) AND the first above-the-fold interactive/visual micro-anchor (never a giant decorative stock banner that pushes answers below the fold).
4. **Buying Committee & Internal Champion Enablement**: map which sections serve the Technical Specifier (engineer/architect/installer) and which section/module serves as the "Internal Champion Weapon" (30-second TCO/risk ledger that the specifier can forward to Procurement/CFO/Owner to get budget approved).
5. **Self-Contained RAG Citation Chunks & Extractive Format-to-Query Lock (Koray Holistic SEO + Kevin Indig GEO)**:
   - **Zero Throat-Clearing (`Answer-First / BLUF`)**: Every question H2 must open with a 40–60 word self-contained passage (explicit entity + operating boundary + direct verdict + quantified metric, zero dangling pronouns referring back to the H2, and zero narrative warm-up filler).
   - **Extractive Format-to-Query Lock**: Match the structural primitive right below the BLUF opening to the query's cognitive job:
     - *Comparison / Cost / X-vs-Y H2* → BLUF passage + `≤4-column` comparative attribute table or `.b2b-mod-*` split card within the first 120 words.
     - *Process / How-To / Installation H2* → BLUF passage + numbered `<ol>` sequence with bold verb-first step leads and tolerance gates.
     - *Selection / Specification Boundary H2* → BLUF passage + `If [Site Condition] → Specify [Exact Grade/Thickness]` decision matrix.
   - **Macro-Context vs. Supplementary Micro-Context Separation (Koray Contextual Vector)**: Keep the first 70–75% of H2s strictly locked on the primary entity and core specification/procurement decision (Macro-Context); place supplementary/adjacent micro-contexts (maintenance chemistry, edge-case retrofits, secondary applications) in the final 25% bridge zone leading into `/article-resources` and `/article-faq`.
6. **Content-Type Pattern Check**: list which library categories influence which parts of the skeleton.
7. Proposed H2 count and sequence derived from the Reader Advancement Mechanism.
8. Format rhythm map — which format per H2, where repetition is intentional, and where variation prevents template feel.
9. Preliminary voice lens assignments referencing `evidence-opinion-pack.md` (and Named Author/Engineer persona attribution from `project-profile.md`).
10. Rhythm check — heavy/light alternation.

Use the unified stop language. Wait for approval of the structural approach before writing H2s.

---

#### H2 7:3 Golden Ratio

Every H2 is a **question** by default. Each question is composed of:

- **70% clean SEO base** — standard entities, search-intent match, PAA-friendly language.
- **30% micro-tension hook** — a small word or phrase that creates curiosity or stakes.

Micro-tension word bank (rotate, never repeat adjacent):

| Category | Words / Phrases |
|---|---|
| Challenge | Actually, Really, Honestly, Truly |
| Risk | Mistake, Costly, Trap, Lock You Out, Lock In, Dead End |
| Revelation | Hidden, Sneaky, Wrong, Nobody Tells You, The Real Reason |
| Priority | Number One, First, Before Anything Else, Must-Know |
| Comparison | Best, Worst, Smartest, Fastest, Cheapest |

Section function is internal; H2 text is search-facing. A section that "Warns about retrofit cost" can have the H2 *"Is It Really More Costly to Add a Battery to Solar Later?*"

Use the unified stop language. Wait for approval of the H2 ratio approach before proceeding.

---

### Phase 1 — Candidate Pool Review

`/article-skeleton` does not extract live data. Verify the upstream pool is sufficient:

- Confirm `intent-research.md` met its minimum live-channel thresholds or has an acceptable failure log.
- Confirm `content-type-library.md` contains the selected primary exemplars.

Mine H2 candidates from:

| Source | What to Extract |
|---|---|
| `intent-research.md` | Consolidated candidate pool and intent mapping |
| `topic-card.md` Outline Sketch | Proposed H2s, search intent, priority angles |
| `benchmark-candidates.md` | Selected exemplars and cognitive models |
| `benchmarks/<source>-extraction.md` | Actual H2s from selected benchmarks |
| `benchmark-success-formula.md` §2.15 + §3 | Question ladder, decision framework, native rhythm |
| `evidence-opinion-pack.md` | Opinion map and voice lenses |

Build a synthesis table:

| # | Candidate wording | Source | Intent cluster | Reader question type | Relevance | Final H2 # or discard |
|---|---|---|---|---|---|---|

If the pool is insufficient, **return to `/article-intent-research`** rather than inventing candidates.

---

### Phase 1.5 — H2 Heading Strategy Artifact

Produce `articles/<article-slug>/h2-heading-strategy.md` using `templates/h2-heading-strategy.md`.

Required contents:

1. **Upstream Research Reference** — source artifacts and evidence locations; do not duplicate raw extraction logs.
2. **Synthesis table** — the Phase 1 candidate review.
3. **External input absorption** — if user provided H2s, reverse-engineer SEO base and hook.
4. **Final H2 table** — each H2 as a question with 70% SEO base, 30% hook, source(s), voice lens, format, AIO answer type, arc node role.
5. **Hook rotation map**, **red-line check**, **AIO capture preview**, **rhythm audit**, **benchmark alignment check**.
6. **Phase 1 Completion Checklist**.

This file is the authoritative H2 source for Phase 2 and Phase 3.

---

### Phase 2 — Structure Extraction

Start from the approved `h2-heading-strategy.md` final H2s and the Success Formula. Read the Structural Blueprint plus Dimensions 5, 7, 12, and 15 from `benchmark-success-formula.md`. Read `content-type-library.md` for cross-industry / unrelated / non-text patterns.

Determine:

1. H2 sequence and function — what job does each H2 do?
2. Format rhythm — where should sections differ, and where should intentional repetition preserve momentum?
3. AIO capture opportunities — which sections naturally answer real search questions?
4. Rhythm pattern — where does the article breathe? Where does it intensify?

---

### Numeric Control Vector

Before writing section contracts, choose the article's numeric controls and justify them:

| Control | Normal Range | Default | Notes |
|---|---|---|---|
| Target H2 count | 5–12 | — | Higher when benchmark is broad or buyer decision has many branches |
| H2 hook ratio | 20–40% | 30% | Higher when CTR is the primary strategic goal |
| Minimum upstream candidate sources | 3 | `intent-research.md`, `topic-card.md`, `benchmark-candidates.md` | If reduced, document rationale |
| AIO capture target | 2–12 | — | Higher when the topic is question-led |
| Evidence pressure | 40–90 / 100 | — | Higher when buyer risk is high |
| Format repetition tolerance | 1–3 consecutive similar sections | — | Justify any intentional repetition |

---

### Phase 3 — Per-Section Specification

For each H2 from the approved `h2-heading-strategy.md`, define the section contract using `templates/section-contracts.md`.

Ensure every contract includes:

| Field | What It Specifies |
|---|---|
| H2 heading | The final 7:3 question |
| H2 70% SEO base | The clean, intent-matched question without the hook |
| H2 30% hook element | The tension word/phrase and hook category |
| H2 source | `intent-research` / `content-type-library` / `topic-card` / `benchmark` / `PAA` / `Reddit` / `Autocomplete` / `user-input` / `synthesized` |
| Content-type library influence | Which library category or entry shaped this section (optional) |
| Voice lens + translation | Which lens and how it shapes wording |
| Evidence role / anchors | Decision-critical / support / setup / transition; specific Tier 1 anchors when decision-critical |
| AIO extractability | Direct answer / comparison / checklist / definition / question |
| Format type | Prose / table / case spotlight / FAQ / process walkthrough / warning / comparison / checklist |
| Visual hint | For `/article-enrich` |
| Internal/external links | Required links |
| Continue-reading hook | Last 1-2 sentences of the section that hook the next H2. Required for every non-final H2. Must use one of: loss/risk frame, question the next section answers, or quantified tease. Generic academic transitions ("In the next section we will discuss...") are forbidden — they leak dwell-time. See `/article-draft` Phase 2 Hard Writing Requirement 2. |
| Arc node role | Which of the 6 narrative-arc nodes this section serves |

#### H2 source traceability rule

Every H2 in `skeleton.md` must echo the source declared in `h2-heading-strategy.md`. If a final H2 is "synthesized," explain which inputs were synthesized and why direct sources were insufficient.

#### Format Variation Rule

No two consecutive sections may repeat the same format by default habit. Audit the skeleton before finalizing. If repetition is benchmark-native, justify it explicitly.

---

### Phase 4 — Rhythm Audit

- **Format rhythm**: repeated format without benchmark-native reason? → break one.
- **Cognitive load balance**: dense section followed by lighter section?
- **Voice lens variation**: neighboring same lens? → justify or vary.
- **Question ladder integrity**: trace from H2-01 to CTA without a jump?
- **Hook rotation**: adjacent H2s using the same tension device? → rotate or rewrite.
- **Arc readiness**: clearly mark where the Trust Shift lands and where the Opening Reframe sits.

---

## Output

Create `articles/<article-slug>/skeleton.md` with all per-section specs + rhythm audit.

Update `state.json`: `currentStage: article-skeleton`, `nextCommand: /article-arc`. Optionally record `h2HeadingStrategy` path.

### Required Artifact

- `skeleton.md`

### Optional Artifact

- `h2-heading-strategy.md` — must be produced and approved before section contracts are written.

## Examples

### Example 1: Building a skeleton
输入: `/article-skeleton content-workspace/steel-screen`
输出: `skeleton.md created with 8 section contracts and a 7:3 H2 heading strategy.`

## Guardrails

- **No live extraction in /article-skeleton.** Route back to `/article-intent-research` if the candidate pool is insufficient.
- **No section without a reader function.** If a section has no clear reader job or benchmark-informed reason to exist, do not draft it.
- **Decision-critical sections need Tier 1 anchors.** If a decision-critical section lacks Tier 1 evidence, return to `/article-evidence-opinions`.
- **Every H2 source is traceable.** Sources must match `intent-research.md`, `content-type-library.md`, or another upstream artifact.

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

Wait for explicit approval before `/article-arc`.
