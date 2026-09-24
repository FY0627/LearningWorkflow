---
name: human-approval
description: >-
  Trigger when an implementation plan and review summary are completed, or revised following
  review feedback, and await human approval. Present the review panel, record the approved
  version and scope, and process approval or adjustment feedback.
---

# Human Review and Approval

This is the decision gate between implementation-plan and implementation.
It presents the plan, records the decision, and hands off. It does not author solutions,
implement changes, create recovery tools, or manage unattended delegation.
Reversibility does not exempt an implementation plan from review.

## Entry conditions

In this workflow, implementation-plan hands off as soon as the plan and review summary are
complete. Standalone use accepts a completed plan from the current task without requiring
that particular planning skill. Replies to an existing panel continue that review; they do
not restart plan generation or require another panel before processing the response.

## Inputs

Receive the plan location, identifiable revision, review summary, and any prior approval.
A document revision or content hash is sufficient; a Git commit is not required.
User-provided plans can be reviewed without rerunning the planning skill.

The plan must state the intended result, scope and exclusions, approach, acceptance checks,
material effects, and execution prerequisites. Recovery readiness must distinguish a verified
existing checkpoint from planned preparation, or explain why recovery is not applicable.
Git repository existence alone does not establish that current contents are saved.
For changes to existing code, the plan must identify the relevant audit summary, comparable
source baseline, evidence coverage, and the planner's comparison with current code. These
are completeness fields for this gate, not a request to re-audit code here.

## Workflow

1. If a prior approval is supplied or referenced, load references/authorization-record.md
   and check its revision and scope. If valid, hand off without asking again. If no prior
   approval is present, inspect the plan and summary without loading that reference.
2. Return missing or contradictory decision-relevant information to implementation-plan.
   For changes to existing code, a missing audit summary, baseline, coverage, or comparison,
   or a plan that reports stale evidence or unresolved material dependencies, blocks a review
   panel. Return the evidence gap to planning; do not independently judge source dependencies
   or infer safety from the existence of an audit document.
   Do not invent a solution, user choice, recovery guarantee, or successful verification.
3. Load references/approval-panel.md and display the summary, full-plan link, and choices.
   Do not require a separate long report before the panel. Await the operator; silence does
   not start implementation.
4. Process the response using a deterministic three-point lock:
   - A response that requests a material change is adjustment feedback, even if it also
     says to start. Return the change to planning before executing affected work.
   - Entity lock: matches the exact revision or hash of the displayed plan.
   - Verb lock: requires the explicit Option A / approval identifier. Vague assent
     (e.g., "looks good", "proceed") without the identifier is held in waiting.
   - Scope lock: covers either the entire disclosed scope ("ALL") or an explicitly
     pre-defined independent phase in the plan.
   - Concrete adjustment feedback returns to planning; no adjustment identifier is required.
     An adjustment identifier without feedback requires clarification.
   - Answer questions without treating them as approval. Clarify vague assent without the
     approval identifier; do not repeat an unchanged panel to solicit assent.
   - Explicit cancellation ends the review. Waiting is the default, not a third panel option.
5. On approval, load references/authorization-record.md, append the structured
   authorization stamp directly to the plan document, and hand off to implementation.
   No second confirmation is needed for the same scope.
   Execution must satisfy and verify pending prerequisites before affected modifications.
6. On adjustment, hand the current plan and feedback to implementation-plan. Review the
   revised plan when ready. Requirement changes may require upstream clarification.

## Scope and validity

Approval covers the identified plan and its disclosed effects, not future work with the same
title. Changes to functionality, acceptance criteria, scope, material effects, or premises
on which approval depended require renewed review. Routine implementation choices within
approved scope do not require command-by-command approval.
Previously approved tasks may continue during a revision only when implementation-plan
identifies them by stable task ID and unchanged task contract, implementation confirms no
changed or unknown dependency, and the existing authorization covers them. If any condition
is unproven, hold the task. Never infer approval for an unapproved task from a request to
revise another task.
Record purely editorial revisions without silently changing the approved meaning.
Partial approval is strictly restricted to explicitly pre-defined independent phases or
modules already partitioned in the plan. Any ad-hoc scope reduction or unscheduled task
slicing must be treated as Option B (Adjustment) and returned to implementation-plan to
re-evaluate dependencies. Never synthesize a new task list within this skill.

## Handoff

Invoke implementation only after an explicit approval has been recorded in the plan document's
authorization stamp, or a supplied prior approval has been verified as covering the current
revision. Pass the plan location and revision, approved scope, acceptance criteria, authority
record, and outstanding execution prerequisites.
Pending prerequisites belong to implementation's preparation; they block the affected changes,
not the handoff itself. A question, silence, adjustment, or ambiguous selection never starts it.

Invoke implementation-plan when concrete revision feedback is available, or the plan lacks
decision-relevant information. Pass the current revision, exact feedback or missing facts,
and any approved constraints to preserve. An adjustment selection without details first needs
clarification; do not invent a revision request. A question alone is answered in the review.
The planner returns a completed revised plan and summary to this skill for another decision.

Use the available workflow mechanism to pass the plan and decision to the next node.
When the target skill is available, read it and continue through the supported handoff rather
than asking whether to invoke the next node. The same agent may apply the next skill.
A skill file is not a dispatcher. Do not spawn an agent without runtime support and authority.
Without automatic dispatch, state the next node and its inputs; do not claim it has started.
Missing neighboring skills limit handoff, not standalone review of a supplied plan.

## Boundaries

- Implementation-plan owns the solution and review summary; this skill presents them.
- Show recovery readiness, coverage, and limitations. Do not generate or display recovery commands.
- Do not create backups, commits, or restoration mechanisms merely to display a panel.
- Delegation is not human selection of the approval option. Personal delegation is out of scope.

## References

- references/approval-panel.md: load before rendering a new or revised review panel. A reply
  that does not require a new panel does not require reloading this template.
- references/authorization-record.md: load when a prior approval must be checked or a new
  explicit approval must be recorded. Waiting, questions, and revision feedback do not by
  themselves require this reference. Reuse references already read in the current context.
