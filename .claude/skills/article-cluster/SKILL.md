---
description: "Use after: /profile-answer when you have keyword data and need to generate a data-driven topic pool with Deep SEO Cards, weighted scoring, and a prioritized article queue."
argument-hint: '[content-workspace/project-slug]'
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
name: article-cluster
---

# /article-cluster

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug>`.

Verify: `project-profile.draft.md` and `state.json` with `lockedProfile: false`. This skill runs **before** `/profile-lock` as part of profile establishment.

## Purpose

Transform the draft profile and keyword data into a strategically rich, quantitatively validated topic roadmap. The output is not a flat list — it is a full content strategy document (`topic-cluster.md`) with an executive summary, benchmark analysis, content pillars, 50+ detailed Deep SEO Cards, tiering, and a prioritized article queue. The user then selects the first article, which is carried forward into `/profile-research-deep` and locked into the profile.

## Instructions

**Phase 1 (Agent)**: Spawn **topic-cluster-researcher** to process the profile + keyword data + live SERP analysis into a full `topic-cluster.md` with executive summary, benchmark analysis, 4-8 content pillars, **50+ candidate cards** (concise bullet-style, matching the S3 reference format), tiering, and article queue. The agent reads real CSV exports from `source-library/` if present, falls back to `keyword-research/*-analysis-*.md` reports if CSVs are absent, uses the `search-toolbox` skill for SERP research, and applies the weighted scoring model. Keep this work in a subagent context.

**Phase 2 (Main)**: Review the agent's output with the user. Adjust tiers, add/remove topics.

**Phase 3 (Main)**: Create the topic-card for the first article.

**Skills**: `b2b-seo-article-sop` (Deep SEO Card template at `templates/deep-seo-card.md`), `evidence-policy` (Tier 1 availability check), `search-toolbox` (tool selection and fallback logic for SERP analysis).

---

### Phase 0 — Plan Preview

Present: data sources (which SEMrush CSVs exist), batch plan, scoring calibration, success criteria.

Use the unified stop language. Wait for approval.

---

### Phase 1 — Topic Pool Generation + SEO Validation (Agent)

Spawn **topic-cluster-researcher** [sonnet] with: the draft profile, all available SEMrush CSV exports, and the Deep SEO Card template.

The agent executes:
1. **Data Inventory & Live Apify Cold-Start Harvest (严禁无数据盲猜)** — reads `source-library/keyword/*.csv` if available. **If `source-library/keyword/*.csv` is empty**, NEVER invent 50 `[estimated]` keywords from memory alone: first run `python3 scripts/apify_research.py` (`--preset google-serp` / `rag-web-browser` + Google Autocomplete/PAA) seeded from `source-library/evidence/` (e.g., `catalog-146-patterns-truth.md` and `site-pages-and-cases-truth.md`) to harvest a real SERP & PAA keyword dataset into `source-library/keyword/` before generating cards!
2. **Benchmark Analysis** — audits top-ranking pages and identifies content gaps.
3. **50+ Candidate Generation (Pain-Point SEO 5 B2B Archetypes + Anti-DIY Filter)** — Build the pool across Benji Hyam & Devesh Khanal's (*Grow and Convert*) **5 High-Converting B2B Pain-Point SEO Archetypes** rather than chasing high-volume consumer vanity terms:
   - **Archetype 1 — Category & Specification Commercial Queries** (e.g., `custom laser cut stainless steel screens`, `architectural metal partition manufacturer`)
   - **Archetype 2 — Comparison & Alternative Queries (`X vs Y`)** (e.g., `304 vs 316 stainless steel screen`, `PVD vs powder coated metal partition`, `hybrid vs string inverter without battery`)
   - **Archetype 3 — Technical Bottleneck & Failure-Prevention JTBD Queries** (e.g., `how to anchor floor-to-ceiling metal screen without drilling marble`, `how to prevent laser cut panel warping`)
   - **Archetype 4 — Cost Anatomy, Quote Red-Flags & BOM Driver Queries** (e.g., `custom stainless steel screen cost per square meter`, `solar battery retrofit hidden cost`)
   - **Archetype 5 — Engineering Compliance, Tolerance & Disqualification Queries** (e.g., `open area percentage for HVAC return screen`, `coastal wind load calculation for exterior privacy screen`)
   - **B2C / DIY SERP Noise Filter (防 C 端流量陷阱)**: Whenever a high-volume keyword's Google SERP Top 5 is dominated by B2C retail/DIY platforms (Amazon, Wayfair, Etsy, Home Depot, IKEA, Pinterest DIY room dividers), **do NOT target the bare B2C term** — either disqualify it or reframe the card around commercial/architectural B2B modifiers (`commercial`, `architectural`, `304/316 stainless steel`, `custom fabricated`, `hospitality`).
4. **SEO Validation & B2B Revenue-Weighted Scoring** — per-topic: produces a concise candidate card with seed keyword, primary keyword, long-tail keywords, intent, volume, traffic potential, LSI terms, SERP snapshot, dominant formats, gaps/opportunities, persona fit, replication feasibility, and a per-card Opportunity Score derived from the **B2B Pain-Point 5-dimension weighted model** (`Buying Intent & Conversion Proximity 30%`, `E-E-A-T & Proprietary Info Gain 25%`, `Competition / SERP Gap 20%`, `Cluster Reach / Volume 15%` with **Zero-Volume High-Ticket Override**, `Production Feasibility 10%`). Never penalize a high-intent engineering/procurement query just because third-party tools report 10–50 monthly searches.
5. **Hub & Spoke Topology + SERP Cannibalization Guard (防自相残杀与拓扑包裹)**:
   - **SERP Overlap Check**: If two candidate keywords share >60% of the same top-10 ranking URLs on Google SERP (or answer the exact same buyer job), **merge them into one card** (one as Primary Keyword, the other as Secondary/Long-tail). Never split overlapping intents into two articles that cannibalize each other.
   - **Hub & Spoke Mapping**: Assign every card a `Cluster Role`: either `Pillar Hub` (comprehensive overview anchoring a content pillar) or `Supporting Spoke` (deep-dive into a specific cost, failure mode, comparison, or application that links back to its Pillar Hub).
6. **Tiering** — T1/T2/T3 based on weighted score and Hub-and-Spoke launch sequence (launch high-converting spokes alongside or right after their Pillar Hub).
7. **Strategic Synthesis** — executive summary, 4-8 content pillars with Hub-and-Spoke topology diagrams, cannibalization merge log, first article recommendation, article queue, AIO implications, gaps to avoid.
8. **Self-Validation** — before handing back, the agent runs `scripts/validate_topic_cluster.py` against `topic-cluster.md` and fixes any card-count, field-completeness, or tier-threshold issues.

Agent outputs `topic-cluster.md` with all cards, scores, and tiering.

---

### Phase 2 — Review Topic Pool

Present the agent's output. Key questions:
- Are Tier 1 topics truly the best starting points?
- Any high-business-value topics that scored low due to data gaps?
- Any topics to add, remove, or re-tier?

Use the unified stop language. Wait for approval.

---

### Phase 3 — First Article Topic Card

For the highest-scoring Tier 1 topic (or the user's preferred starting point), create `articles/<article-slug>/topic-card.md`:

- Strategic justification
- Reader profile
- Keyword assignment (primary/secondary/supporting from the SEO Card)
- Benchmark targets (article type + best-in-class reference URLs)
- Outline sketch (H2-level)
- Information Gain anchors (which Tier 1 evidence will be used)
- E-E-A-T strategy

---

## Output

Create:
- `topic-cluster.md`
- `articles/<article-slug>/topic-card.md`

Update `state.json`: `currentStage: article-cluster`, `nextCommand: /profile-research-deep`, `activeArticle: <slug>`, and record the selected article in `articles[]`.

## Examples

### Example 1: Building a Topic Pool
输入: `/article-cluster content-workspace/steel-screen`
输出: `topic-cluster.md generated containing 52 B2B Deep SEO Cards and strategic Content Pillars.`

## Guardrails

- **Volume vs Intent**: Prioritize search intent alignment over high search volume. Long-tail commercial keywords must take precedence.
- **Card Completeness**: Do not leave any fields blank or marked as TBD in the Deep SEO Cards. Every card must include a per-card 5-dimension weighted scoring table.
- **Count Enforcement**: The final `topic-cluster.md` must contain at least 50 candidate cards unless the user explicitly approves a smaller strategic shortlist.
- **Data Traceability**: When CSVs are unavailable, derive figures from `keyword-research/*-analysis-*.md` and mark them `[estimated from keyword-research report]`.
- **Validation Gate**: Run `scripts/validate_topic_cluster.py` before creating the topic card. If validation fails, return to Phase 1.

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

Wait for explicit approval before proceeding.
