---
title: "Harness Mechanism 8 — Normative Specifications (SDD)"
details: "H8 of the Diaz et al. (2026) methodological harness (counted as one of the eight mechanisms; the paper also names autonomy calibration as H7 and review/consultation as H8 in some passages — the exact numbering varies). Normative specifications encode the team's standing norms — coding conventions, error-handling patterns, security baselines, autonomy defaults — as durable, versioned artifacts that the agent must consult. They are the mechanism by which team culture becomes machine-readable. Worked example: the team's normative spec mandates a particular error-handling pattern; the refund agent consults it before implementing."
tags: [concept, software-engineering, agentic, harness, specification, governance]
created: 2026-09-13
updated: 2026-09-13
type: concept
sources:
  - "Papers/spec-driven-development-agentic-software-engineering-2026.md"
---

# Harness Mechanism 8 — Normative Specifications (SDD)

One of the [[Concepts/agentic-harness-team-governance-sdd-2026|methodological harness]] mechanisms in [[Entities/diaz-2026-sdd-harness-paper|Diaz et al. (2026)]].

> **Numbering note.** The paper counts the methodological harness as having eight mechanisms grouped into three functions (knowledge management, production support, governance), but the explicit H1–H8 numbering is applied to: context engineering (H1), persistent shared knowledge (H2), executable specifications (H3), evidence-backed acceptance (H4), N-version generation (H5), working-tree isolation (H6), autonomy calibration (H7), and review/consultation (H8). Normative specifications appear as the standing rules that the autonomy-calibration record consults and the persistent-knowledge store accumulates. The wiki treats normative specifications as a distinct mechanism because it carries its own commitment and worked example in the paper; treat the exact H-numbering as fluid.

## Commitment

The team commits to encoding **standing norms** — coding conventions, error-handling patterns, security baselines, autonomy defaults, observability expectations — as durable, versioned, normative specifications that the agent must consult.

## Why norms must be specifications

Without normative specifications, the agent either:

- has to re-derive every convention from the codebase (expensive and inconsistent across agents), or
- follows a per-session prompt that drifts from session to session.

With normative specifications, the norms are machine-readable, version-controlled, and referenceable. A new agent reading the norms knows the team's error-handling pattern; a reviewer can cite a clause to reject a variant that violates a norm; the persistent-knowledge store can accumulate norm updates with proper attribution.

## Worked example (e-commerce refund)

The team's normative specification includes:

- "All error responses must follow the RFC-7807 problem-details schema."
- "All financial operations must be idempotent under network retries."
- "All public API changes must include a contract test before merge."
- "All sub-tasks that touch the ledger require synchronous sign-off."

The refund agent consults these norms before implementing. When the agent produces a variant that violates the idempotency norm, the [[Concepts/harness-mechanism-evidence-backed-acceptance-sdd-2026|evidence-backed acceptance (H4)]] reviewer rejects it with a citation to the normative clause. The variant's failure is then written into the persistent-knowledge store (H2) as a cautionary example.

## Related Concepts

- [[Concepts/specifications-as-contract-substrate-agentic-se]] — the substrate the norms are encoded into.
- [[Concepts/harness-mechanism-autonomy-calibration-sdd-2026]] — H7 routes through the norms.
- [[Concepts/harness-mechanism-persistent-shared-knowledge-sdd-2026]] — H2 accumulates norm updates.