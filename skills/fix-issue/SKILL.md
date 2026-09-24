---
name: fix-issue
description: >-
  Triage a reported defect and collect reproducible evidence before root-cause analysis or
  requirements work. Use for errors, regressions, or incorrect behavior; this routing node
  does not authorize an immediate patch.
---

# Fix Issue

## Workflow

1. Record expected and actual behavior, reproduction steps, environment, and observed impact.
2. Inspect available logs, failing checks, and relevant source locations. Record what was actually observed and what remains unverified.
3. Route causal uncertainty to `root-cause-analysis`. Route unclear intended behavior to `requirements-spec`.

## Boundaries

- Do not treat an error message or suspected file as a proven root cause.
- Do not bypass planning and human approval merely because the request is called a bug fix.

## Output Contract

Provide reproduction status, exact evidence locations, affected behavior, known constraints, open questions, and the next evidence node. Write the user-facing summary in the user's language.
