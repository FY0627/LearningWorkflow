---
name: code-consolidation
description: >-
  Integrate approved changes from parallel implementation tasks into one coherent codebase.
  Use when multiple branches, agents, or modules must be reconciled after their contracts
  and local verification results are available.
---

# Code Consolidation

## Workflow

1. Collect approved task outputs, their revisions, interface contracts, and verification results.
2. Compare changes for conflicts in shared files, data contracts, behavior, and configuration.
3. Merge or refactor within approved scope, preserving intended behavior and tracing any contract deviation back to `implementation`.
4. Run relevant integration checks and hand the consolidated candidate to verification.

## Boundaries

- Do not treat a clean merge as proof of functional compatibility.
- Do not fold unapproved work into the integrated candidate or silently resolve a product decision.

## Output Contract

Report integrated task IDs and revisions, resolved conflicts, changed contracts, verification results, and unresolved risks. Write user-facing content in the user's language.
