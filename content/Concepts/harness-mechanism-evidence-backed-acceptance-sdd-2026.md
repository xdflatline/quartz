---
title: "Harness Mechanism 4 — Evidence-Backed Acceptance (SDD)"
details: "H4 of the Diaz et al. (2026) methodological harness. Evidence-backed acceptance is the practice that a human reviewer accepts an agent's output only against concrete evidence (test runs, contract checks, property assertions) rather than against the appearance of correctness. It is the mechanism that absorbs the review-bottleneck volume produced by N-version generation. Worked example: the human reviewer for the refund feature requires the agent to attach the property-based test output, the contract-test output, and the load-test results before accepting."
tags: [concept, software-engineering, agentic, harness, review]
created: 2026-09-13
updated: 2026-09-13
type: concept
sources:
  - "Papers/spec-driven-development-agentic-software-engineering-2026.md"
---

# Harness Mechanism 4 — Evidence-Backed Acceptance (SDD)

H4 of the [[Concepts/agentic-harness-team-governance-sdd-2026|methodological harness]] in [[Entities/diaz-2026-sdd-harness-paper|Diaz et al. (2026)]].

## Commitment

The team commits to **accepting agent output only against concrete evidence** — test runs, contract checks, property assertions, load results — rather than against the appearance of correctness in the diff or the agent's narrative justification.

## Why this is the review bottleneck's antidote

Industrial reports (Faros AI 2025, Qodo 2025) identify **PR review time** as the binding constraint as agent output multiplies. The Faros AI finding of +98% merged PRs alongside +91% PR review time is the headline version of the productivity paradox.

Evidence-backed acceptance replaces "review the diff" with "review the evidence":

- The agent runs the [[Concepts/harness-mechanism-executable-specifications-sdd-2026|executable specifications (H3)]] itself and attaches the output.
- The human reviewer audits the evidence against the specification, not the implementation.
- A failed check is a blocked merge; a passed check with suspicious design is a flagged consultation.

This shifts the human reviewer's effort from re-deriving correctness to auditing evidence, which compresses review time per PR without lowering the bar.

## Worked example (e-commerce refund)

The human reviewer for the refund flow requires the agent to attach, before merge:

- the property-based test output (idempotency assertion passes);
- the contract-test output (event schema matches);
- the load-test result (p99 < 200 ms at 10x peak).

The reviewer checks that the evidence exists, that it is consistent with the feature specification, and that no failing checks were silently ignored. The reviewer does **not** re-derive whether the implementation is correct from the diff alone.

## Related Concepts

- [[Concepts/harness-mechanism-executable-specifications-sdd-2026]] — H3 produces the evidence H4 consumes.
- [[Concepts/harness-mechanism-n-version-generation-sdd-2026]] — H5 generates the volume H4 absorbs.
- [[Concepts/harness-mechanism-review-and-consultation-sdd-2026]] — H8 is the broader pattern of which H4 is the acceptance half.