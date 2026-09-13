---
title: "Harness Mechanism 3 — Executable Specifications (SDD)"
details: "H3 of the Diaz et al. (2026) methodological harness. Executable specifications are specifications that can be evaluated automatically — acceptance criteria expressed as tests, contracts, or checks that an agent (or a CI pipeline) can run. They transform the specification from a static document into a substrate the agent operates against. Worked example: the refund feature spec includes a property-based test asserting that refund(N) composed with refund(N) under any retry sequence yields a single credit."
tags: [concept, software-engineering, agentic, harness, specification]
created: 2026-09-13
updated: 2026-09-13
type: concept
sources:
  - "Papers/spec-driven-development-agentic-software-engineering-2026.md"
---

# Harness Mechanism 3 — Executable Specifications (SDD)

H3 of the [[Concepts/agentic-harness-team-governance-sdd-2026|methodological harness]] in [[Entities/diaz-2026-sdd-harness-paper|Diaz et al. (2026)]].

## Commitment

The team commits to writing specifications whose acceptance criteria are **evaluable**, not merely readable: tests, contracts, property-based assertions, or other automated checks the agent (or CI) can run.

## Why executability matters

Under SDD, the specification is the substrate the agent operates against. A non-executable specification is, for the agent, just text: it cannot know whether it has satisfied the spec without a human interpreting it. An executable specification is a contract: the agent can run the test, observe the result, and report concrete evidence.

This is also what makes [[Concepts/harness-mechanism-evidence-backed-acceptance-sdd-2026|evidence-backed acceptance (H4)]] possible at team scale. Without H3, every agent output requires a human to decide whether it satisfies the spec; with H3, the team absorbs the volume through automated checks first.

## Worked example (e-commerce refund)

The refund feature spec includes:

- a **property-based test** asserting that `refund(N)` composed with `refund(N)` under any retry sequence yields a single credit;
- a **contract test** verifying that the refund endpoint emits the agreed event schema;
- a **performance assertion** that the p99 refund latency under 10x peak load stays below 200 ms.

When an agent implements the refund flow, it runs these checks as part of its work. When it hands off to a human reviewer, the reviewer can audit the evidence the checks produced.

## Related Concepts

- [[Concepts/specifications-as-contract-substrate-agentic-se]] — the substrate H3 makes evaluable.
- [[Concepts/harness-mechanism-evidence-backed-acceptance-sdd-2026]] — H4 consumes the evidence H3 produces.
- [[Concepts/harness-mechanism-n-version-generation-sdd-2026]] — H5 relies on H3 to discriminate among variants.