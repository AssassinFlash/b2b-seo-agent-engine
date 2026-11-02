# HTML Chart And Infographic Pattern Library

This file is a chart/diagram reference for B2B article enrichment. It is not the full HTML expression layer.

For article-native HTML components such as decision cards, risk maps, procurement checklists, AIO answer blocks, spec cards, and render fallback planning, use `article-html-visuals` and `article-html-visuals/references/html-expression-patterns.md`.

Use this file only when the article needs a chart-like or diagram-like pattern. The antv MCP tool names are retained for Codex users; in Claude Code, implement the HTML pattern directly.

---

## How to Use This Reference

When you encounter a chart or diagram opportunity in an article, scan the **Article Scenario** column to find the matching B2B context. Then jump to the **HTML Pattern** section for the implementation approach. Every pattern can be enriched with CSS animations only when the motion serves comprehension, not decoration.

## Design Principles

1. **Visual-first**: Bars, icons, and charts convey the message. Text is annotation only.
2. **One takeaway per visual**: If the reader scans it in 3 seconds, they should get the point.
3. **Large canvas, low density**: Give elements room. A bigger infographic with whitespace beats a cramped one.
4. **See the difference**: Comparisons should make differences visible at a glance — bar lengths, color contrast, size variation.
5. **Real data only**: Every number in an infographic must come from Tier 1 or Tier 2 evidence.

---

## Flow & Process

### 1. Process Flow → Horizontal Arrow Chain

**Article scenario**: Manufacturing process, QC workflow, spec review steps, buyer journey stages

**HTML pattern**: Horizontally arranged circles or cards connected by arrow SVGs. Each step has: numbered circle (distinct color), title, one-line description, duration/status badge.

**Antv equivalent** (Codex): `generate_flow_diagram`

**Example**: [infographic-5gate-qc.html] — 5-gate QC from Design Review to Pre-Shipment Photo

```
Layout:  [1] → [2] → [3] → [4] → [5]
Colors:  Each step a distinct brand color
Animation: Pulse on the first/active step
```

### 2. Root Cause Analysis → Fishbone Diagram

**Article scenario**: Why screens fail, why installations go wrong, defect analysis

**HTML pattern**: Central horizontal spine with angled branches (cause categories) and leaf nodes (specific causes). CSS transforms for the angled branches, thin lines for the spine.

**Antv equivalent** (Codex): `generate_fishbone_diagram`

### 3. Stage Progression → Funnel

**Article scenario**: Buyer journey, specification process, lead qualification stages

**HTML pattern**: Stacked trapezoid shapes (CSS clip-path or border tricks), widest at top narrowing to bottom. Each stage labeled with the count or percentage that passes through.

**Antv equivalent** (Codex): `generate_funnel_chart`

### 4. Data Flow → Sankey Diagram

**Article scenario**: Material flow, budget allocation, energy/cost breakdown

**HTML pattern**: Left-to-right flow bands with varying thickness. CSS flex columns with proportional heights connected by SVG curved paths. Rare in B2B manufacturing articles — use only when flow volume matters.

**Antv equivalent** (Codex): `generate_sankey_chart`

---

## Comparison & Ranking

### 5. Horizontal Comparison → Bar Chart

**Article scenario**: Cost comparison, lead time comparison, performance ranking

**HTML pattern**: Labeled horizontal bars with proportional widths. Each bar: material name on left, colored bar (gradient fill), value label inside or beside. Grouped bars for multi-item comparison. Winner gets distinct treatment (bold, accent color, badge).

**Antv equivalent** (Codex): `generate_bar_chart`

**Example**: 304-vs-316 cost bars — 304 at 62% width, 316 at 87% width, Al at 50%. Instant visual comparison.

```
304  ████████████████████████████████░░░░░░░░░░░░  baseline
316  ██████████████████████████████████████████████  +40%
Al   █████████████████████████████░░░░░░░░░░░░░░░░   −20%
```

### 6. Vertical Comparison → Column Chart

**Article scenario**: Side-by-side category comparison where vertical reading feels more natural

**HTML pattern**: Flex columns of varying heights standing on a baseline. Each column: label below, height proportional to value, color fill. Useful when comparing 3-5 items with a strong "tallest wins" narrative.

**Antv equivalent** (Codex): `generate_column_chart`

### 7. Multi-Dimension → Radar / Spider Chart

**Article scenario**: Material selection across dimensions (corrosion, cost, weldability, strength, finish)

**HTML pattern**: Polygon overlay on a circular axis grid. SVG polygon points for each grade, different stroke/fill colors. 5-6 axes labeled around the perimeter. Best for "holistic comparison" where no single dimension tells the story.

**Antv equivalent** (Codex): `generate_radar_chart`

### 8. Two-Variable Relationship → Scatter Plot

**Article scenario**: Open area % vs privacy level, cost vs complexity, thickness vs weight

**HTML pattern**: SVG or CSS grid with positioned dots. X and Y axes labeled. Each dot = one data point (product, project, material). Trend line optional.

**Antv equivalent** (Codex): `generate_scatter_chart`

### 9. Dual-Axis → Compound Chart

**Article scenario**: Cost (left axis) vs durability/years (right axis) on same chart

**HTML pattern**: Two overlaid datasets with different Y-axis scales. Left axis in one color, right axis in another. Bars for one metric, line/area for the other. Use only when the relationship between two different-unit metrics is the story.

**Antv equivalent** (Codex): `generate_dual_axes_chart`

---

## Distribution & Statistics

### 10. Distribution → Histogram

**Article scenario**: Tolerance distribution, panel thickness variation, delivery time spread

**HTML pattern**: Vertical bars of varying heights, touching (no gaps). X-axis = value ranges, Y-axis = frequency. Narrow technical use — only deploy when the distribution shape IS the insight.

**Antv equivalent** (Codex): `generate_histogram_chart`

### 11. Quartile Summary → Boxplot

**Article scenario**: Lead time variability, cost range by supplier, quality metric spread

**HTML pattern**: Horizontal boxes with whisker lines. Box = IQR, center line = median, whiskers = range. CSS flex with positioned pseudo-elements. Technical look — pair with a one-sentence takeaway.

**Antv equivalent** (Codex): `generate_boxplot_chart`

### 12. Distribution + Density → Violin Plot

**Article scenario**: Detailed tolerance analysis, statistical quality reporting

**HTML pattern**: Mirrored density curves (SVG path). Very niche for B2B articles — only use when the audience is engineers and the data supports statistical rigor.

**Antv equivalent** (Codex): `generate_violin_chart`

---

## Proportion & Composition

### 13. Part-to-Whole → Donut / Pie Chart

**Article scenario**: Market share, material usage breakdown, project type distribution

**HTML pattern**: SVG circle with stroke-dasharray for segments. Donut preferred over pie (cleaner, space for center label). Max 4-5 segments. Label directly on or beside segments — no legend required for 5 or fewer.

**Antv equivalent** (Codex): `generate_pie_chart`

### 14. Single Proportion → Liquid / Gauge

**Article scenario**: Open area percentage (40%), material purity, completion rate

**HTML pattern**: Large number with a circular progress ring (SVG stroke-dashoffset). The number IS the visual. Use when ONE percentage is the entire story.

**Antv equivalent** (Codex): `generate_liquid_chart`

### 15. Hierarchical Size → Treemap

**Article scenario**: Product categories by revenue, content pillars by traffic

**HTML pattern**: Nested rectangles sized by value. CSS grid with proportional areas. Limited B2B application — mostly for internal dashboards, not reader-facing articles.

**Antv equivalent** (Codex): `generate_treemap_chart`

### 16. Set Overlap → Venn Diagram

**Article scenario**: Design ∩ Specification ∩ Procurement, Material ∩ Application ∩ Budget

**HTML pattern**: Overlapping circles (CSS border-radius + absolute positioning, or SVG). Intersection areas highlighted. Best for showing "projects that satisfy ALL three constraints."

**Antv equivalent** (Codex): `generate_venn_chart`

---

## Structure & Organization

### 17. Hierarchy → Org Chart

**Article scenario**: Project team structure, supplier evaluation hierarchy, decision-maker map

**HTML pattern**: Top-down tree with connecting lines. Each node: name, role, optional photo placeholder. CSS flex columns connected by thin borders or SVG lines.

**Antv equivalent** (Codex): `generate_organization_chart`

### 18. Concept Map → Mind Map

**Article scenario**: Content pillar visualization, keyword cluster map, product feature tree

**HTML pattern**: Central node with radiating branches. Curved SVG paths from center to leaf nodes. Different branch colors for categories. Works well as a table-of-contents alternative.

**Antv equivalent** (Codex): `generate_mind_map`

### 19. Relationship Map → Network Graph

**Article scenario**: Internal linking architecture, supplier-partner network, material-application matrix

**HTML pattern**: Nodes (circles) connected by lines (edges). Force-directed layout via CSS positioning or D3.js. More complex to implement — reserve for articles where relationships ARE the story.

**Antv equivalent** (Codex): `generate_network_graph`

---

## Time & Trend

### 20. Trend Line → Line Chart

**Article scenario**: Material price over time, shipping cost trends, production volume growth

**HTML pattern**: SVG polyline with data points. X-axis = time, Y-axis = value. Multiple lines for comparison. Annotate inflection points. Keep gridlines subtle.

**Antv equivalent** (Codex): `generate_line_chart`

### 21. Cumulative Trend → Area Chart

**Article scenario**: Stacked project volume over years, cumulative cost savings

**HTML pattern**: SVG filled area under a line. Gradient fill from line color to transparent. Good for "growth over time" narratives.

**Antv equivalent** (Codex): `generate_area_chart`

---

## Geographic

### 22-24. Map Visuals → (Use with caution)

**Article scenario**: Factory locations, project pins on world map, shipping routes

**HTML pattern**: A simplified vector world map (SVG) with colored dots or paths overlaid. Or skip the map entirely and use a clean location-card grid. Real geographic maps add complexity — only use when geography IS the insight.

**Antv equivalent** (Codex): `generate_district_map`, `generate_pin_map`, `generate_path_map`

---

## B2B-Specific Patterns (No Chart Tool Equivalent)

These are custom HTML patterns for B2B manufacturing articles. Chart tools can't make these — only HTML can.

### 25. Specification Card Grid

**Article scenario**: Tolerance comparison, PVD color swatches, material grade summary

**HTML pattern**: Flex grid of 3-5 cards. Each card: distinctive SVG icon (different per card), large number, label, one-line description. Color-coded per category. This is the most versatile B2B pattern — use it anywhere you have 3-5 related specs to show at a glance.

**Example**: Laser ±0.1mm | Perforation ±0.2mm | Expanded ±0.5mm | PVD 20+ colors

```
┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│  🔵 icon  │  │  🟢 icon  │  │  🟣 icon  │  │  🟡 icon  │
│  ±0.1mm  │  │  ±0.2mm  │  │  ±0.5mm  │  │   20+    │
│  Laser   │  │  Perf.   │  │  Expand. │  │  Colors  │
└──────────┘  └──────────┘  └──────────┘  └──────────┘
```

### 26. Side-by-Side Decision Cards

**Article scenario**: 304 vs 316, PVD vs Brushed, Laser vs Perforation — any binary choice

**HTML pattern**: Two wide cards side by side with a subtle center divider. Each card: grade/name as headline, 3 check/star items, big price/cost number at bottom, distinct background tint. Green checks for the "works here" items, accent stars for premium features. Bottom bar with the one-sentence takeaway.

**Example**: 304-vs-316 cards with green checks on left, cyan star-items on right, 100 vs 140 cost index at bottom, final sentence in gray bar.

### 27. Annotated Cross-Section / Diagram

**Article scenario**: Wall fixing detail, floor-mounted frame, ceiling track interface

**HTML pattern**: A central diagram (simplified SVG or CSS shapes) with labeled callout lines pointing to each component. Labels on both sides for balance. Use when the physical relationship between parts matters.

### 28. Timeline / Milestone Bar

**Article scenario**: Project phases, lead time breakdown, certification process

**HTML pattern**: Horizontal line with milestone dots. Each dot: date or day count, event name, one-line context. Alternating above/below the line for visual rhythm. Color-coded phases.

### 29. Checklist-as-Visual

**Article scenario**: Specification package, RFQ prep, what to send supplier

**HTML pattern**: A styled checklist where each item has a checkbox icon, bold item name, and one-line explanation. Distinct from a Markdown checklist — bigger, more visual, with icons and color. Think "packing list" aesthetic.

---

## Decision Flow

```
What kind of insight am I communicating?

├── A PROCESS or SEQUENCE?
│   └── Flow chart (#1), Timeline (#28), or Funnel (#3)
│
├── A COMPARISON between 2-3 things?
│   └── Bar chart (#5), Side-by-side cards (#26), or Radar (#7)
│
├── A SET OF SPECS or NUMBERS to show at a glance?
│   └── Spec card grid (#25), Checklist-as-visual (#29)
│
├── A PHYSICAL STRUCTURE or assembly?
│   └── Cross-section diagram (#27)
│
├── A PART-TO-WHOLE or percentage?
│   └── Donut (#13), Liquid gauge (#14)
│
├── A TREND over time?
│   └── Line chart (#20), Area chart (#21)
│
├── A DISTRIBUTION or spread?
│   └── Histogram (#10), Boxplot (#11)
│
└── A HIERARCHY or relationship?
    └── Org chart (#17), Mind map (#18), Network (#19)
```

---

## Usage in Enriched Draft

```markdown
**HTML / Chart Visual Candidate**
- Pattern: Side-by-side Decision Cards (#26)
- Concept: 304 vs 316 material comparison — when to use each
- Key visual elements: cost bar chart, performance comparison bars, environment-match icon cards
- Alt text: 304 vs 316 stainless steel comparison showing cost, corrosion resistance, and ideal applications
- Caption suggestion: 304 handles interiors. 316 handles everything else.
- Dimensions: 780px wide, flexible height
```
