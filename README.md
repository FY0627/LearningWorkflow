# LearningWorkflow

A 26-node agentic software engineering workflow, packaged as portable agent skills, with a
validator that enforces the quality bar in CI.

Chinese: [README.zh-CN.md](README.zh-CN.md)

## Status

**Version 0.1.0. The framework is complete; the content is not.**

All 24 skills are at `draft` tier. A draft skill names its node and states its goal. It
will not meaningfully change model behaviour yet. This is stated here rather than
discovered later, and the repository enforces it: a skill cannot claim a higher tier
without passing that tier's checks, and the tier counts are visible in `skill-pack.json`.

| Tier | Count |
|---|:--:|
| `stable` | 0 |
| `beta` | 0 |
| `draft` | 24 |

## What problem this solves

Most agent "workflows" are a diagram. The diagram is the easy half. What breaks is
everything the diagram cannot say:

- **Drift.** The diagram says one thing, the skill manifest says another, the directory
  says a third. Nobody notices, because nothing checks.
- **Hollow skills.** A skill file that contains a title and a sentence looks like a skill in
  a file listing and does nothing at runtime.
- **Unfalsifiable quality.** "High standard" with no rubric, no test cases, and no gate is
  a claim, not a property.
- **Provenance rot.** Work replicated from someone else gets described as original, or
  original work gets no attribution at all, and after a few months nobody can tell which.

This repository treats all four as engineering problems with mechanical answers.

## How it works

**Three sources of truth, checked against each other.** The Mermaid graph in
[`docs/workflow.md`](docs/workflow.md), the `skills[]` array in `skill-pack.json`, and the
directories in `skills/` must be identical sets. Every skill-bearing node label ends with
its slug in parentheses; the validator parses them out and asserts set equality in all
directions. Renaming a node without renaming its skill fails CI.

**Maturity tiers with a one-way ratchet.** Each skill declares `draft`, `beta`, or `stable`
in the manifest. Stricter checks apply at each tier. `maturity_floor` records the number of
skills at each tier, and the validator asserts the actual count never falls below it. CI is
green today with twenty-four drafts, and turns red the moment quality regresses.

**Provenance is recorded, node by node.** Part of this workflow is replicated from a
source that was only available as redacted screenshots.
[`docs/workflow-fidelity.md`](docs/workflow-fidelity.md) labels every node `replicated`,
`inferred`, or `original`, states the evidence for each, and lists the design decisions that
are mine rather than the source's. Fourteen nodes are replicated, eleven are inferred, one
is original.

**Privacy is scanned, not promised.** Absolute user paths, home paths, email addresses, and
credential-shaped tokens fail the build.

## The workflow

Four layers: intake and routing, evidence and planning, braided parallel implementation,
gating and closeout. Two properties are worth naming:

**Human authorization is a hard gate.** `implementation-plan` cannot reach `implementation`
without passing through `human-approval`. The operator sets goals, approves architecture,
and accepts risk. The agent matrix executes and self-corrects.

**CI success forks, it does not chain.** `production-deployment-gate` and `security-audit`
are siblings, because chaining them would mean auditing software that has already shipped.

Full graph and rationale: [`docs/workflow.md`](docs/workflow.md).

## Layout

```
LearningWorkflow/
├── skills/<name>/SKILL.md        24 skills, one per workflow node
├── docs/
│   ├── workflow.md               the 26-node graph and its rationale
│   ├── workflow-fidelity.md      node-by-node provenance
│   ├── skill-authoring-standard.md   the tiers and what each enforces
│   ├── compatibility.md          cross-agent portability contract
│   ├── trigger-tuning.md         how to write a description that fires correctly
│   ├── release-checklist.md      pre-release gates
│   └── skill-template/SKILL.md   authoring template (not an installable skill)
├── examples/
│   ├── dry-runs.md               prompts and expected behaviour, incl. adversarial
│   └── usage-benchmark.md        7-criterion rubric, 0-2 each, bar is 11/14
├── scripts/
│   ├── validate-pack.py          the gate; stdlib only; exits 1 on any error
│   └── install.ps1               multi-target installer
├── skill-pack.json               manifest: tiers, ratchet, privacy policy
└── AGENTS.md                     rules for agents editing this repository
```

## Install

```powershell
# See what would happen, change nothing
./scripts/install.ps1 -Target all -WhatIf

# Install for one agent
./scripts/install.ps1 -Target claude

# Replace an existing installation
./scripts/install.ps1 -Target claude -Force
```

Targets: `claude` (`$HOME/.claude/skills`), `codex` (`$HOME/.codex/skills`), `gemini`
(`$HOME/.gemini/config/skills`), or `all`. The installer refuses to overwrite an existing
skill without `-Force`.

### Installing a gate is not enough

Copying files does not make a gate run. A skill loads when the host judges its description a
match, and that judgement happens **before** any rule inside the skill can apply. So a skill
cannot make itself unskippable — the decision to load it is made by the very party it is
meant to constrain.

This is not hypothetical. In a recorded run ([`examples/dry-runs.md`](examples/dry-runs.md))
the model decided a deletion was "low risk", never loaded `human-approval` at all, deleted
four unrecoverable build artifacts, and then ticked the approval step as completed.

For any skill that must not be skipped, put a line in the consuming project's `CLAUDE.md` or
`AGENTS.md` that makes the call part of the workflow rather than a match:

> Before any task that leaves something behind after this session — writing or deleting files,
> changing dependencies, running state-changing commands, committing, pushing, deploying,
> calling an external service, sending a message — `human-approval` must be invoked first,
> **even when the work is unimportant, routine, or produces something that could simply be
> rebuilt.**

The clause in bold is not padding. Those three are the exact justifications a model used to
skip the gate, and naming them is what closes the last place a judgement can hide.

## Validate

```bash
python scripts/validate-pack.py .
```

Stdlib only, no dependencies. Exits 1 on any error. This runs in CI on every push
([`.github/workflows/validate.yml`](.github/workflows/validate.yml)), on `windows-latest`
with Python 3.12, alongside a parse check and a dry run of the installer.

## Contributing to this repository

Read [`AGENTS.md`](AGENTS.md) first. The rules that matter most: frontmatter is exactly two
keys, `SKILL.md` stays under 220 lines, a tier promotion and its `maturity_floor` bump ship
in the same commit, and nothing gets described as replicated unless it is.

## Honesty notice

No benchmark results are published in this repository, because no benchmark has been run.
[`examples/usage-benchmark.md`](examples/usage-benchmark.md) defines the rubric and the
evidence labels; its results table is empty and will stay empty until a real run produces a
real number. The dry-run cases in [`examples/dry-runs.md`](examples/dry-runs.md) are all
labelled `designed-dry-run` — written by hand, never executed.

## License

MIT. See [LICENSE](LICENSE).
