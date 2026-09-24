---
name: feature-ready
description: >-
  Route a feature request with an already settled outcome, scope, and acceptance criteria
  into planning. Use when further intent clarification is unnecessary; readiness of the
  request does not establish current evidence about existing code.
---

# Feature Ready

## Workflow

1. Confirm that the desired user outcome, scope, exclusions, and acceptance conditions are explicit.
2. Identify any missing evidence needed for planning, especially a current codebase audit when existing code will change.
3. Hand the settled request and known evidence gaps to `implementation-plan`. The planner returns missing code evidence to source investigation before review.

## Boundaries

- Do not use this route to avoid unresolved product decisions or root-cause analysis.
- Do not treat a clear feature request as proof that code tasks are independent.

## Output Contract

Provide the settled feature goal, acceptance conditions, constraints, available evidence, and missing planning inputs. Write the user-facing summary in the user's language.
