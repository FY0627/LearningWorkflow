---
name: skill-name-here
description: >-
  Produce <the concrete deliverable this skill exists to create>. Use when the user asks
  about <trigger term>, <synonym>, <tool or file name>, <error string>, or <非英文触发词>.
---

# Human Readable Skill Name

> This is the authoring template. It is deliberately **not** inside `skills/`, because it
> is not an installable skill. Copy this directory to `skills/<slug>/` and replace every
> angle-bracket placeholder. Rules and tiers: [`../skill-authoring-standard.md`](../skill-authoring-standard.md).

## Workflow

1. Clarify scope before acting. State what you will and will not touch.
2. Load `references/<file>.md` **when** <the exact condition that makes it relevant>.
3. Load `references/<other>.md` **when** <a different, non-overlapping condition>.
4. Produce the deliverable described under Output Contract.
5. State what remains unverified.

Each step is an imperative. Each reference is named together with the condition that
triggers loading it — a reference the model must guess at is a reference it will not load.

## <Domain Rule Section>

Rename this to the risk this skill actually carries: Safety Gates, Privacy Rules, Data
Handling, Rollback Rules. Write conditions and required behaviours, not warnings.

- Never <the specific action that must not happen>.
- Prefer <safe approach> over <risky approach> when <condition>.
- Before <irreversible action>, produce <the artifact that makes it reversible>.

Multi-condition gates are stated as all-must-be-true lists:

Proceed only when all of the following hold:
1. <condition>
2. <condition>
3. <a rollback path is documented>

## Output Contract

Every item must be verifiable by reading the output alone. If a reader cannot tell whether
an item is present, it is not a contract item.

- <Named section the deliverable must contain.>
- <A classification, using the skill's own named taxonomy.>
- <Verification steps: how the reader confirms this is correct.>
- <Rollback steps, where the work is reversible.>
- <What was not done, and why.>

## References

- `references/<file>.md`: <what it holds> — load when <condition>.
- `references/<other>.md`: <what it holds> — load when <condition>.

Keep `references/` one level deep. Keep this file under 220 lines; move detail down a
layer rather than growing this one.
