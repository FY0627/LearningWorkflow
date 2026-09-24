---
name: requirements-spec
description: >-
  Turn clarified intent or defect expectations into a reviewable requirements specification.
  Use when the user outcome, behavior boundaries, and acceptance criteria must be recorded
  before implementation planning.
---

# Requirements Specification

## Workflow

1. Identify the user problem, affected users, target outcome, and confirmed constraints.
2. Define behavior through scenarios, inputs, outputs, failure cases, and exclusions that matter to the user.
3. State acceptance checks in observable terms. Include performance, accessibility, privacy, or security requirements when relevant to the request.
4. Separate confirmed requirements from assumptions and unresolved choices; return decision-relevant gaps to `clarify-intent`.
5. Hand the specification to `implementation-plan` as product evidence, not as proof of current code dependencies.

## Boundaries

- Do not choose architecture or implementation details merely to fill a template.
- Do not report assumptions as user-approved requirements.

## Output Contract

Produce a requirements document with the problem, users and scenarios, scope and exclusions, functional behavior, relevant quality constraints, acceptance checks, and unresolved decisions. Write it in the user's language unless requested otherwise.
