---
name: api-backend-agents
description: >-
  Implement approved API, service, or database tasks against a settled interface contract.
  Use when backend work is part of an authorized plan and other tracks depend on the
  resulting request, response, or data behavior.
---

# API and Backend Tasks

## Workflow

1. Read the assigned plan task, API or data contract, dependencies, allowed change scope, and acceptance checks.
2. Check shared consumers and existing conventions before changing endpoints, schemas, persistence, or authentication behavior.
3. Implement within the authorized task and verify affected behavior with relevant tests.
4. Report the settled interface, actual changes, test results, and any contract deviation to `implementation` and downstream consumers.

## Boundaries

- Hold a material contract change for plan revision and approval before dependent work proceeds.
- This skill does not require spawning another agent or inventing backend work for a task without it.

## Output Contract

Provide implemented task IDs, endpoint or data contracts, changed locations, compatibility effects, verification results, and unresolved issues. Write user-facing content in the user's language.
