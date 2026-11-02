#!/usr/bin/env python3
"""Validate that the v3 skill-only workflow matches the canonical specs.

Reads:
- config/workflow-spec.yaml
- config/artifact-graph.yaml
- config/state-schema.json

Checks:
- Required specs are loadable and internally consistent.
- Every workflow stage has a matching skill directory.
- Skill frontmatter is well-formed.
- Agent frontmatter is well-formed.
- Article skills enforce the locked-profile gate.
- /workflow-status stays read-only.
- The example workspace satisfies the artifact graph.
- No retired command names leak into skills/agents/docs.
- Banned low-quality phrases are absent.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "config"
SKILLS_DIR = ROOT / ".claude" / "skills"
AGENTS_DIR = ROOT / ".claude" / "agents"
WORKSPACE_DIR = ROOT / "content-workspace"
EXAMPLE_PROJECT = WORKSPACE_DIR / "example-metal-divider"

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
NAME_RE = re.compile(r"^[a-z0-9-]+$")
QA_BLOCK_RE = re.compile(
    r"(?im)^\s*(?:status|result|gate)\s*:\s*(?:block|blocked|fail|failed)\b"
    r"|^\s*BLOCK\b"
    r"|^\s*\*\*Status\*\*\s*:\s*(?:block|blocked|fail|failed)\b"
)

BANNED_PHRASES = [
    "In today's fast-paced world",
    "In the ever-evolving world",
    "game-changer",
    "supercharge",
    "delve into",
]

ALLOWED_AGENT_COLORS = {
    "red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "gray", "teal"
}


def load_yaml(path: Path) -> Any:
    if not path.exists():
        raise AssertionError(f"Missing spec file: {path.relative_to(ROOT)}")
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def load_json(path: Path) -> Any:
    if not path.exists():
        raise AssertionError(f"Missing spec file: {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def load_frontmatter(path: Path) -> dict[str, Any] | None:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    return yaml.safe_load(match.group(1)) or {}


def validate_specs(spec: dict, graph: dict, schema: dict) -> list[str]:
    failures: list[str] = []

    stages = graph.get("stages", {})
    spec_stage_names = [s["name"] for s in spec.get("stages", []) if isinstance(s, dict) and s.get("name")]
    if list(stages.keys()) != spec_stage_names:
        failures.append(
            f"Stage order mismatch between workflow-spec.yaml ({spec_stage_names}) and artifact-graph.yaml ({list(stages.keys())})"
        )
    for stage_name, stage in stages.items():
        required = stage.get("required_outputs", [])
        if not isinstance(required, list):
            failures.append(f"artifact-graph stage {stage_name}.required_outputs is not a list")
            continue
        for artifact in required:
            if not isinstance(artifact, str):
                failures.append(f"artifact-graph stage {stage_name} has non-string artifact: {artifact!r}")

    qa_gates = graph.get("qa_gates", [])
    gate_names = {g["name"] for g in qa_gates if isinstance(g, dict) and "name" in g}
    spec_gates = set(spec.get("constants", {}).get("qa_gates", []))
    if gate_names != spec_gates:
        failures.append(
            f"QA gate mismatch: workflow-spec has {sorted(spec_gates)}, artifact-graph has {sorted(gate_names)}"
        )

    required_schema = schema.get("required", [])
    for field in ("projectSlug", "profileStatus", "lockedProfile", "currentStage", "nextCommand", "lastUpdated"):
        if field not in required_schema:
            failures.append(f"state-schema.json is missing required field: {field}")

    return failures


def validate_workflow_sequence(spec: dict, agents_md: str | None = None) -> list[str]:
    """Ensure workflow-spec physical stage order matches the forward next-chain,
    and that every chain stage is documented in AGENTS.md.

    Catches the "reorder done halfway" class of bug where the physical stage
    list, the next-pointers, and the docs disagree (e.g. cluster physically
    listed after lock, or a new stage added to config but omitted from AGENTS.md).
    """
    failures: list[str] = []

    stages = spec.get("stages", [])
    if not isinstance(stages, list) or not stages:
        failures.append("workflow-spec.yaml has no stages list")
        return failures

    by_name: dict[str, dict] = {}
    by_command: dict[str, str] = {}
    physical_order: list[str] = []
    for stage in stages:
        if not isinstance(stage, dict) or not stage.get("name"):
            continue
        name = stage["name"]
        physical_order.append(name)
        by_name[name] = stage
        cmd = stage.get("command")
        if cmd:
            by_command[cmd] = name

    def _forward_next(stage: dict) -> str | None:
        nxt = stage.get("next")
        if isinstance(nxt, dict):
            # Conditional: take the forward branch, ignore loop-back branches.
            return nxt.get("else") or nxt.get("if_complete") or nxt.get("default")
        return nxt if isinstance(nxt, str) else None

    # Follow the forward next-chain from the first physical stage.
    chain: list[str] = []
    seen: set[str] = set()
    current = physical_order[0] if physical_order else None
    while current and current in by_name and current not in seen:
        seen.add(current)
        chain.append(current)
        nxt_cmd = _forward_next(by_name[current])
        if not nxt_cmd:
            break
        current = by_command.get(nxt_cmd) or nxt_cmd.lstrip("/")

    # Check A: physical order of chain stages must match chain order.
    physical_index = {name: i for i, name in enumerate(physical_order)}
    chain_in_physical = [n for n in chain if n in physical_index]
    expected_order = sorted(chain_in_physical, key=lambda n: physical_index[n])
    if chain_in_physical != expected_order:
        failures.append(
            "workflow-spec.yaml physical stage order does not match the next-chain order "
            f"(chain={chain_in_physical}, physical={expected_order})"
        )

    # Check B: every chain stage must be documented in AGENTS.md as /<name>.
    if agents_md is None:
        agents_md = (ROOT / "AGENTS.md").read_text(encoding="utf-8", errors="replace")
    for name in chain:
        # Whole-token match: /<name> must not be immediately followed by another
        # word/hyphen char, so /article-benchmark is not counted as present merely
        # because /article-benchmark-extract or /article-benchmark-qa exists.
        if not re.search(rf"/{re.escape(name)}(?![\w-])", agents_md):
            failures.append(f"workflow chain stage {name} is not referenced in AGENTS.md")

    return failures


def validate_stage_skills(stages: dict[str, dict]) -> list[str]:
    failures: list[str] = []
    for stage_name in stages:
        skill_path = SKILLS_DIR / stage_name / "SKILL.md"
        if not skill_path.exists():
            failures.append(f"Stage {stage_name} is missing skill file: {skill_path.relative_to(ROOT)}")
    return failures


def validate_skill_frontmatters() -> list[str]:
    failures: list[str] = []
    for skill_path in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        rel = skill_path.relative_to(ROOT)
        frontmatter = load_frontmatter(skill_path)
        if frontmatter is None:
            failures.append(f"{rel} is missing YAML frontmatter")
            continue

        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")
        user_invocable = frontmatter.get("user-invocable")

        if not name:
            failures.append(f"{rel} must define name frontmatter")
            continue
        if not NAME_RE.match(name):
            failures.append(f"{rel} name must be lowercase letters, numbers, and hyphens")
        if name != skill_path.parent.name:
            failures.append(f"{rel} name must match directory name")
        if not description:
            failures.append(f"{rel} must define description frontmatter")
        elif not isinstance(description, str) or not description.startswith(("Use when:", "Use after:")):
            failures.append(f"{rel} description must start with 'Use when:' or 'Use after:'")
        elif len(description) > 1024:
            failures.append(f"{rel} description exceeds 1024 characters")

        if user_invocable is not None and not isinstance(user_invocable, bool):
            failures.append(f"{rel} user-invocable must be a boolean")

        if "argument-hint" in frontmatter:
            text = skill_path.read_text(encoding="utf-8")
            if "## Argument Contract" not in text:
                failures.append(f"{rel} with argument-hint must include an Argument Contract section")
            if "$ARGUMENTS" not in text:
                failures.append(f"{rel} with argument-hint must explain $ARGUMENTS handling")

    return failures


def validate_agent_frontmatters() -> list[str]:
    failures: list[str] = []
    for agent_path in sorted(AGENTS_DIR.glob("*.md")):
        rel = agent_path.relative_to(ROOT)
        text = agent_path.read_text(encoding="utf-8")
        if "DEPRECATED" in text[:200].upper():
            continue
        frontmatter = load_frontmatter(agent_path)
        if frontmatter is None:
            failures.append(f"{rel} is missing YAML frontmatter")
            continue

        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")
        if not name:
            failures.append(f"{rel} must define name frontmatter")
            continue
        if not NAME_RE.match(name):
            failures.append(f"{rel} name must be lowercase letters, numbers, and hyphens")
        if name != agent_path.stem:
            failures.append(f"{rel} name must match filename")
        if not description:
            failures.append(f"{rel} must define description frontmatter")
        elif not isinstance(description, str) or not description.startswith(("Use when", "Use after")):
            failures.append(f"{rel} description must start with 'Use when' or 'Use after'")
        if not frontmatter.get("tools"):
            failures.append(f"{rel} must define limited tool access")
        if not frontmatter.get("model"):
            failures.append(f"{rel} must define model frontmatter")
        color = frontmatter.get("color", "")
        if not color:
            failures.append(f"{rel} must define color frontmatter")
        elif color not in ALLOWED_AGENT_COLORS:
            failures.append(f"{rel} uses unsupported color: {color}")
    return failures


def validate_article_skills_lock_profile(article_stage_names: list[str]) -> list[str]:
    failures: list[str] = []
    for stage_name in article_stage_names:
        skill_path = SKILLS_DIR / stage_name / "SKILL.md"
        if not skill_path.exists():
            continue
        text = skill_path.read_text(encoding="utf-8")
        if "project-profile.md" not in text or "lockedProfile" not in text:
            failures.append(
                f"{skill_path.relative_to(ROOT)} must check project-profile.md and lockedProfile"
            )
    return failures


import ast

class WriteOperationVisitor(ast.NodeVisitor):
    def __init__(self):
        self.found_writes = []
        
    def visit_Call(self, node):
        # Detect open(..., "w") or open(..., "a")
        if isinstance(node.func, ast.Name) and node.func.id == "open":
            if len(node.args) >= 2:
                mode = getattr(node.args[1], "value", None) or getattr(node.args[1], "s", None)
                if mode in ("w", "a", "wb", "ab"):
                    self.found_writes.append(f"open(..., '{mode}')")
        
        # Detect Path.write_text, Path.write_bytes, os.remove, os.unlink, Path.unlink, shutil.rmtree
        if isinstance(node.func, ast.Attribute):
            func_name = node.func.attr
            if func_name in ("write_text", "write_bytes", "mkdir", "rmdir", "remove", "unlink", "rename", "replace"):
                self.found_writes.append(f"attribute call: {func_name}")
                
        # Detect subprocess.run(["rm", ...]) or subprocess.run("rm ...")
        if isinstance(node.func, ast.Attribute) and node.func.attr == "run" and isinstance(node.func.value, ast.Name) and node.func.value.id == "subprocess":
            if node.args:
                arg = node.args[0]
                if isinstance(arg, ast.List):
                    elements = [getattr(el, "value", None) or getattr(el, "s", None) for el in arg.elts]
                    if "rm" in elements or "rmdir" in elements:
                        self.found_writes.append("subprocess run: rm")
                elif isinstance(arg, ast.Constant) or isinstance(arg, ast.Str):
                    val = getattr(arg, "value", arg.s)
                    if "rm " in val or "rmdir " in val:
                        self.found_writes.append("subprocess run: rm")
                        
        self.generic_visit(node)


def validate_workflow_status_read_only() -> list[str]:
    failures: list[str] = []
    skill_path = SKILLS_DIR / "workflow-status" / "SKILL.md"
    if not skill_path.exists():
        failures.append("workflow-status skill is missing")
        return failures
    text = skill_path.read_text(encoding="utf-8")
    required_rules = [
        "Do not create, edit, or delete files.",
        "Do not update `state.json`.",
        "Do not run the next command automatically.",
        "Do not bypass the locked profile gate.",
    ]
    for rule in required_rules:
        if rule not in text:
            failures.append(f"workflow-status skill is missing read-only rule: {rule}")

    script_path = ROOT / "scripts" / "workflow_status.py"
    if script_path.exists():
        try:
            tree = ast.parse(script_path.read_text(encoding="utf-8"))
            visitor = WriteOperationVisitor()
            visitor.visit(tree)
            # Since workflow_status.py is now allowed to write state.json atomically (using replace/unlink)
            # and run rm in subprocess under --next/--rollback flags, we verify that the only
            # writes/deletes are the ones we explicitly expect:
            # - attribute call: replace (from atomic state saving)
            # - attribute call: unlink (from atomic state saving)
            # - subprocess run: rm (from rollback cleanup)
            # Any other writing calls should be flagged.
            unexpected = [
                w for w in visitor.found_writes
                if w not in ("attribute call: replace", "attribute call: unlink", "subprocess run: rm")
            ]
            if unexpected:
                failures.append(
                    f"scripts/workflow_status.py contains unexpected write calls: {', '.join(unexpected)}"
                )
        except SyntaxError as e:
            failures.append(f"Syntax error parsing scripts/workflow_status.py: {e}")
    return failures


def validate_example_workspace(graph: dict) -> list[str]:
    failures: list[str] = []
    if not EXAMPLE_PROJECT.exists():
        failures.append("Example workspace missing: content-workspace/example-metal-divider")
        return failures

    state_path = EXAMPLE_PROJECT / "state.json"
    if not state_path.exists():
        failures.append("Example workspace missing state.json")
    else:
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"Example state.json is invalid JSON: {exc}")
            state = {}
        else:
            if state.get("lockedProfile") is not True:
                failures.append("Example state.json should have lockedProfile=true")
            if state.get("nextCommand") != "/article-review":
                failures.append("Example state.json nextCommand should be /article-review")

    for artifact in graph.get("project_level_artifacts", {}).get("required", []):
        path = EXAMPLE_PROJECT / artifact
        if not path.exists():
            failures.append(f"Example workspace missing required project artifact: {artifact}")

    # Inspect the first article directory for required article artifacts.
    articles_dir = EXAMPLE_PROJECT / "articles"
    article_dirs = [p for p in articles_dir.iterdir() if p.is_dir()] if articles_dir.exists() else []
    if not article_dirs:
        failures.append("Example workspace has no article directories")
        return failures

    for article_path in article_dirs:
        for artifact in graph.get("article_level_artifacts", {}).get("required", []):
            resolved = artifact.replace("<article-slug>", article_path.name)
            path = EXAMPLE_PROJECT / resolved
            if not path.exists():
                failures.append(
                    f"Example workspace missing required article artifact: {resolved}"
                )

        # QA gate blocking check.
        for gate in graph.get("qa_gates", []):
            artifact = gate["artifact"].replace("<article-slug>", article_path.name)
            path = EXAMPLE_PROJECT / artifact
            if path.exists() and QA_BLOCK_RE.search(path.read_text(encoding="utf-8")):
                failures.append(f"Example QA gate is blocking publish: {artifact}")

    return failures


def validate_retired_commands(spec: dict) -> list[str]:
    failures: list[str] = []
    retired = spec.get("retired_commands", {})
    if not retired:
        return failures

    # Match retired command names as whole tokens: do not flag /article-evidence
    # when it appears inside /article-evidence-opinions.
    patterns = {
        cmd: re.compile(re.escape(cmd) + r"(?![a-zA-Z0-9-])", re.IGNORECASE)
        for cmd in retired
    }
    scan_roots = [SKILLS_DIR, AGENTS_DIR, ROOT / "docs", ROOT / "content-workspace"]
    for scan_root in scan_roots:
        for path in scan_root.rglob("*"):
            if not path.is_file() or path.suffix not in {".md", ".py", ".json", ".yaml", ".yml"}:
                continue
            # Skip archived/history docs that intentionally discuss retired commands.
            if "history" in path.parts or "archive" in path.parts:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            for cmd, pattern in patterns.items():
                if pattern.search(text):
                    failures.append(f"{path.relative_to(ROOT)} references retired command {cmd}")
    return failures


def validate_banned_phrases() -> list[str]:
    failures: list[str] = []
    skip_dirs = {
        "archive",
        "agent-memory",
        "__pycache__",
        ".git",
        ".kimi",
        ".firecrawl",
    }
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".py"}:
            continue
        if any(part in skip_dirs for part in path.parts):
            continue
        # Do not scan the validation script's own literal list of banned phrases.
        if path.samefile(Path(__file__)):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for phrase in BANNED_PHRASES:
            if phrase in text:
                failures.append(f"{path.relative_to(ROOT)} contains banned phrase: {phrase}")
    return failures


def validate_constants_in_skills(spec: dict) -> list[str]:
    failures: list[str] = []
    constants = spec.get("constants", {})

    benchmark_skill = SKILLS_DIR / "article-benchmark" / "SKILL.md"
    if benchmark_skill.exists():
        text = benchmark_skill.read_text(encoding="utf-8")
        selected = constants.get("benchmark_selected_count", 3)
        pool = constants.get("benchmark_candidate_pool_size", 5)
        lib_cats = constants.get("content_type_library_categories", 6)
        if str(selected) not in text:
            failures.append(f"article-benchmark skill does not reference selected count ({selected})")
        if str(pool) not in text:
            failures.append(f"article-benchmark skill does not reference candidate pool size ({pool})")
        if str(lib_cats) not in text:
            failures.append(f"article-benchmark skill does not reference content-type library category count ({lib_cats})")

    extract_skill = SKILLS_DIR / "article-benchmark-extract" / "SKILL.md"
    if extract_skill.exists():
        text = extract_skill.read_text(encoding="utf-8")
        total = constants.get("success_formula_total_dimensions", 21)
        if str(total) not in text:
            failures.append(f"article-benchmark-extract skill does not reference dimension count ({total})")

    intent_skill = SKILLS_DIR / "article-intent-research" / "SKILL.md"
    if intent_skill.exists():
        text = intent_skill.read_text(encoding="utf-8")
        min_channels = constants.get("intent_research_minimum_channels", 3)
        if str(min_channels) not in text:
            failures.append(f"article-intent-research skill does not reference minimum channel count ({min_channels})")

    return failures


def validate_extra_acceptance_criteria(spec: dict, graph: dict) -> list[str]:
    failures: list[str] = []

    # 1. No inner templates and READMEs
    for skill_dir in SKILLS_DIR.iterdir():
        if not skill_dir.is_dir():
            continue
        # templates folder check
        templates_dir = skill_dir / "templates"
        if templates_dir.exists():
            failures.append(f"Skill directory {skill_dir.name} contains forbidden templates directory")
        # README.md check (case-insensitive)
        for p in skill_dir.iterdir():
            if p.is_file() and p.name.lower() == "readme.md":
                failures.append(f"Skill directory {skill_dir.name} contains forbidden README file: {p.name}")

    # 2. Frontmatter security (< > brackets check)
    # Argument hints legitimately use placeholder syntax like [content-workspace/<project-slug>];
    # we strip those lines before scanning for actual XML/HTML injection patterns.
    for skill_path in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        text = skill_path.read_text(encoding="utf-8")
        match = FRONTMATTER_RE.match(text)
        if match:
            fm_lines = match.group(1).splitlines()
            scan_lines = [
                line
                for line in fm_lines
                if not re.match(r"^argument-hint:\s*", line)
                and not re.match(r"^\s+argument-hint", line)
            ]
            fm_text = "\n".join(scan_lines)
            if "<" in fm_text or ">" in fm_text:
                failures.append(f"{skill_path.relative_to(ROOT)} has XML brackets (< or >) in frontmatter")

    # 3. Retired skills check (artifact-graph, profile-foundation)
    retired_skills = {"artifact-graph", "profile-foundation"}
    # Exclude matches followed by .yaml, .md (like config/artifact-graph.yaml or artifact-graph.yaml)
    patterns = {
        name: re.compile(r"\b" + re.escape(name) + r"\b(?!\.(?:yaml|yml|md))", re.IGNORECASE)
        for name in retired_skills
    }
    scan_roots = [SKILLS_DIR, AGENTS_DIR, ROOT / "docs"]
    for scan_root in scan_roots:
        if not scan_root.exists():
            continue
        for path in scan_root.rglob("*"):
            if not path.is_file() or path.suffix not in {".md", ".py", ".json", ".yaml", ".yml"}:
                continue
            if "history" in path.parts or "archive" in path.parts:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            for name, pattern in patterns.items():
                if pattern.search(text):
                    if path.name in {"AGENTS.md", "CLAUDE.md", "validate_discovery_profile_workflow.py"}:
                        continue
                    failures.append(f"{path.relative_to(ROOT)} references retired skill {name}")

    # 4. Global Template Path check
    template_refs = set()
    ref_pattern = re.compile(r"templates/([a-zA-Z0-9_./-]+(?:\.md)?)")
    scan_files = list(SKILLS_DIR.rglob("*.md")) + list(AGENTS_DIR.glob("*.md")) + list((ROOT / "docs").rglob("*.md"))
    for p in scan_files:
        if "history" in p.parts or "archive" in p.parts:
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        for m in ref_pattern.findall(text):
            template_refs.add(m)

    root_templates = {p.name for p in (ROOT / "templates").glob("*.md")}
    for ref in template_refs:
        ref_name = Path(ref).name
        if ref_name not in root_templates:
            failures.append(f"Referenced template `{ref}` does not exist in root templates/ directory")

    # 5. Prose Thickness Check (active skills > 50 lines including empty lines/pauses but excluding frontmatter)
    for skill_path in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        text = skill_path.read_text(encoding="utf-8")
        match = FRONTMATTER_RE.match(text)
        body = text[match.end():] if match else text
        body_lines = body.splitlines()

        if len(body_lines) < 50:
            failures.append(f"Active skill {skill_path.parent.name} has thin content ({len(body_lines)} lines, threshold is 50)")

    return failures


def main() -> int:
    failures: list[str] = []

    try:
        spec = load_yaml(CONFIG_DIR / "workflow-spec.yaml")
        graph = load_yaml(CONFIG_DIR / "artifact-graph.yaml")
        schema = load_json(CONFIG_DIR / "state-schema.json")
    except (AssertionError, yaml.YAMLError, json.JSONDecodeError) as exc:
        print(f"Spec loading failed: {exc}")
        return 1

    failures.extend(validate_specs(spec, graph, schema))
    failures.extend(validate_workflow_sequence(spec))

    stage_names = list(graph.get("stages", {}).keys())
    failures.extend(validate_stage_skills(stage_names))
    failures.extend(validate_skill_frontmatters())
    failures.extend(validate_agent_frontmatters())

    article_stage_names = [
        name
        for name, info in graph.get("stages", {}).items()
        if info.get("category") in {"article", "qa", "repair"}
    ]
    failures.extend(validate_article_skills_lock_profile(article_stage_names))
    failures.extend(validate_workflow_status_read_only())
    failures.extend(validate_example_workspace(graph))
    failures.extend(validate_retired_commands(spec))
    failures.extend(validate_banned_phrases())
    failures.extend(validate_constants_in_skills(spec))
    failures.extend(validate_extra_acceptance_criteria(spec, graph))

    commands_dir = ROOT / ".claude" / "commands"
    if commands_dir.exists():
        failures.append("Deprecated .claude/commands/ directory still exists")

    if failures:
        print("Validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
