#!/usr/bin/env python3
"""PreToolUse hook: refuse to write a publish artifact for an article that has not earned it.

scripts/validate_publish.py is a precondition that /article-publish-pack is told to
respect. This hook enforces the same step-and-verdict check on the Write and Edit
tools themselves so an agent cannot skip upstream stages or model-authored QA gates
and jump straight to writing publish-package.md.

Reads the PreToolUse payload on stdin. Stays silent and exits 0 for every file it
does not guard, which is nearly all of them.

Escape hatch, for when the gate itself needs to be bypassed explicitly:

    B2B_SEO_PUBLISH_GATE=off
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

WORKSPACE_DIR = "content-workspace"

GUARDED_FILENAMES = {
    "topic-card.md",
    "intent-research.md",
    "content-type-library.md",
    "benchmark-candidates.md",
    "benchmark-success-formula.md",
    "benchmark-asset-ledger.md",
    "evidence-opinion-pack.md",
    "evidence-handoff-summary.md",
    "knowledge-gap-register.md",
    "upstream-revision-suggestions.md",
    "skeleton.md",
    "h2-heading-strategy.md",
    "narrative-arc.md",
    "draft.md",
    "truth-qa.md",
    "information-gain-qa.md",
    "benchmark-drift-audit.md",
    "reader-qa.md",
    "repair-plan.md",
    "enriched-draft.md",
    "image-plan.md",
    "html-visual-plan.md",
    "visual-asset-candidates.md",
    "visual-asset-candidates.json",
    "visual-fit-review.md",
    "visual-render-check.md",
    "visual-spec.md",
    "asset-upload-checklist.md",
    "resources.md",
    "faq.md",
    "publish-package.md",
    "publish-ready-body.md",
    "preview-in-host-theme.html",
    "title-options.md",
    "wordpress-preview-check.md",
    "schema.json",
    "keyword-record.csv",
    "performance-review.md",
}


def allow() -> int:
    """Say nothing. The normal permission flow continues untouched."""
    return 0


def deny(reason: str) -> int:
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        },
        sys.stdout,
    )
    return 0


PROFILE_GUARDED_FILENAMES = {
    "topic-cluster.md",
    "project-profile.research.md",
    "project-profile.md",
    "project-profile.json",
    "state.json",
}


def _resolve_target_path(file_path: str) -> Path:
    """Resolve file_path to an existing file under REPO_ROOT when invoked from a parent/external working directory."""
    p = Path(file_path)
    if p.exists() or p.is_absolute():
        return p
    candidate = REPO_ROOT / p
    if candidate.exists():
        return candidate
    parts = p.parts
    if WORKSPACE_DIR in parts:
        idx = len(parts) - 1 - parts[::-1].index(WORKSPACE_DIR)
        ws_candidate = REPO_ROOT.joinpath(*parts[idx:])
        if ws_candidate.exists():
            return ws_candidate
    return candidate


def locate_profile_target(file_path: str) -> tuple[str, str] | None:
    """Return (project-relative-path, filename) if this path is a guarded project-level profile artifact."""
    path = Path(file_path)
    if path.name not in PROFILE_GUARDED_FILENAMES:
        return None
    parts = path.parts
    try:
        index = len(parts) - 1 - parts[::-1].index(WORKSPACE_DIR)
    except ValueError:
        return None
    if len(parts) == index + 3:
        return f"{WORKSPACE_DIR}/{parts[index + 1]}", path.name
    return None


def locate_article(file_path: str) -> tuple[str, str, str] | None:
    """Return (project-relative-path, article-slug, guarded-name) if this path is a guarded article artifact."""
    path = Path(file_path)
    parts = path.parts
    try:
        index = len(parts) - 1 - parts[::-1].index(WORKSPACE_DIR)
    except ValueError:
        return None

    # content-workspace/<project>/articles/<slug>/<file>
    if len(parts) >= index + 5 and parts[index + 2] == "articles":
        if len(parts) == index + 5 and path.name in GUARDED_FILENAMES:
            return f"{WORKSPACE_DIR}/{parts[index + 1]}", parts[index + 3], path.name
        # content-workspace/<project>/articles/<slug>/html-visuals/<id>.html
        if len(parts) == index + 6 and parts[index + 4] == "html-visuals" and path.suffix.lower() == ".html":
            return f"{WORKSPACE_DIR}/{parts[index + 1]}", parts[index + 3], "html-visual-plan.md"
        # content-workspace/<project>/articles/<slug>/benchmarks/<source>-raw-observations.md
        if len(parts) == index + 6 and parts[index + 4] == "benchmarks":
            return f"{WORKSPACE_DIR}/{parts[index + 1]}", parts[index + 3], "benchmark-success-formula.md"
        # content-workspace/<project>/articles/<slug>/visual/<asset>
        if len(parts) == index + 6 and parts[index + 4] == "visual":
            return f"{WORKSPACE_DIR}/{parts[index + 1]}", parts[index + 3], "visual-spec.md"
    return None


def main() -> int:
    if os.environ.get("B2B_SEO_PUBLISH_GATE", "").lower() == "off":
        return allow()

    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return allow()

    file_path = (payload.get("tool_input") or {}).get("file_path")
    if not isinstance(file_path, str) or not file_path:
        return allow()

    profile_target = locate_profile_target(file_path)
    if profile_target is not None:
        project, target_name = profile_target
        tool_input = payload.get("tool_input") or {}
        target_path = _resolve_target_path(file_path)
        effective_json_text = ""
        if isinstance(tool_input.get("content"), str):
            effective_json_text = tool_input["content"]
        elif (
            isinstance(tool_input.get("old_string"), str)
            and isinstance(tool_input.get("new_string"), str)
            and target_path.exists()
        ):
            existing_text = target_path.read_text(encoding="utf-8", errors="replace")
            if tool_input.get("replace_all"):
                effective_json_text = existing_text.replace(tool_input["old_string"], tool_input["new_string"])
            else:
                effective_json_text = existing_text.replace(tool_input["old_string"], tool_input["new_string"], 1)

        if target_name in {"state.json", "project-profile.json"} and effective_json_text:
            try:
                parsed_json = json.loads(effective_json_text)
            except Exception as exc:  # noqa: BLE001
                return deny(f"Blocked writing invalid JSON to {target_name}: {exc}")
            schema_file = (
                REPO_ROOT / "config" / ("state-schema.json" if target_name == "state.json" else "profile-schema.json")
            )
            try:
                from workflow_status import validate_state

                schema_err = validate_state(parsed_json, schema_file)
            except Exception as exc:  # noqa: BLE001
                return deny(f"Schema validator failed on {target_name}: {exc}")
            if schema_err:
                return deny(f"Blocked writing schema-violating {target_name}:\n  {schema_err}")

        if target_name == "state.json":
            return allow()

        try:
            from validate_publish import validate_profile_lock_write

            code, blockers = validate_profile_lock_write(project, target_name, REPO_ROOT)
        except Exception as error:  # noqa: BLE001
            return deny(f"The profile gate could not run: {type(error).__name__}: {error}")
        if code == 0:
            return allow()
        lines = [f"Cannot write {target_name} in {project}:", ""]
        for blocker in blockers:
            lines.append(f"  [{blocker.check}] {blocker.detail}")
            lines.append(f"      fix: {blocker.fix}")
        return deny("\n".join(lines))

    located = locate_article(file_path)
    if located is None:
        return allow()

    project, slug, guarded_name = located

    try:
        from validate_publish import validate_stage_write

        code, blockers = validate_stage_write(project, slug, guarded_name, REPO_ROOT)
    except Exception as error:  # noqa: BLE001 — a broken gate must not become an open gate
        return deny(
            f"The publish gate could not run, so {Path(file_path).name} was not written: "
            f"{type(error).__name__}: {error}\n"
            f"Fix scripts/validate_publish.py, or set B2B_SEO_PUBLISH_GATE=off to bypass."
        )

    # Real-time content inspection for incoming scoped HTML modules (.b2b-mod-* / .linker-article-*) and CSP in Write/Edit payloads
    tool_input = payload.get("tool_input") or {}
    target_path = _resolve_target_path(file_path)
    effective_text = ""
    if "content" in tool_input and isinstance(tool_input.get("content"), str):
        effective_text = tool_input["content"]
    elif (
        isinstance(tool_input.get("old_string"), str)
        and isinstance(tool_input.get("new_string"), str)
        and target_path.exists()
    ):
        existing_text = target_path.read_text(encoding="utf-8", errors="replace")
        if tool_input.get("replace_all"):
            effective_text = existing_text.replace(tool_input["old_string"], tool_input["new_string"])
        else:
            effective_text = existing_text.replace(tool_input["old_string"], tool_input["new_string"], 1)
    elif isinstance(tool_input.get("new_string"), str):
        effective_text = tool_input["new_string"]

    if effective_text and target_path.name == "schema.json":
        try:
            from validate_publish import validate_article_schema_json

            schema_errs = validate_article_schema_json(effective_text, "schema.json")
            if schema_errs:
                return deny("Blocked writing invalid schema.json:\n  " + "\n  ".join(schema_errs))
        except Exception as error:  # noqa: BLE001 — fail closed
            return deny(f"The schema.json gate failed while inspecting {target_path.name}: {type(error).__name__}: {error}")

    if effective_text and target_path.name == "keyword-record.csv":
        try:
            from validate_publish import validate_keyword_record_csv

            csv_errs = validate_keyword_record_csv(effective_text, "keyword-record.csv")
            if csv_errs:
                return deny("Blocked writing invalid keyword-record.csv:\n  " + "\n  ".join(csv_errs))
        except Exception as error:  # noqa: BLE001 — fail closed
            return deny(f"The keyword-record.csv gate failed while inspecting {target_path.name}: {type(error).__name__}: {error}")

    if effective_text and target_path.name == "publish-package.md":
        import re as _re

        if _re.search(r'"@context"\s*:\s*"https?://schema\.org"', effective_text):
            return deny(
                "Blocked writing inline Schema JSON-LD inside publish-package.md (violates Schema Separation red-line). "
                "Write JSON-LD exclusively to schema.json."
            )

    if effective_text and target_path.suffix.lower() in {".md", ".html"}:
        try:
            from assemble_publish_draft import (
                FORBIDDEN_INLINE_JS_RE,
                extract_balanced_b2b_modules,
                validate_scoped_html_snippet,
            )
            import re as _re

            no_code_fences = _re.sub(r"```.*?```", "", effective_text, flags=_re.DOTALL)
            if FORBIDDEN_INLINE_JS_RE.search(no_code_fences):
                return deny(
                    f"Blocked writing CSP-violating inline JS (<script>, onclick/oninput..., or javascript:) to {target_path.name}."
                )
            for _, _, mod_html in extract_balanced_b2b_modules(no_code_fences):
                if mod_html.lower().startswith("<div"):
                    for err in validate_scoped_html_snippet(mod_html, target_path.name):
                        return deny(f"Blocked writing invalid/CSP-violating HTML snippet to {target_path.name}:\n  {err}")
        except Exception as error:  # noqa: BLE001 — fail closed
            return deny(f"The HTML/CSP gate failed while inspecting {target_path.name}: {type(error).__name__}: {error}")

    if code == 0:
        return allow()

    lines = [
        f"{slug} is not publishable, so {Path(file_path).name} must not be written.",
        "",
    ]
    for blocker in blockers:
        lines.append(f"  [{blocker.check}] {blocker.detail}")
        lines.append(f"      fix: {blocker.fix}")
    lines += [
        "",
        "This is config/workflow-spec.yaml `publish_requires_all_qa_gates_pass` enforced at "
        "the tool boundary. Clear the blockers and try again; do not work around this by "
        "writing the file another way.",
    ]
    return deny("\n".join(lines))


if __name__ == "__main__":
    raise SystemExit(main())
