---
name: clarify-intent
description: >-
  Clarify an ambiguous feature, change, or problem request before requirements are written.
  Use when the user's desired outcome, affected people, scope, or acceptance criteria are
  unclear; do not ask the user to choose routine implementation details.
---

# Clarify Intent

## Workflow

1. Restate the user's problem, desired outcome, and who experiences it. Separate facts from assumptions.
2. Ask only the questions whose answers could change the outcome, scope, or acceptance criteria. Infer routine technical choices from the project when possible.
3. Record included and excluded behavior, constraints, and observable acceptance conditions.
4. Route a clarified feature request to `requirements-spec`. Route a suspected defect to `root-cause-analysis` when its cause must be established.

## Boundaries

- Do not turn uncertainty about architecture, tools, or styling into unnecessary demands on the user.
- Do not claim source behavior was inspected unless it was. Do not edit code or approve implementation here.

## Output Contract

Provide the confirmed user problem, target outcome, scope, acceptance conditions, unresolved decisions, and next node. Mark assumptions explicitly. Write the user-facing summary in the user's language.
