# Skill-First Read-Only Audit

Date: 2026-06-17
Scope: `.claude/skills`, `.claude/agents`, `config/`, `CLAUDE.md`, `AGENTS.md`
Mode: read-only audit of active system files. No active Skill, Agent, config, or constitution file was changed.

## Executive Summary

The project is not structurally broken.

The current active surface is already close to the intended skill-only architecture:

- 34 active Skills.
- 5 active Agents.
- 0 active Commands.
- 21 workflow stages in `config/workflow-spec.yaml`.
- Every workflow stage has a matching Skill.
- Every artifact graph stage has a matching Skill.
- No forbidden `README.md`, lowercase `skill.md`, uppercase variant, or `templates/` directory exists inside active Skill folders.

The biggest risk is not official Skill format. The biggest risk is product readability:

1. Some Skills are valid but too heavy to understand quickly.
2. Some navigation/control Skills overlap in purpose.
3. `CLAUDE.md` and `AGENTS.md` overlap enough to drift.
4. A few Skill examples or labels contradict the stated user experience.

Recommendation: do not rewrite the system. Start with a small cleanup pass after approval, focused on clarity and official Skill quality.

## Evidence Checked

Official guidance used:

- Anthropic PDF: `The Complete Guide to Building Skills for Claude`.
- Claude Code Skills docs: `https://code.claude.com/docs/en/skills`.
- Claude Code memory docs: `https://code.claude.com/docs/en/memory`.
- Claude Code extension overview: `https://code.claude.com/docs/en/features-overview`.

Current repo checks run:

```bash
python3 scripts/deep_audit.py
python3 scripts/validate_discovery_profile_workflow.py
python3 -m pytest tests/
```

Observed baseline:

- `deep_audit.py`: `Total issues found: 0`
- workflow validator: `Validation passed.`
- pytest: `30 passed in 0.41s`

This proves the current structural/test baseline is green. It does not prove the product architecture is easy to understand.

## Official Skill Structure Result

Status: good.

All active Skills pass the important structural shape:

- Skill folders are under `.claude/skills/<skill-name>/SKILL.md`.
- Folder names are kebab-case.
- Each active Skill uses `SKILL.md` exactly.
- `name` matches the folder name.
- `description` exists.
- Descriptions are under 1024 characters.
- No XML angle brackets were found in frontmatter.
- No active Skill directory contains a forbidden `README.md`.
- No active Skill directory contains a forbidden `templates/` subfolder.
- Supporting folders found are limited to `references/` and `scripts/`.

Product meaning: the system is not failing at the basic Claude Skill packaging layer. The next improvement should be quality, not rescue.

## Product Architecture Findings

### Finding 1: The system has a good main spine

The workflow stages and Skill files align.

`workflow-spec.yaml` has 21 stages. All have matching Skills. The artifact graph stages also have matching Skills.

This means the main product journey exists:

`profile` -> `cluster` -> `benchmark` -> `evidence` -> `skeleton` -> `arc` -> `draft` -> `QA` -> `enrich` -> `publish` -> `review`

Decision: do not rebuild this sequence in the first cleanup pass.

### Finding 2: There are 13 Skills outside the canonical workflow stage list

These are not necessarily bad. Most are supporting knowledge Skills:

- `b2b-seo-article-sop`
- `benchmark-led-answerability`
- `benchmark-transmutation`
- `evidence-policy`
- `image-strategy`
- `internal-linking`
- `publish-package`
- `quality-gates`
- `search-toolbox`
- `structure-variation`
- `voice-and-humanization`
- `workflow-next`
- `workflow-rollback`

The first 11 read as support Skills. That is healthy.

The last 2 are different: `workflow-next` and `workflow-rollback` are user-invocable control Skills, but they are not clearly placed in the workflow product map.

Product risk: a non-technical operator may not understand whether these are official stages, emergency tools, or shortcuts.

Recommended later action: add a "workflow control" section to the product map instead of treating them like article stages.

### Finding 3: `article-next`, `workflow-status`, `workflow-next`, and `workflow-rollback` need clearer roles

Current intended roles seem to be:

- `/article-next`: lightweight recommendation.
- `/workflow-status`: full read-only status cockpit.
- `/workflow-next`: advance state after validation.
- `/workflow-rollback`: move backward and clean downstream artifacts.

This is a useful product set, but the naming makes them feel similar.

Specific issue: `article-next` says it is read-only, but its example says:

`Advancing stage to article-skeleton. Updated state.json successfully.`

That contradicts the stated purpose.

Product risk: this is exactly the kind of wording that makes the system feel unsafe or confusing, even if the code is fine.

Recommended later action: fix examples and add a short decision table:

- "Need quick hint?" -> `/article-next`
- "Need full recovery/status?" -> `/workflow-status`
- "Need to advance state?" -> `/workflow-next`
- "Need to go backward?" -> `/workflow-rollback`

### Finding 4: `CLAUDE.md` and `AGENTS.md` overlap about half their content

Measured result:

- `CLAUDE.md`: 113 lines.
- `AGENTS.md`: 110 lines.
- Rough equal-line overlap: about 50%.

This is not an immediate breakage. But it is a long-term drift risk.

Product risk: two files both look like the "constitution." A future agent may update one and forget the other.

Recommended later action: make `AGENTS.md` the cross-platform constitution and make `CLAUDE.md` the Claude Code loading/project-map layer. This should be done carefully, not as a bulk rewrite.

### Finding 5: Some Skills are too heavy for first-pass comprehension

Official Skill guidance favors progressive disclosure: keep `SKILL.md` focused and move detailed references into linked files when the body becomes large.

Skills over 200 body lines:

- `image-strategy`: 430 lines.
- `article-draft`: 273 lines.
- `article-enrich`: 252 lines.
- `internal-linking`: 228 lines.
- `article-arc`: 205 lines.

This is not automatically wrong. Complex Skills can be long. But these should be reviewed first for progressive disclosure.

Most important case: `image-strategy`.

It already has `references/`, but the main body is still 430 lines. It contains many reusable pattern libraries and examples that may be better as references.

Product risk: the Skill may be powerful but expensive to read and hard to maintain.

Recommended later action: do not rewrite content. First split only obvious reference material while preserving the operational rules.

### Finding 6: Agent files are currently acceptable

The 5 Agent files are short enough:

- 50 to 58 body lines each.
- Each declares skills.
- They mostly read as specialist roles, not full hidden workflows.

There is some procedural detail in agents, but not enough to justify an immediate refactor.

Decision: do not touch agents in the first cleanup batch unless a Skill change exposes a direct contradiction.

## Skill Audit Matrix

Legend:

- Official: Claude-style structure and frontmatter.
- Trigger: whether the description has a clear use moment.
- Body: whether progressive-disclosure review is needed.
- Product role: how the Skill fits the system.
- Action: recommended next step, not yet implemented.

| Skill | Product role | Official | Trigger | Body | Action |
|---|---|---:|---:|---:|---|
| `profile-discover` | Main workflow | Pass | Good | Good | Keep |
| `profile-answer` | Main workflow | Pass | Good | Good | Keep |
| `profile-research-deep` | Main workflow | Pass | Good | Good | Keep |
| `profile-lock` | Main workflow | Pass | Good | Good | Keep |
| `article-cluster` | Main workflow | Pass | Good | Good | Keep |
| `article-benchmark` | Main workflow | Pass | Good | Good | Keep |
| `article-benchmark-extract` | Main workflow | Pass | Good | Medium | Keep, later review for density |
| `article-evidence-opinions` | Main workflow | Pass | Good | Good | Keep |
| `article-skeleton` | Main workflow | Pass | Good | Good | Keep |
| `article-arc` | Main workflow | Pass | Good | Heavy | Later progressive-disclosure review |
| `article-draft` | Main workflow | Pass | Good | Heavy | Later progressive-disclosure review |
| `article-truth-qa` | QA workflow | Pass | Good | Good | Keep |
| `article-information-gain-qa` | QA workflow | Pass | Good | Good | Keep |
| `article-benchmark-qa` | QA workflow | Pass | Good | Good | Keep |
| `article-reader-qa` | QA workflow | Pass | Good | Good | Keep |
| `article-repair` | Repair workflow | Pass | Good | Good | Keep |
| `article-enrich` | Main workflow | Pass | Good | Heavy | Later progressive-disclosure review |
| `article-publish-pack` | Main workflow | Pass | Good | Good | Keep |
| `article-review` | Post-publish workflow | Pass | Good | Good | Keep |
| `article-next` | Navigation | Pass | Good | Good | Fix contradictory example later |
| `workflow-status` | Diagnostic cockpit | Pass | Good | Good | Keep, clarify relation to `article-next` later |
| `workflow-next` | Workflow control | Pass | Good | Good | Add to product map later |
| `workflow-rollback` | Workflow control | Pass | Good | Good | Add to product map later |
| `b2b-seo-article-sop` | Supporting knowledge | Pass | Good | Good | Keep |
| `benchmark-led-answerability` | Supporting knowledge | Pass | Good | Good | Keep |
| `benchmark-transmutation` | Supporting knowledge | Pass | Good | Good | Keep |
| `evidence-policy` | Supporting knowledge | Pass | Good | Good | Keep |
| `image-strategy` | Supporting knowledge | Pass | Dense | Very heavy | Highest priority progressive-disclosure review |
| `internal-linking` | Supporting knowledge | Pass | Good | Heavy | Later progressive-disclosure review |
| `publish-package` | Supporting knowledge | Pass | Good | Good | Keep |
| `quality-gates` | Supporting knowledge | Pass | Good | Good | Keep |
| `search-toolbox` | Supporting knowledge | Pass | Good | Good | Keep |
| `structure-variation` | Supporting knowledge | Pass | Good | Medium | Keep |
| `voice-and-humanization` | Supporting knowledge | Pass | Good | Medium | Keep |

## What Should Not Be Changed Yet

Do not start by deleting or merging Skills.

Do not rewrite the benchmark-led writing system.

Do not turn the first pass into permission/security hardening.

Do not make `deep_audit.py` the only quality definition.

Do not touch agents until Skill roles are clearer.

## Safe Next Step

If the operator approves, the safest first implementation batch is:

1. Fix only `article-next` wording and example contradiction.
2. Add a short workflow-control explanation to the product map.
3. Create or update a Skill-quality audit checklist so future reviews can detect the same problems.

Do not start with `image-strategy`, because it is large and important. Splitting it should be a separate, reviewable pass.

## Decision Needed

Before implementation, confirm one of these:

1. "Only fix navigation clarity first."
2. "Start with the constitution relationship between `AGENTS.md` and `CLAUDE.md`."
3. "Start with progressive disclosure for long Skills."
4. "Do not change anything yet; keep auditing."

Recommended choice: 1.
