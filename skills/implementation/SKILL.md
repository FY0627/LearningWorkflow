---
name: implementation
description: >-
  Execute an explicitly approved implementation plan and coordinate authorized tasks.
  Use after human approval when source changes, task delegation, verification, and
  mid-execution change control must stay within the approved revision and scope.
---

# Implementation

## Workflow

1. Read the supplied plan and approval evidence, including user-provided inputs. Verify the identifiable revision, authorized scope, task contracts, acceptance checks, and prerequisites; their originating skill or document format is not a prerequisite. Do not ask again when authority is valid. Resolve missing planning facts or authority before affected work, using the relevant planning or approval skill when available.
2. Before dispatch and when code state changes, compare the plan's source baseline and audit scope with current code. Track expected changes from approved tasks separately from unplanned changes. A repository revision difference alone does not invalidate every task.
3. Establish and verify required checkpoints or other execution prerequisites before affected modifications.
4. Choose execution order from the approved task dependencies. Use subagents for bounded tasks that benefit from parallel execution when runtime support and authority permit; otherwise work sequentially. Give each assignment its task ID, plan revision, contracts, dependencies, allowed scope, and self-checks. The main agent coordinates shared interfaces, checks returned changes and evidence, and resolves integration conflicts within the approved contracts. Agent count follows the work.
5. Distinguish status questions and clarifications that preserve the execution basis from feedback that changes it. Answer the former while continuing authorized work. For changed execution premises or unplanned source changes, pause only affected and unknown-impact tasks and child agents. Record completed, active, and unstarted work; confirm paused agents have actually stopped before using their results.
6. Resolve evidence gaps through `report-source` and `codebase-audit-summary`, and material changes to functionality, scope, acceptance, effects, or premises through `implementation-plan` and `human-approval`, when available. If a required skill is unavailable, perform the scoped investigation and prepare the necessary plan revision directly, preserving stable task IDs and prior authorization. Present changed scope, effects, acceptance checks, and prerequisites to the user; obtain and record explicit approval of the revised version and scope before executing work that changes the authorization basis. Continue proven-unaffected work only under Change Control. Missing skill files neither block these responsibilities nor waive renewed approval.
7. Run relevant implementation self-checks and repair failures within the approved scope. Record actual evidence and assess Code Delivery Readiness before handing off. Self-checks support downstream review; they do not establish full user-journey acceptance, visual acceptance, security audit, CI gate, release, or closeout results.

## Specialist Skill Use

- Before implementing a task, inspect the available installed skill
  descriptions for an applicable specialist method. Read and apply a matching
  skill before choosing an ad hoc implementation approach. Determine
  applicability from the task, project context, and the skill's scope.
- When no applicable installed skill is available, implement the task using
  project conventions, source evidence, and available tools. A missing skill
  alone is not a blocker; identify any actual missing information, permission,
  or tool needed to proceed.
- If an applicable skill cannot be used, report the concrete limitation
  and use an equivalent approach when authorized and feasible. Preserve
  the task's requirements and disclose any verification gaps.
- Implementation owns execution organization and code delivery. Specialist
  skills supply methods for bounded work; applying them neither transfers
  overall responsibility nor expands the approved scope or permissions.
- Loading a skill means reading and applying its instructions. Delegating
  means assigning bounded work to another agent. Either the main agent or
  an authorized child agent may apply a skill; loading one does not require
  or authorize delegation.
- Apply this selection rule explicitly. Do not assume that the host
  automatically prioritizes specialist skills.

## Change Control

- Continue an unaffected task only when the original approval still covers it and its goal, contracts, shared dependencies, acceptance checks, material effects, and prerequisites remain unchanged. Disjoint file names alone do not prove independence.
- Hold a task when impact cannot be established. Never extend old approval to revised work.
- Routine implementation choices within the approved scope do not need command-by-command approval.

## Code Delivery Readiness

- Complete the approved implementation and run the relevant self-checks.
  Diagnose and repair defects that prevent the approved work from meeting
  its requirements; do not hand known-defective work to the user as a
  completed deliverable.
- If necessary information, permissions, or tools prevent further progress,
  report the specific blocker and what is needed to proceed. Keep the work
  incomplete; a blocker report is not code delivery.
- An existing issue does not block code delivery only when evidence shows
  that it predates the changes and does not compromise the approved work
  or its dependencies. Disclose the issue, impact, and verification limits.
  Investigate uncertain impact before declaring readiness.
- Code delivery readiness does not establish downstream acceptance,
  security, CI, release, or project completion.

## Handoff

- When code delivery is ready, pass the delivery materials to the next
  applicable node under the active plan and workflow. If its skill,
  prerequisites, authority, and runtime support are available, read it and
  continue without a separate permission question. The same agent may
  perform the next role.
- If no downstream skill is available, deliver the code, self-check evidence,
  limitations, and recommended follow-up verification directly to the user.
  State which downstream work remains unperformed; do not claim workflow
  completion or a handoff that did not occur.
- On downstream failure evidence, identify the affected candidate and tasks,
  diagnose and repair defects within existing authorization, rerun relevant
  self-checks, and return the updated candidate and evidence for rechecking.
  Changes to requirements, scope, material effects, or approved solution
  premises follow Change Control and renewed planning and approval.

## Output Contract

Provide a concise delivery summary, linking existing artifacts where possible:

- Plan revision and authorized scope; completed and held task IDs.
- Candidate code location and comparable revision or snapshot, including
  relevant uncommitted changes; actual changes and integration status.
- Self-check commands or procedures, environment, observed results, and
  evidence locations; failed or unrun checks and their impact.
- Known issues, evidence for any pre-existing issue classification, blockers,
  plan deviations, renewed approvals, and the recovery entry point.
- Code delivery readiness, next node or standalone follow-up recommendations,
  actual handoff status, and the information needed to inspect and check
  the candidate.

Write user-facing content in the user's language.
