---
description: "Use when: you need a read-only project and article status cockpit with blockers and the next safe command."
argument-hint: '[content-workspace/project-slug] [article-slug?]'
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
name: workflow-status
---

# /workflow-status

## Purpose

Use when you need a read-only project and article status cockpit with blockers and the next safe command.

## Argument Contract

Use `$ARGUMENTS` as an optional project workspace path plus an optional article slug:

```text
/workflow-status [content-workspace/<project-slug>] [article-slug?]
```

If `$ARGUMENTS` is empty:

- If `content-workspace/` has no projects, recommend `/profile-discover`.
- If `content-workspace/` has one project, inspect that project.
- If `content-workspace/` has multiple projects, list candidates and ask the user to rerun with one project path.

If a project is provided but no article slug is provided, read `state.json.activeArticle`. If no active article exists, show the project status and article queue.

## Instructions

This is the main read-only status cockpit. It diagnoses, but it does not repair.

- Do not create, edit, or delete files.
- Do not update `state.json`.
- Do not run the next command automatically.
- Do not bypass the locked profile gate.
- If `lockedProfile` is not true, only recommend `/profile-answer`, `/article-cluster`, `/profile-research-deep`, or `/profile-lock`.
- If the profile is locked, inspect the artifact graph and recommend exactly one next safe command.

Prefer running:

```bash
python3 scripts/workflow_status.py $ARGUMENTS
```

If shell execution is unavailable, reproduce the same logic by reading `state.json`, profile files, and article artifacts directly.

## Output Contract

Output these sections exactly:

- `Current Position`
- `Progress Bar`
- `Blocking Issues`
- `Next Safe Command`
- `What You Can Ignore For Now`
- `Article Queue`

The answer should make it obvious:

- where the project is now
- which artifacts are missing
- whether a QA gate is blocking progression
- which single command is safe to run next
- which later-stage files the operator can ignore for now

## Examples

### Example 1: Querying Project Status
输入: `/workflow-status content-workspace/steel-screen`
输出: `Current Stage: article-skeleton. Next Command: /article-arc. Files verified: locked.`

## Guardrails

- **Strict Read-Only**: Do not write, delete, or rename any files under this command context.
- **Audit Consistency**: Ensure the CLI output matches state.json exactly without introducing arbitrary data.
