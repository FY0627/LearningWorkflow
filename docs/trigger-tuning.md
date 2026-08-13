# Trigger Tuning

The `description` field is the only part of a skill the model reads when deciding whether
to load it. Everything else in `SKILL.md` is invisible until that decision has already
been made. A perfect body behind a vague description never runs.

## The formula

```
<Capability sentence: what this produces.>
Use when the user asks about <dense list of concrete trigger terms>.
```

Two sentences. The first states the deliverable in the imperative. The second is a keyword
surface — the terms a real user would actually type, including synonyms, tool names, file
names, and error strings.

Non-English trigger terms belong inline in that list when users type them. A skill whose
users say "需求澄清" should contain `需求澄清` even though the description is otherwise
English. Terms are matched, not translated.

## Length

120–500 characters at `stable`. The floor is not decoration: under about 120 characters
there is not enough surface for the model to distinguish this skill from an adjacent one.
The ceiling exists because every skill's description sits in context on every request.

## Write both lists before writing the description

For each skill, write these out first. They are the input to the description, and they are
also what [`../examples/dry-runs.md`](../examples/dry-runs.md) tests.

**Should trigger**
- Phrasings a user would plausibly type that this skill is the right answer to.
- Include at least one that does not share vocabulary with the skill's name.

**Should not trigger**
- The neighbouring skill this one is most likely to be confused with, and why the boundary
  falls where it does.
- A superficially similar request that this skill would handle badly.

If you cannot write the second list, the skill's boundary is not yet decided, and no
amount of description tuning will fix that.

## Neighbours in this pack

These pairs sit closest together and are the ones most likely to mis-trigger. Each pair
needs an explicit boundary sentence in both descriptions before either reaches `stable`.

| Pair | Boundary question |
|---|---|
| `clarify-intent` / `requirements-spec` | Eliciting the intent vs. writing it down as a spec |
| `fix-issue` / `root-cause-analysis` | Routing a defect vs. diagnosing it |
| `report-source` / `codebase-audit-summary` | Investigating source vs. producing the audit artifact |
| `visual-e2e-verify` / `e2e-verify` | Does it look right vs. does it work |
| `agents-md` / `telemetry-global-memory` | Written conventions vs. observed runtime lessons |
| `implementation` / `subagents-overview` | Doing the work vs. decomposing it |

## Failure modes

- **Over-triggering.** The description lists generic engineering vocabulary, so the skill
  loads on unrelated work and burns context. Fix by removing generic terms, not by adding
  negations — the model does not reliably act on "do not use this for X".
- **Under-triggering.** The description only contains the skill's own name restated. Fix by
  adding the words users actually type.
- **Silent overlap.** Two skills share a trigger surface and the model picks arbitrarily.
  Fix by moving the boundary into both descriptions, in the same commit.
