---
title: "Harness Mechanism 6 — Working-Tree Isolation (SDD)"
details: "H6 of the Diaz et al. (2026) methodological harness. Working-tree isolation is the practice that each agent (or N-version variant) operates in an isolated working tree — a separate filesystem, branch, or sandbox — so candidates cannot trample each other's intermediate state. Without it, N-version generation (H5) is unsafe because variants' side effects contaminate each other. Worked example: each of the three refund-flow variants runs in its own ephemeral branch and ephemeral container; the system spec's standing rule requires isolation for any multi-agent parallel work."
tags: [concept, software-engineering, agentic, harness, isolation]
created: 2026-09-13
updated: 2026-09-13
type: concept
sources:
  - "Papers/spec-driven-development-agentic-software-engineering-2026.md"
---

# Harness Mechanism 6 — Working-Tree Isolation (SDD)

H6 of the [[Concepts/agentic-harness-team-governance-sdd-2026|methodological harness]] in [[Entities/diaz-2026-sdd-harness-paper|Diaz et al. (2026)]].

## Commitment

The team commits to running each agent (or each N-version variant) in an **isolated working tree** — separate branch, separate filesystem, or ephemeral container — so intermediate state cannot leak between candidates.

## Why isolation is non-negotiable for H5

[[Concepts/harness-mechanism-n-version-generation-sdd-2026|N-version generation (H5)]] assumes that comparing variant outputs is meaningful. If variants share filesystem state, the comparison is contaminated: variant B may overwrite variant A's intermediate files; side effects (network calls, DB writes, file emissions) may be partially committed by both; the evidence trails may merge.

Isolation makes each variant a closed experiment: reproducible, attributable, diffable. The team can then compare evidence trails without wondering which output came from which variant.

## Worked example (e-commerce refund)

Each of the three refund-flow variants runs in its own ephemeral branch and ephemeral container. The system specification's standing rule requires isolation for any multi-agent parallel work; the autonomy-calibration record flags a feature as "multi-variant required" only when isolation is confirmed.

After evaluation, the selected variant is merged; the others are discarded. The isolation cost (branch overhead, container spin-up) is amortized across the comparison step that follows.

## Related Concepts

- [[Concepts/harness-mechanism-n-version-generation-sdd-2026]] — H5 is what H6 makes safe.
- [[Concepts/harness-mechanism-autonomy-calibration-sdd-2026]] — H7 records when isolation is required.
- [[Concepts/harness-mechanism-normative-specifications-sdd-2026]] — H7 captures the standing rule that isolation is mandatory for parallel work.