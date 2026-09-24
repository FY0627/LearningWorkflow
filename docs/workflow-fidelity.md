# Workflow Fidelity and Provenance

This document records, node by node, how much of [`workflow.md`](workflow.md) is
replicated from a source workflow and how much is my own design.

It exists because the honest answer is "partly, and here is exactly which parts."
An unattributed replication and an overstated original contribution are the same
failure in opposite directions.

Chinese mirror: [`workflow-fidelity.zh-CN.md`](workflow-fidelity.zh-CN.md).

## Evidence available

The source workflow was available to me only as **redacted screenshots** — node boxes
are visible, most label text is blurred out. Two images: a full-graph view and a
magnified view of the lower half.

I have **no** access to the source repository, source Mermaid, or an unredacted node list.

## Method

Mermaid `flowchart TD` graphs are laid out by dagre. Two properties make the topology
partially recoverable even when the text is unreadable:

1. A child node is always placed at a lower rank than its parent.
2. Nodes at the same rank are the same graph distance from the root, so **two boxes on
   the same horizontal line cannot be parent and child** — they are siblings or unrelated.

Counting boxes per rank therefore reconstructs the shape of the graph, though not its
labels. That is the entire basis for every `inferred` classification below.

## Provenance labels

| Label | Meaning | Count |
|---|---|:--:|
| `replicated` | Label text was legible in the screenshots; I implemented its evident meaning | 14 |
| `inferred` | A box occupies this position at this rank, but the text was redacted. The position is evidence; **the content is my design** | 11 |
| `original` | No counterpart found at this position. My addition | 1 |

`inferred` is the honest majority. It means: I know a node belongs here, I do not know
what the author called it, and everything inside the corresponding skill is mine.

## Node table

### Layer 1 — Intake and routing

| Node | Label | Provenance | Basis |
|---|---|---|---|
| `START` | Request, idea, or existing project | `replicated` | Text fully legible |
| `DECISION` | What does this work need? | `replicated` | Text fully legible |
| `clarify-intent` | Clarify Intent | `replicated` | Leading characters `clar…` legible |
| `fix-issue` | Fix Issue | `replicated` | Leading characters `fix …` legible |
| `report-source` | Source Investigation | `replicated` | `reportSou…` legible |
| `feature-ready` | Feature Ready | `replicated` | Trailing `…eady` legible. Rank placement uncertain — see open question 1 |

### Layer 2 — Evidence and planning

| Node | Label | Provenance | Basis |
|---|---|---|---|
| `requirements-spec` | Requirements Spec | `inferred` | Box at evidence rank, text redacted |
| `root-cause-analysis` | Root Cause Analysis | `inferred` | Box at evidence rank, text redacted |
| `codebase-audit-summary` | Codebase Audit Summary | `inferred` | Box at evidence rank, text redacted |
| `implementation-plan` | Implementation Plan | `inferred` | Box present, text redacted |
| `human-approval` | Human Review & Approval | `inferred` | Two boxes occupy the ranks between the evidence layer and `implementation`, matching plan + approval. **Not original** |

### Layer 3 — Implementation and verification

| Node | Label | Provenance | Basis |
|---|---|---|---|
| `implementation` | Implementation | `replicated` | Text fully legible |
| `subagents-overview` | Subagents Overview | `replicated` | `subagentsOv…` legible |
| `sandbox-test` | Local Sandbox Testing | `inferred` | Box at rank 1 of the parallel section, text redacted |
| `api-backend-agents` | API & Backend Subagents | `inferred` | Box at the rank-2 sync point, text redacted. Assignment of *this* skill to *that* position is my design decision — see design decision 3 |
| `frontend-components` | Frontend Components | `replicated` | `fronten…` legible |
| `code-consolidation` | Code Consolidation | `inferred` | Box at rank 3, text redacted |
| `visual-e2e-verify` | Visual Verification | `inferred` | Box at rank 4, text redacted |
| `e2e-verify` | End-to-End Verification | **`original`** | The source has a single node at this position. I split it into visual acceptance and end-to-end acceptance — see design decision 2 |

### Layer 4 — Gating and closeout

| Node | Label | Provenance | Basis |
|---|---|---|---|
| `github-actions-ci` | GitHub Actions CI | `replicated` | `…thub-actions-ci` legible |
| `production-deployment-gate` | Production Deployment Gate | `inferred` | A box exists directly below the `required checks pass` edge. **Not original** |
| `telemetry-global-memory` | Telemetry & Global Memory | `inferred` | Box below the deployment gate, text redacted |
| `security-audit` | Security Audit | `replicated` | Trailing `…udit` legible |
| `agents-md` | Update Conventions | `replicated` | Text fully legible |
| `organize-docs` | Organize Documentation | `replicated` | Text fully legible |
| `project-closeout` | Project Closeout | `replicated` | Text fully legible |

## Design decisions

These are changes I made deliberately. They are **not** replication, and are not claimed as such.

### 1. `security-audit` is a sibling of `production-deployment-gate`, not its child

In the source screenshot, the deployment-gate box and the security-audit box sit on the
same horizontal line. By the rank property above, they cannot be parent and child — both
are children of `github-actions-ci`.

An earlier replication attempt had chained them: `github-actions-ci → deployment-gate →
security-audit`. That ordering audits software that has already passed its release gate.
Corrected to a fork.

**Open sub-question for a later phase:** siblings means the deployment gate is not
gated on the audit result. Gating release on the audit is arguably stronger than
either arrangement. I have kept the evidence-backed topology rather than substituting
my preference, and flagged it here instead.

### 2. The single verification node is split in two

The source has one node where this workflow has `visual-e2e-verify` and `e2e-verify`.
The split exists because two skills already carried these two responsibilities, and a
24-skill pack pointing at 23 nodes is a defect the validator must be able to catch.

Visual acceptance answers "does it look right"; end-to-end acceptance answers "does it
work end to end". Different evidence, different failure modes.

### 3. The parallel section is braided (2-1-2-1), and the sync node is my assignment

Rank counts in the source's parallel section are **2-1-2-1**: two boxes, then one, then
two, then one. An earlier replication attempt rendered **1-2-2-1** — two straight parallel
rails converging only at the end, with no mid-point sync.

The braided shape is replicated. **Which skill occupies the rank-2 sync point is my
decision**: `api-backend-agents`, on the reasoning that both tracks depend on a stable
API surface before UI work and consolidation can proceed independently. The source's
label there was redacted.

### 4. Two failure edges instead of one

The source has a single labelled failure edge returning to `implementation`. Its origin
point is ambiguous in the screenshot — it sits closer to the CI node's height than to the
verification node's.

Rather than guess at pixels, I resolved this on semantics: `e2e-verify` failing and
`github-actions-ci` failing are different failures with different diagnoses, so they get
separate return edges. **This is design, not replication.**

### 5. Evidence freshness return edges

The dashed `implementation-plan → report-source` and `implementation → report-source`
edges are workflow design additions, not claims about visible edges in the redacted source.
They route missing or stale code evidence back to scoped investigation before a plan is
reviewed, or when relevant unplanned source changes invalidate an approved plan's premises.
`feature-ready` signals that the requested outcome is specified; it does not establish
current evidence about an existing codebase.

## Open questions

1. **`feature-ready` rank placement.** In the source it appears to sit at the evidence
   rank on the far right, reached by a long edge directly from `DECISION`, rather than at
   the routing rank alongside the other three branches. Both readings produce the same
   reachability. Unresolved; current implementation places it at the routing rank.

2. **Redacted labels will stay redacted.** Nothing in the `inferred` column can be
   upgraded to `replicated` without access to the source. If that access never arrives,
   these stay `inferred` permanently. They do not get quietly promoted.

## Rule

An `inferred` or `original` node may never be described as replicated, in this repository,
in a README, in a portfolio, or in conversation. Honest uncertainty outranks false
certainty.
