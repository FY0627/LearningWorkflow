# Irreversibility Tiers

Loaded by `human-approval` at Workflow step 3, once the task's action list exists. Every action
on that list is classified separately; the task then takes the highest tier among them.

## Purpose

Decide the tier from the two questions below, using the actual action and its concrete undo.
Do not judge importance or match action names to an exhaustive list.

## The two questions

Ask them in this order. The order is not by severity — question 2 has no meaning until
question 1 is answered, because there is nothing to weigh the cost of undoing until an undo
exists at all.

**Q1 — Can the operator undo it themselves?**

- Is there a command that reverses it, and can that command be written down *before* acting?
- A precise inverse can be sufficient without a separate backup or commit. For an edit,
  determine whether it preserves the observed pre-action content, encoding, and line endings.
  The implementation must supply an executable inverse, not just describe the desired result.
- A credential that does not exist yet but can be created first — a backup, a branch, a tag —
  counts only once it actually exists. Classify the action as it stands right now.
- **Check before concluding, in either direction.** "It's source code, so it's probably in
  git" is an assumption, and so is treating a credential as absent without looking. Where the
  environment allows it, inspect the relevant target state and proposed recovery source.
  A dirty target rules out a whole-file Git restore that would lose edits, not every undo.
- **A universal fallback is not a substitute for checking.** Proposing a `.bak` copy beside
  every file works in every environment, which is exactly why it is tempting — and why it
  hides the question instead of answering it. Its cost lands on the operator, who ends up with
  a directory full of `.bak` files. Where a check would reveal a cleaner credential — a commit,
  a branch — do the check and offer that one.
- If no existing safe inverse is established and recovery requires a new backup, creating
  it first becomes an option on the panel. That
  costs the operator one keystroke, and costs nothing at all if the credential turns out to
  have been there.
- "Themselves" is the operative word. If undoing depends on a party the operator does not
  control — a vendor refunding a charge, a recipient deleting a message — the answer is **no**.
- **Regenerating is not undoing.** An undo gives back the artifact that was there. A rebuild
  gives a new one, produced from whatever the inputs say now, and it will differ — different
  timestamp, different code state, possibly a different commit. So "it can be rebuilt" is not
  a yes to this question. Build outputs, installers, bundles, exported files, caches: deleting
  them is undoable only if a copy of *that* artifact still exists somewhere.
- **A hedged command is not a command.** If the undo can only be written as "run X, or whatever
  this project's equivalent is", then it could not be written down before acting, and the
  answer here is no. Uncertainty about the undo is itself the answer.

**Q2 — Does undoing take other things with it?**

- Would the undo also discard work that should have been kept: later commits, someone else's
  changes, downstream state built on top of it?
- This asks about collateral damage from the undo itself. It does **not** ask whether some
  policy forbids undoing. A rule against reverting is not a property of the action.

### Workspace changes and scope

Inspect workspace status before acting, including staged, unstaged, and untracked changes,
and compare existing changes with every planned action and its concrete undo scope. A dirty
workspace alone is not a reason to gate. When execution and undo preserve all existing work,
unrelated changes do not raise the tier: proceed without requesting confirmation.

Check all affected paths, not just one representative file. Account for commands that also
change the index or reach outside the named targets. Do not clean, stash, or reset unrelated
work merely to obtain a clean workspace. Overlap requires checking whether a precise undo
preserves the existing work; overlap alone does not establish collateral loss. If undo would
discard other work, Q2 is yes; if preservation cannot be established, use Tier 2.

After execution, compare the result with the observed starting state before claiming that
only planned changes occurred. Evidence supports only what it measures: a status listing
establishes listed state, not content identity. Limit the claim to the relevant verification;
do not broaden inspection merely to make a universal "nothing else changed" statement.
An undo command must preserve pre-existing changes. All of this
is checking, not reporting: what reaches the operator is the brief, evidence-based close in step 6.
Showing an undo command does not require executing it.

Choose an undo that preserves existing work when one can be established; do not choose a
known destructive whole-file restore merely to classify an otherwise reversible edit as Tier 1.
If a precise inverse cannot be established, state what is missing and present the applicable
options rather than repeatedly reconsidering the same evidence. For later use, disclose the
undo's state assumptions; where practical, have it refuse to write when those assumptions fail.

These paired designed cases vary only the inverse method; neither is execution evidence.
In both, a file contains uncommitted user edits before an agent appends known bytes:

| Undo method | Classification |
|---|---|
| Restore the whole file from Git, losing the user's earlier edits | Tier 1 for this method; seek a preserving inverse before gating. |
| Check the expected post-edit bytes, then remove exactly the appended bytes, preserving the original bytes and index | Tier 0; no new backup is required. Refuse the undo if the expected state no longer matches. |

These paired designed cases vary only where pre-existing changes lie; they are not test results:

| Planned action and undo | Pre-existing changes | Classification |
|---|---|---|
| Edit tracked `src/widget.ts`; restore that path from its checked Git baseline | Only `notes.txt` is modified; the target matches the baseline | Tier 0: execution and undo preserve the unrelated changes; proceed without a gate. |
| Edit tracked `src/widget.ts`; restore that path from its checked Git baseline | Only `src/widget.ts` is modified; the target differs from the baseline | Tier 1 for this undo: it discards existing edits; a verified precise undo preserving them could instead qualify for Tier 0. |

**Does not count as "other things":**

| Answer | Why it does not count |
|---|---|
| "The undo removes what this action produced" | That is what an undo is. Counting it would leave Tier 0 permanently empty. |
| "A rule says I am not allowed to revert" | A policy is not a property of the action. |

If either question cannot be answered, the action is Tier 2. Fail closed.

## Tiers

| Tier | Q1 undoable by self | Q2 takes other things | Meaning |
|:--:|:--:|:--:|---|
| **0** | yes | no | Undo is clean. No gate. |
| **1** | yes | yes | Undo exists but costs work that was worth keeping. |
| **2** | no | — | Cannot be undone. |

## Worked examples

| Action | Q1 | Q2 | Tier |
|---|:--:|:--:|:--:|
| Edit a file in a clean git worktree | yes | no | 0 |
| Change one number in `skill-pack.json` | yes | no | 0 |
| Swap a demo's fake data for real API calls, nothing built on top yet | yes | no | 0 |
| `git push --force` to a shared branch | yes | yes — discards others' commits | 1 |
| Revert a TTS approach after unrelated work landed on the same branch | yes | yes — discards the UI, parameter and ASR work | 1 |
| Delete a large directory with no backup | no | — | 2 |
| Delete a build output (APK, bundle) with no copy kept | no — a rebuild is a different artifact | — | 2 |
| Send an email to a customer | no — needs the recipient | — | 2 |
| Call a metered API | no — needs the vendor | — | 2 |

## Notes

- Classification is evaluated **at the moment of the check**, not in the abstract. Deleting a
  directory is Tier 2 without a backup and Tier 0 after one is made. Reversibility can be
  manufactured; the gate's job is to report which one is true right now.
- This file deliberately does not enumerate actions. An action list would always be
  incomplete, and combined with fail-closed an incomplete list turns every unlisted action
  into a gate — which gets the gate switched off within days.

## Acceptance criteria

- Each tier's evaluation includes an actual run with recorded evidence, not only designed examples.
- An unfamiliar action is classified using Q1 and Q2 with the relevant observed facts;
  neither its absence from examples nor a desired execution speed determines the tier.
- A proposed clean undo restores the pre-action state within its stated scope while preserving
  existing work; its applicability conditions and any unresolved limitations are explicit.
- Two different people applying this file to the same action reach the same tier.
- No step requires the reader to decide whether something is "important" or "risky".
