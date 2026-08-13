# Changelog

All notable changes to this project are documented here.

## 0.1.0

First versioned state. This release establishes the framework; skill content is
deliberately out of scope and every skill remains at `draft`.

Version was set to `0.1.0` rather than kept at the previously declared `1.0.0`. Twenty-four
draft skills and a validator that had never gated anything is not a 1.0.

### Added

- `scripts/validate-pack.py`, rewritten from scratch. Stdlib only, `raise SystemExit(main())`.
  Checks: required files, manifest schema and placeholder detection, `VERSION`/manifest
  version sync, declared-license-requires-LICENSE, three-way consistency between the
  workflow graph and the manifest and the `skills/` directory, per-tier skill rules, the
  maturity ratchet, and a privacy scan for user paths, home paths, emails, and tokens.
  Frontmatter is parsed as YAML rather than substring-matched.
- `.github/workflows/validate.yml` — runs the validator on `windows-latest` with Python
  3.12 on every push and pull request, plus a PowerShell parse check and an installer dry
  run.
- Maturity tiers (`draft`/`beta`/`stable`) and `maturity_floor` in `skill-pack.json`, so
  quality cannot regress once gained.
- `docs/workflow-fidelity.md` and its Chinese mirror — node-by-node provenance with the
  labels `replicated` (14), `inferred` (11), `original` (1), the evidence for each, and
  four explicitly declared design decisions.
- `docs/skill-authoring-standard.md`, `docs/compatibility.md`, `docs/trigger-tuning.md`,
  `docs/release-checklist.md`.
- `examples/dry-runs.md` and `examples/usage-benchmark.md` — a 7-criterion 0-2 rubric with
  a stated bar of 11/14, and three evidence labels that forbid presenting a designed
  example as a real run.
- `README.md` / `README.zh-CN.md`, `AGENTS.md`, `LICENSE` (MIT), `CHANGELOG.md`,
  `.gitignore`, `.gitattributes`.

### Changed

- Repository restructured: `.agents/skills/` to `skills/`, `.agents/scripts/` to `scripts/`,
  and `.agents/{VERSION,skill-pack.json}` to the repository root. A portfolio repository
  should not hide its contents in a dot-directory.
- `Frank_Agentic_Workflow.md` became `docs/workflow.md`, rewritten English-primary with
  `docs/workflow.zh-CN.md` as the Chinese mirror.
- Every skill-bearing node label now ends with `(skill-slug)`. This is a machine contract:
  the validator parses these to enforce three-way consistency.
- `skill-pack.json` schema upgraded — `skills[]` is now objects with `name`, `path`,
  `status`, and `description`; added `docs[]`, `maturity_floor`, `privacy`, and `workflow`.
  `repository` now points at the real repository; `author` no longer credits the tool that
  generated the first draft.
- `scripts/install.ps1` rewritten: `-Target claude|codex|gemini|all`, `-WhatIf` dry run via
  `SupportsShouldProcess`, `-LiteralPath` throughout, and it now throws rather than silently
  skipping when a skill already exists. Previously it installed only to
  `~/.gemini/config/skills`, which meant Claude Code could not discover any skill in this pack.
- `docs/skill-template/` moved out of `skills/`. It is an authoring template, not an
  installable skill, and the installer was previously copying it into users' skill
  directories.

### Fixed

- **Manifest drift.** The repository had 28 skill directories against 24 declarations, and
  the four undeclared ones were the better-written half. Resolved by keeping the slug the
  workflow graph uses and absorbing the richer body:
  - `codebase-audit` (37 lines of real content) merged into `codebase-audit-summary`
    (9-line stub that held the manifest slot).
  - `subagents-dispatch` merged into `subagents-overview`.
  - `knowledge-accumulation` merged into `agents-md`.
- **Node/skill count mismatch.** 24 declared skills pointed at 23 skill-bearing nodes,
  because `e2e-verify` and `visual-e2e-verify` shared one node. Split into visual
  acceptance and end-to-end acceptance.
- **`security-audit` was chained after `production-deployment-gate`**, which audits software
  that has already passed its release gate. Corrected to a fork from `github-actions-ci`,
  matching the source workflow's rank structure.
- **The parallel section was two straight rails** where the source has a braided
  fan-out/sync/fan-out/sync structure. Corrected; the mid-point sync exists because both
  tracks depend on a stable API surface.
- **Overstated provenance.** Eight nodes were marked as original additions. At least two of
  those positions are occupied in the source. All inline provenance claims were removed and
  replaced with the evidence-based table in `docs/workflow-fidelity.md`.
- **Declared MIT with no LICENSE file.** LICENSE added; the validator now fails if a
  declared license has no file.
- **`AGENTS.md` never existed**, despite two skills whose job is to maintain it.
- **The validator could not fail.** It never called `sys.exit`, so it always exited 0
  regardless of how many errors it printed, and its content checks were two substring
  matches over the whole file.
