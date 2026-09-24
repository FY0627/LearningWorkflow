---
name: codebase-audit-summary
description: >-
  Summarize current source evidence and cross-task dependencies before changing existing
  code. Use after source investigation when planning needs a comparable code baseline,
  producer-consumer map, shared contracts, and known evidence gaps.
---

# Codebase Audit Summary

## Workflow

1. Define the requested change and the investigated source scope. Record a comparable code baseline: a revision plus relevant worktree changes, or an equivalent snapshot when version control is unavailable.
2. Review source-investigation findings and trace affected interfaces, data fields, configuration, shared state, producers, and consumers. Include UI components and design tokens when they are relevant.
3. If a prior audit exists, compare its baseline with current code. Reinspect changed parts and unchanged consumers they may affect. Without a comparable prior baseline, investigate the task and its dependency scope afresh; expand only when shared dependencies lead farther.
4. Record source locations, dependency relationships, and unresolved gaps. Use runtime or test evidence when dynamic access prevents reliable static tracing.
5. Hand the scoped audit to `implementation-plan` only with a clear account of which dependency questions are resolved and which still need investigation.

## Boundaries

- Keep the audit scoped to the planned work; do not imply that a partial audit covers the entire repository.
- A file search with no match or a technology inventory is not proof that tasks are independent.
- Do not mark a material unknown dependency as absent or imply that an old summary still covers changed code.

## Output Contract

Provide the code baseline and comparison status; investigated scope; source evidence locations; affected contracts and producer-consumer relationships; shared dependencies; independence evidence or unresolved gaps; and any relevant project conventions. Write the user-facing summary in the user's language.
