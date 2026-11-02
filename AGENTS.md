# B2B SEO Agent Guide & Code Constitution (v3.0)

This project is built around one root rule: no article agent may invent project context. All article work must depend on a locked `project-profile`, and each stage must write durable artifacts. Updated 2026-06-17.

Both [CLAUDE.md](./CLAUDE.md) and [AGENTS.md](./AGENTS.md) serve as the dual-constitution of this repository to ensure full compatibility across multiple AI platforms (Claude Code, Gemini, Codex, Kimi, etc.).

---

## 1. Required Sequence

```text
/profile-discover
/profile-answer
/article-cluster
/profile-research-deep
/profile-lock
/article-intent-research
/article-benchmark
/article-benchmark-extract
/article-evidence-opinions
/article-skeleton
/article-arc
/article-draft
/article-truth-qa
/article-information-gain-qa
/article-benchmark-qa
/article-reader-qa
/article-repair (if a QA gate blocks)
/article-enrich
/article-visual
/article-resources
/article-faq
/article-publish-pack
/article-next
/article-review (30/60/90 days post-publish)
```

Use `/workflow-status` whenever the operator needs to recover context, inspect blockers, check article queue progress, or decide the next safe skill. It is read-only and must not update artifacts or advance stages.

### 1.1 Peer Co-Research & Calibration at Every Stage (`⏸`)
Every stage pauses for **Peer Co-Research & Calibration (对等共研与校准)**. Never merge stages or auto-advance.
- **Neither Human > AI nor AI > Human**: At each pause, both sides examine the output, absorb the domain findings, and conduct divergent research. Only verified evidence, sound logic, and real buyer search intent win. If the AI missed something, the operator challenges it; if the operator brings back an angle or source that is biased, unsupported, or misaligned with buyer intent, the AI must push back with evidence rather than blindly obeying.

### 1.2 Mandatory Apify-First Search & Persistent Credential Lifecycle (铁律)
Whenever any step requires search, external fact verification, competitor research, industry rule confirmation, or material gathering, **Apify MUST be used first** (`python3 scripts/apify_research.py` or `mcp__apify__*`, backed by the persistent rotating token pool in `.env.apify.local` and `~/.config/b2b-seo-agent/apify.env`).
- **Cross-Machine First-Run & Mid-Session Token Hot-Swap (`/system-setup`)**:
  - On a newly cloned machine, run `python3 scripts/setup_env.py --fix` (or `/system-setup`) to verify Python dependencies, hooks, and Apify token readiness.
  - Whenever the user provides `apify_api_...` token(s) in chat — at initial setup or mid-workflow — immediately persist them via `python3 scripts/apify_research.py set-tokens <token...>` or `python3 scripts/apify_research.py add-token <new_token> --prepend --prune-dead`. This writes `0600` files to both `~/.config/b2b-seo-agent/apify.env` and `.env.apify.local` so all future sessions automatically use the updated pool.
- **Apify broken → fix it until it works**: Never bypass Apify or downgrade research depth without diagnosing token slots (`python3 scripts/apify_research.py check`), Actor choice, input schema, dataset parsing, `--browser` mode, or timeouts first. Do not worry about Actor call cost (monthly tokens expire anyway).
- **Combinatorial escalation**: Combine Apify Actors, Scrapling, Scrapy, Crawl4AI, Firecrawl, Playwright real Chrome, and Computer Use across `不同关键词 → 不同页面 → 不同数据源 → 不同 Actor → 不同抓取方式 → 不同技术路径` before ever concluding data cannot be found.

---

## 2. System Rules & Constraints (TRACE Model)

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

## 3. Core Operating Policies

### 3.1 Locked Profile Gate
Article production skills must check `project-profile.md`, `project-profile.json`, and `state.json`. If `lockedProfile` is not true, stop and route to `/profile-discover`, `/profile-answer`, `/article-cluster`, `/profile-research-deep`, or `/profile-lock`.

### 3.2 Benchmark-Led Writing
The drafting stack is **Imitate → Inject → Differentiate**:
1. **Imitate** the selected benchmark article's structure, rhythm, answerability moments, and voice.
2. **Inject** the project's Tier 1 evidence, project data, verified facts, and expert judgments where they change the reader's decision.
3. **Differentiate** through scene-driven voice execution, project-specific proof, and non-lazy structure variation.

The imitation/injection/differentiation ratio is a writing decision, not a fixed constitution rule. Before drafting, the agent must choose exact working percentages for the current article, make sure the three values total 100, and explain why: stronger benchmark fit usually means heavier imitation; stronger proprietary evidence or unusual buyer risk usually means heavier injection/differentiation.

Use the same numeric-control rule for other subjective controls: AIO capture target, bold judgment target, opinion intensity, evidence pressure, section count, and format repetition tolerance must be chosen as concrete numbers, then justified. Numbers give the agent direction; they are not mechanical quotas or fake quality scores.

Before drafting, read the **full benchmark article** — not a sample. Anchor the voice in the primary benchmark, then let the project's evidence and style shape the prose.

Borrowed benchmark assets are allowed. They must be recorded in `benchmark-asset-ledger.md`, transformed into the current profile's role, and referenced by the section contracts embedded in `skeleton.md`.

AIO capture is a strategic goal. Capture as many natural AI Overview opportunities as the article earns, but do not force a fixed number of answer blocks, a bold sentence in every H2, or a machine-answer format that breaks benchmark rhythm.

### 3.3 Evidence Stage as Upstream Validator
`/article-evidence-opinions` is both an evidence gatherer and an upstream validator. If fact checking reveals errors in `benchmark-success-formula.md`, `topic-card.md`, or other upstream artifacts, the agent must emit `upstream-revision-suggestions.md`, update `state.json` accordingly, and pause before `/article-skeleton` until corrections are accepted. Optionally produce `evidence-handoff-summary.md` as a structured handoff brief to the skeleton/draft stages.

### 3.4 QA Gates
Run all four QA gates before publish packaging:
1. **Truth QA** — every claim maps to evidence; also rechecks arithmetic, units, comparative claims, and safety-critical specs.
2. **Information Gain QA** — the article and its decision-critical sections contain insights only this business can provide.
3. **Benchmark Drift QA** — the draft still follows the Structural Blueprint and benchmark success formula.
4. **Reader QA** — it reads like one continuous human-authored piece and blocks complete-but-flat drafts.

Do not let evidence work, answerability, or visual enrichment turn benchmark-led content into a mechanical SEO template.

### 3.5 H2 Design Principle
Headings are search-facing questions, not internal section labels. By default every H2 must:
- Be formatted as a question.
- Balance **70% clean SEO** (standard entities, search-intent match, PAA/AIO indexability) with **30% micro-tension** (Actually, Really, Mistake, Costly, Trap, Number One, Lock You Out) to serve both Google AI Overviews and human click-through.
- Integrate upstream H2 assets from `intent-research.md`, `content-type-library.md`, `topic-card.md`, `benchmark-candidates.md`, `benchmarks/*-extraction.md`, and `benchmark-success-formula.md`; do not ignore or duplicate them.

**Verifiable research requirement:** Live multi-channel research (Google PAA, Google Autocomplete, Reddit/forums, Chinese social, non-text sources) belongs to `/article-intent-research`. `/article-skeleton` consumes the pre-built pool in `intent-research.md` and does not perform live extraction. Every live-extracted candidate must be traceable to a source URL, extraction method, and timestamp. Inferred or "style" candidates are unacceptable substitutes. If a channel cannot be extracted, the failure must be logged with a workaround.

Section function (what the paragraph does) and H2 text (what the searcher sees) are two different things. The former is borrowed from benchmarks; the latter must be rewritten through the 7:3 lens.

### 3.5a Seven Deep-Search & B2B Persuasion Pillars (v3.4 Upgrade)

1. **Buying Committee Multi-Persona & Internal Champion Enablement**: Equip the technical searcher (Specifier) with a forwardable TCO/risk decision ledger for the budget approver (Procurement/CFO/Owner).
2. **Self-Contained RAG Citation Chunks (GEO / AI Search)**: Open key question H2s with a 40–60 word self-contained passage (explicit entity + condition + verdict + metric, no dangling pronouns).
3. **SERP Consensus Target vs. Contrarian Counter-Move**: Extract what SERP Top 5 repeat in unison in `intent-research.md` and counter those platitudes with Tier 1 proof.
4. **Above-the-Fold Viewport Contract (Navboost)**: Pair the first 180 words (direct answer + reframe + path router) with an immediate interactive/visual micro-anchor.
5. **Hub & Spoke Topology + Cannibalization Guard**: Merge keywords with >60% SERP URL overlap in `/article-cluster` and assign `Pillar Hub` vs. `Supporting Spoke` roles.
6. **Named E-E-A-T Technical Author & Reviewer**: Bind named engineer/reviewer personas in `project-profile.md` through prose and `schema.json` `author`/`reviewedBy`.
7. **Forensic Specificity & Anti-Sell Disqualification Proof**: Document caliper/tolerance-level proof alongside 2–3 honest scenarios where our high-spec product is overkill/not recommended.

### 3.6 Anti-Presupposition Rule

During planning stages — before `lockedProfile` is true and before `/article-skeleton` begins — agents must describe *how* an answer will be found, not what the answer is expected to be.

Planning outputs must NOT include:
- Expected specific answers or conclusions
- Unverified examples presented as facts
- Specific numbers, prices, or specs not sourced from the locked profile or verified research
- Prejudged benchmark selections or H2 sequences

This rule works alongside the Locked Profile Gate: the profile prevents inventing project context; the Anti-Presupposition Rule prevents agents from baking expected outcomes into the methodology itself.

---

## 4. Local Validation

Before claiming the workflow structure is ready, run these validation tools:
```bash
python3 scripts/validate_discovery_profile_workflow.py
python3 -m pytest tests/
python3 scripts/deep_audit.py
```

## 5. Headroom Context Compression

Headroom is installed and active for Claude Code globally. It compresses tool outputs, files, logs, and conversation context before sending to the LLM, which helps in long-context article stages (benchmark extraction, evidence review, QA gates). The proxy is managed by Claude Code startup hooks and exposes a `headroom_retrieve` MCP tool for accessing original uncompressed sources. Do not strip context manually to save tokens.

## 6. Subagent-First Context Policy

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
