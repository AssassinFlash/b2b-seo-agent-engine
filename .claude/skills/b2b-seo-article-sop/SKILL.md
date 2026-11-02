---
name: b2b-seo-article-sop
description: "Use when: (1) orienting to the full article workflow, (2) checking which skill comes next, (3) understanding artifact dependencies between stages. The canonical article production workflow — maps each stage to its skill, artifact outputs, and pause checkpoints. Updated for v3.0 (skill-only, benchmark from best-in-class, voice system, structure variation, one-shot drafting)."
user-invocable: false

---

# B2B SEO Article SOP (v3.0)

## Purpose

Provide the canonical map of article production stages. Updated for v3.0: skill-only invocation, 3 selected benchmarks from a 5-article candidate pool, 21-dimension Success Formula, 4-gate QA, and publish packaging.

## When to Use

- Recovering context after time away from a project
- Checking artifact dependencies before running a skill
- Understanding what a stage produces and what it requires

## Workflow v3.0

| Stage | Skill | Key Artifacts | Pause? |
|---|---|---|---|
| 1. Discover | `/profile-discover` | `project-profile.draft.md`, `state.json` | ⏸ answer discovery questions |
| 2. Answer | `/profile-answer` | updated `project-profile.draft.md`, `state.json` | ⏸ if more questions needed |
| 3. Topic Cluster | `/article-cluster` | `topic-cluster.md`, `topic-card.md` | ⏸ review topic pool and pick first article |
| 4. Deep Research | `/profile-research-deep` | `project-profile.research.md` | ⏸ if research gaps remain |
| 5. Lock Profile | `/profile-lock` | `project-profile.md`, `project-profile.json` | ⏸ approve locked profile |
| 6. Intent Research | `/article-intent-research` | `intent-research.md` | ⏸ approve research plan |
| 7. Benchmark Library | `/article-benchmark` | `content-type-library.md`, `benchmark-candidates.md` | ⏸ user selects 3 primary exemplars |
| 8. Success Formula | `/article-benchmark-extract` | `benchmark-success-formula.md`, `benchmark-asset-ledger.md` (21 dimensions) | ⏸ Peer Co-Research |
| 9. Evidence + Opinions | `/article-evidence-opinions` | `evidence-opinion-pack.md` | ⏸ Peer Co-Research |
| 10. Differentiated Skeleton | `/article-skeleton` | `skeleton.md` with embedded section contracts | ⏸ Peer Co-Research |
| 11. Narrative Arc | `/article-arc` | `narrative-arc.md` (6 nodes) | ⏸ Peer Co-Research |
| 12. Draft | `/article-draft` | `draft.md` (pure prose) | ⏸ Peer Co-Research |
| 13. Truth QA | `/article-truth-qa` | `truth-qa.md` | ⏸ Peer Co-Research (block if failed) |
| 14. Information Gain QA | `/article-information-gain-qa` | `information-gain-qa.md` | ⏸ Peer Co-Research (block if failed) |
| 15. Benchmark Drift QA | `/article-benchmark-qa` | `benchmark-drift-audit.md` | ⏸ Peer Co-Research (block if failed) |
| 16. Reader QA | `/article-reader-qa` | `reader-qa.md` | ⏸ Peer Co-Research (block if failed) |
| 17. Repair | `/article-repair` | `repair-plan.md`, updated `draft.md` | ⏸ diagnosis, ⏸ rewrite plan |
| 18. Enrich | `/article-enrich` | `enriched-draft.md`, `image-plan.md`, optional `html-visual-plan.md` | ⏸ open-ended component proposal & sample |
| 19. Visual | `/article-visual` | `visual-spec.md`, `visual/` | ⏸ Peer Co-Research |
| 20. Resources & Navigation | `/article-resources` | `resources.md` (open-ended interactive/callout/routing modules) | ⏸ Peer Co-Research |
| 21. Objection & Friction Layer | `/article-faq` | `faq.md` (friction resolution & conversion modules) | ⏸ Peer Co-Research |
| 22. Publish Pack (Handoff Draft) | `/article-publish-pack` | `publish-package.md`, `schema.json`, `keyword-record.csv`, `site-link-graph.json` | ⏸ handoff draft for external citation tool |
| 23. Performance Review | `/article-review` | `performance-review.md` | ⏸ review findings (30/60/90 days post-publish) |

## Retired Skills

For the history of retired v1.0 commands, see `docs/history/v1-to-v2-changelog.md`.

## Core Skills Referenced

- `voice-and-humanization` — 4-lens opinion processing + bold usage
- `structure-variation` — reader-state → Markdown structure mapping
- `image-strategy` — article visual need, dynamic visual mix, image roles, and option mechanism
- `article-html-visuals` — embedded HTML expression blocks, visual explainers, static fallbacks, and render checks
- `visual-material-hunt` — source-backed article visual assets, product photos, platform media, and marketplace image candidates for `image-strategy`
- `internal-linking` — link roles, accordion blocks, reader-stage routing
- `evidence-policy` — Tier 1/2/3 source classification
- `quality-gates` — 4-gate QA system
- `benchmark-transmutation` — borrowed asset ledger rules
- `benchmark-led-answerability` — answerability structures + source checks
- `article-skeleton` — per-section contract fields embedded in skeleton.md
- `publish-package` — publishing asset checklist

## Supporting Templates

- `templates/deep-seo-card.md` — 14-field Deep SEO Card template used for the selected first-article `topic-card.md`. Includes 5-dimension weighted scoring section.

---

## Guardrails

- Never skip a pause checkpoint — every stage requires user approval before advancing
- Never run article skills without a locked profile
- Never draft without an approved skeleton and arc
- QA gates have blocking authority — a single BLOCK stops progression

---

## Examples

### Input (user asks):
```
"What comes after /article-skeleton?"
```

### Output:
```
Next command: /article-arc
Requires: skeleton.md (user-approved)
Produces: narrative-arc.md (6 nodes + arc-to-skeleton mapping)
Pause: yes — user reviews the arc before drafting
Status check: run /workflow-status content-workspace/project-slug article-slug
```

### Input (user asks):
```
"What skills should I use when writing?"
```

### Output:
```
Drafting: voice-and-humanization + structure-variation (pure prose)
Enrichment (post-QA): image-strategy + article-html-visuals + visual-material-hunt + article-visual-fit + internal-linking (visual expression, sourcing, fit review, nav layer)
QA gates: evidence-policy + quality-gates (verification)
```

## Instructions

Execute the steps described in the canonical sequence.
