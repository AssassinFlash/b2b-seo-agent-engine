# Visual Spec — solar-without-a-battery

**Stage:** `/article-visual`  
**Date:** 2026-06-25  
**Article:** `solar-without-a-battery`  
**Design system source:** `project-profile.md` §Visual Design System & Asset Acquisition

---

## Visual Opportunity Audit

| # | Marker / final asset | Section | Cognitive job | Original enrich intent correct? | Corrected intent |
|---|---|---|---|---|---|
| v-01 | `saj-r5-r6-c6-on-grid-inverter-series-overview.webp` | H2-01 opener | Orient the reader with a real product family visual before the Path A/B/C idea | **No** — a generic Path A/B/C diagram would have been too abstract for the first screen | Use a sourced real product lineup image; let the text handle the Path logic |
| v-02 | H2 overview + LCD photo + grid on/off flow diagram | H2-02 definition | Define "battery-ready" through product reality + interface/monitoring + operating mode | **No** — one diagram alone was insufficient | Use a 3-layer visual stack: product overview, LCD screen, and mode-flow diagram |
| v-03 | `saj-net-metering-vs-net-billing-calculator.gif` | H2-03 | Show why tariff structure changes the battery decision | **No** — a pure 3-question flowchart would miss the money logic | Use an animated calculator/curve demonstration |
| v-03b | `saj-three-solar-pathways.webp` | H2-03/H2-05 | Give a hardware-path overview that complements the tariff calculator | **Partly** | Add a static comparison architecture diagram in addition to the GIF |
| v-04 | `saj-dc-vs-ac-coupling-retrofit.gif` + scenario table | H2-04 | Visualize the retrofit trap and energy flow inefficiency | **Yes** on the need for a coupling diagram, **No** on the initial level of detail | Pair the animated coupling diagram with a scenario-led cost table |
| v-05 | Patio install photo + generator sync infographic + FAQ block | H2-05 | Move from abstract path comparison to what owning the system actually looks like | **No** — comparison framework needed more than a plain routing block | Add concrete install/operation visuals and implementation FAQ at the exact readiness point |
| v-06 | 3-column markdown table | H2-06 | Turn red flags into a scannable screening tool | **Partly** | Markdown table beats fancy HTML here — the structure is the visual |
| v-07 | tip/callout block | H2-07 | Make the one installer question feel like a tool, not prose | **Yes** | Lightweight callout is enough; no heavier visual required |
| v-08 | Product cards + H2 outdoor wall photo | H2-08 | Route readers from decision to product + show a real install context for Path B | **No** — prose-only CTA was too weak | Add product cards + one real outdoor install photo to make the path tangible |

---

## v-01: SAJ Product Lineup Orientation Image

### Position
- Section: H2-01
- After paragraph: the article title and before the direct answer opener
- Cognitive job: give the reader a concrete visual of the product family before Path A/B/C distinctions are introduced

### Visual content
A clean product-lineup image showing the SAJ R5/R6/C6 inverter family. The visual should feel like "here are the real hardware families we are talking about," not like a diagram or a sales banner. No extra labels beyond what is already on the sourced image.

### Format
- Output: real photo (sourced image)
- Dimensions: article content width
- File size target: N/A (sourced remote image)
- Path: remote URL (`wp-content/uploads/.../SAJ-R5-R6-C6-On-Grid-Inverter-Series-Overview.webp`)

### Acquisition strategy
#### Priority 1 — Search
- Keywords: `SAJ R5 R6 C6 inverter series overview`
- Platforms: official Sunriver / SAJ pages first
- Denoise word bag: `saj inverter series on-grid grid-tied product overview`
- Volume cap: 10 (official pages only)

#### Priority 2 — Image-to-image AI generation
- Not needed. Real product lineup image exists and is good enough.

#### Priority 3 — HTML synthesis
- Not needed. This is a real product family orientation photo, not a chart.

#### Fallback
- Text-only opening with no image

### Design
- Style: sourced real product image; do not stylize
- Alt text: `SAJ Solar Inverter and Energy Storage System Lineup`

### Truth-bounded check
- No generated labels. The image comes from the official product source.

### Status
- Source found and embedded in final enriched-draft

---

## v-02: Battery-Ready Definition Stack

### Position
- Section: H2-02
- After the H2 heading, before the definition paragraphs and between the product-definition and premium-definition paragraphs
- Cognitive job: define battery-ready through product reality and operating evidence, not just abstract prose

### Visual content
This is a **three-layer stack**:
1. **Product overview photo** of the SAJ H2 hybrid inverter (what the hardware looks like)
2. **LCD monitoring panel photo** showing solar / battery / grid / load status (proof that it has an operating brain and visible state)
3. **Grid On / Grid Off flow diagram** showing how the H2 behaves in normal vs backup modes

The three visuals work together: product body → interface → operating mode.

### Format
- Output: 2 real images + 1 static WebP diagram
- Dimensions: article content width; stack vertically
- File size target: product photo remote, local webp diagrams <100KB each
- Paths:
  - remote product overview URL
  - `https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-h2-lcd-monitor-screen.webp`
  - `https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-h2-grid-on-off-flow.webp`

### Acquisition strategy
#### Priority 1 — Search
- Product overview: keyword `SAJ H2 3-6k hybrid inverter product overview`
- Platforms: official Sunriver / SAJ pages first
- LCD panel: search/harvest from existing local photo or video frames showing live status screen
- Grid On / Off diagram: official manual screenshot or clean HTML-synthesized diagram
- Denoise word bag: `saj h2 hybrid inverter lcd grid on grid off backup mode`

#### Priority 2 — Image-to-image AI generation
- For LCD panel only if a real LCD photo exists but needs enhancement (de-noise, sharpen, crop)
- Base image mandatory: actual H2 LCD photo
- No pure generation of a fake interface screen

#### Priority 3 — HTML synthesis
- Grid On / Off flow diagram may be HTML-synthesized if no official diagram exists
- Static WebP output preferred; labels must be sharp on mobile

#### Fallback
- Prose-only definition with bold anchors

### Design
- Product photo left untouched
- Diagram uses dark background + warm orange accents, Space Mono labels
- Static, not animated — small labels must remain sharp

### Truth-bounded check
- All mode labels and ports must match T1.1 / T1.2
- No invented interface states

### Status
- All three layers exist in current enriched-draft and are embedded

---

## v-03: Net Metering vs Net Billing Animated Calculator

### Position
- Section: H2-03
- After the paragraph explaining net metering vs net billing, before the third qualification question
- Cognitive job: make tariff differences visible as money / credit behavior, not as abstract policy terms

### Visual content
An animated calculator or chart showing how value changes when moving from net metering (full retail credit) to net billing (fractional credit). The visual should make it obvious why battery value changes under NEM 3.0 / net billing. The reader should feel the money logic move, not just read it.

### Format
- Output: animated GIF
- Dimensions: article content width
- File size target: <500KB
- Path: `https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-net-metering-vs-net-billing-calculator.gif`

### Acquisition strategy
#### Priority 1 — Search
- Not applicable. This is not a photo search problem.

#### Priority 2 — Image-to-image AI generation
- Forbidden. This is data visualization, not scene-ization.

#### Priority 3 — HTML synthesis
- Build as interactive HTML (Chart.js line/bar or slider-driven calculator), then capture as GIF
- Data source: the draft's net metering vs net billing explanation + evidence pack policy context
- Animation: curve/credit change, not decorative motion
- Recording: Playwright DOM-selector crop on outer card container, 15fps, 3-4s loop
- Animation constraint: no dashed-line flow, only curve/slider state change

#### Fallback
- Prose-only tariff explanation

### Design
- Dark background, warm orange for net billing negative value, teal/green for net metering value
- Space Mono for labels and numbers

### Truth-bounded check
- Do not invent tariff percentages not in the evidence; keep it conceptual if exact values are unavailable

### Status
- GIF exists and is embedded in current enriched-draft
- Source HTML should be preserved in `html-visuals/v-03.html`

---

## v-03b: Three Solar Pathways Static Diagram

### Position
- Section: H2-03 / H2-05 support layer
- After the animated tariff calculator, before the section's path conclusion bullets
- Cognitive job: show the three hardware pathways in one glance

### Visual content
Three columns side-by-side: Path A string/grid-tied, Path B battery-ready hybrid, Path C all-in-one ESS. Each column should show the hardware composition (panels → inverter → battery/house/grid) with clear labels for R6 / H2 / HS3. This is not a table of numbers — it is an architecture picture.

### Format
- Output: static WebP
- Dimensions: article content width; 3 columns
- File size target: 30-100KB (text must be sharp)
- Path: `https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-three-solar-pathways.webp`

### Acquisition strategy
#### Priority 1 — Search
- Not a search problem; needs custom composition

#### Priority 2 — Image-to-image AI generation
- Not preferred. Small text labels and exact architecture make AI risky.

#### Priority 3 — HTML synthesis
- Build as clean HTML/CSS diagram, then capture to static WebP
- No animation — small labels need maximum clarity on mobile
- Source HTML should be `html-visuals/v-05.html` or a dedicated v-03b source

#### Fallback
- Prose comparison + markdown table (already present)

### Design
- Flat technical style, dark background, warm orange path accents, Space Mono labels

### Truth-bounded check
- R6/H2/HS3 labels and hardware paths must match the article's Path A/B/C definitions

### Status
- Static WebP exists and is embedded in current enriched-draft

---

## v-04: DC-Coupled vs AC-Coupled Retrofit Trap

### Position
- Section: H2-04
- Above the prose cost explanation, paired with a scenario cost table
- Cognitive job: make the retrofit trap tangible through both cost and energy flow

### Visual content
This is a **dual asset**:
1. **Scenario cost table** (in the article body) — Day 1 Hybrid vs AC-Coupled Retrofit vs Inverter Swap
2. **Animated flow schematic** — DC-coupled path (short, clean, efficient) vs AC-coupled path (extra inverter, extra conversion, red/slow)

The table proves the money. The GIF proves the mechanism.

### Format
- Output: markdown table + animated GIF
- GIF file size target: <500KB
- Path: `https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-dc-vs-ac-coupling-retrofit.gif`

### Acquisition strategy
#### Priority 1 — Search
- Not a search problem; the key visual is a synthesized technical schematic

#### Priority 2 — Image-to-image AI generation
- Not preferred. Technical topology and labels must be exact.

#### Priority 3 — HTML synthesis
- Build as HTML+CSS flow schematic
- Animate only direction arrows / color emphasis
- No dashed-line flow animation (it flickers and blurs labels)
- Playwright DOM-selector crop, 15fps, 3-4s loop

#### Fallback
- Prose-only cost scenarios (already present)

### Design
- Teal for DC-coupled efficient path, red for AC-coupled retrofit path
- Dark background, Space Mono labels

### Truth-bounded check
- Coupling topology must match T1.1 and H2-04's prose
- No invented efficiency percentages if not sourced

### Status
- GIF exists and is embedded in current enriched-draft
- Cost table is present in markdown above it

---

## v-05: Path Comparison Context Support

### Position
- Section: H2-05
- After the path comparison table, inside FAQ Group 1
- Cognitive job: make the installation/compatibility consequences feel real with a physical install photo and generator sync visual

### Visual content
A **context support package**:
1. Patio-covered residential install photo (`saj-inverter-patio-covered-installation.webp`) inside FAQ Group 1, under install-time answer
2. Generator synchronization infographic (`saj-ess-generator-charging-sync.webp`) inside the generator-compatibility FAQ

This is less a single visual and more a visual reinforcement layer for the FAQ group.

### Format
- Output: 2 real/static images embedded inline inside FAQ answers
- Paths:
  - `https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-inverter-patio-covered-installation.webp`
  - `https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-ess-generator-charging-sync.webp`

### Acquisition strategy
#### Priority 1 — Search
- Patio install photo: local or sourced real installation shot
- Generator sync infographic: official technical diagram or clean extracted image from documentation

#### Priority 2 — Image-to-image AI generation
- Patio install photo may be enhanced if low quality (enhance mode only)
- Generator infographic should not be AI-generated unless based on a real diagram; prefer search or HTML synthesis

#### Priority 3 — HTML synthesis
- If no generator infographic exists, HTML synthesis is preferred to AI generation because labels and flow must be accurate

#### Fallback
- FAQ prose only

### Design
- Real-world photos retain their realism; no stylization required

### Truth-bounded check
- Generator sync behavior must match the linked technical source; do not imply generator support if the model cannot do it

### Status
- Both visuals are present in current enriched-draft, embedded within FAQ Group 1

---

## v-06: Red-Flag Screening Table

### Position
- Section: H2-06
- At the start of the section, before the 7-item prose list
- Cognitive job: compress quote red flags into a scanning table before the prose explains them

### Visual content
Three-column table:
- What the quote says
- What it actually means (the trap)
- What you should ask the installer

This is the visual. No separate image is needed.

### Format
- Output: markdown table
- No external asset

### Acquisition strategy
- No search
- No AI generation
- No HTML synthesis (markdown table is superior here)

#### Fallback
- The existing 7-item numbered list (already present)

### Design
- Use markdown only; structure is the visual

### Truth-bounded check
- Each row's interpretation must align with H2-06 prose and T1/T2 constraints

### Status
- Table exists in current enriched-draft

---

## v-07: Installer Question Action Anchor

### Position
- Section: H2-07
- At the start of the section, before explanatory prose
- Cognitive job: make the one question feel like a tool the reader can use immediately

### Visual content
A lightweight callout block emphasizing the exact question. No additional image. The visual job is typographic emphasis, not illustration.

### Format
- Output: markdown blockquote or callout (current enriched-draft uses a callout block)
- No external asset

### Acquisition strategy
- No search
- No AI generation
- No HTML synthesis required

#### Fallback
- Plain blockquote

### Design
- Minimal; question should stand out but not look like an ad banner

### Truth-bounded check
- The question text must match the body and the expert stance backing it

### Status
- Callout block exists in current enriched-draft

---

## v-08: Product-Routing Close

### Position
- Section: H2-08
- At the start of the section (product cards) and in the closing accordion / CTA block
- Cognitive job: route the reader from understanding to a concrete product page, while making the products feel real and available

### Visual content
This is a **mixed package**:
1. Three product cards with official product images (R6, H2, HS3) + "Best for" copy + Learn More link
2. One real outdoor wall-mount install photo for Path B to prove the hybrid is not just a datasheet
3. Routing box and closing CTA

### Format
- Output: 3 remote product images + 1 local real install photo + markdown/accordion structure
- Paths:
  - remote R6 product image
  - remote H2 product image
  - local `https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-h2-outdoor-wall-installation.webp`
  - remote HS3 product image

### Acquisition strategy
#### Priority 1 — Search
- Official product photos from Sunriver / SAJ pages
- Local install photo from sourced video/social or local capture

#### Priority 2 — Image-to-image AI generation
- The Path B install photo may be enhanced or scene-ized if a real H2 outdoor wall-mount photo exists but needs cleanup
- Base image mandatory

#### Priority 3 — HTML synthesis
- Not required — cards are content cards, not a diagram

#### Fallback
- Prose-only CTA links (already the previous fallback)

### Design
- Product cards should visually align with the design system but respect the real product photos

### Truth-bounded check
- Product model names and use-case copy must match T1.1 / T1.3 / T1.4 / T1.7

### Status
- Cards and install photo are present in current enriched-draft

---

## Summary

| # | Format | Primary acquisition path | Status |
|---|---|---|---|
| v-01 | Real photo | Search | Embedded |
| v-02 | Real photo + static WebP | Search / local / HTML-synthesized diagram | Embedded |
| v-03 | Animated GIF | HTML synthesis | Embedded |
| v-03b | Static WebP | HTML synthesis | Embedded |
| v-04 | Markdown table + Animated GIF | HTML synthesis | Embedded |
| v-05 | Real photo + infographic in FAQ | Search / local | Embedded |
| v-06 | Markdown table | No visual asset needed | Embedded |
| v-07 | Markdown callout | No visual asset needed | Embedded |
| v-08 | Real product photos + local install photo | Search / local | Embedded |

---

## Visual Library Updates

New assets used in this article that should be registered in the project visual library:

| Asset | Type | Source | Tags | Reusable? |
|---|---|---|---|---|
| `saj-three-solar-pathways.webp` | static diagram | HTML synthesis | `path-a,path-b,path-c,comparison,hybrid,string,ess` | yes |
| `saj-net-metering-vs-net-billing-calculator.gif` | animation | HTML synthesis | `net-metering,net-billing,nem-3.0,tariff,battery-value` | yes |
| `saj-dc-vs-ac-coupling-retrofit.gif` | animation | HTML synthesis | `dc-coupled,ac-coupled,retrofit,hybrid,string` | yes |
| `saj-h2-lcd-monitor-screen.webp` | real photo | local/sourced | `saj-h2,lcd,monitoring,grid-on,grid-off` | yes |
| `saj-h2-grid-on-off-flow.webp` | diagram | local/sourced | `saj-h2,grid-on,grid-off,flow` | yes |
| `saj-inverter-patio-covered-installation.webp` | install photo | local/sourced | `install-photo,patio,hybrid,inverter` | yes |
| `saj-h2-outdoor-wall-installation.webp` | install photo | local/sourced | `install-photo,outdoor,wall-mount,saj-h2` | yes |
