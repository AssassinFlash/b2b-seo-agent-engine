# Authoring Standards for Skills and Agents

This project uses two instruction surfaces:

- **Skills**: reusable procedural knowledge and templates in `.claude/skills/`.
  - **User-invocable skills** (`user-invocable: true`): workflow entrypoints like `/profile-discover`, `/article-skeleton`.
  - **Policy skills** (`user-invocable: false`): loaded by agents/skills via the Skill tool — e.g. `voice-and-humanization`, `evidence-policy`.
- **Agents**: focused subagents for specialized work in `.claude/agents/`.

## TRACE Quality Model

Use TRACE for every skill and agent:

- Trust: no hidden side effects, no secret leakage, no unsafe borrowing or unsupported claims.
- Reliability: stable inputs, clear outputs, explicit stop points, friendly missing-input behavior.
- Adaptability: trigger conditions are specific enough to invoke when needed and avoid false positives.
- Convention: consistent frontmatter, naming, arguments, sections, templates, and artifact names.
- Effectiveness: output is directly usable in the artifact graph.

## Skill Rules

- Every `SKILL.md` must include `name` and `description` frontmatter.
- `name` uses lowercase letters, numbers, and hyphens.
- `description` starts with `Use when` and describes trigger conditions, not a workflow summary.
- User-invocable skills must include `argument-hint` and an `## Argument Contract` section explaining how to interpret `$ARGUMENTS`.
- Policy skills should include `user-invocable: false` and may omit `argument-hint`.
- Keep `SKILL.md` concise; move templates and heavy examples into supporting files.
- Reference supporting files explicitly so the agent knows when to load them.
- Reference workflow constants from `config/workflow-spec.yaml` instead of hardcoding numbers (e.g. benchmark count, Success Formula dimensions).
- Include guardrails when the skill can cause unsafe claims, benchmark misuse, or workflow drift.

## User-Invocable Skill Rules

- Every user-invocable skill must include `description`, `argument-hint`, and `user-invocable: true`.
- Every user-invocable skill must include an `## Argument Contract` section explaining how to interpret `$ARGUMENTS`.
- Skills create or update artifacts and then stop.
- Skills must never auto-run the next skill.
- Skills must check required upstream artifacts and route back when prerequisites are missing.
- Article skills must require a locked `project-profile` (`state.json` indicates `lockedProfile: true`).
- Skills must use explicit stop-language when prerequisites are missing: say exactly what is missing and which skill to run next.
- Every mutating skill must include a Phase 0 Plan Preview and a unified pause block before execution.

### Phase 0 Plan Preview

Before executing, output a structured plan with:

1. **Upstream Consumption Report**: what was read from upstream artifacts and what it means for this stage.
2. **Purpose & Success Criteria**: what "done and good" looks like.
3. **Steps & Deliverables**: concrete actions, output file names, and expected structures.
4. **Input Dependencies & Assumptions**: required files/info and what is being assumed.
5. **Risk & Boundaries**: what this stage does NOT do.
6. **Tool Strategy**: which skills will guide tool selection, not a laundry list of MCP tools.

### Unified Pause Block

Every pause must use this exact format:

```text
=== ⏸ 停止 · 等待你的指令 ===
允许的指令：
  · 批准 / 继续 — 按计划执行
  · 修改：[你的修改要求]
  · 跳过 — 跳过此阶段
  · 停止 — 终止
==========================
```

Wait for explicit approval before proceeding.

## Agent Rules

- Every agent must include `name`, `description`, `tools`, `model`, and `color` frontmatter.
- `name` uses lowercase letters and hyphens.
- `description` must clearly state when to use the agent.
- Each agent has one primary responsibility.
- Tool access should be limited to what the agent needs.
- Agents must state inputs, outputs, guardrails, and pass/block behavior when applicable.
- Agents should preload required policy skills via the `skills:` frontmatter list.

## Workflow v3.0

The article workflow was redesigned into a skill-only, spec-driven system:

1. **No `.claude/commands/` directory**: all entrypoints are `.claude/skills/*/SKILL.md`.
2. **Single source of truth**: `config/workflow-spec.yaml`, `config/artifact-graph.yaml`, `config/state-schema.json`.
3. **Benchmark count fixed at 3** user-selected articles; candidate pool size is 5.
4. **Success Formula uses 21 dimensions**: 15 mandatory + 5 optional + Prose Craft.
5. **Voice and humanization unified** in `voice-and-humanization` skill.
6. **Section contracts embedded** in `skeleton.md`; no standalone `article-section-contracts` skill.
7. **Deprecated agents removed** rather than kept with DEPRECATED tags.

Full workflow: `cluster → benchmark(pause) → benchmark-extract(pause) → evidence-opinions(pause) → skeleton(pause) → arc(pause) → draft(pause) → QA gates → enrich(pause) → publish-pack → review`

## Project-Specific Non-Negotiables

- Do not treat depth, linearity, or stop gates as defects.
- Do not create generic SEO factory behavior.
- Do not let Answerability override benchmark-led writing.
- Do not let borrowed benchmark assets masquerade as owned facts.
- Do not draft without section contracts.
- Do not publish without Truth QA, Information Gain QA, Benchmark Drift QA, and Reader QA.
- Decision-critical sections must be anchored by Tier 1 evidence when proprietary proof changes the buyer's judgment. Transition, pacing, setup, reframing, and reader-bridge sections may exist without forced Tier 1 proof.
- Read the **full benchmark article**, not a sample, before drafting.
- Draft from an article-specific Numeric Control Vector: exact imitation / injection / differentiation percentages plus AIO, bold, opinion, evidence, H2, and format-repetition controls. The numbers steer execution; they are not fake quality scores.
- Do not write content that a competitor could reproduce by swapping the brand name. Every article must contain information only this business can provide.

## Template Files

Template files (under `templates/` or skill `references/`) may omit YAML frontmatter. They are supporting material, not invocation surfaces. If a template is meant to be filled by an agent, the calling skill or agent must describe the expected output format and file path.

## Information Gain Principle

Mannlee Case Reference (2025-2026): A B2B door manufacturer achieved 16K monthly organic traffic through well-written informational blog content. Google's March 2026 Core Update introduced Information Gain as a central ranking metric. Mannlee's traffic collapsed because their content contained zero information that only their factory, team, or projects could provide. A competitor could replace "Mannlee" with their own brand name on any article and 80%+ of the content would remain valid.

This case establishes a binding precedent: **content that does not leverage the business's unique expertise, data, or operations is not worth producing — regardless of how well it is written.**
