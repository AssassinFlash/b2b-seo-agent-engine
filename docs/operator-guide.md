# Operator Guide

This project is intentionally deep. The status cockpit exists so the depth stays usable after you step away from a project.

> **Reminder**: All workflow entrypoints are now skills in `.claude/skills/*/SKILL.md`. When you see `/profile-discover` or `/workflow-status`, that is the skill's `name`; it is invoked through the Skill tool, not through `.claude/commands/`.

## Resume Rule

When returning to any project, start with:

```text
/workflow-status content-workspace/<project-slug>
```

If you were working on a specific article:

```text
/workflow-status content-workspace/<project-slug> <article-slug>
```

The cockpit is read-only. It diagnoses progress, blockers, and the next safe skill. It never updates `state.json`, never creates artifacts, and never auto-runs the next step.

## How to Read the Cockpit

- `Current Position`: project, profile lock, active article, selected article, and timestamp.
- `Progress Bar`: the artifact graph from profile to review, with each layer marked `done`, `partial`, `todo`, or `blocked`.
- `QA Gate Status`: each QA file (`truth-qa.md`, `information-gain-qa.md`, `benchmark-drift-audit.md`, `reader-qa.md`) and whether it passes.
- `Blocking Issues`: what prevents the next stage from being safe.
- `Next Safe Skill`: the single skill to run next.
- `What You Can Ignore For Now`: later-stage files that should not distract you yet.
- `Article Queue`: every article workspace, its completion percentage, and its next skill.

## Common Stuck States

- No project workspace: run `/profile-discover` with the rough business seed.
- Draft profile exists but is not locked: stay in `/profile-answer`, `/article-cluster`, `/profile-research-deep`, or `/profile-lock`.
- Locked profile exists but no active article workspace: run `/workflow-status` to diagnose.
- An article has benchmarks but no skeleton: run `/article-skeleton`.
- A QA file is blocking: repair the article or evidence, then rerun the blocked QA skill.
- Publish artifacts are missing: do not publish; run `/article-publish-pack`.
- A post-publish review has not run: run `/article-review` 30/60/90 days after publishing.

## Relationship to `/article-next`

`/article-next` is a lightweight next-step hint. `/workflow-status` is the primary operator cockpit. Use `/workflow-status` when you are unsure where you are, when returning after time away, or when a project has multiple articles.

## Stop-Language

If a skill reports that required artifacts are missing, the profile is not locked, or the previous gate failed, stop immediately. Do not proceed by inventing context. Run the recommended skill or provide the missing input first.
