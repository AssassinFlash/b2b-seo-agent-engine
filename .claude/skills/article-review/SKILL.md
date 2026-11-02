---
description: "Use when: an article has been live for 30/60/90 days and you want to analyze GSC or SEMrush performance against the original SEO Card predictions, then feed insights back to the topic-cluster strategy."
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
name: article-review
---

# /article-review

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Verify: the article has been published (state.json shows publish-pack completed), `topic-cluster.md` exists with the original SEO Card, `topic-card.md` exists.

## Purpose

Close the feedback loop with **available performance evidence**, not aspirational metrics. The system produces articles based on SEO Card predictions — this skill checks whether those predictions were right, whether the title/opener/H2 hooks earned behavior, diagnoses variances, and feeds insights back to the topic-cluster, article-title, article-draft, and skeleton strategies.

Short-term performance is a first-class constraint: if the page gets impressions but weak CTR, fix title/meta/H1; if it gets clicks but weak engagement, fix opener, section hooks, and content promise; if it gets neither, revisit intent/keyword fit. Do not pretend unavailable metrics exist — classify data sources by tier.

## Instructions

**Phase 1 (Agent)**: Spawn **performance-review-strategist** to analyze available performance data by tier (GSC core metrics first; analytics only if available; manual SERP/AIO checks where needed), compare vs SEO Card baseline, diagnose title/opener/H2/cluster variances, and produce strategy recommendations.

**Phase 2 (Main)**: Review recommendations with user. Decide which insights to feed back to the next cluster run.

**Skills**: `b2b-seo-article-sop` (SEO Card template for baseline comparison).

**Skills**: `search-toolbox` — use if live SERP position data is needed when GSC exports are unavailable.

### Performance Data Tiers

Do not pretend every metric is available. Classify the review input by tier and only draw conclusions the data supports.

| Tier | Metrics | Source | How to use |
|---|---|---|---|
| **Tier 1 — Core, request first** | GSC clicks, impressions, CTR, average position, query-level CTR, page-level clicks | Google Search Console export | Primary short-term performance signal. Weak CTR with impressions = title/meta/H1 issue. Good CTR with low rank = demand signal worth supporting. |
| **Tier 2 — If analytics installed** | GA4 engagement time, engaged sessions, bounce rate, conversions/clickouts, scroll depth (if configured) | GA4 / Clarity / Hotjar / analytics export | Diagnose whether clicks stayed. Low engagement after high CTR = opener/content promise mismatch. |
| **Tier 3 — Manual or sampled** | AIO citation appearance, featured snippet, SERP title rewrite, competitor title changes, live SERP layout | Manual SERP checks / rank tracker / search-toolbox | Diagnose SERP packaging. If Google rewrites the title, article-title or metadata needs repair. |
| **Proxy-only** | return-to-SERP / pogo-sticking | Not directly available | Infer cautiously from high CTR + low engagement + rank drop / poor conversions. Label as proxy, never as measured fact. |

### Performance Diagnosis & Clearscope Strike-Distance Refresh Rules (Bernard Huang Protocol)

- **Strike-Distance Query Injection (Positions 4–15 with High Impressions)** → the highest-ROI B2B SEO move: extract GSC queries where this page already ranks in positions 4–15 without a dedicated heading, and inject a surgical H3 or `<details class="b2b-mod-faq">` block answering that exact query with a 40–60 word BLUF passage + Tier 1 metric to push it into Top 3 + AI Overviews.
- **Impressions but weak CTR (<1.5% in Top 5)** → review title, meta description, H1, SERP promise, and single CTR hook mechanism (`title-options.md`).
- **Good CTR but weak engagement / rapid pogo-sticking** → review Above-the-Fold 3-second test (first ~180 words + interactive micro-anchor), section-end continue-reading hooks, and H2 promise mismatch.
- **Good engagement but rank stalled at #6–#12 (Authority / Internal Link Deficit)** → run `python3 scripts/update_link_graph.py` and add 2–3 contextual inbound links from existing high-authority Hub/Spoke pages using varied descriptive anchors (Cyrus Shepard First-Link Priority).
- **AIO / GEO citation missing despite Top 5 ranking** → upgrade H2 opening 40–60 words with the **Princeton GEO Citation Triple** (condition-bounded statistic + attributable Named-Engineer/Standard quote + physical failure cause-and-effect chain).
- **SERP title rewrite** → compare Google's rewritten title to `title-options.md`; feed the wording back into `/article-title`.

---

### Phase 0 — Plan Preview

Present: available data sources, comparison baseline, time window.

Use the unified stop language. Wait for approval.

---

### Phase 1 — Performance Analysis (Agent)

Spawn **performance-review-strategist** [sonnet] with: GSC exports (Tier 1, if available), GA4/Clarity/Hotjar analytics exports (Tier 2, if available), manual SERP/AIO/title-rewrite observations (Tier 3, if available), SEMrush position data (if available), the original topic-cluster.md SEO Card, topic-card.md, keyword-record.csv, `title-options.md` (if present), and `draft.md` / `enriched-draft.md` for opener/H2 hook diagnosis.

Agent outputs `performance-review.md` with: performance summary, SEO Card comparison table, root cause analysis, topic-cluster strategy recommendations, content insights, keyword discoveries.

---

### Phase 2 — Review & Integrate

Present the agent's findings. Key decisions:

- Which over-performing topic patterns should the next cluster run prioritize?
- Which under-performing topic types should be deprioritized or reformatted?
- What new keyword discoveries should enter the keyword universe?
- Any technical SEO issues to flag for site audit?

Use the unified stop language.

---

## Output

Create `articles/<article-slug>/performance-review.md`.

Update `topic-cluster.md` (if applicable): annotate the reviewed topic's SEO Card with actual performance data and a link to the review.

Update `state.json`: `lastReviewed: <date>`.

## Examples

### Example 1: Auditing 30-Day Rank Data
输入: `/article-review content-workspace/steel-screen`
输出: `performance-review.md generated tracking 15 keywords on Google Search Console.`

## Guardrails

- **Actionable Adjustments**: Do not recommend vague changes. Propose specific query additions, internal links, or heading adjustments.
- **Milestone Adherence**: Only review rankings for pages that have stabilized for at least 30 days post-publishing.

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
