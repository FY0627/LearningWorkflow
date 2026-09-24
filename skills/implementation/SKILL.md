---
name: implementation
description: >-
  Execute an explicitly approved implementation plan and coordinate authorized tasks.
  Use after human approval when source changes, task delegation, verification, and
  mid-execution change control must stay within the approved revision and scope.
---

# Implementation

## Workflow

1. Read the approved plan and authorization record. Verify the plan revision, approved task scope, acceptance checks, and pending prerequisites. Return missing or invalid authority to `human-approval`; do not ask again when existing authority is valid.
2. Before dispatch and when code state changes, compare the plan's source baseline and audit scope with current code. Track expected changes from approved tasks separately from unplanned changes. A repository revision difference alone does not invalidate every task.
3. Establish and verify required checkpoints or other execution prerequisites before affected modifications.
4. Execute approved tasks directly or delegate bounded work when the host supports it and prerequisites are met. Give each child agent the task ID, plan revision, input and output contracts, dependencies, acceptance checks, and allowed change scope.
5. On user feedback or unplanned source changes, pause affected and unknown-impact tasks and child agents. Record completed, active, and unstarted work; confirm agents have actually stopped before using their results.
6. Send evidence gaps from unplanned changes to `report-source` and `codebase-audit-summary`, then send affected work to `implementation-plan` for revision and `human-approval` for renewed review. Route material changes to functionality, scope, acceptance, effects, or premises through the same plan and review path.
7. Complete authorized work, verify outcomes, and report results and a concrete recovery entry point.

## Change Control

- Continue an unaffected task only when the original approval still covers it and its goal, contracts, shared dependencies, acceptance checks, material effects, and prerequisites remain unchanged. Disjoint file names alone do not prove independence.
- Hold a task when impact cannot be established. Never extend old approval to revised work.
- Routine implementation choices within the approved scope do not need command-by-command approval.

## Output Contract

Report completed and held task IDs, actual changes, verification results, deviations from the plan, renewed approvals, and available recovery steps or entry points. Distinguish observed results from unrun checks. Write the user-facing report in the user's language.
