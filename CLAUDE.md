# B2B SEO Agent System Operating Guide (v3.0)

This project implements a deep B2B SEO agent system built on a universal startup protocol, specialized project profiles, benchmark-led writing from best-in-class content sites, unified voice/humanization execution, structure variation, and 4-gate QA. Updated 2026-06-17.

> **v3.0 change**: All workflow entrypoints are now user-invocable skills located in `.claude/skills/*/SKILL.md`. There is no `.claude/commands/` directory. Agents are invoked only by skills, never directly by the operator.

---

## 1. Primary Flow

```text
vague business input
-> discovery research / question loop
-> topic cluster (50+ Deep SEO Cards; pick first article) [⏸]
-> locked project-profile [⏸]
-> intent research (verifiable live search-intent/H2 candidate pool) [⏸]
-> benchmark candidates (best-in-class content, NOT competitor SERP) [⏸]
-> benchmark structural blueprint + reader advancement mechanism extraction (21 Success Formula dimensions, no final outline) [⏸]
-> evidence gathering + opinion processing (unified voice-and-humanization policy) [⏸]
-> differentiated skeleton (structure variation per section; section contracts embedded) [⏸]
-> narrative arc (benchmark-native reader journey) [⏸]
-> one-shot draft (continuous pass, voice + structure execution) [⏸]
-> truth QA → information gain QA → benchmark drift QA → reader QA [⏸]
-> repair loop (if blocked) → re-run gates [⏸]
-> enrich (visual markers + HTML expression) [⏸]
-> visual (executable visual spec for multimodal AI) [⏸]
-> resources (curiosity cards + routing + link coverage) [⏸]
-> faq (friction map + conclusion-first answers + objection-to-CTA) [⏸]
-> WordPress publish pack
-> performance review (30/60/90 days)
```

All article stages pause for **Peer Co-Research & Calibration (对等共研与校准)**. Do not auto-advance, and never merge stages to skip pauses.

### 1.1 Peer Co-Research Protocol at Every Pause (`⏸`)
Every stage stops so the operator and the AI can examine the output together, absorb the findings, and conduct divergent supplementary research:
- **Neither Human > AI nor AI > Human**: Only verified evidence, logic, and real buyer search intent win.
- If the AI missed an angle or drifted from business reality, the operator challenges it or supplies new material from their own search.
- If the operator brings back a link, hypothesis, or direction that is one-sided, unsupported, or misaligned with real search intent, the AI **must push back with evidence and logic** rather than blindly obeying and stuffing it into the artifact.
- Advance only after both sides have debated any disagreements and reached consensus.

### 1.2 Mandatory Apify-First Search & Research Rule (铁律)
Whenever any step requires search, external fact verification, competitor research, industry rule confirmation, or material gathering, **Apify MUST be used first** (`python3 scripts/apify_research.py` or `mcp__apify__*`, backed by the 3 rotating monthly tokens in `.env.apify.local` / `~/.config/b2b-seo-agent/apify.env`).
- **Apify broken → fix it until it works**: Never bypass Apify or downgrade research depth without diagnosing token slots, Actor choice, input schema, dataset parsing, `--browser` mode, or timeouts first. Do not worry about Actor call cost (monthly tokens expire anyway).
- **Combinatorial escalation**: Combine Apify Actors, Scrapling, Scrapy, Crawl4AI, Firecrawl, Playwright real Chrome, and Computer Use. Never conclude "not found" because a single crawler or page failed; pivot across `不同关键词 → 不同页面 → 不同数据源 → 不同 Actor → 不同抓取方式 → 不同技术路径`.

Drafting uses **Imitate → Inject → Differentiate** as a numeric steering model. `/article-draft` must choose exact working percentages for the current article before writing, and the three values must total 100. Stronger benchmark fit means heavier imitation; stronger proprietary evidence or buyer risk means heavier injection/differentiation.

For subjective writing controls, use a **Numeric Control Vector**: choose concrete target numbers, explain the choice, then execute against them. These numbers are execution parameters, not quality scores. Do not leave core controls as vague freedom, and do not turn numbers into paragraph-by-paragraph quotas.

---

## 2. System Rules & Constraints (TRACE Model)

To maintain consistency across diverse AI clients (including Claude Code, Gemini, Codex, Kimi, etc.), all developers and AI models must strictly adhere to these guidelines. Both [CLAUDE.md](./CLAUDE.md) and [AGENTS.md](./AGENTS.md) serve as the dual-constitution of this repository.

### 2.1 TRACE Quality Framework
- **T - Trust (信任)**: No hidden side effects. Every claim must trace to a verified source.
- **R - Reliability (可靠性)**: Stable execution. Clear error boundaries. Always check upstream prerequisites.
- **A - Adaptability (适用性)**: Specific description trigger phrases to avoid over/under-triggering.
- **C - Convention (规范性)**: Consistent directory structures, naming conventions, and frontmatter.
- **E - Effectiveness (有效性)**: Directly usable outputs that satisfy the artifact graph.

### 2.2 Skill Directory Structure Rules
Each skill must occupy a dedicated directory under `.claude/skills/`:
- **Folder Name**: Must be kebab-case (e.g. `voice-and-humanization`).
- **Main Instruction File**: Must be named exactly **`SKILL.md`** (all caps, case-sensitive).
- **Sub-folders**: Only the following folders are permitted (all optional):
  - `references/`: Documentation and guide materials (e.g. `references/patterns.md`).
  - `scripts/`: Executable automation code (Python, Bash, etc.).
  - `assets/`: Icons, fonts, or localized assets.
- **Strict Prohibitions**:
  - **No `README.md`** is allowed inside any skill directory (all documentation belongs in `SKILL.md` or `references/`).
  - **No `templates/`** folders are allowed inside skill directories. All templates must reside in the root `templates/` directory.

### 2.3 YAML Frontmatter Security & Formats
Every `SKILL.md` must declare a clean YAML frontmatter:
- **Required Fields**:
  - `name`: Matches the kebab-case directory name exactly.
  - `description`: Starts with `Use when:` or `Use after:`. Explains what the skill does and specific trigger phrases. Must be under 1024 characters.
  - `user-invocable`: Boolean (`true` or `false`).
  - `allowed-tools`: List of tools accessed (only required if `user-invocable: true`).
- **Forbidden Delimiters**:
  - **No XML brackets `< >`** are allowed anywhere in the frontmatter (injection security prevention).
  - Do not use reserved names starting with `claude` or `anthropic`.

### 2.4 Single Source of Truth
- **Workflow Spec**: Configured solely in `config/workflow-spec.yaml`.
- **Artifact Graph**: Defined solely in `config/artifact-graph.yaml`.
- **State Schema**: Defined solely in `config/state-schema.json`.
- **Clean Archive Policy**: Retired skills or commands must be physically removed from active folders. No retired directories (such as `artifact-graph` or `profile-foundation`) may remain in `.claude/skills/`.

---

## 3. Article Production Skills

| Stage | Skill | Creates | Pause |
|---|---|---|---|
| Discover | `/profile-discover` | `project-profile.draft.md` | ⏸ answer discovery questions |
| Answer | `/profile-answer` | updated `project-profile.draft.md` | ⏸ if more questions needed |
| Cluster | `/article-cluster` | `topic-cluster.md` (50+ Deep SEO Cards + scoring), `topic-card.md` | ⏸ review topic pool and pick first article |
| Research | `/profile-research-deep` | `project-profile.research.md` | ⏸ if research gaps remain |
| Lock | `/profile-lock` | `project-profile.md`, `project-profile.json` | ⏸ approve locked profile |
| Intent Research | `/article-intent-research` | `intent-research.md` | ⏸ approve research plan |
| Benchmark Library | `/article-benchmark` | `content-type-library.md`, `benchmark-candidates.md` | ⏸ user selects 3 |
| Extract | `/article-benchmark-extract` | `benchmark-success-formula.md`, `benchmark-asset-ledger.md` | ⏸ iterative |
| Evidence+Opinions | `/article-evidence-opinions` | `evidence-opinion-pack.md`, optional `upstream-revision-suggestions.md`, optional `evidence-handoff-summary.md` | ⏸ iterative; pause if upstream corrections required |
| Skeleton | `/article-skeleton` | `skeleton.md` + secondary heading library | ⏸ review |
| Arc | `/article-arc` | `narrative-arc.md` | ⏸ review |
| Draft | `/article-draft` | `draft.md` | ⏸ review |
| Truth QA | `/article-truth-qa` | `truth-qa.md` | ⏸ if blocked |
| Info Gain QA | `/article-information-gain-qa` | `information-gain-qa.md` | ⏸ if blocked |
| Benchmark QA | `/article-benchmark-qa` | `benchmark-drift-audit.md` | ⏸ if blocked |
| Reader QA | `/article-reader-qa` | `reader-qa.md` | ⏸ if blocked |
| Repair | `/article-repair` | `repair-plan.md`, updated `draft.md` | ⏸ after rewrite plan |
| Enrich | `/article-enrich` | `enriched-draft.md`, `image-plan.md` | ⏸ final review |
| Visual | `/article-visual` | `visual-spec.md`, `visual/` | ⏸ review specs |
| Resources | `/article-resources` | `resources.md` | ⏸ review cards |
| FAQ | `/article-faq` | `faq.md` | ⏸ review friction map |
| Publish | `/article-publish-pack` | `publish-package.md`, `schema.json`, `keyword-record.csv` | — |
| Review | `/article-review` | `performance-review.md` | ⏸ 30/60/90 days post-publish |

**Optional artifacts** (produced when article complexity warrants):
- `articles/<article-slug>/benchmarks/<source>-raw-observations.md` — per-benchmark raw forensic observations
- `articles/<article-slug>/evidence-handoff-summary.md` — structured handoff brief from `/article-evidence-opinions` to skeleton/draft stages
- `articles/<article-slug>/intent-research.md` — verifiable search-intent/H2 candidate pool produced by `/article-intent-research`
- `articles/<article-slug>/content-type-library.md` — broad content-type library produced by `/article-benchmark`
- `articles/<article-slug>/h2-heading-strategy.md` — 7:3 SEO/CTR heading plan produced by `/article-skeleton`
- `articles/<article-slug>/knowledge-gap-register.md` — pre-writing risk inventory for spec-heavy articles
- `articles/<article-slug>/upstream-revision-suggestions.md` — corrections forced back onto upstream artifacts when evidence validation finds errors

### 3.1 H2 Design & Verifiable Research

H2 headings produced by `/article-skeleton` follow the **7:3 rule by default**: 70% clean SEO question (standard entities, PAA/AIO-friendly) + 30% micro-tension hook (Actually, Really, Mistake, Costly, Number One, Lock You Out).

Section function borrowed from benchmarks must be translated into search-facing questions. Do not use internal section labels like "Key Takeaways" or "Path A vs. Path B" as H2s unless they are also real search queries.

**Verifiable research requirement:** Live multi-channel research (Google PAA, Google Autocomplete, Reddit/forums, Chinese social, non-text sources) belongs to `/article-intent-research` and is recorded in `intent-research.md`. `/article-skeleton` consumes the pre-built pool and does not perform live extraction. Every candidate must record source URL, extraction method, and timestamp. Inferred or "style" candidates are not acceptable substitutes for live extraction.

### 3.3 Seven Deep-Search & B2B Persuasion Pillars (v3.4 Upgrade)

1. **Buying Committee Multi-Persona & Internal Champion Enablement (Gartner 买方委员会穿透)**: Every article serves both the primary technical searcher (Engineer/Architect/Installer) and equips them with a forwardable 30-second TCO/risk decision ledger to convince the commercial/budget approver (Procurement/CFO/Owner).
2. **Self-Contained RAG Citation Chunks (GEO / Perplexity / SearchGPT / Google AIO 独立语义块)**: Key question H2s open with a 40–60 word self-contained passage carrying the explicit subject entity, operating condition, direct verdict, and quantified metric — zero dangling pronouns referring back to the H2.
3. **SERP Consensus Target vs. Contrarian Counter-Move (Google Information Gain Patent `US20200349181A1`)**: `/article-intent-research` extracts the 3–5 platitudes repeated across current SERP Top 5 pages so `/article-evidence-opinions` and `/article-draft` can directly dismantle or qualify them.
4. **Above-the-Fold Viewport Contract (Navboost 防跳出零滚动区)**: `/article-skeleton` and `/article-enrich` design the first ~180 words + first interactive/visual micro-anchor to lock in the searcher within 3 seconds (no giant decorative stock hero banners pushing answers below the fold).
5. **Hub & Spoke Topical Topology + Cannibalization Guard**: `/article-cluster` merges candidate keywords with >60% SERP URL overlap into one card and maps explicit Pillar Hub vs. Supporting Spoke roles.
6. **Named E-E-A-T Technical Author & Reviewer Personas**: `project-profile.md` defines named engineers/experts with field credentials, carried through workshop callouts and `schema.json` `author` / `reviewedBy` JSON-LD.
7. **Forensic Specificity & Anti-Sell Disqualification Proof**: `/article-evidence-opinions` and `/article-visual` pair caliper/instrument-level forensic proof with honest disqualification boundaries (telling buyers when NOT to buy the high-spec option).

### 3.2 Anti-Presupposition Rule

During planning stages — before `lockedProfile` is true and before `/article-skeleton` begins — agents must describe *how* an answer will be found, not what the answer is expected to be.

Planning outputs must NOT include:
- Expected specific answers or conclusions
- Unverified examples presented as facts
- Specific numbers, prices, or specs not sourced from the locked profile or verified research
- Prejudged benchmark selections or H2 sequences

This rule works alongside the Locked Profile Gate: the profile prevents inventing project context; the Anti-Presupposition Rule prevents agents from baking expected outcomes into the methodology itself.

---

## 4. Development & Testing Commands

To verify your work before completion:
- **Verify Workflow Config**: `python3 scripts/validate_discovery_profile_workflow.py`
- **Run Unit Tests**: `python3 -m pytest tests/` (or `python3 -m unittest discover -s tests`)
- **Run Deep Structural Audit**: `python3 scripts/deep_audit.py` (Must output *Total issues found: 0*)

## 5. Subagent-First Context Policy

For any task that requires processing a large amount of source text, parallel analysis, or multi-step synthesis, **default to subagents** rather than loading everything into the main context window.

**Trigger conditions — proactively ask the operator if subagents are preferred when you notice:**
- Reading or analyzing more than one full-length article in the same stage (e.g., `/article-benchmark-extract`, `/article-evidence-opinions`, QA gates).
- Combining more than two independent research sources into a single synthesis.
- Running multi-file audits, cross-reference checks, or batch validations.
- The main context is approaching compaction, or the skill naturally maps to parallel work units.

**Execution rule:**
- Use one subagent per bounded unit of work (one article, one source, one file, one check type).
- Subagents read source material, perform analysis, and **write results to durable artifacts** under the article workspace.
- The main context reads only the subagent outputs / summaries and performs final synthesis.
- Do not bring full raw source text back from subagents into the main context unless the operator explicitly asks for it.

This policy protects context budget, improves reproducibility, and keeps the main context focused on decisions rather than ingestion.
