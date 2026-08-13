# Compatibility and Portability

This pack targets no single agent product. A skill directory here is a plain folder with a
`SKILL.md` and optional `references/`, which is the widest common denominator across agent
runtimes that support skills at all.

## The portability contract

1. **Frontmatter is exactly `name` and `description`.** No vendor keys, no tool
   allowlists, no model pins, no version fields. The validator rejects any extra key.
   Anything a specific product needs goes in a sidecar file inside the skill directory, not
   in `SKILL.md`.
2. **`references/` is one level deep.** No nested directories. Runtimes that flatten a
   skill directory on install still resolve every link.
3. **Links inside `SKILL.md` are relative** and stay inside the skill directory. A skill
   must not link to `../../docs/`, because the install target has no `docs/`.
4. **No executable prerequisites.** A skill states what to do; it does not require a
   binary to be installed to be readable.

## Install targets

`scripts/install.ps1` copies each skill directory into the agent's skills path:

| Target | Path |
|---|---|
| `claude` | `$HOME/.claude/skills` |
| `codex` | `$HOME/.codex/skills` |
| `gemini` | `$HOME/.gemini/config/skills` |

`-Target all` installs to all three. `-DestinationRoot <path>` overrides for anything else.
The script refuses to overwrite an existing skill unless `-Force` is passed, and `-WhatIf`
performs a full dry run.

## Degradation path

If an agent has no skill mechanism at all, the pack still works as documentation:

- [`workflow.md`](workflow.md) is a readable process description on its own.
- Individual `SKILL.md` files can be pasted into a prompt or a project instruction file.
- [`skill-authoring-standard.md`](skill-authoring-standard.md) describes the conventions
  well enough to port the pack to another format by hand.

Nothing in this repository depends on a runtime feature to be useful. That is deliberate:
a workflow that only exists inside one vendor's product is a workflow that expires when
that product changes.

## What is intentionally not here

- **No vendor UI metadata** — display names, colours, default prompts. If a target
  platform wants these, they belong in a per-platform sidecar (for example
  `skills/<name>/agents/<platform>.yaml`), added when that platform is actually targeted.
- **No tool permissions.** Permission policy belongs to the operator's environment, not to
  a portable skill.
- **No model selection.** A skill that only works on one model is a prompt, not a skill.
