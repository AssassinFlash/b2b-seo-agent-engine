#!/usr/bin/env python3
"""Refuse to publish an article that has not completed upstream stages and 4-Gate QA.

Checks only structural step completion and model-authored QA gate verdicts (no
mechanical prose/keyword/length scoring). Exits non-zero when an article is not
publishable, and /article-publish-pack (plus the PreToolUse hook) blocks
writing final publish artifacts until blockers are resolved.

    python3 scripts/validate_publish.py content-workspace/<project-slug> <article-slug>
    python3 scripts/validate_publish.py content-workspace/<project-slug> <article-slug> --json

Exit codes:
    0   publishable
    1   blocked; every reason is printed
    2   the request itself was wrong (no such project or article)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(Path(__file__).resolve().parent))
from workflow_status import (  # noqa: E402
    ARTICLE_STAGE_FILES,
    PROJECT_STAGE_FILES,
    QA_FILES,
    load_json,
    profile_is_locked,
    validate_state,
)


VERDICT_PASS = "PASS"
VERDICT_BLOCK = "BLOCK"
VERDICT_UNKNOWN = "UNKNOWN"

PASSING_TOKENS = {"PASS", "PASSED"}
BLOCKING_TOKENS = {"BLOCK", "BLOCKED", "FAIL", "FAILED"}

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


@dataclass(frozen=True)
class Blocker:
    check: str
    detail: str
    fix: str


def _classify_token(token: str) -> str:
    upper = token.upper()
    if upper in PASSING_TOKENS:
        return VERDICT_PASS
    if upper in BLOCKING_TOKENS:
        return VERDICT_BLOCK
    return VERDICT_UNKNOWN


def _verdict_from_frontmatter(text: str) -> str | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    verdict = FRONTMATTER_VERDICT_RE.search(match.group(1))
    if not verdict:
        return None
    return _classify_token(verdict.group(1))


def _verdict_from_status_line(text: str) -> str | None:
    body = HTML_COMMENT_RE.sub("", text)
    for match in EXPLICIT_STATUS_LINE_RE.finditer(body):
        raw_val = match.group(1).strip().strip("`*_ ")
        if not raw_val:
            return VERDICT_UNKNOWN
        tokens = {_classify_token(t) for t in SHOUTED_VERDICT_RE.findall(raw_val.upper())}
        tokens.discard(VERDICT_UNKNOWN)
        if len(tokens) > 1 or "|" in raw_val:
            # Template placeholder like `PASS | PASS with watchlist | BLOCK`
            return VERDICT_UNKNOWN
        if len(tokens) == 1:
            return tokens.pop()
    return None


def _verdict_from_status_section(text: str) -> str:
    body = HTML_COMMENT_RE.sub("", text)
    heading = STATUS_HEADING_RE.search(body)
    if not heading:
        return VERDICT_UNKNOWN

    section = body[heading.end() :]
    next_heading = ANY_HEADING_RE.search(section)
    if next_heading:
        section = section[: next_heading.start()]

    found = {_classify_token(token) for token in SHOUTED_VERDICT_RE.findall(section)}
    found.discard(VERDICT_UNKNOWN)
    if len(found) != 1:
        return VERDICT_UNKNOWN
    return found.pop()


def read_gate_verdict(path: Path) -> str:
    """Return PASS, BLOCK, or UNKNOWN for a model-authored QA artifact."""
    text = path.read_text(encoding="utf-8", errors="replace")
    from_fm = _verdict_from_frontmatter(text)
    if from_fm is not None:
        return from_fm
    from_line = _verdict_from_status_line(text)
    if from_line is not None:
        return from_line
    return _verdict_from_status_section(text)


def check_profile_lock(project_path: Path, state: dict[str, Any]) -> list[Blocker]:
    if profile_is_locked(project_path, state):
        return []
    return [
        Blocker(
            check="profile-lock",
            detail="the project profile is not locked",
            fix="run /profile-lock; it is the only skill allowed to set lockedProfile: true",
        )
    ]


def check_upstream_artifacts(project_path: Path, article_path: Path) -> list[Blocker]:
    """Every publish-path stage before /article-publish-pack must have produced its outputs."""
    blockers: list[Blocker] = []

    for stage_label, command, required_files in PROJECT_STAGE_FILES:
        missing = [name for name in required_files if not (project_path / name).exists()]
        if missing:
            blockers.append(
                Blocker(
                    check=f"artifacts:{command.lstrip('/')}",
                    detail=f"{stage_label} never produced {', '.join(missing)}",
                    fix=f"run {command}",
                )
            )

    is_legacy_article = (
        (article_path / "skeleton.md").exists()
        and not (article_path / "intent-research.md").exists()
    )
    legacy_optional_stages = {"Intent Research", "Visual", "Resources", "FAQ"}

    for stage_label, command, required_files in ARTICLE_STAGE_FILES:
        if stage_label in {"Repair", "Publish", "Review"}:
            continue
        if is_legacy_article and stage_label in legacy_optional_stages:
            continue
        if is_legacy_article and stage_label == "Benchmark":
            required_files = ["benchmark-candidates.md"]

        missing = [name for name in required_files if not (article_path / name).exists()]
        if missing:
            blockers.append(
                Blocker(
                    check=f"artifacts:{command.lstrip('/')}",
                    detail=f"{stage_label} never produced {', '.join(missing)}",
                    fix=f"run {command}",
                )
            )

    return blockers


def check_gates(article_path: Path) -> list[Blocker]:
    blockers: list[Blocker] = []
    for gate_label, file_name, command in QA_FILES:
        gate_key = command.lstrip("/").replace("article-", "")
        path = article_path / file_name
        if not path.exists():
            blockers.append(
                Blocker(
                    check=f"gate:{gate_key}",
                    detail=f"{gate_label} never ran; {file_name} does not exist",
                    fix=f"run {command}",
                )
            )
            continue

        verdict = read_gate_verdict(path)
        if verdict == VERDICT_PASS:
            continue
        if verdict == VERDICT_BLOCK:
            blockers.append(
                Blocker(
                    check=f"gate:{gate_key}",
                    detail=f"{gate_label} records a BLOCK verdict in {file_name}",
                    fix=f"run /article-repair, then re-run {command}",
                )
            )
        else:
            blockers.append(
                Blocker(
                    check=f"gate:{gate_key}",
                    detail=f"{gate_label} records no readable PASS/BLOCK verdict in {file_name}",
                    fix=f"{file_name} must record `Status: PASS` or `verdict: PASS` (or `BLOCK`)",
                )
            )
    return blockers


def validate(project_arg: str, article_slug: str, root: Path = ROOT) -> tuple[int, list[Blocker]]:
    project_path = Path(project_arg)
    if not project_path.is_absolute():
        project_path = root / project_path

    if not project_path.exists():
        return 2, [Blocker("input", f"no such project workspace: {project_arg}", "check the path")]

    article_path = project_path / "articles" / article_slug
    if not article_path.exists():
        return 2, [Blocker("input", f"no such article: articles/{article_slug}", "check the slug")]

    blockers: list[Blocker] = []
    state_path = project_path / "state.json"
    state, load_err = load_json(state_path)
    if load_err:
        blockers.append(
            Blocker("state", load_err, "repair state.json against config/state-schema.json")
        )
    elif state:
        schema_path = root / "config" / "state-schema.json"
        if not schema_path.exists():
            schema_path = ROOT / "config" / "state-schema.json"
        schema_err = validate_state(state, schema_path)
        if schema_err:
            blockers.append(
                Blocker("state", schema_err, "repair state.json against config/state-schema.json")
            )

    blockers += check_profile_lock(project_path, state)
    blockers += check_upstream_artifacts(project_path, article_path)
    blockers += check_gates(article_path)
    blockers += check_csp_and_glossary(project_path, article_path)

    return (1 if blockers else 0), blockers


def _find_non_https_schema_urls(node: Any, path: str = "$") -> list[str]:
    bad: list[str] = []
    if isinstance(node, dict):
        for k, v in node.items():
            if k in {"url", "@id", "contentUrl", "image", "logo", "sameAs"} and isinstance(v, str):
                if not v.startswith("https://"):
                    bad.append(f"{path}.{k} must be an absolute https:// URL (got {v!r})")
            elif k == "sameAs" and isinstance(v, list):
                for idx, item in enumerate(v):
                    if isinstance(item, str) and not item.startswith("https://"):
                        bad.append(f"{path}.sameAs[{idx}] must be an absolute https:// URL (got {item!r})")
            else:
                bad.extend(_find_non_https_schema_urls(v, f"{path}.{k}"))
    elif isinstance(node, list):
        for idx, item in enumerate(node):
            bad.extend(_find_non_https_schema_urls(item, f"{path}[{idx}]"))
    return bad


def validate_article_schema_json(raw_text: str, source_name: str = "schema.json") -> list[str]:
    """Validate that an article's schema.json is valid JSON-LD with @context and @graph/@type and no unfilled placeholders."""
    errs: list[str] = []
    stripped = raw_text.strip()
    if stripped.startswith("```"):
        errs.append(f"{source_name} must be pure JSON, not wrapped in Markdown ```json code fences")
        return errs
    try:
        data = json.loads(stripped)
    except Exception as exc:
        errs.append(f"{source_name} is not valid JSON: {exc}")
        return errs
    if not isinstance(data, dict):
        errs.append(f"{source_name} root must be a JSON object")
        return errs
    ctx = str(data.get("@context") or "")
    if "schema.org" not in ctx:
        errs.append(f"{source_name} must declare \"@context\": \"https://schema.org\"")
    if "@graph" not in data and "@type" not in data:
        errs.append(f"{source_name} must contain \"@graph\" (array of entities) or \"@type\"")
    if isinstance(data.get("@graph"), list) and len(data["@graph"]) == 0:
        errs.append(f"{source_name} \"@graph\" cannot be empty")
    if re.search(r"(\{\{.*?\}\}|\bTBD\b|\bTODO\b)", stripped):
        errs.append(f"{source_name} contains unfilled placeholders (TBD / TODO / {{{{...}}}})")
    errs.extend(_find_non_https_schema_urls(data))
    return errs


def validate_keyword_record_csv(raw_text: str, source_name: str = "keyword-record.csv") -> list[str]:
    """Validate that keyword-record.csv contains a recognizable keyword/phrase column and at least 1 data row."""
    import csv
    import io

    errs: list[str] = []
    stripped = raw_text.strip()
    if len(stripped) <= 10:
        return errs
    try:
        reader = csv.DictReader(io.StringIO(stripped))
        fieldnames = reader.fieldnames or []
        has_kw_col = any(f and any(tok in f.lower() for tok in ("keyword", "phrase")) for f in fieldnames)
        if not has_kw_col:
            errs.append(f"{source_name} header {fieldnames} must include a 'Keyword' or 'Keyword / Phrase' column")
            return errs
        valid_rows = 0
        for row in reader:
            for k, v in row.items():
                if k and any(tok in k.lower() for tok in ("keyword", "phrase")) and v and v.strip():
                    valid_rows += 1
                    break
        if valid_rows == 0:
            errs.append(f"{source_name} contains 0 non-empty keyword rows")
    except Exception as exc:
        errs.append(f"{source_name} is not valid CSV: {exc}")
    return errs


def check_csp_and_glossary(project_path: Path, article_path: Path) -> list[Blocker]:
    """Enforce CSP Zero-JS / 68ch snippet rules, schema.json validity, and project-profile.json forbiddenTerms before publishing."""
    blockers: list[Blocker] = []
    try:
        from assemble_publish_draft import (
            FORBIDDEN_INLINE_JS_RE,
            HTML_MARKER_RE,
            check_unmerged_resources_and_faq,
            extract_balanced_b2b_modules,
            scan_external_image_hotlinks,
            scan_forbidden_terms,
            strip_control_metadata,
            validate_scoped_html_snippet,
        )
    except ImportError:
        return blockers

    enriched = article_path / "enriched-draft.md"
    if enriched.exists():
        body = strip_control_metadata(enriched.read_text(encoding="utf-8", errors="replace"))
        for v in scan_forbidden_terms(body, project_path):
            blockers.append(
                Blocker(
                    check="glossary:forbidden-term",
                    detail=v,
                    fix="replace forbidden terms in enriched-draft.md with canonical glossary terms from project-profile.json",
                )
            )
        for hotlink in scan_external_image_hotlinks(body, project_path):
            blockers.append(
                Blocker(
                    check="csp:external-image-hotlink",
                    detail=hotlink,
                    fix="upload external images to local WordPress media library (/wp-content/uploads/...) to comply with img-src 'self'",
                )
            )
        for merge_warn in check_unmerged_resources_and_faq(article_path, body):
            blockers.append(
                Blocker(
                    check="merge:resources-or-faq",
                    detail=merge_warn,
                    fix="merge the generated resources.md / faq.md modules into enriched-draft.md before packaging",
                )
            )
        no_code_fences = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
        if FORBIDDEN_INLINE_JS_RE.search(no_code_fences):
            blockers.append(
                Blocker(
                    check="csp:inline-js",
                    detail="enriched-draft.md contains <script>, inline event handlers (onclick/oninput...), or javascript: URIs",
                    fix="remove all inline JS/event handlers to comply with host CSP (`script-src 'self'`)",
                )
            )
        for _, _, mod_html in extract_balanced_b2b_modules(no_code_fences):
            if mod_html.lower().startswith("<div"):
                for err in validate_scoped_html_snippet(mod_html, "enriched-draft.md inline snippet"):
                    blockers.append(
                        Blocker(
                            check="csp:inline-html",
                            detail=err,
                            fix="remove <script>/onclick/external fonts or >2-col grids from inline .b2b-mod-* snippet",
                        )
                    )

        html_vis_dir = article_path / "html-visuals"
        for m in HTML_MARKER_RE.finditer(no_code_fences):
            vis_id = m.group(1)
            candidate = html_vis_dir / f"{vis_id}.html"
            if not candidate.exists() and html_vis_dir.exists():
                matches = list(html_vis_dir.glob(f"{vis_id}*.html"))
                candidate = matches[0] if matches else candidate
            if not candidate.exists():
                blockers.append(
                    Blocker(
                        check="csp:missing-html-visual",
                        detail=f"enriched-draft.md references `{m.group(0)}` but no matching `html-visuals/{vis_id}*.html` file exists",
                        fix=f"create `html-visuals/{vis_id}.html` or remove the unresolved marker from enriched-draft.md",
                    )
                )
            else:
                html_txt = candidate.read_text(encoding="utf-8", errors="replace")
                for err in validate_scoped_html_snippet(html_txt, f"html-visuals/{candidate.name}"):
                    blockers.append(
                        Blocker(
                            check="csp:html-visual",
                            detail=err,
                            fix=f"fix CSP/scoping violation in html-visuals/{candidate.name}",
                        )
                    )

    schema_json_path = article_path / "schema.json"
    if schema_json_path.exists():
        for err in validate_article_schema_json(schema_json_path.read_text(encoding="utf-8", errors="replace")):
            blockers.append(
                Blocker(
                    check="schema:json-ld",
                    detail=err,
                    fix="fix schema.json so it is valid JSON-LD with @context and @graph/@type",
                )
            )

    kw_csv_path = article_path / "keyword-record.csv"
    if kw_csv_path.exists():
        for err in validate_keyword_record_csv(kw_csv_path.read_text(encoding="utf-8", errors="replace")):
            blockers.append(
                Blocker(
                    check="keywords:csv",
                    detail=err,
                    fix="ensure keyword-record.csv has a 'Keyword' or 'Keyword / Phrase' header and at least 1 keyword row",
                )
            )

    pub_pack_path = article_path / "publish-package.md"
    if pub_pack_path.exists():
        pp_text = pub_pack_path.read_text(encoding="utf-8", errors="replace")
        if re.search(r'"@context"\s*:\s*"https?://schema\.org"', pp_text):
            blockers.append(
                Blocker(
                    check="schema:separation",
                    detail="publish-package.md contains an inline Schema JSON-LD block (violates Schema Separation red-line)",
                    fix="keep all Schema JSON-LD exclusively inside schema.json and reference it by path in publish-package.md",
                )
            )
    return blockers


STAGE_PREREQUISITES: dict[str, list[tuple[str, str]]] = {
    "intent-research.md": [
        ("topic-card.md", "/article-cluster"),
    ],
    "content-type-library.md": [
        ("topic-card.md", "/article-cluster"),
        ("intent-research.md", "/article-intent-research"),
    ],
    "benchmark-candidates.md": [
        ("topic-card.md", "/article-cluster"),
        ("intent-research.md", "/article-intent-research"),
    ],
    "benchmark-success-formula.md": [
        ("benchmark-candidates.md", "/article-benchmark"),
    ],
    "benchmark-asset-ledger.md": [
        ("benchmark-candidates.md", "/article-benchmark"),
    ],
    "evidence-opinion-pack.md": [
        ("benchmark-success-formula.md", "/article-benchmark-extract"),
        ("benchmark-asset-ledger.md", "/article-benchmark-extract"),
    ],
    "evidence-handoff-summary.md": [
        ("benchmark-success-formula.md", "/article-benchmark-extract"),
    ],
    "knowledge-gap-register.md": [
        ("benchmark-success-formula.md", "/article-benchmark-extract"),
    ],
    "upstream-revision-suggestions.md": [
        ("benchmark-success-formula.md", "/article-benchmark-extract"),
    ],
    "skeleton.md": [
        ("benchmark-success-formula.md", "/article-benchmark-extract"),
        ("evidence-opinion-pack.md", "/article-evidence-opinions"),
    ],
    "h2-heading-strategy.md": [
        ("benchmark-success-formula.md", "/article-benchmark-extract"),
        ("evidence-opinion-pack.md", "/article-evidence-opinions"),
    ],
    "narrative-arc.md": [
        ("skeleton.md", "/article-skeleton"),
        ("benchmark-success-formula.md", "/article-benchmark-extract"),
        ("evidence-opinion-pack.md", "/article-evidence-opinions"),
    ],
    "draft.md": [
        ("skeleton.md", "/article-skeleton"),
        ("narrative-arc.md", "/article-arc"),
        ("evidence-opinion-pack.md", "/article-evidence-opinions"),
        ("benchmark-success-formula.md", "/article-benchmark-extract"),
    ],
    "truth-qa.md": [
        ("draft.md", "/article-draft"),
        ("evidence-opinion-pack.md", "/article-evidence-opinions"),
    ],
    "information-gain-qa.md": [
        ("draft.md", "/article-draft"),
        ("benchmark-success-formula.md", "/article-benchmark-extract"),
        ("truth-qa.md", "/article-truth-qa"),
    ],
    "benchmark-drift-audit.md": [
        ("draft.md", "/article-draft"),
        ("benchmark-success-formula.md", "/article-benchmark-extract"),
        ("benchmark-asset-ledger.md", "/article-benchmark-extract"),
        ("truth-qa.md", "/article-truth-qa"),
        ("information-gain-qa.md", "/article-information-gain-qa"),
    ],
    "reader-qa.md": [
        ("draft.md", "/article-draft"),
        ("skeleton.md", "/article-skeleton"),
        ("truth-qa.md", "/article-truth-qa"),
        ("information-gain-qa.md", "/article-information-gain-qa"),
        ("benchmark-drift-audit.md", "/article-benchmark-qa"),
    ],
    "repair-plan.md": [
        ("draft.md", "/article-draft"),
    ],
}

QA_GATE_SEQUENCE = [
    ("truth-qa.md", "Truth QA", "/article-truth-qa"),
    ("information-gain-qa.md", "Info Gain QA", "/article-information-gain-qa"),
    ("benchmark-drift-audit.md", "Benchmark QA", "/article-benchmark-qa"),
    ("reader-qa.md", "Reader QA", "/article-reader-qa"),
]

POST_QA_STAGE_ARTIFACTS: dict[str, list[tuple[str, str]]] = {
    "enriched-draft.md": [("draft.md", "/article-draft")],
    "image-plan.md": [("draft.md", "/article-draft")],
    "html-visual-plan.md": [("draft.md", "/article-draft")],
    "visual-asset-candidates.md": [("draft.md", "/article-draft")],
    "visual-asset-candidates.json": [("draft.md", "/article-draft")],
    "visual-fit-review.md": [("draft.md", "/article-draft")],
    "visual-render-check.md": [("draft.md", "/article-draft")],
    "visual-spec.md": [("enriched-draft.md", "/article-enrich")],
    "asset-upload-checklist.md": [("enriched-draft.md", "/article-enrich")],
    "resources.md": [("enriched-draft.md", "/article-enrich"), ("visual-spec.md", "/article-visual")],
    "faq.md": [
        ("enriched-draft.md", "/article-enrich"),
        ("visual-spec.md", "/article-visual"),
        ("resources.md", "/article-resources"),
    ],
    "performance-review.md": [
        ("publish-package.md", "/article-publish-pack"),
        ("keyword-record.csv", "/article-publish-pack"),
    ],
}

PUBLISH_STAGE_ARTIFACTS = {
    "publish-package.md",
    "publish-ready-body.md",
    "preview-in-host-theme.html",
    "title-options.md",
    "wordpress-preview-check.md",
    "schema.json",
    "keyword-record.csv",
}

PROFILE_LOCK_ARTIFACTS = {
    "topic-cluster.md",
    "project-profile.research.md",
    "project-profile.md",
    "project-profile.json",
}


def validate_profile_lock_write(
    project_arg: str,
    target_filename: str,
    root: Path = ROOT,
) -> tuple[int, list[Blocker]]:
    """Guard topic-cluster.md, project-profile.research.md, project-profile.md, and project-profile.json against premature writes and double-lock overwrites."""
    if target_filename not in PROFILE_LOCK_ARTIFACTS:
        return 0, []
    project_path = Path(project_arg)
    if not project_path.is_absolute():
        project_path = root / project_path
    if not project_path.exists():
        return 2, [Blocker("input", f"no such project workspace: {project_arg}", "check the path")]

    blockers: list[Blocker] = []
    state, _ = load_json(project_path / "state.json")

    if target_filename == "topic-cluster.md":
        if not (project_path / "project-profile.draft.md").exists() and not (project_path / "project-profile.md").exists():
            blockers.append(
                Blocker(
                    check="prereq:project-profile.draft.md",
                    detail="cannot write topic-cluster.md before project-profile.draft.md exists",
                    fix="run /profile-discover first",
                )
            )
        return (1 if blockers else 0), blockers

    if target_filename == "project-profile.research.md":
        for req_file, fix_cmd in [
            ("project-profile.draft.md", "/profile-discover"),
            ("topic-cluster.md", "/article-cluster"),
        ]:
            if not (project_path / req_file).exists():
                blockers.append(
                    Blocker(
                        check=f"prereq:{req_file}",
                        detail=f"cannot write project-profile.research.md before {req_file} exists",
                        fix=f"run {fix_cmd} first",
                    )
                )
        return (1 if blockers else 0), blockers

    # Double-Lock Prevention: if lockedProfile is already true and both locked files already exist, refuse overwrite
    if (
        state.get("lockedProfile") is True
        and (project_path / "project-profile.md").exists()
        and (project_path / "project-profile.json").exists()
    ):
        blockers.append(
            Blocker(
                check="profile:double-lock",
                detail=f"{target_filename} is already locked (lockedProfile: true)",
                fix="run /workflow-rollback before modifying a locked project profile",
            )
        )
        return 1, blockers

    # Prerequisite check for /profile-lock
    for req_file, fix_cmd in [
        ("project-profile.draft.md", "/profile-discover"),
        ("topic-cluster.md", "/article-cluster"),
        ("project-profile.research.md", "/profile-research-deep"),
    ]:
        if not (project_path / req_file).exists():
            blockers.append(
                Blocker(
                    check=f"prereq:{req_file}",
                    detail=f"cannot write {target_filename} before {req_file} exists",
                    fix=f"run {fix_cmd} first",
                )
            )
    return (1 if blockers else 0), blockers


def validate_stage_write(
    project_arg: str,
    article_slug: str,
    target_filename: str,
    root: Path = ROOT,
) -> tuple[int, list[Blocker]]:
    """Verify upstream stage prerequisites before writing any guarded stage artifact."""
    if target_filename in PUBLISH_STAGE_ARTIFACTS:
        return validate(project_arg, article_slug, root)

    project_path = Path(project_arg)
    if not project_path.is_absolute():
        project_path = root / project_path
    if not project_path.exists():
        return 2, [Blocker("input", f"no such project workspace: {project_arg}", "check the path")]

    article_path = project_path / "articles" / article_slug
    if not article_path.exists():
        return 2, [Blocker("input", f"no such article: articles/{article_slug}", "check the slug")]

    blockers: list[Blocker] = []
    state, load_err = load_json(project_path / "state.json")
    if load_err:
        blockers.append(Blocker("state", load_err, "repair state.json"))

    if target_filename == "topic-card.md":
        if not (project_path / "project-profile.draft.md").exists() and not (project_path / "project-profile.md").exists():
            blockers.append(
                Blocker(
                    check="prereq:project-profile.draft.md",
                    detail="cannot write topic-card.md before project-profile.draft.md exists",
                    fix="run /profile-discover first",
                )
            )
        return (1 if blockers else 0), blockers

    blockers += check_profile_lock(project_path, state)

    if target_filename in STAGE_PREREQUISITES:
        for req_file, fix_cmd in STAGE_PREREQUISITES[target_filename]:
            if not (article_path / req_file).exists():
                blockers.append(
                    Blocker(
                        check=f"prereq:{req_file}",
                        detail=f"cannot write {target_filename} before {req_file} exists",
                        fix=f"run {fix_cmd} first (do not skip stages)",
                    )
                )
        # If target_filename is one of the 4 sequential QA gates, verify all preceding QA gates passed
        qa_names = [q[0] for q in QA_GATE_SEQUENCE]
        if target_filename in qa_names:
            target_idx = qa_names.index(target_filename)
            for prev_file, prev_label, prev_cmd in QA_GATE_SEQUENCE[:target_idx]:
                prev_path = article_path / prev_file
                if prev_path.exists():
                    prev_verdict = read_gate_verdict(prev_path)
                    if prev_verdict != VERDICT_PASS:
                        blockers.append(
                            Blocker(
                                check=f"gate-order:{prev_file}",
                                detail=f"cannot write {target_filename} while preceding {prev_label} ({prev_file}) has verdict {prev_verdict}",
                                fix=f"run /article-repair and re-run {prev_cmd} until PASS before proceeding to later QA gates",
                            )
                        )
        return (1 if blockers else 0), blockers

    if target_filename in POST_QA_STAGE_ARTIFACTS:
        for req_file, fix_cmd in POST_QA_STAGE_ARTIFACTS[target_filename]:
            if not (article_path / req_file).exists():
                blockers.append(
                    Blocker(
                        check=f"prereq:{req_file}",
                        detail=f"cannot write {target_filename} before {req_file} exists",
                        fix=f"run {fix_cmd} first",
                    )
                )
        blockers += check_gates(article_path)
        return (1 if blockers else 0), blockers

    return 0, []


def render(article_slug: str, blockers: list[Blocker]) -> str:
    if not blockers:
        return f"PUBLISH GATE: PASS — {article_slug} is ready for /article-publish-pack.\n"

    lines = [
        f"PUBLISH GATE: BLOCK — {article_slug} has {len(blockers)} unresolved requirement(s):",
        "",
    ]
    for blocker in blockers:
        lines.append(f"  [{blocker.check}] {blocker.detail}")
        lines.append(f"      -> {blocker.fix}")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify an article has earned its publish pack.")
    parser.add_argument("project_path", help="content-workspace/<project-slug>")
    parser.add_argument("article_slug", help="Article directory name under articles/")
    parser.add_argument("--json", action="store_true", dest="json_output", help="Emit JSON.")
    parser.add_argument("--root", default=str(ROOT), help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    code, blockers = validate(args.project_path, args.article_slug, Path(args.root))
    if args.json_output:
        payload = {
            "article": args.article_slug,
            "publishable": code == 0,
            "blockers": [asdict(b) for b in blockers],
        }
        print(json.dumps(payload, indent=2))
    else:
        sys.stdout.write(render(args.article_slug, blockers))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
