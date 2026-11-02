---
description: "Use when: one or more QA gates have blocked and you need a structured diagnosis and rewrite plan followed by re-running the blocking gate."
argument-hint: '[content-workspace/project-slug] [article-slug]'
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
name: article-repair
---

# /article-repair

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Before repair, verify: `project-profile.md`, `state.json` indicates `lockedProfile: true`, `draft.md` exists, at least one QA file exists with BLOCK status.

## Purpose

QA gates can BLOCK — but they diagnose problems, they don't prescribe cures. This skill delegates root cause diagnosis to `content-repair-strategist` (Opus), then executes the approved repair plan.

## Instructions

**Phase 1 — Diagnosis**: Spawn **content-repair-strategist** [Opus] as a subagent. This agent reads all blocking QA files, the benchmark success formula, the skeleton, the arc, and the evidence pack. It produces `repair-plan.md`. Subagent context keeps diagnostic reasoning isolated from repair execution.

**Phase 2 — Repair**: Main context executes the approved plan.

**Skills to load**: `benchmark-transmutation` (formula re-sync), `structure-variation` (format audit), `voice-and-humanization` (Part 2), `search-toolbox` (tool selection if benchmark articles need re-reading).

---

### Phase 0 — Plan Preview

Present: which gate(s) blocked, preliminary assessment of repair scope (targeted/structural/full), whether the benchmark formula needs re-examination.

```
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，按计划推进
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
```

Wait for explicit approval.

---

### Phase 1 — Root Cause Diagnosis (Agent)

Spawn **content-repair-strategist** [Opus] with: `draft.md`, all blocking QA files, `benchmark-success-formula.md`, `skeleton.md`, `narrative-arc.md`, `evidence-opinion-pack.md`.

Agent outputs `repair-plan.md` with:
1. **Failure Summary** — which gates, which checks
2. **Root Cause Analysis** — per-failure trace to upstream artifacts
3. **Benchmark Re-Sync Notes** — formula still valid?
4. **Section-by-Section Rewrite Plan** — Problem / Root Cause / **Rewrite Strategy** / Repair Action / Priority table
5. **Repair Scope Recommendation** — targeted / structural / full with justification
6. **Post-Repair Gate Sequence** — which gates to re-run in order

### Rewrite Strategy Menu

The repair plan must choose one or more concrete rewrite strategies — not a vague "improve section" instruction. Use this menu adapted from the self-media rewrite prompt collection, translated for B2B SEO:

| Strategy | Use when | Repair action |
|---|---|---|
| **Structure reconstruction** | The section order or hierarchy causes the reader to lose the thread | Reorder section jobs, move the decision rule earlier, convert list → framework or framework → checklist |
| **Perspective shift** | The section sounds supplier-centric or abstract | Rewrite from buyer view / installer view / procurement view / homeowner risk view |
| **Content concretization** | Claims are accurate but flat, generic, or non-memorable | Add specific numbers, named hardware, scenario, cost range, quote line, or field-language translation (only if supportable) |
| **Logic reordering** | The reasoning reaches the right conclusion too late | Convert explanation → answer-first; move consequence before mechanism; use counterexample before rule |
| **Format conversion** | The current format hides the reader job | Convert prose → table, table → decision tree, checklist → red-flag list, FAQ → direct answer block |
| **RAG Citation Chunk reconstruction** | Question H2 opening relies on dangling pronouns ("it", "this mode") or buries the conclusion | Rewrite the first 40–60 words of the H2 into a self-contained chunk (Explicit Subject Entity + Condition + Bold Verdict + Quantified Metric) |
| **Buying Committee & Anti-Sell injection** | Section sounds like a one-way sales pitch or ignores CFO/Procurement sign-off | Add an Anti-Sell Disqualification Boundary (when NOT to buy) and/or an Internal Champion 30-Second TCO & Risk Ledger |
| **Language optimization** | The logic is right but the prose reads AI-generic | Apply `voice-and-humanization`: shorter paragraphs, full-sentence bold anchors, stance vs hype boundary, Named Engineer field voice, benchmark transitions |

For each blocked section, the repair-plan table should include a `Rewrite strategy` column with one or more of these strategy names.

---

### Phase 2 — Review Repair Plan

Present `repair-plan.md`. User reviews, challenges, adjusts.

```

## Examples

### Example 1: Creating Content Repair Plan
输入: `/article-repair content-workspace/steel-screen screen-article`
输出: `repair-plan.md created. Rewriting sections H2-03 and H2-05 to inject Tier 1 factory evidence.`

## Guardrails

- **Zero-Overwrite**: Keep the original draft and assets intact during repair. Update only the targeted section blocks.
- **Re-Audit Gate**: All repaired sections must be re-run through the blocked QA verifier to ensure the block is cleared.

=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，按计划推进
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
```

Wait for explicit approval.

---

### Phase 3 — Execute Repair

- **Targeted** (1-3 sections): Edit specific sections in `draft.md`
- **Structural** (3+ sections): Rewrite full article in one pass, preserving intact prose
- **Full re-draft**: Return to `/article-draft` Phase 2 after re-anchoring style

Update draft-born claims if new claims added.

---

### Phase 4 — Re-run Blocking Gates

Re-run the gate(s) that blocked. If still BLOCK → return to Phase 1.

Do NOT proceed until all previously-blocking gates PASS.

---

## Output

Create `articles/<article-slug>/repair-plan.md`. Update `articles/<article-slug>/draft.md` with `## Repair Notes`. Update `state.json`.
