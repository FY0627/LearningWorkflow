#!/usr/bin/env python3
"""Validate the skill pack: structure, three-way consistency, maturity tiers, privacy.

Stdlib only. Exits 1 on any ERROR so it can gate CI.

Usage:
    python scripts/validate-pack.py [repo_root]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

REQUIRED_FILES = [
    "README.md",
    "README.zh-CN.md",
    "AGENTS.md",
    "LICENSE",
    "VERSION",
    "CHANGELOG.md",
    "skill-pack.json",
    "docs/workflow.md",
    "docs/workflow.zh-CN.md",
    "docs/workflow-fidelity.md",
    "docs/skill-authoring-standard.md",
    "docs/compatibility.md",
    "docs/trigger-tuning.md",
    "docs/release-checklist.md",
    "docs/skill-template/SKILL.md",
    "examples/dry-runs.md",
    "examples/usage-benchmark.md",
    "scripts/install.ps1",
    ".github/workflows/validate.yml",
]

VALID_STATUSES = ("draft", "beta", "stable")

# Node ids in the workflow graph that intentionally carry no skill.
CONTROL_FLOW_NODES = {"START", "DECISION"}

SKILL_MD_MAX_LINES = 220

# (min_description_chars, min_body_lines) per maturity tier.
TIER_MINIMUMS = {
    "draft": (20, 0),
    "beta": (60, 40),
    "stable": (120, 40),
}
DESCRIPTION_MAX_CHARS = 500

# Beta and above must be English-primary (see docs/compatibility.md).
MIN_ASCII_RATIO = 0.70

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

# Node definitions inside the mermaid block: ID["label"] or ID{"label"}.
MERMAID_NODE_RE = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*[\[{]\"([^\"]*)\"[\]}]")
TRAILING_SLUG_RE = re.compile(r"\(([a-z0-9]+(?:-[a-z0-9]+)*)\)\s*$")

BLOCK_SCALAR_MARKERS = {">", ">-", ">+", "|", "|-", "|+"}

PRIVACY_PATTERNS = [
    (
        re.compile(r"[A-Za-z]:\\Users\\(?!<|%|Public\b|Default\b)[A-Za-z0-9._-]+"),
        "absolute Windows user profile path (use <User> or %USERPROFILE%)",
    ),
    (
        re.compile(r"/(?:home|Users)/(?!<)[A-Za-z0-9._-]+"),
        "absolute POSIX home path (use <User> or $HOME)",
    ),
    (
        re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
        "email address",
    ),
    (
        re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{16,}|sk-[A-Za-z0-9]{20,})\b"),
        "credential or API token",
    ),
]

SCANNED_SUFFIXES = {".md", ".json", ".ps1", ".py", ".yaml", ".yml", ".txt"}

PLACEHOLDER_MARKERS = ("<", ">", "your-", "yourname", "example.com", "/Frank/", "USERNAME")


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: str, message: str) -> None:
        self.errors.append(f"ERROR: {where}: {message}")

    def warn(self, where: str, message: str) -> None:
        self.warnings.append(f"WARN:  {where}: {message}")


# --------------------------------------------------------------------------
# Minimal YAML frontmatter parser (stdlib only, scalars and block scalars)
# --------------------------------------------------------------------------


def parse_frontmatter(text: str) -> tuple[dict[str, str] | None, str | None]:
    """Return (fields, error). Supports `key: value` and `key: >-` block scalars."""
    lines = text.split("\n")
    if not lines or lines[0].rstrip() != "---":
        return None, "must start with a '---' frontmatter fence"

    end = -1
    for i in range(1, len(lines)):
        if lines[i].rstrip() == "---":
            end = i
            break
    if end < 0:
        return None, "frontmatter fence is never closed"

    fields: dict[str, str] = {}
    key: str | None = None
    parts: list[str] = []
    literal = False

    def flush() -> None:
        nonlocal key, parts
        if key is not None:
            joined = "\n".join(parts) if literal else " ".join(p for p in parts if p)
            fields[key] = joined.strip()
        key, parts = None, []

    for raw in lines[1:end]:
        stripped = raw.strip()
        is_continuation = raw[:1] in (" ", "\t") or not stripped
        if key is not None and is_continuation:
            parts.append(stripped)
            continue

        match = re.match(r"^([A-Za-z0-9_.-]+):\s*(.*)$", raw)
        if not match:
            return None, f"cannot parse frontmatter line: {raw!r}"

        flush()
        name, value = match.group(1), match.group(2).strip()
        if value in BLOCK_SCALAR_MARKERS:
            key, parts, literal = name, [], value.startswith("|")
        else:
            fields[name] = value.strip("\"'")

    flush()
    return fields, None


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------


def check_required_files(root: Path, report: Report) -> None:
    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            report.error(rel, "required file is missing")


def load_manifest(root: Path, report: Report) -> dict | None:
    path = root / "skill-pack.json"
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.error("skill-pack.json", f"is not valid JSON: {exc}")
        return None

    for field in ("name", "version", "description", "license", "repository", "skills"):
        if not data.get(field):
            report.error("skill-pack.json", f"missing required field {field!r}")

    repository = str(data.get("repository", ""))
    if repository:
        if not repository.startswith("https://github.com/"):
            report.error("skill-pack.json", "repository must be an https://github.com/ URL")
        elif any(marker in repository for marker in PLACEHOLDER_MARKERS):
            report.error(
                "skill-pack.json",
                f"repository still contains a placeholder: {repository!r}",
            )

    floor = data.get("maturity_floor")
    if not isinstance(floor, dict):
        report.error("skill-pack.json", "missing required field 'maturity_floor'")
    else:
        for tier in ("beta", "stable"):
            if not isinstance(floor.get(tier), int):
                report.error("skill-pack.json", f"maturity_floor.{tier} must be an integer")

    if not isinstance(data.get("privacy"), dict):
        report.error("skill-pack.json", "missing required field 'privacy'")

    return data


def check_version_sync(root: Path, manifest: dict, report: Report) -> None:
    path = root / "VERSION"
    if not path.is_file():
        return
    version_file = path.read_text(encoding="utf-8").strip()
    manifest_version = str(manifest.get("version", "")).strip()
    if version_file != manifest_version:
        report.error(
            "VERSION",
            f"is {version_file!r} but skill-pack.json declares {manifest_version!r}",
        )


def check_license_present(root: Path, manifest: dict, report: Report) -> None:
    if manifest.get("license") and not (root / "LICENSE").is_file():
        report.error(
            "LICENSE",
            f"skill-pack.json declares license {manifest['license']!r} but no LICENSE file exists",
        )


def workflow_slugs(root: Path, report: Report) -> set[str]:
    """Extract skill slugs from the trailing `(slug)` of every mermaid node label."""
    path = root / "docs" / "workflow.md"
    if not path.is_file():
        return set()

    text = path.read_text(encoding="utf-8")
    block = re.search(r"```mermaid\n(.*?)```", text, re.DOTALL)
    if not block:
        report.error("docs/workflow.md", "contains no ```mermaid code block")
        return set()

    slugs: set[str] = set()
    for node_id, label in MERMAID_NODE_RE.findall(block.group(1)):
        match = TRAILING_SLUG_RE.search(label)
        if node_id in CONTROL_FLOW_NODES:
            if match:
                report.error(
                    "docs/workflow.md",
                    f"control-flow node {node_id} must not carry a skill slug",
                )
            continue
        if not match:
            report.error(
                "docs/workflow.md",
                f"node {node_id} label does not end with a '(skill-slug)': {label!r}",
            )
            continue
        slug = match.group(1)
        if slug in slugs:
            report.error("docs/workflow.md", f"skill slug {slug!r} appears on more than one node")
        slugs.add(slug)
    return slugs


def check_three_way_consistency(
    root: Path, manifest: dict, graph: set[str], report: Report
) -> None:
    """The workflow graph, the manifest, and the skills/ directory must agree exactly."""
    declared = {
        entry.get("name", "")
        for entry in manifest.get("skills", [])
        if isinstance(entry, dict)
    }
    skills_dir = root / "skills"
    on_disk = (
        {p.name for p in skills_dir.iterdir() if p.is_dir()} if skills_dir.is_dir() else set()
    )

    for label, left, right in (
        ("declared in skill-pack.json but absent from skills/", declared, on_disk),
        ("present in skills/ but not declared in skill-pack.json", on_disk, declared),
        ("declared in skill-pack.json but absent from docs/workflow.md", declared, graph),
        ("in docs/workflow.md but not declared in skill-pack.json", graph, declared),
    ):
        for name in sorted(left - right):
            report.error("three-way consistency", f"{name!r} is {label}")


def check_skill(root: Path, entry: dict, dry_runs: str, report: Report) -> str | None:
    """Validate one manifest skill entry. Returns its status when valid."""
    name = entry.get("name", "")
    where = f"skills/{name or '?'}"

    if not name or not SLUG_RE.match(name):
        report.error("skill-pack.json", f"skill name {name!r} is not a valid kebab-case slug")
        return None

    status = entry.get("status", "")
    if status not in VALID_STATUSES:
        report.error(where, f"status {status!r} must be one of {VALID_STATUSES}")
        return None

    expected_path = f"skills/{name}"
    if entry.get("path") != expected_path:
        report.error("skill-pack.json", f"{name}: path should be {expected_path!r}")

    skill_md = root / "skills" / name / "SKILL.md"
    if not skill_md.is_file():
        report.error(f"{where}/SKILL.md", "is missing")
        return status

    text = skill_md.read_text(encoding="utf-8")
    fields, parse_error = parse_frontmatter(text)
    if fields is None:
        report.error(f"{where}/SKILL.md", parse_error or "unparseable frontmatter")
        return status

    extra = set(fields) - {"name", "description"}
    if extra:
        report.error(
            f"{where}/SKILL.md",
            f"frontmatter must contain only 'name' and 'description'; found extra {sorted(extra)}",
        )

    if fields.get("name") != name:
        report.error(
            f"{where}/SKILL.md",
            f"frontmatter name {fields.get('name')!r} does not match directory {name!r}",
        )

    description = fields.get("description", "").strip()
    min_chars, min_body_lines = TIER_MINIMUMS[status]
    if not description:
        report.error(f"{where}/SKILL.md", "frontmatter has no description")
    else:
        if len(description) < min_chars:
            report.error(
                f"{where}/SKILL.md",
                f"description is {len(description)} chars; {status} requires at least {min_chars}",
            )
        if len(description) > DESCRIPTION_MAX_CHARS:
            report.error(
                f"{where}/SKILL.md",
                f"description is {len(description)} chars; maximum is {DESCRIPTION_MAX_CHARS}",
            )
        if status in ("beta", "stable"):
            ascii_ratio = sum(c.isascii() for c in description) / len(description)
            if ascii_ratio < MIN_ASCII_RATIO:
                report.error(
                    f"{where}/SKILL.md",
                    f"{status} skills must be English-primary; description is "
                    f"{ascii_ratio:.0%} ASCII, need {MIN_ASCII_RATIO:.0%}",
                )

    lines = text.split("\n")
    if len(lines) > SKILL_MD_MAX_LINES:
        report.error(
            f"{where}/SKILL.md",
            f"is {len(lines)} lines; maximum is {SKILL_MD_MAX_LINES} "
            "(move detail into references/)",
        )

    body = text.split("---", 2)[-1]
    body_lines = [line for line in body.split("\n") if line.strip()]
    if len(body_lines) < min_body_lines:
        report.error(
            f"{where}/SKILL.md",
            f"body has {len(body_lines)} non-blank lines; {status} requires at least {min_body_lines}",
        )

    if status in ("beta", "stable") and "## Workflow" not in body:
        report.error(f"{where}/SKILL.md", f"{status} skills must have a '## Workflow' section")

    if status == "stable":
        for section in ("## Output Contract", "## References"):
            if section not in body:
                report.error(f"{where}/SKILL.md", f"stable skills must have a '{section}' section")

        for placeholder in ("[TODO", "TODO:", "TBD", "FIXME"):
            if placeholder in text:
                report.error(
                    f"{where}/SKILL.md", f"stable skills must not contain {placeholder!r}"
                )

        refs_dir = root / "skills" / name / "references"
        if refs_dir.is_dir():
            for ref in sorted(refs_dir.rglob("*.md")):
                rel = ref.relative_to(root / "skills" / name).as_posix()
                if rel not in text:
                    report.error(
                        f"{where}/{rel}",
                        "reference file is never linked from SKILL.md (orphan)",
                    )

        if name not in dry_runs:
            report.error(
                "examples/dry-runs.md",
                f"stable skill {name!r} has no dry-run case",
            )

    return status


def check_ratchet(manifest: dict, statuses: list[str], report: Report) -> None:
    floor = manifest.get("maturity_floor")
    if not isinstance(floor, dict):
        return
    counts = {tier: statuses.count(tier) for tier in VALID_STATUSES}
    # stable also satisfies a beta floor.
    achieved = {"beta": counts["beta"] + counts["stable"], "stable": counts["stable"]}
    for tier in ("beta", "stable"):
        required = floor.get(tier)
        if isinstance(required, int) and achieved[tier] < required:
            report.error(
                "maturity ratchet",
                f"{achieved[tier]} skill(s) at {tier}+ but maturity_floor.{tier} "
                f"requires {required}; quality must not regress",
            )


def check_privacy(root: Path, report: Report) -> None:
    this_file = Path(__file__).resolve()
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in SCANNED_SUFFIXES:
            continue
        if ".git" in path.parts or path.resolve() == this_file:
            continue
        rel = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            report.warn(rel, "could not be read as UTF-8; skipped privacy scan")
            continue
        for pattern, label in PRIVACY_PATTERNS:
            match = pattern.search(text)
            if match:
                line_no = text[: match.start()].count("\n") + 1
                report.error(f"{rel}:{line_no}", f"{label}: {match.group(0)!r}")


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------


def main(argv: list[str]) -> int:
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")

    root = Path(argv[1] if len(argv) > 1 else ".").resolve()
    if not root.is_dir():
        print(f"ERROR: {root} is not a directory")
        return 1

    report = Report()
    check_required_files(root, report)

    manifest = load_manifest(root, report)
    statuses: list[str] = []
    if manifest is not None:
        check_version_sync(root, manifest, report)
        check_license_present(root, manifest, report)
        check_three_way_consistency(root, manifest, workflow_slugs(root, report), report)

        dry_runs_path = root / "examples" / "dry-runs.md"
        dry_runs = dry_runs_path.read_text(encoding="utf-8") if dry_runs_path.is_file() else ""

        for entry in manifest.get("skills", []):
            if not isinstance(entry, dict):
                report.error("skill-pack.json", f"skills[] entry is not an object: {entry!r}")
                continue
            status = check_skill(root, entry, dry_runs, report)
            if status:
                statuses.append(status)

        check_ratchet(manifest, statuses, report)

    check_privacy(root, report)

    for line in report.warnings:
        print(line)
    for line in report.errors:
        print(line)

    counts = {tier: statuses.count(tier) for tier in VALID_STATUSES}
    print(
        f"\n{len(statuses)} skill(s): "
        + ", ".join(f"{counts[tier]} {tier}" for tier in VALID_STATUSES)
    )
    if report.errors:
        print(f"FAILED: {len(report.errors)} error(s), {len(report.warnings)} warning(s)")
        return 1
    print(f"OK: 0 errors, {len(report.warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
