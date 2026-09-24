# UI Design Decision Guide

Load this guide only when creating a new visual direction or assessing design choices without an established project design system. Product requirements, accessibility needs, and explicit user direction take precedence.

## Start with the user task

- Make the main action and information hierarchy easy to find. Remove decoration that competes with the task.
- Choose type, spacing, and color for legibility and hierarchy. Use fonts already licensed or available in the project before adding a remote dependency.
- Make controls and content adapt to their container and expected text lengths. Inspect relevant narrow and wide layouts rather than relying on one fixed viewport.
- Preserve semantic elements, keyboard focus, contrast, and clear interactive states.

## Challenge common visual shortcuts

- Use a dashboard layout when the user actually needs monitoring or comparison, not as a default page shell.
- Avoid cards, icons, pills, gradients, glow, and grid backgrounds that add no meaning or weaken readability.
- Keep nesting shallow enough that structure, focus order, and responsive behavior remain understandable.

## Use design tokens deliberately

- Inspect the existing design system before adding new colors, type scales, spacing, radii, or shadows.
- Centralize values that repeat across components. Do not add a full token system for a one-off value.
- Validate the rendered result against the product's actual content, states, and accessibility needs.
