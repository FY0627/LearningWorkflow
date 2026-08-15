# Approval Panel Template

Loaded by `human-approval` at Workflow step 5, when a gate has been triggered and the panel
must be rendered.

## Purpose

Fix the panel's shape so the 100-word ceiling and the 3-decision ceiling are enforced by a
template rather than by the model's restraint on any given run.

## Template

Render in the operator's own language. Structure, not wording, is what this file fixes.

```
<one line: what is about to happen, and that it has stopped here>

  A. <option>
  B. <option that first creates a restore credential, when one can be created>
  C. <do not proceed>

Consequence:  A <fact> / B <fact> / C <fact>
Undo:         A none; B <command that runs as printed>; C n/a
```

Keep the identifiers in the same order on every line. A reader who has to re-locate B between
one line and the next is spending the budget on navigation.

## Rules

- **Ceiling: 150 Chinese characters, or 100 English words.** Commands and file paths do not
  count — they are payload to paste, not text to read; the operator scans them to see what they
  are and reads them only when actually undoing something. The ceiling is a ceiling, not a
  quota.
- **Render everything in the operator's language, labels included.** A Chinese panel with
  `Consequence:` / `Undo:` headings is half-translated.
- **Only options carry identifiers.** Consequences and undo lines are read, never quoted back,
  so labelling them adds noise and costs words. The rule: *label only what the operator will
  say out loud.*
- **One option is always "do not proceed."** Without it the panel silently assumes the work
  should happen and reduces the operator to choosing how. That assumption is the failure this
  gate exists to stop.
- **The number of options follows the situation.** Three is what the worked example happens to
  have, not a format. Two is fine; five means the decision is probably too big.
- **Undo commands must run as printed.** `Move-Item <backup_path> data/tts_dataset` is not an
  undo command — a placeholder cannot be pasted. If the path is not decided yet, that is a fact
  about the option and belongs in its consequence, not hidden inside angle brackets.
- **Where a restore credential can be created first — a backup, a branch, a tag — that is its
  own option.** It is usually the one the operator wants, and it is invisible unless offered.
- **Consequences are stated as facts.** No evaluative wording that tilts toward an option
  ("looks messy", "not worth keeping"). The panel presents; it does not campaign.
- **No "why" line that echoes the operator.** Restating what they already said consumes the
  budget and adds nothing to the decision.
- **Undo is a command, not a description.** "Restore the backup to the right place" is not an
  undo. Options with no undo say so plainly; options that changed nothing say n/a.
- **Tiers are not printed.** 0/1/2 is machine vocabulary for budget and stop conditions. The
  panel says whether it can be taken back, in plain words. Same fact, two audiences.

## When it does not fit

Not fitting is a signal, not a formatting problem: the decision on this screen is bigger than
one decision. Send it back upstream to be split before compressing anything.

If it still does not fit after splitting, give way in this order — and never silently:

| Give way first | | Never give way |
|---|---|---|
| 1. Consequence detail | 2. The ceiling — **say the panel exceeded it** | 3. The irreversible part · 4. Any option |

An operator who loses consequence detail knows they can ask for more. An operator who loses an
option does not know anything was taken. **Unobservable loss is protected last.**

Exceeding the ceiling must be stated on the panel, not absorbed quietly. The ceiling exists so
the panel still works on the operator's most tired day; if it is being exceeded routinely, that
is upstream sending decisions too large, and the drift needs to be visible to be caught.

Dropping an option or an irreversible consequence to satisfy the ceiling is never permitted.
A panel that hides an option is worse than no panel, because the operator believes they saw
everything.

## Worked examples

Two, deliberately. A single filled-in example cannot tell a reader which of its details are
required and which are incidental, and it gets copied whole — language, option count and all.
These two hold the structure constant and vary everything else, so the difference between them
is the answer to "what am I allowed to change".

Deleting a TTS dataset that has no backup, raised mid-task:

```
Stopped: about to delete the old TTS dataset. There is no backup.

  A. Delete it
  B. Back it up elsewhere first, then delete
  C. Do not delete

Consequence:  A gone for good / B recoverable / C old dataset keeps taking space
Undo:         A none; B mv data/tts_dataset_old data/tts_dataset; C n/a
```

≈ 60 words.

Sending a statement to a customer — different language, two options rather than three, and no
credential that can be created first, so there is no "back it up and then proceed" middle
option to offer:

```
已暂停:即将向客户发送对账邮件。

  A. 发送
  B. 不发送

后果:A 对方立即看到,无法撤回 / B 保持未发送
撤销:A 无;B 不适用
```

≈ 40 characters.

What is constant across both: the stop line, identifiers on options only, a "do not proceed"
option, consequences as facts, an undo line in the same identifier order. What varies: the
language, the number of options, whether a credential can be created first. Nothing else in
either example is a requirement.

## Acceptance criteria

- Rendering a real decision with this template stays under the ceiling. **Met** — the example
  above, and a forward test rendered ~140 Chinese characters excluding commands. See
  `examples/dry-runs.md`.
- The operator can decide without opening the plan.
- A reader who has not read the plan cannot produce the identifiers it asks for.
- No rendered panel reads as advocating one of its own options.
