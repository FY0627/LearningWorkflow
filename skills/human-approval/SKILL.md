---
name: human-approval
description: >-
  Gate that stops execution before an agent acts on an implementation plan or crosses an
  irreversibility line. Requires explicit, plan-specific consent from the operator, and treats
  silence, questions, partial answers, and after-the-fact notification as refusal. Also governs
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
2. Classify the pending action by reversibility. **Lookup only** — load
   `references/irreversibility-tiers.md` and match. Do not reason about importance.
3. If the action does not appear in the table, classify it as irreversible. Fail closed.
4. Tier 0 (fully reversible) requires no gate. Do the work without interrupting, then close
   with a single line carrying two things: the fact the check established, and the undo command
   that fact makes available — e.g. *"tracked, worktree clean; `git checkout -- skills/`
   reverts this"*, phrased in the operator's language, not this file's. After the work, never
   as a question. Neither half can be written without
   having actually checked, which is what keeps a silent pass distinguishable from a skill that
   never loaded. A bare "I applied human-approval" is a claim, not evidence, and does not
   satisfy this.
5. Otherwise render the approval panel per **Output Contract**.
6. Accept only consent that satisfies **Consent**. Anything else is not consent: state what is
   still needed, once, and stop. Do not argue, do not re-explain the plan.
7. Record the granted scope: which options, which accepted risks, which action tiers.
8. During execution, watch the **Expiry** conditions. On any of them, stop and return here.

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

Consent exists only when the operator returns, from the panel, **by identifier**:

- the option they chose, and
- the risk they accept.

These identifiers exist only inside the plan. An operator who did not read it cannot produce
them, and the agent does not need to judge anything to check them.

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

Expired approval returns to step 5. It is not renewed by the agent's own judgement that the
change was small.

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
- Give every option and every risk a short identifier the operator can quote back.
- State, for each decision: the choice, the part that cannot be undone, the risk being
  accepted, and the paste-ready undo command.
- Survive the 30-second test: the operator on their worst, most tired day must still be able to
  decide from it. Design for that day, not for an attentive one.

The panel must **not** contain how the work will be done. Implementation detail is delegated
work; it belongs in the plan, not in the gate. It is the primary cause of panel bloat.

The ceiling is **100 words, one screen** — 30 seconds at decision-reading speed, not skim
speed. At that budget the panel cannot be prose. It is a table: one row per decision, each row
carrying an identifier, the irreversible part, the accepted risk, and the undo command. Every
explanation lives in the plan, not here.

## References

- `references/irreversibility-tiers.md`: the reversibility criteria. Load before classifying
  any pending action, and treat any action it does not resolve as irreversible.
- `references/approval-panel.md`: the panel template. Load when a gate has triggered and the
  panel is about to be rendered.
- `references/authorization-record.md`: the record format. Load when authority is granted, and
  again before each action taken in unattended mode.
