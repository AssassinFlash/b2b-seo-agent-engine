#!/usr/bin/env python3
"""Cross-machine environment bootstrapper, doctor, and credential manager.

Zero third-party imports required (100% Python stdlib) so this script always runs
on a freshly cloned machine even before PyYAML or Playwright are installed.

Capabilities:
  1. `doctor` (default): inspect Python version, PyYAML/Playwright availability,
     real Google Chrome binary, PreToolUse hook registration, script permissions,
     and persistent Apify token pool health.
  2. `--fix` / `--install-deps`: install missing Python packages (`pyyaml`, `pytest`),
     fix script `chmod +x` and `.env.apify.local` `0600` permissions.
  3. `--set-apify-tokens` / `--add-apify-token` / `--prune-dead-tokens`:
     persistently save or rotate Apify API tokens into BOTH `.env.apify.local`
     and `~/.config/b2b-seo-agent/apify.env` (`chmod 600`).
  4. `--set-key KEY=VALUE`: save optional fallback API keys (`TAVILY_API_KEY`,
     `FIRECRAWL_API_KEY`, `EXA_API_KEY`, `YOU_API_KEY`) to `~/.config/b2b-seo-agent/search.env`.
  5. `--init-workspace <project-slug>`: scaffold a fresh project workspace under
     `content-workspace/<project-slug>/` ready for `/profile-discover`.
"""

from __future__ import annotations

import argparse
from datetime import date
import importlib.util
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = Path.home() / ".config" / "b2b-seo-agent"
SEARCH_ENV_PATH = CONFIG_DIR / "search.env"

CHROME_CANDIDATES = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary",
    "/usr/bin/google-chrome",
    "/usr/bin/google-chrome-stable",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
)


def find_chrome_binary() -> str | None:
    for candidate in CHROME_CANDIDATES:
        if Path(candidate).exists():
            return candidate
    for binary in ("google-chrome", "google-chrome-stable", "chromium"):
        found = shutil.which(binary)
        if found:
            return found
    return None


def check_python_module(mod_name: str) -> bool:
    return importlib.util.find_spec(mod_name) is not None


def set_search_env_keys(pairs: list[str]) -> dict:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    existing: dict[str, str] = {}
    if SEARCH_ENV_PATH.exists():
        for line in SEARCH_ENV_PATH.read_text(encoding="utf-8", errors="replace").splitlines():
            s = line.strip()
            if s and not s.startswith("#") and "=" in s:
                k, v = s.split("=", 1)
                existing[k.strip()] = v.strip().strip("'\"")
    updated_keys: list[str] = []
    for item in pairs:
        if "=" not in item:
            raise ValueError(f"Expected KEY=VALUE format, got: {item!r}")
        k, v = item.split("=", 1)
        k_s = k.strip()
        v_s = v.strip().strip("'\"")
        if k_s:
            if v_s:
                existing[k_s] = v_s
            else:
                existing.pop(k_s, None)
            updated_keys.append(k_s)
    lines = [
        "# Optional Search & Scraper Fallback API Keys (0600 permissions)",
        "# Loaded by b2b-seo-agent-engine helper scripts when present.",
    ]
    for k, v in sorted(existing.items()):
        lines.append(f"{k}={v}")
    SEARCH_ENV_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    os.chmod(SEARCH_ENV_PATH, 0o600)
    return {"updated_keys": updated_keys, "path": str(SEARCH_ENV_PATH)}


def init_workspace(slug: str) -> dict:
    clean_slug = slug.strip().strip("/").split("/")[-1].lower()
    if not clean_slug or not all(c.isalnum() or c == "-" for c in clean_slug):
        raise ValueError(f"Invalid project slug {slug!r}; use lowercase kebab-case (e.g. 'my-b2b-site').")
    ws = ROOT / "content-workspace" / clean_slug
    (ws / "articles").mkdir(parents=True, exist_ok=True)
    (ws / "source-library").mkdir(parents=True, exist_ok=True)
    (ws / "knowledge").mkdir(parents=True, exist_ok=True)

    readme_path = ws / "source-library" / "README.md"
    if not readme_path.exists():
        readme_path.write_text(
            f"# Source Library — `{clean_slug}`\n\n"
            "Place raw product catalogs, engineering datasheets, factory QC checklists, "
            "and SEMrush/GSC exports in this directory before running `/profile-discover`.\n",
            encoding="utf-8",
        )

    fact_lib = ws / "knowledge" / "fact-library.json"
    if not fact_lib.exists():
        fact_lib.write_text(
            json.dumps({"projectSlug": clean_slug, "lastUpdated": str(date.today()), "claims": []}, indent=2) + "\n",
            encoding="utf-8",
        )

    link_graph = ws / "knowledge" / "site-link-graph.json"
    if not link_graph.exists():
        link_graph.write_text(
            json.dumps({"projectSlug": clean_slug, "lastUpdated": str(date.today()), "nodes": {}, "edges": []}, indent=2) + "\n",
            encoding="utf-8",
        )

    state_file = ws / "state.json"
    if not state_file.exists():
        state_file.write_text(
            json.dumps(
                {
                    "projectSlug": clean_slug,
                    "profileStatus": "draft",
                    "lockedProfile": False,
                    "currentStage": "profile-discover",
                    "nextCommand": "/profile-discover",
                    "activeArticle": None,
                    "articleQueue": [],
                    "lastUpdated": str(date.today()),
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

    return {
        "initialized_workspace": str(ws.relative_to(ROOT)),
        "state_file": str(state_file.relative_to(ROOT)),
        "next_command": f"/profile-discover content-workspace/{clean_slug}",
    }


def fix_permissions_and_deps(install_deps: bool = False) -> list[str]:
    actions: list[str] = []
    for script in (ROOT / "scripts").rglob("*.py"):
        try:
            mode = script.stat().st_mode
            if not (mode & 0o111):
                os.chmod(script, mode | 0o755)
                actions.append(f"chmod +x {script.relative_to(ROOT)}")
        except OSError:
            pass

    if install_deps:
        missing_pkgs = []
        if not check_python_module("yaml"):
            missing_pkgs.append("pyyaml")
        if not check_python_module("pytest"):
            missing_pkgs.append("pytest")
        if missing_pkgs:
            cmd = [sys.executable, "-m", "pip", "install", "--quiet", *missing_pkgs]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0:
                actions.append(f"Installed Python packages: {', '.join(missing_pkgs)}")
            else:
                actions.append(f"Failed to auto-install {missing_pkgs}: {res.stderr.strip()[:200]}")
    return actions


def run_doctor(verify_apify_live: bool = True) -> dict:
    sys.path.insert(0, str(ROOT / "scripts"))
    import apify_research  # noqa: E402

    tokens = apify_research.load_tokens(allow_empty=True)
    apify_slots = []
    if tokens and verify_apify_live:
        apify_slots = apify_research._verify_all_tokens(tokens)
    elif tokens:
        apify_slots = [
            {"slot": s, "masked_token": apify_research.mask_token(t), "configured": True}
            for s, t in tokens
        ]

    apify_ready = any(
        r.get("authenticated") and not r.get("quota_exhausted") for r in apify_slots
    ) if verify_apify_live else bool(tokens)

    settings_path = ROOT / ".claude" / "settings.json"
    hook_registered = False
    if settings_path.exists():
        try:
            settings_data = json.loads(settings_path.read_text(encoding="utf-8"))
            pre_hooks = (settings_data.get("hooks") or {}).get("PreToolUse") or []
            hook_registered = any("publish_gate.py" in json.dumps(h) for h in pre_hooks)
        except ValueError:
            hook_registered = False

    chrome_bin = find_chrome_binary()
    pyyaml_ok = check_python_module("yaml")
    playwright_ok = check_python_module("playwright")
    pytest_ok = check_python_module("pytest")

    next_actions: list[str] = []
    if not apify_ready:
        next_actions.append(
            "Configure Apify token(s): paste your `apify_api_...` key(s) in chat or run "
            "`python3 scripts/apify_research.py set-tokens <apify_api_...>`"
        )
    if not pyyaml_ok:
        next_actions.append(
            "Install PyYAML: run `python3 scripts/setup_env.py --fix` or `pip install pyyaml`"
        )
    if not chrome_bin:
        next_actions.append(
            "Optional (for live Google PAA DOM extraction & visual screenshots): install Google Chrome"
        )

    return {
        "ready": bool(apify_ready and pyyaml_ok and hook_registered),
        "platform": f"{platform.system()} {platform.release()} ({platform.machine()})",
        "python": sys.version.split()[0],
        "dependencies": {
            "pyyaml": pyyaml_ok,
            "pytest": pytest_ok,
            "playwright_python": playwright_ok,
            "real_chrome_binary": chrome_bin,
        },
        "security_hooks": {
            "pre_tool_use_publish_gate": hook_registered,
            "local_env_file_exists": apify_research.LOCAL_ENV_PATH.exists(),
            "global_env_file_exists": apify_research.GLOBAL_ENV_PATH.exists()
            or apify_research.LEGACY_GLOBAL_ENV_PATH.exists(),
        },
        "apify_token_pool": {
            "configured_count": len(tokens),
            "ready": apify_ready,
            "slots": apify_slots,
        },
        "recommended_actions": next_actions,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fix", action="store_true", help="Fix script permissions and install missing Python deps (pyyaml, pytest)")
    parser.add_argument("--no-network", action="store_true", help="Check local token presence without making live HTTP calls to Apify")
    parser.add_argument("--set-apify-tokens", nargs="+", metavar="TOKEN", help="Persistently set/overwrite the Apify token pool (0600)")
    parser.add_argument("--add-apify-token", nargs="+", metavar="TOKEN", help="Add/promote Apify token(s) into the persistent pool")
    parser.add_argument("--prune-dead-tokens", action="store_true", help="Remove invalid (401/403) or exhausted Apify tokens")
    parser.add_argument("--set-key", nargs="+", metavar="KEY=VALUE", help="Persist optional search API keys to ~/.config/b2b-seo-agent/search.env")
    parser.add_argument("--init-workspace", metavar="PROJECT_SLUG", help="Initialize a new project workspace under content-workspace/<slug>")
    args = parser.parse_args(argv)

    sys.path.insert(0, str(ROOT / "scripts"))
    import apify_research  # noqa: E402

    output: dict = {}
    if args.fix:
        output["fix_actions"] = fix_permissions_and_deps(install_deps=True)
    else:
        fix_permissions_and_deps(install_deps=False)

    if args.set_apify_tokens:
        output["apify_update"] = apify_research.write_persistent_tokens(args.set_apify_tokens, sync_global=True)

    if args.add_apify_token:
        existing = [tok for _, tok in apify_research.load_tokens(allow_empty=True)]
        combined = list(args.add_apify_token) + existing
        output["apify_update"] = apify_research.write_persistent_tokens(combined, sync_global=True)

    if args.prune_dead_tokens:
        existing = apify_research.load_tokens(allow_empty=True)
        alive = []
        pruned = []
        for slot, tok in existing:
            try:
                q = apify_research.check_slot_quota(tok)
                if q.get("quota_exhausted"):
                    pruned.append({"slot": slot, "masked_token": apify_research.mask_token(tok), "reason": "quota_exhausted"})
                else:
                    alive.append(tok)
            except apify_research.ApiError as exc:
                pruned.append({"slot": slot, "masked_token": apify_research.mask_token(tok), "reason": f"http_{exc.status}"})
        output["apify_pruned"] = pruned
        output["apify_update"] = apify_research.write_persistent_tokens(alive, sync_global=True)

    if args.set_key:
        output["search_keys_update"] = set_search_env_keys(args.set_key)

    if args.init_workspace:
        output["workspace_init"] = init_workspace(args.init_workspace)

    doctor_report = run_doctor(verify_apify_live=not args.no_network)
    output["doctor"] = doctor_report
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0 if doctor_report["ready"] else 1


if __name__ == "__main__":
    sys.exit(main())
