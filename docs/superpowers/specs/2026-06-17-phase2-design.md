# B2B SEO Agent System — Phase 2 Design Specification

This document defines the architectural and functional design specifications for the Phase 2 optimization of the B2B SEO Agent System.

## 1. Deterministic QA Runner (`scripts/run_qa_verifier.py`)

### 1.1 Purpose
Replace LLM-based self-evaluation ("prompt heuristics") with deterministic, programmatic data validation for all four QA gates before publishing packaging. This ensures no low-quality or hallucinated drafts slip through to WordPress.

### 1.2 Data Flow & APIs
- **State Loading**: The runner reads `state.json` to identify `activeArticle` (slug) and `currentStage`.
- **Target File**: Primary analysis is run on `content-workspace/<project-slug>/articles/<activeArticle>/draft.md`.
- **Tavily / Exa Live Search Integration (Option A)**:
  1. The runner parses `draft.md` to extract the primary keyword, secondary keywords, and H2/H3 headings.
  2. It executes live search queries via Tavily Search API (`mcp__tavily__tavily_search`) or Exa Search API (`mcp__exa__exa_search`) for the primary keyword and H2 headings to retrieve the top 5 ranking URLs.
  3. It retrieves the full text content of these 5 competitor pages.
- **Verification Engine**:
  - **Gate 1: Truth QA**: Cross-references claims marked in `draft.md` against the profile evidence ledger and `source-library/` CSV databases. Programmatically verifies that cited source numbers map to actual records.
  - **Gate 2: Information Gain QA**: Computes semantic/textual uniqueness compared to the top 5 retrieved competitor texts. Utilizes a local similarity index (e.g., Cosine/Jaccard similarity) coupled with LLM evaluation to identify unique value/insights (case studies, unique factory data, proprietary diagrams) in the draft.
    - **Threshold**: Information Gain Uniqueness score must be $\ge 40\%$.
  - **Gate 3: Benchmark Drift QA**: Verifies structural layout (H2/H3 count, reading flow, formats) against the chosen benchmark target.
  - **Gate 4: Reader QA**: Validates readability metrics and scans for a blacklist of AI-typical filler words/phrases (e.g., "in conclusion", "delve", "testament").
- **Output Artifacts**:
  - Writes a comprehensive report to `content-workspace/<project-slug>/articles/<activeArticle>/qa-report.json` and a user-readable version at `qa-report.md`.
  - On failure, sets `state.json`'s `qaStatus` to `FAIL` and blocks progress.

### 1.3 Error Handling & Fallback
- If the Tavily/Exa API calls fail (network failure, credentials missing, or rate limits), the runner falls back to analyzing locally cached competitor benchmark documents inside `source-library/` or `project-profile.research.md`.
- A warning banner `[WARNING: Live search failed, using local competitor library]` is prepended to the QA report.

---

## 2. Workflow Navigator (`scripts/workflow_status.py`)

### 2.1 State Flow Enforcement
- The script manages the 15-stage workflow outlined in `config/workflow-spec.yaml` by checking and mutating `state.json`.
- **Command `/workflow-next`**:
  - Inspects `state.json`. If the current stage is one of the QA gates (e.g., `article-truth-qa`), it executes `scripts/run_qa_verifier.py`.
  - **Read-Only Safety Lock (Option A)**:
    - If the verifier fails, the Navigator blocks the transition to the next stage.
    - It locks `nextCommand` in `state.json` to `/article-repair`.
    - **Scene Preservation**: No generated drafts, images, or schemas are deleted or modified. The user/AI must repair the draft file directly and re-run.
  - If validation passes, updates `currentStage` to the next phase in `config/workflow-spec.yaml` and updates `nextCommand`.

### 2.2 Rollback Engine (`/workflow-rollback <stage>`)
- Allows manual or automated rollback to a previous stage.
- **Execution Protocol**:
  1. Validates that the requested `<stage>` exists and is chronologically prior to the `currentStage`.
  2. Updates `currentStage` in `state.json` to `<stage>`.
  3. **Downstream Asset Cleanup**: Deletes or archives temporary files generated in subsequent stages (e.g., partial schemas, incorrect image plans) to prevent stale/incorrect assets from polluting the new execution branch.

---

## 3. Agent Persona Decoupling

### 3.1 Single Source of Truth (SSOT)
All detailed operational SOPs (Phase 1, 2, 3, etc.) are stripped from agent instructions in `.claude/agents/*.md` and consolidated entirely inside `.claude/skills/<skill-name>/SKILL.md`.

### 3.2 Decoupled Agent Spec Structure
Each agent definition in `.claude/agents/` is simplified to contain:
1. **Persona & Tone**: Who they are (e.g., SEO Specialist, Editor, QA).
2. **Red-Lines / Constraints**: Unbendable business boundaries (e.g., "Do not bypass `run_qa_verifier.py`", "Must reject any claim unsupported by evidence").
3. **Inputs/Outputs**: Clear file contracts.
4. **Declared Skills**: YAML list of skills they are permitted to run.

The 5 target agent files to be refactored:
- `topic-cluster-researcher.md`
- `content-repair-strategist.md`
- `performance-review-strategist.md`
- `publish-package-qa.md`
- `publish-readiness-agent.md`
