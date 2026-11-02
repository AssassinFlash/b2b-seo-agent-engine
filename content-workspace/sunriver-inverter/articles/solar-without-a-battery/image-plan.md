# Image Plan — solar-without-a-battery

**Stage:** `/article-enrich`  
**Date:** 2026-06-25  
**Article:** solar-without-a-battery  
**Asset status:** Custom animated GIFs and static WebP diagrams generated from HTML visuals and integrated into the draft

---

## Asset Reality Report

| Asset type | Available | Notes |
|---|---|---|
| Real project photos | 3 | Added local installer photos (saj-h2-outdoor-wall-installation.webp, saj-inverter-patio-covered-installation.webp) and LCD screen close-up (saj-h2-lcd-monitor-screen.webp) |
| Factory/process photos | 0 | No factory/QC photo inventory |
| Product photos | 165 | Sourced via Apify across Sunriver site, Alibaba, Made-in-China, Amazon, YouTube, and TikTok |
| Finish/detail photos | 0 | Not applicable for inverter/hardware article |
| Diagrams/Flowcharts | 1 | 1 static WebP comparison diagram (`saj-three-solar-pathways.webp`) captured from clean HTML |
| Animated GIFs | 2 | Custom animations (`saj-net-metering-vs-net-billing-calculator.gif`, `saj-dc-vs-ac-coupling-retrofit.gif`) compiled from Playwright recordings of interactive HTML visuals |

**Decision:** We are using **2 custom animated GIFs**, **1 static WebP diagram**, and **3 local WebP product/installer photos** alongside standard web product images and native Markdown structures.

---

## Visual Material Library (For Operator Review)

All multi-channel image candidates, B2B listings, and YouTube installation videos with precise frame timestamps are cataloged in the interactive material library:
* **Interactive Viewer**: [visual-material-library.html](./visual-material-library.html)
* **Metadata Catalog**: [visual-asset-candidates.md](./visual-asset-candidates.md)

---

## Visual Opportunity Map

| ID | Section | Reader job | Route | Description | Fallback | Status |
|---|---|---|---|---|---|---|
| v-01 | H2-01 | Opening orientation | real-image | SAJ R5/R6/C6 Series Overview image. Link: https://sunriver-energy.example.com/wp-content/uploads/2025/09/SAJ-R5-R6-C6-On-Grid-Inverter-Series-Overview.webp | Text-only Key Takeaways block | Sourced image embedded |
| v-02 | H2-02 | Definition anchor | real-image | SAJ H2 hybrid inverter product overview + local LCD monitoring panel (saj-h2-lcd-monitor-screen.webp) and Grid On/Off flow diagram (saj-h2-grid-on-off-flow.webp) | Prose-only definition | Local + Sourced images embedded |
| v-03 | H2-03 | Decision routing | animated-gif | Net Metering vs. Net Billing credit comparison animated calculator (https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-net-metering-vs-net-billing-calculator.gif) | Prose-only decision criteria | Animated GIF embedded |
| v-03b | H2-03 | Pathway comparison | static-webp | Side-by-side hardware comparison of Path A, B, and C (https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-three-solar-pathways.webp) | Prose comparison | Static WebP embedded |
| v-04 | H2-04 | Cost comparison | animated-gif | Scenario table + DC-Coupled vs. AC-Coupled retrofit animated flow schematic (https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-dc-vs-ac-coupling-retrofit.gif) | Prose-only cost scenarios | Markdown table + Animated GIF embedded |
| v-05 | H2-05 | Comparison framework | FAQ / real-image | Quick answers block with residential patio install photo (saj-inverter-patio-covered-installation.webp) and generator synchronization infographic (saj-ess-generator-charging-sync.webp) | Existing FAQ prose | Local images and FAQ Q&As embedded |
| v-06 | H2-06 | Risk screening | markdown-table | Red-flag checklist table with "What the quote says" / "What it means" / "What to ask" columns | Prose-only numbered checklist | Markdown table embedded |
| v-07 | H2-07 | Action anchor | markdown-blockquote | Blockquote warning card with single installer question | Blockquote | Markdown blockquote embedded |
| v-08 | H2-08 | Product-routing close | real-image | Stacked product path cards (R6, H2, HS3) + real outdoor wall mount photo for Path B (saj-h2-outdoor-wall-installation.webp) | Prose-only CTA links | Sourced + Local images embedded |

---

## Visual Mix Control

| Route | Count | % |
|---|---|---|
| Real product photos | 3 | 33.3% |
| Markdown tables & blockquotes | 3 | 33.3% |
| Animated GIFs | 2 | 22.2% |
| Custom WebP Diagrams | 1 | 11.1% |

**Rationale:** This B2B buyer's guide uses web-sourced product images, native Markdown tables, 2 custom animated GIFs, and 1 static WebP diagram (compiled from clean HTML) to provide a rich, visually intuitive experience with small page load footprints.

---

## Internal Link Blocks

| Placement | Type | Links |
|---|---|---|
| H2-01 end | Resource block | [Can a hybrid inverter work without a battery?](/can-hybrid-inverter-work-without-battery/) |
| H2-02 end | Resource block | [Modern hybrid solar systems explained](/modern-hybrid-solar-systems/) |
| H2-04 end | Resource block | [5 solar battery specs to avoid — Solar Rush mistake](/5-solar-battery-specs-to-avoid-solar-rush-mistake/) |
| H2-05 end | Accordion block | Path-specific product routing: R6, H2, HS3 product pages + all-in-one comparison |
| H2-06 end | Resource block | [5 solar battery specs to avoid — Solar Rush mistake](/5-solar-battery-specs-to-avoid-solar-rush-mistake/) |
| H2-08 end | Accordion block | Path-specific product routing + contact page |

**Density check:** 4 resource blocks, 2 accordion blocks, 0 inline "click here" links — within the 5-8 inline / 2-3 resource / 1-2 accordion target range.

---

## Publish-Pack Handoff Notes

- HTML visual source codes are stored under `html-visuals/` for future edits and reference.
- The enriched draft embeds the optimized animated GIFs (`saj-net-metering-vs-net-billing-calculator.gif`, `saj-dc-vs-ac-coupling-retrofit.gif`) and 1 static WebP diagram (`saj-three-solar-pathways.webp`) in standard Markdown syntax.
- No custom iframe or active scripts are needed inside the published WordPress content, ensuring perfect SEO indexability and mobile rendering speed.
- All target URLs for internal links are verified and active on the website.
