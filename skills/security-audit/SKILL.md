---
name: security-audit
description: >-
  Review an implementation candidate for security defects and sensitive-data exposure.
  Use on the security track after a candidate is available, alongside release governance;
  findings must refer to inspected code and actual checks.
---

# Security Audit

## Workflow

1. Identify the candidate revision, changed components, exposed interfaces, and relevant threat surfaces.
2. Inspect authorization, input handling, data exposure, dependency changes, and secret handling where applicable.
3. Run available security checks, verify findings against source evidence, and distinguish confirmed issues from uncertain leads.
4. Route required fixes to `implementation` and report audit status to release and documentation tracks.

## Boundaries

- Do not present a scan with no findings as proof that no vulnerabilities exist.
- Do not include credentials or private data in reusable audit reports.

## Output Contract

Report inspected scope and revision, methods run, findings with evidence and severity, unresolved coverage gaps, and remediation status. Write the user-facing report in the user's language.
