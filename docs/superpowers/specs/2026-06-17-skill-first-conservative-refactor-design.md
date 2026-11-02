# Skill-First Conservative Refactor Design

Date: 2026-06-17
Project: `b2b-seo-agent-system-v3-skills`

## 1. Product Goal

Make the existing B2B SEO agent system understandable, trustworthy, and maintainable without rebuilding it from scratch.

The first optimization pass must start with Skills. Each Skill should be judged as a product capability, not just a markdown file:

- Does it follow Anthropic's current Skill structure?
- Does its trigger description make clear when it should be used?
- Does its body contain only the instructions needed after the Skill is loaded?
- Does it belong to a clear business stage in the article production workflow?
- Does it produce or protect durable artifacts in the expected workspace?

The outcome should help a non-technical operator understand what the system is, where they are in the workflow, and why each Skill exists.

## 2. Evidence Base

This design is based on:

- Anthropic PDF: `The Complete Guide to Building Skills for Claude`, downloaded and read locally from `https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf`.
- Claude Code official Skills documentation: `https://code.claude.com/docs/en/skills`.
- Claude Code official memory documentation for `CLAUDE.md` and `AGENTS.md`: `https://code.claude.com/docs/en/memory`.
- Claude Code official extension overview: `https://code.claude.com/docs/en/features-overview`.
- Current repository inspection on 2026-06-17.

Important interpretation: official Anthropic guidance allows supporting files such as `scripts/`, `references/`, and `assets/`. This project may keep a stricter local convention where shared output templates live in the root `templates/` directory to avoid duplicate template drift.

## 3. Scope

### In Scope

1. Review all active Skills under `.claude/skills/*/SKILL.md`.
2. Classify Skills into product roles:
   - Main workflow Skills invoked by the operator.
   - Supporting knowledge Skills loaded by other Skills or agents.
   - Diagnostic/navigation Skills.
   - Legacy, duplicate, or unclear Skills to mark for later decisions.
3. Optimize Skill frontmatter and body structure where needed.
4. Check that Skill promises align with:
   - `config/workflow-spec.yaml`
   - `config/artifact-graph.yaml`
   - `config/state-schema.json`
5. Review Agent files only to ensure they are role/persona definitions and not hidden alternate SOPs.
6. Clarify the relationship between `AGENTS.md` and `CLAUDE.md`.
7. Extend validation only where it helps detect Skill-quality and product-architecture drift.
8. Produce a human-readable audit matrix explaining what changed and why.

### Out of Scope

1. No major workflow redesign.
2. No broad deletion or merging of Skills in the first pass.
3. No security-first permission hardening as the main objective.
4. No rewrite of the article production methodology unless a Skill clearly contradicts the locked workflow.
5. No live publishing, WordPress deployment, or external system changes.

## 4. Current Product Diagnosis

The repo already has the right high-level direction:

- Commands have been removed from the active Claude surface.
- Active workflow entrypoints are Skills.
- The project has a workflow spec, artifact graph, and state schema.
- Local validation currently passes.

The remaining risk is deeper than simple structure:

- Some Skills may be technically valid but not written as high-quality Skills.
- Some descriptions may trigger too broadly or fail to explain the business moment.
- Some long bodies may mix core instructions with detailed reference content that should be progressively disclosed.
- Some helper Skills may look like operator-facing Skills, or vice versa.
- `CLAUDE.md` and `AGENTS.md` currently overlap enough that they can drift unless one becomes the source of truth.
- The operator experience is still hard to read as one product system.

## 5. Target Architecture

### 5.1 Instruction Source of Truth

Recommended relationship:

- `AGENTS.md`: cross-platform product constitution and durable project rules.
- `CLAUDE.md`: Claude Code entrypoint that imports or mirrors `AGENTS.md` with only Claude-specific additions.

The design goal is not to make both files identical. It is to prevent two independent constitutions from slowly disagreeing.

### 5.2 Skill Roles

Every Skill should belong to one clear product role.

Main workflow Skills:
- Represent user-visible stages.
- Have `user-invocable: true`.
- Describe the business moment in plain language.
- State required inputs, output artifacts, stop points, and next expected action.

Supporting knowledge Skills:
- Have `user-invocable: false`.
- Provide reusable policy, writing guidance, search selection, or formatting logic.
- Keep detailed examples in `references/` when the body becomes large.

Diagnostic/navigation Skills:
- Help the operator recover context or decide the next safe action.
- Must clearly state that they diagnose rather than advance the workflow.

Unclear or legacy-like Skills:
- Should not be deleted immediately.
- Should be flagged in the audit matrix with a decision needed: keep, merge later, convert to reference, or retire later.

### 5.3 Agents

Agents should be specialized roles, not hidden workflows.

Each Agent should answer:

- What role does it play?
- Which business judgment is it responsible for?
- Which Skills does it rely on?
- What must it never do?

Detailed step-by-step execution should live in Skills, not Agents.

### 5.4 Config Files

The product map should be:

- `config/workflow-spec.yaml`: stage order and next-step logic.
- `config/artifact-graph.yaml`: required inputs and outputs.
- `config/state-schema.json`: allowed state shape.
- `AGENTS.md`: human-readable constitution.
- `CLAUDE.md`: Claude Code loading layer.
- `.claude/skills/*/SKILL.md`: executable user and agent workflows.
- `.claude/agents/*.md`: specialist roles.
- `templates/`: shared output templates.

## 6. Skill Review Criteria

Each Skill will be reviewed against these criteria.

### 6.1 Official Structure

- Folder name is kebab-case.
- Entry file is exactly `SKILL.md`.
- Frontmatter exists and parses.
- `name` matches the folder name.
- `description` includes both what the Skill does and when to use it.
- Frontmatter contains no XML angle brackets.
- Supporting files live in allowed project locations.
- No `README.md` exists inside Skill directories.

### 6.2 Trigger Quality

Descriptions should be specific enough for Claude to choose correctly:

- Good: "Use when benchmark candidates have been selected and you need to extract reader-advancement mechanisms and the benchmark asset ledger."
- Weak: "Helps with article work."

Each description should identify:

- The stage or business situation.
- The prerequisite condition.
- The expected outcome.
- Important trigger phrases if the Skill is operator-facing.

### 6.3 Progressive Disclosure

The Skill body should contain the core workflow only.

Move or keep detailed material in `references/` when:

- The content is long.
- The content is optional.
- The content is a lookup table, pattern library, or extended example.
- The content is only needed for one branch of the workflow.

### 6.4 Artifact Contract

Each main workflow Skill should clearly state:

- Required inputs.
- Files it creates or updates.
- State changes.
- Stop point.
- What it must not do.

This must match `artifact-graph.yaml` and `workflow-spec.yaml`.

### 6.5 Product Clarity

A non-technical operator should be able to answer:

- Why does this Skill exist?
- When should I run it?
- What will I get after running it?
- What should I review before continuing?
- What is the next Skill?

## 7. Implementation Plan After Approval

### Phase 1: Build Skill Audit Matrix

Create a human-readable matrix covering all 34 Skills:

- Skill name
- Role category
- Official structure status
- Trigger quality
- Body/progressive-disclosure status
- Artifact contract status
- Product clarity status
- Recommended action

This can be created as a markdown report under `docs/audit/`.

### Phase 2: Apply Low-Risk Skill Improvements

Edit Skills where improvements are clear and local:

- Tighten descriptions.
- Move repeated or bulky detail into `references/` only when clearly beneficial.
- Normalize purpose, argument contract, inputs, outputs, and stop points.
- Align wording with the workflow and artifact graph.
- Keep existing business methodology intact.

### Phase 3: Align Constitution Files

Update `AGENTS.md` and `CLAUDE.md` so their relationship is explicit:

- Avoid duplicated long sections where possible.
- Keep `AGENTS.md` as the cross-platform constitution.
- Keep `CLAUDE.md` as Claude Code's entrypoint and project map.

### Phase 4: Agent Role Check

Review the five active agents:

- Keep persona, expertise, and red lines.
- Remove or flag hidden SOP duplication if found.
- Ensure each agent references Skills rather than redefining the workflow.

### Phase 5: Validation

Run:

```bash
python3 scripts/validate_discovery_profile_workflow.py
python3 -m pytest tests/
python3 scripts/deep_audit.py
```

If validator improvements are added, run those too.

## 8. Acceptance Criteria

The pass is complete when:

1. Every Skill has a recorded audit outcome.
2. Every Skill either passes official-structure checks or has a documented reason and fix.
3. Main workflow Skills clearly state business moment, required inputs, outputs, stop point, and next step.
4. Supporting Skills are clearly not operator-facing.
5. No active Skill looks like a random documentation dump.
6. `AGENTS.md` and `CLAUDE.md` no longer read like two competing constitutions.
7. Agent files remain role definitions, not alternate execution manuals.
8. Validation commands pass.
9. The final report explains changes in product language.

## 9. Explicit Non-Goals

- Do not collapse the 34 Skills into a smaller set during this pass.
- Do not remove Agents unless a later review clearly proves they are obsolete.
- Do not optimize for security permissions unless a tool list directly prevents product clarity.
- Do not change the benchmark-led writing philosophy in this pass.
- Do not treat `deep_audit.py` passing as sufficient proof of product quality.

## 10. Open Implementation Notes

- Current working tree has existing uncommitted changes across Skills, agents, config, scripts, and tests. Implementation must preserve those changes and avoid reverting user work.
- The final audit should distinguish between current local state and older remembered state.
- If a Skill is compliant but confusing, mark it as a product-clarity issue rather than a technical failure.
- If official guidance and project convention differ, prefer the stricter project convention when it supports maintainability and does not violate Claude Skill behavior.
