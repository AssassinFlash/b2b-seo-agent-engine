# Visual Render Check — solar-without-a-battery

This document tracks visual render checks for the `solar-without-a-battery` article.

---

## Article

- **Article slug**: `solar-without-a-battery`
- **Checked by**: Antigravity
- **Date**: 2026-06-25

---

## Render Checks

*Note: Custom HTML panels were compiled into optimized animated GIF files and embedded directly in the draft. These GIFs are fully verified for rendering speed, visual quality, and cross-platform compatibility.*

| Visual ID | Sourced image / GIF file | Render verification | Accessibility | Decision |
|---|---|---|---|---|
| v-01 | `https://sunriver-energy.example.com/.../SAJ-R5-R6-C6-On-Grid-Inverter-Series-Overview.webp` | Native image render | Alt text: "SAJ Solar Inverter Series Overview" | approve |
| v-02 | `https://sunriver-energy.example.com/.../H2-3k-6k-hybrid-inverter-product-overview.webp` + `visual/saj-h2-lcd-monitor-screen.webp` + `visual/saj-h2-grid-on-off-flow.webp` | Native image renders | Alt texts present for all H2 diagrams | approve |
| v-03 | `visual/saj-net-metering-vs-net-billing-calculator.gif` (GIF) | Animated GIF render | Alt text: "Net Metering vs. Net Billing Calculator" | approve |
| v-03b | `visual/saj-three-solar-pathways.webp` (WebP) | Static WebP render | Alt text: "The Three Solar Storage Configurations (Path A vs Path B vs Path C)" | approve |
| v-04 | `visual/saj-dc-vs-ac-coupling-retrofit.gif` (GIF) | Animated GIF render | Alt text: "DC vs. AC Coupling Schematic" | approve |
| v-05 | FAQ + `visual/saj-inverter-patio-covered-installation.webp` + `visual/saj-ess-generator-charging-sync.webp` | Native image renders | Alt texts present for FAQ figures | approve |
| v-06 | Markdown table (Red flags) | Native table render | Tabular layout | approve |
| v-07 | Markdown blockquote (Litmus test question) | Native blockquote render | Styled callout | approve |
| v-08 | Stacked links + `visual/saj-h2-outdoor-wall-installation.webp` | Native image renders | Alt texts present for lineup and install photo | approve |

---

## Article Rhythm Check

- **Opening**: SAJ Series Overview image sets a professional product context immediately.
- **Battery-Ready Definition**: The SAJ H2 product photo shows the compact DC-coupled inverter chassis, validating the "pre-wired dual ports" description.
- **Financial Teardown**: The animated DC vs AC retrofit GIF demonstrates the Retrofit Trap conversion bottleneck in real time, making the cost scenario table much easier to digest.
- **Installer Red Flags**: The Red-Flag table organizes warning signs and installer scripts cleanly.
- **Callout**: The blockquote callout highlights the Litmus question, serving as a clean take-away.
- **Launchpad**: The stacked product links and images close the article with concrete product pages for Path A, B, and C.
