---
title: "Harness Mechanism — Review and Consultation (SDD)"
details: "The review/consultation pathway in the Diaz et al. (2026) methodological harness. When an agent encounters a sub-task whose autonomy level (H7) exceeds its grant, it raises a consultation by citing the specification clause it cannot resolve. A human reviewer — possibly a different human than the author of the original brief — answers by reference. This is the mechanism that lets cross-human handover happen under SDD: the consult is routed to the right expert, not to whoever happened to write the original prompt."
tags: [concept, software-engineering, agentic, harness, review]
created: 2026-09-13
updated: 2026-09-13
type: concept
sources:
  - "Papers/spec-driven-development-agentic-software-engineering-2026.md"
---

# Harness Mechanism — Review and Consultation (SDD)

The review/consultation pathway in the [[Concepts/agentic-harness-team-governance-sdd-2026|methodological harness]] of [[Entities/diaz-2026-sdd-harness-paper|Diaz et al. (2026)]].

## Commitment

The team commits to a structured pathway by which an agent that cannot resolve a sub-task against its current [[Concepts/harness-mechanism-autonomy-calibration-sdd-2026|autonomy grant (H7)]] **raises a consultation by citing the specification clause** it cannot satisfy.

## Why "cite the clause" matters

Vibe coding has no consultation pathway: the agent either silently does its best guess or hallucinates a justification. Under SDD, the consultation is a typed request — "I cannot satisfy specification clause S because clause C contradicts it" — that a human reviewer can answer by reference.

This makes cross-human handover work: the agent raised the consult; a different human than the one who wrote the original brief can answer it because the consult is grounded in a citable specification clause. Routing rules and expertise mapping (which the paper highlights as operational implications of the N-to-N topology) become possible.

## Worked example (e-commerce refund)

The agent implementing the refund flow encounters a sub-task that requires changing the ledger schema. Its autonomy record (H7) marks ledger-schema changes as "synchronous sign-off required." The agent halts and raises a consultation: "Specification clause S-states-refunds-must-be-idempotent cannot be satisfied with the current ledger schema; I propose a schema change X."

A human reviewer — possibly the database engineer, not the developer who wrote the original brief — evaluates the proposal against the system specification, approves or rejects, and writes the decision into the [[Concepts/harness-mechanism-persistent-shared-knowledge-sdd-2026|persistent-knowledge store (H2)]].

## Related Concepts

- [[Concepts/harness-mechanism-autonomy-calibration-sdd-2026]] — H7 routes into the review/consultation pathway.
- [[Concepts/harness-mechanism-persistent-shared-knowledge-sdd-2026]] — H2 stores the resolution.
- [[Concepts/specifications-as-contract-substrate-agentic-se]] — the substrate that makes the consultation citable.