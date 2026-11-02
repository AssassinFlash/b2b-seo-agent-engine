---
description: "Use when: the researched draft profile is approved and you need to create the locked project profile used by all downstream article work."
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
name: profile-lock
---

# /profile-lock

## Purpose

Use when the researched draft profile and selected first-article topic card are approved and you need to create the locked project profile used by all downstream article work.

## Argument Contract

Use `$ARGUMENTS` as the project workspace path, typically `content-workspace/<project-slug>`.

Use this skill after `/profile-research-deep` when the project direction, first article topic, source boundaries, and publishing rules are clear enough to become the root context.

## Required Inputs

- `project-profile.draft.md`
- `project-profile.research.md`
- `articles/<article-slug>/topic-card.md`
- User confirmations or corrections
- Source library notes
- `state.json` with `profileStatus: researched`

## Instructions

1. Read `templates/project-profile.md` as the canonical structure.
2. Create `project-profile.md` and `project-profile.json` from the template, the draft, the deep-research notes, and the selected topic card.
3. Preserve uncertainties as explicit assumptions or evidence gaps.
4. Do not convert defaults into article facts.
5. Define red lines, brand role, **Glossary & Forbidden Terms (`forbiddenTerms` / `preferredTerms`, e.g., using `pattern` instead of `product` and `inquiry` instead of `order/cart`)**, **Allowed Materials (`allowedMaterials`, e.g., `Stainless Steel (304 / 316)` only)**, **Host Blog Engine & Column Measure (`hostBlogEngine` / `proseMeasureCh`, e.g., `68ch` on `#md-blog-single`)**, named E-E-A-T author/reviewer personas, buying committee roles (specifier vs. procurement vs. approver), benchmark policy, source library, publishing platform rules, content pillars, and default article SOP settings.
6. Record the selected first article (`firstArticle`) and its `topic-card.md` path in the **First Article Lock** section of `project-profile.md` and in `project-profile.json` (which MUST conform to `config/profile-schema.json`).
7. Set `lockedProfile: true` only when the profile is usable by downstream skills.

## Output Files

Create or update:

- `project-profile.md`
- `project-profile.json`
- `state.json`

`state.json` must set:

```json
{
  "profileStatus": "locked",
  "currentStage": "profile-lock",
  "nextCommand": "/article-intent-research",
  "lockedProfile": true
}
```

### Stop Point

Stop after locking the profile. Topic selection already happened in `/article-cluster`; the next step is `/article-intent-research` for the selected article.

## Examples

### Example 1: Locking the Project Profile
输入: `/profile-lock content-workspace/steel-screen`
输出: `state.json updated with lockedProfile: true. Content creation pipeline activated.`

## Guardrails

- **Double-Lock Prevention**: Once lockedProfile is set to true, do not allow modifications to project-profile.md.
- **Integrity Validation**: Validate that all required structural fields in project-profile.md are fully populated before locking.

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
