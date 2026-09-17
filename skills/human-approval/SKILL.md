---
name: human-approval
description: >-
  Check authorization and reversibility before actions. Proceed with requested, fully
  reversible work; gate actions with irreversible effects or collateral loss on undo.
  Requires explicit option selection for gated work; silence and vague assent grant nothing.
  Also governs delegated work under a bounded, logged, self-expiring action budget.
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
   not the wording of the request. Load `references/irreversibility-tiers.md` and answer
   Q1 and Q2 for the actual action and proposed undo. Examples are not an exhaustive list.
4. If either answer remains unresolved after relevant checks, classify as Tier 2 and state
   the missing fact. An action missing from the examples is not a reason to gate.
5. **The task takes the highest tier on its list.** A lower-tier action gets no path of its
   own — it is carried by the tier above it, and it stays visible there. Alone, a Tier 0 edit
   closes with its own trace line and the operator sees it; bundled under something bigger it
   would vanish, leaving the gate protecting it *worse* than no gate at all.
6. Tier 0 — every action on the list — requires no gate, even when the workspace contains
   unrelated uncommitted changes that execution and undo will preserve. Proceed without asking
   for a reply. Check the relevant workspace state before acting, whether existing changes
   overlap the action and its undo, and the result measured against that starting state.
   Close in the operator's language with the result, relevant validation outcome, and a
   concrete undo preserving existing work. For routine success, use a short paragraph plus
   the undo command; omit a separate audit report. Include starting-state details only when
   they explain preservation or an undo condition. Scale detail to decisions the operator
   must make, not the number of checks performed. Failures, partial completion, and material
   limitations remain visible. Claims must not exceed the evidence. This is a report, not
   a request for confirmation; no fixed line count overrides necessary task information.
7. Otherwise load `references/approval-panel.md` — now, not earlier — and render the panel per
   **Output Contract**.
8. Accept only consent that satisfies **Consent**. Anything else is not consent: state what is
   still needed, once, and stop. Do not argue, do not re-explain the plan.
9. Load `references/authorization-record.md` and record the granted scope: selected options,
   their disclosed consequences and undo conditions, and their action tiers.
10. During execution, watch the **Expiry** conditions. On any of them, stop and return here.

### Check boundaries

Use current workspace evidence to resolve Q1 and Q2, then proceed or present the panel.
Do not repeat a resolved check without a changed fact, failed command, or conflicting result.
Inspect the reach of both execution and undo. Each additional inspection must resolve a
specific uncertainty that could change authorization, classification, or verification.
Stop expanding when the evidence suffices to decide. Examples illustrate criteria; only
observed task facts establish current state. Supporting checks with side effects belong to
the action list and must preserve existing work just like the requested action.

## Refusals

This skill must not:

- Write code, write documentation, or author a plan. Those belong to other skills.
- Decide for itself whether the work is important, critical, or risky enough to need approval.
  That determination comes from Q1/Q2 and the authorized scope, never from
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
- The reversibility tier of the remaining work rises above the approved tier.

Expired approval returns to step 7. It is not renewed by the agent's own judgement that the
change was small.

A retry, substituted command, or recovery action requires a fresh classification at step 3
before execution. Check its actual targets, side effects, and undo conditions. A command
change alone does not expire consent when the disclosed scope and consequences remain covered.
For an ungated task, continue silently if all actions remain Tier 0 within the requested scope.
If new consent is needed, pause before acting and present the updated panel directly; do not
first refuse and wait for the operator to insist. An unresolved classification is Tier 2,
not an automatic permission to execute. This skill checks authority; implementation chooses
how to perform the authorized work.

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

Present the review subject in one line above a table. Use separate columns for option,
consequence, and undo, with one row per option. Only options carry identifiers. Use an em dash
in the undo cell when no undo applies; state irreversible loss explicitly in consequences.
For partly reversible options, list the available undo and identify the unrecoverable part.
Follow the localized length limits and overflow rules in `references/approval-panel.md`.

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
