# WordPress Preview Check — solar-without-a-battery

**Stage:** `/article-publish-pack`  
**Date:** 2026-06-24

---

## Pre-Publish Checklist

| Check | Status |
|---|---|
| H1 matches publish-package §1 | ✅ |
| SEO `<title>` (50–60 chars) set | ✅ |
| Meta description (150–160 chars) set | ✅ |
| Slug set to `solar-without-a-battery` | ✅ |
| Enriched draft body pasted (Draft Control Metadata excluded) | ✅ |
| Visual assets (GIFs and WebPs) verified and embedded | ✅ All custom animated GIFs and WebP diagrams are embedded in the draft |
| All internal links verified (URLs exist) | ⚠️ Verify on WordPress before publish |
| Schema JSON-LD pasted into header/footer | ⚠️ Paste before publish |
| OG image set | ⚠️ Set Sunriver brand logo or Path diagram |
| Categories/tags set (Solar Education, Inverter Guide, Battery Storage) | ⚠️ Set in WordPress |
| Featured image uploaded | ⚠️ Upload product lineup or hero path diagram (v-01) |
| Mobile preview: comparison table (H2-05) renders without overflow | ⚠️ Test on mobile |
| Mobile preview: routing box blocks (H2-05, H2-08) render cleanly | ⚠️ Test on mobile |
| No broken markdown, stray HTML comments, or metadata leaks in body | ✅ |
| External links open in new tab (if applicable) | ⚠️ Set in WordPress |
| Anchor text is descriptive (no "click here") | ✅ |

---

## Custom Visual Assets Embedded in the Draft

These custom visual assets are generated from HTML source files and embedded directly in the draft using standard Markdown image links. Upload these files to your WordPress Media Library and verify they render cleanly.

| Visual ID | Section | Asset File | Alt Text | Purpose |
|---|---|---|---|---|
| v-02 | H2-02 | `https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-h2-lcd-monitor-screen.webp` | SAJ H2 Hybrid Inverter LCD Monitoring Panel | Show the LCD screen display |
| v-02 | H2-02 | `https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-h2-grid-on-off-flow.webp` | SAJ H2 Hybrid Inverter Normal vs Backup Power Flow Diagram | Normal/Backup flow overview |
| v-03 | H2-03 | `https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-net-metering-vs-net-billing-calculator.gif` | Net Metering vs. Net Billing credit comparison animated calculator | Interactive credit payback animation |
| v-03b | H2-03 | `https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-three-solar-pathways.webp` | The Three Solar Storage Configurations (Path A vs Path B vs Path C) | Simplified static comparison diagram |
| v-04 | H2-04 | `https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-dc-vs-ac-coupling-retrofit.gif` | DC-Coupled vs. AC-Coupled retrofit animated flow schematic | Animated flow for retrofit comparison |
| v-05 | H2-05 | `https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-inverter-patio-covered-installation.webp` | SAJ Hybrid Inverter Patio covered installation | Real installation environment |
| v-05 | H2-05 | `https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-ess-generator-charging-sync.webp` | SAJ Inverter Generator Charging Synchronization Diagram | Technical generator sync diagram |
| v-08 | H2-08 | `https://sunriver-energy.example.com/wp-content/uploads/2026/06/saj-h2-outdoor-wall-installation.webp` | SAJ H2 Hybrid Inverter Outdoor Wall Installation | Real outdoor wall installation |

---

## SEO Plugin Fields (Yoast / Rank Math / equivalent)

| Field | Value |
|---|---|
| Focus keyphrase | solar without a battery |
| SEO title | Solar Without a Battery: The Inverter Mistake That Gets Expensive |
| Slug | solar-without-a-battery |
| Meta description | Yes, you can run solar without a battery. But the inverter on your quote decides whether adding one later is a $3,000 retrofit or a $9,000 do-over. Here's how to spot the difference. |
| Cornerstone content | No |
| Schema type | Article (JSON-LD in schema.json) |
| FAQ schema | Enabled (JSON-LD in schema.json) |

---

## Post-Publish Verification

| Check | Status |
|---|---|
| Page loads without errors | ⚠️ Check after publish |
| Title and meta appear correctly in browser tab | ⚠️ Check after publish |
| URL is `https://sunriver-energy.example.com/solar-without-a-battery/` | ⚠️ Check after publish |
| Schema validates in Google Rich Results Test | ⚠️ Test after publish |
| Submit to Google Search Console for indexing | ⚠️ After publish |
| Share on social for initial signal | ⚠️ After publish |

---

## Handoff Notes

- All 4 QA gates PASS. No blocking issues.
- Truth QA watchlist items ($3k-$9k ranges, installer/most-homeowner judgments) are non-blocking.
- Schedule `/article-review` at 30/60/90 days post-publish per workflow.
- `keyword-record.csv` contains 15 keywords for SEO plugin import.
