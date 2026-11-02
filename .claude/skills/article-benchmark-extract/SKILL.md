---
name: article-benchmark-extract
description: "Use when: primary exemplars have been selected from the content-type library and you need to extract the success formula, reader-advancement mechanisms, and create the benchmark-asset ledger."
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

# /article-benchmark-extract

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Before extraction, verify:
- `project-profile.md` exists, `state.json` indicates `lockedProfile: true`
- `benchmark-candidates.md` exists with 3 selected primary exemplars noted
- `content-type-library.md` exists (optional but recommended for pattern context)
- `intent-research.md` exists (optional, to align extraction with user questions)

### Handoff Read (MANDATORY — complete before Phase 0 Plan Preview)

| Upstream File | Extract | Used For |
|---|---|---|
| `benchmark-candidates.md` | Article Type Classification section | Confirming the article type before extraction — determines which of the 21 Success Formula dimensions are most critical |
| `benchmark-candidates.md` | All user-selected candidates with URLs and Deep Structure Analysis (per-article structure breakdown) | Primary source for dimension-by-dimension extraction. Must have full scraped content of each selected article ready before extraction begins |
| `benchmark-candidates.md` | The per-article project-adaptation notes (e.g., "对本项目的借鉴" / transmutation notes) | Cross-article pattern synthesis — these notes are the raw material for the Unified Success Formula |
| `content-type-library.md` (optional) | Broader pattern landscape and non-selected library entries | Distinguishing selected-exemplar patterns from category-wide conventions; identifying gap/opportunity patterns |
| `intent-research.md` (optional) | User question clusters and intent mapping | Ensuring the extracted Reader Advancement Mechanism aligns with what users actually ask |
| `project-profile.md` §7 | Benchmark Policy | Knowing which borrowable asset types are allowed and which are blocked |
| `project-profile.md` §5 | Brand Voice and Red Lines | Ensuring extracted patterns don't conflict with profile constraints |

## Purpose

Deep-read the user-selected primary exemplars (see `config/workflow-spec.yaml` `benchmark_selected_count`). Extract both:

1. **Structural Blueprint** — the borrowable section-job sequence, pacing shifts, answerability moments, evidence deployment pattern, and intentional repetition that make the benchmark work.
2. **Reader Advancement Mechanism** — the cognitive path each article takes the reader through, from arrival anxiety to confident action.

The deliverable is not a final outline. Do not propose final project H2s or lock the current article's exact section sequence. But do give `/article-skeleton` enough structural material to imitate the benchmark intelligently instead of rebuilding from default SEO habits.

---

## Phase 0 — Plan Preview (output first, do NOT execute)

Before any extraction, present a plan:

1. **Library Context** (MANDATORY first item when `content-type-library.md` exists): confirm what was read from the library and how the selected exemplars cover the intent clusters from `intent-research.md`.
2. **Selected Exemplar Justification**: explain why these 3 were chosen from the library and what problem-solving models they represent.
3. **Upstream Consumption Report**: confirm exactly what was read from `benchmark-candidates.md`:
   - Article type classification from candidates file → confirms extraction focus
   - All user-selected candidates with Deep Structure Analysis → these are the subjects of extraction
   - Per-candidate project-adaptation / transmutation notes → raw material for cross-article synthesis
4. **Articles to Analyze**: confirm the user-selected articles with titles and URLs
5. **Active Dimensions**: which of the 21 Success Formula dimensions (15 mandatory + 5 optional + Prose Craft) are most critical for this article type
6. **Extraction Method**: how each article will be read and synthesized
7. **Success Criteria**: what "good mechanism extracted" looks like

Output the plan. ```
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，按计划推进
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
```

Wait for explicit approval.

---

## Instructions

**[Imitate]** This skill operates on layer 1 of the Imitate → Inject → Differentiate stack.

**Main context work**:
- **Pre-extraction HTML Denoising (MANDATORY)**: Before reading any benchmark article, if you downloaded raw HTML, you MUST run the denoise script to strip away navigation menus, sidebars, related posts, and footers.
  ```bash
  python3 scripts/denoise_html.py <input.html> <output.md>
  ```
  Only read and extract Linguistic DNA from the resulting clean `output.md`. Never extract from boilerplate UI text (Garbage in, garbage out).
- Read the user-selected, denoised benchmark articles in full
- Synthesize findings across articles into the Unified Success Formula
- Present findings to user for iterative discussion

**Subagent-appropriate work**:
- Deep-reading individual benchmark articles. Each article can be read by a separate subagent using the extraction dimensions defined below. This keeps each article's analysis in its own context window.
- Subagents write per-article extraction notes; main context synthesizes. Let subagents use the `search-toolbox` skill (**Mandatory Apify-first** via `python3 scripts/apify_research.py` or `mcp__apify__*`, combined with `scripts/denoise_html.py` and Crawl4AI/Firecrawl/Playwright) to fetch full, clean benchmark text.

**Mandatory intermediate artifact — Raw Observations**

Before synthesizing the Unified Success Formula, each selected primary exemplar MUST first produce a durable raw-observations file:

- File location: `articles/<article-slug>/benchmarks/<source>-raw-observations.md`
- Format: bullet-form observations only. Write what the benchmark actually does, sentence by sentence or section by section.
- Constraint: do NOT perform cross-article abstraction, synthesis, or comparison inside this file. Each raw-observations file must be readable as a standalone deconstruction of one article.
- Content: concrete observations about structure, pacing, proof, voice, callouts, visuals, and memorable phrases. Avoid generic labels.

Example acceptable bullet: "The opener poses a forced-choice question ('Should I install a battery now or later?') and immediately admits this is an increasingly common reader dilemma."
Example unacceptable bullet: "This article uses a question-based opener." (too abstract)

Only after all selected-exemplar raw-observations files exist should the main context synthesize `benchmark-success-formula.md`.

**Optional library pattern notes**

If a non-selected library entry contributes a borrowable idea (e.g., a comparison framework from a cross-industry source), record it in a "Pattern Notes" section of `content-type-library.md` or in `articles/<article-slug>/benchmarks/library-pattern-notes.md`. Do not run the full 21-dimension extraction on library entries.

**Skills to load in main context**: `benchmark-transmutation` — for borrowable asset types, transformation rules, risk labels, and ledger template. Also reference `structure-variation` as a constraint: it prevents lazy template repetition while allowing intentional benchmark-native rhythm. When extracting patterns from benchmark articles, separate "this repetition makes the article work" from "this is just the source's house style." Use `search-toolbox` to select extraction tools and fallbacks.

---

### Extraction Dimensions

### Mandatory (15 — extract for every benchmark article)

| # | Dimension | What to Extract |
|---|---|---|
| 1 | Core Promise | What does this article actually promise the reader? |
| 2 | Reader State | What does the reader know, fear, and want when they arrive? |
| 3 | Opening Tension | What creates the "must keep reading" force? |
| 4 | Angle | Whose perspective? What decision point? |
| 5 | Question Ladder | What sequence of reader questions does the article answer? |
| 6 | Information Progression | How does information escalate? |
| 7 | Decision Framework | Does the article give the reader a judgment tool? |
| 8 | Contrast | How does the article use comparison and trade-offs? |
| 9 | Specificity | Where are concrete scenes, parameters, conditions? |
| 10 | Information Density | Does every paragraph advance something? |
| 11 | Cognitive Load | How does the article manage complexity? |
| 12 | Rhythm | How does cadence vary? Where does it breathe? |
| 13 | Proof Strategy | How does the article prove credibility — without self-praise? |
| 14 | Human Texture | Does it sound like someone who has seen real projects go wrong? |
| 15 | Section Function | What job does each section do? |

### Optional (5 — activate per article type)

| # | Dimension | When |
|---|---|---|
| 16 | Actionability | How-To, Buyer's Guide, Process Walkthrough |
| 17 | Conversion Bridge | Articles with a CTA |
| 18 | Friction Removal | Buyer's Guide, Cost Guide, Procurement |
| 19 | Editorial POV | Opinion, Thought Leadership |
| 20 | Memorability | All types |

### Prose Craft (1 — always analyzed)

| # | Dimension | When |
|---|---|---|
| 21 | Prose Craft | All types — activated when `/article-draft` will imitate a specific benchmark's voice at the sentence and paragraph level |

### What Dim 21 Extracts: High-Fidelity Linguistic DNA Card

For each benchmark article, extract its sentence-level writing DNA. Formulate this as a **Linguistic DNA Card** to be used as a writing reference. Capture:

| Sub-dimension | What to Extract | Purpose & Example |
|---|---|---|
| **Alternative Transitions** | Transitions used by the author (avoid academic words like "Furthermore", "Moreover", "In conclusion"). | Replace AI-filler transitions with benchmark habits: "But here is the catch", "The math is simple", "Now let's look at the numbers". |
| **Paragraph Openers** | Common sentence starters that set the immediate scene. | Emulate style: "If you are...", "Let's be honest:", "Here is what most suppliers won't tell you". |
| **Metaphors & Domain Context** | The vocabulary field and analogy types preferred by the author. | Emulate sports analogies, cooking, or workshop fabrication terminology. |
| **Reasoning Trajectory** | Pacing and argument flow (how the author connects evidence to conclusion). | Understand how they transition from problem state, build tension, introduce data, and deliver opinions. |

This feeds directly into `/article-draft` Phase 1 Step 1.5 as the **Linguistic DNA Card / Vocabulary Palette** saved under a dedicated `# Linguistic DNA Card` section in `benchmark-success-formula.md`.

---

### Hook Distribution Map + Copyable Execution Rules

Extract the self-media layer from the benchmarks: not just what structure they use, but **where they keep the reader moving**.

Add two sections to `benchmark-success-formula.md`:

1. **Hook Distribution Map**
   - Opener hook: what makes the reader stay after the first 3-5 seconds?
   - Section-end hooks: how each major section pulls into the next.
   - Skimmer hooks: bold, bullets, tables, visual anchors, or line breaks that stop the eye.
   - CTA / next-action hook: what makes the final action feel natural?
   - For each hook, record the reader emotion (curiosity, fear of loss, relief, confidence, urgency) and whether it is borrowable for the current article.

2. **Copyable Execution Rules**
   - 10-15 concrete rules that can be applied during `/article-draft` (not vague lessons).
   - Each rule should state: what the benchmark does, why it works, and how to adapt it without copying.
   - Prioritize opener mechanics, continue-reading hooks, full-sentence bold / citation anchors, tables, and CTA transitions.

This section is adapted from self-media burst-content analysis: opener design, hook distribution, interaction points, and "replicable feature lists." Translate the mechanism into B2B SEO; do not copy short-video tone.

---

## Output Format

Present as: Cross-Article Patterns → Dimension-by-Dimension Extraction → Structural Blueprint → **Hook Distribution Map** → **Copyable Execution Rules** → Reader Advancement Mechanism → What We Are NOT Borrowing.

**Structural Blueprint must include**:
- Borrowable section jobs in order, without converting them into final project headings.
- Pacing: where the benchmark slows down, speeds up, repeats, compares, or lands a judgment.
- Evidence rhythm: where proof appears, where the author uses experience, and where proof is intentionally withheld for setup or tension.
- AIO / answerability moments: where the benchmark makes an answer extractable without turning the article into a FAQ.
- Repetition diagnosis: mark each repeated pattern as `intentional-rhythm`, `house-style`, or `avoid`.

**Borrowable patterns must be recorded in Observation → Tactic → Implementation format**

Whenever the Structural Blueprint or Dimension-by-Dimension Extraction identifies a reusable pattern, write it as:

1. **Observation**: What the benchmark article actually does, with a concrete example or quote.
2. **Tactic**: What our article must do to imitate the pattern at the structural or prose level.
3. **Implementation**: How `/article-skeleton` should apply it — e.g., as an H2 job, a paragraph contract, a callout placement, a table requirement, or a CTA design.

This format prevents the success formula from becoming purely analytical and ensures `/article-skeleton` can act on it without re-inventing execution mechanics.

**Critical guardrails**:

- **Selected exemplars only**: The full 21-dimension extraction applies only to the 3 selected primary exemplars. Library entries are pattern references, not extraction subjects.
- **Library assets in the ledger**: If a borrowed structural idea comes from the library, the asset ledger must state the source category and transformation rule.
- The Reader Advancement Mechanism describes cognitive progression (what the reader needs at each stage, how they advance from anxiety to action). The Structural Blueprint may describe borrowable section jobs and rhythm, but it must NOT:
- Propose final project H2 headings.
- Lock the current article's exact section count.
- Assign final formats to every section.
- Treat a benchmark's repeated format as automatically borrowable.
- Set word count targets — content determines length.

If you find yourself writing the current project's finished outline, stop and move that work to `/article-skeleton`. If you remove all structural information, you have under-extracted the benchmark.

---

## Examples

### Example 1: Extracting Success Formula
输入: `/article-benchmark-extract content-workspace/steel-screen`
输出: `benchmark-success-formula.md and benchmark-asset-ledger.md generated detailing 21 dimensions of writing patterns.`

## Guardrails

- **Rigorous Auditing**: Identify exact structural variations and paragraph lengths rather than generalizing.
- **Asset Ledger Integrity**: Record every borrowed visual asset format in the asset ledger without modification.

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

Ask: does this structural blueprint and reader advancement mechanism feel right? Any dimension needing adjustment? Any element off-brand? Confirm that the blueprint gives enough structure to imitate without locking the final outline.

**Do not proceed until the user confirms the Reader Advancement Mechanism.**

---

## Output

Create:
- `articles/<article-slug>/benchmark-success-formula.md` — the extracted reader advancement mechanism and prose execution patterns.
- `articles/<article-slug>/benchmark-asset-ledger.md` — every borrowed structural pattern, viewpoint, case pattern, data point, or brand stance recorded with source, transformation rule, risk label, and final expression rule.

Use `templates/benchmark-success-formula.md` as the structure for the success-formula artifact.

Update `state.json`: `currentStage: article-benchmark-extract`, `nextCommand: /article-evidence-opinions`, `benchmarkStatus: success-formula-extracted`.
