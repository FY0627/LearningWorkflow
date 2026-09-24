---
name: telemetry-global-memory
description: >-
  Capture observed post-release signals and durable lessons after an actual deployment.
  Use when performance, reliability, or user-outcome data are available for the released
  revision; do not invent measurements or call a planned release deployed.
---

# Telemetry and Global Memory

## Workflow

1. Confirm which revision was deployed, when, and which user outcomes or service signals matter.
2. Collect available post-release observations and compare them with prior baselines or acceptance targets where available.
3. Separate measured results, incidents, hypotheses, and unanswered questions.
4. Record reusable lessons and follow-up work for `project-closeout` and the next cycle.

## Boundaries

- Do not collect private user data merely to fill a telemetry report.
- If no deployment or measurement occurred, record that state instead of fabricating a result.

## Output Contract

Provide the released revision, observation window, signal sources, measured results, limitations, user-impact findings, and follow-up actions. Write user-facing content in the user's language.
