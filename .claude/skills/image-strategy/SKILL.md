---
name: image-strategy
description: "Use when: (1) marking visual opportunity hints in /article-skeleton section contracts, (2) judging what kind of visual a paragraph needs (photo / diagram / comparison / proof / no visual), and (3) helping /article-visual choose the right acquisition path and output format. This skill is reference logic only. /article-enrich places markers; /article-visual expands them into executable specs, multi-channel search instructions, image-to-image AI prompts, and HTML synthesis plans."
user-invocable: false

---

# Image Strategy

## Purpose

Images are not decoration, but they are also not the article's main product. They are supporting evidence and explanation tools placed where the reader needs to **see** something to understand, trust, compare, or continue reading. Never place images per H2 count — place them per cognitive decision point.

`image-strategy` is the **judgment layer** of the visual pipeline. It decides:
- whether a visual belongs at all,
- what role the visual serves,
- which format is most suitable (real photo / static WebP / GIF / interactive HTML / markdown table / no visual),
- and which acquisition path makes sense (search / image-to-image AI generation / HTML synthesis).

It does **not** own execution. `/article-enrich` places visual markers only. `/article-visual` expands those markers into executable specs using this skill plus `visual-material-hunt` and `article-html-visuals`.

## When to Use (v3.0 visual pipeline)

- `/article-skeleton`: mark **visual opportunity hints** in each section contract. State what the visual job is, not how to source it.
- `/article-draft`: **pure prose only**. No image placeholders, no accordions, no resource blocks.
- `/article-enrich`: place only `<!-- visual: v-XX -->` markers and a minimal image-plan placeholder if needed. Do not expand into sourcing logic here.
- `/article-visual`: read the markers and use this skill to choose the visual role, format, and acquisition path. This is where the detailed spec is produced.
- `/article-publish-pack`: make the final asset selection from `visual-spec.md` and the project visual library; do not regenerate visual strategy from scratch.

---

## The 7 Article Image Roles

Every image must have a defined task. Classify before placing.

### 1. Opening Anchor — Above-the-Fold Anti-Pogo Micro-Anchor

**Task**: Help the reader immediately orient or route themselves within the first viewport (Google Navboost anti-pogo-sticking) WITHOUT pushing the opening answer below the fold.

**Placement**: Integrated alongside or right after the first 120–180 words — **never** a giant full-screen decorative stock hero banner above the text that forces the reader to scroll before seeing the answer.

**Best content**: Compact 3-path hardware/material router strip, annotated side-by-side real install comparison, or real project/application cut-away that proves immediate technical authority.

**For metal room divider**: hotel lobby, restaurant interior, villa living room, commercial space — the product IN a real space.

**Placeholder format**:
- Markdown visible placeholder: `![alt text with keywords](https://placehold.co/1200x700 "title")`
- Planning route in `image-plan.md` when availability is uncertain

### 2. Context Image — Application Scene

**Task**: Help the reader imagine the product in THEIR project. Each context image should show a DIFFERENT design decision, not the same product in different rooms.

**Placement**: Application H2s. But NOT one per H2. Use only when the image shows a decision difference (scale, finish, material, environment).

| Scene | What the image should demonstrate |
|---|---|
| Hotel | Large scale, high ceiling, zone without blocking sightlines |
| Restaurant | Semi-private zones, warm lighting, easy-clean finish |
| Villa | Indoor decoration, light/shadow, luxury texture |
| Office | Brand pattern, modular, commercial feel |
| Outdoor | 316 SS, weather resistance, pool/courtyard/facade |

**Rule**: If two context images look interchangeable, use only one of them.

**Placeholder format**:
- Markdown visible placeholder: `![alt text with keywords](https://placehold.co/900x600 "title")`
- Planning route in `image-plan.md` when availability is uncertain

### 3. Detail Image — Material & Process Close-Up

**Task**: Make abstract technical differences visible. Show what words cannot describe.

**Placement**: Material sections, finish sections, process sections.

**Examples**: PVD color swatches, brushed vs mirror comparison, surface texture close-up, edge quality, weld detail.

**Placeholder format**:
- Markdown visible placeholder: `![alt text with keywords](https://placehold.co/900x600 "title")`
- Planning route in `image-plan.md` when availability is uncertain

### 4. Comparison Visual — Side-by-Side Decision Support

**Task**: Help the reader choose between options at a glance.

**Placement**: Whenever the reader needs to compare: 304 vs 316, laser vs perforated vs expanded, brushed vs mirror, PVD vs powder coat, mounting methods.

**Format**: Side-by-side photo, 3-column diagram, or annotated comparison image.

**Placeholder format**:
- Markdown visible placeholder: `![alt text with keywords](https://placehold.co/1000x650 "title")`
- Planning route in `image-plan.md` or `html-visual-plan.md`

### 5. Diagram / Annotated Visual — Explanation Graphic

**Task**: Explain a concept that is hard to grasp from text alone. This is the most underused and highest-value image type for B2B manufacturing articles.

**Placement**: Open area explanation, privacy/light/airflow trade-off, fixing methods, panel rigidity, QC workflow, export packing layers.

**Examples**: Diagram showing 20%/40%/60% open area differences. Cross-section of mounting methods. Production workflow with QC gates marked.

**Generation priority**: Diagrams, explainers, and decision cards are often better as HTML expression blocks than as photos. A clear process strip or comparison matrix can beat a blurry factory photo, but do not create one unless it improves this exact paragraph.

**Placeholder format**:
- Markdown visible placeholder: `![alt text with keywords](https://placehold.co/1000x650 "title")`
- Route note below it when more than one route is plausible. HTML expression blocks should be planned with `article-html-visuals`.

### 6. Forensic Proof Image — Caliper, Test-Bench & Pass/Fail QC Evidence

**Task**: Prove you are not making empty supplier claims. Show forensic, un-faked workshop and field reality: caliper/micrometer readings, oscilloscope/multimeter captures, salt-spray or load-test results, and **Pass vs. Fail defect anatomy** (e.g., what a burned heat-affected weld zone or under-rated terminal block actually looks like).

**Placement**: QC sections, specification sections, red-flag teardown sections, case study sections.

**Examples**: Inspector measuring 2.0 mm wall thickness with digital caliper, side-by-side Pass vs. Fail PVD batch comparison, crate moisture-barrier packing layers, drawing-to-product verification.

**Key principle**: Glossy AI-looking renders destroy B2B trust. Forensic specificity and annotated Pass/Fail boundaries build immediate engineering credibility.

**Placeholder format**:
- Markdown visible placeholder: `![alt text with keywords](https://placehold.co/900x600 "title")`
- Planning route in `image-plan.md` when availability is uncertain

### 7. Optional Next-Step Visual

**Task**: Support a final quote checklist, spec handoff, or "what to send" moment. Rarely needed — most article CTAs are better as text or links.

**Placement**: Near final CTA, quote checklist, or "what to send" section.

---

## The 5-Question Gate (ask before placing any image)

1. **Can the reader understand this without an image?** If yes → skip.
2. **Does this position need trust-building?** If yes -> the primary route should be a real proof image, never AI-generated.
3. **Is there a complex comparison here?** If yes → table or comparison visual. Sometimes a table alone is better.
4. **Is this a reader fatigue point?** If yes → light visual to shift reading mode.
5. **Would an image here break the logical flow?** If yes → delay until the argument completes.

### Truth-Bounded Generation Rules

- If the paragraph needs **trust-building** (proof, installation, product appearance), the primary route should be a **real photo** or an **image-to-image AI generation** whose base is a real photo. Never use pure text-to-image for B2B product visuals.
- If the paragraph needs **precise technical information** (ports, voltage labels, energy flow, system topology, exact numbers), prefer **HTML synthesis** over AI generation. AI should not invent technical schematics or spec labels.
- If the paragraph needs a **conceptual comparison** or **scene-ized product shot**, image-to-image AI is valid — but the base image must be a real product photo, and the prompt must state what must not change (model, interface count, product proportions).
- If no suitable real base photo exists and the visual would require pure text-to-image, the route should downgrade to HTML synthesis or text/table fallback.

Every approved visual opportunity in the enriched draft needs a realistic availability path. Use multiple routes when uncertainty is high, but do not force four choices when one strong real asset, one clear HTML block, or no visual is obviously best.

Before enrichment, choose an exact **visual mix control** for the current article and justify it. Example: real proof/photos 40%, HTML expression blocks 35%, text/table fallback 25%. The values must total 100, but they are directional planning controls, not quotas.

| Route | When to Use | Asset Type |
|---|---|---|
| Primary real-image/media route | Best available real image: project photo, factory proof shot, real sample, product detail, or approved video | Real photo / verified media |
| Backup or reserve route | Useful external candidate, detail crop, stock concept, or alternate real asset when the primary route is unavailable | Source-backed candidate / alternate asset |
| Text/table/no-visual route | The section is clearer without an image, or a simple table/checklist is enough | Text / table / no visual |
| HTML expression route | Decision card, comparison matrix, explainer, process strip, spec card, or chart when HTML helps more than a photo | HTML component / static fallback / antv chart |

**Selection rule**: The operator (or publish-pack stage) picks the highest-quality route that is actually available. Do not force a real-photo route if it does not exist. A low-quality real photo damages trust more than a well-chosen diagram, HTML block, table, or no image.

**For Diagram / Explanation visuals (type 5), HTML expression is often the best route, not an automatic route.** Use `article-html-visuals` when the section needs a decision card, comparison matrix, process strip, spec card, annotated explainer, or static fallback.

### Route Design Principles

- The primary route should be the best honest route: real project, real context, real proof, or a clearly superior HTML expression.
- The backup route should be a practical substitute: same reader job, different source or format.
- The fallback route should still serve the cognitive decision point: detail crop, table, checklist, HTML block, or no visual.
- Use HTML expression for article-native explanation blocks, not just charts.
- If real-image/media routes need external sourcing, use `visual-material-hunt` and then `article-visual-fit`. Do not invent source paths or accept search pages, captcha pages, or profile pages as image assets.
- If HTML expression is selected, use `article-html-visuals` to plan the component, output mode, and render check.

Example for an opening/application scene:
- Primary: Real Riyadh hotel lobby photo (full scene)
- Backup: Source-backed concept/application photo
- Fallback: Text-only opening or finish close-up if it still helps
- HTML expression: usually not needed for opening scene photos, unless a short orientation answer block helps more than a scene image

Example for a 5-gate QC process diagram:
- Primary: Real factory photo of QC inspection station if it proves the process
- Backup: Source-backed process image or detail crop
- Fallback: Text-only numbered list describing the 5 gates
- HTML expression: a hand-crafted process strip with numbered steps, proof gates, and a static fallback screenshot, only if it improves understanding

---

## Chart Generation via antv MCP (When Available)

The `@antv/mcp-server-chart` provides chart tools for cases where actual chart output is needed. Use `mcp__antv-chart__generate_*` only when the article has chart-worthy data and the server is connected.

See `references/antv-chart-tools.md` for the antv MCP tool reference. Use `article-html-visuals/references/html-expression-patterns.md` for article-native HTML components that are broader than charts.

---

## HTML Expression Blocks

When no suitable real photo exists, or when a real photo would not explain the decision, consider an HTML expression block. This is not a last-resort generated visual. It is a first-class article presentation method for decision cards, comparison matrices, process strips, spec cards, risk maps, annotated explainers, and AIO answer blocks.

Use `article-html-visuals` for component choice, fixed-canvas/static fallback decisions, and render checks. Keep this skill focused on whether the visual moment belongs in the article at all.

### When To Consider HTML Expression

- The article has a decision point that needs visual compression.
- A comparison would be easier as a card/matrix than as prose.
- The section needs an answer block for AIO, but fixed snippet formatting would hurt the prose.
- A photo exists but would be decorative or misleading.
- The benchmark uses modular visual rhythm and the current draft is visually flat.

### HTML Expression Route

```markdown
**HTML Expression Route**
- Component: Process Strip
- Concept: 5-gate QC process from design review to pre-shipment photo
- Placement: after the 5-gate checklist, before closing paragraph
- Alt text (for screen readers): Five-gate quality control process for custom metal screen manufacturing
- Output format: responsive HTML embed + optional static PNG/WebP fallback
```

---

## Placeholder And Route Format

Every visual opportunity in `image-plan.md` must be traceable. In `enriched-draft.md`, use the lightest format that preserves reader flow:

1. A visible Markdown placeholder when the final output is an image or static fallback.
2. An HTML component marker when the final output is an embedded HTML block.
3. A route note when availability, licensing, or format is still undecided.

### Visible Markdown Placeholder

This renders as a gray box in preview and makes the image position unambiguous:

```markdown
![Alt text with keywords](https://placehold.co/1200x700 "Title text")
```

Rules:
- `alt` must include the target keyword naturally
- `title` should describe the intended image in human terms
- dimensions must match the image role (Opening Anchor: 1200x700 when used, Context/Detail/Proof: 900x600, Comparison/Diagram: 1000x650)

### Route Note

When a route note is useful, include only the fields needed to make a publish decision. Use the 7-field version for real image sourcing; use the HTML expression version for components.

| # | Field | Description | Example |
|---|---|---|---|
| 1 | **Source file** | Path to the actual image file (to be filled later) | `visuals/metal-divider/riyadh-hotel-lobby-rose-gold-pvd.webp` |
| 2 | **Placement** | Exact sentence/paragraph after which the image appears | "After the spec-stats lede, before 'Why 316?'" |
| 3 | **Suggested capture** | What to frame, angle, or highlight | "Wide shot showing full-height PVD Rose Gold divider spanning the lobby atrium" |
| 4 | **Alt text** | Concise, descriptive, SEO-friendly | "Custom PVD Rose Gold stainless steel metal room divider installed in luxury hotel lobby in Riyadh" |
| 5 | **Caption suggestion** | One-line context for the reader | "PVD Rose Gold stainless steel divider — Riyadh luxury hotel lobby, 212 panels" |
| 6 | **Web search keywords** | Keywords to find this image | "PVD rose gold stainless steel hotel lobby divider large scale" |
| 7 | **AI image prompt** (optional) | If the image needs to be generated | "Photorealistic architectural interior of a luxury hotel lobby with full-height PVD rose gold stainless steel decorative screen" |

HTML expression option fields:

| Field | Meaning |
|---|---|
| Component | Decision card, comparison matrix, risk map, process strip, spec card, annotated explainer, AIO answer block |
| Reader job | What the block helps the reader decide or understand |
| Placement | Exact paragraph/section moment |
| Evidence | Source IDs for claims and numbers |
| Output mode | Responsive embed, fixed article card, static fallback, or inline micro-block |
| Render check | Whether `visual-render-check.md` is required |

### Lightweight Example in Enriched Draft

Keep the article body readable. Put selection details in `image-plan.md`, `html-visual-plan.md`, or `visual-fit-review.md`.

```markdown
## Hotel lobbies punish materials

`212 panels`. `316 stainless`. `Rose Gold PVD`. `±0.1mm`. Riyadh.

![Custom PVD Rose Gold stainless steel metal room divider installed in a hotel lobby](https://placehold.co/1200x700 "PVD Rose Gold hotel lobby divider")

Why 316? The Saudi climate...
```

Planning note in `image-plan.md`: primary real project route if the verified project photo exists; otherwise reserve a source-backed application photo or leave the opening text-only.

### Bare Format (for lightweight or obvious placements)

When a full route note is overkill (e.g., a simple icon or diagram where the operator will obviously generate it), the minimal format is acceptable:

```markdown
![alt text with keywords](https://placehold.co/WxH "title")
```

Do not expand every visual into a long option block inside the article body. Keep detailed selection logic in `image-plan.md`, `html-visual-plan.md`, or `visual-fit-review.md`.

---

## Dynamic Visual Mix By Article Type

Use article type as a starting point, then choose exact working percentages for the current article. The numbers are planning controls to help the agent avoid drifting too far, not quotas.

| Article Type | Real photos / proof | HTML expression blocks | Simple tables / no visual | Typical bias |
|---|---|---|---|---|
| Buyer's Guide | 25-45% | 30-50% | 15-35% | compare and decide |
| Application Guide | 45-70% | 10-30% | 10-25% | show context and fit |
| Technical Deep-Dive | 10-35% | 40-65% | 10-30% | explain mechanisms |
| Case Study | 65-90% | 0-20% | 5-20% | prove the real project |
| Cost Guide | 10-35% | 35-60% | 15-35% | make tradeoffs visible |

The agent must write the chosen mix in the plan preview. Example: `real proof/photos 30%, HTML expression blocks 45%, simple table/no visual 25%`. If the best article needs zero HTML blocks, that is acceptable. If it needs several, justify the reader job for each.

---

## Examples

### Input (section text):
```
For most indoor dividers, 304 stainless steel is enough. 
The decision changes when the divider moves outdoors or 
into a more aggressive environment.
```

### Output (with visual opportunity marked):
```
For most indoor dividers, 304 stainless steel is enough. 
The decision changes when the divider moves outdoors or 
into a more aggressive environment.

<!-- html-visual: material-grade-comparison-card -->
```

### Input (weak image placement — every H2 gets a photo):
```
## Hotels — [insert photo of gold divider]
## Restaurants — [insert photo of gold divider]  
## Villas — [insert photo of gold divider]
```

### Output (correct — only where each image shows a different decision):
```
## Hotels — ![large-scale PVD gold stainless steel room divider spanning hotel lobby atrium](url "title")
  (Shows: scale, ceiling height, zone without blocking sightlines)
  (Selection details live in image-plan.md)

## Restaurants — [no image — the zoning logic is better served by text + a decision rule]

## Villas — ![mirror PVD gold metal screen divider reflecting natural light in Dubai villa living room](url "title")
  (Shows: indoor light interaction, luxury residential context — different decision from hotel scale)
  (Selection details live in image-plan.md)
```

---

## Guardrails

### Anti-Patterns
- Placing one image per H2 regardless of need
- Using the same type of project photo for every application section
- Opening image showing a factory or machine when the article needs an application scene
- Forcing a real-photo route when only a low-quality or irrelevant real photo exists
- AI-generated images presented as real project photos (destroys credibility)
- Providing only one option when availability is uncertain
- Skipping traceability and only writing decorative metadata
- Adding a chart or HTML block because the template expects one
- Using a blurry photo of a whiteboard sketch when a clean generated flowchart would be clearer

### When to Skip Images
- Strong opinion paragraphs in flow (let the argument land)
- Short transition sections
- Sections adequately served by a table or checklist
- When no image/media/HTML route would add value

### When to Use HTML Expression Instead of Photograph
- Process explanations where the sequence matters more than the environment.
- Decision frameworks where the reader needs a rule, not atmosphere.
- Material comparisons where differences should be visible at a glance.
- QC/process sections where a photo is weak proof but a process strip clarifies expectations.
- Specification references where a compact card is more useful than a decorative photo.
- AIO answer moments where a concise block helps without forcing snippet-like prose.

### Material Quality Overrides
If real project photos are abundant and high-quality → lead with them, structure article as Application Guide or Case Study.
If only factory photos are available → lean toward Buyer's Guide or Technical Deep-Dive structure. Do not pretend to have project evidence you cannot show.
If no real images exist → use diagrams and tables. Do not fill the article with AI-generated fake project images.

## Instructions

Execute the steps described in the canonical sequence.
