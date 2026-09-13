---
title: "Harness Mechanism 7 — Autonomy Calibration (SDD)"
details: "H7 of the Diaz et al. (2026) methodological harness. Autonomy calibration is the practice of recording, per task or per task class, the autonomy level an agent is granted: which sub-tasks it may complete without human consultation, which require human-in-the-loop review, and which require synchronous sign-off. It is the mechanism that stabilizes the trust calibration between humans and agents. Worked example: the autonomy record for the refund flow grants the agent permission to write the implementation and run tests, requires human consultation before any change to the public API surface, and requires synchronous sign-off before any change to the ledger schema."
tags: [concept, software-engineering, agentic, harness, autonomy]
created: 2026-09-13
updated: 2026-09-13
type: concept
sources:
  - "Papers/spec-driven-development-agentic-software-engineering-2026.md"
---

# Harness Mechanism 7 — Autonomy Calibration (SDD)

H7 of the [[Concepts/agentic-harness-team-governance-sdd-2026|methodological harness]] in [[Entities/diaz-2026-sdd-harness-paper|Diaz et al. (2026)]].

## Commitment

The team commits to **recording, per task or per task class, the autonomy level** granted to the agent: which sub-tasks it may complete without human consultation, which require human-in-the-loop review, and which require synchronous sign-off.

## Why calibration is needed

ASE shifts the human role from "writer" to "orchestrator and verifier" (Hassan et al. 2025). But "autonomy" is not a binary; it is a calibration:

- some sub-tasks are low-risk (writing tests, generating docs) and can be fully delegated;
- some are medium-risk (refactoring within a module) and benefit from human review;
- some are high-risk (changes to a public API, changes to financial ledgers, changes to security-sensitive code paths) and require synchronous human sign-off.

A team that grants blanket high autonomy loses the safety net; a team that grants blanket low autonomy bottlenecks on every keystroke. Calibration is the practice of **choosing per task class** and **recording the choice** so it is auditable.

## Worked example (e-commerce refund)

The autonomy record for the refund feature:

- **Fully delegated**: writing the implementation against the feature spec; running the executable specifications; emitting the persistent-knowledge entry.
- **Human-in-the-loop review**: any change to a module outside the payments service; any change that affects the public API surface.
- **Synchronous sign-off**: any change to the ledger schema; any change to the idempotency-key generation rule.

The agent reads the record before it acts; a sub-task that triggers a higher autonomy level halts the agent and raises a consultation.

## Related Concepts

- [[Concepts/harness-mechanism-normative-specifications-sdd-2026]] — H7 captures and applies the standing autonomy norms.
- [[Concepts/harness-mechanism-review-and-consultation-sdd-2026]] — H8 is the review/consultation pathway H7 routes into.
- [[Concepts/harness-mechanism-context-engineering-sdd-2026]] — H1 surfaces the autonomy record to the agent.