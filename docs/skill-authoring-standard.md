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
