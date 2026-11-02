---
description: "Use when: the draft exists and you need to audit information gain — whether the article and its decision-critical sections contain insights only this business could provide."
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
name: article-information-gain-qa
---

# /article-information-gain-qa

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Before QA, verify: `project-profile.md` exists, `state.json` indicates `lockedProfile: true`, `draft.md` exists, `truth-qa.md` exists, `evidence-opinion-pack.md` exists.

## Purpose

Gate 2 of 4. The Mannlee precedent proves that factually correct B2B content can collapse when Google weights Information Gain. This gate asks: "Could a competitor reproduce this article's important decisions by swapping their brand name?" If yes, the article lacks information gain and must be repaired.

## Instructions

**Main context**: read the draft section by section, cross-reference each section against the evidence-opinion pack, and run the competitor-replaceability test.

`Draft Control Metadata` is QA metadata, not an article section. Use it to understand intended evidence pressure and format rhythm, but exclude it from replaceability, Tier 1 placement, and section-value judgments.

**Subagent for competitor comparison** (spawn if needed): If it is unclear whether a section's claims are replaceable, spawn a subagent to search 2-3 competitor pages for equivalent claims. Let the subagent use the `search-toolbox` skill to choose tools and fallbacks. The subagent reports whether the section's core insight already exists elsewhere.

**Skills to load**: `evidence-policy` (Tier 1/2/3 classification and Information Gain rules), `quality-gates` (Gate 2 criteria, output template), `search-toolbox` (complete tool inventory with decision logic — read BEFORE any external comparison).

**External comparison strategy** — only when competitor comparison is needed. Use the `search-toolbox` skill to select the right search/extraction tool for each competitor or benchmark page.

### Required Checks

1. **Decision-section Tier 1 coverage**: technical decisions, cost/risk trade-offs, supplier evaluation, process proof, case-study proof, specifications, and conversion-critical recommendations must anchor their core claim in Tier 1 evidence.
2. **Competitor-replaceability test**: for each decision-critical section, replace the business name with "a competitor" — does the section still stand? If yes, it lacks information gain.
3. **Article-level proprietary weight**: the article must contain enough Tier 1 evidence to change the reader's decision. Do not reduce this to an even per-H2 quota.
4. **No Tier 3-only sections**: a section built only on generic knowledge must be cut or rebuilt
5. **Specificity, Forensic Proof & Princeton GEO Citation Triple Check**: verify that decision-critical sections combine all three proven GEO citation boosters — (a) **Condition-bounded statistics/tolerances**, (b) **Attributable Named-Engineer or Primary-Standard quotes**, and (c) **Physical cause-and-effect failure chains** — rather than generic adjectives
6. **SERP Consensus Counter-Check (Google Information Gain Patent + Animalz Counter-Narrative)**: verify that the draft actively dismantles, qualifies, or deepens the competitor platitudes listed in `intent-research.md`'s `SERP Consensus Target` using the *Antithesis → Forensic Teardown → Conditional Rule Synthesis* spine rather than repeating the SERP consensus vector
7. **Anti-Sell / Disqualification Honesty Check**: verify that the article includes honest boundary conditions (when NOT to choose a given path/spec) so it reads like an engineering advisor rather than a one-way sales brochure

### Pass/Block

- **BLOCK**: the article is majority replaceable, a decision-critical section lacks Tier 1 support, a Tier 3-only section makes a central claim, or available proprietary expertise is unused where it matters.
- **PASS**: decision-critical sections use Tier 1 evidence, generic/setup sections do not pretend to prove more than they can, and the article's core value could not be reproduced by a competitor swapping brand names.

## Output

Write `articles/<article-slug>/information-gain-qa.md`.

Update `state.json`: `currentStage: article-information-gain-qa`, `nextCommand: /article-benchmark-qa`.

## Examples

### Example 1: Information Gain Audit
输入: `/article-information-gain-qa content-workspace/steel-screen screen-article`
输出: `information-gain-qa.md generated. Status: PASS with decision-section evidence map and replaceability diagnosis.`

## Guardrails

- **No Single Similarity Threshold**: Use competitor similarity as evidence, not as the only decision rule. Name what is replaceable and where proprietary proof changes the answer.
- **Proprietary Focus**: Verify that the article details specific tolerances or processes unique to the factory's locked profile.

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

If the gate is blocked, present the blocked sections with exact replaceability evidence and recommend `/article-repair`.
