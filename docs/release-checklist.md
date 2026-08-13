# Release Checklist

Every item here maps to a check in [`../scripts/validate-pack.py`](../scripts/validate-pack.py)
or to a decision the validator cannot make. Run the validator first; it covers the
mechanical half in one command.

```
python scripts/validate-pack.py .
```

## Mechanical — the validator proves these

- [ ] `python scripts/validate-pack.py .` exits 0
- [ ] All required files exist (README pair, AGENTS.md, LICENSE, VERSION, CHANGELOG,
      manifest, docs, examples, install script, CI workflow)
- [ ] `VERSION` matches `skill-pack.json`'s `version`
- [ ] `repository` is a real GitHub URL with no placeholder
- [ ] Three-way consistency holds: workflow graph, manifest, and `skills/` agree exactly
- [ ] Every skill passes the checks for its declared tier
- [ ] `maturity_floor` has been raised to match any tier promotions in this release
- [ ] Privacy scan is clean — no user paths, home paths, emails, or tokens
- [ ] `./scripts/install.ps1 -Target all -WhatIf` completes without error
- [ ] CI is green on the branch being released

## Judgement — the validator cannot prove these

- [ ] `CHANGELOG.md` has an entry for this version describing what actually changed
- [ ] No skill was promoted a tier without its body genuinely meeting that tier's intent,
      as opposed to merely satisfying the string checks
- [ ] [`workflow-fidelity.md`](workflow-fidelity.md) still describes provenance accurately;
      nothing was quietly promoted from `inferred` to `replicated`
- [ ] Any new design decision that departs from the source workflow is recorded in
      `workflow-fidelity.md` as a design decision, not presented as replication
- [ ] New or changed descriptions have both a should-trigger and a should-not-trigger list
      worked out, per [`trigger-tuning.md`](trigger-tuning.md)
- [ ] `examples/usage-benchmark.md` was actually run against any skill promoted to
      `stable`, and the score meets the stated bar
- [ ] Every benchmark or dry-run result carries an honest evidence label — a designed
      example is never presented as a real run

## Version bump

- [ ] Decide the version: patch for fixes, minor for new skills or tier promotions,
      major for a breaking change to the workflow graph or the frontmatter contract
- [ ] Update `VERSION` and `skill-pack.json` together in one commit
- [ ] Tag the release only after CI is green on the merge commit
