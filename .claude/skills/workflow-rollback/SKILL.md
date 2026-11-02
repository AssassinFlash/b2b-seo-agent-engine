---
name: workflow-rollback
description: "Use when: you want to rollback the workflow state of the project to a previous stage and clean up downstream artifacts."
argument-hint: 'content-workspace/project-slug [stage-name]'
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

# /workflow-rollback

## Argument Contract
Use `$ARGUMENTS` as:
```text
/workflow-rollback content-workspace/<project-slug> <stage-name>
```

## Purpose
Roll back the project workflow state to a previous stage in case of errors, QA blocks, or revisions, cleaning up downstream files.

## Instructions
1. Load `state.json` from the target project directory.
2. Verify that `<stage-name>` matches a valid stage in the sequence.
3. Verify that the target stage is chronologically prior to the current stage.
4. Update `currentStage` in `state.json` to the target stage.
5. Derive the target stage's next command and write it to `nextCommand`.
6. Cleanup downstream artifacts:
   - Identify all stages after the target stage in the sequence.
   - Look up the artifacts corresponding to those stages in `ARTICLE_STAGE_FILES` and `QA_FILES`.
   - Programmatically delete those downstream files to avoid state contamination.
7. Save the updated `state.json` with the current timestamp.

Prefer running:
```bash
python3 scripts/workflow_status.py $ARGUMENTS --rollback <stage-name>
```

If shell execution is not available, replicate the behavior:
- Read `state.json` from the project.
- Remove files manually and save state.json.

### Canonical Sequence
Valid stages list for rollback targets:
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
### Example 1: Rolling back to article-skeleton
输入: `/workflow-rollback content-workspace/decorative-screen article-skeleton`
输出: `Rolling back to 'article-skeleton'. Cleaning up downstream files: narrative-arc.md, draft.md. Updated state.json successfully.`

### Example 2: Rolling back to locked profile
输入: `/workflow-rollback content-workspace/decorative-screen profile-lock`
输出: `Rolling back to 'profile-lock'. Cleaning up all downstream files. Updated state.json successfully.`

## Guardrails
- **No Forward Rolling**: Do not use rollback to transition to future stages or skip stages.
- **Clean Deletion**: Downstream files must be permanently deleted to prevent stale state pollution.
- **Target Verification**: Never roll back to a stage that does not exist in the canonical sequence.
- **Save Integrity**: Always write the timestamp and correctly calculated nextCommand in state.json.
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，按计划推进
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
