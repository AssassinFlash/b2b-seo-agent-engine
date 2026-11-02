---
description: "Use when: the draft exists and you need to audit whether it still follows the benchmark success formula and avoids SEO-template drift."
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
name: article-benchmark-qa
---

# /article-benchmark-qa

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Before QA, verify: `project-profile.md`, `state.json` indicates `lockedProfile: true`, `draft.md`, `benchmark-success-formula.md`, `truth-qa.md`, `information-gain-qa.md` all exist.

## Purpose

Gate 3 of 4. Verify the draft still follows the benchmark success formula — not the competitor's structure, but the reader advancement mechanism. Catch well-intended additions (answerability blocks, E-E-A-T insertions, truth QA repairs) that broke pacing, tone, or article type fidelity.

## Instructions

**Main context**: read the draft against the success formula, write the drift audit.

**Skills to load**: `benchmark-transmutation` (borrowed asset transformation rules), `benchmark-led-answerability` (structure rules, source checks), `structure-variation` (format monotony detection), `quality-gates` (Gate 3 criteria, output template at `templates/benchmark-drift-audit.md`).

**No MCP tools needed** — all verification is against local artifacts.

---

### Required Checks

1. Article type still matches benchmark
2. Structure, pacing, information flow follow the Structural Blueprint and reader advancement mechanism
3. No forced FAQ or answer blocks where benchmark doesn't support them
4. Borrowed assets transformed, not copied
5. E-E-A-T insertions didn't create template prose
6. Repeated section formats are intentional benchmark rhythm, not lazy template drift (`structure-variation`)
7. **Imitation / Injection / Differentiation ratio drift** — read the **target** ratio from `/article-draft` Phase 0 plan (or `Draft Control Metadata` block in `draft.md`), then estimate the **actual** ratio from the executed draft. Diagnose drift if the actual ratio deviates ≥ 10 percentage points from target on any axis (e.g. target imitation 25% but draft reads 50% imitation = drift). Note: for spec-heavy B2B, differentiation-led ratios (differentiation ≥ imitation) are the common case and should NOT be flagged as drift simply for being differentiation-heavy — only flag when the executed ratio doesn't match the declared one.

### Pass/Block

- **BLOCK**: article type drifted, structure broken, forced answerability, reads like template
- **PASS**: all checks confirm benchmark fidelity

## Output

Write `articles/<article-slug>/benchmark-drift-audit.md`.

Update `state.json`: `currentStage: article-benchmark-qa`, `nextCommand: /article-reader-qa`.

## Examples

### Example 1: Performing Benchmark QA
输入: `/article-benchmark-qa content-workspace/steel-screen screen-article`
输出: `benchmark-drift-audit.md created. Status: PASS with concrete drift diagnosis.`

## Guardrails

- **No Fake Scores**: Do not use numeric alignment percentages unless backed by a defined external measurement. Diagnose concrete drift instead.
- **Rhythm Diagnosis**: Flag repeated section formats only when they feel lazy or break benchmark rhythm. Preserve intentional repetition that helps the article work.

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
