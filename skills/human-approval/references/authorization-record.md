# Authorization Record Format

Loaded by `human-approval` at Workflow step 7, and again before each action taken in
unattended mode.

## Purpose

Fix the format of what gets written down when authority is granted and while it is being
spent, so the record is executable rather than descriptive.

## When the window opens

Record, before the first action:

- **A restore point for the whole window** — a branch, tag, or commit hash. Not per action:
  per window. Tier 0 actions stack, and once later work sits on top of earlier work, undoing
  the earlier action starts taking the later work with it. A window-level restore point is
  what keeps a long unattended run reversible as a unit.
- **What was approved**: the option identifiers the operator returned, and the highest tier
  they authorised.
- **The stopping condition**, stated before the run rather than judged during it.

## Before each action

- The action, and its tier from `irreversibility-tiers.md`.
- Its restore credential: a paste-ready command, a commit hash, a backup path. Prose such as
  "impact: moderate" is not a credential. The test is whether the operator can undo the action
  from the record alone, without asking anyone.
- Written **before** the action, never after. A credential recorded afterwards is a report.

## Stopping

Return control on whichever comes first:

- An action classifies above the approved tier. Stop **before** taking it, not partway through.
- The approved task list is exhausted.
- A premise the plan listed is falsified.

The task list is the approved `implementation-plan`'s item list. This skill does not author it,
extend it, or decide that one more item belongs on it — see the refusals in `SKILL.md`. Without
a closed list, "finish what can be finished" means "keep going".

Work discovered mid-window that is not on the list is not one more Tier 0 item to absorb. It
changes the action set, which expires the authorisation. Stop and return.

If an action fails partway rather than being stopped before it starts, apply the credential
recorded for it, close the window, and return with the failure. Do not attempt a second action
to repair the first — repair is not on the approved list.

## When the window closes

- Why it stopped: which of the three conditions fired.
- What is done, what is half-done, and what abandoning would cost versus finishing.
- The window restore point, repeated, so rolling back the whole run needs no searching.

## Acceptance criteria

- The operator can undo any recorded action using the record alone, without asking anyone.
- The operator can undo the entire window using the record alone.
- Reading the record answers: what was authorised, why it stopped, and what state the work is
  in right now.
