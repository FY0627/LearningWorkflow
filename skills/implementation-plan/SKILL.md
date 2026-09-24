---
name: implementation-plan
description: >-
  Convert requirements, diagnosis, and current code evidence into a versioned implementation
  plan for human review. Use before code changes when task boundaries, dependencies,
  acceptance checks, and recovery readiness must be explicit.
---

# Implementation Plan

## Workflow

1. Gather the relevant requirements, root-cause analysis, and codebase audit. For changes to existing code, require an audit covering the proposed scope, a comparable source baseline including relevant uncommitted changes, evidence locations, and a comparison with current code. A settled feature request alone is not code evidence.
2. If the audit is missing, stale, or not comparable, return to `report-source` and `codebase-audit-summary`. Reinspect changes since a known baseline and their affected consumers. Without a baseline, reinvestigate the task and dependency scope. Expand the investigation when shared dependencies are found.
3. Write stable task IDs. For each task, state the goal, input and output contracts, proposed file or component scope, shared interfaces or state, dependencies, acceptance checks, and execution prerequisites. Mark which tasks may run in parallel and why.
4. Treat a missing dependency as unknown, never as independent. Continue investigation when a material dependency remains unknown; do not hand the plan to `human-approval` yet.
5. State the result, scope and exclusions, material effects, verification, and recovery readiness. Distinguish a verified existing checkpoint, a checkpoint still to prepare, and a justified not-applicable case. A Git repository alone is not a saved checkpoint.
6. On implementation feedback, classify affected, downstream, unaffected, and unknown-impact tasks against their contracts. Revise only affected work, preserve stable IDs and existing authorization for unchanged tasks, and version the revised plan.
7. When the plan and review summary are complete, load and follow `human-approval` in the same task when available. Hand over the plan location, version, and summary without a separate permission question. If unavailable, provide the plan entry point and keep implementation stopped.

## Boundaries

- Produce a Markdown plan only; do not change source code or create backups or commits merely to finish planning.
- A planning handoff does not authorize child agents or implementation. Do not skip review because an action appears reversible.
- Requirement changes return to intent or requirements work. Local solution revisions return to this plan without repeating unrelated upstream work.

## Output Contract

Produce `implementation_plan.md` with a revision identifier; goals and scope; referenced evidence and code baseline; task contracts, dependencies, and independence reasons; acceptance and verification; material effects; prerequisites; and recovery readiness. Provide a concise review summary. Write user-facing content in the user's language.
