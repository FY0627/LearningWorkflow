# Plan Authorization Record

Load when a supplied or referenced prior approval must be checked, or when explicit new
approval must be recorded. Do not load just because a plan awaits review or the operator
asks a question or requests adjustments. This file specifies a record; reading it grants
no authority and is not itself an approval.
Use the workflow's existing task record; do not create a new file or commit requirement merely
for this gate. The receiving executor must have access to the record.

## Required information

- Plan location and identifiable revision; preserve the reviewed version or its identity.
- The operator's actual selection and associated panel.
- Approved scope, exclusions, and any explicitly approved independent subset.
- Acceptance criteria and material effects, directly or through the preserved plan.
- Execution prerequisites and their verified or pending status.
- Next node and handoff status: ready, handed off, or blocked with a reason.

An identifier without its plan and disclosure is insufficient. Questions and adjustment
requests are not approvals. Do not record authority the operator has not granted.

## Validity

Implementation must use the approved revision and scope. Material changes return to review
under the entrypoint's validity rules. Verify pending prerequisites before affected edits;
an approval record does not prove preparation succeeded.
Retain prior decisions as history when a revised plan needs new approval.

## Acceptance criteria

- The receiver can distinguish approved work from blocked work.
- The record distinguishes a human decision from a proposed or incomplete handoff.
- The record does not claim to implement snapshots, rollback, or unattended delegation.
