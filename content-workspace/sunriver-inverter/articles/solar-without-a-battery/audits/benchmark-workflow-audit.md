# Benchmark Workflow Audit — Solar Without a Battery

**Audit date:** 2026-06-24  
**Auditor:** Kimi Code CLI  
**Scope:** Compare the S4-phase workflow outputs for the SAJ HS3 Installation Guide against the current `/article-benchmark-extract` outputs for `solar-without-a-battery`. Identify strengths, gaps, and concrete improvements for `benchmark-success-formula.md`.

---

## Executive Summary

- The **S4 workflow excels at writer-ready execution mechanics**: it delivers a small set of high-leverage tactics (5 tactics vs. 21 dimensions), an explicit `Why → How → Verify` paragraph template, a callout taxonomy (`[WARNING]` / `[IMPORTANT]` / `[PRO TIP]`), and a visual rule (`One Action, One Image`). These are largely absent from the current `benchmark-success-formula.md`.
- The **current 21-dimension extraction is stronger at strategic framing**: it provides cross-article synthesis, explicit risk labels, a borrow/do-not-borrow matrix, reader-advancement stages, pacing percentages, repetition diagnosis, and a prose-craft / linguistic-DNA card. These should be preserved.
- The **biggest gap is practical usability for `/article-skeleton`**: the current file is rich analysis but thin on the concrete structural templates a writer needs to draft section contracts. The S4 Phase 3 outline demonstrates the level of specificity the success formula should feed downstream.
- The **second biggest gap is non-text assets**: the current output has no visual plan, SEO meta plan, keyword strategy, internal-linking plan, or CTA design. The S4 workflow includes visual, safety-callout, and launchpad patterns that translate directly to publish-pack requirements.
- **Recommended priority:** fold the S4 execution mechanics into the current framework *without* losing the current analytical rigor. Add a `Writer's Playbook` section, a `Visual & Callout Plan`, an `SEO & Metadata` section, and an `Internal Linking & CTA` section.

---

## Side-by-Side Comparison

| Audit Area | S4 Workflow (SAJ HS3 Installation) | Current `benchmark-success-formula.md` (Solar Without a Battery) | Verdict |
|------------|-----------------------------------|------------------------------------------------------------------|---------|
| **Number of extracted dimensions** | 5 synthesized tactics (Phase 2) + themed ingredient lists (Phase 1) + full outline (Phase 3) | 21 consolidated dimensions + structural blueprint + reader advancement + prose craft card | Current is more granular; S4 is more actionable. |
| **Format of success formula** | Narrative playbook: observation → tactic → implementation rule | Analytical card set: dimension name → definition → borrow source → example | S4 is more writer-implementable; current is more auditor-friendly. |
| **Paragraph-level template** | Explicit `Why → How → Verify` loop for every H3 | Reasoning trajectory (condition → evidence → implication → recommendation) | S4 is more concrete for how-to/installation content. Current's reasoning trajectory is good but less procedural. |
| **Callout / aside taxonomy** | `[WARNING]`, `[IMPORTANT]`, `[PRO TIP]` with defined roles | Mentions callouts indirectly (e.g., key takeaways, red-flag catalog) | S4 is clearer and more repeatable. |
| **Visual plan** | `One Action, One Image` rule; annotated screenshots; diagrams; meta box with time/difficulty | No explicit visual plan | S4 is far ahead. |
| **SEO / meta / keyword strategy** | Not present as a dedicated section | AIO/answerability moments and primary keyword cluster from `project-profile.md` referenced implicitly | Neither is complete; current has AIO but no meta or keyword deployment plan. |
| **Internal linking plan** | Not present | Internal link inventory exists in `project-profile.md` but not wired into the article formula | Current has better source material but no plan. |
| **CTA design** | `Launchpad` conclusion pattern (next tutorials / next steps) | `Soft CTA` mentioned as section job, no design rules | S4 has a clearer conclusion mechanics pattern. |
| **Reader advancement mechanism** | Implicit in phased outline | Explicit table: stage → mental state → what section does | Current is stronger and should be preserved. |
| **Risk / borrow governance** | Not explicit | `Risk Label` column in ledger + `What We Are NOT Borrowing` table | Current is much stronger. |
| **Cross-article synthesis** | Brief benchmark mix table | Unified structural engine, article type classification, reframe statement | Current is stronger and should be preserved. |
| **Pacing / word-count guidance** | Implicit in phased outline | Explicit pacing table with % of article by segment | Current is stronger and should be preserved. |
| **Repetition diagnosis** | Not present | Explicit table: repeated pattern → diagnosis → action | Current is stronger and should be preserved. |
| **Prose craft / voice DNA** | Not present as a dedicated card | Dedicated `Linguistic DNA Card` with transitions, paragraph openers, metaphors | Current is stronger and should be preserved. |
| **Process reflection** | Phase 4 process summary with learnings | Not present | S4 process summary is valuable for methodology but optional for the article artifact. |
| **Ingredient gathering** | Phase 1: headings library + content requirement checklist | Not present | S4's ingredient-gathering artifact is useful for complex how-to topics but may be redundant for the current article type. |

---

## A. Structure & Organization

### How the S4 Success Formula organizes dimensions vs. the current 21-dimension extraction

The S4 formula is organized as a **small playbook of tactics** (5 tactics) derived from immersive reading of 3 benchmarks. Each tactic bundles:

1. **Observation** — what the benchmark does.
2. **Playbook Tactic** — what the new article must do.
3. **Implementation detail** — structural components (e.g., H2 block contents, callout types).

The current file is organized as a **21-dimension analytical matrix**. Each dimension names a quality (e.g., `Core Promise`, `Cognitive Load`, `Memorability`) and explains how the article should satisfy it. This is excellent for auditing voice and strategy but does not directly tell `/article-skeleton` "put this H2 here, with this paragraph shape."

### Which format is more actionable for `/article-skeleton`

The **S4 format is more directly actionable** because it outputs structural decisions in playbook form. For example, Tactic 3 (`Why-How-Verify`) gives `/article-skeleton` a repeatable section contract template. The current file's `Section Function` list (§2.15) is the closest equivalent but lacks the procedural paragraph template.

### Sections in S4 files that should be added to the current `benchmark-success-formula.md`

1. **Tactic 1 — Pre-Flight Checklist Opening** (`S4_Phase2_..._v5.md` §54–61): the consolidated opening block with Goal Statement, Tools & Personnel, Time & Difficulty, and Critical Safety Overview. Solar-without-a-battery is not a hardware tutorial, but the *pattern* of a top-of-article expectation-setting block is transferable.
2. **Tactic 3 — Why-How-Verify Instructional Loop** (`S4_Phase2_..._v5.md` §66–72): a paragraph-level contract for any section that teaches a decision or action.
3. **Tactic 4 — Crowd-Sourced Expertise Callout** (`S4_Phase2_..._v5.md` §73–79): the `[WARNING]` / `[IMPORTANT]` / `[PRO TIP]` taxonomy.
4. **Tactic 5 — Launchpad Conclusion** (`S4_Phase2_..._v5.md` §80–85): how the conclusion advances the reader rather than merely summarizing.
5. **Phase 1 Content Requirement Checklist** (`S4_Phase1_..._Ingredients.md` §58–104): the idea of a discrete, checkable content inventory grouped by theme. For `solar-without-a-battery` this would be a "must-cover claims" checklist (e.g., verify the H2 runs grid-tied without battery, no generic tax advice).
6. **Phase 4 Process Summary** (`S4_Phase4_..._Process_Summary.md`): the reflection on benchmark selection and dialectical refinement. This should become a short `Methodology Note` in the current workflow, not the article artifact itself.

---

## B. Depth of Extraction

### Does the S4 workflow extract more specific patterns?

**Yes, at the paragraph and visual level.** Examples:

- S4 specifies the exact sentence-level shape: *"The 'Why' (Context): A brief, 1-2 sentence paragraph..."* and *"The 'How' (Action): The direct, clear instructions, using imperative language..."*
- S4 specifies visual pairing: *"Every single instruction to touch the device is paired with a photo."*
- S4 specifies callout types and voice: `[PRO TIP]` framed as *"From our experience, doing X before Y saves a lot of time."*
- S4 Phase 3 turns all of this into an outline where every H3 has Why/How/Verify and assigned callouts.

The current file extracts patterns at the section-function and voice-register level but rarely reaches the paragraph contract or image-contract level.

### Missing elements in the current output

| Missing Element | Where It Appears in S4 | Why It Matters |
|-----------------|------------------------|----------------|
| **Visual plan** | iFixit `One Action, One Image` rule; annotated screenshots; meta box | Publish-pack and `/article-enrich` need image-plan.md input. Without a visual plan, enrichment is ad hoc. |
| **SEO meta / title / description strategy** | Not in S4 either, but title and meta box patterns appear | Current file names title but does not derive H1/SEO title/meta description/OG rules. |
| **Keyword deployment plan** | Not in S4 | Current `project-profile.md` lists keywords, but the success formula does not say where to place them (H1, H2, first 100 words, URL slug). |
| **Internal linking plan** | Not in S4 | `project-profile.md` has inventory; success formula should assign links to sections. |
| **CTA design rules** | Launchpad conclusion | Current file says "soft product CTA" but gives no design rules (when, how many, wording constraints). |
| **Callout taxonomy** | `[WARNING]` / `[IMPORTANT]` / `[PRO TIP]` | Safety and credibility signaling needs explicit rules, especially for a supply partner making hardware claims. |
| **Content requirement checklist** | Phase 1 ingredient checklist | A truth-QA-ready checklist of claims the article must and must not make. |
| **Benchmark selection rationale** | Phase 4 learnings | Helps future audits understand why these benchmarks were chosen and what to avoid. |

---

## C. Practical Usability

### Which output makes it easier for a writer to draft the article?

**The S4 output, because it produces an outline.** The Phase 3 file is essentially a draft-ready skeleton: every H2 has a Why, every H3 has Why/How/Verify, and callouts are pre-assigned. A writer could start drafting from Phase 3 with minimal translation.

The current `benchmark-success-formula.md` is a **strategy brief**, not a skeleton. A writer must still do significant work to convert §2.15 (Section Function) and §3.1 (Borrowable section-job sequence) into actual H2/H3 contracts. This is the correct handoff target for `/article-skeleton`, but the success formula could make that handoff easier by supplying reusable templates.

### Does the S4 output include ready-to-use templates, prompts, or examples?

Yes. Notable examples:

- **Why-How-Verify template** with parenthetical labels that can be copied into an outline.
- **Callout templates** with literal bracket labels and example copy (e.g., *"[WARNING] CRITICAL SAFETY OVERVIEW..."*).
- **Time / difficulty / personnel meta box** with example values (*"Time Estimate: 3-5 hours. Difficulty: Difficult. Requires certified electrical knowledge."*).
- **Final verification checklist** with checkbox syntax (`[ ]`).

The current output includes:

- Transition tables.
- Paragraph opener examples.
- Metaphor list.
- Path A/B/C framework.
- Reader-advancement table.

These are useful but are **voice and argument ingredients**, not **section templates**.

---

## D. Gaps in Current Output

### Important elements from the S4 workflow missing from `benchmark-success-formula.md`

1. **Section-level paragraph contract (`Why → How → Verify`)** — the most transferable S4 pattern for any article that teaches a decision.
2. **Callout taxonomy with defined roles** — needed for safety warnings, critical technical details, and practitioner tips.
3. **Visual / image contract** — e.g., `One Concept, One Diagram` for the path framework; product imagery rules; comparison-table screenshot guidelines.
4. **Top-of-article expectation block** — a transferable version of the Pre-Flight Checklist: what the reader will learn, what they should know first, how long it takes to read/decide.
5. **Launchpad conclusion design** — specific next-step routing (product pages, related articles, contact) instead of a generic CTA.
6. **Content requirement checklist** — discrete claims and elements the final article must contain, usable by Truth QA.
7. **SEO meta & keyword deployment rules** — how to turn the working title into H1/SEO title/meta/URL; where primary and secondary keywords belong.
8. **Internal link assignment** — which sections link to which Sunriver product/blog pages and why.
9. **Benchmark selection rationale / methodology note** — why these three benchmarks were chosen and what each contributes.

### What should be added or reorganized

Add a new top-level section **"Writer's Playbook"** after the current `Structural Blueprint` (or merge into it) that contains:

- `Paragraph Contract: Why → How → Verify`
- `Callout Taxonomy`
- `Visual Contract`
- `Expectation-Setting Opener Block`
- `Launchpad Conclusion Block`

Add a new top-level section **"SEO, Metadata, and Linking Plan"** that contains:

- `Title / H1 / SEO title / meta description rules`
- `Keyword placement map`
- `Internal link assignment table`
- `CTA placement and wording rules`

Add a **"Content Requirement Checklist"** as an appendix or within the structural blueprint, mapping each required claim to a section.

---

## E. Things Current Output Does Better

The following strengths should be **preserved, not replaced**:

| Strength | Location in Current File | Why Preserve It |
|----------|--------------------------|-----------------|
| **Cross-article synthesis table** | §1.1 | Explains why the benchmark mix fits Sunriver. |
| **Unified structural engine / reframe** | §1.2 | Gives the article a single conceptual anchor. |
| **Article type classification** | §1.3 | Prevents format drift during drafting. |
| **Explicit risk labels** | `benchmark-asset-ledger.md` + §5 | Safe / transformed / watch / blocked governance is audit-ready. |
| **Borrow / do-not-borrow table** | §5 | Blocks source drift and competitor copying. |
| **Reader advancement mechanism** | §4 | Maps mental states to section functions. |
| **Pacing table with percentages** | §3.2 | Gives length and rhythm targets. |
| **Evidence rhythm** | §3.3 | Ensures no long theory blocks without proof. |
| **AIO / answerability moments** | §3.4 | Directly supports AIO capture without forcing FAQs. |
| **Repetition diagnosis** | §3.5 | Distinguishes intentional rhythm from accidental cliché. |
| **Linguistic DNA card** | §2.20 | Gives `/article-draft` concrete voice material. |
| **Path A/B/C decision framework** | §2.7 | The article's core intellectual product. |
| **Red-flag catalog** | §2.15, §3.1 | Translates JingSourcing's pattern into a Sunriver-specific section job. |

---

## Recommendations Ranked by Impact

### High Impact

1. **Add a `Why → How → Verify` paragraph contract to the Structural Blueprint.** This is the single biggest usability upgrade from the S4 workflow.
2. **Add a callout taxonomy (`[WARNING]` / `[IMPORTANT]` / `[PRO TIP]`)** with role definitions and example copy, especially for safety, warranty, and installer-pitch caveats.
3. **Add a Visual & Image Contract** specifying when the article needs a comparison table, a wiring/path diagram, product images, and screenshot/annotated-image rules.
4. **Add an SEO, Metadata & Keyword Deployment section** that translates the `project-profile.md` keyword cluster into H1/H2/first-100-words placement rules.
5. **Add an Internal Link Assignment table** mapping each major section to the most relevant Sunriver product/blog page from the `project-profile.md` inventory.

### Medium Impact

6. **Add a transferable `Expectation-Setting Opener Block`** (adapted from S4's Pre-Flight Checklist) that tells the reader what they will learn, what they should already know, and what decision they will be able to make.
7. **Add a `Launchpad Conclusion Block`** design with specific next-step routing (product pages, related articles, contact).
8. **Add a `Content Requirement Checklist`** of claims/elements the article must include, usable by Truth QA.
9. **Embed the S4 Phase 4 `benchmark selection rationale` as a short methodology note** in `benchmark-asset-ledger.md` or as an appendix to `benchmark-success-formula.md`.
10. **Reorganize §2.15 and §3.1 into a single `Section Contract Library`** where each borrowable section job is paired with its paragraph contract, callout type, and evidence source.

### Low Impact

11. **Add an `Ingredient Gathering` appendix** only if future articles are complex how-to guides where a headings library + content checklist materially reduces research time.
12. **Add a `Dialectical Reflection` note** documenting the selection/pivot decisions, primarily for project retrospectives.

---

## Proposed Concrete Edits to `benchmark-success-formula.md`

The following edits are written as `StrReplaceFile`-ready `old / new` pairs where possible. They assume the current file remains otherwise intact.

### Edit 1 — Insert `Writer's Playbook` after `## 3. Structural Blueprint`

**Old:**

```markdown
## 4. Reader Advancement Mechanism
```

**New:**

```markdown
## 4. Writer's Playbook (for `/article-skeleton`)

### 4.1 Paragraph contract: Why → How → Verify

Every section that teaches a decision or action should follow this three-part shape:

1. **Why (Context):** 1–2 sentences explaining why this section matters and what risk it addresses.
2. **How (Action):** The core instruction, comparison, or framework, using imperative or direct language.
3. **Verify (Feedback):** The expected outcome, a check the reader can perform, or a concrete sign that the decision is correct.

Borrowed from S4 / Ahrefs + DigitalOcean + iFixit. Calibrate to Sunriver's contrarian voice: the "Why" can be a provocation, not a neutral setup.

### 4.2 Callout taxonomy

Use three callout types consistently:

- **`[WARNING]`** — Safety, warranty, or compliance caveats that could cost the reader money or cause rework. Example: *"[WARNING] A string inverter without AC-coupled battery support will require an inverter swap if you later want DC-coupled battery backup."*
- **`[IMPORTANT]`** — Technical details essential for success that are easy to miss. Example: *"[IMPORTANT] The SAJ H2 can run grid-tied without a battery, but battery expansion voltage and capacity thresholds must match the future battery module."*
- **`[PRO TIP]`** — Practitioner advice framed as experience, not self-praise. Example: *"[PRO TIP] From what Sunriver sees in the field, the most expensive retrofit is not the battery — it is replacing an inverter that was never battery-ready."*

### 4.3 Visual contract

- **One concept, one diagram:** Anytime the article introduces a new decision framework (e.g., Path A/B/C, AC vs. DC coupling), pair it with a diagram or comparison table.
- **Product images:** Use Sunriver product photography for R6, H2, and HS3 when named.
- **Annotated screenshots:** Only if showing the eSAJ app or a config screen; otherwise prefer diagrams and tables.
- **Comparison table:** One mandatory table comparing Path A, Path B, and Path C across cost now, future battery cost, backup today, and inverter replacement risk.
- **Image plan handoff:** `/article-enrich` should turn this contract into `image-plan.md` with alt text tied to the article's decision framework.

### 4.4 Expectation-setting opener block

Immediately after the contradiction hook, include a short block that sets expectations:

- **What you will learn:** One sentence summarizing the decision framework.
- **What you should already know:** Basic solar terminology (inverter, battery, grid-tied, hybrid).
- **What you will be able to do:** Choose Path A, B, or C and ask one hard question before signing a quote.

### 4.5 Launchpad conclusion block

The conclusion must do more than summarize. It should:

1. Restate the core reframe in one punchy sentence.
2. Offer a single action item (the installer question).
3. Route the reader to the next most relevant Sunriver resource based on their likely path:
   - Path A → `/product/r6-15k-25k-three-phase-on-grid-inverter/`
   - Path B → `/product/h2-3k-6k-single-phase-hybrid-inverter/`
   - Path C → `/product/hs3-3k-6k-single-phase-all-in-one-energy-storage-system/`

## 5. Reader Advancement Mechanism
```

*Note: Renumber subsequent sections accordingly (current §4 becomes §6, etc.).*

---

### Edit 2 — Insert `SEO, Metadata, and Linking Plan` before `## 5. What We Are NOT Borrowing`

**Old:**

```markdown
## 5. What We Are NOT Borrowing
```

**New:**

```markdown
## 5. SEO, Metadata, and Linking Plan

### 5.1 Title / H1 / SEO metadata

- **H1:** *Solar Without a Battery: The Battery Industry Hopes You Never Read This*
- **SEO title (≤ 60 chars):** *Solar Without a Battery: Is a Battery-Ready Inverter Smarter?*
- **Meta description (≤ 155 chars):** *Skipping the battery now can be smart — if your inverter is battery-ready. Compare string, hybrid, and all-in-one paths before you sign.*
- **URL slug:** `solar-without-a-battery`
- **OG image:** Use the article hero diagram (Path A/B/C) or a Sunriver product lineup image.

### 5.2 Keyword placement map

| Keyword | Placement | Notes |
|---------|-----------|-------|
| `solar without a battery` | H1, first 100 words, URL slug | Primary cluster anchor. |
| `solar system without battery` | H2 or early paragraph | Natural variant. |
| `solar panel without battery` | Body paragraph | Use in scenario copy. |
| `home battery backup without solar` | Related-question paragraph or internal link context | Addressed by redirecting to battery-now path. |
| `hybrid inverter without battery` | Path B section | Core technical claim. |
| `battery-ready inverter` | Repeated intentionally across opener, framework, and close | Conceptual anchor; see §3.5 repetition diagnosis. |

### 5.3 Internal link assignment

| Section | Link target | Link role |
|---------|-------------|-----------|
| Path framework / Path A | `/product/r6-15k-25k-three-phase-on-grid-inverter/` | Product routing |
| Path framework / Path B | `/product/h2-3k-6k-single-phase-hybrid-inverter/` | Product routing |
| Path framework / Path C | `/product/hs3-3k-6k-single-phase-all-in-one-energy-storage-system/` | Product routing |
| Myth debunk / hybrid basics | `/can-hybrid-inverter-work-without-battery/` | Educational depth |
| Path framework / modern hybrid | `/modern-hybrid-solar-systems/` | Educational depth |
| All-in-one comparison | `/all-in-one-energy-storage-system-comparison/` | Educational depth |
| Red flags / battery specs | `/5-solar-battery-specs-to-avoid-solar-rush-mistake/` | Educational depth |
| Close / next steps | `/contact/` | Conversion |

### 5.4 CTA placement and wording rules

- **No CTA before the educational framework is complete.** (Borrowed from EnergySage.)
- **First CTA:** soft product-path routing inside the Path framework section (e.g., *"If Path B fits, see the SAJ H2 specs."*).
- **Second CTA:** the closing single action item (the installer question) plus contact/link routing.
- **Wording constraints:**
  - Do not use "Get a quote" as the primary CTA.
  - Use "Compare the SAJ H2 specs" or "Ask your installer this question" instead.
  - Never imply Sunriver performs installation labor.

## 6. What We Are NOT Borrowing
```

*Note: Renumber subsequent sections accordingly (current §5 becomes §6, etc.).*

---

### Edit 3 — Strengthen `Section Function` with paragraph-contract mapping

**Old:**

```markdown
### 2.15 Section Function

Borrowable section jobs (NOT final H2s):
1. **Contradiction hook** — title reframe + proof in first 150 words.
2. **Key takeaways preview** — 3–5 bullets that give the whole answer away.
3. **Need / path qualification** — force the reader to choose a hardware path before discussing battery timing.
4. **Myth debunk** — "battery mandatory" pressure and the non-battery-ready trap.
5. **Path framework** — Path A / B / C comparison with specs and trade-offs.
6. **Red-flag catalog** — installer-quote warning signs.
7. **Single action item** — the one question to ask before signing.
8. **Lesson-pivot close** — reframe from "no battery" to "right battery-ready hardware path."
9. **Soft product CTA** — route to R6 / H2 / HS3 pages or contact.
```

**New:**

```markdown
### 2.15 Section Function

Borrowable section jobs (NOT final H2s). Each job should be paired with the `Why → How → Verify` paragraph contract (§4.1) and an assigned callout type where relevant.

1. **Contradiction hook** — title reframe + proof in first 150 words. *Why:* reader assumes battery is mandatory. *How:* reframe + proof. *Verify:* reader understands battery-less solar is a strategy.
2. **Key takeaways preview** — 3–5 bullets that give the whole answer away. *Why:* skimmers and AIO. *How:* bullet list. *Verify:* reader can state Path A/B/C.
3. **Need / path qualification** — force the reader to choose a hardware path before discussing battery timing. *Why:* prevents one-size-fits-all advice. *How:* 2–3 qualifying questions. *Verify:* reader knows which path they are on.
4. **Myth debunk** — "battery mandatory" pressure and the non-battery-ready trap. *Why:* counters the most common misinformation. *How:* wrong-way teardown + right-way spec. *Verify:* reader can explain the retrofit trap. *[WARNING] possible.*
5. **Path framework** — Path A / B / C comparison with specs and trade-offs. *Why:* the core decision tool. *How:* comparison table + scenario. *Verify:* reader can pick a path for their project.
6. **Red-flag catalog** — installer-quote warning signs. *Why:* defensive competence. *How:* numbered list of warning signs. *Verify:* reader can screen a quote. *[IMPORTANT] or [PRO TIP] possible.*
7. **Single action item** — the one question to ask before signing. *Why:* conversion to action. *How:* copy-paste question. *Verify:* reader knows what to ask.
8. **Lesson-pivot close** — reframe from "no battery" to "right battery-ready hardware path." *Why:* memorability and next-step routing. *How:* punchy reframe + launchpad links. *Verify:* reader remembers the reframe phrase.
9. **Soft product CTA** — route to R6 / H2 / HS3 pages or contact. *Why:* move reader to technical review. *How:* path-specific link. *Verify:* reader clicks the relevant product page.
```

---

### Edit 4 — Add a `Content Requirement Checklist` appendix

**Old:**

```markdown
## 6. Output Handoff

Next skill: `/article-evidence-opinions`
This success formula should be read by `/article-skeleton` before any section contracts are written.
```

**New:**

```markdown
## 7. Content Requirement Checklist (for Truth QA)

- [ ] The article states that battery-less solar is viable only with the right inverter path.
- [ ] The article names SAJ R6, H2, and HS3 and maps each to Path A/B/C.
- [ ] The article explains that the SAJ H2 can run grid-tied without a battery.
- [ ] The article explains that the SAJ H2 supports plug-and-play DC-coupled battery expansion (with voltage/capacity thresholds and a disclaimer to confirm with installer).
- [ ] The article does not claim any product works with any battery.
- [ ] The article does not give specific pricing without a published source.
- [ ] The article does not present tax advice as an individualized recommendation.
- [ ] All tax/regulatory/financial claims carry an "as of 2026 / confirm with a licensed professional" disclaimer.
- [ ] The article includes at least one comparison table for Path A/B/C.
- [ ] The article includes at least one red-flag catalog for installer quotes.
- [ ] The article ends with one concrete question to ask an installer.
- [ ] The article includes 4–6 contextual internal links to existing Sunriver product/blog pages.
- [ ] The article includes 3–5 attributed external sources (standards, IRS, EU, industry data).

## 8. Output Handoff

Next skill: `/article-evidence-opinions`
This success formula should be read by `/article-skeleton` before any section contracts are written.
```

*Note: If edits 1 and 2 are applied, the current `## 6. Output Handoff` becomes `## 8. Output Handoff`.*

---

## Preserve / Drop Recommendations

### Preserve

- 21-dimension analytical framework (with integration into the Writer's Playbook).
- Cross-article synthesis table (§1.1) and unified structural engine (§1.2).
- Article type classification (§1.3).
- Explicit risk labels in `benchmark-asset-ledger.md` and the `What We Are NOT Borrowing` table.
- Reader advancement mechanism table.
- Pacing table with percentages.
- Evidence rhythm section.
- AIO / answerability moments.
- Repetition diagnosis table.
- Linguistic DNA card (§2.20).
- Path A/B/C decision framework.
- Red-flag catalog as a section job.

### Drop

- Nothing should be dropped wholesale. However, the current §2.15 and §3.1 overlap; merge them into a single `Section Contract Library` that maps section jobs to paragraph contracts, callouts, and evidence sources.
- The S4 Phase 1 "ingredient gathering" artifact is not needed for this article type but could be revived as a reusable template for future hardware how-to guides.

---

## Final Note

The current `benchmark-success-formula.md` is a strong strategic document. The recommended upgrades make it a stronger **operational** document for `/article-skeleton` while preserving its analytical and governance strengths. The highest-leverage additions are the `Why → How → Verify` paragraph contract, the callout taxonomy, the visual contract, and the SEO/metadata/linking plan.
