---
title: "Harness Mechanism 5 — N-Version Generation (SDD)"
details: "H5 of the Diaz et al. (2026) methodological harness. N-version generation is the practice of having multiple agents (or the same agent multiple times) produce independent candidate implementations of the same specification, so the team can compare, audit, and select rather than accept the first output. It is the mechanism that multiplies agent output volume, on the assumption that evidence-backed acceptance (H4) can discriminate among variants. Worked example: three agents independently implement the refund flow from the same feature specification; the team selects the variant whose evidence trail best matches the spec."
tags: [concept, software-engineering, agentic, harness, generation]
created: 2026-09-13
updated: 2026-09-13
type: concept
sources:
  - "Papers/spec-driven-development-agentic-software-engineering-2026.md"
---

# Harness Mechanism 5 — N-Version Generation (SDD)

H5 of the [[Concepts/agentic-harness-team-governance-sdd-2026|methodological harness]] in [[Entities/diaz-2026-sdd-harness-paper|Diaz et al. (2026)]].

## Commitment

The team commits to **producing multiple independent candidate implementations** of a specification — typically by running the same prompt across multiple agents or the same agent multiple times with varied seeds/contexts — and selecting among them rather than accepting the first output.

## Why N-version is the volume generator

Vibe coding produces one output per developer per task. ASE makes it cheap to produce many candidates per task, and Diaz et al. argue the team should lean into that: generate N variants, evaluate each against the [[Concepts/harness-mechanism-executable-specifications-sdd-2026|executable specifications (H3)]], and pick the variant whose evidence trail best matches the spec.

This is the mechanism that produces the volume that [[Concepts/harness-mechanism-evidence-backed-acceptance-sdd-2026|evidence-backed acceptance (H4)]] then absorbs. Without H5 there is no need for H4's automation; without H4 there is no way to evaluate N variants.

## Why isolation is required

N-version generation is only safe when paired with [[Concepts/harness-mechanism-working-tree-isolation-sdd-2026|working-tree isolation (H6)]]: each variant must run in its own isolated environment so the agents cannot trample each other's intermediate state. Without isolation, the variants' side effects contaminate one another and the comparison is meaningless.

## Worked example (e-commerce refund)

Three agents independently implement the refund flow from the same feature specification. Each runs the property-based test, the contract test, and the load test in its own isolated working tree. The team compares the evidence trails:

- Variant A: passes all checks, p99 = 180 ms.
- Variant B: passes idempotency, fails contract test (event schema drift), p99 = 220 ms.
- Variant C: passes all checks, p99 = 140 ms but uses a non-idiomatic pattern that violates a normative specification about error handling.

Variant A is selected; Variant C is rejected on normative grounds; Variant B is sent back for a contract fix.

## Related Concepts

- [[Concepts/harness-mechanism-executable-specifications-sdd-2026]] — H3 is the discriminator.
- [[Concepts/harness-mechanism-evidence-backed-acceptance-sdd-2026]] — H4 is the absorber of the volume H5 produces.
- [[Concepts/harness-mechanism-working-tree-isolation-sdd-2026]] — H6 is what makes H5 safe.
- [[Concepts/harness-mechanism-autonomy-calibration-sdd-2026]] — H7 controls when N-version is triggered vs. a single agent run.