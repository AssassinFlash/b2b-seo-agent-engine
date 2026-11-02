---
description: "Use when: the user has answered discovery questions and you need to update the draft profile and decide next steps."
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
name: profile-answer
---

# /profile-answer

## Purpose

Use when the user has answered discovery questions and you need to update the draft profile and decide next steps.

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug>` plus any user-provided answer text. If the path is missing, stop and ask for it.

Use this skill after `/profile-discover` when the user has answered some, but not necessarily all, discovery questions.

## Required Inputs

- `content-workspace/<project-slug>/project-profile.draft.md`
- Latest user answers, corrections, links, files, catalogs, site notes, market notes, or publishing constraints
- `state.json` with `profileStatus: draft`

## Instructions

1. Engage in **Peer Co-Research & Calibration (对等共研)**: neither human > AI nor AI > human. Cross-check user-supplied materials, links, or assumptions against market/search reality, push back with evidence where an angle is too narrow or conflicts with real buyer search behavior, and update `project-profile.draft.md` once aligned.
2. Keep unconfirmed defaults and assumptions clearly labeled.
3. Ensure the draft profile captures the **Buying Committee Matrix** (Specifier / Procurement / Approver), **Named E-E-A-T Author & Reviewer personas**, **Forensic Proof inventory**, and **Anti-Sell disqualification rules**.
4. Add a short `Answer Assimilation Log` section showing what changed and what was debated/calibrated.
5. Decide whether another 反问循环 is required.
6. Ask only questions that materially affect project-profile quality.
7. If enough direction is confirmed, set the next command to `/article-cluster` (so keyword data can drive Hub-and-Spoke topic selection before deep research and profile lock).

## Output Files

Update:

- `project-profile.draft.md`
- `state.json`

`state.json` must keep:

```json
{
  "profileStatus": "draft",
  "currentStage": "profile-answer",
  "nextCommand": "/article-cluster",
  "lockedProfile": false
}
```

### Stop Point

Stop after updating the draft and asking the next focused question set or recommending `/article-cluster`.

## Examples

### Example 1: Gathering Profile Answers
输入: `/profile-answer content-workspace/steel-screen`
输出: `project-profile.json updated with answers for 12 outstanding engineering questions.`

## Guardrails

- **Zero Guesswork**: Do not fabricate technical specifications. If details are missing, prompt the operator with multiple-choice questions.
- **Format Integrity**: Verify that answers are parsed and written as valid JSON-LD entity nodes.

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
