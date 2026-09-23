# Plan Authorization Record

Load when a supplied or referenced prior approval must be checked, or when explicit new
approval must be recorded. Do not load just because a plan awaits review or the operator
asks a question or requests adjustments. This file specifies a record; reading it grants
no authority and is not itself an approval.

Append the authorization record directly to the target plan document (e.g., `implementation_plan.md`)
under the `## Authorization Record` section. Do not create a separate standalone file or
require a Git commit merely for this gate. The receiving executor directly inspects this
embedded block.

## Required information

- Plan location and identifiable revision; preserve the reviewed version or its identity.
- The operator's actual selection and associated panel.
- Approved scope (`ALL` or an explicitly pre-defined independent phase).
- For task-level continuation across revisions, stable task IDs, the approved task-contract
  identity, and any dependencies whose unchanged state was verified. An unverified or changed
  dependency suspends continuation; it does not invalidate unrelated approved work.
- Acceptance criteria and material effects, directly or through the preserved plan.
- Execution prerequisites and their verified or pending status.
- Next node and handoff status: ready, handed off, or blocked with a reason.

An identifier without its plan and disclosure is insufficient. Questions and adjustment
requests are not approvals. Do not record authority the operator has not granted.
Keep the reviewed plan content identifiable independently of this appended record: a content
hash, if used, covers the plan body before `## Authorization Record`, not the appended stamp.
Preserve the prior authorization when revised tasks are sent back to planning.

## Paired designed examples — not execution evidence

```markdown
## Authorization Record

- Status: APPROVED
- Plan Revision: v2 (Hash: 9f8a3c)
- Operator Selection: A. 批准
- Approved Scope: ALL
- Approved At: 2026-09-19T21:00:00Z
- Execution Prerequisites: Checkpoint R01 verified
- Handoff Status: READY_FOR_IMPLEMENTATION (Target: implementation)
```

```markdown
## Authorization Record

- Status: APPROVED
- Plan Revision: v2 (Hash: 9f8a3c)
- Operator Selection: A. 批准 (Phase 1 only)
- Approved Scope: Phase 1 (Database & Backend API)
- Excluded / Pending: Phase 2 (Frontend UI)
- Approved At: 2026-09-19T21:00:00Z
- Execution Prerequisites: Pending backup of migration table
- Handoff Status: READY_FOR_IMPLEMENTATION (Target: implementation)
```

Both examples embed into the plan document. The first covers full scope; the second covers
a pre-defined independent phase while explicitly holding unapproved phases in pending state.

## Validity

Implementation must use the approved revision and scope. Material changes return to review
under the entrypoint's validity rules. Verify pending prerequisites before affected edits;
an approval record does not prove preparation succeeded.
Retain prior decisions as history when a revised plan needs new approval.

## Acceptance criteria

- The receiver can distinguish approved work from blocked work.
- The record distinguishes a human decision from a proposed or incomplete handoff.
- The record is physically embedded in the plan document without creating separate files.
- The record does not claim to implement snapshots, rollback, or unattended delegation.
