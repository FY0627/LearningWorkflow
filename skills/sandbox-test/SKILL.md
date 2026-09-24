---
name: sandbox-test
description: >-
  Verify candidate implementation changes in an isolated local environment before shared
  integration. Use for relevant unit, component, or service checks when a runnable project
  and suitable test commands are available.
---

# Local Sandbox Testing

## Workflow

1. Identify the candidate revision, changed behavior, relevant test commands, and required environment.
2. Run applicable checks in a local or isolated workspace without changing production state.
3. Capture exact commands, results, failures, and limitations. Investigate failures enough to route them to `implementation`.
4. Hand verified results and unresolved risks to the next applicable integration task.

## Boundaries

- A green subset of tests is not proof that every user scenario works.
- Do not mark an unrun check as passed or use a claimed pass rate in place of actual results.

## Output Contract

Report the candidate revision, environment, checks run, pass and fail results, unrun checks, and next action. Write the user-facing report in the user's language.
