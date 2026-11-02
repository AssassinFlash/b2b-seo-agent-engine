#!/usr/bin/env python3
"""
Deep audit of the B2B SEO Agent System.
Read-only scan of .claude/commands, .claude/agents, .claude/skills,
templates/, docs/, and config/ to find structural inconsistencies,
missing references, deprecated-but-referenced files, and thin content.
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple, Any

import yaml

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
CLAUDE = ROOT / ".claude"
TEMPLATES = ROOT / "templates"
DOCS = ROOT / "docs"
CONFIG = ROOT / "config"

COMMANDS_DIR = CLAUDE / "commands"
AGENTS_DIR = CLAUDE / "agents"
SKILLS_DIR = CLAUDE / "skills"

SUPPORT_SUBDIRS = {"templates", "examples", "references"}


def load_frontmatter(path: Path) -> Tuple[Dict[str, Any], str]:
    """Return frontmatter dict and body text."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except Exception as e:
        fm = {"_parse_error": str(e)}
    body = parts[2]
    return fm, body


def find_markdown_files(directory: Path, exclude_support: bool = False) -> List[Path]:
    if not directory.exists():
        return []
    files = []
    for p in directory.rglob("*.md"):
        if exclude_support:
            rel_parts = p.relative_to(directory).parts
            if any(part in SUPPORT_SUBDIRS for part in rel_parts[:-1]):
                continue
        files.append(p)
    return sorted(files)


def find_support_files(directory: Path) -> List[Path]:
    """Find markdown files inside any templates/examples/references subdir under directory."""
    files = []
    if directory.exists():
        for p in directory.rglob("*.md"):
            rel_parts = p.relative_to(directory).parts
            if any(part in SUPPORT_SUBDIRS for part in rel_parts[:-1]):
                files.append(p)
    return sorted(files)


def is_deprecated(fm: Dict[str, Any], body: str) -> bool:
    """Detect deprecated/retired status from frontmatter or description."""
    status = str(fm.get("status", "")).lower()
    desc = str(fm.get("description", "")).lower()
    if status in {"retired", "deprecated"}:
        return True
    if "deprecated" in desc or "retired" in desc or "do not use for new work" in desc:
        return True
    # Check first non-empty body line for deprecation marker
    first_lines = "\n".join(body.lower().splitlines()[:3])
    if any(marker in first_lines for marker in ["# deprecated", "# retired", "> **deprecated", "> **retired"]):
        return True
    return False


def extract_command_refs(text: str, command_names: Set[str]) -> Set[str]:
    """Find references to existing commands only (slash-prefixed and in command list)."""
    # Backtick-enclosed commands — keep only known command names
    refs = {w for w in re.findall(r"`/(\w[\w-]*)`", text) if w in command_names}
    # Plain slash commands; keep only those that match a known command to avoid
    # false positives from paths/headings like /open, /long, /data
    candidates = set(re.findall(r"/(\w[\w-]*)", text))
    refs.update(candidates & command_names)
    return refs


def extract_skill_refs(text: str, skill_names: Set[str]) -> Set[str]:
    """Find references to actual skills only."""
    refs = set()
    # backtick skill names that are known skills
    refs.update({w for w in re.findall(r"`([a-z][a-z0-9-]+)`", text) if w in skill_names})
    # frontmatter-style skills: list items
    refs.update({w for w in re.findall(r"-\s+([a-z][a-z0-9-]+)", text) if w in skill_names})
    # quoted inline references like `search-toolbox` already covered
    return refs


def extract_agent_refs(text: str, agent_names: Set[str]) -> Set[str]:
    """Find references to actual agents only."""
    refs = set()
    # bold agent names that are known agents
    refs.update({w for w in re.findall(r"\*\*([a-z][a-z0-9-]+)\*\*", text) if w in agent_names})
    # explicit spawn references
    refs.update({w for w in re.findall(r"[Ss]pawn\s+\*\*([a-z][a-z0-9-]+)\*\*", text) if w in agent_names})
    return refs


def extract_template_refs(text: str) -> Set[str]:
    """Find templates/... references."""
    return set(re.findall(r"templates/[a-zA-Z0-9_./-]+(?:\.md)?", text))


def main():
    issues: List[Tuple[str, str]] = []
    stats: Dict[str, Any] = {
        "commands": [],
        "agents": [],
        "skills": [],
        "templates": [],
        "support_files": [],
    }

    # Load files
    command_files = find_markdown_files(COMMANDS_DIR)
    agent_files = find_markdown_files(AGENTS_DIR)
    skill_files = find_markdown_files(SKILLS_DIR, exclude_support=True)
    support_skill_files = find_support_files(SKILLS_DIR)
    template_files = find_markdown_files(TEMPLATES)

    commands: Dict[str, Path] = {}
    agents: Dict[str, Path] = {}
    skills: Dict[str, Path] = {}
    templates: Dict[str, Path] = {}
    support_files: Dict[str, Path] = {}

    for p in command_files:
        fm, body = load_frontmatter(p)
        name = p.stem
        commands[name] = p
        stats["commands"].append({"name": name, "lines": len(body.splitlines()), "deprecated": is_deprecated(fm, body)})

    for p in agent_files:
        fm, body = load_frontmatter(p)
        name = fm.get("name") or p.stem
        agents[name] = p
        stats["agents"].append({
            "name": name,
            "lines": len(body.splitlines()),
            "deprecated": is_deprecated(fm, body),
            "tools": fm.get("tools", []),
            "skills": fm.get("skills", []),
        })

    for p in skill_files:
        fm, body = load_frontmatter(p)
        name = fm.get("name") or p.stem
        skills[name] = p
        stats["skills"].append({"name": name, "lines": len(body.splitlines()), "deprecated": is_deprecated(fm, body)})

    for p in support_skill_files:
        rel = str(p.relative_to(SKILLS_DIR))
        basename = p.name
        support_files[rel] = p
        support_files[basename] = p  # also index by filename for template lookup
        stats["support_files"].append({"path": rel, "lines": len(p.read_text(encoding="utf-8").splitlines())})

    for p in template_files:
        name = p.name
        templates[name] = p
        stats["templates"].append({"name": name, "lines": len(p.read_text(encoding="utf-8").splitlines())})

    command_names = set(commands.keys())
    agent_names = set(agents.keys())
    skill_names = set(skills.keys())
    template_names = set(templates.keys())
    support_names = set(support_files.keys())

    # 1. Missing templates referenced by skills/commands/agents
    all_template_refs: Dict[str, Set[str]] = defaultdict(set)
    for p in command_files:
        fm, body = load_frontmatter(p)
        for r in extract_template_refs(body):
            all_template_refs[p.name].add(r)
    for p in agent_files:
        fm, body = load_frontmatter(p)
        for r in extract_template_refs(body):
            all_template_refs[p.name].add(r)
    for p in skill_files:
        fm, body = load_frontmatter(p)
        for r in extract_template_refs(body):
            all_template_refs[p.name].add(r)

    for source, refs in all_template_refs.items():
        for ref in refs:
            filename = ref.replace("templates/", "")
            if filename not in template_names and filename not in support_names:
                issues.append(("missing_template", f"{source} references `{ref}` but file does not exist in templates/ or skill support dirs"))
            elif filename in support_names and filename not in template_names:
                issues.append(("template_path_mismatch", f"{source} references `{ref}` but file only exists under `.claude/skills/*/templates/{filename}`"))

    # 2. Missing skills referenced by commands/agents/skills
    all_skill_refs: Dict[str, Set[str]] = defaultdict(set)
    for p in list(command_files) + list(agent_files) + list(skill_files):
        fm, body = load_frontmatter(p)
        source = p.name if p in command_files else (fm.get("name") or p.stem)
        refs = set(fm.get("skills", []) or [])
        # Also check explicit .claude/skills/<name> and `/profile-*`, `/article-*`, `/workflow-*` slash-skill references
        refs.update(re.findall(r"\.claude/skills/([a-z0-9-]+)", body))
        refs.update(re.findall(r"`/((?:profile|article|workflow)-[a-z0-9-]+)`", body))
        for r in refs:
            if r not in skill_names:
                all_skill_refs[source].add(r)

    for source, refs in all_skill_refs.items():
        for r in refs:
            issues.append(("missing_skill", f"{source} references skill `{r}` but no SKILL.md found"))

    # 3. Missing agents referenced by commands/skills
    all_agent_refs: Dict[str, Set[str]] = defaultdict(set)
    for p in list(command_files) + list(skill_files):
        fm, body = load_frontmatter(p)
        source = p.name if p in command_files else (fm.get("name") or p.stem)
        refs = set(re.findall(r"[Ss]pawn\s+\*\*([a-z][a-z0-9-]+)\*\*", body))
        for r in refs:
            if r not in agent_names:
                all_agent_refs[source].add(r)

    for source, refs in all_agent_refs.items():
        for r in refs:
            issues.append(("missing_agent", f"{source} references agent `{r}` but file does not exist"))

    # 4. Missing scripts referenced in skills/agents
    for p in list(agent_files) + list(skill_files) + list(support_skill_files):
        fm, body = load_frontmatter(p)
        source = fm.get("name") or str(p.relative_to(ROOT))
        for script_ref in set(re.findall(r"(?<![a-zA-Z0-9_./-])(scripts/[a-zA-Z0-9_./-]+\.py)", body)):
            if not (ROOT / script_ref).exists():
                issues.append(("missing_script", f"{source} references `{script_ref}` but file does not exist"))

    # 5. Deprecated files still referenced by active files
    deprecated_commands = {s["name"] for s in stats["commands"] if s["deprecated"]}
    deprecated_agents = {s["name"] for s in stats["agents"] if s["deprecated"]}
    deprecated_skills = {s["name"] for s in stats["skills"] if s["deprecated"]}

    for p in command_files:
        name = p.stem
        if name in deprecated_commands:
            continue
        fm, body = load_frontmatter(p)
        for ref in deprecated_commands:
            # Match the deprecated command path, but not when it is a prefix of a longer command name
            if re.search(rf"/{re.escape(ref)}(?![a-zA-Z0-9_-])", body):
                issues.append(("deprecated_ref", f"active command {name} references deprecated command `/{ref}`"))
        for ref in deprecated_agents:
            if ref in extract_agent_refs(body, agent_names):
                issues.append(("deprecated_ref", f"active command {name} references deprecated agent `{ref}`"))
        for ref in deprecated_skills:
            if ref in extract_skill_refs(body, skill_names):
                issues.append(("deprecated_ref", f"active command {name} references deprecated skill `{ref}`"))

    for p in agent_files:
        fm, body = load_frontmatter(p)
        name = fm.get("name") or p.stem
        if name in deprecated_agents:
            continue
        for ref in deprecated_skills:
            if ref in extract_skill_refs(body, skill_names) or ref in fm.get("skills", []):
                issues.append(("deprecated_ref", f"active agent {name} references deprecated skill `{ref}`"))

    # 6. Thin content warning (active files < 50 lines)
    thin_threshold = 50
    for s in stats["commands"]:
        if not s["deprecated"] and s["lines"] < thin_threshold:
            issues.append(("thin_command", f"active command `{s['name']}` is only {s['lines']} lines"))
    for s in stats["agents"]:
        if not s["deprecated"] and s["lines"] < thin_threshold:
            issues.append(("thin_agent", f"active agent `{s['name']}` is only {s['lines']} lines"))
    for s in stats["skills"]:
        if not s["deprecated"] and s["lines"] < thin_threshold:
            issues.append(("thin_skill", f"active skill `{s['name']}` is only {s['lines']} lines"))

    # 7. Orphan templates (exist but not referenced in commands/agents/skills/docs)
    referenced_filenames = set()
    for refs in all_template_refs.values():
        for ref in refs:
            referenced_filenames.add(ref.replace("templates/", ""))
    # Also collect bare artifact-name references like `image-plan.md` from runtime files and docs
    scan_files = list(command_files) + list(agent_files) + list(skill_files)
    if DOCS.exists():
        scan_files.extend(p for p in DOCS.rglob("*.md") if p.is_file())
    for p in scan_files:
        fm, body = load_frontmatter(p)
        for m in re.findall(r"`([a-zA-Z0-9_./-]+\.md)`", body):
            referenced_filenames.add(Path(m).name)
    for t in template_names:
        if t not in referenced_filenames:
            issues.append(("orphan_template", f"template `{t}` exists but is not referenced anywhere"))

    # 8. Frontmatter issues
    for p in agent_files:
        fm, body = load_frontmatter(p)
        name = fm.get("name")
        if not name:
            issues.append(("frontmatter", f"agent file {p.name} missing `name` in frontmatter"))
        if "description" not in fm:
            issues.append(("frontmatter", f"agent {name or p.name} missing `description`"))
        if "tools" not in fm:
            issues.append(("frontmatter", f"agent {name or p.name} missing `tools`"))
        if "model" not in fm:
            issues.append(("frontmatter", f"agent {name or p.name} missing `model`"))
        if fm.get("skills") and "Skill" not in fm.get("tools", []):
            issues.append(("frontmatter", f"agent {name or p.name} lists skills but `Skill` tool not declared in tools"))

    for p in command_files:
        fm, body = load_frontmatter(p)
        if "description" not in fm:
            issues.append(("frontmatter", f"command {p.name} missing `description`"))

    # 9. Duplicate names
    seen_names: Dict[str, int] = defaultdict(int)
    for name in agents:
        seen_names[name] += 1
    for name, count in seen_names.items():
        if count > 1:
            issues.append(("duplicate_name", f"agent name `{name}` used {count} times"))

    # 10. State/workflow consistency
    required_workflow = [
        "profile-discover", "profile-answer", "article-cluster",
        "profile-research-deep", "profile-lock", "article-intent-research",
        "article-benchmark", "article-benchmark-extract",
        "article-evidence-opinions", "article-skeleton", "article-arc", "article-draft",
        "article-truth-qa", "article-information-gain-qa", "article-benchmark-qa",
        "article-reader-qa", "article-repair", "article-enrich", "article-visual", "article-resources", "article-faq", "article-publish-pack",
        "article-review", "article-next", "workflow-status", "workflow-next", "workflow-rollback"
    ]
    # In skill-only projects, a matching skill satisfies the workflow item.
    skill_only_mode = not COMMANDS_DIR.exists() or len(command_files) == 0
    for cmd in required_workflow:
        exists_as_command = cmd in command_names
        exists_as_skill = cmd in skill_names
        if skill_only_mode:
            if not exists_as_skill and not exists_as_command:
                issues.append(("workflow_gap", f"required workflow item `/{cmd}` has no command or skill file"))
        else:
            if not exists_as_command:
                issues.append(("workflow_gap", f"required workflow command `/{cmd}` has no file"))

    # 11. Stop-block & anti-skip enforcement across skills
    for p in skill_files:
        fm, body = load_frontmatter(p)
        name = fm.get("name") or p.stem
        if "跳过 — 跳过此阶段" in body or "Skip — skip this stage" in body:
            issues.append(("skip_stage_prompt", f"skill `{name}` still contains a skip-stage prompt"))

    # 12. Workspace state.json schema compliance
    schema_path = CONFIG / "state-schema.json"
    workspaces_dir = ROOT / "content-workspace"
    if schema_path.exists() and workspaces_dir.exists():
        import json as _json
        sys.path.insert(0, str(ROOT / "scripts"))
        from workflow_status import validate_state  # noqa: E402
        for state_file in sorted(workspaces_dir.glob("*/state.json")):
            try:
                state_data = _json.loads(state_file.read_text(encoding="utf-8"))
                err = validate_state(state_data, schema_path)
                if err:
                    issues.append(("workspace_state_schema", f"{state_file.relative_to(ROOT)}: {err}"))
            except Exception as exc:
                issues.append(("workspace_state_schema", f"{state_file.relative_to(ROOT)}: invalid JSON ({exc})"))

    # 13. Workspace project-profile.json schema compliance
    profile_schema_path = CONFIG / "profile-schema.json"
    if profile_schema_path.exists() and workspaces_dir.exists():
        import json as _json
        sys.path.insert(0, str(ROOT / "scripts"))
        from workflow_status import validate_state  # noqa: E402
        for prof_file in sorted(workspaces_dir.glob("*/project-profile.json")):
            try:
                prof_data = _json.loads(prof_file.read_text(encoding="utf-8"))
                err = validate_state(prof_data, profile_schema_path)
                if err:
                    issues.append(("workspace_profile_schema", f"{prof_file.relative_to(ROOT)}: {err}"))
            except Exception as exc:
                issues.append(("workspace_profile_schema", f"{prof_file.relative_to(ROOT)}: invalid JSON ({exc})"))

    # Print report
    print("=" * 70)
    print("B2B SEO Agent System — Deep Audit Report")
    print("=" * 70)
    print()
    print(f"Commands: {len(command_files)} | Agents: {len(agent_files)} | Skills: {len(skill_files)} | Templates: {len(template_files)} | Skill support files: {len(support_skill_files)}")
    print(f"Deprecated commands: {len(deprecated_commands)} | agents: {len(deprecated_agents)} | skills: {len(deprecated_skills)}")
    print(f"Total issues found: {len(issues)}")
    print()

    categories = defaultdict(list)
    for cat, msg in issues:
        categories[cat].append(msg)

    for cat in sorted(categories):
        msgs = categories[cat]
        print(f"\n## {cat.upper().replace('_', ' ')} ({len(msgs)})")
        for msg in msgs:
            print(f"- {msg}")

    print("\n" + "=" * 70)
    print("Stats by file type (active + deprecated)")
    print("=" * 70)
    for kind in ["commands", "agents", "skills", "templates"]:
        print(f"\n{kind.upper()}:")
        for item in sorted(stats[kind], key=lambda x: x["lines"]):
            dep = " [DEPRECATED]" if item.get("deprecated") else ""
            print(f"  {item['lines']:4d} lines  {item['name']}{dep}")

    if stats["support_files"]:
        print("\nSKILL SUPPORT FILES (templates/examples/references):")
        for item in sorted(stats["support_files"], key=lambda x: x["lines"]):
            print(f"  {item['lines']:4d} lines  {item['path']}")


if __name__ == "__main__":
    main()
