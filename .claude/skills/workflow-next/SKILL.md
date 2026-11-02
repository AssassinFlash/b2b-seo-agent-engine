---
name: workflow-next
description: "Use when: you want to advance the workflow state of the project to the next stage after satisfying all validations."
argument-hint: 'content-workspace/project-slug [article-slug?]'
user-invocable: true
allowed-tools:
  - Bash
  - Read
  - Edit
  - Write
  - WebSearch
  - WebFetch
  - Agent
  - mcp__tavily__*
  - mcp__exa__*
  - mcp__crawl4ai__*
  - mcp__firecrawl__*
  - mcp__plugin_playwright_playwright__*
---

# /workflow-next

## Argument Contract
Use `$ARGUMENTS` as:
```text
/workflow-next content-workspace/<project-slug> [article-slug?]
```

## Purpose
Advance the project status to the next stage in the canonical workflow sequence, but only after executing all validations and QA gates.

## Instructions
1. Load `state.json` from the target project directory.
2. Verify the project profile is locked if trying to advance beyond the profile-lock stage.
3. If the current stage is one of the four QA gates (truth-qa, information-gain-qa, benchmark-drift-qa, reader-qa):
   - Verify the model-authored QA gate artifact exists and its verdict is `PASS` (not `BLOCK`).
   - If the QA gate is blocked or missing, block transition. Lock nextCommand to `/article-repair` (if blocked) and do not modify `currentStage`.
   - Preserve all generated files for user/AI manual editing and repair.
4. If all validations and checks for the current stage pass:
   - Identify the next stage in the workflow.
   - Write the updated `currentStage` and its corresponding `nextCommand` to `state.json`.
   - Update the `lastUpdated` timestamp with the current date-time.
5. Print the transition details to stdout.

Prefer running:
```bash
python3 scripts/workflow_status.py $ARGUMENTS --next
```

If shell execution is not available, replicate the behavior:
- Read `state.json` from the project.
- Match stages and write the changes back to `state.json`.

### Canonical Sequence
Valid progression:
- profile-discover
- profile-answer
- article-cluster
- profile-research-deep
- profile-lock
- article-intent-research
- article-benchmark
- article-benchmark-extract
- article-evidence-opinions
- article-skeleton
- article-arc
- article-draft
- article-truth-qa
- article-information-gain-qa
- article-benchmark-qa
- article-reader-qa
- article-enrich
- article-visual
- article-resources
- article-faq
- article-publish-pack
- article-review

## Examples
### Example 1: Advancing from skeleton to arc
输入: `/workflow-next content-workspace/decorative-screen stainless-divider`
输出: `Transitioning from 'article-skeleton' to 'article-arc'. Updated state.json successfully.`

### Example 2: Advancing blocked by QA failure
输入: `/workflow-next content-workspace/decorative-screen stainless-divider` (在 truth-qa 阶段校验失败)
输出: `Validation failed for gate truth-qa. Halting transition. nextCommand locked to /article-repair.`

## Guardrails
- **No Force Transitions**: Do not skip or bypass QA validation gates.
- **Preserve Assets**: Never delete or overwrite target drafts or research packs when validation fails.
- **Lock Verification**: Always confirm profile-lock status before allowing cluster-level transitions.
- **Pause Execution**: Stop and wait for explicit user approval before final file writes if specified by the pause protocol.
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，按计划推进
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
