---
name: article-truth-qa
description: "Use when: the draft exists and you need Gate 1 Truth QA. Supports strict mode and light/non-blocking mode. Default to evidence-pack-based verification unless external new claims, safety-critical claims, or user instructions require strict multi-source re-verification."
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
---

# /article-truth-qa

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Before QA, verify: `project-profile.md` exists, `state.json` indicates `lockedProfile: true`, `draft.md` exists, `evidence-opinion-pack.md` exists.

## Purpose

Gate 1 of 4. Verify that the draft stays inside its evidence boundaries. The upstream `evidence-opinion-pack.md` already performs the main fact-gathering and source verification; this gate's default job is **not** to redo that research. Its job is to catch obvious contradictions, profile red-line violations, unsupported draft-born claims, unsafe extrapolations, and numerical/unit/comparative/safety errors that the draft introduced.

Truth QA should protect factual support without flattening the article. Strong stance is allowed — even encouraged under the performance-first doctrine — when it is supportable or clearly marked as judgment. Truth QA does **not** exist to make good copy conservative; it exists to prevent unsupported claims from masquerading as fact.

## Modes

### Light / Non-Blocking Mode (`--light`, `--non-blocking`)

Use when the operator explicitly wants a fast pass or when the upstream evidence pack is already trusted. In light mode:

- Rely on `evidence-opinion-pack.md` Tier 1 / Tier 2 mappings; do not re-run full external research.
- Read `Draft Control Metadata` and focus on its **Truth QA Watchlist**.
- Check obvious contradictions, profile red lines, and draft-born claims that are so unsupported they would damage the article.
- Keep performance-first hooks and quantified stance when they are plausible and not obviously contradicted. Put them on a watchlist rather than blocking by default.
- Write the report's scope honestly: `Mode: Light / non-blocking pass`. Do not claim every fact was independently reverified.
- PASS unless there is a clear red-line violation, impossible claim, dangerous safety claim, or obvious contradiction with the evidence pack.

### Strict Mode (default unless `--light` is specified)

Use when the draft contains new external standards, safety-critical claims, fresh numerical claims not in the evidence pack, or when the operator asks for rigorous verification. Strict mode performs the full claim-by-claim verification and may spawn subagents for external checks.

## Instructions

**Main context**: read the draft, cross-reference claims against the evidence pack, write the QA report.

`Draft Control Metadata` is QA metadata, not publishable body copy. Read it for control context, but do not audit its numeric controls as factual article claims.

**Subagent for external verification** (strict mode only; spawn if needed): If a claim references an external standard or source not in the evidence pack, spawn a subagent and let it use the `search-toolbox` skill to choose tools and fallbacks. Cross-reference at least two independent sources from different backends. In `--light` mode, do not spawn unless a claim is safety-critical or obviously dangerous.

**Skills to load**: `evidence-policy` (Tier classification, evidence labels, minimums), `quality-gates` (Gate 1 criteria, output template at `templates/truth-qa.md`), `search-toolbox` (complete tool inventory with decision logic and fallback chains — read BEFORE any external verification).

**Verification protocol** — Multi-Tool Serial Verification with multi-backend redundancy. Use the `search-toolbox` skill to select the right tool at each step. Start with broad search, escalate to full-page extraction, and use structured-data extraction for specs, certifications, and thresholds.

**2-source minimum rule**: Every external claim must be verified against at least 2 independent sources from different backends. One source = `weak`. Zero sources = `unverified` → BLOCK.

---

### Required Checks

1. Every factual claim maps to evidence or is removed/weakened
2. Draft-born claims are listed and resolved
3. Borrowed data keeps source, region, year, scope boundaries
4. Borrowed case patterns are not presented as owned cases
5. Red lines from `project-profile.md` §5 enforced
6. Tier 3 claims flagged (detailed check deferred to Gate 2)
7. **Visual truth check** — if the article contains generated or synthesized visuals, verify the visual's labels, numbers, model names, and interface counts match the evidence pack. AI-generated visuals must be image-to-image only with a real base image; pure text-to-image product visuals are not allowed.
8. **NEW**: All numerical calculations audited for arithmetic correctness
8. **NEW**: All units consistent and comparable
9. **NEW**: All comparative claims ("highest", "best", "lowest", "fastest") re-validated against corrected data
10. **NEW**: All safety-critical specifications verified against authoritative sources
11. **NEW**: All `upstream-revision-suggestions.md` items followed up
12. **Glossary, Allowed Materials & Industry Baseline Guard**:
    - Verify customer-facing text contains zero `forbiddenTerms` from `project-profile.json` / `project-profile.md` (e.g., never calling a `pattern` a `product`, never calling an `inquiry` an `order/cart`).
    - Verify the draft never claims the brand manufactures materials outside `allowedMaterials` (e.g., if the project only fabricates `Stainless Steel (304 / 316)`, never offer Aluminum, Brass, or Corten as our catalog options).
    - Verify competitor research and industry averages are explicitly framed as **Industry Baselines / Reference Averages**, never misrepresented as our own factory measurements (`竞品调研和行业平均值只作参照，不得写成我方实测`), and customer-facing downloads never link to third-party domains.

### Calculation & Units Verification Protocol

Extract every number, formula, percentage, and unit from the draft into a numbered `calculation-audit` table. Independently recalculate each derived value from its stated inputs. Check unit consistency across comparisons:

- Energy vs power: `kWh` vs `kW`
- Cost rates vs total cost: `$/kWh` vs `$/kW` vs `$`
- Peak vs continuous vs nominal ratings
- Per-unit vs aggregate quantities
- Currency, time period, and regional scope

Flag any arithmetic discrepancy >5% as BLOCK. Flag any unit mismatch as BLOCK, even if the numeric value happens to be close. For compound units (e.g., efficiency percentages, CAGR, ROI), verify both the numerator and denominator trace to the evidence pack.

If a calculation depends on a draft-born assumption, label it `draft-born` and resolve per the draft-born claim procedure.

### Comparative Claim Re-Validation

Find every superlative and comparative adjective in the draft: "highest", "best", "lowest", "fastest", "most efficient", "cheapest", "largest", "smallest", "leading", "first", "only", and any explicit or implicit ranking.

For each comparative claim:

1. Identify the comparison set (region, year, product category, metric)
2. Re-verify against the evidence pack after S5 corrections
3. Confirm the claim remains true under the corrected comparison set

BLOCK if the claim is no longer true after arithmetic, unit, or boundary corrections. Weaken or re-scope the claim rather than pass a false comparative.

### Safety-Critical Spec Check

Identify any claim touching safety, warranty, compliance, fire risk, structural load, electrical ratings, health, or regulatory approval.

Require 2+ independent authoritative sources for each safety-critical claim. Authoritative sources include manufacturer datasheets, official certification bodies, recognized standards organizations, or regulator publications. Marketing pages and press releases do not count as authoritative for safety-critical specs.

BLOCK on single-source safety claims. Never pass a safety, warranty, or compliance claim that cannot be independently confirmed.

### Upstream Revision Follow-Up

If `upstream-revision-suggestions.md` exists in the article workspace, read it and verify each item was implemented in the current draft.

For each suggestion record:

- `implemented`: confirmed in draft — pass
- `not implemented` but `accepted`: BLOCK and route to `/article-repair` or the upstream stage that produced the suggestion
- `rejected` with documented reason: note in the QA report, but do not block on reasoned rejection

If the file does not exist, continue. If it exists and is non-empty, the presence of unimplemented accepted suggestions is a BLOCK.

### Pass/Block

**Strict mode**

- **BLOCK**: unverified claim, borrowed case as owned, red-line violation, arithmetic discrepancy >5%, unit mismatch, comparative claim invalidated by corrected data, single-source safety claim, unimplemented accepted upstream revision suggestion.
- **PASS**: all claims verified/weakened, draft-born resolved, red lines clear, calculations independently verified, units consistent, comparatives hold under corrected data, safety-critical claims backed by 2+ authoritative sources, upstream revision suggestions addressed.

**Light / non-blocking mode**

- **BLOCK only**: clear red-line violation, impossible claim, dangerous safety claim, obvious contradiction with the evidence pack, or a draft-born claim that cannot be plausibly framed as judgment/estimate.
- **PASS with watchlist**: pack-backed claims are consistent, draft-born estimates are plausible but not independently reverified, strong stance is supportable as judgment, and no obvious contradiction exists.
- Light mode may leave `watchlist` items for later editorial / strict QA without blocking the workflow.

## Output

Write `articles/<article-slug>/truth-qa.md`.

The report must include:

- `Mode` and `Scope` at the top. If run with `--light`, explicitly state that the report relies on upstream evidence and does not independently reverify every claim.
- `Pack-Backed Claim Mapping`: the major claim families mapped to evidence pack anchors.
- `Draft-Born Claim Watchlist`: performance-first hooks, estimates, or strong stance claims that are plausible but not independently reverified.
- A dedicated section titled `Calculation / Units / Comparative / Safety Findings` that contains:
  - `calculation-audit` table with original value, recalculated value, delta, status (strict mode), or accepted evidence-anchor / watchlist status (light mode)
  - `unit-mismatch` findings
  - `comparative-claim` re-validation list
  - `safety-critical-spec` checklist with source counts or evidence-pack anchors
  - `upstream-revision-follow-up` status

Update `state.json`: `currentStage: article-truth-qa`, `nextCommand: /article-information-gain-qa` if PASS, or route to `/article-repair` if BLOCK.

## Examples

### Example 1: Truth QA Run
输入: `/article-truth-qa content-workspace/steel-screen screen-article`
输出: `truth-qa.md generated. Status: PASS (14 claims verified, 0 unreferenced assertions, calculations and units verified, 0 safety single-sources).`

### Example 2: Truth QA Block
输入: `/article-truth-qa content-workspace/solar-inverter inverter-article`
输出: `truth-qa.md generated. Status: BLOCK — unit mismatch ($/kW used as $/kWh) and 1 single-source fire-safety claim. Route to /article-repair.`

## Guardrails

- **Exact Mapping**: Every assertion of fact must map directly to a numbered evidence point from the project profile.
- **No Extrapolations**: Reject any claim that goes beyond the literal findings of the verified evidence pack.
- **Independent Recalculation**: Never trust a draft's derived number without recalculating it.
- **Unit Parity Before Comparison**: Two numbers are comparable only after their units and scopes are normalized.
- **Safety Redundancy**: Safety-critical claims require two independent authoritative sources — no exceptions.

## PAUSE

```
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，按计划推进
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
```

Wait for explicit approval before proceeding.
