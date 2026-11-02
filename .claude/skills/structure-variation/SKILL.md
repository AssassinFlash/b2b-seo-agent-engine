---
name: structure-variation
description: "Use when: (1) building the article skeleton in /article-skeleton, (2) auditing section rhythm before drafting, (3) detecting format monotony in Reader QA, (4) any time two consecutive H2s feel like they follow the same template. Ensure every section in a Markdown article uses the structural format that matches the reader's current cognitive task. Prevents template-copy across sections — the most common failure mode in AI-generated B2B content."
user-invocable: false

---

# Structure Variation

## Purpose

Structure variation is not about visual variety. It is about matching each section's Markdown format to what the reader needs at that exact moment — reframing, comparing, deciding, trusting, or acting. When every H2 uses the same template (paragraph → bullet list → recommendation), the reader predicts the format by section 2 and stops reading.

## When to Use

- `/article-benchmark-extract`: as a diagnostic reference — distinguish lazy repeated templates from intentional benchmark-native rhythm
- `/article-skeleton`: assign a structural format to each H2 based on its function
- `/article-draft`: execute each section in its assigned format
- Reader QA: detect sections that read identically despite different topics

---

## Reader State → Markdown Structure Map

| Reader State | What They Need | Best Structure |
|---|---|---|
| **First 3 seconds on page (Above-the-Fold Navboost Viewport)** | Immediate proof they clicked the right result (zero pogo-sticking) | **Direct contrarian answer + 3-Path Self-Router / Micro-Anchor in first 180 words.** Never open with a giant decorative stock banner or encyclopedia definition. |
| Just arrived, scanning, deciding to stay | A clear, surprising reframe | **Opinion-led continuous prose.** Strong H2 as judgment, not label. Opening paragraphs that challenge assumptions. No lists yet. |
| Convinced, needs orientation | Map of what's ahead | **Ordered list or decision framework.** "The N decisions that shape every X." |
| Comparing options (2–4 columns max) | Dimension-by-dimension comparison | **Markdown Table (≤4 columns) + judgment paragraph.** Because `#md-blog-single` uses `table-layout: fixed; width: 100%`, a 5+ column Markdown table crushes text into unreadable vertical strips on 320px/390px mobile screens. For 5+ dimensions, use a **2-column Scoped HTML Bento Grid, Pure CSS Radio-Tab Switcher, or `.linker-article-comparison` block** instead! |
| Unfamiliar with concepts | Human explanation | **Paragraph + specific scene.** One concept per paragraph through a real scenario. |
| Worried about wrong decisions | Risk awareness & honest boundaries | **Blockquote for core warning** + short paragraphs for specific failure modes + **Anti-Sell Disqualification box** (when NOT to buy the high-spec option). |
| Wants proof of experience | Forensic project/workshop evidence | **Mini forensic case study.** Location, caliper/instrument specs, failure mode avoided, outcome. Short. No sales language. |
| **Technical specifier needs budget sign-off from CFO / Procurement / Owner** | Forwardable internal business case | **Internal Champion Enablement Block (30-Second Executive TCO & Risk Ledger).** Upfront delta vs. 5-year rework/failure cost in a clean, screenshot-ready ledger. |
| Ready to understand process | Step-by-step walkthrough | **Ordered list with "why" per step.** Not "Step 1: X." But "Step 1: X — here's why this catches problems early." |
| Final check before acting | Quick practical answers | **Objection-resolution module** (conclusion-first FAQ, cost ledger card, or myth-vs-reality toggle). |
| Ready to act | What to send, what happens next | **Copyable RFQ / Installer Interrogation Checklist.** Specific clauses the buyer can copy-paste directly to vendors. |

---

## HTML Structural Liveness Palette (用多样化 HTML 结构打破排版死板，让文章活跃有呼吸感)

Plain Markdown (`##` + paragraphs + `-` bullets + standard `| table |`) quickly looks rigid and monotonous over a 3,000–4,500 word B2B guide. Whenever a section needs visual energy, scannability, or multi-dimensional contrast, weave in **diverse, self-contained HTML structural blocks** (planned in `/article-skeleton` and built in `/article-enrich` + `/article-html-visuals`):

| Structural Fatigue Symptom | HTML Structural Block to Inject Instead | Why It Makes the Page Feel Alive |
|---|---|---|
| Three bullet lists in a row | **Bento-Grid Spec & Metric Cards** (2×2 max 2-col CSS Grid for `68ch` with oversized monospace numbers + 1-line engineering verdict) | Turns dry parameters into scannable visual anchors |
| Multi-condition "it depends" prose | **Interactive Scenario / Environment Switcher Tabs** (Zero-JS Pure CSS radio pill tabs: e.g., *Indoor Dry* / *Humid Lobby* / *Coastal Salt-Air*) | Reader clicks their exact environment and sees only the specs that apply |
| Standard flat Markdown table | **Spec-Sheet Promise vs. Shop-Floor Reality Split Card** (left side: what vendors claim; right side: caliper/field reality + delta badge) | Creates immediate visual tension and contrast |
| Sequential process steps | **Horizontal Process Pipeline / Step Strip** with tolerance & lead-time badges between nodes | Shows flow and bottlenecks at a glance instead of a vertical wall of text |
| Long cost or BOM explanation | **Layered Cost-Anatomy Bar + Expandable Drawer** (proportional stacked bar showing hidden cost drivers) | Makes hidden fees and TCO proportions visually obvious |
| Tolerance or threshold discussion | **Visual Safe-Zone / Failure-Zone Gauge Strip** (green/amber/red threshold bar with marker pins) | Lets engineers see the operating margin instantly |

---

## The Anti-Pattern: Template Replication

This is the most common AI content failure. It looks like:

```
## Application 1
Paragraph. Bullet list. Recommendation.
  ### Design Considerations
  - A / - B / - C
  ### Recommended Materials
  Paragraph.

## Application 2
Paragraph. Bullet list. Recommendation.
  ### Design Considerations
  - A / - B / - C
  ### Recommended Materials
  Paragraph.

## Application 3
[same template again]
```

This is not structure variation. This is template copying. The reader predicts format by section 2 and stops reading by section 3.

### How to Break It

- Context 1: full narrative + project spotlight (longest, establishes the pattern)
- Context 2: compact decision framework (shorter, faster, different rhythm)
- Context 3: risk-forward angle — "what goes wrong if you choose wrong here"
- Context 4: mini case study only (shortest, pure evidence)

Or merge contexts. Maybe the article doesn't need four separate application sections. Two with different structures + a comparison table for the rest.

---

## H2 Naming Rule

H2s should be cognitive nodes, not topic labels. There are three valid H2 forms — choose based on the section's primary job.

### The Three H2 Forms

| Form | Example | When to Use | AI Overview? |
|---|---|---|---|
| **Judgment** | "Hotel lobbies punish materials" | The section's job is to change how the reader thinks — reframe a problem, introduce a mental model, challenge an assumption | Weak — AI must infer the question |
| **Question** | "What metal screen survives a hotel lobby?" | The section directly answers a real search query. The question IS what someone would type into Google. Use natural language, not keyword strings | Strong — AI Overview extracts the bold answer beneath it |
| **Action Node** | "Before you RFQ" | The section's job is to move the reader to action. Short. Imperative. No judgment or query to answer | N/A — not a knowledge section |

### How to Choose

```
Can someone search this exact question on Google?
  ├── YES → Use a Question H2. AI Overview will match it.
	  │         Make the first natural answer extractable.
  │         Example: "Why does my restaurant screen look different at night?"
  │
  └── NO → Is this section changing how the reader thinks?
            ├── YES → Use a Judgment H2.
            │         Example: "It is a specification decision. Not a product choice."
            │
            └── NO → Is this section moving the reader to act?
                      └── Use an Action Node.
                          Example: "Before you RFQ"
```

### Rules

- **Mix forms**: An all-judgment article reads like a manifesto. An all-question article reads like an FAQ. The best articles use both — judgment for reframes, question for answer sections, action for the exit.
- **Question must match real queries**: Only use a question H2 when the section genuinely answers a search intent. Don't force "What is X?" when the section's real job is to change thinking.
- **Question wording**: Natural language, not keyword strings. "What metal screen survives a hotel lobby?" not "hotel lobby metal screen material selection guide."
- **Answer must deliver**: When you use a Question H2, the section should contain a clear direct answer at the first natural point. Bold it only if bolding improves skimmability without breaking benchmark rhythm.

### Examples

| Weak (Label) | Strong (Judgment) | Strong (Question) |
|---|---|---|
| Materials | Choose the Material by Environment, Not by Appearance | Which stainless steel grade is right for my project? |
| Hotel Applications | A Hotel Lobby Divider Is Not Just a Screen — It's an Architectural Component | What metal screen survives a hotel lobby? |
| Installation | How the Fixing Method Affects Everything from Shipping to Maintenance | How should I fix a metal room divider to drywall? |
| FAQ | FAQ (fine as-is) | — |

---

## Section Function Audit

Before drafting, audit every H2:

1. What is the reader's mental state here? (Confused? Comparing? Anxious? Deciding?)
2. What structure best serves that state? (Consult the map above.)
3. Is this structure different from the previous section's? If two consecutive sections use the same format because of default habit, break one. If the benchmark's success depends on intentional repetition, keep the rhythm but vary internal tension, proof, examples, or sentence cadence.
4. Does this section's structure match its function? A "Material Selection Guide" should not be prose — use table + judgment. A "Common Mistakes" section should not be a bullet list — use blockquote warnings.

---

## Rhythm Audit Checklist

Before drafting, check the skeleton:

- [ ] No two consecutive sections repeat the same structure lazily; any repeated format is justified by benchmark-native rhythm or reader need
- [ ] At least one section opens with a counterintuitive or surprising statement
- [ ] At least one section is short and punchy (under 150 words) between two longer sections
- [ ] Tables only appear where comparison is genuinely needed
- [ ] Blockquotes only appear for warnings, strong opinions, or client voices — never for marketing
- [ ] Ordered lists only appear for processes or ranked priorities — never as decoration
- [ ] The article does not end with a section that reads like the one before it

---

## Examples

### Input (skeleton with template problem):
```
H2-02: Hotels
  - Design Considerations (bullet list)
  - Recommended Materials (paragraph)
H2-03: Restaurants  
  - Design Considerations (bullet list)
  - Recommended Materials (paragraph)
H2-04: Residential
  - Design Considerations (bullet list)
  - Recommended Materials (paragraph)
```

### Output (structure-varied skeleton):
```
H2-02: Hotel Lobby Divider Is an Architectural Component, Not Decor
  Format: Opinion-led prose + full project spotlight (Riyadh, 200+ panels)
  Reader job: Reframe understanding of what a lobby divider actually does

H2-03: Restaurant Dividers — Two Rules That Prevent the Most Common Regret
  Format: Risk-forward narrative + compact decision pair
  Reader job: Learn from others' mistakes; make faster judgment for dining spaces

H2-04: For Villas, the Material Decision Changes at the Threshold
  Format: Conditional judgment prose + mini case (Dubai, 80 sqm)
  Reader job: Understand indoor vs. outdoor material logic for residential
```

---

## Guardrails

### Anti-Patterns (Do NOT do this)
- Applying the same template format to every application/context section
- Using tables without a judgment paragraph below them
- Using blockquotes for generic marketing text
- Using ordered lists as decoration instead of for actual sequences
- Varying structure randomly — every change must serve a reader need (consult the map)

### When This Skill Should NOT Be Used
- For the FAQ section (its structure is self-evident)
- For sections under 100 words (format variation matters less at micro-scale)
- For pure list-based content like specification sheets

### When to Break the Rules
- A sequence of case studies may use the same format — but vary internal rhythm (one opens with specs, another with a quote, another with a problem statement)
- A very long technical section may need one consistent format for clarity — then vary the NEXT section more aggressively

## Instructions

Execute the steps described in the canonical sequence.
