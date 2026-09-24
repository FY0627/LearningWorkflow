---
name: root-cause-analysis
description: >-
  Explain a defect's causal chain before a repair plan is written. Use when observed
  failures, regressions, or architectural symptoms require evidence-backed diagnosis
  rather than a patch based on the first plausible explanation.
---

# Root Cause Analysis

## Workflow

1. Record the observed failure, expected behavior, reproduction status, and affected users.
2. List plausible causes, inspect discriminating evidence, and rule them in or out. A 5 Whys chain may help, but only when each link has evidence.
3. Identify the supported cause, contributing conditions, affected behavior, and remaining uncertainty.
4. Pass the diagnosis and repair constraints to `implementation-plan`; request more source investigation if the cause remains unproven.

## Boundaries

- Distinguish a trigger, symptom, and root cause.
- Do not claim a fix has been verified or modify code as part of the analysis.

## Output Contract

Produce a causal report with observations, evidence locations, tested hypotheses, supported cause or unresolved gap, impact, and planning constraints. Write it in the user's language unless requested otherwise.
