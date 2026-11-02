# antv Chart Tool Mapping for B2B Articles

Complete reference for using `@antv/mcp-server-chart` tools in article enrichment. These tools generate real charts and diagrams — not placeholders. Use them when diagram/chart-type visual opportunities arise.

## MCP Server Config

```json
{
  "mcpServers": {
    "mcp-server-chart": {
      "command": "npx",
      "args": ["-y", "@antv/mcp-server-chart"]
    }
  }
}
```

## Full Tool Inventory (26 tools)

### Flow & Process

| Tool | B2B Article Use Case | Example |
|---|---|---|
| `generate_flow_diagram` | Manufacturing process, QC workflow, spec review process | 5-gate QC: Design Review → Material Approval → Production Sample → QC Inspection → Pre-Shipment Photo |
| `generate_fishbone_diagram` | Root cause analysis | Why screens fail during installation |
| `generate_funnel_chart` | Stage-by-stage progression | Buyer journey: awareness → consideration → decision → purchase |
| `generate_sankey_chart` | Data flow and volume | Material flow from raw steel to finished panels |

### Comparison & Ranking

| Tool | B2B Article Use Case | Example |
|---|---|---|
| `generate_bar_chart` | Horizontal category comparison | Cost per sqm by manufacturing method |
| `generate_column_chart` | Vertical category comparison | Lead time comparison across suppliers |
| `generate_radar_chart` | Multi-dimensional data | 304 vs 316 across corrosion, cost, weldability, availability |
| `generate_scatter_chart` | Two-variable relationships | Open area % vs. privacy level |
| `generate_dual_axes_chart` | Two variables with different units | Cost (USD) vs. durability (years) |

### Distribution & Statistics

| Tool | B2B Article Use Case | Example |
|---|---|---|
| `generate_histogram_chart` | Data distribution by intervals | Panel thickness tolerance distribution |
| `generate_boxplot_chart` | Quartiles, outliers | Lead time variability across projects |
| `generate_violin_chart` | Distribution + density | Combining boxplot and density for tolerance data |

### Proportion & Composition

| Tool | B2B Article Use Case | Example |
|---|---|---|
| `generate_pie_chart` | Proportions as sectors | Competitor market share, keyword distribution |
| `generate_liquid_chart` | Proportions as water-filled spheres | Open area percentage, material purity |
| `generate_treemap_chart` | Hierarchical data as sized rectangles | Product categories by revenue or application |
| `generate_venn_chart` | Set relationships | Overlap between design, specification, and procurement requirements |

### Structure & Organization

| Tool | B2B Article Use Case | Example |
|---|---|---|
| `generate_organization_chart` | Structure and personnel | Project team hierarchy, supplier evaluation team |
| `generate_mind_map` | Hierarchical thought processes | Content pillar structure, keyword cluster map |
| `generate_network_graph` | Node relationships | Internal linking architecture, supplier network |

### Time & Trend

| Tool | B2B Article Use Case | Example |
|---|---|---|
| `generate_line_chart` | Trends over time | Material price trends, shipping cost trends |
| `generate_area_chart` | Trends over continuous variables | Cumulative project volume over years |

### Geographic (China-only via AMap)

| Tool | B2B Article Use Case | Example |
|---|---|---|
| `generate_district_map` | Administrative divisions + data | Factory locations in Guangdong |
| `generate_pin_map` | POI distribution | Project locations worldwide |
| `generate_path_map` | Route planning | Shipping routes from Foshan to destination ports |

### Text & Tabular

| Tool | B2B Article Use Case | Example |
|---|---|---|
| `generate_word_cloud_chart` | Word frequency | Keyword research visualization |
| `generate_spreadsheet` | Pivot table | Material specification comparison table |

## Decision Flow: Photo or Chart?

```
Is the visual about a REAL thing that exists?
  ├── YES → Use a real photo/media route if available
  └── NO → Is it a PROCESS, COMPARISON, or CONCEPT?
            ├── YES → Use antv chart or article-html-visuals, whichever explains better
            └── NO → Is it a trust/proof need?
                      ├── YES → Use real proof/detail or skip
                      └── NO → Skip unless an HTML expression block adds reader value
```

## Usage in Enriched Draft

```markdown
**HTML / Chart Visual Candidate — antv MCP**
- Tool: `generate_flow_diagram`
- Data/Input: 5-step process: Design Review → Material Approval → Production Sample → QC Inspection → Pre-Shipment Photo
- Alt text: Five-gate quality control process diagram for custom metal screen manufacturing
- Caption suggestion: Every panel passes through five gates before shipping.
- Dimensions: 1000 × 650 (diagram type)
```
