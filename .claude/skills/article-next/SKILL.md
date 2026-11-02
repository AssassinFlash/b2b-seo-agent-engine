---
description: "Use when: you want a lightweight read-only recommendation for the next safe command without skipping approval gates."
argument-hint: '[content-workspace/project-slug]'
user-invocable: true

allowed-tools:
  - Bash
  - Read
name: article-next
---

# /article-next

## Purpose

Use when you want a lightweight read-only recommendation for the next safe command without skipping approval gates.

## Argument Contract

Use `$ARGUMENTS` as the project workspace path, typically `content-workspace/<project-slug>`. The article slug is optional; if omitted, infer the active article from `state.json` (`activeArticle`) or, if only one article exists, from the `articles/` directory.

Read `state.json` (and optionally `articles/<article-slug>/state.json` if the project uses per-article state), summarize the current workflow status, and recommend the next command.

This is a lightweight next-step hint. If the user needs a full progress bar, blocker diagnosis, article queue, or recovery view after time away, route them to `/workflow-status`.

---

## Decision Procedure

1. **Locate state.**
   - If `content-workspace/<project-slug>/state.json` exists, load it.
   - If not, recommend `/profile-discover` and stop.

2. **Profile lock check.**
   - If `lockedProfile` is missing or `false`, the project is still in profile establishment.
   - Recommend the next safe profile command based on `profileStatus` and existing artifacts:
     - `draft` → `/profile-answer`
     - `article-cluster` or `topic-card` exists → `/profile-research-deep`
     - `researched` → `/profile-lock`
     - missing/unknown → `/profile-discover`
   - Stop. Do not suggest article production commands.

3. **Determine active article.**
   - If `activeArticle` is set, use it.
   - Else if the `articles/` directory contains exactly one slug, use that slug.
   - Else if multiple articles exist, list them and ask the user to specify one.
   - Else (no articles yet) → this is an inconsistent locked state; route to `/workflow-status`.

4. **Read article state.**
   - Look for `articles/<article-slug>/state.json` first.
   - Fall back to the project-level `state.json` fields `currentStage`, `nextCommand`, `articleStatus`.

5. **Recommend the next command.**
   - Use the explicit `nextCommand` if present and valid.
   - Validate that the recommended command matches the canonical sequence and that its required input artifact exists.
   - If a required artifact is missing, override the recommendation and tell the user what is missing.

6. **Repair branch.**
   - If `articleStatus` is `blocked` or a QA gate file contains `BLOCK`, recommend `/article-repair` instead of advancing.
   - Do not advance past a failed gate.

---

## Canonical Sequence

Valid article progression after `/profile-lock` (stop at every ⏸ gate for Peer Co-Research & Calibration — never skip stages):

`/article-intent-research` → `/article-benchmark` → `/article-benchmark-extract` → `/article-evidence-opinions` → `/article-skeleton` → `/article-arc` → `/article-draft` → `/article-truth-qa` → `/article-information-gain-qa` → `/article-benchmark-qa` → `/article-reader-qa` → `/article-repair` (if blocked) → `/article-enrich` → `/article-visual` → `/article-resources` → `/article-faq` → `/article-publish-pack` → `/article-review`

---

## Output Format

Output only:

- **Current status** (project + active article stage)
- **Missing inputs**, if any
- **Recommended next command**
- **One-sentence reason**

Example:

```text
Project: metal-divider-b2b | Profile: locked
Article: stainless-steel-screen-guide | Stage: article-reader-qa
Missing inputs: none
Recommended next command: /article-enrich content-workspace/metal-divider-b2b stainless-steel-screen-guide
Reason: All four QA gates passed; enrichment is the next safe stage.
```

---

## Guardrails

- Do not run the next command automatically.
- 不得自动越过停点.
- Do not bypass the locked profile gate.
- Do not recommend advancing past a failed QA gate.
- If in doubt, route to `/workflow-status` for a full diagnostic.

## Instructions

Execute the steps described in the canonical sequence.

## Examples

### Example 1: Read-Only Next Command Recommendation
输入: `/article-next content-workspace/steel-screen screen-article`
输出: `Project: steel-screen | Stage: article-evidence-opinions | Recommended next command: /article-skeleton content-workspace/steel-screen screen-article (read-only; state.json not modified).`
