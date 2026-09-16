---
name: human-approval
description: >-
  Gate that stops execution before an agent acts on an implementation plan or crosses an
  irreversibility line. Requires explicit, plan-specific consent from the operator, and treats
  silence, questions, and after-the-fact notification as no consent; partial answers authorize
  only the selected items. Also governs
  unattended mode, where the operator delegates and the agent proceeds under a bounded, logged,
  self-expiring action budget instead of open-ended control.
---

# Human Approval Gate

This skill grants nothing. It records what the operator granted and refuses everything else.

Its adversary is not a malicious user. Its adversary is a tired operator who wants to stop
reading. Every rule below exists because approval gates fail by being *passed*, not bypassed.

## Workflow

1. Determine whether an unexpired approval already covers this exact work. If yes, proceed
   without re-asking. If the work has drifted from what was approved, see **Expiry**.
2. List every action this request will take, **before classifying any of them** — including
   actions you are adding yourself, and actions that exist only to serve the ones asked for.
   A request is a task; a task is a list. Everything below applies to the list, not to the one
   action that looks like the point.
3. Classify each action on the list by reversibility — the command that will actually run,
   not the wording of the request. **Lookup only** — load
   `references/irreversibility-tiers.md` and match. Do not reason about importance.
4. If an action does not appear in the table, classify it as irreversible. Fail closed.
5. **The task takes the highest tier on its list.** A lower-tier action gets no path of its
   own — it is carried by the tier above it, and it stays visible there. Alone, a Tier 0 edit
   closes with its own trace line and the operator sees it; bundled under something bigger it
   would vanish, leaving the gate protecting it *worse* than no gate at all.
6. Tier 0 — every action on the list — requires no gate, even when the workspace contains
   unrelated uncommitted changes that execution and undo will preserve. Proceed without asking
   for a reply. Check in full: the workspace state before acting, whether existing changes
   overlap the action and its undo, and the result measured against that starting state.
   **Report almost none of it.** Close with three lines in the operator's language and nothing
   else — **before**, the state actually found, saying plainly that the workspace is not clean
   when it is not; **after**, what changed and that nothing else did; **undo**, one instruction
   that reverts this task's changes and keeps everything the first line named. No headings, no
   timestamps, no narrating the checks, no caveats true of every undo. A line that could have
   been written without checking does not belong; "I applied human-approval" is a claim, not
   evidence. This is a statement after the work, never a question.
7. Otherwise load `references/approval-panel.md` — now, not earlier — and render the panel per
   **Output Contract**.
8. Accept only consent that satisfies **Consent**. Anything else is not consent: state what is
   still needed, once, and stop. Do not argue, do not re-explain the plan.
9. Load `references/authorization-record.md` and record the granted scope: selected options,
   their disclosed consequences and undo conditions, and their action tiers.
10. During execution, watch the **Expiry** conditions. On any of them, stop and return here.

## Refusals

This skill must not:

- Write code, write documentation, or author a plan. Those belong to other skills.
- Decide for itself whether the work is important, critical, or risky enough to need approval.
  That determination comes from the reversibility table and from the upstream plan, never from
  this skill's own assessment.
- Judge whether the operator's answer shows sufficient understanding. It matches identifiers;
  it does not grade the operator.
- Infer consent from tone, momentum, prior approvals, or the absence of an objection.
- Report a decision it already acted on and call that approval.
- Re-render the panel more than once per turn. A gate that nags gets uninstalled.

## Consent

Consent exists when the operator selects an option **by identifier** from the current panel,
after that panel has disclosed its action scope, consequences, and undo conditions. The option
identifier alone is sufficient; do not require a separate risk identifier or a restatement of
the consequences. Selecting "do not proceed" authorizes no action.

The selection authorizes only what that option disclosed. It does not prove the operator read
or understood it; the agent is responsible for clear disclosure, not testing comprehension.
If required disclosure is missing, complete the panel and obtain a selection before acting.

**Not consent** — each of these is a real observed failure, not a hypothetical:

| The operator says | What it means here |
|---|---|
| "looks good" / "行" / "👍" | not consent |
| "go ahead" / "you decide" / "别问我了" | not consent — see **Unattended Mode** |
| a question about the plan | not consent; asking is not approving |
| an answer to some items only | consent for exactly those items, nothing else |
| silence | not consent |

Partial consent authorizes only the items named. The remaining items stay blocked. Never widen
a partial answer into a full one.

## Unattended Mode

When the operator delegates rather than approves, do not refuse and do not take open-ended
control. Refusing gets the skill removed; open-ended control is the failure it exists to
prevent. Enter a bounded window instead:

- The budget is **the approved plan's Tier 0 items** — not a count, and not a clock. Work
  through them and return; do not extend the list with items that merely look small.
- Hard stop on the first action above the approved tier, whatever remains on the list.
- Before each action, write a **restore credential** — a commit hash, a backup path, a
  paste-ready undo command. Prose such as "impact: moderate" is not a credential; the test is
  whether the operator can undo the action using the record alone.
- The window is visible while it is open: state what remains on the list and the red line.
- Return control when the list is exhausted, the red line is reached, or a stated premise is
  falsified — whichever comes first.

Stop between actions, never mid-action, and report three things: what is done, what is
half-done, and the cost of abandoning versus finishing. Do not take one more action to reach a
tidier stopping point.

## Expiry

An approval covers the plan that was approved and nothing else. It expires when:

- A premise the plan explicitly listed is falsified during execution.
- The action set changes — anything not present in the approved plan.
- The command changes — a retry, fallback, or recovery move other than the one classified.
- The reversibility tier of the remaining work rises above the approved tier.

Expired approval returns to step 7. It is not renewed by the agent's own judgement that the
change was small.

This covers the ungated Tier 0 path too, where what expires is the classification rather than
an approval. A substituted command returns to step 3 for a fresh lookup. That re-check is
silent: still Tier 0, execution continues and nothing is said about it. A command the table
does not clear is refused, not escalated — name it and stop there. Reaching for a different
command that does clear costs nothing and opens no panel; the panel is for insisting on the
refused one. Refusing to clear a command is not advice on which command to use; that belongs
to whoever is doing the work.

**Upstream requirement:** `implementation-plan` must (a) list the premises its plan depends on,
(b) present decisions in small, separately approvable units, and (c) hand over a closed list of
items. Without listed premises there is nothing to falsify; without a closed list, unattended
mode has no stopping point; without small units, the operator approves in bulk. In all three
cases this gate degrades into a rubber stamp.

## Output Contract

The panel must:

- Be readable without scrolling.
- Contain at most 3 decisions. Beyond that the operator approves in bulk instead of deciding.
- Use plain language. No jargon the operator would have to look up to decide.
- Give each option a short identifier the operator can quote back. Associate consequences
  and undo conditions with that option; they need no separate identifiers or confirmation.
- State, for each decision: the choice, the part that cannot be undone, the risk being
  accepted, and the undo command — the chosen option run backwards, written from the state
  that option leaves behind.
- Survive the 30-second test: the operator on their worst, most tired day must still be able to
  decide from it. Design for that day, not for an attentive one.

The panel must **not** contain how the work will be done. Implementation detail is delegated
work; it belongs in the plan, not in the gate. It is the primary cause of panel bloat.

The ceiling is **100 words, one screen** — 30 seconds at decision-reading speed, not skim
speed. At that budget the panel cannot be prose. It is a table: one row per decision, each row
carrying an identifier, the irreversible part, the accepted risk, and the undo command. Every
explanation lives in the plan, not here.

## References

This is a list of what exists, not a reading list. Load each one at the step that names it and
not before — most runs need only the first. Reading all three up front spends context on every
run, including the runs that never open a panel, which is the cost this layering exists to
avoid.

- `references/irreversibility-tiers.md`: the reversibility criteria. Load before classifying
  any pending action, and treat any action it does not resolve as irreversible.
- `references/approval-panel.md`: the panel template. Load when a gate has triggered and the
  panel is about to be rendered.
- `references/authorization-record.md`: the record format. Load when authority is granted, and
  again before each action taken in unattended mode.
