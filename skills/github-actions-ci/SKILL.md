---
name: github-actions-ci
description: >-
  Check the repository's required GitHub Actions CI results for an implementation candidate.
  Use when the workflow reaches its repository gate for lint, types, tests, build, or other
  configured checks; do not assume a workflow ran merely because changes were pushed.
---

# GitHub Actions CI

## Workflow

1. Identify the candidate commit or revision and the repository's required checks.
2. Run or inspect CI through the available authorized mechanism. Record each check's actual status and run evidence.
3. Route failed checks with logs and revision details to `implementation` for diagnosis and repair.
4. Pass a candidate onward only when the required checks have actually passed.

## Boundaries

- Do not create a commit or push merely to claim a CI result without authority for that repository operation.
- An absent, queued, or skipped check is not a passing check.

## Output Contract

Report the candidate revision, required checks, run links or evidence, actual statuses, failures, and any checks not run. Write the user-facing report in the user's language.
