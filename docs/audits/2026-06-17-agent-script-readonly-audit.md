# Agent and Script Read-Only Audit

Date: 2026-06-17
Scope: `.claude/agents/`, `scripts/`, `tests/`, and their links to Skills/config.
Mode: read-only audit. No active Agent, Skill, script, config, or constitution file was changed.

## Executive Summary

The user's concern is valid: the first audit was Skill-first and did not deeply inspect Agents or scripts.

This second audit finds:

- Agent layer is mostly healthy and compact.
- Script layer is functional and tested for the main paths, but it contains deeper product-architecture risks than the Agent layer.
- The biggest risk is not "bad code." The biggest risk is mismatched product meaning: some script names, Skill descriptions, and validator names suggest one role while the actual behavior is broader.

Most important script finding:

`scripts/workflow_status.py` is both:

1. A read-only status cockpit renderer.
2. A state mutation tool for `--next` and `--rollback`.

This can be valid, but the product language must make that dual role explicit. Otherwise an operator may believe a "status" tool is always read-only when it can also write state and delete downstream artifacts under flags.

## Inventory

### Agents

Active Agents:

| Agent | Body lines | Declared Skills | Role |
|---|---:|---:|---|
| `content-repair-strategist` | 51 | 5 | QA block diagnosis and repair strategy |
| `performance-review-strategist` | 50 | 2 | 30/60/90 day performance review |
| `publish-package-qa` | 50 | 1 | Final publish package audit |
| `publish-readiness-agent` | 50 | 1 | Publish package creation |
| `topic-cluster-researcher` | 58 | 3 | Topic pool and Deep SEO Card research |

### Scripts

Active scripts:

| Script | Lines | Tested | Product role |
|---|---:|---:|---|
| `deep_audit.py` | 403 | No direct unit test | Structural audit of commands, agents, skills, templates, docs, config |
| `denoise_html.py` | 41 | Yes | Strip boilerplate HTML before benchmark extraction |
| `run_qa_verifier.py` | 426 | Yes | Deterministic four-gate QA report generator |
| `sync_draft_born_claims.py` | 69 | Yes | Move verified draft-born claims into fact library |
| `validate_discovery_profile_workflow.py` | 537 | Indirect | Workflow, Skill, Agent, artifact, and acceptance validator |
| `workflow_status.py` | 752 | Yes | Status cockpit plus workflow state mutation for next/rollback |

Observed test references:

- `denoise_html.py` -> `tests/test_denoise_html.py`
- `run_qa_verifier.py` -> `tests/test_qa_verifier.py`
- `sync_draft_born_claims.py` -> `tests/test_sync_draft_born_claims.py`
- `workflow_status.py` -> `tests/test_workflow_status.py`
- `validate_discovery_profile_workflow.py` -> indirectly referenced by `tests/test_workflow_status.py`
- `deep_audit.py` -> no direct unit test found

## Agent Findings

### Finding A1: Agent frontmatter is structurally healthy

All active Agents have:

- `name`
- `description`
- `tools`
- `skills`
- `model`
- `memory`
- `color`

All declared Skills exist.

No immediate Agent frontmatter breakage was found.

### Finding A2: Agents are mostly role definitions, not alternate full workflows

This is good.

The five Agents are short and mostly define:

- persona
- judgment area
- red lines
- output expectations

They do not currently look like massive hidden SOPs. This means the system is already close to the desired "Skills hold workflow, Agents hold role" model.

### Finding A3: Some Agent language still carries legacy migration residue

Examples:

- `content-repair-strategist`: "Adapted from legacy Codex_1118 S8.5..."
- `topic-cluster-researcher`: "Adapted from Legacy Codex_1118 S3."

This is not a functional bug.

Product risk: it makes the v3 system feel like a patched migration rather than a clean current product. For a non-technical operator, this weakens trust.

Recommended later action: replace legacy-origin language with a short current-product purpose statement, but do not change the Agent's behavior.

### Finding A4: Agent roles are useful but should be shown in the product map

The current product map explains Skills better than Agents.

Recommended later action: add a small Agent role table to the human-facing system map:

- `topic-cluster-researcher`: used by `/article-cluster`
- `content-repair-strategist`: used by `/article-repair`
- `publish-readiness-agent`: used by `/article-publish-pack`
- `publish-package-qa`: used after publish package generation
- `performance-review-strategist`: used by `/article-review`

This would make Agents feel intentional rather than hidden.

## Script Findings

### Finding S1: `workflow_status.py` has mixed product roles

The script name says status, but the file supports three modes:

- default: render read-only status cockpit
- `--next`: mutate `state.json` to advance workflow
- `--rollback`: mutate `state.json` and delete downstream artifacts

The Skill layer partly recognizes this split:

- `/workflow-status` calls the script for read-only status.
- `/workflow-next` calls the same script with `--next`.
- `/workflow-rollback` calls the same script with `--rollback`.

This is technically workable, but product language needs to be clearer.

Risk: an operator may think `workflow_status.py` is always read-only. It is only read-only in default mode.

Recommended later action: do not split the file yet. First update documentation/product map to say:

- `workflow_status.py` is the workflow navigator engine.
- `/workflow-status` uses its read-only mode.
- `/workflow-next` uses its state-advance mode.
- `/workflow-rollback` uses its rollback-cleanup mode.

### Finding S2: `validate_workflow_status_read_only()` is now semantically stale

Inside `validate_discovery_profile_workflow.py`, the function `validate_workflow_status_read_only()` validates the `workflow-status` Skill's read-only rules, but also explicitly allows `workflow_status.py` writes/deletes for `--next` and `--rollback`.

This is not necessarily a runtime bug.

Product risk: the validator name no longer matches what it validates. It creates confusion for future maintainers.

Recommended later action: rename or document this validator conceptually as "workflow status default mode is read-only; navigator mutation modes are restricted."

### Finding S3: `sync_draft_born_claims.py` has high product significance

This script reads `truth-qa.md`, extracts "Draft-born Claims," and writes them into:

`knowledge/fact-library.json`

It stores claims with:

```json
{
  "source_article": "...",
  "claim": "...",
  "status": "verified_draft_born"
}
```

This is useful because it can create a reusable fact library.

But it is also risky as a product concept:

- It assumes "Draft-born Claims" in Truth QA are already verified.
- It gives them a verified-looking status.
- Downstream `article-evidence-opinions` treats `knowledge/fact-library.json` claims as Tier 1 reusable facts.

Product risk: if a Truth QA section contains weak or unclear draft-born claims, the system can accidentally promote them into reusable evidence.

Recommended later action: keep the script, but tighten the product contract before relying on it:

- Define exactly what qualifies as "Draft-born Claims."
- Confirm whether they must be manually approved before sync.
- Consider status names like `draft_born_pending_review` vs `verified_draft_born` if approval is not explicit.

Do not change this script until the business meaning is confirmed.

### Finding S4: `run_qa_verifier.py` is valuable but heuristic

The script creates:

- `qa-report.json`
- `qa-report.md`
- `truth-qa.md`
- `information-gain-qa.md`
- `benchmark-drift-audit.md`
- `reader-qa.md`

It checks:

- evidence markers
- unverified numeric/spec claims
- Tier 1 evidence density
- competitor replaceability using Tavily or local source library
- benchmark structure drift
- AI filler phrases
- AIO and visual monotony soft warnings

This is a strong deterministic layer, but it is still heuristic.

Product risk: users may read "deterministic QA" as "truth guaranteed." It is better understood as "automated blocking and warning layer before human review."

Recommended later action: adjust human-facing language from "guarantees quality" to "catches common quality failures and forces review."

### Finding S5: `denoise_html.py` is small and correctly placed, but dependency visibility is weak

The script depends on `beautifulsoup4`.

If missing, it exits with a message.

It has a unit test and a clear role in `/article-benchmark-extract`.

Product risk: low. The only improvement would be documenting the dependency in the tool/runtime guide.

### Finding S6: `deep_audit.py` is useful but not enough

`deep_audit.py` scans structural consistency across commands, agents, skills, templates, docs, and config.

It has no direct unit test.

Product risk: because this script reports `Total issues found: 0`, users may over-trust it as a complete product-quality audit.

Recommended later action: keep it, but label it as a "structural audit," not a "product architecture audit."

### Finding S7: generated/cache files exist under scripts/tests

Observed local files:

- `scripts/.DS_Store`
- `scripts/__pycache__/...`
- `tests/.DS_Store`
- `tests/__pycache__/...`

These are not active system logic.

Product risk: low, but they make the repository look less clean to non-technical review.

Recommended later action: ignore/clean these only when doing repository hygiene. Do not mix this with product architecture changes.

## Script-to-Skill Alignment

| Script | Referenced by | Alignment |
|---|---|---|
| `workflow_status.py` | `/workflow-status`, `/workflow-next`, `/workflow-rollback` | Works, but product naming should clarify read-only vs mutation modes |
| `run_qa_verifier.py` | `/workflow-next`, tests, Phase 2 design | Works, but should be framed as heuristic deterministic guardrail |
| `denoise_html.py` | `/article-benchmark-extract`, tests | Good fit |
| `sync_draft_born_claims.py` | `/article-publish-pack`, tests, evidence workflow | Useful but product contract needs confirmation |
| `validate_discovery_profile_workflow.py` | `CLAUDE.md`, `AGENTS.md`, tests | Useful, but contains stale naming around read-only validation |
| `deep_audit.py` | `CLAUDE.md`, `AGENTS.md`, read-only audits | Useful structural audit, not complete product audit |

## Risk Ranking

High product risk:

1. `sync_draft_born_claims.py` promoting claims into `fact-library.json` without a clearly documented human approval boundary.
2. `workflow_status.py` combining read-only and mutation behavior under a status-oriented name.

Medium product risk:

1. Validator naming drift in `validate_workflow_status_read_only()`.
2. Overstating deterministic QA as if it guarantees article truth/quality.
3. Legacy-origin wording in Agent descriptions.

Low product risk:

1. `deep_audit.py` lacks direct unit tests.
2. `denoise_html.py` dependency is not prominently documented.
3. `.DS_Store` and `__pycache__` files are present locally.

## Recommended Next Step

Do not modify scripts yet.

The safest next action is a clarification pass, not code changes:

1. Add a human-readable "Agent and Script Map" to the project docs.
2. Clarify that `workflow_status.py` is the workflow navigator engine with read-only and mutation modes.
3. Clarify the approval boundary for `sync_draft_born_claims.py` before any code or Skill changes.

If implementation is later approved, start with documentation and examples, not script rewrites.

## Decision Needed

Before changing any active file, confirm which risk matters most:

1. "Make Agent and Script roles visible in docs first."
2. "Clarify workflow status / next / rollback behavior first."
3. "Clarify draft-born claims and fact-library approval first."
4. "Keep auditing; do not change anything."

Recommended choice: 1, then 3.
