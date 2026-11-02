# v1.0 → v2.0 → v3.0 变更日志（只读历史）

> 本文档记录历史变更，不参与当前工作流。当前工作流的唯一事实来源是：
> - `config/workflow-spec.yaml`
> - `config/artifact-graph.yaml`
> - `config/state-schema.json`

## v1.0 命令

v1.0 使用 `.claude/commands/` 中的 slash commands：

- `/article-keywords`
- `/article-outline`
- `/article-evidence`
- `/article-section-contracts`

## v2.0 变更

在 v2.0 中，工作流被重新设计为 skill-first，并合并了部分命令：

| v1.0 命令 | v2.0 替代 | 原因 |
|---|---|---|
| `/article-keywords` | `/article-skeleton` | 关键词研究合并到骨架构建阶段 |
| `/article-outline` | `/article-skeleton` + `/article-arc` | Outline 拆分为骨架与叙事弧线 |
| `/article-evidence` | `/article-evidence-opinions` | 工厂 E-E-A-T 与证据收集重构为 evidence-opinion pack |
| `/article-section-contracts` | `/article-skeleton` | Section contracts 内嵌到 `skeleton.md` |

v2.0 还引入了 4 个 QA gate：

1. `/article-truth-qa` → `truth-qa.md`
2. `/article-information-gain-qa` → `information-gain-qa.md`
3. `/article-benchmark-qa` → `benchmark-drift-audit.md`
4. `/article-reader-qa` → `reader-qa.md`

## v3.0 重构

v3.0 完成了 command → skill 的彻底迁移，并建立了规范驱动：

- 删除 `.claude/commands/`；所有入口为 `.claude/skills/*/SKILL.md`。
- 新增 `config/workflow-spec.yaml`、`config/artifact-graph.yaml`、`config/state-schema.json` 作为唯一事实来源。
- 合并重复/矛盾的技能：
  - `profile-foundation` + `project-profile-bootstrap` → `profile-foundation`
  - `voice-factory` + `humanizer` → `voice-and-humanization`
  - `section-contracts` 内嵌到 `/article-skeleton`
- 删除 deprecated agents：`benchmark-led-draft-writer`、`keyword-map-builder`、`section-contract-builder`、`serp-outline-analyst`。
- 删除迁移期审计 skill 与文档：`audit-legacy-agents`、`audit-migration-map`、`audit-video-sop`、`migration-map.md`、`legacy-agent-audit.md`、`video-sop-gap-map.md`。
- 旧样例 `content-workspace/stainless-steel-screen-export/` 与 `.firecrawl/` 数据归档到 `archive/`。
- Agent 调用关系清理：仅保留被 skill 直接调用的 agent，删除未调用或重复的 agent。
  - 保留：`topic-cluster-researcher`、`performance-review-strategist`、`content-repair-strategist`、`publish-readiness-agent`、`publish-package-qa`。
  - 删除：`benchmark-drift-auditor`、`benchmark-transmutation-architect`、`evidence-eat-validator`、`information-gain-qa-editor`、`project-profile-architect`、`reader-experience-editor`、`truth-qa-editor`、`workflow-auditor`、`legacy-agent-auditor`。
- 搜索策略调整：`search-toolbox` 将 firecrawl 从“完全禁用”改为“配额受限的后备工具”，仅在 tavily/exa/crawl4ai/agent-browser 失败后使用。
- 统一 `state.json` 字段为 `nextCommand`（camelCase），清理 skill 中残留的 `next command` 写法。
- 新增可验证样例 `content-workspace/example-metal-divider/` 与基于 spec 的验证脚本。
