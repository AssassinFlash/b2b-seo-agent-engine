---
name: article-arc
description: "Use when: the section contracts are ready and you need to design the 6-node narrative arc that locks the reader's cognitive journey before drafting."
argument-hint: '[content-workspace/project-slug] [article-slug]'
user-invocable: true

allowed-tools:
  - Bash
  - Read
  - Edit
  - Write
  - WebSearch
  - WebFetch
  - Agent
  - mcp__you__*
  - mcp__tavily__*
  - mcp__exa__*
  - mcp__crawl4ai__*
  - mcp__firecrawl__*
  - mcp__plugin_playwright_playwright__*
  - mcp__apify__*
  - mcp__agent-reach__*
  - mcp__douyin__*
  - mcp__linkedin__*
  - mcp__mcp-server-chart__*
---

# /article-arc

## Agent Routing

This skill executes in the main context with explicit skill loading. **[Imitate → Inject]** — operates on layers 1 and 2 of the Imitate → Inject → Differentiate stack.

Skills loaded during this stage: `structure-variation` (rhythm audit checklist).

## Argument Contract

Use `$ARGUMENTS` as `content-workspace/<project-slug> <article-slug>`.

Before designing the arc, verify:
- `project-profile.md` exists, `project-profile.json` exists, `state.json` indicates `lockedProfile: true`. If the locked profile is missing, stop and route to `/profile-discover`, `/profile-answer`, `/profile-research-deep`, or `/profile-lock`.
- `skeleton.md` exists with user-approved section structure
- `evidence-opinion-pack.md` exists
- `benchmark-success-formula.md` exists

### Handoff Read (MANDATORY — complete before Phase 0 Plan Preview)

| Upstream File | Extract | Used For |
|---|---|---|
| `skeleton.md` | Per-section arc-node-role field (which reader-journey role each H2 primarily serves) | Validating that the skeleton has a coherent benchmark-native arc assignment before designing the narrative. If roles are missing or unbalanced, flag before proceeding |
| `skeleton.md` | Full H2 sequence with section functions and voice lens assignments | The arc must follow the skeleton's cognitive sequence — not redesign it |
| `benchmark-success-formula.md` Dimensions 2, 3, 4, 14 | Reader state, opening tension, angle, human texture per benchmark | Imitating how benchmarks handle narrative transitions between nodes |
| `evidence-opinion-pack.md` Part 3 | Per-scene voice lens and intensity | Ensuring the arc's emotional progression matches the voice intensity assigned per scene |
| `project-profile.md` §3 | Target buyers | The arc's trust shift must land for the primary buyer persona |

## Purpose

A 3,000-word article without a pre-designed arc becomes "module stacking". The arc locks the reader's cognitive journey before a single paragraph is written.

## Instructions

### Skeleton-Arc Consistency Check (before Phase 0)

Before designing the arc, re-read `skeleton.md`. Verify:

- Each section has an **arc node role** assigned (Reframe / First Turn / Middle Build / Trust Shift / Arrival, or another benchmark-native role if the selected benchmark uses a different arc)
- The Trust Shift section is positioned where the benchmark rhythm and reader journey make it feel earned, not mechanically forced
- The Opening Reframe appears early enough to justify continued reading, unless the benchmark intentionally delays the reframe
- At least one Middle Build section format differs from its neighbors (rhythm preserved)
- If inconsistencies found: flag them. Do NOT proceed to arc design until resolved or explicitly overridden.

---

### Phase 0 — Plan Preview (output first, do NOT execute)

Before designing the arc, present a plan:

1. **Upstream Consumption Report** (MANDATORY first item): confirm exactly what was read from upstream:
   - From skeleton.md: arc-node-role per section = [list]. Verify the roles support the benchmark-native reader journey; do not force all 6 nodes to appear visibly if the article type does not need them.
   - From skeleton.md: the Skeleton-Arc Consistency Check result from Phase 4. Any flags?
   - From benchmark-success-formula Dim 2,3,4,14: arc patterns from benchmarks = [summary]. "Backlinko's trust shift lands in Chapter 1, HubSpot D's reframe is paragraph 1."
2. **Arc Sketch**: one sentence per active node — what happens to the reader at each meaningful turn
3. **Key Transitions**: the transitions most likely to decide whether the reader keeps going
4. **Arc-to-Skeleton Map (preliminary)**: which skeleton sections serve which arc nodes

Output the plan. ```
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，按计划推进
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
```

Wait for explicit approval.

---

---

### Benchmark Arc Reference (do before The 6 Nodes)

Before designing our narrative arc, read Dimensions 2 (Reader State), 3 (Opening Tension), 4 (Angle), and 14 (Human Texture) from `benchmark-success-formula.md`. These capture how each of the selected benchmark articles built their narrative arcs:

- Where did Backlinko's trust shift land? (Answer: Chapter 1 defines authority, Chapters 2-5 prove depth, Bonus chapter seals it)
- How did EnergySage handle the reframe moment? (Answer: first paragraph — "Your roof doesn't work? Here are alternatives.")
- What rhythm did HubSpot C use to keep 8000 words readable? (Answer: heavy classification → heavy examples → light decision guide → medium industry → light FAQ)
- How did HubSpot D make company structure feel personal? (Answer: "If I had a cupcake business..." — real person, real judgment)

This is about copying useful proportions and pacing, not forcing every article into the same visible story template. If the benchmark wins through a fast trust shift, delayed reframe, comparison-first opening, or case-proof-first arc, preserve that logic.

---

### The 6 Nodes

Use these as diagnostic nodes, not mandatory chapter beats. Merge, compress, reorder, or make a node implicit when the benchmark structure and article type call for it.

### Node 1 — Starting State (Buying Committee Arrival)

Define the reader's state when they arrive (both the primary Technical Specifier who typed the query and the Commercial/Budget Approver they must ultimately convince).

- What do they think they need? (Often narrower or simpler than what they actually need.)
- What **SERP Consensus misconception** might they be carrying from reading competitor pages?
- What decision are they trying to make, and what internal objection from Procurement/CFO will block them if left unaddressed?

Example: "The reader thinks they need a decorative metal screen. They're browsing by pattern and color. They don't yet understand that environment, material grade, open area, and fixing method matter more than appearance for project success — or how to justify the 316L cost delta to their project owner."

### Node 2 — Opening Reframe & Above-the-Fold Lock-In (Navboost Anti-Pogo)

How does the opening (first 150–180 words + Above-the-Fold micro-anchor) deliver the direct answer, reframe their understanding, and route them so they never bounce back to Google SERP?

The reframe should make the reader think: "I was asking the wrong question — and this page has the exact engineering math I need."

Example: "A metal room divider is not a decorative accessory. In real projects, it behaves like an architectural component that affects privacy, light, airflow, circulation, durability, cleaning, installation, and long-term maintenance."

### Node 3 — First Turn

Where does the first major shift happen? (Usually in the first 20-25% of the article.)

The first turn moves the reader from "this is about aesthetics" to "I need to make a specification decision based on conditions, not preferences."

This is where a Decision Framework typically enters.

### Node 4 — Middle Build

How does the middle section progressively upgrade the reader's judgment?

The middle must NOT be a flat list of equivalent sections. Each section should build on the judgment established in the previous one. The reader's ability to make their own decisions should increase as they move through.

Map the dependency chain: "The reader first learns to judge environment → then material → then manufacturing method → then pattern/open area → then finish → then installation requirements → then cost drivers."

### Node 5 — Trust Shift

Where does the reader transition from "I understand this product" to "I trust this supplier to manage project risk"?

This shift often happens in the latter third, but benchmark rhythm has priority. It is not a "why choose us" section. It's: "Here are the ways this goes wrong, and here is how a well-controlled manufacturing process prevents each one."

The reader should feel: the same expertise that explained the complexity also controls it.

### Node 6 — Arrival State

Define the reader's state after finishing.

- What do they now understand that they didn't at Node 1?
- What judgment can they now make independently?
- What information do they know they need to provide to get an accurate quote?
- What's the natural next action? (This determines the CTA.)

Example: "The reader now knows that custom metal room dividers are not ordered by photo and color alone. They are specified by environment, material grade, manufacturing method, pattern density, finish, fixing method, and supplier QC process. They know what information affects pricing and what to send a supplier for an accurate project recommendation."

---

### Arc-to-Skeleton Mapping

For each skeleton section, state which arc node(s) it serves and how:

| Skeleton Section | Arc Node(s) | Role in the Arc |
|---|---|---|
| H2-01 | Node 2 (Reframe) + Node 3 (First Turn) | Establish what a custom divider actually is; introduce the first decision framework |
| H2-02 | Node 4 (Middle Build) | Apply the framework to a specific context; deepen judgment |
| ... | ... | ... |
| H2-0N | Node 5 (Trust Shift) | Transition to trust through process transparency |
| CTA | Node 6 (Arrival) | Natural landing based on what the reader now knows |

---

## Output

Create:
- `articles/<article-slug>/narrative-arc.md` — active arc nodes + arc-to-skeleton mapping

Update `state.json`:
```json
{
  "currentStage": "article-arc",
  "nextCommand": "/article-draft",
  "lockedProfile": true
}
```

---

## Examples

### Example 1: Mapping skeleton to 6-node arc
输入: `/article-arc content-workspace/steel-screen screen-article`
输出: `narrative-arc.md created containing 6-node mapping aligned with the 12 sections in skeleton.md.`

## Guardrails

- **Consistency Check**: Verify that every heading in skeleton.md has a clear reader-journey role.
- **Tone Balance**: Ensure the Trust Shift feels earned in the benchmark-native rhythm, not introduced by formula.
- **Intent Protection**: Reject arcs that cater to DIY installers; all paths must lead commercial buyers to factory specification checkpoints.

## PAUSE

```
=== ⏸ 停止 · 对等共研与校准（严禁跳步）===
请与我一起审阅并推敲本阶段的产出（人类与 AI 对等共研，唯证据、买家意图与逻辑胜出）：
  · 批准 / 继续 — 共识达成，按计划推进
  · 补充 / 探讨：[粘贴你扩散搜索到的新素材、新角度或质疑，我们交叉验证]
  · 修改：[你的修改要求]
  · 停止 — 终止
==========================================
```

Present the arc and ask:
- Does the reader's mental path from Node 1 to Node 6 feel natural?
- Is the First Turn strong enough to justify the reader continuing?
- Does the Trust Shift feel earned or forced?
- Does the Arrival State naturally lead to the CTA, or is the CTA a hard break?
