---
name: subagents-overview
description: >-
  Map approved implementation tasks to bounded subagent assignments when parallel work is
  useful. Use after an authorized plan identifies task contracts and dependencies; do not
  invent approval or assume that every workflow node needs a separate agent.
---

# Subagents Overview

## Workflow

1. Read the approved task IDs, contracts, dependencies, acceptance checks, and allowed scopes from `implementation`.
2. Identify tasks that can run concurrently based on shared interfaces, state, and files. Keep dependent or unknown-impact tasks sequenced or held.
3. Define each assignment's input, deliverable, change boundary, owner, and integration point.
4. Return the assignment map to `implementation` for runtime dispatch and status control.

## Boundaries

- A task matrix is not permission to spawn agents. Dispatch depends on the host's capabilities and the approved scope.
- Do not split approved tasks into new work that changes contracts or effects without revising the plan.

## Output Contract

Provide a task-to-agent matrix with stable IDs, dependencies, interface contracts, allowed files or components, acceptance checks, and sequencing reasons. Write user-facing content in the user's language.
