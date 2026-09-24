---
name: e2e-verify
description: >-
  Verify complete user journeys against approved acceptance criteria after implementation
  is integrated. Use when behavior must be checked across UI, API, data, or service
  boundaries; visual appearance is evaluated separately by visual-e2e-verify.
---

# End-to-End Verification

## Workflow

1. Read the approved acceptance criteria and identify representative user journeys and failure paths.
2. Run available end-to-end checks or perform documented manual journeys against the candidate revision.
3. Compare actual outcomes with expected behavior, capture evidence, and report gaps to `implementation`.
4. Pass a verified candidate and remaining limitations to `github-actions-ci` when the workflow requires that gate.

## Boundaries

- Do not replace a failed or unavailable journey check with an assumption that unit tests cover it.
- Do not claim visual acceptance from a behavioral test unless visual evidence was separately inspected.

## Output Contract

Report the candidate revision, journeys attempted, expected and observed outcomes, failures, evidence, and unrun scenarios. Write the user-facing report in the user's language.
