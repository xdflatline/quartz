---
title: "Production Is Truth"
details: "Sam Newman's mantra, borrowed from Charity Majors: regardless of what the code says, what the spec says, what the documentation says, or what people believe — the running system in production is the only place the actual behavior of the system lives. Documentation, specs, and code are aspirations; production is ground truth. This anchors the entire observability-first stance Newman takes in *Building Resilient Distributed Systems*."
tags:
  - concept
  - software-engineering
  - infrastructure
created: 2026-10-09
updated: 2026-10-09
type: concept
sources:
  - Raw/pragmatic-engineer-resilient-systems-sam-newman-2026.md
---

## Definition

**Production is truth** is the working principle that the only valid source of truth about how a system actually behaves is the running system in production. Specifications, code, tests, documentation, design docs, and chat threads are *intentions* — they describe what the system is supposed to do. Production describes what it *actually* does. When they disagree, production wins.

## Why it matters for resilience

Without accepting production-as-truth, you can't:

- Diagnose why a system is behaving unexpectedly (because the team's model and the system's model have already diverged).
- Set realistic SLOs (because you don't know what the system actually does under load).
- Decide whether a fix worked (because you're checking against your mental model, not against the system).
- Move toward spec-as-source-of-truth safely (because the safety net is the live system, not the spec).

## How you operationalize it

- **Treat the system as emitting a stream of structured events** (logs, metrics, traces) — Newman uses this phrase directly. From that stream, build higher-level abstractions (traces from spans, SLOs from SLIs).
- **Verify every architectural claim against production**. Newman's example: if your modular structure ends up being a process structure, "I can go look at the networks to find out my architecture." You shouldn't have to, but at least you can.
- **Spec-driven development is only safe if production keeps you honest**. The spec becomes the *target*; production is the *reality*. Drift between them is the signal you act on.

## Origin and propagation

The phrase and the underlying stance are associated with Charity Majors (Honeycomb). Newman uses it as a recurring touchstone — "It's like football is life, production is truth" — and explicitly attributes it when he channels Charity's framing.

## Related Concepts

- [[Concepts/three-rules-of-distributed-systems]] — You can't see the rules firing without production-grade observability
- [[Concepts/cognitive-depth-vs-cognitive-surrender]] — Production is the only antidote to surrender; you have to actually look at it
- [[Concepts/lit-where-good-looks-like]] — Defining "good" only matters if you can also verify against production