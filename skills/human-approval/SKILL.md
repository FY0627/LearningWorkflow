---
name: human-approval
description: >-
  Present a completed implementation plan for human review, record approval of its version
  and scope, and hand off to implementation or plan revision. Invoke when a plan is ready
  or materially revised, and when the operator responds to its review panel.
---

# Human Review and Approval

This is the decision gate between implementation-plan and implementation.
It presents the plan, records the decision, and hands off. It does not author solutions,
implement changes, create recovery tools, or manage unattended delegation.
Reversibility does not exempt an implementation plan from review.

## Inputs

Receive the plan location, identifiable revision, review summary, and any prior approval.
A document revision or content hash is sufficient; a Git commit is not required.
User-provided plans can be reviewed without rerunning the planning skill.

The plan must state the intended result, scope and exclusions, approach, acceptance checks,
material effects, and execution prerequisites. Recovery readiness must distinguish a verified
existing checkpoint from planned preparation, or explain why recovery is not applicable.
Git repository existence alone does not establish that current contents are saved.

## Workflow

1. Load references/authorization-record.md when checking prior approval. If it covers this
   revision and scope, hand off without asking again. Otherwise inspect the plan and summary.
2. Return missing or contradictory decision-relevant information to implementation-plan.
   Do not invent a solution, user choice, recovery guarantee, or successful verification.
3. Load references/approval-panel.md and display the summary, full-plan link, and choices.
   Do not require a separate long report before the panel. Await the operator; silence does
   not start implementation.
4. Process the response:
   - The explicit approval identifier approves the displayed revision and disclosed scope.
   - Concrete adjustment feedback returns to planning; no adjustment identifier is required.
     An adjustment identifier without feedback requires clarification.
   - Answer questions without treating them as approval. Clarify vague assent without the
     approval identifier; do not repeat an unchanged panel to solicit assent.
   - Explicit cancellation ends the review. Waiting is the default, not a third panel option.
5. On approval, load references/authorization-record.md, record authority, and hand the
   plan and record to implementation. No second confirmation is needed for the same scope.
   Execution must satisfy and verify pending prerequisites before affected modifications.
6. On adjustment, hand the current plan and feedback to implementation-plan. Review the
   revised plan when ready. Requirement changes may require upstream clarification.

## Scope and validity

Approval covers the identified plan and its disclosed effects, not future work with the same
title. Changes to functionality, acceptance criteria, scope, material effects, or premises
on which approval depended require renewed review. Routine implementation choices within
approved scope do not require command-by-command approval.
Record purely editorial revisions without silently changing the approved meaning.
Partial approval covers only explicitly named independent parts; resolve dependencies or
ambiguous scope before implementation.

## Handoff

Use the available workflow mechanism to pass the plan and decision to the next node.
A skill file is not a dispatcher. Do not spawn an agent without runtime support and authority.
Without automatic dispatch, state the next node and its inputs; do not claim it has started.
Missing neighboring skills limit handoff, not standalone review of a supplied plan.

## Boundaries

- Implementation-plan owns the solution and review summary; this skill presents them.
- Execution/recovery tooling creates checkpoints and provides actual recovery instructions.
  Show readiness and limitations here, not a mandatory rollback script.
- Do not create backups, commits, or restoration mechanisms merely to display a panel.
- Delegation is not human selection of the approval option. Personal delegation is out of scope.

## References

- references/approval-panel.md: load when displaying a completed or materially revised plan.
- references/authorization-record.md: load when checking or recording authority.
