#!/usr/bin/env python3
"""Project-local Apify research entry point; Python standard library only.

Loads tokens from project `.env.apify.local` or `~/.config/b2b-seo-agent/apify.env`
(supporting both APIFY_TOKEN_FALLBACK_1/2 and APIFY_TOKEN_SPARE1/2), automatically
selects an authenticated slot, and supports:
  - check: verify all configured token slots
  - discover: search Apify Actor Store for specialized actors
  - schema: inspect an Actor's default build input schema
  - run: run apify/rag-web-browser (or any --actor with --input-json) and fetch dataset
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
SLOT_KEYS = (
    ("APIFY_TOKEN",),
    ("APIFY_TOKEN_FALLBACK_1", "APIFY_TOKEN_SPARE1"),
    ("APIFY_TOKEN_FALLBACK_2", "APIFY_TOKEN_SPARE2"),
)


def _load_env_file(env_file: Path) -> None:
    if not env_file.exists():
        return
    if env_file.stat().st_mode & 0o077:
        os.chmod(env_file, 0o600)
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line_s = line.strip()
        if line_s and not line_s.startswith("#") and "=" in line_s:
            key, value = line_s.split("=", 1)
            k = key.strip()
            v = value.strip().strip("'\"")
            if v and k not in os.environ:
                os.environ[k] = v


def load_tokens() -> list[tuple[int, str]]:
    _load_env_file(ROOT / ".env.apify.local")
    _load_env_file(Path.home() / ".config" / "b2b-seo-agent" / "apify.env")
    tokens: list[tuple[int, str]] = []
    seen: set[str] = set()
    for idx, candidates in enumerate(SLOT_KEYS, start=1):
        for key in candidates:
            val = os.environ.get(key, "").strip()
            if val and val not in seen:
                tokens.append((idx, val))
                seen.add(val)
                break
    if not tokens:
        raise RuntimeError(
            "Missing Apify credentials: configure .env.apify.local or ~/.config/b2b-seo-agent/apify.env"
        )
    return tokens


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
    api(token, "/users/me")
    info: dict = {"http_status": 200, "authenticated": True, "quota_exhausted": False}
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
    raise RuntimeError("All Apify token slots failed or exhausted quota: " + json.dumps(failures))


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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="Verify all configured Apify token slots without printing secrets")

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
    run.add_argument("--slot", type=int, choices=(1, 2, 3), help="Force a specific credential slot")

    args = parser.parse_args(argv)
    tokens = load_tokens()

    if args.command == "check":
        results = []
        for slot, token in tokens:
            try:
                q = check_slot_quota(token)
                results.append({"slot": slot, **q})
            except ApiError as exc:
                results.append({"slot": slot, "http_status": exc.status, "authenticated": False})
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
