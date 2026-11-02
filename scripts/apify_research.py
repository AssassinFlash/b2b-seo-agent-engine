#!/usr/bin/env python3
"""Project-local Apify research & persistent token-pool manager; Python standard library only.

Loads tokens from project `.env.apify.local`, `~/.config/b2b-seo-agent/apify.env`,
or `~/.config/b2b-seo-agent/apify.env` (supporting APIFY_TOKEN, APIFY_TOKEN_FALLBACK_1..9,
and APIFY_TOKEN_SPARE1..9), automatically selects an authenticated slot with remaining
monthly USD quota, and supports:
  - check: verify all configured token slots and show masked tokens + remaining USD quota
  - set-tokens: overwrite persistent token pool with 1..N tokens (writes 0600 to global + local env)
  - add-token: append/promote 1..N tokens into the persistent pool (optionally --prune-dead)
  - remove-token: remove a token by slot index (1, 2, ...) or token substring/suffix
  - prune-dead: test all slots and automatically remove invalid (401/403) or exhausted tokens
  - discover: search Apify Actor Store for specialized actors
  - schema: inspect an Actor's default build input schema
  - run: run apify/rag-web-browser (or any --actor / --preset with --input-json) and fetch dataset
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "https://api.apify.com/v2"
LOCAL_ENV_PATH = ROOT / ".env.apify.local"
GLOBAL_ENV_PATH = Path.home() / ".config" / "b2b-seo-agent" / "apify.env"
LEGACY_GLOBAL_ENV_PATH = Path.home() / ".config" / "b2b-seo-agent" / "apify.env"

SLOT_KEYS: tuple[tuple[str, ...], ...] = (
    ("APIFY_TOKEN",),
    ("APIFY_TOKEN_FALLBACK_1", "APIFY_TOKEN_SPARE1"),
    ("APIFY_TOKEN_FALLBACK_2", "APIFY_TOKEN_SPARE2"),
    ("APIFY_TOKEN_FALLBACK_3", "APIFY_TOKEN_SPARE3"),
    ("APIFY_TOKEN_FALLBACK_4", "APIFY_TOKEN_SPARE4"),
    ("APIFY_TOKEN_FALLBACK_5", "APIFY_TOKEN_SPARE5"),
    ("APIFY_TOKEN_FALLBACK_6", "APIFY_TOKEN_SPARE6"),
    ("APIFY_TOKEN_FALLBACK_7", "APIFY_TOKEN_SPARE7"),
    ("APIFY_TOKEN_FALLBACK_8", "APIFY_TOKEN_SPARE8"),
    ("APIFY_TOKEN_FALLBACK_9", "APIFY_TOKEN_SPARE9"),
)


def mask_token(token: str) -> str:
    t = token.strip()
    if len(t) <= 14:
        return "***"
    return f"{t[:10]}...{t[-4:]}"


def _read_env_dict(env_file: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    if not env_file.exists():
        return out
    try:
        if env_file.stat().st_mode & 0o077:
            os.chmod(env_file, 0o600)
    except OSError:
        pass
    for line in env_file.read_text(encoding="utf-8", errors="replace").splitlines():
        line_s = line.strip()
        if line_s and not line_s.startswith("#") and "=" in line_s:
            key, value = line_s.split("=", 1)
            k = key.strip()
            v = value.strip().strip("'\"")
            if k and v:
                out[k] = v
    return out


def _load_env_file(env_file: Path, override: bool = False) -> None:
    for k, v in _read_env_dict(env_file).items():
        if override or k not in os.environ:
            os.environ[k] = v


def load_tokens(allow_empty: bool = False) -> list[tuple[int, str]]:
    for env_path in (LOCAL_ENV_PATH, GLOBAL_ENV_PATH, LEGACY_GLOBAL_ENV_PATH):
        _load_env_file(env_path)
    tokens: list[tuple[int, str]] = []
    seen: set[str] = set()
    for idx, candidates in enumerate(SLOT_KEYS, start=1):
        for key in candidates:
            val = os.environ.get(key, "").strip()
            if val and val not in seen:
                tokens.append((idx, val))
                seen.add(val)
                break
    if not tokens and not allow_empty:
        raise RuntimeError(
            "Missing Apify credentials: run `python3 scripts/apify_research.py set-tokens <apify_api_...>` "
            "or invoke `/system-setup` to persist your Apify API key(s)."
        )
    return tokens


def write_persistent_tokens(token_list: list[str], sync_global: bool = True) -> dict:
    """Persist deduplicated token list into .env.apify.local and ~/.config/b2b-seo-agent/apify.env with chmod 600."""
    cleaned: list[str] = []
    seen: set[str] = set()
    for raw in token_list:
        for part in re.split(r"[\s,;]+", raw.strip()):
            t = part.strip().strip("'\"")
            if not t:
                continue
            if t not in seen:
                cleaned.append(t)
                seen.add(t)

    lines = [
        "# Persistent Apify API Token Pool (auto-managed by scripts/apify_research.py)",
        "# Permissions: 0600 (owner read/write only). Never commit to Git.",
    ]
    for i, tok in enumerate(cleaned):
        if i == 0:
            lines.append(f"APIFY_TOKEN={tok}")
        else:
            lines.append(f"APIFY_TOKEN_FALLBACK_{i}={tok}")
            lines.append(f"APIFY_TOKEN_SPARE{i}={tok}")
    content = "\n".join(lines) + "\n"

    written_paths: list[str] = []
    targets = [LOCAL_ENV_PATH]
    if sync_global:
        targets.append(GLOBAL_ENV_PATH)
        if LEGACY_GLOBAL_ENV_PATH.exists():
            targets.append(LEGACY_GLOBAL_ENV_PATH)

    for target in targets:
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            os.chmod(target, 0o600)
            written_paths.append(str(target))
        except OSError:
            continue

    # Refresh in-process environment variables so immediate check/run uses the updated pool
    for candidates in SLOT_KEYS:
        for k in candidates:
            os.environ.pop(k, None)
    _load_env_file(LOCAL_ENV_PATH, override=True)

    return {
        "configured_slots": len(cleaned),
        "masked_tokens": [mask_token(t) for t in cleaned],
        "persisted_to": written_paths,
    }


class ApiError(RuntimeError):
    def __init__(self, status: int, error_type: str):
        self.status = status
        super().__init__(f"Apify HTTP {status}: {error_type}")


def api(token: str, path: str, payload: dict | None = None):
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        BASE + path,
        data=data,
        headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"},
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            try:
                kind = json.loads(exc.read()).get("error", {}).get("type", "unknown")
            except (ValueError, AttributeError):
                kind = "non-json-error"
            if payload is None and (exc.code == 429 or exc.code >= 500) and attempt < 2:
                try:
                    delay = min(20, max(1, int(exc.headers.get("Retry-After", "3"))))
                except ValueError:
                    delay = 3
                time.sleep(delay * (attempt + 1))
                continue
            raise ApiError(exc.code, kind) from None
        except (urllib.error.URLError, TimeoutError):
            if payload is None and attempt < 2:
                time.sleep(2 * (attempt + 1))
                continue
            raise RuntimeError(
                "Apify network/timeout error. If this happened on a start POST, check existing runs before retrying."
            ) from None


def check_slot_quota(token: str) -> dict:
    """Verify token authentication and check /users/me/limits for remaining monthly USD quota."""
    me = (api(token, "/users/me") or {}).get("data") or {}
    info: dict = {
        "http_status": 200,
        "authenticated": True,
        "quota_exhausted": False,
        "masked_token": mask_token(token),
    }
    if me.get("username"):
        info["username"] = me.get("username")
    try:
        limits_data = (api(token, "/users/me/limits") or {}).get("data") or {}
        current = limits_data.get("current") or {}
        limits = limits_data.get("limits") or {}
        used = current.get("monthlyUsageUsd")
        max_usd = limits.get("maxMonthlyUsageUsd")
        if isinstance(used, (int, float)) and isinstance(max_usd, (int, float)) and max_usd > 0:
            info["monthlyUsageUsd"] = round(float(used), 4)
            info["maxMonthlyUsageUsd"] = round(float(max_usd), 4)
            info["remainingUsd"] = round(float(max_usd - used), 4)
            if used >= max_usd:
                info["quota_exhausted"] = True
    except ApiError:
        pass
    return info


def select_token(tokens: list[tuple[int, str]]) -> tuple[int, str]:
    failures = []
    for slot, token in tokens:
        try:
            q = check_slot_quota(token)
            if q.get("quota_exhausted"):
                failures.append({"slot": slot, "reason": "monthly_quota_exhausted", "remainingUsd": q.get("remainingUsd", 0)})
                continue
            return slot, token
        except ApiError as exc:
            if exc.status not in (401, 403, 402, 429):
                raise
            failures.append({"slot": slot, "http_status": exc.status})
    raise RuntimeError(
        "All Apify token slots failed or exhausted quota: "
        + json.dumps(failures)
        + ". Paste a fresh Apify token in chat or run `python3 scripts/apify_research.py add-token <new_token> --prune-dead`."
    )


def api_with_transient_retry(token: str, path: str, payload: dict | None = None, retries: int = 3):
    """Call api() with bounded retries on transient 500/502/503/504 or network errors during polling."""
    for attempt in range(retries):
        try:
            return api(token, path, payload)
        except ApiError as exc:
            if exc.status in (500, 502, 503, 504) and attempt + 1 < retries:
                time.sleep(2 * (attempt + 1))
                continue
            raise
        except RuntimeError:
            if attempt + 1 < retries and payload is None:
                time.sleep(2 * (attempt + 1))
                continue
            raise


def call_with_failover(tokens: list[tuple[int, str]], path: str) -> tuple[int, str, dict]:
    """Execute a read API request across token slots, failing over on 401/402/403/429."""
    failures = []
    for slot, token in tokens:
        try:
            q = check_slot_quota(token)
            if q.get("quota_exhausted"):
                failures.append({"slot": slot, "reason": "monthly_quota_exhausted"})
                continue
            return slot, token, api(token, path)
        except ApiError as exc:
            if exc.status not in (401, 402, 403, 429):
                raise
            failures.append({"slot": slot, "http_status": exc.status})
    raise RuntimeError("All Apify token slots failed on request: " + json.dumps(failures))


def launch_run_with_failover(
    tokens: list[tuple[int, str]],
    actor_ref: str,
    payload: dict,
    max_charge_usd: float | None = None,
) -> tuple[int, str, dict]:
    """Try launching an Actor run across available token slots, failing over on 401/402/403/429."""
    failures = []
    for slot, token in tokens:
        try:
            q = check_slot_quota(token)
            if q.get("quota_exhausted"):
                failures.append({"slot": slot, "reason": "monthly_quota_exhausted"})
                continue
            actor_info = api(token, f"/acts/{actor_ref}")["data"]
            build = actor_info.get("defaultRunOptions", {}).get("build", "latest")
            options: dict[str, int | float | str] = {"build": build, "timeout": 180, "memory": 2048}
            if max_charge_usd is not None:
                options["maxTotalChargeUsd"] = max_charge_usd
            query_str = urllib.parse.urlencode(options)
            meta = api(token, f"/acts/{actor_ref}/runs?{query_str}", payload)["data"]
            return slot, token, meta
        except ApiError as exc:
            if exc.status not in (401, 402, 403, 429):
                raise
            failures.append({"slot": slot, "http_status": exc.status, "detail": str(exc)[:200]})
    raise RuntimeError("All Apify token slots failed to launch Actor run: " + json.dumps(failures))


def _resolve_repo_path(path: Path) -> Path:
    path = Path(path)
    if not path.is_absolute() and not path.exists():
        if str(path).startswith("content-workspace") or (ROOT / path.parent).exists():
            return ROOT / path
    return path


def save(path: Path, value) -> None:
    path = _resolve_repo_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def save_compact_summary(json_path: Path, items: list | dict) -> Path:
    """Write a lightweight .summary.md file next to large Apify JSON outputs to protect main/subagent context."""
    json_path = _resolve_repo_path(json_path)
    summary_path = json_path.with_suffix(".summary.md")
    rows = items if isinstance(items, list) else (items.get("items") or [items])
    lines = [
        f"# Apify Research Compact Summary — `{json_path.name}`",
        "",
        f"- **Total items**: {len(rows)}",
        "",
    ]
    for idx, item in enumerate(rows[:25], start=1):
        if not isinstance(item, dict):
            continue
        title = (
            item.get("title")
            or (item.get("metadata") or {}).get("title")
            or item.get("name")
            or f"Item {idx}"
        )
        url = item.get("url") or (item.get("metadata") or {}).get("url") or ""
        md = str(item.get("markdown") or item.get("text") or item.get("description") or "")
        headings = re.findall(r"(?m)^#{1,3}\s+(.+)$", md)[:8]
        snippet = re.sub(r"\s+", " ", md)[:280].strip()
        lines.append(f"## {idx}. {title}")
        if url:
            lines.append(f"- **URL**: {url}")
        if headings:
            lines.append(f"- **Headings**: {' | '.join(headings)}")
        if snippet:
            lines.append(f"- **Excerpt**: {snippet}...")
        lines.append("")
    summary_path.write_text("\n".join(lines), encoding="utf-8")
    return summary_path


def _verify_all_tokens(tokens: list[tuple[int, str]]) -> list[dict]:
    results = []
    for slot, token in tokens:
        try:
            q = check_slot_quota(token)
            results.append({"slot": slot, **q})
        except ApiError as exc:
            results.append({
                "slot": slot,
                "http_status": exc.status,
                "authenticated": False,
                "masked_token": mask_token(token),
            })
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="Verify all configured Apify token slots without printing secrets")

    set_tok = sub.add_parser("set-tokens", help="Overwrite persistent Apify token pool (writes 0600 to local & global env)")
    set_tok.add_argument("tokens", nargs="+", help="One or more Apify API tokens (e.g. apify_api_...)")
    set_tok.add_argument("--local-only", action="store_true", help="Write only to repo .env.apify.local")
    set_tok.add_argument("--no-verify", action="store_true", help="Skip live API verification after writing")

    add_tok = sub.add_parser("add-token", help="Add or promote token(s) into the persistent Apify token pool")
    add_tok.add_argument("tokens", nargs="+", help="One or more new Apify API tokens")
    add_tok.add_argument("--prepend", action="store_true", help="Place new token(s) at Slot #1 (primary)")
    add_tok.add_argument("--prune-dead", action="store_true", help="Automatically remove invalid or exhausted existing tokens")
    add_tok.add_argument("--local-only", action="store_true", help="Write only to repo .env.apify.local")
    add_tok.add_argument("--no-verify", action="store_true", help="Skip live API verification")

    rm_tok = sub.add_parser("remove-token", help="Remove a token by slot number (1, 2, ...) or token suffix/substring")
    rm_tok.add_argument("target", help="Slot number (e.g. '1') or token suffix/substring")
    rm_tok.add_argument("--local-only", action="store_true", help="Write only to repo .env.apify.local")

    prune = sub.add_parser("prune-dead", help="Test all slots and remove invalid (401/403) or quota-exhausted tokens")
    prune.add_argument("--local-only", action="store_true", help="Write only to repo .env.apify.local")

    discover = sub.add_parser("discover", help="Search Apify Actor Store for task-specific actors")
    discover.add_argument("query")
    discover.add_argument("--limit", type=int, default=8)
    discover.add_argument("--output", type=Path, required=True)

    schema = sub.add_parser("schema", help="Inspect an Actor's default build input schema")
    schema.add_argument("actor", help="username/name or Actor ID")
    schema.add_argument("--output", type=Path, required=True)

    run = sub.add_parser("run", help="Run apify/rag-web-browser or a specified --actor / --preset")
    run.add_argument("query", nargs="?", default="", help="Search query or URL")
    run.add_argument("--actor", default="apify/rag-web-browser", help="Actor username/name (default: apify/rag-web-browser)")
    run.add_argument(
        "--preset",
        choices=("rag-browser", "google-serp", "website-crawler"),
        help="Optional preset recipe that selects actor + default payload shape",
    )
    run.add_argument("--input-json", help="Custom JSON payload string or @path for non-default actors")
    run.add_argument("--max-results", type=int, default=5)
    run.add_argument("--max-charge-usd", type=float, help="Optional per-run USD charge ceiling")
    run.add_argument("--browser", action="store_true", help="Use browser-playwright mode in rag-web-browser")
    run.add_argument("--output", type=Path, required=True)
    run.add_argument("--resume", help="Resume waiting on an existing runId")
    run.add_argument("--slot", type=int, choices=tuple(range(1, len(SLOT_KEYS) + 1)), help="Force a specific credential slot")

    args = parser.parse_args(argv)

    if args.command == "set-tokens":
        meta = write_persistent_tokens(args.tokens, sync_global=not args.local_only)
        tokens = load_tokens(allow_empty=True)
        checks = [] if args.no_verify else _verify_all_tokens(tokens)
        print(json.dumps({**meta, "slots": checks}, ensure_ascii=False, indent=2))
        return 0 if (args.no_verify or any(r.get("authenticated") and not r.get("quota_exhausted") for r in checks)) else 1

    if args.command == "add-token":
        existing = [tok for _, tok in load_tokens(allow_empty=True)]
        if args.prune_dead and existing:
            alive: list[str] = []
            for tok in existing:
                try:
                    q = check_slot_quota(tok)
                    if not q.get("quota_exhausted"):
                        alive.append(tok)
                except ApiError:
                    continue
            existing = alive
        combined = (list(args.tokens) + existing) if args.prepend else (existing + list(args.tokens))
        meta = write_persistent_tokens(combined, sync_global=not args.local_only)
        tokens = load_tokens(allow_empty=True)
        checks = [] if args.no_verify else _verify_all_tokens(tokens)
        print(json.dumps({**meta, "slots": checks}, ensure_ascii=False, indent=2))
        return 0 if (args.no_verify or any(r.get("authenticated") and not r.get("quota_exhausted") for r in checks)) else 1

    if args.command == "remove-token":
        existing = load_tokens(allow_empty=True)
        target = args.target.strip()
        kept: list[str] = []
        removed: list[str] = []
        is_slot_num = target.isdigit() and 1 <= int(target) <= len(SLOT_KEYS)
        for slot, tok in existing:
            matched = (int(target) == slot) if is_slot_num else (len(target) >= 4 and target in tok)
            if matched:
                removed.append(mask_token(tok))
            else:
                kept.append(tok)
        meta = write_persistent_tokens(kept, sync_global=not args.local_only)
        print(json.dumps({"removed": removed, **meta}, ensure_ascii=False, indent=2))
        return 0

    if args.command == "prune-dead":
        existing = load_tokens(allow_empty=True)
        alive: list[str] = []
        pruned: list[dict] = []
        for slot, tok in existing:
            try:
                q = check_slot_quota(tok)
                if q.get("quota_exhausted"):
                    pruned.append({"slot": slot, "masked_token": mask_token(tok), "reason": "quota_exhausted"})
                else:
                    alive.append(tok)
            except ApiError as exc:
                pruned.append({"slot": slot, "masked_token": mask_token(tok), "reason": f"http_{exc.status}"})
        meta = write_persistent_tokens(alive, sync_global=not args.local_only)
        print(json.dumps({"pruned": pruned, **meta}, ensure_ascii=False, indent=2))
        return 0

    tokens = load_tokens()

    if args.command == "check":
        results = _verify_all_tokens(tokens)
        print(json.dumps(results, ensure_ascii=False))
        return 0 if any(r["authenticated"] and not r.get("quota_exhausted") for r in results) else 1

    if args.command in ("discover", "schema"):
        if args.command == "discover":
            if not 1 <= args.limit <= 100:
                raise RuntimeError("Store limit must be 1–100")
            path = "/store?" + urllib.parse.urlencode({"search": args.query, "limit": args.limit})
            slot, token, resp = call_with_failover(tokens, path)
            data = resp["data"]
            fields = ("id", "username", "name", "title", "description", "url", "categories")
            result = {
                "source": BASE + path,
                "query": args.query,
                "total": data.get("total"),
                "status": "discovered-not-adopted",
                "actors": [{k: item.get(k) for k in fields} for item in data.get("items", [])],
            }
        else:
            actor_ref = args.actor.replace("/", "~")
            if not re.fullmatch(r"[A-Za-z0-9_.~-]+", actor_ref):
                raise RuntimeError("Actor must be username/name or ID")
            path = "/acts/" + actor_ref + "/builds/default"
            slot, token, resp = call_with_failover(tokens, path)
            data = resp["data"]
            input_schema = data.get("inputSchema") or data.get("actorDefinition", {}).get("input")
            if isinstance(input_schema, str):
                input_schema = json.loads(input_schema)
            result = {
                "source": BASE + path,
                "actor": args.actor,
                "slot": slot,
                "buildId": data.get("id"),
                "buildNumber": data.get("buildNumber"),
                "buildStatus": data.get("status"),
                "status": "schema-checked",
                "inputSchema": input_schema,
            }
        save(args.output, result)
        print(
            json.dumps(
                {
                    "status": result["status"],
                    "output": str(args.output),
                    "candidates": len(result.get("actors", [])),
                    "buildNumber": result.get("buildNumber"),
                },
                ensure_ascii=False,
            )
        )
        return 0

    if args.slot:
        tokens = [(slot, token) for slot, token in tokens if slot == args.slot]
        if not tokens:
            raise RuntimeError("Requested credential slot is not configured")

    if getattr(args, "preset", None) == "google-serp" and args.actor == "apify/rag-web-browser":
        args.actor = "apify/google-search-scraper"
    elif getattr(args, "preset", None) == "website-crawler" and args.actor == "apify/rag-web-browser":
        args.actor = "apify/website-content-crawler"
    actor_ref = args.actor.replace("/", "~")

    if args.resume:
        slot, token, resp = call_with_failover(tokens, "/actor-runs/" + urllib.parse.quote(args.resume, safe=""))
        meta = resp["data"]
    else:
        if args.input_json:
            if args.input_json.startswith("@"):
                input_path = _resolve_repo_path(Path(args.input_json[1:]))
                payload = json.loads(input_path.read_text(encoding="utf-8"))
            else:
                payload = json.loads(args.input_json)
        elif getattr(args, "preset", None) == "google-serp":
            if not args.query:
                raise RuntimeError("Provide query for --preset google-serp")
            payload = {
                "queries": args.query,
                "resultsPerPage": args.max_results,
                "maxPagesPerQuery": 1,
            }
        elif getattr(args, "preset", None) == "website-crawler":
            if not args.query:
                raise RuntimeError("Provide start URL in query for --preset website-crawler")
            payload = {
                "startUrls": [{"url": u.strip()} for u in args.query.split(",") if u.strip()],
                "maxCrawlPages": args.max_results,
                "saveMarkdown": True,
            }
        else:
            if not args.query:
                raise RuntimeError("Provide query or --input-json")
            payload = {
                "query": args.query,
                "maxResults": args.max_results,
                "outputFormats": ["markdown"],
                "requestTimeoutSecs": 90,
                "desiredConcurrency": 2,
                "scrapingTool": "browser-playwright" if args.browser else "raw-http",
            }
        slot, token, meta = launch_run_with_failover(tokens, actor_ref, payload, args.max_charge_usd)

    journal = args.output.with_suffix(".run.json")
    record = {
        "actor": args.actor,
        "slot": slot,
        "query": args.query,
        "runId": meta["id"],
        "datasetId": meta.get("defaultDatasetId"),
        "status": meta.get("status"),
        "buildId": meta.get("buildId"),
    }
    save(journal, record)
    print(json.dumps(record, ensure_ascii=False), flush=True)

    deadline = time.monotonic() + 240
    while meta["status"] in ("READY", "RUNNING", "ABORTING", "TIMING-OUT"):
        if time.monotonic() > deadline:
            raise RuntimeError("Run still in progress after wait window; use --resume with the saved runId")
        time.sleep(3)
        meta = api_with_transient_retry(token, "/actor-runs/" + meta["id"] + "?waitForFinish=20")["data"]

    record.update(
        status=meta["status"],
        datasetId=meta.get("defaultDatasetId"),
        usageTotalUsd=meta.get("usageTotalUsd"),
        runStats=meta.get("stats"),
        finishedAt=meta.get("finishedAt"),
    )
    save(journal, record)
    if meta["status"] != "SUCCEEDED":
        raise RuntimeError(f"Actor did not succeed ({meta['status']}); inspect run logs/schema and repair")

    items = api_with_transient_retry(token, "/datasets/" + meta["defaultDatasetId"] + "/items?clean=true&format=json")
    save(args.output, items)
    summary_path = save_compact_summary(args.output, items)
    print(
        json.dumps(
            {
                "status": meta["status"],
                "items": len(items) if isinstance(items, list) else 1,
                "usageTotalUsd": meta.get("usageTotalUsd"),
                "output": str(args.output),
                "compactSummary": str(summary_path),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("Interrupted wait; resume with --resume <runId>.", file=sys.stderr)
        sys.exit(130)
    except (RuntimeError, ValueError, KeyError, OSError) as exc:
        message = re.sub(r"apify_api_[A-Za-z0-9]+", "[REDACTED]", str(exc))
        print(message, file=sys.stderr)
        sys.exit(1)
