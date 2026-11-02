---
description: "Use when: the arc, skeleton, evidence pack, and benchmark assets are ready and you need to write the article in one continuous pass using benchmark-led imitation plus Humanizer review."
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
name: article-draft
---

# /article-draft

## Purpose

Use when the arc, skeleton, evidence pack, and benchmark assets are ready and you need to write the article in one continuous pass using benchmark-led imitation plus Humanizer review.

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Before drafting, verify: `project-profile.md`, `state.json` indicates `lockedProfile: true`, `skeleton.md`, `narrative-arc.md`, `evidence-opinion-pack.md`, `benchmark-success-formula.md`.

### Handoff Read (MANDATORY — complete before Phase 0 Plan Preview)

| Upstream File | Extract | Used For |
|---|---|---|
| `skeleton.md` | Full per-section specification: H2 heading, format type, voice lens suggestion, evidence anchors, forbidden moves, transition signals | The section-by-section writing contract. Formats and evidence anchors are binding; voice lens suggestions are reference, not rigid rules |
| `narrative-arc.md` | Full 6-node arc design: starting state, opening reframe, first turn, middle build, trust shift, exit point | The emotional spine of the article. Every paragraph must serve its position on this arc |
| `evidence-opinion-pack.md` Part 3 & Industry Controversies | Per-scene processed opinions (exact text) plus dynamic B2B controversies and expert polarized stances | Hard, opinionated viewpoints to inject into related paragraphs. These provide the "expert stance" layer |
| `evidence-opinion-pack.md` Part 2 | Per-stage Tier 1 facts with verification status | Hard evidence to embed in each section. Facts marked `externally-verified` can be stated with confidence |
| `benchmark-success-formula.md` | Reader advancement mechanism, structural patterns, human texture, and the **Linguistic DNA Card** | The imitation target: how the benchmarks move readers, deploy evidence, and their specific Vocabulary Palette (Transitions, Paragraph Openers, Metaphors) |
| Selected benchmark article(s) | Full text of the primary (and optionally auxiliary) style anchor | Read the entire article, not a sample. Capture its structure, rhythm, transitions, bold usage, and voice organically |
| `project-profile.md` §5 | Red lines | Every paragraph checked against red lines before writing |

## Instructions

**[High-Fidelity Imitation + Stylistic Integration]** This skill runs the full writing stack.

**Philosophy**: Write the article as if you understand why the primary benchmark anchor works from the inside. Imitate its voice, cadence, sentence rhythm, structural logic, and reasoning trajectory with high fidelity. Before drafting, choose a working ratio for imitation, injection, and differentiation based on the current article instead of using a pre-filled default. Use the **Linguistic DNA Card** extracted in the success formula as a **Vocabulary Palette (词汇调色盘)**.

To prevent AI tone:
- **Prioritize Palette Choices**: Choose paragraph openers and transitions directly from the palette.
- **Organic Flow Over Constraints**: Do not apply rigid constraints like sentence-length standard deviations or hard checkpoints. Let the narrative flow naturally.
- **Seamless Data Integration**: Weave in our specific Tier 1 project facts, delivery controversies, and polarized stances by expressing them in the benchmark's tone and sentence logic. This creates a unified hybrid voice rather than a copy-pasted document.

- **Imitate**: Borrow the benchmark's structural logic, pacing, and prose texture.
- **Inject**: Replace the benchmark's examples, numbers, and case patterns with the project's Tier 1 evidence.
- **Differentiate**: Apply the project's own style where the benchmark's voice would violate red lines, sound unnatural, or fail to highlight unique evidence. Use `voice-and-humanization` and `structure-variation` as references, not as mechanical rules.
- **Ratio Choice**: In Phase 0, select and justify exact imitation / injection / differentiation percentages. The three values must total 100. Use higher imitation when the benchmark strongly matches intent, reader journey, and article type. Use higher injection/differentiation when the project evidence is unusually strong, the buyer decision is risk-heavy, or the benchmark structure would hide the project's advantage.

Numeric steering ranges:

| Parameter | Normal Range | Push Higher When | Push Lower When |
|---|---:|---|---|
| Imitation % | 40-80 | benchmark is highly aligned and the goal is to clone its rhythm closely | benchmark article type or buyer journey only partly fits |
| Injection % | 15-45 | proprietary project/factory evidence is the main advantage | evidence is thin or mainly supports only a few sections |
| Differentiation % | 5-25 | buyer risk is high, the project has unusual expert judgment, or benchmark structure would hide the advantage | benchmark voice/style already fits the project closely |

The selected percentages steer the draft. They are not paragraph quotas. If execution later needs to deviate by more than 10 points from the chosen vector, explain the reason in the Draft Retrospective.

**Main context only — no subagents.** The draft must be written in one continuous pass to maintain coherence, voice consistency, and natural transitions. Subagents would fracture the voice.

**Skills**: `voice-and-humanization` (lens descriptions, opinion emergence, dynamic AIO/bold guidance, anti-AI cleanup), `structure-variation` (rhythm guidance).

**No MCP tools needed.** All research is complete. All evidence is in the pack.

---

### Phase 0 — Plan Preview (output first, do NOT execute)

Before any writing, present a structured plan:

1. **Upstream Consumption Report** (MANDATORY first item): confirm exactly what was read from upstream:
   - From skeleton.md: section contracts (H2, format type, voice lens suggestion, evidence anchors, forbidden moves, transitions) per section = [summary table]
   - From narrative-arc.md: 6-node arc with emotional spine = [one-line per node]
   - From evidence-opinion-pack: processed opinions, **dynamic B2B controversies, and expert polarized stances** = [list of stances & controversies]. These form the expert backbone of the draft.
   - From evidence-opinion-pack Part 2: verified Tier 1 facts per stage = [summary]. Hard evidence anchors.
   - From benchmark-success-formula.md: the reader advancement mechanism, structural patterns, and the **Linguistic DNA Card (Vocabulary Palette)** we are emulating.
2. **Purpose & Success Criteria**: what the article must achieve for the reader
3. **Numeric Control Vector**: choose exact values and write rationale for each:
   - **Imitation / Injection / Differentiation %** (total 100). For spec-heavy B2B buyer guides where proprietary evidence (factory data, named hardware, retrofit-trap quantification) is the main advantage, the common case is **differentiation ≥ imitation**. Do not default to imitation-led ratios unless the benchmark anchor matches intent + reader + article type with high fidelity.
   - **Self-Contained RAG Citation Chunks (GEO / AI Search 独立语义块)** + **Full-sentence bold targets**: For decision-critical H2s, design a 40–60 word opening passage that is 100% self-contained when chunked by RAG systems (Perplexity, SearchGPT, Google AIO) — it must state the explicit subject entity (never "it" or "this option" referring back to the H2), the operating boundary/condition, the direct verdict, and a concrete metric, anchored by ≥ 1 full-sentence bold judgment (≥8 words).
   - **Short navigation bolds** (Path labels, Rule numbers, list-item leads, table emphasis): used for skimmer wayfinding; do **NOT** count toward the AI citation anchor budget. See `voice-and-humanization` Part 3 What to Bold.
   - **Opinion intensity (1-10)**: B2B buyer guides typically land at **7-8 at decision sections** (stance climax, see `voice-and-humanization` Opinion Intensity Scale). 9-10 is sparing; below 4 when buyer risk is high is under-controlled.
   - **AIO / GEO capture target**: how many H2s carry a self-contained RAG citation chunk.
   - **Evidence pressure (0-100)**: how strict the evidence-per-claim ratio is. 80+ for spec-heavy B2B, incorporating **Forensic Specificity** (caliper/instrument metrics, failure modes) and **Anti-Sell Disqualification Honesty** (telling the buyer when NOT to buy the high-spec option).
   - **Buying Committee & Internal Champion Enablement**: ensure the draft equips the technical reader (specifier/engineer) with a forwardable TCO/risk summary or decision ledger they can hand to their procurement/CFO approver.
   - **Target H2 count** and **format repetition tolerance**.
   - **Above-the-Fold / Navboost 3-second test**: the first ~180 words must deliver a direct answer + contrarian reframe hook + path/framework preview so the searcher immediately locks in (zero pogo-sticking).
   - **Continue-reading hooks**: each non-final H2 should end with a hook to the next section (loss frame, question, or quantified tease), not just an academic transition signal.

   Add a one-paragraph rationale tied to benchmark fit, evidence strength, buyer risk, and AIO capture needs.
4. **Writing Plan**: arc nodes → section sequence → format type per section → where the benchmark anchor's style will be most visible
5. **Key Opinions**: the 2-3 strongest judgments the article will deliver
6. **Risk & Boundaries**: what this draft will NOT do
7. **Style Anchor Proposal**: which benchmark article(s) the draft will IMITATE in voice and cadence. Anchor choice must be informed by reading the full benchmark, not by topic similarity.

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

### Phase 1 — Interactive Style Anchoring (mandatory, pre-drafting)

After plan approval, lock the writing style before writing a single word.

### Step 1: Benchmark Links Recap

Compile a recap of all known style anchors. Include:
- Benchmark articles from the success formula (clickable URLs with one-line "why this works")
- Any user-provided style reference links
- One-line note per link: what to emulate (voice, pacing, structure, persuasion technique)

### Step 1.5 — Read the Full Benchmark (MANDATORY, before anchor selection)

Open the primary anchor candidate's article. **Read the entire article**, not a sample. Do not rely on memory or summaries.

> **Why this step matters beyond style:** the benchmark anchor is usually a SERP top result for the target intent. Reading it in full is your chance to **use real ranking data to falsify or confirm abstract advice**. Example: if a stylesheet or external expert says "key-takeaways blocks are SEO toys, skip them," reading the SERP-leading anchor and finding it uses one anyway is decisive evidence the abstract advice is wrong. Treat this step as **the empirical calibration of the entire Phase 0 plan**, not just voice study.

While reading, note the following organically — do not produce a formal card unless it helps you:
- How the article opens and closes (does the opener deliver answer + hook + framework in the first ~200 words?)
- How sections transition (are there continue-reading hooks at H2 endings?)
- Where and how bold/italic/code formatting is used (full-sentence bolds vs short navigation bolds — count both)
- Paragraph rhythm and sentence variety
- How evidence, examples, and opinions are deployed
- Where first-person appears, if at all

If the full benchmark has not been read, stop. Do not proceed to Step 2.

### Step 2: Confirm Style Anchors (Stop A)

Ask the user to select:
- **ONE primary anchor** — the article whose voice and cadence the draft will embody
- **Optionally ONE auxiliary anchor** — for clarity/rhythm support where the primary style needs variation

Adopt a "become-them persona": write as if you authored the primary anchor, then inject the project's data and differentiated judgment. Do not describe the benchmarks — write as them.

```
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，按计划推进
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
```

Wait for explicit approval.

### Step 2.5 — Opener Concept Selection (Stop A2)

Before writing the sample paragraph, generate **only the opener concepts the article naturally supports**. Do not fill a quota. Usually 3-5 is enough, but stop sooner if the next concept only repeats an existing mechanism.

For each opener concept, provide:

| Field | What to state |
|---|---|
| Core idea | One-sentence premise of the opener |
| Hook type | Direct-answer + loss hook / contrarian reframe / quantified trap / one-question setup / scenario-counterexample / other |
| Dwell-time mechanism | Why this opener makes the reader keep scrolling in the first 3-5 seconds |
| Evidence / fact boundary | Which fact or judgment supports the hook; if unsupported, do not use it |
| Risk | What could make this opener feel hypey, too soft, or off-brand |
| Benchmark fit | Why this opener matches the selected anchor's rhythm |

Ask the user to choose one concept (or approve your recommendation) before writing the 150-200 word sample. This is adapted from self-media opener workflows: analyze the benchmark's opener, generate distinct opener mechanisms, then write the sample from the chosen mechanism — **not** from a generic intro template.

```
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的 Opener Concept（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 使用推荐 opener concept 写 sample
  · 选择：[concept 编号]
  · 补充 / 探讨：[你的新角度或质疑]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
```

Wait for explicit approval.

### Step 3: Sample Paragraph (Stop B)

Write a **150-200 word sample paragraph** in the selected voice, using content from the evidence-opinion-pack. This paragraph should demonstrate:
- The primary anchor's sentence rhythm and cadence
- How opinions emerge (conditional judgment / trade-off / counterexample / field language)
- Natural keyword integration
- The article's core tone

```
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，按计划推进
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
```

Wait for explicit approval. Do NOT proceed to full draft until the sample is approved.

---

### Phase 2 — Full Draft (one continuous pass)

**Main context only — no subagents.** Write the entire article in one continuous pass along the narrative arc.

**Skills to load**: `voice-and-humanization` (Parts 1, 2, 3 — including Benchmark Calibration, Dynamic AIO Capture, Stance vs Hype Boundary, and Markdown in Prose), `structure-variation`.

#### Hard Writing Requirements (in addition to NCV)

These are non-negotiable for CTR + dwell-time. Reader QA will check them.

1. **Opener 3-second test** — the first ~200 words MUST deliver:
   - **Direct answer to the title** in the first sentence (no suspense, no "energy storage is the rising star" preambles)
   - **Reframe / loss hook** in the next 1-2 sentences (what does the reader stand to lose by not reading on? Quantify if possible.)
   - **Path / framework preview** in the next paragraph (give the skimmer a way to locate themselves so they know it's worth scrolling)
   - If any of the three is missing, the opener is failing the dwell-time test. Rewrite before moving on.

2. **Continue-reading hooks at every non-final H2 ending** — each section's last 1-2 sentences must hook the next H2 with one of:
   - A loss / risk frame ("The cheapest inverter on your quote can quietly close the battery door. Here's how to spot which one does it.")
   - A question that the next section answers ("If you're on Path B, your next worry is whether deferring the battery actually costs you more. Here's the real math.")
   - A quantified tease ("Even with the right path picked, the wrong quote can still trap you. These are the lines to watch for.")
   - Generic academic transitions ("In the next section, we will discuss...") are forbidden — they leak dwell-time.

3. **Full-sentence AI-citation bold per H2** — at least 1 standalone judgment / definition / decision-rule sentence (≥8 words) bolded per H2, as the AI Overview / Bing Copilot extractable anchor. See `voice-and-humanization` Part 3 What to Bold. Short navigation bolds (Path labels, Rule numbers) do not count toward this target.

4. **Stance, not hype** — quantified, named, falsifiable stance at intensity 7-8 is encouraged at decision sections. Hype words at any intensity are forbidden. See `voice-and-humanization` Stance vs Hype Boundary.

**Constraint references** (loaded as mental models, not invoked as tools during writing):

| Reference | Role | How it constrains writing |
|---|---|---|
| Full Benchmark Read (Phase 1.5) | Positive target | "Write like THIS" — imitate the anchor's structure, rhythm, and reasoning trajectory using the Vocabulary Palette, then organically integrate our Tier 1 data and expert stances according to the approved ratio decision |
| `voice-and-humanization` skill | Negative filter | "Don't write like AI" — invoke the skill to load its full pattern reference as a writing constraint |

The full benchmark read and Humanizer work together: the benchmark gives the target voice, Humanizer keeps you from drifting into AI-default prose. Load both before writing. Keep both in mind while writing.

**No MCP tools needed.** All research is complete.

---

### Writing Rules

1. **Follow the arc, not the H2s.** The narrative arc is the master.
2. **Vary structure by scene** (`structure-variation`). Avoid lazy repeated templates; preserve intentional benchmark rhythm when it is part of the article's pull.
3. **Execute the approved voice.** Stay anchored in the primary benchmark's voice. The skeleton may suggest lens variations — treat them as options, not orders. Never announce opinions — let them emerge.
4. **Dynamic AIO capture** (`voice-and-humanization` Part 3). Make natural answer opportunities extractable when they serve the reader. For spec-heavy B2B articles, plan at least one **full-sentence bold** AI-citation anchor per H2 (a standalone judgment / decision rule / definition), while keeping short navigation bolds separate. Do not let snippet shape override the benchmark's prose rhythm or turn the article into a snippet farm.
5. **Human texture**: use conditional judgments, trade-off admissions, specific named projects, and field-language statements where the article needs them. Do not satisfy these as a checklist.
6. **CTA earned**: follows naturally from Arrival State.
7. **Vocabulary Palette Execution**: Actively select transition phrasing and paragraph starters from the benchmark's **Linguistic DNA Card** to maintain high-fidelity tone clone.
8. **Controversy & Stance Injection**: Weave every generated B2B delivery controversy and expert polarized stance into the relevant article sections. State them with conviction using the benchmark's voice.
9. **Natural inline links — consume skeleton contracts**: For each H2, read the `Internal/external link requirements` field from the skeleton contract. Place at least one inline link matching the skeleton's internal link assignment at the first natural moment in that section's body — using descriptive anchor text and a space-separated CommonMark title attribute (`[anchor](URL "title")`). Do not place accordion blocks, resource cards, or routing — those are `/article-resources` stage. The skeleton's link contract is the source of truth; `/article-resources` will later verify coverage and fill gaps, so inline links placed now reduce gaps later.
10. **Back-Half Density Parity (防长文后半截塌陷铁律)**: In a 3,000–4,500 word continuous pass, LLMs naturally tend to rush H2-05 through H2-08 by shrinking paragraphs and replacing forensic scenes with skeletal bullet lists. You MUST keep the second half of the article at the exact same forensic specificity, shop-floor scene richness, and Tier 1 proof density as the first half.
11. **External Citation Hygiene & `{{CITE}}` Tool-Handoff Slots (禁残缺脚注与水文外链)**:
    - For primary standards, official datasheets, or sources already verified via Apify in `evidence-opinion-pack.md`, use clean inline Markdown links `[descriptive anchor](URL)`.
    - **Never** use dangling `[^1]` footnote syntax without definitions, and **never** cite low-authority AI blog posts or generic LinkedIn pulse articles as proof.
    - Whenever a statistic, market range, or regulatory reference is intended for the operator to look up and attach in their external citation tool site after packaging, insert a structured handoff slot: **`{{CITE: exact claim needing citation | recommended search query}}`**. `scripts/assemble_publish_draft.py` will automatically index every `{{CITE: ...}}` slot into a top-level lookup table in `publish-package.md`.

### Safety Rules

- No unverified claims. Every factual statement traces to the evidence-opinion-pack.
- Draft-born claims captured at end for Truth QA.
- No GEO or mechanical answer-block prose.
- Profile red lines enforced.
- No image placeholders. No accordion blocks. No resource cards. Pure prose with inline links only.

---

### Draft Self-Audit — Humanizer (post-writing verification)

Humanizer was already loaded as a writing constraint in Phase 2. Now invoke it a second time — as an auditor — to scan the completed draft and produce an editorial report.

**Procedure**:

1. Invoke `voice-and-humanization` via the Skill tool, passing the full draft text
2. Humanizer returns detected AI patterns with line references
3. Review each detection against the full benchmark read:
   - **False positive / benchmark-intentional?** The pattern is actually from the anchor's style → keep it. Mark `[benchmark-intentional]`.
   - **Real AI-ism?** Generic filler, mechanical phrasing, promotional tone → fix it. Mark `[fixed]`.
4. Apply fixes
5. Append a brief Humanizer report to the PAUSE presentation (detected, fixed, intentional exceptions)

**Rule**: Humanizer is detection, not auto-rewrite. The full benchmark read is the authority. If Humanizer flags what the benchmark intentionally does, the benchmark wins.

### Humanizer Output (MANDATORY — append to PAUSE presentation)

After the self-audit, present an editorial report. This is proof that the skill was invoked and acted upon without pretending subjective quality can be reduced to a fake precision score.

Include:
- Benchmark-native moves preserved.
- Real AI-default patterns removed, with line references where useful.
- Patterns kept because they match the benchmark anchor.
- AIO capture moments added or preserved, and why they do not break the prose.
- Any section that still risks feeling flat or assembled.

If no material issues are found, say so plainly and name the benchmark evidence that supports that judgment. Do not report "0 patterns" as a numeric performance claim.

---

## Output

Create `articles/<article-slug>/draft.md` with:
- the complete article body,
- draft-born claims appended for Truth QA,
- a `## Draft Control Metadata` block containing:
  - the Numeric Control Vector chosen in Phase 0 and any execution drift rationale,
  - **Upstream Asset Traceability Checklist (上游高价值资产 100% 落地核销表)**: a markdown table mapping every Tier 1 forensic fact (`T1-xxx`), every `SERP Consensus Target` counter-move, and every `Anti-Sell Disqualification Boundary` from `evidence-opinion-pack.md` / `skeleton.md` to the exact H2 section where it landed in `draft.md` (zero silent drops allowed),
  - **Truth QA Watchlist**: quantified stance, cost ranges, source-required claims, high-stakes assertions, and any sentence likely to need softening if unsupported,
  - **Dwell-time / CTR execution notes**: opener 3-second test result, continue-reading hook coverage, and full-sentence bold AI-citation anchor coverage.

`Draft Control Metadata` is QA/control metadata, not publishable article copy. Downstream enrich and publish-pack stages must read it for diagnosis but exclude it from the final publishable body. Truth QA should use the Watchlist to verify supportability — not to automatically soften strong claims.

Update `state.json`: `currentStage: article-draft`, `nextCommand: /article-truth-qa`.

---

## Examples

### Example 1: Generating the One-Shot Draft
输入: `/article-draft content-workspace/steel-screen screen-article`
输出: `draft.md generated (4,200 words) using continuous writing mode, mimicking HubSpot C rhythm.`

## Guardrails

- **No Section-by-Section Iteration**: The draft must be written in a single continuous pass to preserve narrative flow and voice consistency.
- **Imitation Check**: Strictly mimic the structural rhythm and paragraph spacing of the selected primary benchmark where it creates reader pull. Use the approved ratio as a steering decision, not as a paragraph-by-paragraph quota.

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

Present the full draft. Ask: does it read as one continuous piece? Do the voice switches feel natural? Does any paragraph sound like a supplier wrote it?

### Draft Retrospective (after user approval, before proceeding to QA)

Record in project memory (`memory/draft-retrospective-<article-slug>.md`):

- How many revision rounds did this draft take before approval?
- Root cause of each revision (voice drift, format monotony, missing prose craft reference, insufficient benchmark imitation, user style feedback)
- Does any upstream command, agent, or skill need updating based on what was learned?
- One actionable recommendation for improving the workflow before the next draft

This prevents the same lessons from being re-learned on every article. File under the project memory directory.

Use the unified stop language.
