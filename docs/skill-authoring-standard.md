# Skill Authoring Standard

Every rule below is enforced by [`../scripts/validate-pack.py`](../scripts/validate-pack.py)
and runs in CI on every push. This document describes what the validator does; the
validator is the authority. If the two disagree, the validator wins and this document
is the bug.

## Maturity tiers

A skill declares its tier in `skill-pack.json`, not in its frontmatter. Frontmatter stays
at exactly two keys so a skill directory remains portable across agent platforms that
know nothing about this repository.

| Tier | Means |
|---|---|
| `draft` | The node exists and is named. The body may be a stub. **Do not expect it to change model behaviour.** |
| `beta` | Has a real workflow. English-primary. Usable, not yet contract-grade. |
| `stable` | Has an output contract, references, and at least one adversarial dry-run case. Safe to depend on. |

## What each tier must satisfy

| Check | draft | beta | stable |
|---|:--:|:--:|:--:|
| Directory exists with a `SKILL.md` | ✓ | ✓ | ✓ |
| Frontmatter parses as YAML | ✓ | ✓ | ✓ |
| Frontmatter has **only** `name` and `description` | ✓ | ✓ | ✓ |
| `name` matches the directory name exactly | ✓ | ✓ | ✓ |
| `path` in the manifest is `skills/<name>` | ✓ | ✓ | ✓ |
| `SKILL.md` is at most 220 lines | ✓ | ✓ | ✓ |
| Description length | ≥ 20 | ≥ 60 | 120–500 |
| Description is English-primary (≥ 70% ASCII) | | ✓ | ✓ |
| Body has at least 40 non-blank lines | | ✓ | ✓ |
| Has a `## Workflow` section | | ✓ | ✓ |
| Has `## Output Contract` and `## References` | | | ✓ |
| Contains no `TODO` / `TBD` / `FIXME` | | | ✓ |
| Every file in `references/` is linked from `SKILL.md` | | | ✓ |
| Appears in `examples/dry-runs.md` | | | ✓ |

Drafts may be written in any language. The English-primary requirement starts at `beta`,
so raising a skill's tier is also the moment its language is settled — one decision, not two.

## Repository-level rules

These apply regardless of tier.

- **Three-way consistency.** The set of skill slugs in `docs/workflow.md`, the set declared
  in `skill-pack.json`, and the set of directories in `skills/` must be identical. Any
  difference in any direction is an error. This is what prevents orphan skills, phantom
  declarations, and diagram drift.
- **Every skill-bearing node label ends with `(skill-slug)`.** Control-flow nodes
  (`START`, `DECISION`) must **not** carry a slug.
- **`VERSION` must equal `skill-pack.json`'s `version`.**
- **A declared license requires a `LICENSE` file.**
- **`repository` must be a real `https://github.com/` URL** with no placeholder left in it.
- **No privacy leaks** in any `.md/.json/.ps1/.py/.yaml/.yml/.txt` file: absolute user
  profile paths, home directory paths, email addresses, or credential-shaped tokens.
  Use `<User>`, `%USERPROFILE%`, or `$HOME` instead.

## The maturity ratchet

`skill-pack.json` carries a floor:

```json
"maturity_floor": { "beta": 0, "stable": 0 }
```

The validator asserts the actual count at each tier is **greater than or equal to** the
floor. When a skill reaches a new tier, raise the floor in the same commit. From then on,
CI fails if the count ever drops.

This is the mechanism that makes "the standard only goes up" a property of the repository
rather than a promise. It also lets CI be green today, with twenty-four drafts, without
pretending they are finished.

## Information architecture

Three layers, borrowed from the way well-built skill packs are structured:

1. **`SKILL.md`** — always loaded into context. Short, imperative, policy-shaped. Capped at
   220 lines because context is the scarce resource.
2. **`skills/<name>/references/*.md`** — loaded conditionally. `SKILL.md` must name each
   reference **and the exact condition under which to load it**. One level deep, no nesting.
3. **`docs/*.md`** — long-form material for humans. Never loaded by the agent.

A rule that belongs in layer 2 but sits in layer 1 costs context on every single run.

## How to write a rule

Sixteen recorded runs against `human-approval` produced one finding that generalises past that
skill: **how a rule is phrased decides whether it will need patching again.** Three levels.

1. **Name a forbidden form.** *"Never write `<backup_path>` in an undo command."* The next run
   wrote `备份路径` and sailed through. Naming a form invites a change of form, and the set of
   forms is open — it cannot be finished.
2. **Name an action or a test.** *"Select the undo line, paste it into a terminal, press enter.
   If any part would have to be replaced first, it fails."* Form stops mattering: placeholder,
   Chinese, a blank space all fail identically. But a test covers only what it tests. This one
   asks whether the line runs, and later passed a command that ran perfectly and deleted the
   operator's only backup.
3. **Define the thing.** *"The undo is the option run backwards."* Everything that is not that is
   excluded without being listed, including cases the author never imagined.

Write at level 3 wherever the thing can be defined, and ship the definition with a mechanical
check beside it. A definition alone drifts: *"required whenever a credential can be made"* was
read as *whenever it is worth making one*, and the rule then passed on a small file and failed on
a large directory. **The definition sets the direction; the check stops the drift.**

### Templates and examples outrank the prose above them

Nine recorded runs copied a template or a worked example over the rule stated beside it —
language, option count, ordering, and once an answer. Two consequences follow.

**A template ships no filled-in cells.** `none` and `n/a` are common answers, not defaults. A run
printed 「撤销：A 无」 having never asked whether A could be undone; the template had already
answered, and half of A was a `git checkout` away. Every cell must be a slot.

**Ship examples that disagree on every dimension a reader may vary.** Anything all the examples
agree on is copied without the reader noticing it was a choice. Two examples that each held a
single action taught panels to carry a single action, and the rule saying otherwise sat directly
above them, unread. The fix was a third example that differs precisely there.

### The rule count is the ceiling, not the token count

Layer 1's cap earns its keep — `SKILL.md` is loaded on every run. Layer 2 is cheaper than it
looks: a fully gated run of `human-approval` reads roughly 6.7k tokens across four files, about
3% of a 200k window, and a run that takes no gate never opens the panel file at all.

What is actually scarce is how many rules a model holds at once. One recorded run held 14 of 15
in a single reference file — and had applied the fifteenth correctly an hour earlier, on the same
machine, on a near-identical prompt.

So the number to watch is the rule count, and it must not climb once per defect. When a new defect
appears, first ask whether it is the other half of a rule already present. *The undo's destination
must be the original path* and *the undo's starting point must be the post-option state* looked
like two findings; they were one rule seen from two sides, and merging them left the count where
it started.

## Section conventions for `beta` and above

```
# <Human Readable Name>

## Workflow
1. Numbered steps. Each step that needs a reference says which one and when to load it.

## <Domain Rule Sections>
Imperative bullets stating a condition and a required behaviour. Not prose.

## Output Contract
What the deliverable must contain. Every item verifiable by reading the output.

## References
- `references/<file>.md`: one line on what it holds and when it applies.
```

## Worksheet — not yet filled in

The rules above are mechanical. The reasoning behind them is not, and copying someone
else's reasoning teaches nothing. The following are open and are meant to be argued out
and written down by the repository owner, not handed over as conclusions.

- [ ] Why 220 lines and not 400? What exactly does a long `SKILL.md` cost?
- [ ] Why is `description` the highest-leverage field in the whole file?
- [ ] Why does the 120-character floor at `stable` improve trigger accuracy rather than
      just add words?
- [ ] Why must safety rules be written as refusals and multi-condition gates instead of
      warnings?
- [ ] Why must an output contract be verifiable by reading the output alone?
- [ ] Which of these rules would survive if the skill had to work on a model half as capable?

Reference material for working these out is listed in
[`compatibility.md`](compatibility.md) and [`trigger-tuning.md`](trigger-tuning.md).
