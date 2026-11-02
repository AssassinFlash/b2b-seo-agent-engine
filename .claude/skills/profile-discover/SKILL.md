---
description: "Use when: you only have a vague B2B business description and need to start discovery-first project profiling."
argument-hint: '[rough business description]'
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
name: profile-discover
---

# /profile-discover

## Purpose

Use when you only have a vague B2B business description and need to start discovery-first project profiling.

## Argument Contract

Use `$ARGUMENTS` as the user's raw business seed. It may be only one sentence.

Use this skill when the user has only a vague business idea, a partial product category, or a rough B2B SEO goal. Do not ask the user to fill a complete form first.

Input can be as small as:
- "我做金属屏风外贸，想做 SEO。"
- "We sell an industrial product but I do not know how to structure content."
- "I want to create B2B articles for this business: $ARGUMENTS"

## Instructions

0. **Pre-Flight Environment & Credential Check (New Machine Guard)**:
   - Run `python3 scripts/setup_env.py --no-network` (and `python3 scripts/apify_research.py check` before external lookup).
   - If the workspace directory does not exist yet, initialize it with `python3 scripts/setup_env.py --init-workspace <project-slug>`.
   - If this is a newly cloned computer with no Apify API token configured yet (or all tokens are exhausted), ask the user to paste their `apify_api_...` token(s) in chat and persist them immediately via `python3 scripts/apify_research.py set-tokens <token...>` (or `/system-setup`) so all subsequent stages use them automatically.
1. Treat the user's input as a discovery seed, not as a complete brief.
2. Run a light research pass before asking detailed questions (using **Apify first** via `python3 scripts/apify_research.py` or `mcp__apify__*` when external lookup is needed). This is the 轻量探索 stage:
   - Category definition & industry standards
   - Common product lines & technical boundaries
   - **B2B Buying Committee roles**: who searches (Technical Specifier: engineer/architect/installer) vs. who evaluates commercial terms (Procurement/Supply Chain) vs. who approves the budget (Owner/CFO/Project Director)
   - **Named E-E-A-T Technical Author & Reviewer candidates**: what real engineer/specialist persona will sign and review the technical guides
   - **Anti-Sell / Disqualification boundaries**: which low-margin, DIY, or mismatched inquiries the business actively wants to filter OUT
   - **Forensic proof availability**: what caliper measurements, test bench logs, pass/fail QC samples, and project records exist
   - **April Dunford Competitive Alternatives (Status-Quo Inertial Enemy)**: what buyers actually default to when they don't buy from us (e.g., frameless glass partitions, wood slats, drywall, local sign-shop painted mild steel, or pure string inverters) and why those status-quo alternatives fail after 12–24 months
   - Competitor or benchmark surface
   - Search intent patterns and likely content types
3. Use defaults to fill a useful `project-profile.draft.md`.
4. Clearly mark default values as defaults. 默认值 may guide the next questions, but they are not verified facts.
5. Do not lock the profile. The output is explicitly 不直接锁定.
6. End with a focused `Questions for User` section. Ask only questions that materially affect product scope, buyer targeting, evidence, markets, or publishing strategy.
7. Treat S0/S1/S2 style strategic discovery as internal capability, not as a long form the user must fill.

## Output Files

Create or update these files under `content-workspace/<project-slug>/`:

- `project-profile.draft.md`
- `state.json`
- `source-library/README.md`

`state.json` must set:

```json
{
  "profileStatus": "draft",
  "currentStage": "profile-discover",
  "nextCommand": "/profile-answer",
  "lockedProfile": false
}
```

### Stop Point

After producing `project-profile.draft.md`, stop. Do not run deep research and do not generate articles until the user answers or approves the next step.

## Examples

### Example 1: Running Discovery Research
输入: `/profile-discover content-workspace/steel-screen`
输出: `project-profile.md generated containing manufacturer capabilities, factory machinery, and B2B buyer profiles.`

## Guardrails

- **Direct Scrapes**: Verify information from verified factory directories, catalogues, or internal business registries.
- **Commercial Intent**: Ignore B2C retail questions. Focus strictly on architectural, structural, and OEM procurement intents.

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
