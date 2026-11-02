# Workflow Process Audit — Sunriver Inverter B2B SEO Project

**Audit date:** 2026-06-24  
**Auditor:** Kimi Code CLI  
**Scope:** Reverse-engineer the legacy S4 workflow operations that produced the four S4 artifacts, compare them with the current v3 skill-based workflow, and recommend system-level improvements to workflow, skills, templates, and processes.  
**Related audits (already on file):**
- `benchmark-workflow-audit.md` — S4 success-formula patterns vs. current `benchmark-success-formula.md`.
- `s4-headings-content-audit.md` — Legacy S4 heading/content artifact integration recommendation.

This report is intentionally one level higher: it looks at *operations*, not only article-level content.

---

## Executive Summary

The legacy S4 workflow was a four-phase, human-in-the-loop content architecture process:

1. **Ingredient gathering** — heading libraries, content checklists, knowledge-gap flags, benchmark URLs, buyer-voice mining.
2. **Forensic benchmark analysis** — deep reading of 2–3 best-in-class articles, raw observations, synthesis into a small playbook of tactics.
3. **Outline construction** — apply the playbook to the ingredients, producing a draft-ready H2/H3 skeleton with paragraph contracts, callouts, and visual cues.
4. **Process reflection** — document what worked, what failed, and why the benchmark mix mattered.

The current v3 workflow systematizes most of this into a skill-based pipeline (`article-benchmark` → `article-benchmark-extract` → `article-evidence-opinions` → `article-skeleton` → `article-arc` → `article-draft` → four QA gates → `article-enrich` → `article-publish-pack`). It adds strong governance (locked profile, 21-dimension extraction, `benchmark-asset-ledger.md`, Truth/Information-Gain/Benchmark-Drift/Reader QA gates) and removes the risk of turning a single agent monologue into an outline.

However, the S4 workflow contained operational scaffolding that v3 has not fully preserved:

- **Writer-ready execution templates** (`Why → How → Verify`, `[WARNING]/[IMPORTANT]/[PRO TIP]` taxonomy, visual pairing rules, launchpad conclusion).
- **Pre-skeleton ingredient pack** (standalone heading library + content checklist + knowledge-gap register produced *before* skeleton work).
- **Research burden estimation** (explicit hours-per-product and scope sizing).
- **Competitor brand profiling** (for comparison/buyer's-guide articles).
- **Process reflection / benchmark-selection rationale capture** (the S4 Phase 4 learnings).

**Highest-leverage fixes:** fold the S4 execution templates into `/article-benchmark-extract` output (the "Writer's Playbook"), add an optional `knowledge-gap-register.md` artifact, add a lightweight `process-retrospective.md` template, and add research-burden/effort fields to the Deep SEO Card / topic card. These are low-effort, high-impact upgrades that do not require new workflow stages.

---

## S4 Operation Inventory

| # | Operation Name | Inputs | Outputs | Tool / Technique | Purpose / Value | v3 Stage Equivalent |
|---|---|---|---|---|---|---|
| 1 | **SERP / competitor heading extraction** | Primary keyword; top-ranking pages | Secondary Heading Library (15–18 H2s) with reader-question type, buyer intent, content angle | SERP scrape / H2 extraction; question-type taxonomy | Generate an outline candidate pool grounded in real search results | `/article-skeleton` Phase 1 — Secondary Heading Library |
| 2 | **Article-type & buyer-journey classification** | Heading library, keyword intent, SERP landscape | Article type (e.g., "Ranked List + Buyer's Guide Hybrid"); awareness → evaluation → comparison → decision → action journey | Heuristic taxonomy; pattern matching | Decide what structural pattern the article should follow | `/article-benchmark` Phase 1 (10-type taxonomy) + `/article-benchmark-extract` Reader Advancement Mechanism |
| 3 | **Brand / competitor profile research** | Product names, datasheets, market reports, pricing data | Per-brand profiles: specs, pros/cons, best-for, price/kWh | Datasheet review; price research; web search | Fuel comparison tables and scenario recommendations | Partially in `/profile-research-deep` and `/article-evidence-opinions` for SAJ; **no generic competitor-brand profiling operation** |
| 4 | **Content requirement checklist compilation** | Heading library, buyer journey, brand profiles, regulatory topics | Grouped checklist (market context, technical foundation, brand profiles, comparison matrix, scenarios, installation, regulatory) | Thematic synthesis; completeness audit | Ensure no decision-critical topic is omitted | Distributed across `evidence-opinion-pack.md`, `skeleton.md` section contracts, and (newly recommended) `benchmark-success-formula.md` checklist |
| 5 | **Knowledge gap flagging** | Brand profiles, technical terms, claims made in planning | Register of 60+ unverified specs, terms, and claims | Source-gap analysis; assumption marking | Create a pre-writing evidence risk register for the fact-checker | Inline in `/article-evidence-opinions` verification status + `/article-truth-qa` blockers; **no standalone pre-research register** |
| 6 | **Benchmark source curation** | Article type, topic, best-in-class domain list | 3–5 benchmark URLs with scrape requests and value notes | Best-in-class domain search; expert curation | Seed the success-formula analysis with the right sources | `/article-benchmark` → `benchmark-candidates.md` |
| 7 | **Buyer-voice forum mining** | Topic keywords; Reddit / installer forums | Real buyer decision factors, pain points, misconceptions | Reddit/forum search; thematic coding | Ground headings and warnings in actual buyer language | `/article-evidence-opinions` Phase 2b + `/article-skeleton` Phase 1 (Reddit/forums channel) |
| 8 | **Regulatory & incentive inventory** | Market, product category, jurisdiction | ITC, SGIP, state incentives, net metering, codes (NEC, EU Battery Regulation) | Official-source search | Provide freshness anchors and decision context | `/profile-research-deep` source library + `/article-evidence-opinions` fact inventory |
| 9 | **Research burden estimation** | Product count, scope, verification depth | Estimated hours (e.g., 8 products × 1 hr), words per product, fact-checker load | Scope sizing; analogous estimation | Allow resource planning and scope control | `/article-cluster` word-count/difficulty scoring; **no explicit time/effort estimate** |
| 10 | **Thematic heading clustering (how-to)** | Competitor guides, SEO tools, installer forums | Theme-based heading library (e.g., Pre-Installation, Safety, Physical Install, Wiring, Commissioning) | Thematic analysis; journey mapping | Build procedural-guide structure | `/article-skeleton` Phase 1 |
| 11 | **Tools / materials / safety checklist extraction** | Install guides, manuals, field documentation | Tools list, PPE list, critical safety warnings | Manual extraction; checklist compilation | Ensure procedural accuracy and safety coverage | Inline in `/article-evidence-opinions` + `/article-skeleton` section contracts; **no dedicated checklist artifact** |
| 12 | **Forum mistake / pitfall mining** | Installer forums, Reddit, support threads | Common mistakes (CT orientation, firmware updates, grounding, etc.) | Community search; pattern extraction | Generate credible `[PRO TIP]` and `[WARNING]` content | `/article-evidence-opinions` buyer-voice research |
| 13 | **Benchmark selection across model types** | Topic, desired intellectual depth | A deliberate mix of models (e.g., Logical Command / Strategic Workflow / Physical Action) | Expert curation; cross-industry search | Avoid simplistic benchmark choice that produces generic outline | `/article-benchmark` selects 3 same-type candidates; **no explicit multi-model mix rule** |
| 14 | **Forensic benchmark deep reading** | Selected benchmark URLs | Raw observation files per benchmark | Full-article immersive reading; pixel-level deconstruction | Identify specific tactics that make the benchmark work | `/article-benchmark-extract` 21-dimension extraction |
| 15 | **Cross-article pattern synthesis** | Raw observations from 2–3 benchmarks | Unified Success Formula / Playbook (5 tactics or 21 dimensions) | Comparative synthesis; abstraction | Convert observations into reusable structural rules | `/article-benchmark-extract` Structural Blueprint + Reader Advancement Mechanism |
| 16 | **Paragraph / visual / callout template extraction** | Raw benchmark observations | `Why → How → Verify` loop; `[WARNING]/[IMPORTANT]/[PRO TIP]` taxonomy; `One Action, One Image` rule; expectation-setting opener; launchpad conclusion | Structural pattern extraction; visual heuristic | Give `/article-skeleton` reusable section and paragraph contracts | **Missing** — only partially addressed by the Writer's Playbook recommendation in `benchmark-workflow-audit.md` |
| 17 | **Iterative correction / dialectical refinement** | First formula/outline; operator feedback | Improved formula/outline | Human-AI debate; pivot on failure | Raise quality through structured disagreement | Implicit in v3 stop/approval pauses; **not explicit as a methodology** |
| 18 | **Outline construction from formula + ingredients** | Success formula, heading library, content checklist, evidence notes | Final H2/H3 outline with paragraph contracts and callouts | Synthesis; formatting | Produce a draft-ready skeleton | `/article-skeleton` + `/article-arc` |
| 19 | **Visual / diagram planning** | Outline steps; benchmark visual patterns | Image/diagram placeholders (e.g., clearance diagram, wiring diagram, app screenshots) | Visual design heuristics | Feed `/article-enrich` and `image-plan.md` | `/article-skeleton` visual hints + `/article-enrich` `image-plan.md`; **no visual playbook in success formula** |
| 20 | **Benchmark selection rationale capture** | Selected benchmarks, pivot reasons, discarded alternatives | Documentation of why the mix was chosen | Reflective documentation | Enable future audits and avoid repeating bad benchmark choices | **Missing** |
| 21 | **Process reflection & learning capture** | Stage execution outcomes, failures, corrections | Phase 4 Process Summary with codified learnings | Retrospective; lessons-learned capture | Improve methodology over time | **Missing** |

---

## v3 Coverage Matrix

| S4 Operation | Covered in v3? | Where / How | Gap Severity |
|---|---|---|---|
| 1. SERP / competitor heading extraction | ✅ Full | `/article-skeleton` Phase 1 explicitly produces a 15+ candidate heading library. | None |
| 2. Article-type & buyer-journey classification | ✅ Full | `/article-benchmark` 10-type taxonomy + `/article-benchmark-extract` Reader Advancement Mechanism + `/article-arc` 6-node arc. | None |
| 3. Brand / competitor profile research | ⚠️ Partial | SAJ product evidence is gathered in `/profile-research-deep` and `/article-evidence-opinions`. There is no standardized operation for profiling *competitor* brands in comparison/buyer's-guide articles. | Medium |
| 4. Content requirement checklist compilation | ⚠️ Partial | Requirements are embedded per section in `/article-skeleton` and in the recommended `benchmark-success-formula.md` checklist. No standalone Phase-1 artifact. | Low |
| 5. Knowledge gap flagging | ⚠️ Partial | Verification status lives in `evidence-opinion-pack.md` and QA blockers. No standalone pre-research knowledge-gap register. | Medium |
| 6. Benchmark source curation | ✅ Full | `/article-benchmark` → `benchmark-candidates.md`, pool of 5, user selects 3. | None |
| 7. Buyer-voice forum mining | ✅ Full | Required in `/article-evidence-opinions` Phase 2b and used in `/article-skeleton` Phase 1. `search-toolbox` / `agent-reach` routes are documented. | None |
| 8. Regulatory & incentive inventory | ✅ Full | Locked into `project-profile.md` source library and verified in `/article-evidence-opinions`. | None |
| 9. Research burden estimation | ❌ Missing | No explicit hours/effort estimate per article or per product. | Low–Medium |
| 10. Thematic heading clustering | ✅ Full | `/article-skeleton` Phase 1 supports multi-channel heading research and thematic grouping. | None |
| 11. Tools / materials / safety checklist extraction | ⚠️ Partial | Checklist items become section-contract fields, but there is no dedicated artifact for procedural how-to guides. | Low |
| 12. Forum mistake / pitfall mining | ✅ Full | Handled by buyer-voice research in `/article-evidence-opinions`. | None |
| 13. Benchmark selection across model types | ⚠️ Partial | v3 selects best-in-class sources but does not explicitly require a *mix of structural models* (e.g., command + workflow + physical). | Medium |
| 14. Forensic benchmark deep reading | ✅ Full | `/article-benchmark-extract` mandates denoising and 21-dimension extraction. | None |
| 15. Cross-article pattern synthesis | ✅ Full | Unified Structural Blueprint + Reader Advancement Mechanism in `/article-benchmark-extract`. | None |
| 16. Paragraph / visual / callout template extraction | ⚠️ Partial | Current extraction is analytical; writer-ready paragraph and callout templates are not a required output. | High |
| 17. Iterative correction / dialectical refinement | ⚠️ Partial | Stop/approval pauses exist, but no skill frames the first proposal as a "starting point for debate." | Low |
| 18. Outline construction from formula + ingredients | ✅ Full | `/article-skeleton` + `/article-arc`. | None |
| 19. Visual / diagram planning | ⚠️ Partial | `/article-enrich` produces `image-plan.md`, but the success formula does not systematically extract benchmark visual patterns. | Medium |
| 20. Benchmark selection rationale capture | ❌ Missing | No required artifact documents why these benchmarks were chosen or what each contributes. | Low–Medium |
| 21. Process reflection & learning capture | ❌ Missing | No stage or template captures per-stage learnings or failure pivots. | Medium |

---

## Gap Analysis

### Theme 1 — Writer-ready execution templates are under-specified

The S4 workflow produced a small, high-leverage playbook: `Why → How → Verify`, `[WARNING]/[IMPORTANT]/[PRO TIP]`, `One Action, One Image`, expectation-setting opener, launchpad conclusion. These are concrete enough to drop into `skeleton.md` section contracts.

v3's `/article-benchmark-extract` extracts 21 dimensions and a Structural Blueprint, but the output is still largely analytical. A downstream `/article-skeleton` agent must translate dimensions into paragraph templates. This translation step is where quality often leaks.

**System-level risk:** Without required execution templates, every `/article-skeleton` run reinvents paragraph contracts, callout usage, and visual pairing. This produces inconsistent drafts and makes QA gates spend cycles catching the same missing patterns.

### Theme 2 — Pre-skeleton ingredient pack is fragmented

S4 Phase 1 produced one file containing headings, content checklist, knowledge-gap flags, benchmark URLs, and buyer voice. v3 distributes these across `article-benchmark`, `article-evidence-opinions`, and `article-skeleton`. That distribution is correct for governance, but it removes the *standalone scoping artifact* that a project lead can review before committing to a deep outline.

**System-level risk:** For complex articles (how-to, multi-brand comparison), the absence of a single pre-skeleton ingredient pack makes it harder to spot scope creep or missing evidence early.

### Theme 3 — No standardized competitor brand profiling

The legacy S4 Phase 1 built full profiles for 7 competitor brands plus SAJ. v3 avoids competitor SERP cloning, which is correct, but for articles whose topic *is* a comparison (e.g., "Best All-in-One ESS 2025"), competitor profiling is legitimate research, not copying. v3 has no template or skill for it.

**System-level risk:** Future comparison articles either skip necessary competitive context or recreate ad-hoc research spreadsheets outside the workflow.

### Theme 4 — Research burden is not estimated

S4 explicitly estimated research time (8 products × 1 hour). v3 scores opportunity and difficulty but does not estimate hours. This makes sprint planning and client/resource allocation harder.

**System-level risk:** Articles are selected by opportunity score alone, without a realistic view of research cost.

### Theme 5 — Process reflection and benchmark rationale are not captured

S4 Phase 4 documented why the benchmark mix was chosen, the failed first formula, and the dialectical refinement that saved the outline. v3 has no equivalent artifact. Lessons learned stay in the conversation context and are lost for the next article.

**System-level risk:** The workflow does not learn. Repeated benchmark-selection mistakes or outline failures are not institutionalized.

### Theme 6 — Visual playbook is implicit

S4's success formula included specific visual rules (`One Action, One Image`, annotated screenshots, diagrams, meta box). v3 handles visuals later in `/article-enrich` and `image-strategy`, but the success formula does not systematically extract visual patterns from benchmarks.

**System-level risk:** Visual planning becomes reactive rather than benchmark-informed, leading to missing diagrams or generic stock imagery.

---

## Prioritized Recommendations

### High Impact / Low Effort (Do Immediately)

#### 1. Require a Writer's Playbook section in `/article-benchmark-extract` output
- **What to change:**
  - `.claude/skills/article-benchmark-extract/SKILL.md` — add a new output subsection under "Output Format" requiring a `Writer's Playbook` inside `benchmark-success-formula.md`.
  - Add `templates/benchmark-writers-playbook.md` as a reusable template.
  - Optionally update `templates/benchmark-asset-ledger.md` to reference the playbook.
- **Why it improves the workflow:** Translates 21-dimension analysis into reusable paragraph contracts, callout rules, and visual cues before `/article-skeleton` begins. Reduces reinvention and QA rework.
- **Implementation sketch:**
  - Add the following required subsections to `benchmark-success-formula.md` output:
    1. `Paragraph Contract: Why → How → Verify`
    2. `Callout Taxonomy: [WARNING] / [IMPORTANT] / [PRO TIP]`
    3. `Visual Contract` (diagram/table/image rules)
    4. `Expectation-Setting Opener Block`
    5. `Launchpad Conclusion Block`
  - The existing `benchmark-workflow-audit.md` already drafted concrete copy for these subsections; use it as the seed.

#### 2. Add an optional `knowledge-gap-register.md` article artifact
- **What to change:**
  - `config/artifact-graph.yaml` — add `articles/<article-slug>/knowledge-gap-register.md` as an optional output of `/article-evidence-opinions`.
  - `config/state-schema.json` — add optional `knowledgeGaps` array under article items.
  - `.claude/skills/article-evidence-opinions/SKILL.md` — require producing the register *before* Phase 2b external verification when the article type is How-To, Buyer's Guide, or Comparison.
  - Add `templates/knowledge-gap-register.md`.
- **Why it improves the workflow:** Creates a standalone pre-research risk register that mirrors S4's "Knowledge Gap Flags." Project leads can review it before committing to drafting.
- **Implementation sketch:**
  - Template columns: Claim/Spec, Current Status (verified / assumption / needs-external / blocked), Source Needed, Owner (profile / evidence-opinions / truth-qa), Risk Label (low/medium/high).
  - `/article-truth-qa` can read the register and confirm all `needs-external` items are resolved or flagged.

#### 3. Add research-burden / effort-estimate fields to the Deep SEO Card and topic card
- **What to change:**
  - `templates/deep-seo-card.md` — add `Estimated Research Hours` and `Estimated Production Hours` fields.
  - `templates/section-contracts.md` — optionally add a `Research effort` field.
  - `.claude/skills/article-cluster/SKILL.md` — populate the new fields using product count, evidence depth, and verification difficulty.
- **Why it improves the workflow:** Brings S4-style research burden estimation into topic selection and sprint planning.
- **Implementation sketch:**
  - Simple formula: base 2 hrs + (entities to profile × 0.5–1.5 hrs) + (external verifications × 0.5 hr).
  - Mark estimates as `[estimated]` and let `/profile-research-deep` refine them.

### High Impact / Medium Effort (Plan as Workflow Improvement)

#### 4. Create a `competitor-brand-profile.md` template and optional operation
- **What to change:**
  - Add `templates/competitor-brand-profile.md`.
  - Update `.claude/skills/article-evidence-opinions/SKILL.md` to spawn a subagent or section when `article-type` is Comparison, Buyer's Guide, or Cost Guide.
  - Update `config/artifact-graph.yaml` to list `articles/<article-slug>/competitor-brand-profiles.md` as optional.
- **Why it improves the workflow:** Standardizes the competitor profiling that S4 did ad-hoc, while keeping it governed by the evidence-policy and benchmark-asset-ledger.
- **Implementation sketch:**
  - Template fields: Brand, Product/Model, Specs, Pros/Cons, Best-for, Price Positioning, Source URL, Risk Label, How We'll Transform It.
  - Rule: competitor facts must be transformed into Sunriver's supply-partner perspective and recorded in `benchmark-asset-ledger.md` if borrowed.

#### 5. Add a visual-playbook extraction requirement to `/article-benchmark-extract`
- **What to change:**
  - `.claude/skills/article-benchmark-extract/SKILL.md` — add a "Visual Patterns" dimension (or fold into Dim 15 / Prose Craft) requiring extraction of:
    - Image-to-action pairing rules
    - Annotated screenshot / diagram conventions
    - Meta-box / expectation-block conventions
    - Table vs. prose choices for comparisons
  - Add `templates/visual-playbook.md`.
- **Why it improves the workflow:** Makes visual planning benchmark-informed rather than reactive.
- **Implementation sketch:**
  - Output a `Visual Playbook` section in `benchmark-success-formula.md` with: `Visual Type`, `Benchmark Source`, `When to Use`, `Transformation Rule`, `Alt-Text Pattern`.
  - `/article-enrich` reads this section when building `image-plan.md`.

#### 6. Add a lightweight process-retrospective artifact
- **What to change:**
  - Add `templates/process-retrospective.md`.
  - Update `config/artifact-graph.yaml` to make `articles/<article-slug>/process-retrospective.md` an optional output of `/article-skeleton`, `/article-arc`, or `/article-publish-pack`.
  - Update `.claude/skills/article-skeleton/SKILL.md` and `.claude/skills/article-arc/SKILL.md` to prompt the agent to append 3–5 bullets capturing pivots, benchmark mix rationale, and lessons.
  - Update `AGENTS.md` to document the optional retrospective.
- **Why it improves the workflow:** Preserves S4 Phase 4 learning-capture without adding a mandatory stage.
- **Implementation sketch:**
  - Template prompts: What was the hardest structural decision? What benchmark mix was chosen and why? What failed and how was it corrected? What should the next article do differently?

### Medium Impact / Low Effort

#### 7. Add a benchmark-selection rationale field to `benchmark-candidates.md`
- **What to change:**
  - `.claude/skills/article-benchmark/SKILL.md` — require a one-line "Why this mix" rationale for the final 3 selected candidates.
  - Update `templates/benchmark-asset-ledger.md` to include a `Selection Rationale` section.
- **Why it improves the workflow:** Captures S4's "benchmark selection is the single most influential decision" lesson in a lightweight way.

#### 8. Add an explicit "dialectical refinement" protocol to skills with high creative risk
- **What to change:**
  - `.claude/skills/article-benchmark-extract/SKILL.md` and `.claude/skills/article-skeleton/SKILL.md` — add a note: "The first proposal is a well-researched starting point for debate, not a final answer."
  - Add a prompt in the PAUSE block asking the operator: *Does this feel like the right depth? Any section that could be simplified or enriched?*
- **Why it improves the workflow:** Codifies S4's most important cultural lesson without adding process friction.

### Low Impact / Document and Defer

#### 9. Revive the full S4-style "ingredient pack" as an optional pre-skeleton stage
- **What to change:**
  - New optional skill `.claude/skills/article-ingredients/SKILL.md` (or sub-section of `/article-skeleton`) that produces `articles/<slug>/ingredient-pack.md`.
  - `config/artifact-graph.yaml` optional artifact.
- **Why it might help:** For complex how-to or multi-brand comparison articles, a single Phase-1 scoping file reduces fragmentation.
- **Why it is deferred:** v3 already distributes the same content across existing skills; adding a new stage risks redundancy.

#### 10. Add a standalone procedural checklist template for how-to articles
- **What to change:**
  - Add `templates/procedural-checklist.md`.
- **Why it might help:** S4 produced excellent tools/materials/safety checklists for installation guides.
- **Why it is deferred:** The section-contract format in `templates/section-contracts.md` can already hold checklist fields; a separate template is only justified if how-to volume grows.

---

## Implementation Roadmap

### Week 1 — Immediate Wins
1. Update `article-benchmark-extract/SKILL.md` to require the Writer's Playbook (§1 above).
2. Create `templates/benchmark-writers-playbook.md`.
3. Update `templates/deep-seo-card.md` with research-burden fields (§3 above).
4. Update `article-cluster/SKILL.md` to populate the new fields.

### Week 2–3 — Risk & Reflection Artifacts
1. Create `templates/knowledge-gap-register.md`.
2. Update `config/artifact-graph.yaml` and `state-schema.json` to list the new optional artifacts.
3. Update `article-evidence-opinions/SKILL.md` to produce the register for complex article types.
4. Create `templates/process-retrospective.md` and add optional prompts to `article-skeleton` and `article-arc`.
5. Update `AGENTS.md` to mention the new optional artifacts.

### Month 2 — Specialized Article Types
1. Create `templates/competitor-brand-profile.md`.
2. Update `article-evidence-opinions/SKILL.md` to invoke competitor profiling for Comparison / Buyer's Guide / Cost Guide articles.
3. Add visual-playbook extraction to `article-benchmark-extract/SKILL.md` and create `templates/visual-playbook.md`.
4. Update `article-enrich/SKILL.md` to read the visual playbook when building `image-plan.md`.

### Month 3 — Validation
1. Run the updated workflow on the next Sunriver article (likely a comparison or how-to topic).
2. Compare new artifacts against the S4 files to confirm the workflow now captures the missing scaffolding.
3. Update `templates/` and `AGENTS.md` based on findings.

---

## Risks

### Risks of Implementing

| Risk | Mitigation |
|---|---|
| **Scope creep** — adding too many optional artifacts bloats every article | Make all new artifacts optional and gated by article type or operator request. |
| **Template rigidity** — Writer's Playbook could be applied mechanically | Emphasize in the skill that the playbook is a default; benchmark-native rhythm and `structure-variation` still override it. |
| **Approval friction** — extra outputs slow the workflow | Keep new artifacts short (1–2 pages) and append them to existing files where possible (e.g., Writer's Playbook inside `benchmark-success-formula.md`). |
| **State-schema bloat** | Add new fields as optional only; do not make them required for `state.json` validation. |

### Risks of Not Implementing

| Risk | Consequence |
|---|---|
| **Inconsistent draft quality** | Without Writer's Playbook, every `/article-skeleton` agent reinvents paragraph contracts, leading to repeated QA failures. |
| **Loss of tacit knowledge** | Without process retrospectives, the S4 Phase 4 learnings (benchmark selection, dialectical refinement, surgical enrichment) are not transferred to new agents. |
| **Scope surprises** | Without research-burden estimates, high-opportunity topics with heavy research costs may be selected without resource planning. |
| **Weak comparison articles** | Without competitor-brand profiling, future comparison pieces lack standardized research depth or drift into competitor cloning. |
| **Reactive visuals** | Without a visual playbook, enrichment relies on ad-hoc decisions, reducing the chance of benchmark-informed diagrams and callouts. |

---

## Final Note

The v3 workflow is already stronger than the legacy S4 workflow in governance, repeatability, and QA discipline. The gaps identified here are not failures — they are opportunities to fold the best operational scaffolding from S4 (writer-ready templates, pre-research risk registers, research burden estimation, and learning capture) into the v3 system without losing its analytical rigor.

The highest-leverage next step is **Recommendation 1**: make the Writer's Playbook a required output of `/article-benchmark-extract`. This single change would have prevented most of the usability gaps noted in `benchmark-workflow-audit.md` and would give `/article-skeleton` a direct, repeatable path from benchmark analysis to section contracts.

No files were modified in the production of this report.
