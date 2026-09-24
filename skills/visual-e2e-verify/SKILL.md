---
name: visual-e2e-verify
description: >-
  Inspect rendered UI for visual and interaction-state defects after frontend work is
  integrated. Use for layout, typography, responsive behavior, focus states, and visible
  regressions; full user-journey behavior belongs to e2e-verify.
---

# Visual Verification

## Workflow

1. Identify the candidate revision, intended design, supported screens, and relevant UI states.
2. Inspect the rendered result at viewport sizes and content lengths that matter to the product. Check layout, legibility, overflow, focus, and visible interaction feedback.
3. Capture observed evidence and defects. Route UI defects to `frontend-components` or `implementation` for repair.
4. Pass the visual result and remaining limitations to `e2e-verify` when a user-journey check is required.

## Boundaries

- Do not claim a screen passed without inspecting it.
- Do not use a visual check as evidence that backend behavior or a complete user journey works.

## Output Contract

Report the candidate revision, inspected screens and states, viewports or devices used, observed pass and fail results, evidence locations, and uninspected cases. Write the user-facing report in the user's language.
