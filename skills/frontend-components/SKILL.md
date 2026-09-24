---
name: frontend-components
description: >-
  Build or revise approved user-interface components against the product requirements and
  settled API contracts. Use for pages, interaction states, responsive layout, and styles;
  respect an existing design system before introducing a new one.
---

# Frontend Components

## Workflow

1. Read the approved task, user scenarios, interface contract, project design system, and acceptance checks.
2. Inspect existing components, tokens, accessibility patterns, and responsive behavior before changing UI code.
3. Build the required states and interactions, then inspect the result across the relevant screen sizes and input methods.
4. Report changed components, observed behavior, and remaining visual or interaction risks to `implementation` and `visual-e2e-verify`.

## Boundaries

- User needs and the project's design system determine visual choices. Do not impose a generic visual theme over explicit product direction.
- A settled API contract may not be changed silently to simplify a component.

## Output Contract

Provide changed components, supported states, responsive and accessibility checks, API assumptions, and verification status. Write user-facing content in the user's language.

## References

- [references/ui-design-rules.md](references/ui-design-rules.md): load when creating a new visual direction or evaluating design choices without an established project design system; use it as guidance under the product requirements.
