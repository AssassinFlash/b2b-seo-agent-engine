# S4 Headings & Content Audit — Legacy Artifact Integration Recommendation

**Artifact audited:** `S4_Phase1_BestAllInOneSystems2025_Secondary_Headings_and_Content.md`  
**Current article:** `solar-without-a-battery`  
**Audit date:** 2026-06-23  
**Auditor:** v3 workflow agent  

---

## 1. Artifact Diagnosis

### 1.1 What it is
The legacy file is a **pre-outline content ingredient pack** from an older S4 workflow ("Codex_1118 V22"). It was produced by a "Success Formula Architect" agent for a **different article topic**: *"Best All-in-One Energy Storage System for Residential Use in 2025: Top 7 Brands Compared."*

Its function is to gather raw heading candidates, content requirements, and research gaps **before** the final article structure is locked and before fact-checking begins.

### 1.2 Content sample and format

| Section | Format | Purpose |
|---------|--------|---------|
| **Secondary Heading Library** | 18 H2 candidates with reader-question type, buyer intent, content angle | SERP / competitor heading inventory for outline design |
| **Content Requirement Checklist** | Checkbox inventory per topic: market context, technical foundation, 8 brand profiles, comparison matrix, scenarios, installation, regulatory | Research scope and completeness checklist |
| **Knowledge Gap Flags** | 60+ unverified specs, terms, claims to be validated by an S5 fact researcher | Pre-writing evidence risk register |
| **Research Sources Identified** | Benchmark URLs + scrape requests, competitor brand list, Reddit/forum buyer questions | Source library seed and competitive set |
| **Phase 1 Completion Summary** | Article type classification, buyer journey, SAJ positioning notes, research burden estimate | Handoff summary to next phase |

### 1.3 Content type classification
This is **SERP heading scrapes + competitor H2/H3 inventory + content gap analysis + brand-specific research checklist**. It is **not** a success formula (it does not extract *why* a benchmark article works) and **not** a final outline (it does not assign section contracts, voice lenses, or rhythm).

---

## 2. Current v3 Workflow Mapping

### 2.1 Is there an equivalent stage or artifact?

**Yes.** The current v3 workflow has a direct equivalent inside `/article-skeleton`:

- **`/article-skeleton` Phase 1 — "Secondary Heading Library (multi-channel H2 research)"** explicitly states: *"Adapted from Codex_1118 V22 S4 Phase 1."*
- The skill requires production of *"a Secondary Heading Library of 15+ H2 candidates, each tagged with: proposed H2 text, source channel, reader question type, and relevance (keep/modify/discard)."*
- This output is appended to `skeleton.md` as raw material that feeds into Phase 2 structure extraction.

### 2.2 Where each legacy component maps

| Legacy S4 Component | v3 Equivalent Location | Notes |
|---------------------|------------------------|-------|
| Secondary Heading Library (18 H2s) | `/article-skeleton` Phase 1 output → `skeleton.md` appendix | Direct functional equivalent |
| Content Requirement Checklist | `/article-evidence-opinions` Part 2 (Fact Inventory) + `/article-skeleton` section-contract "Evidence anchors" | v3 embeds requirements per section rather than as a flat checklist |
| Knowledge Gap Flags | `/article-evidence-opinions` verification status + `/article-truth-qa` blockers | v3 tracks evidence state inline rather than in a standalone pre-research register |
| Research Sources Identified | `/article-benchmark` → `benchmark-candidates.md` + source library | v3 captures this earlier and ties it to selected benchmarks |
| Article type / buyer journey summary | `/article-benchmark-extract` → `benchmark-success-formula.md` §1.3 + §6 Reader Advancement Mechanism | v3 version is benchmark-derived, not assumption-derived |

### 2.3 What `/article-benchmark-extract` already covers

`/article-benchmark-extract` extracts the **success formula** from user-selected benchmarks across 21 dimensions. The current `benchmark-success-formula.md` for `solar-without-a-battery` already contains:

- Cross-article pattern synthesis
- Dimension-by-dimension extraction (Core Promise, Reader State, Question Ladder, Section Function, etc.)
- Structural Blueprint (borrowable section-job sequence)
- Reader Advancement Mechanism
- Content Requirement Checklist for Truth QA

The legacy S4 artifact **does not overlap** with these sections because it was built for a different article topic and article type (ranked brand comparison vs. counter-intent inverter-path guide).

---

## 3. Gap Analysis

### 3.1 What the current workflow already handles well

- **Heading research:** `/article-skeleton` Phase 1 is the official, structured home for the legacy S4 "Secondary Heading Library" function.
- **Benchmark-derived structure:** `/article-benchmark-extract` already produces a `benchmark-success-formula.md` with §3 Structural Blueprint and §2.15 Section Function for the *current* article.
- **Evidence risk register:** `/article-evidence-opinions` and the section-contract "Evidence anchors" field in `/article-skeleton` fulfill the legacy "Knowledge Gap Flags" function in a more integrated way.

### 3.2 What the legacy artifact could add if properly curated

Despite being for the wrong topic, the artifact contains a small number of **reusable assets** for `solar-without-a-battery`:

| Reusable Asset | Relevance to Current Article |
|----------------|------------------------------|
| SAJ HS2 / HS3 positioning notes (§1, §2) | Useful for Path C (all-in-one ESS now) and the comparison table |
| `$500–700/kWh` value-tier price framing for SAJ | Could inform Path C value positioning **if** a current published source can verify it |
| Comparison matrix column set (capacity, power, efficiency, warranty, price/kWh, expandability, integration) | Could validate the column choices for the Path A/B/C table |
| Scenario-based recommendation pattern (best for whole-home backup, expandability, EV charging, etc.) | Could inspire the Path A/B/C scenario routing in the current article |
| Buyer pain points from Reddit/forums | Could validate the red-flag catalog in the current article |

### 3.3 What must NOT be carried over

- **The 7 competitor brand profiles** (Tesla, FranklinWH, Enphase, SolaX, Villara, Canadian Solar, Qcells) are off-topic for `solar-without-a-battery` and would cause benchmark drift.
- **The ranked list / buyer's-guide article type** conflicts with the current article's locked type: *contrarian buyer's guide / risk-avoidance explainer / product-routing decision guide* (see `benchmark-success-formula.md` §1.3).
- **Unverified specs and 2025 pricing** must not enter the current draft without fresh verification.

---

## 4. Integration Recommendation

### 4.1 Option A — Merge into `benchmark-success-formula.md` (NOT RECOMMENDED)

Add a new appendix to the current `benchmark-success-formula.md` titled "Legacy S4 Ingredient Reference."

**Pros:** Keeps everything in one place.  
**Cons:** The legacy artifact is for a different topic and article type; merging it would dilute the benchmark-derived focus of `benchmark-success-formula.md` and risk introducing off-topic competitor brands into the current article's structural blueprint. It would also violate the `/article-benchmark-extract` guardrail that the Structural Blueprint must NOT propose final project H2s.  
**Verdict:** Reject.

### 4.2 Option B — Feed directly into `/article-skeleton` or `/article-evidence-opinions` (PARTIAL / CAUTIOUS)

Extract only the SAJ-relevant and scenario-pattern-relevant snippets and paste them into the upstream artifacts as optional references.

**Pros:** Reuses the few relevant assets immediately.  
**Cons:** Mixes unverified 2025 data and wrong-article assumptions into the current workflow. Requires heavy curation and re-verification before use.  
**Verdict:** Only acceptable if each snippet is explicitly tagged as `[legacy reference — verify before use]`.

### 4.3 Option C — Archive as standalone reference and cite selectively (RECOMMENDED)

Move the legacy artifact to an archive/reference location (e.g., `content-workspace/sunriver-inverter/articles/solar-without-a-battery/references/legacy-s4-all-in-one-ess-ingredients.md`) and add a short "Legacy Reference Note" to `/article-skeleton` Phase 1 output or to `benchmark-success-formula.md` §9 (Output Handoff) pointing to it.

**Pros:**
- Preserves the historical research asset without polluting the current article artifacts.
- Allows the `/article-skeleton` agent to pull only curated SAJ / comparison-pattern snippets when designing Path C or the comparison table.
- Keeps the current `benchmark-success-formula.md` focused on the selected benchmarks for the current topic.

**Cons:** Requires an extra file to manage.  
**Verdict:** Recommended.

---

## 5. Concrete Content to Add (If Integration Proceeds)

If Option C is accepted, add the following lightweight note to `benchmark-success-formula.md` §9 Output Handoff:

```markdown
## 9.1 Legacy Reference Note

A legacy S4 "Content Ingredient Gathering" artifact exists for a related but different topic:
`references/legacy-s4-all-in-one-ess-ingredients.md`.

It may be consulted during `/article-skeleton` Phase 1 for:
- SAJ HS2/HS3 positioning language when designing Path C.
- Comparison-table column patterns (capacity, power, efficiency, warranty, price/kWh, expandability, integration).
- Scenario-based recommendation patterns for the Path A/B/C decision framework.

All data from this legacy artifact must be re-verified against current Sunriver product specs and published sources before entering the draft.
```

The legacy artifact itself should be relocated to:

```
content-workspace/sunriver-inverter/articles/solar-without-a-battery/references/legacy-s4-all-in-one-ess-ingredients.md
```

No other changes to `benchmark-success-formula.md`, `skeleton.md`, or `evidence-opinion-pack.md` are warranted.

---

## 6. Preserve / Drop / Watch Recommendation

| Disposition | Scope | Reason |
|-------------|-------|--------|
| **Preserve** | The full legacy file as an archived reference | It contains curated heading patterns and SAJ positioning notes that may be useful for future all-in-one ESS articles |
| **Drop** | Any wholesale merge into `benchmark-success-formula.md`, `skeleton.md`, or `evidence-opinion-pack.md` | Wrong topic, wrong article type, and unverified 2025 data |
| **Watch** | SAJ HS2/HS3 snippets, comparison matrix column set, scenario recommendation patterns | These can be selectively referenced during `/article-skeleton` Phase 1 if re-verified |

**Final recommendation:** Do not treat the legacy S4 artifact as a current workflow artifact. Treat it as a **historical research note** for a related topic. Archive it under `references/`, add a single legacy-reference pointer to `benchmark-success-formula.md` §9, and let `/article-skeleton` draw from it only if the section designer explicitly validates each snippet. For `solar-without-a-battery`, the official heading-inventory function is already covered by `/article-skeleton` Phase 1.
