#!/usr/bin/env python3
"""Extract real Google "People also ask" questions for a list of queries.

Mandatory Apify-First Order (CLAUDE.md §1.2):
Always run `python3 scripts/apify_research.py run --preset google-serp "<query>" --output <out.json>`
FIRST to capture Google SERP + PAA via Apify's rotating 3-slot tokens. Use this persistent
real-Chrome Playwright script as the complementary expansion / verification channel when interactive
PAA accordion clicking is needed. Never fabricate PAA questions.
"""
from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path
from urllib.parse import quote_plus


UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)
# Selector that matched PAA question text in live testing (2026-06-24). Google
# rotates DOM, so this is recorded as observed, not as a stable contract.
PAA_SELECTOR_HINT = "div[role='button'] / div[jsname] within the 'People also ask' region"


def _utcstamp() -> str:
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def extract_via_apify(queries: list[str], hl: str, gl: str) -> list[dict]:
    """Primary Apify-First PAA extractor using apify/google-search-scraper across the 3 token slots."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import apify_research as ar

    tokens = ar.load_tokens()
    payload = {
        "queries": "\n".join(queries),
        "resultsPerPage": 10,
        "maxPagesPerQuery": 1,
        "languageCode": hl,
        "countryCode": gl.lower(),
    }
    slot, token, meta = ar.launch_run_with_failover(tokens, "apify~google-search-scraper", payload)
    import time

    deadline = time.monotonic() + 180
    while meta["status"] in ("READY", "RUNNING", "ABORTING", "TIMING-OUT"):
        if time.monotonic() > deadline:
            raise RuntimeError("Apify Google SERP run timed out")
        time.sleep(3)
        meta = ar.api_with_transient_retry(token, "/actor-runs/" + meta["id"] + "?waitForFinish=20")["data"]
    if meta["status"] != "SUCCEEDED":
        raise RuntimeError(f"Apify Google SERP actor status: {meta['status']}")
    items = ar.api_with_transient_retry(token, "/datasets/" + meta["defaultDatasetId"] + "/items?clean=true&format=json")
    out: list[dict] = []
    for idx, q in enumerate(queries):
        item = items[idx] if isinstance(items, list) and idx < len(items) else (items[0] if isinstance(items, list) and items else {})
        paa_raw = item.get("peopleAlsoAsk") or []
        questions = [p.get("question", "").strip() for p in paa_raw if isinstance(p, dict) and p.get("question")]
        out.append(
            {
                "query": q,
                "query_url": f"https://www.google.com/search?q={quote_plus(q)}&hl={hl}&gl={gl}",
                "rendered": True,
                "sorry_redirect": False,
                "selector_observed": f"apify/google-search-scraper (slot {slot}) peopleAlsoAsk[]",
                "timestamp": _utcstamp(),
                "questions": questions,
                "related_queries": [r.get("title", "") for r in (item.get("relatedQueries") or []) if isinstance(r, dict)],
                "error": None if questions else "No peopleAlsoAsk returned in SERP dataset",
            }
        )
    return out


def extract_one(page, query: str, hl: str, gl: str, max_retries: int = 2) -> dict:
    url = f"https://www.google.com/search?q={quote_plus(query)}&hl={hl}&gl={gl}"
    rec = {
        "query": query,
        "query_url": url,
        "rendered": False,
        "sorry_redirect": False,
        "selector_observed": None,
        "timestamp": _utcstamp(),
        "questions": [],
        "error": None,
    }
    # Google's anti-bot is rate-sensitive: consecutive /search hits can trip the
    # /sorry wall even with a persistent context. Retry with a backoff if hit.
    for attempt in range(max_retries + 1):
        try:
            page.goto(url, timeout=30000, wait_until="domcontentloaded")
            page.wait_for_timeout(3500)
            for _ in range(3):  # scroll to trigger lazy PAA load
                page.mouse.wheel(0, 1200)
                page.wait_for_timeout(1200)
            if "/sorry" not in page.url:
                break  # got a real SERP
            rec["sorry_redirect"] = True
            if attempt < max_retries:
                page.wait_for_timeout(8000 * (attempt + 1))  # backoff 8s, 16s
        except Exception as e:  # pragma: no cover
            if "Timeout" in type(e).__name__ or isinstance(e, TimeoutError):
                rec["error"] = "navigation timeout"
            else:
                rec["error"] = f"{type(e).__name__}: {e}"
            return rec
    try:
        rec["sorry_redirect"] = "/sorry" in page.url
        if rec["sorry_redirect"]:
            rec["error"] = "Google /sorry anti-bot wall after retries — caller should fall back to Apify SERP actor"
            return rec
        body = page.inner_text("body")
        if "people also ask" not in body.lower():
            rec["error"] = "PAA section not present in SERP for this query"
            return rec
        rec["rendered"] = True
        rec["selector_observed"] = PAA_SELECTOR_HINT
        questions = page.eval_on_selector_all(
            "div[role='button'], div[jsname]",
            """els => {
                const seen = new Set();
                const out = [];
                for (const e of els) {
                    const t = (e.innerText || '').trim();
                    if (t && t.length < 120 && t.endsWith('?') && !t.includes('\\n') && !seen.has(t)) {
                        seen.add(t); out.push(t);
                    }
                }
                return out.slice(0, 12);
            }""",
        )
        rec["questions"] = questions
    except Exception as e:  # pragma: no cover
        rec["error"] = f"{type(e).__name__}: {e}"
    return rec


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("queries", nargs="*", help="search queries to extract PAA for")
    ap.add_argument("--queries-file", help="newline-separated file of queries")
    ap.add_argument("--hl", default="en", help="Google hl param (language), default en")
    ap.add_argument("--gl", default="us", help="Google gl param (country), default us")
    ap.add_argument("--json", action="store_true", help="emit a JSON array (default: one JSON object per line)")
    ap.add_argument("--headless", action="store_true", help="run headless (default: headed — needed to pass Google anti-bot)")
    ap.add_argument(
        "--browser-only",
        action="store_true",
        help="use persistent real-Chrome Playwright directly instead of trying Apify first",
    )
    ap.add_argument(
        "--profile-dir",
        default=str(Path(__file__).resolve().parent.parent / ".playwright-profile"),
        help="persistent Chrome user-data dir (default: .playwright-profile).",
    )
    args = ap.parse_args()

    queries = list(args.queries)
    if args.queries_file:
        queries += [ln.strip() for ln in Path(args.queries_file).read_text(encoding="utf-8").splitlines() if ln.strip()]
    if not queries:
        ap.error("no queries provided")

    results: list[dict] = []
    if not args.browser_only:
        try:
            results = extract_via_apify(queries, args.hl, args.gl)
        except Exception as exc:
            print(f"Apify PAA primary route warning ({exc}); attempting real-Chrome complement...", file=sys.stderr)

    if not results or not any(r.get("questions") for r in results):
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            if results:
                pass
            else:
                print("playwright is not installed and Apify route returned no results", file=sys.stderr)
                return 2
        else:
            profile_dir = Path(args.profile_dir)
            profile_dir.mkdir(parents=True, exist_ok=True)
            results = []
            with sync_playwright() as p:
                ctx = p.chromium.launch_persistent_context(
                    str(profile_dir),
                    channel="chrome",
                    headless=args.headless,
                    user_agent=UA,
                    viewport={"width": 1280, "height": 1000},
                    locale=args.hl,
                    args=["--disable-blink-features=AutomationControlled", f"--lang={args.hl}"],
                )
                try:
                    page = ctx.new_page()
                    page.add_init_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")
                    for i, q in enumerate(queries):
                        results.append(extract_one(page, q, args.hl, args.gl))
                        if i < len(queries) - 1:
                            page.wait_for_timeout(5000)
                finally:
                    ctx.close()

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for r in results:
            print(json.dumps(r, ensure_ascii=False))
    # exit non-zero only if every query failed
    return 0 if any(r["questions"] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
