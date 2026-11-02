---
description: "Use when: the draft exists and you need to audit human readability, natural flow, rhythm, and non-mechanical tone before enrichment."
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
name: article-reader-qa
---

# /article-reader-qa

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Before QA, verify: `project-profile.md`, `state.json` indicates `lockedProfile: true`, `draft.md`, `truth-qa.md`, `information-gain-qa.md`, `benchmark-drift-audit.md` all exist.

## Purpose

Gate 4 of 4. The final human-quality check. Verify the article reads like one continuous human-authored piece, not stitched-together modules. Catch the most dangerous failure mode: a draft that is complete, sourced, and orderly but still flat, templated, or unpersuasive.

## Instructions

**Main context only** — this is a subjective reading audit. Subagents cannot judge voice or human texture.

**Skills to load**: `voice-and-humanization` (opinion emergence, dynamic AIO/bold guidance, anti-AI cleanup), `structure-variation` (rhythm audit checklist), `quality-gates` (Gate 4 criteria, output template at `templates/reader-qa.md`).

**No MCP tools needed.**

---

### Required Checks

1. **Reader pull**: after each section, does the reader have a reason to continue?
2. **Flatness detection**: any section that is correct but has no tension, judgment, scene, or consequence?
3. **Template feeling**: do sections repeat the same opening, proof move, close, or emotional shape?
4. **Benchmark energy**: does the draft preserve the selected benchmark's pace, curiosity, and persuasion logic, not just its outline?
5. **AIO integration**: do extractable answers feel natural in prose, or do they interrupt the benchmark rhythm?
6. **Voice lens execution**: does prose match the scene without forcing lens names or styles?
7. **Opinion intensity**: too many strong opinions? too few? (`voice-and-humanization` Part 2)
8. **Bold usage**: judgments worth extracting, or keyword stuffing? (`voice-and-humanization` Part 3)
9. **Transitions**: forward pull vs backward summary
10. **Human texture & Named Expert inventory**: conditional judgments, trade-offs, anti-sell honesty, named projects, field language, and credible Named Engineer/Author voice
11. **Supplier voice detection**: flag sentences a competitor's sales manager could say
12. **Opening & Above-the-Fold Navboost strength**: does the first viewport (first ~180 words) reframe, answer directly, and route the reader without pogo-sticking?
13. **Self-Contained RAG Citation Chunks (GEO / AI Search)**: can the opening 40–60 words of key question H2s be extracted standalone by Perplexity / SearchGPT / Google AIO (explicit subject entity + condition + verdict + metric, without dangling pronouns)?
14. **Buying Committee Champion Check**: does the article give the technical specifier a concrete summary/ledger they can forward to their procurement/CFO approver?
15. **Back-Half Density Parity & Anti-Pattern-Fatigue Check**: do H2-05 through the final H2 maintain the same forensic specificity, workshop scene depth, and paragraph rhythm as H2-01–H2-04 (no late-draft collapse into thin bullet outlines), and does the article avoid repeating identical `> ### → Related:` callout templates across consecutive sections?

### Numeric Control Vector Audit

Do not grade with fake scores. Diagnose whether the draft chose and executed concrete control numbers:

| Control | Missing / Under-Controlled Signal | Over-Controlled Signal |
|---|---|---|
| Imitation / injection / differentiation | draft ignores the benchmark's rhythm and becomes generic | draft copies the benchmark shape but hides project evidence |
| AIO / bold intensity | buyer questions are answered vaguely or too late; no full-sentence bold AI-citation anchor per H2 | short navigation bolds inflated for no reason (table headers, single words, dollar amounts, every list-item lead); OR a full-sentence bold so long it reads as a screamed paragraph that breaks prose flow. **One full-sentence bold per H2 is the default, not the over-signal — do not penalize.** |
| Opinion intensity | sections explain facts without judgment or consequence; default sits below 4 when buyer risk is high | every paragraph sounds like a hot take at 9-10; OR stance hits 7-8 but with hype words instead of quantified judgments (see voice-and-humanization Stance vs Hype Boundary). **7-8 is the stance climax default for B2B buyer guides — do not penalize.** |
| Evidence pressure | decision-critical claims lack proprietary proof | setup/transition sections read like technical manuals |
| Format rhythm | sections feel interchangeable by section 2 or 3 | formats change for novelty and break the benchmark's reader journey |

If the Numeric Control Vector was not stated upstream, **BLOCK** and route back to `/article-draft` to add `Draft Control Metadata`. Do not silently infer missing controls. If the vector exists but execution differs materially from the selected numbers, diagnose the drift instead of rewriting blindly. Do not require exact math; focus on whether the numbers gave real direction.

### Pass/Block

- **BLOCK**: missing Numeric Control Vector, complete-but-flat reading experience, no forward pull, visible template assembly, AIO answers that interrupt prose, opening doesn't reframe, reads like supplier catalog, voice lenses consistently misapplied
- **PASS**: reads like one continuous human-authored piece with natural rhythm

## Output

Write `articles/<article-slug>/reader-qa.md`.

Update `state.json`: `currentStage: article-reader-qa`, `nextCommand: /article-enrich`.

## Examples

### Example 1: Reader QA Validation
输入: `/article-reader-qa content-workspace/steel-screen screen-article`
输出: `reader-qa.md generated. Status: PASS (Supplier voice instances: 0).`

## Guardrails

- **Supplier Voice Ban**: Reject the draft if phrases like "highest quality", "excellent service", or "industry leader" are found.
- **Flatness Ban**: Reject sections that are merely complete. A section must advance tension, judgment, proof, or reader decision.
- **No Mechanical Readability Rule**: Do not block solely because a paragraph length or sentence length is outside a fixed pattern. Use benchmark rhythm as the reference.
- **No Missing-Control Drift**: If the draft never states or follows its ratio, AIO/bold targets, opinion intensity, or evidence pressure, flag the missing steering decision before repair.

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
