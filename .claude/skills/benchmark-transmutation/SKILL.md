---
name: benchmark-transmutation
description: "Use when: (1) extracting success formulas from benchmark articles in /article-benchmark-extract, (2) recording borrowed assets in benchmark-asset-ledger, (3) building the article skeleton with benchmark-informed structure, (4) any time a non-original structural pattern enters the article. Governs how borrowed benchmark assets (structure, viewpoints, case patterns, data, brand stance) are transformed into project-native article assets. Makes borrowing explicit, traceable, and safe."
user-invocable: false

---

# Benchmark Transmutation

## Purpose

Benchmark imitation is allowed and expected — but it must be explicit, transformed, and ledgered. Borrowing structure from SERP competitors produces weak articles. Instead, borrow structure from best-in-class content sites (Ahrefs, HubSpot, Backlinko, Animalz, CXL, Investopedia, etc.) and transform it through the locked `project-profile.md`. Every borrowed asset must be recorded, transformed, and risk-labeled.

## When to Use

- `/article-benchmark-extract`: when extracting structural patterns from user-selected benchmark articles
- `/article-skeleton`: when applying borrowed patterns to the section structure
- Any time a non-original pattern, viewpoint, or data point enters article design

## Instructions

### 1. Identify Borrowable Asset Types

| Asset Type | What It Is | Example |
|---|---|---|
| Structure | Cognitive progression logic, section-job sequence, pacing, evidence rhythm, answerability moments, and information architecture. This is a borrowable blueprint, not a fill-in-the-blanks outline. | "This article moves from problem recognition → self-diagnosis framework → proof-heavy comparison → decision rule. That sequence is borrowable; the final H2s are project-specific." |
| Viewpoint | An angle or perspective on the topic | "Written from the procurement manager's risk perspective, not the designer's" |
| Case Pattern | How examples are presented | "Each case opens with specs, then problem, then outcome" |
| Data | Market sizing, industry benchmarks | "$11.92B folding screen market (2025)" |
| Brand Stance | How the author positions relative to the reader | "We've tested this. Here's what we found. Here's where it fails." |
| Prose Craft | Sentence rhythm, paragraph structure, bold density, transition patterns — the line-by-line execution of voice. Unlike Structure (section-level), Prose Craft operates at the sentence and paragraph level. | "Backlinko uses 3-line broken openers once per chapter, 3-5 sentence body paragraphs, and 1-line standalone punches for emphasis. Bold appears 1-2 times per chapter. Transitions are plain English." |

### 2. Record Every Borrowed Asset

Use `templates/benchmark-asset-ledger.md`. Each entry requires: source/origin, what is borrowed, why it works, transformation rule (how it becomes project-native), risk label, final expression rule.

### 3. Imitate Structure, Differentiate Content

This replaces the old "Transform, Don't Copy" rule. Structural imitation is the starting point — not something to avoid.

**Layer 1 — Imitate.** The benchmark article's section rhythm, evidence deployment pattern, judgment density, and information progression are fair game for imitation. When HubSpot C alternates between "classification → real-world example" across 15 strategies, that rhythm can be borrowed directly. When Backlinko E opens with a bold assertion, follows with 7 chapter cards, and closes with 4 case studies — that arc can be imitated.

**Layer 2 — Inject.** Swap the benchmark's content with the project's owned proof: project data replaces case studies, forensic workshop/caliper photos replace generic screenshots, Named E-E-A-T Engineer field notes replace generic quotes, and Anti-Sell Disqualification Boundaries (when NOT to buy) replace one-way marketing claims. The structure stays; the substance becomes proprietary and non-replicable by competitors.

**Layer 3 — Differentiate.** Apply `voice-and-humanization` to execute voice per scene (including 40–60 word Self-Contained RAG Citation Chunks and Buying Committee dual-register for Specifier + CFO/Procurement). Apply `structure-variation` to prevent lazy repetition while preserving intentional benchmark-native rhythm. The differentiation is in execution — how the article reads, not what structure it follows.

The old rule was "transform, don't copy." The new rule: **copy the structure, transform the content, differentiate the voice.**

### 4. Risk Labels

- `safe`: public domain / industry standard pattern
- `transformed`: borrowed and adapted — monitor in draft
- `watch`: close to source material — needs operator review
- `blocked`: cannot use — competitor IP, unverifiable data, conflicts with profile red lines

### 5. What Is NOT Borrowable

Some things that appear borrowable in benchmark articles are actually artifacts of that source's brand system — not transferable content strategy.

- **Unexamined format uniformity across sections.** Some benchmark articles use repeated section formats. Do not reject or copy that automatically. Label the repetition: `intentional-rhythm` if it creates reader confidence, `house-style` if it only reflects the publisher's brand habit, or `avoid` if it becomes mechanical. Borrow the logic only after this diagnosis.
- **Brand-specific voice personality.** HubSpot's casual-optimistic tone, Backlinko's "I made a decision, here's why" — these are their voice, not yours. Extract the FUNCTION of the voice (builds trust, signals expertise, creates relatability) but use your own voice-and-humanization lens system to execute it.
- **Lead-gen CTA density.** HubSpot inserts a download CTA between every major section. This is their conversion model, not a content strategy. Borrow the idea of "reader next step at natural decision points," not the frequency or format.

---

## Examples

### Input (borrowed from Ahrefs guide):
"The article opens with a surprising statistic, then a definition, then steps."

### Output (transmuted into Metal Divider's article):
"The article opens with a project scene — 'Last month, an architect sent us a drawing with a note: can you make this work at 4 meters?' — then reframes what a divider actually is, then introduces the 6 decisions framework."

### Input (borrowed from Xometry technical deep-dive):
"Each manufacturing method section uses: method description → tolerance data → best applications → limitations."

### Output (transmuted):
"Each method section uses: method description with Metal Divider's specific tolerance data → a real project that used this method → when NOT to use this method → what the cost trade-off actually means. The tolerance data is ours. The projects are ours. The 'when not to use' is our field experience."

---

## Guardrails

### Cross-Reference with Other Skills

- `structure-variation`: Use it to prevent lazy repeated templates. It should not override an intentional benchmark rhythm that is central to the article's success.
- `voice-and-humanization`: The 4-lens system determines how voice executes per scene. Benchmark voice patterns inform lens selection but do not replace it.

### Anti-Patterns
- Copying a benchmark's H2 sequence and just changing the brand name
- **Borrowing format uniformity without diagnosis**: seeing that a benchmark article uses the same section format throughout and either copying it blindly or rejecting it blindly. First decide whether the repetition is intentional rhythm, house style, or a pattern to avoid.
- Borrowing a competitor's case study framing and presenting it as your own project
- Using borrowed market data without citing source, year, and region
- Applying a borrowed brand stance that conflicts with the locked profile's voice
- **Writing the final outline during Success Formula extraction**: final H2s and final section count belong to `/article-skeleton`; borrowable section jobs and rhythm belong in the Structural Blueprint.

### Red Lines (from project profile)
- Never present borrowed case patterns as owned cases without proof
- Never use data without source, year, region, and scope
- Never copy brand stance that conflicts with the locked profile role
- Never borrow a competitor's actual content, client names, or proprietary data

### When to Ask
- A borrowed asset's risk is unclear → label `watch` and flag for operator review
- A borrowed pattern seems essential but the transformation isn't obvious → discuss before proceeding
