---
name: system-setup
description: "Use when: (1) initializing the B2B SEO Agent Engine after cloning onto a new computer, (2) the user pastes or provides an Apify API key (apify_api_...) or search API key to save for persistent future use, (3) rotating, adding, or pruning expired Apify tokens mid-workflow, or (4) running an environment health check (Python deps, Chrome, hooks, workspaces)."
argument-hint: '[--fix | set-tokens <apify_api_...> | add-token <apify_api_...> | init <project-slug>]'
user-invocable: true

allowed-tools:
  - Bash
  - Read
  - Edit
  - Write
---

# /system-setup

## Argument Contract

Use `$ARGUMENTS` as optional setup commands, Apify tokens (`apify_api_...`), or a new project workspace slug (`content-workspace/<project-slug>`).

If `$ARGUMENTS` is empty, run the full environment doctor and interactive onboarding check.
If `$ARGUMENTS` contains one or more `apify_api_...` tokens, immediately persist them into the machine's global and repo-local credential pool and verify live quota.

## Purpose

Ensure the B2B SEO & GEO Agent Engine works out of the box on **any newly cloned computer** and handles **mid-workflow credential rotation** without manual file editing.

Specifically, this skill solves four cross-machine lifecycle needs:
1. **First-Run Environment Doctor & Auto-Repair**: Checks Python 3.9+, `pyyaml`, `pytest`, Playwright/System Google Chrome, script executable permissions, and `PreToolUse` hook registration (`scripts/hooks/publish_gate.py`).
2. **Persistent Apify Token Pool Setup**: When the user provides one or more `apify_api_...` tokens, saves them with `0600` (`chmod 600`) permissions to **both**:
   - `~/.config/b2b-seo-agent/apify.env` (machine-wide persistence across all sessions, git branches, and clones on that computer)
   - `<repo>/.env.apify.local` (repo-local persistence, git-ignored)
3. **Mid-Session Token Hot-Swap & Auto-Pruning**: When a token expires or hits its monthly USD limit mid-workflow, the user can paste a new token in chat at any pause (`⏸`); this skill adds/promotes the new token, prunes dead/exhausted slots, and lets the current workflow stage resume immediately.
4. **New Workspace Scaffolding**: Initializes a clean `content-workspace/<project-slug>/` directory (`state.json`, `source-library/`, `knowledge/fact-library.json`, `knowledge/site-link-graph.json`) ready for `/profile-discover`.

---

## Instructions

### Case 1: Full Environment Diagnosis & Auto-Fix (Default on a New Machine)

Run the zero-dependency bootstrapper and doctor script:

```bash
python3 scripts/setup_env.py --fix
```

Review the JSON output:
- **`dependencies.pyyaml`**: Auto-installed when `--fix` is passed.
- **`security_hooks.pre_tool_use_publish_gate`**: Confirms `.claude/settings.json` registers `scripts/hooks/publish_gate.py`.
- **`apify_token_pool.ready`**:
  - If `configured_count == 0` or `ready == false`, ask the user directly:
    > "当前电脑尚未配置可用的 Apify API Key（或现有 Key 额度已耗尽）。请直接把你的 1～N 个 `apify_api_...` 密钥粘贴到对话框里，我会自动为你加密持久化到本机 `~/.config/b2b-seo-agent/apify.env` 与项目 `.env.apify.local`（权限 `600`），后续所有会话永久自动调用。"

---

### Case 2: Initial Input or Full Replacement of Apify API Keys

When the user provides their initial Apify token(s) or asks to replace the entire token pool:

```bash
python3 scripts/apify_research.py set-tokens <token_1> [<token_2> <token_3> ...]
```

What this does automatically:
1. Deduplicates and writes `APIFY_TOKEN`, `APIFY_TOKEN_FALLBACK_1..N`, and `APIFY_TOKEN_SPARE1..N` to both `<repo>/.env.apify.local` and `~/.config/b2b-seo-agent/apify.env` with `0600` permissions.
2. Calls Apify `/v2/users/me` and `/v2/users/me/limits` for every slot and prints only **masked tokens** (`apify_api_...xxxx`), account usernames, and remaining monthly USD quota (`remainingUsd`).
3. Never echoes raw secret strings into stdout or Markdown artifacts.

---

### Case 3: Mid-Workflow Hot-Swap / Adding a New Token / Pruning Expired Keys

When the user says mid-task: *"我换了个新的 Apify Key: `apify_api_xxx`"* or *"再加一个备用 Key"* or *"把失效的 Key 清理掉"*:

1. **Add new token(s), promote to primary Slot #1, and automatically prune dead/exhausted tokens**:
   ```bash
   python3 scripts/apify_research.py add-token <new_token_1> [<new_token_2> ...] --prepend --prune-dead
   ```
2. **Remove a specific slot or token suffix**:
   ```bash
   python3 scripts/apify_research.py remove-token <slot_number_or_suffix>
   ```
3. **Prune all dead (401/403) or quota-exhausted tokens without adding a new one**:
   ```bash
   python3 scripts/apify_research.py prune-dead
   ```
4. **Check live quota across all slots at any time**:
   ```bash
   python3 scripts/apify_research.py check
   ```

---

### Case 4: Persisting Optional Fallback Search Keys (Tavily / Firecrawl / Exa / You.com)

If the user provides optional fallback scraper/search API keys on a new computer:

```bash
python3 scripts/setup_env.py --set-key TAVILY_API_KEY=<key> FIRECRAWL_API_KEY=<key>
```

Keys are stored in `~/.config/b2b-seo-agent/search.env` with `0600` permissions.

---

### Case 5: Scaffolding a Brand-New Project Workspace

When starting a new B2B website project on a freshly cloned machine:

```bash
python3 scripts/setup_env.py --init-workspace <project-slug>
```

This creates `content-workspace/<project-slug>/` with valid initial `state.json`, `source-library/README.md`, `knowledge/fact-library.json`, and `knowledge/site-link-graph.json`, ready for `/profile-discover content-workspace/<project-slug>`.

---

## Examples

### Example 1: First-Time Setup on a New Computer
输入: `/system-setup apify_api_ExampleKey1111111111111111111111`
输出: `Persisted 1 Apify token slot to ~/.config/b2b-seo-agent/apify.env and .env.apify.local (0600), verified live quota, and confirmed PyYAML + PreToolUse hook readiness.`

### Example 2: Mid-Workflow Token Hot-Swap
输入: `/system-setup add-token apify_api_NewBackupKey2222222222222222 --prepend --prune-dead`
输出: `Promoted new token to Slot #1, pruned exhausted slot, and updated persistent 0600 env files without interrupting the active article stage.`

## Guardrails

- **Never Commit Secrets**: Never write raw `apify_api_...` tokens into tracked Markdown files, `project-profile.md`, `state.json`, or Git commits. Always use `scripts/apify_research.py` or `scripts/setup_env.py` so secrets stay in `0600` git-ignored env files.
- **Mask Output**: Always report tokens to the user in masked form (`apify_api_...xxxx`) along with their verified `remainingUsd` balance.
- **Seamless Continuation**: If the user provides a new API key in the middle of an article stage (e.g., `/article-intent-research` or `/article-evidence-opinions`), run `add-token --prepend --prune-dead` immediately and resume that exact stage without resetting workflow state.
