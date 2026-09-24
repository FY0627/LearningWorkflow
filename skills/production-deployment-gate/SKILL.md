---
name: production-deployment-gate
description: >-
  Decide whether a verified candidate is ready for a production release. Use after required
  CI checks pass to examine release scope, operational readiness, and approval; entering
  this gate does not itself deploy software.
---

# Production Deployment Gate

## Workflow

1. Confirm the candidate revision, approved release scope, and evidence that required CI checks passed.
2. Review deployment prerequisites, compatibility effects, recovery readiness, and known security-audit status.
3. Present the release decision and unresolved risks to the authorized operator. Execute deployment only when the applicable authorization and deployment mechanism are available.
4. Record the actual release result or held state for telemetry and closeout.

## Boundaries

- Do not describe pending security work as passed or assume CI alone settles a release decision.
- Do not claim production deployment occurred when only a gate review was completed.

## Output Contract

Report the candidate revision, required evidence, known risks and audit status, release decision, authorization, actual deployment status, and recovery entry point. Write the user-facing report in the user's language.
