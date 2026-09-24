---
name: report-source
description: >-
  Investigate existing source code to establish how a requested behavior is produced and
  consumed. Use when planning or diagnosis needs code paths, shared state, interfaces, or
  dependency evidence that cannot be inferred from requirements alone.
---

# Source Investigation

## Workflow

1. Define the behavior or contract under investigation and identify the source snapshot being inspected, including relevant uncommitted changes.
2. Trace entry points, producers, transformations, and consumers across files and configuration. Use runtime evidence when dynamic access makes static references incomplete.
3. Record source locations, observed behavior, and unresolved gaps. Expand the search when a shared contract leads to additional consumers.
4. Send causal findings to `root-cause-analysis` or dependency findings to `codebase-audit-summary`.

## Boundaries

- Absence of a text match is not proof that no dependency exists.
- Do not describe inferred behavior as observed or edit source merely to complete the investigation.

## Output Contract

Provide the investigated question, comparable source baseline, evidence locations, producer and consumer paths, uncertainty, and recommended evidence handoff. Write the user-facing summary in the user's language.
