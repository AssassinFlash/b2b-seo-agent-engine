---
description: "Use when: the discovery draft is approved and you need deeper research before locking the profile."
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
name: profile-research-deep
---

# /profile-research-deep

## Purpose

Use after /article-cluster when a first-article topic has been selected and you need deeper research before locking the profile.

## Argument Contract

Use `$ARGUMENTS` as the project workspace path, typically `content-workspace/<project-slug>`.

Use this skill after `/profile-discover`, `/profile-answer`, and `/article-cluster` have produced a credible draft direction and a selected first-article topic card. This command researches the selected topic deeply and fills broader context gaps, but it does not lock the profile by itself.

## Required Inputs

- `content-workspace/<project-slug>/project-profile.draft.md`
- `content-workspace/<project-slug>/articles/<article-slug>/topic-card.md`
- User answers or corrections from the discovery loop
- Any provided website, catalog, product sheet, target market, or publishing platform notes

## Deep Research Scope

Perform 深度研究 on the selected first-article topic before locking the profile (mandatory **Apify-First** via `python3 scripts/apify_research.py` or `mcp__apify__*`, repairing and escalating across Actors/tools if blocked):
- Competitor websites and SERP patterns for the topic (including **SERP Consensus Platitudes** repeated across top-ranking pages)
- Product category, technical tolerances, and failure-mode anatomy relevant to the topic
- Keyword families, Hub-and-Spoke neighbors, and question clusters around the selected topic
- **Buying Committee friction**: technical specifier questions vs. procurement TCO/warranty objections vs. final approver risk concerns
- **Forensic Source Library & Anti-Sell inventory**: real test logs, caliper tolerances, pass/fail QC proof, and honest disqualification conditions (when NOT to buy)
- **Named E-E-A-T Author & Reviewer verification**: lock the credentials and field voice of the named engineer/reviewer
- Internal link opportunities and site link graph baseline
- Publishing platform constraints
- Source Library confidence and evidence gaps
- Risks from default assumptions that should not become article facts

Do not regenerate the topic pool here; `/article-cluster` already produced it.

## Output Files

Create or update:

- `project-profile.research.md`
- `source-library/README.md`
- `state.json`

`state.json` must set:

```json
{
  "profileStatus": "researched",
  "currentStage": "profile-research-deep",
  "nextCommand": "/profile-lock",
  "activeArticle": "<selected-article-slug>",
  "lockedProfile": false
}
```

Use the phrase ready for profile lock if the evidence is sufficient. If not, stop with specific research gaps.

## Stop Point

Stop after producing the deep research. The first article is already selected; `/profile-lock` will formalize it in the locked profile.

## Examples

### Example 1: Conducting Deep Engineering Research
输入: `/profile-research-deep content-workspace/steel-screen`
输出: `project-profile.md enriched with 15 engineering tolerances and raw material certifications.`

## Guardrails

- **Verification Requirement**: Cross-reference engineering claims against established ASTM or ISO standards.
- **Machinery Details**: Document specific factory machinery models (e.g. Trumpf Fiber Laser cutter) rather than generic descriptions.

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

## Instructions

Execute the steps described in the canonical sequence.
