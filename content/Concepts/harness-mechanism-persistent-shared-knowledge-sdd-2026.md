---
title: "Harness Mechanism 2 — Persistent Shared Knowledge (SDD)"
details: "H2 of the Diaz et al. (2026) methodological harness. Persistent shared knowledge governs what the team knows across sessions and agents — durable records of decisions, rationale, and outcomes that survive agent restarts and team turnover. Diaz et al. identify it as the loop-closing mechanism: without it, the other mechanisms operate within a session but their products do not survive to compound across the team. Worked example: each completed refund flow writes a persistent entry capturing the design decision (why idempotency under retries), the alternatives considered, and the evidence backing the choice."
tags: [concept, software-engineering, agentic, harness, knowledge-management]
created: 2026-09-13
updated: 2026-09-13
type: concept
sources:
  - "Papers/spec-driven-development-agentic-software-engineering-2026.md"
---

# Harness Mechanism 2 — Persistent Shared Knowledge (SDD)

H2 of the [[Concepts/agentic-harness-team-governance-sdd-2026|methodological harness]] in [[Entities/diaz-2026-sdd-harness-paper|Diaz et al. (2026)]].

## Commitment

The team commits to capturing, in a durable shared store, **what the team knows across sessions and agents**: decisions, rationale, alternatives considered, and the evidence backing each choice.

## Why it is the loop-closing mechanism

[[Raw/sdd-agentic-software-engineering-arxiv-2026|Figure 6]] of the paper shows how the eight mechanisms reinforce each other. Persistent shared knowledge is the one that closes the loop: executable specifications make evidence-backed acceptance possible; evidence-backed acceptance absorbs the volume that N-version generation produces; N-version generation, made safe by working-tree isolation, requires explicit autonomy calibration; calibration is stabilized by normative specifications; these norms accumulate through review and consultation; and the accumulation is written to the persistent-knowledge store. The store, together with the engineered context, is what lets the next session, the next agent, and the next teammate begin where the last one left off.

Without persistent shared knowledge, the other mechanisms still operate within a session, but their products do not survive to compound across the team.

## Worked example (e-commerce refund)

After the refund feature is shipped, the team writes a persistent-knowledge entry capturing:

- the decision that refunds must remain idempotent under network retries;
- the alternatives considered (synchronous reconciliation, saga-pattern rollback, client-side retry token);
- the evidence: load-test results showing the chosen approach handles 10x the peak with no duplicate credits;
- the references: the system specification clause and feature specification that authorized the decision.

A new agent (or a new team member, or a future you) reading this entry can begin work on the adjacent dispute-resolution feature without re-deriving the rationale.

## Related Concepts

- [[Concepts/agentic-harness-team-governance-sdd-2026]] — the harness H2 belongs to.
- [[Concepts/harness-mechanism-context-engineering-sdd-2026]] — H1 loads H2 entries into the next session.
- [[Concepts/harness-mechanism-evidence-backed-acceptance-sdd-2026]] — H4 produces the evidence that H2 stores.
- [[Concepts/harness-mechanism-normative-specifications-sdd-2026]] — H7 captures the norms that H2 accumulates.