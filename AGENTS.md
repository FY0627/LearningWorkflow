# AGENTS.md

Rules for any agent — or person — editing this repository.

Run `python scripts/validate-pack.py .` after any structural change. It is the same command
CI runs, and it is the fastest way to find out you broke something.

## Editing skills

- `SKILL.md` frontmatter is **exactly** `name` and `description`. No other keys. The
  validator rejects extras, because extra keys make the skill non-portable.
- `name` must equal the directory name. Renaming a skill means renaming the directory, the
  manifest entry, and the node label in `docs/workflow.md` — in the same commit, or CI
  fails on three-way consistency.
- Keep `SKILL.md` under 220 lines. When it grows, move detail into
  `skills/<name>/references/*.md` — one level deep, never nested.
- Every reference file must be linked from its `SKILL.md`, together with the condition
  under which it should be loaded. Orphan reference files are an error at `stable`.
- **Never ship a single filled-in example.** Worked examples are copied verbatim, and they beat
  the prose rules written around them. Forward tests against `human-approval` caught this three
  times: a placeholder inside angle brackets, an identifier ordering, and the example's own
  language — that last one in a file that explicitly said to render in the operator's language.
  Give at least two examples that hold the structure constant and differ in exactly the things
  that are allowed to differ. The difference between them is what tells a reader which details
  are requirements and which are incidental.
- Do not raise a skill's `status` in `skill-pack.json` without meeting that tier's rules in
  [`docs/skill-authoring-standard.md`](docs/skill-authoring-standard.md). Satisfying the
  string checks is not the same as meeting the intent.
- When you do raise a status, raise `maturity_floor` in the same commit. The floor only
  goes up.

## Editing the workflow

- Every skill-bearing node label ends with `(skill-slug)`. Control-flow nodes (`START`,
  `DECISION`) must not carry a slug.
- Changing the graph means updating both `docs/workflow.md` and `docs/workflow.zh-CN.md`.
- Any change to node provenance goes in [`docs/workflow-fidelity.md`](docs/workflow-fidelity.md)
  in the same commit.

## Provenance and honesty

This repository replicates part of a workflow that was only available as redacted
screenshots. That fact is recorded, not hidden.

- Never describe an `inferred` or `original` node as replicated.
- Never promote a node from `inferred` to `replicated` without new source evidence.
- Never label a designed example as a real run. The evidence labels in
  [`examples/usage-benchmark.md`](examples/usage-benchmark.md) are not decorative.
- If a benchmark was not run, the result table stays empty. An empty table is honest; a
  populated one that describes intentions is not.

## Privacy

- No absolute user paths, home directory paths, email addresses, or credential-shaped
  tokens anywhere in the repository. Use `<User>`, `%USERPROFILE%`, or `$HOME`.
- Do not copy a real machine's configuration into an example. Examples use neutral
  placeholders.
- The privacy scan in the validator covers `.md`, `.json`, `.ps1`, `.py`, `.yaml`, `.yml`,
  and `.txt`. It is a backstop, not permission to be careless in other file types.

## Scripts

- Installers must not overwrite without an explicit `-Force` flag, and must support
  `-WhatIf`.
- Use `-LiteralPath` for every filesystem operation. Set `$ErrorActionPreference = 'Stop'`.
- `scripts/validate-pack.py` is stdlib-only. Adding a dependency means every contributor
  and every CI runner needs it; the check is not worth that.

## Language

- `draft` skills may be written in any language.
- `beta` and `stable` skills must be English-primary; the validator enforces at least 70%
  ASCII in the description.
- `README.md`, `docs/workflow.md`, and `docs/workflow-fidelity.md` are mirrored in Chinese
  as `*.zh-CN.md`. Change both halves together or neither.
- Operational docs (`compatibility.md`, `trigger-tuning.md`, `release-checklist.md`,
  `skill-authoring-standard.md`) are English-only by design. Do not add partial mirrors.

## Commits

- One structural concern per commit. A rename, a tier promotion, and a content rewrite are
  three commits.
- Do not commit with a red validator.
