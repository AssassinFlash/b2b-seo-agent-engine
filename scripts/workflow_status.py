#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

PROFILE_COMMANDS = {"/profile-answer", "/article-cluster", "/profile-research-deep", "/profile-lock"}

PROGRESS_ORDER = [
    "Profile",
    "Cluster",
    "Intent Research",
    "Benchmark",
    "Extract",
    "Evidence",
    "Skeleton",
    "Arc",
    "Draft",
    "Truth QA",
    "Info Gain QA",
    "Benchmark QA",
    "Reader QA",
    "Repair",
    "Enrich",
    "Visual",
    "Resources",
    "FAQ",
    "Publish",
    "Review",
]

ARTICLE_STAGE_FILES = [
    ("Cluster", "/article-cluster", ["topic-card.md"]),
    ("Intent Research", "/article-intent-research", ["intent-research.md"]),
    ("Benchmark", "/article-benchmark", ["content-type-library.md", "benchmark-candidates.md"]),
    ("Extract", "/article-benchmark-extract", ["benchmark-success-formula.md", "benchmark-asset-ledger.md"]),
    ("Evidence", "/article-evidence-opinions", ["evidence-opinion-pack.md"]),
    ("Skeleton", "/article-skeleton", ["skeleton.md"]),
    ("Arc", "/article-arc", ["narrative-arc.md"]),
    ("Draft", "/article-draft", ["draft.md"]),
    ("Repair", "/article-repair", ["repair-plan.md"]),
    ("Enrich", "/article-enrich", ["enriched-draft.md", "image-plan.md"]),
    ("Visual", "/article-visual", ["visual-spec.md"]),
    ("Resources", "/article-resources", ["resources.md"]),
    ("FAQ", "/article-faq", ["faq.md"]),
    ("Publish", "/article-publish-pack", ["publish-package.md", "keyword-record.csv"]),
    ("Review", "/article-review", ["performance-review.md"]),
]

PROJECT_STAGE_FILES = [
    ("Cluster", "/article-cluster", ["topic-cluster.md"]),
]

QA_FILES = [
    ("Truth QA", "truth-qa.md", "/article-truth-qa"),
    ("Info Gain QA", "information-gain-qa.md", "/article-information-gain-qa"),
    ("Benchmark QA", "benchmark-drift-audit.md", "/article-benchmark-qa"),
    ("Reader QA", "reader-qa.md", "/article-reader-qa"),
]

QA_BLOCK_RE = re.compile(
    r"(?im)^\s*(?:status|result|gate)\s*:\s*(?:block|blocked|fail|failed)\b"
    r"|^\s*BLOCK\b"
    r"|^\s*\*\*Status\*\*\s*:\s*(?:block|blocked|fail|failed)\b"
)

FRONTMATTER_RE = re.compile(r"\A---[ \t]*\n(.*?)\n---[ \t]*(?:\n|\Z)", re.DOTALL)
FRONTMATTER_VERDICT_RE = re.compile(
    r"(?im)^[ \t]*verdict[ \t]*:[ \t]*[\"']?([A-Za-z]+)[\"']?[ \t]*$"
)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
EXPLICIT_STATUS_LINE_RE = re.compile(
    r"(?im)^[ \t]*(?:\*\*)?(?:status|verdict|result|gate|pass[ \t]*/[ \t]*block)(?:\*\*)?[ \t]*:[ \t]*([^\n]+)$"
)
STATUS_HEADING_RE = re.compile(r"(?m)^#{2,6}[ \t]+(?:Executive[ \t]+)?(?:Status|Verdict)\b[^\n]*\n")
ANY_HEADING_RE = re.compile(r"(?m)^#{1,6}[ \t]+")
SHOUTED_VERDICT_RE = re.compile(r"\b(PASS|PASSED|BLOCK|BLOCKED|FAIL|FAILED)\b")

STAGE_COMPANION_FILES: dict[str, list[str]] = {
    "article-benchmark-extract": ["benchmarks"],
    "article-evidence-opinions": [
        "evidence-handoff-summary.md",
        "knowledge-gap-register.md",
        "upstream-revision-suggestions.md",
    ],
    "article-skeleton": ["h2-heading-strategy.md"],
    "article-enrich": [
        "html-visual-plan.md",
        "html-visuals",
        "visual-asset-candidates.md",
        "visual-asset-candidates.json",
        "visual-fit-review.md",
        "visual-render-check.md",
    ],
    "article-visual": ["visual", "asset-upload-checklist.md"],
    "article-publish-pack": [
        "publish-ready-body.md",
        "preview-in-host-theme.html",
        "title-options.md",
        "schema.json",
        "keyword-record.csv",
        "wordpress-preview-check.md",
    ],
}


def load_json(path: Path) -> tuple[dict[str, Any], str | None]:
    if not path.exists():
        return {}, None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return {}, f"{path.name} is invalid JSON: {error.msg}"
    if not isinstance(data, dict):
        return {}, f"{path.name} must contain a JSON object"
    return data, None


def save_state_atomic(state: dict[str, Any], path: Path) -> None:
    import tempfile
    import os
    path = Path(path)
    dir_name = path.parent
    with tempfile.NamedTemporaryFile("w", dir=str(dir_name), delete=False, encoding="utf-8", suffix=".tmp") as f:
        json.dump(state, f, indent=2)
        temp_name = f.name
    try:
        os.replace(temp_name, str(path))
    except Exception as e:
        if os.path.exists(temp_name):
            os.unlink(temp_name)
        raise e


def _check_json_type(val: Any, expected_type: str) -> bool:
    if expected_type == "string":
        return isinstance(val, str)
    if expected_type == "boolean":
        return isinstance(val, bool)
    if expected_type == "integer":
        return isinstance(val, int) and not isinstance(val, bool)
    if expected_type == "number":
        return isinstance(val, (int, float)) and not isinstance(val, bool)
    if expected_type == "array":
        return isinstance(val, list)
    if expected_type == "object":
        return isinstance(val, dict)
    if expected_type == "null":
        return val is None
    return True


def _validate_schema_node(instance: Any, schema: dict[str, Any], path: str = "$") -> str | None:
    """Zero-dependency recursive JSON Schema validator supporting required, additionalProperties, type, enum, pattern, oneOf, anyOf, items, and properties."""
    if "oneOf" in schema:
        if not any(_validate_schema_node(instance, sub, path) is None for sub in schema["oneOf"]):
            return f"{path}: value {instance!r} does not match any allowed oneOf schema"
    if "anyOf" in schema:
        if not any(_validate_schema_node(instance, sub, path) is None for sub in schema["anyOf"]):
            return f"{path}: value {instance!r} does not match any allowed anyOf schema"

    expected_type = schema.get("type")
    if isinstance(expected_type, str):
        if not _check_json_type(instance, expected_type):
            return f"{path}: expected type '{expected_type}', got {type(instance).__name__}"
    elif isinstance(expected_type, list):
        if not any(_check_json_type(instance, t) for t in expected_type):
            return f"{path}: expected one of types {expected_type}, got {type(instance).__name__}"

    if "enum" in schema and instance not in schema["enum"]:
        return f"{path}: value {instance!r} is not in allowed enum {schema['enum']}"

    if isinstance(instance, str) and "pattern" in schema:
        if not re.search(schema["pattern"], instance):
            return f"{path}: string {instance!r} does not match pattern {schema['pattern']!r}"

    if isinstance(instance, dict):
        for req in schema.get("required", []):
            if req not in instance:
                return f"{path}: missing required field '{req}'"
        props = schema.get("properties", {})
        add_props = schema.get("additionalProperties", True)
        for k, v in instance.items():
            if k in props:
                err = _validate_schema_node(v, props[k], f"{path}.{k}")
                if err:
                    return err
            elif add_props is False:
                return f"{path}: additional property '{k}' is not allowed"
            elif isinstance(add_props, dict):
                err = _validate_schema_node(v, add_props, f"{path}.{k}")
                if err:
                    return err

    if isinstance(instance, list) and "items" in schema and isinstance(schema["items"], dict):
        for idx, item in enumerate(instance):
            err = _validate_schema_node(item, schema["items"], f"{path}[{idx}]")
            if err:
                return err

    return None


def validate_state(state: dict[str, Any], schema_path: Path) -> str | None:
    if not schema_path.exists():
        return f"Schema file not found at {schema_path}"
    try:
        with open(schema_path, "r", encoding="utf-8") as f:
            schema = json.load(f)
    except Exception as e:
        return f"Failed to load schema JSON: {e}"

    try:
        import jsonschema
        jsonschema.validate(instance=state, schema=schema)
    except ImportError:
        return _validate_schema_node(state, schema)
    except Exception as e:
        return str(e)
    return None


STAGE_TO_ARTICLE_STATUS: dict[str, str] = {
    "profile-discover": "idea",
    "profile-answer": "idea",
    "article-cluster": "topic-card",
    "profile-research-deep": "topic-card",
    "profile-lock": "topic-card",
    "article-intent-research": "intent-research",
    "article-benchmark": "benchmarking",
    "article-benchmark-extract": "benchmarking",
    "article-evidence-opinions": "benchmarking",
    "article-skeleton": "drafting",
    "article-arc": "drafting",
    "article-draft": "drafting",
    "article-truth-qa": "qa",
    "article-information-gain-qa": "qa",
    "article-benchmark-qa": "qa",
    "article-reader-qa": "qa",
    "article-repair": "qa",
    "article-enrich": "enriching",
    "article-visual": "visual",
    "article-resources": "resources",
    "article-faq": "faq",
    "article-publish-pack": "handoff-draft",
    "article-review": "published",
}


def sync_active_article_entry(state: dict[str, Any], stage_name: str, now_iso: str) -> None:
    """Keep state['articles'][i] synchronized with top-level currentStage transitions."""
    active_slug = state.get("activeArticle")
    articles = state.get("articles")
    if not active_slug or not isinstance(articles, list):
        return
    mapped_status = STAGE_TO_ARTICLE_STATUS.get(stage_name)
    for item in articles:
        if isinstance(item, dict) and item.get("slug") == active_slug:
            item["currentStage"] = stage_name
            item["lastUpdated"] = now_iso
            if mapped_status:
                item["status"] = mapped_status
            break
def workspace_dir(root: Path) -> Path:
    return root / "content-workspace"


def project_dirs(root: Path) -> list[Path]:
    workspace = workspace_dir(root)
    if not workspace.exists():
        return []
    return sorted([path for path in workspace.iterdir() if path.is_dir() and not path.name.startswith(".")])


def resolve_project(project_arg: str | None, root: Path) -> tuple[Path | None, list[str], list[str]]:
    issues: list[str] = []
    candidates: list[str] = []

    if project_arg:
        project_path = Path(project_arg)
        if not project_path.is_absolute():
            project_path = root / project_path
        if not project_path.exists():
            issues.append(f"Project workspace not found: {project_arg}")
        return project_path, candidates, issues

    projects = project_dirs(root)
    if not projects:
        issues.append("No project workspace found")
        return None, candidates, issues
    if len(projects) > 1:
        candidates = [path.name for path in projects]
        issues.append("Multiple project workspaces found; rerun with one project path")
        return None, candidates, issues
    return projects[0], candidates, issues


def command_project_path(project_path: Path, root: Path) -> str:
    try:
        return str(project_path.relative_to(root))
    except ValueError:
        return str(project_path)


def append_project(command: str, project_path: Path, root: Path) -> str:
    return f"{command} {command_project_path(project_path, root)}"


def append_article(command: str, project_path: Path, root: Path, article_slug: str) -> str:
    return f"{append_project(command, project_path, root)} {article_slug}"


def stage_status(base: Path, required_files: list[str]) -> tuple[str, list[str]]:
    present = [name for name in required_files if (base / name).exists()]
    missing = [name for name in required_files if name not in present]
    if not present:
        return "todo", missing
    if missing:
        return "partial", missing
    return "done", []


def _classify_qa_token(token: str) -> str:
    upper = token.upper()
    if upper in {"PASS", "PASSED"}:
        return "PASS"
    if upper in {"BLOCK", "BLOCKED", "FAIL", "FAILED"}:
        return "BLOCK"
    return "UNKNOWN"


def read_qa_verdict(path: Path) -> str:
    """Return PASS, BLOCK, or UNKNOWN using the same rules as validate_publish.py."""
    if not path.exists():
        return "UNKNOWN"
    text = path.read_text(encoding="utf-8", errors="replace")
    fm = FRONTMATTER_RE.match(text)
    if fm:
        v = FRONTMATTER_VERDICT_RE.search(fm.group(1))
        if v:
            return _classify_qa_token(v.group(1))
    body = HTML_COMMENT_RE.sub("", text)
    for match in EXPLICIT_STATUS_LINE_RE.finditer(body):
        raw_val = match.group(1).strip().strip("`*_ ")
        if not raw_val:
            return "UNKNOWN"
        tokens = {_classify_qa_token(t) for t in SHOUTED_VERDICT_RE.findall(raw_val.upper())}
        tokens.discard("UNKNOWN")
        if len(tokens) > 1 or "|" in raw_val:
            return "UNKNOWN"
        if len(tokens) == 1:
            return tokens.pop()
    heading = STATUS_HEADING_RE.search(body)
    if heading:
        section = body[heading.end():]
        nxt = ANY_HEADING_RE.search(section)
        if nxt:
            section = section[:nxt.start()]
        found = {_classify_qa_token(t) for t in SHOUTED_VERDICT_RE.findall(section)}
        found.discard("UNKNOWN")
        if len(found) == 1:
            return found.pop()
    if QA_BLOCK_RE.search(body):
        return "BLOCK"
    return "UNKNOWN"


def qa_file_is_blocking(path: Path) -> bool:
    if not path.exists():
        return False
    verdict = read_qa_verdict(path)
    if verdict == "BLOCK":
        return True
    if verdict == "PASS":
        return False
    return bool(QA_BLOCK_RE.search(path.read_text(encoding="utf-8", errors="replace")))


def qa_status(article_path: Path) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for stage_name, file_name, command in QA_FILES:
        path = article_path / file_name
        if not path.exists():
            result[stage_name] = {"status": "todo", "file": file_name, "command": command, "blocking": False}
            continue
        verdict = read_qa_verdict(path)
        if verdict == "BLOCK" or qa_file_is_blocking(path):
            result[stage_name] = {"status": "blocked", "file": file_name, "command": command, "blocking": True}
        elif verdict == "UNKNOWN":
            # Unfilled template placeholder like `PASS | PASS with watchlist | BLOCK`, `Status: TBD`, or empty file
            text = path.read_text(encoding="utf-8", errors="replace")
            if (
                not text.strip()
                or "PASS |" in text
                or "| BLOCK" in text
                or re.search(r"\b(?:TBD|TODO|PENDING)\b", text)
                or EXPLICIT_STATUS_LINE_RE.search(text)
            ):
                result[stage_name] = {"status": "todo", "file": file_name, "command": command, "blocking": False}
            else:
                result[stage_name] = {"status": "done", "file": file_name, "command": command, "blocking": False}
        else:
            result[stage_name] = {"status": "done", "file": file_name, "command": command, "blocking": False}
    return result


def profile_status(project_path: Path, state: dict[str, Any]) -> str:
    if state.get("lockedProfile") is True and (project_path / "project-profile.md").exists() and (
        project_path / "project-profile.json"
    ).exists():
        return "done"
    if state or (project_path / "project-profile.draft.md").exists() or (project_path / "project-profile.research.md").exists():
        return "partial"
    return "todo"


def profile_is_locked(project_path: Path, state: dict[str, Any]) -> bool:
    return bool(
        state.get("lockedProfile") is True
        and (project_path / "project-profile.md").exists()
        and (project_path / "project-profile.json").exists()
        and (project_path / "state.json").exists()
    )


def choose_profile_command(project_path: Path, root: Path, state: dict[str, Any]) -> dict[str, str]:
    next_from_state = str(state.get("nextCommand") or "").strip()
    if next_from_state in PROFILE_COMMANDS:
        command = next_from_state
    elif state.get("profileStatus") == "researched" or (project_path / "project-profile.research.md").exists():
        command = "/profile-lock"
    elif any((article / "topic-card.md").exists() for article in article_dirs(project_path)):
        command = "/profile-research-deep"
    elif (project_path / "project-profile.draft.md").exists() or state.get("profileStatus") == "draft":
        command = "/profile-answer"
    else:
        return {
            "command": "/profile-discover",
            "reason": "No usable draft profile exists yet.",
        }
    return {
        "command": append_project(command, project_path, root),
        "reason": "Profile is not locked, so article commands must stay blocked.",
    }


def article_dirs(project_path: Path) -> list[Path]:
    articles_path = project_path / "articles"
    if not articles_path.exists():
        return []
    return sorted([path for path in articles_path.iterdir() if path.is_dir() and not path.name.startswith(".")])


def project_progress(project_path: Path, project_locked: bool) -> dict[str, str]:
    progress = {stage: "todo" for stage in PROGRESS_ORDER}
    progress["Profile"] = "done" if project_locked else "partial"
    for stage_name, _command, required_files in PROJECT_STAGE_FILES:
        progress[stage_name], _missing = stage_status(project_path, required_files)
    return progress


def repair_is_needed(article_path: Path, qa_results: dict[str, dict[str, Any]] | None = None) -> bool:
    if qa_results is None:
        qa_results = qa_status(article_path)
    return any(info["blocking"] for info in qa_results.values()) or (article_path / "repair-plan.md").exists()


def article_progress(article_path: Path, project_progress_state: dict[str, str]) -> dict[str, str]:
    progress = dict(project_progress_state)
    qa_results = qa_status(article_path)

    # Legacy safety mirror of next_for_article: pre-skeleton intent/benchmark
    # stages are not required for articles that already have a skeleton.
    legacy_skip_stages = {"Intent Research", "Benchmark"}
    is_legacy_article = (
        (article_path / "skeleton.md").exists()
        and not (article_path / "intent-research.md").exists()
    )

    for stage_name, _command, required_files in ARTICLE_STAGE_FILES:
        if stage_name == "Repair":
            # Repair is only required when a QA gate is blocking or a repair plan exists.
            if repair_is_needed(article_path, qa_results):
                progress[stage_name], _missing = stage_status(article_path, required_files)
            else:
                progress[stage_name] = "done"
            continue
        if is_legacy_article and stage_name in legacy_skip_stages:
            progress[stage_name] = "done"
            continue
        progress[stage_name], _missing = stage_status(article_path, required_files)

    for stage_name, info in qa_results.items():
        progress[stage_name] = info["status"]
    return progress


def progress_percent(progress: dict[str, str]) -> int:
    done = sum(1 for value in progress.values() if value == "done")
    return round(done / len(PROGRESS_ORDER) * 100)


def next_for_article(project_path: Path, article_slug: str, root: Path) -> tuple[dict[str, str], list[str]]:
    article_path = project_path / "articles" / article_slug
    issues: list[str] = []

    if not article_path.exists():
        issues.append(f"Article workspace missing: articles/{article_slug}")
        return {
            "command": append_project("/article-cluster", project_path, root),
            "reason": "The selected article workspace does not exist yet.",
        }, issues

    # Legacy safety: articles started before the workflow reorder may have
    # skeleton.md (or later) without intent-research.md / content-type-library.md.
    # In that case, skip the pre-skeleton intent/benchmark gate so the operator
    # is not sent back to research a finished or nearly-finished article.
    legacy_skip_stages = {"Intent Research", "Benchmark"}
    is_legacy_article = (
        (article_path / "skeleton.md").exists()
        and not (article_path / "intent-research.md").exists()
    )

    # Stages before QA: Cluster through Draft
    for stage_name, command, required_files in ARTICLE_STAGE_FILES[:8]:
        if is_legacy_article and stage_name in legacy_skip_stages:
            continue
        status, missing = stage_status(article_path, required_files)
        if status != "done":
            issues.append(f"{stage_name} is incomplete; missing: {', '.join(missing)}")
            return {
                "command": append_article(command, project_path, root, article_slug),
                "reason": f"{stage_name} artifacts must exist before later stages are safe.",
            }, issues

    # QA gates — each tracked independently
    qa_results = qa_status(article_path)
    blocked = [(name, info) for name, info in qa_results.items() if info["blocking"]]
    missing_qa = [(name, info) for name, info in qa_results.items() if info["status"] == "todo"]

    if blocked:
        name, info = blocked[0]
        issues.append(f"{info['file']} is blocking; repair the article or evidence before continuing.")
        return {
            "command": append_article("/article-repair", project_path, root, article_slug),
            "reason": f"{name} is blocking publish progression; diagnose and repair.",
        }, issues

    if missing_qa:
        name, info = missing_qa[0]
        missing_names = [n for n, i in missing_qa]
        issues.append(f"QA is incomplete; missing: {', '.join(missing_names)}")
        return {
            "command": append_article(info["command"], project_path, root, article_slug),
            "reason": f"{name} is the next QA gate before enrichment or publishing.",
        }, issues

    # Post-QA stages: Repair (optional), Enrich, Publish, Review
    for stage_name, command, required_files in ARTICLE_STAGE_FILES[8:]:
        if stage_name == "Repair" and not repair_is_needed(article_path, qa_results):
            continue
        status, missing = stage_status(article_path, required_files)
        if status != "done":
            issues.append(f"{stage_name} is incomplete; missing: {', '.join(missing)}")
            return {
                "command": append_article(command, project_path, root, article_slug),
                "reason": f"{stage_name} artifacts are the next required layer.",
            }, issues

    return {
        "command": append_project("/article-next", project_path, root),
        "reason": "This article has all expected publish artifacts; use article-next to choose the next article or review step.",
    }, issues


def build_article_queue(project_path: Path, root: Path, project_locked: bool) -> list[dict[str, Any]]:
    queue = []
    proj_progress = project_progress(project_path, project_locked)
    for article_path in article_dirs(project_path):
        progress = article_progress(article_path, proj_progress)
        next_command, _issues = next_for_article(project_path, article_path.name, root)
        queue.append(
            {
                "article": article_path.name,
                "progress": progress_percent(progress),
                "next": next_command["command"],
            }
        )
    return queue


def select_article(project_path: Path, article_slug: str | None, state: dict[str, Any]) -> str | None:
    if article_slug:
        return article_slug
    active_article = state.get("activeArticle")
    if isinstance(active_article, str) and active_article.strip():
        return active_article.strip()
    return None


def build_status(project_arg: str | None = None, article_slug: str | None = None, root: Path = ROOT) -> dict[str, Any]:
    root = root.resolve()
    project_path, candidates, project_issues = resolve_project(project_arg, root)

    if project_path is None:
        next_command = "/profile-discover"
        reason = "Start discovery before there is any project workspace."
        if candidates:
            next_command = "/workflow-status content-workspace/<project-slug>"
            reason = "Multiple project workspaces exist, so the status cockpit needs a specific project."
        return {
            "mode": "project-selection" if candidates else "empty-workspace",
            "projectSlug": None,
            "profileStatus": "missing",
            "lockedProfile": False,
            "activeArticle": None,
            "selectedArticle": None,
            "lastUpdated": None,
            "projectCandidates": candidates,
            "progress": {stage: "todo" for stage in PROGRESS_ORDER},
            "progressPercent": 0,
            "blockingIssues": project_issues,
            "nextSafeCommand": {"command": next_command, "reason": reason},
            "ignoreForNow": ["Article artifacts can wait until a project profile exists."],
            "articleQueue": [],
        }

    state, state_issue = load_json(project_path / "state.json")
    issues = list(project_issues)
    if state_issue:
        issues.append(state_issue)

    slug = str(state.get("projectSlug") or project_path.name)
    locked = profile_is_locked(project_path, state)
    selected_article = select_article(project_path, article_slug, state)
    progress = {stage: "todo" for stage in PROGRESS_ORDER}
    progress["Profile"] = profile_status(project_path, state)

    if not locked:
        issues.append("Profile is not locked")
        next_safe = choose_profile_command(project_path, root, state)
        queue = build_article_queue(project_path, root, locked)
        return {
            "mode": "project",
            "projectSlug": slug,
            "profileStatus": str(state.get("profileStatus") or "unknown"),
            "lockedProfile": False,
            "activeArticle": state.get("activeArticle"),
            "selectedArticle": selected_article,
            "lastUpdated": state.get("lastUpdated"),
            "projectCandidates": [],
            "progress": progress,
            "progressPercent": progress_percent(progress),
            "blockingIssues": issues,
            "nextSafeCommand": next_safe,
            "ignoreForNow": ["Article commands and publish artifacts can wait until the profile is locked."],
            "articleQueue": queue,
        }

    queue = build_article_queue(project_path, root, locked)
    proj_progress = project_progress(project_path, locked)
    progress = dict(proj_progress)

    if selected_article:
        progress = article_progress(project_path / "articles" / selected_article, proj_progress)
        next_safe, article_issues = next_for_article(project_path, selected_article, root)
        issues.extend(article_issues)
    elif not queue:
        issues.append("No article workspaces found")
        next_safe = {
            "command": append_project("/workflow-status", project_path, root),
            "reason": "The profile is locked, but no article workspace exists. Run /workflow-status to diagnose.",
        }
    else:
        next_safe = {
            "command": append_article("/workflow-status", project_path, root, queue[0]["article"]),
            "reason": "Choose an article to inspect its stage-level blockers.",
        }

    return {
        "mode": "article" if selected_article else "project",
        "projectSlug": slug,
        "profileStatus": str(state.get("profileStatus") or "locked"),
        "lockedProfile": True,
        "activeArticle": state.get("activeArticle"),
        "selectedArticle": selected_article,
        "lastUpdated": state.get("lastUpdated"),
        "projectCandidates": [],
        "progress": progress,
        "progressPercent": progress_percent(progress),
        "blockingIssues": issues,
        "nextSafeCommand": next_safe,
        "ignoreForNow": ignore_for_now(progress),
        "articleQueue": queue,
    }


def ignore_for_now(progress: dict[str, str]) -> list[str]:
    if progress.get("Profile") != "done":
        return ["Article artifacts can wait until project-profile.md and project-profile.json are locked."]
    ignored = [stage for stage in PROGRESS_ORDER if progress.get(stage) == "todo"]
    if not ignored:
        return ["Nothing obvious to ignore; this article has all expected publish artifacts."]
    return [f"Do not worry about later stages yet: {', '.join(ignored[:5])}."]


def progress_line(progress: dict[str, str]) -> str:
    return " -> ".join(f"{stage}[{progress.get(stage, 'todo')}]" for stage in PROGRESS_ORDER)


def render_markdown(status: dict[str, Any]) -> str:
    issues = status.get("blockingIssues") or ["No blocking issues detected."]
    queue = status.get("articleQueue") or []
    ignore = status.get("ignoreForNow") or ["No ignore guidance available."]
    next_safe = status.get("nextSafeCommand", {})

    lines = [
        "# Workflow Status Cockpit",
        "",
        "## Current Position",
        f"- Project: {status.get('projectSlug') or 'none'}",
        f"- Profile status: {status.get('profileStatus')}",
        f"- Locked profile: {str(status.get('lockedProfile')).lower()}",
        f"- Active article: {status.get('activeArticle') or 'none'}",
        f"- Selected article: {status.get('selectedArticle') or 'none'}",
        f"- Last updated: {status.get('lastUpdated') or 'unknown'}",
        "",
        "## Progress Bar",
        f"- Overall: {status.get('progressPercent', 0)}%",
        f"- {progress_line(status.get('progress', {}))}",
        "",
        "## Blocking Issues",
    ]
    lines.extend(f"- {issue}" for issue in issues)
    lines.extend(
        [
            "",
            "## Next Safe Command",
            "```text",
            str(next_safe.get("command") or "none"),
            "```",
            f"Reason: {next_safe.get('reason') or 'No reason available.'}",
            "",
            "## What You Can Ignore For Now",
        ]
    )
    lines.extend(f"- {item}" for item in ignore)
    lines.extend(["", "## Article Queue"])
    if queue:
        lines.extend(["| Article | Progress | Next |", "| --- | ---: | --- |"])
        for item in queue:
            lines.append(f"| {item['article']} | {item['progress']}% | `{item['next']}` |")
    else:
        lines.append("- No article queue yet.")
    return "\n".join(lines) + "\n"




def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render a read-only workflow status cockpit.")
    parser.add_argument("project_path", nargs="?", help="Project workspace path such as content-workspace/<project-slug>.")
    parser.add_argument("article_slug", nargs="?", help="Optional article slug.")
    parser.add_argument("--json", action="store_true", dest="json_output", help="Output machine-readable JSON.")
    parser.add_argument("--next", action="store_true", dest="next_mutation", help="Advance state to the next stage.")
    parser.add_argument("--rollback", dest="rollback_stage", help="Rollback to a specified stage name.")
    parser.add_argument("--root", default=str(ROOT), help=argparse.SUPPRESS)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    root_path = Path(args.root)
    
    project_path, candidates, project_issues = resolve_project(args.project_path, root_path)
    
    if project_path is None:
        if args.next_mutation or args.rollback_stage:
            print("Error: No project workspace found or multiple candidates found. Specify project path.", file=sys.stderr)
            return 2
        status = build_status(args.project_path, args.article_slug, root_path)
        if args.json_output:
            print(json.dumps(status, ensure_ascii=False, indent=2))
        else:
            print(render_markdown(status), end="")
        return 0
        
    state_path = project_path / "state.json"
    if not state_path.exists():
        if args.next_mutation or args.rollback_stage:
            print("Error: state.json does not exist. Run /profile-discover first.", file=sys.stderr)
            return 2
    else:
        state, state_issue = load_json(state_path)
        if state_issue:
            print(f"Error loading state.json: {state_issue}", file=sys.stderr)
            return 2
        schema_path = root_path / "config" / "state-schema.json"
        val_error = validate_state(state, schema_path)
        if val_error:
            print(f"Error: state.json failed schema validation: {val_error}", file=sys.stderr)
            return 2

    stages_list = [
        "profile-discover", "profile-answer", "article-cluster", "profile-research-deep", "profile-lock",
        "article-intent-research",
        "article-benchmark", "article-benchmark-extract", "article-evidence-opinions",
        "article-skeleton", "article-arc", "article-draft", "article-truth-qa",
        "article-information-gain-qa", "article-benchmark-qa", "article-reader-qa", "article-enrich",
        "article-visual", "article-resources", "article-faq",
        "article-publish-pack", "article-review"
    ]

    # Handle rollback mutation
    if args.rollback_stage:
        target_stage = args.rollback_stage
        matched_stage = None
        label_to_stage = {
            name.lower(): cmd.lstrip("/")
            for name, cmd, _ in ARTICLE_STAGE_FILES + PROJECT_STAGE_FILES
        }
        label_to_stage.update({name.lower(): cmd.lstrip("/") for name, _, cmd in QA_FILES})
        if target_stage.lower() in label_to_stage:
            matched_stage = label_to_stage[target_stage.lower()]
        else:
            for s in stages_list:
                s_clean = s[8:] if s.startswith("article-") else s
                t_clean = target_stage[8:] if target_stage.startswith("article-") else target_stage
                if s.lower() == target_stage.lower() or s_clean.lower() == t_clean.lower():
                    matched_stage = s
                    break
        if not matched_stage:
            print(f"Error: Unknown stage '{target_stage}'. Valid stages: {stages_list}", file=sys.stderr)
            return 2

        idx = stages_list.index(matched_stage)
        current_stage_val = state.get("currentStage")
        if current_stage_val in stages_list:
            current_idx = stages_list.index(current_stage_val)
            if idx > current_idx:
                print(
                    f"Error: Cannot roll forward from '{current_stage_val}' to '{matched_stage}'. Use --next instead.",
                    file=sys.stderr,
                )
                return 2

        state["currentStage"] = matched_stage
        if idx + 1 < len(stages_list):
            state["nextCommand"] = "/" + stages_list[idx + 1]
        else:
            state["nextCommand"] = "/article-next"

        # Update lockedProfile and profileStatus based on target index (lock happens at profile-lock, index 4)
        if idx < 4:
            state["lockedProfile"] = False
            state["profileStatus"] = "draft" if idx < 3 else "researched"
            files_to_remove = ["project-profile.md", "project-profile.json"]
            if idx < 3:
                files_to_remove.append("project-profile.research.md")
            for f in files_to_remove:
                file_path = project_path / f
                if file_path.exists():
                    import subprocess
                    subprocess.run(["rm", "-f", str(file_path)])
        else:
            state["lockedProfile"] = True
            state["profileStatus"] = "locked"

        import datetime
        now_iso = datetime.datetime.now().isoformat()
        state["lastUpdated"] = now_iso
        sync_active_article_entry(state, matched_stage, now_iso)

        # Cleanup downstream files
        article_slug = state.get("activeArticle")
        if article_slug:
            article_dir = project_path / "articles" / article_slug
            if article_dir.exists():
                import subprocess
                stages_after = set(stages_list[idx + 1:])

                # Check for stage files and companion files to remove
                for _name, command, required_files in ARTICLE_STAGE_FILES:
                    canonical_name = command.lstrip("/")
                    if canonical_name in stages_after or (canonical_name == "article-repair" and "article-truth-qa" in stages_after):
                        extra_files = STAGE_COMPANION_FILES.get(canonical_name, [])
                        for f in list(required_files) + extra_files:
                            file_path = article_dir / f
                            if file_path.exists():
                                subprocess.run(["rm", "-rf", str(file_path)])

                # Check for QA files to remove
                for _name, file_name, command in QA_FILES:
                    canonical_name = command.lstrip("/")
                    if canonical_name in stages_after:
                        file_path = article_dir / file_name
                        if file_path.exists():
                            subprocess.run(["rm", "-f", str(file_path)])

                if "article-draft" in stages_after:
                    retro_path = project_path / "memory" / f"draft-retrospective-{article_slug}.md"
                    if retro_path.exists():
                        subprocess.run(["rm", "-f", str(retro_path)])

        # Clean up project-level stage files
        stages_after = set(stages_list[idx + 1:])
        for _name, command, required_files in PROJECT_STAGE_FILES:
            canonical_name = command.lstrip("/")
            if canonical_name in stages_after:
                for f in required_files:
                    file_path = project_path / f
                    if file_path.exists():
                        import subprocess
                        subprocess.run(["rm", "-f", str(file_path)])
                                    
        save_state_atomic(state, state_path)
        print(f"Successfully rolled back to '{matched_stage}' and cleaned downstream artifacts.")
        return 0

    # Handle next mutation
    if args.next_mutation:
        current_stage = state.get("currentStage")
        if current_stage not in stages_list:
            print(f"Error: Current stage '{current_stage}' not in stages list.", file=sys.stderr)
            return 2

        idx = stages_list.index(current_stage)
        required_stages_so_far = set(stages_list[: idx + 1])

        status_info = build_status(args.project_path, args.article_slug, root_path)
        next_safe = status_info.get("nextSafeCommand", {})
        next_cmd = next_safe.get("command", "")

        if "/article-repair" in next_cmd:
            state["nextCommand"] = "/article-repair"
            import datetime
            state["lastUpdated"] = datetime.datetime.now().isoformat()
            save_state_atomic(state, state_path)
            print("Workflow is blocked by QA issues. Locked in /article-repair.")
            return 0

        # Check missing artifacts only for stages up to and including current_stage
        missing_so_far: list[str] = []
        article_slug_val = select_article(project_path, args.article_slug, state)
        article_dir = project_path / "articles" / article_slug_val if article_slug_val else None

        # Profile-level stage artifact checks
        if ("profile-discover" in required_stages_so_far or "profile-answer" in required_stages_so_far) and "profile-lock" not in required_stages_so_far:
            if not (project_path / "project-profile.draft.md").exists() and not (project_path / "project-profile.md").exists():
                missing_so_far.append("Discover/Answer is incomplete; missing: project-profile.draft.md")
        if "profile-research-deep" in required_stages_so_far and "profile-lock" not in required_stages_so_far:
            if not (project_path / "project-profile.research.md").exists() and not (project_path / "project-profile.md").exists():
                missing_so_far.append("Research Deep is incomplete; missing: project-profile.research.md")
        if "profile-lock" in required_stages_so_far:
            st_lock, miss_lock = stage_status(project_path, ["project-profile.md", "project-profile.json"])
            if st_lock != "done":
                missing_so_far.append(f"Profile Lock is incomplete; missing: {', '.join(miss_lock)}")

        for label, command, req_files in PROJECT_STAGE_FILES:
            if command.lstrip("/") in required_stages_so_far:
                st, miss = stage_status(project_path, req_files)
                if st != "done":
                    missing_so_far.append(f"{label} is incomplete; missing: {', '.join(miss)}")

        if idx >= 2 and (not article_dir or not article_dir.exists()):
            missing_so_far.append(
                f"Active article workspace is missing ({f'articles/{article_slug_val}' if article_slug_val else 'activeArticle not set'})"
            )
        elif article_dir and article_dir.exists():
            is_legacy = (article_dir / "skeleton.md").exists() and not (article_dir / "intent-research.md").exists()
            for label, command, req_files in ARTICLE_STAGE_FILES:
                c_name = command.lstrip("/")
                if c_name == "article-repair":
                    continue
                if is_legacy and label in {"Intent Research", "Benchmark"}:
                    continue
                if c_name in required_stages_so_far:
                    st, miss = stage_status(article_dir, req_files)
                    if st != "done":
                        missing_so_far.append(f"{label} is incomplete; missing: {', '.join(miss)}")
            qa_res = qa_status(article_dir)
            for label, file_name, command in QA_FILES:
                c_name = command.lstrip("/")
                if c_name in required_stages_so_far and qa_res.get(label, {}).get("status") != "done":
                    missing_so_far.append(f"{label} is incomplete or unfilled; missing/unfilled: {file_name}")

        if missing_so_far:
            print(f"Workflow is blocked by missing artifacts: {missing_so_far}", file=sys.stderr)
            return 2

        if idx + 1 < len(stages_list):
            next_stage = stages_list[idx + 1]
            state["currentStage"] = next_stage
            next_idx = stages_list.index(next_stage)
            state["lockedProfile"] = (next_idx >= 4)
            state["profileStatus"] = "draft" if next_idx < 3 else ("researched" if next_idx == 3 else "locked")
            if idx + 2 < len(stages_list):
                state["nextCommand"] = "/" + stages_list[idx + 2]
            else:
                state["nextCommand"] = "/article-next"

            import datetime
            now_iso = datetime.datetime.now().isoformat()
            state["lastUpdated"] = now_iso
            sync_active_article_entry(state, next_stage, now_iso)
            save_state_atomic(state, state_path)
            print(f"Successfully transitioned to stage '{next_stage}'. Next command: {state['nextCommand']}")
            return 0
        else:
            print("Already at the final stage.", file=sys.stderr)
            return 2

    # Default: Output status cockpit
    status = build_status(args.project_path, args.article_slug, root_path)
    if args.json_output:
        print(json.dumps(status, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(status), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
