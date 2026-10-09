---
title: "The Three Rules of Distributed Systems"
details: "Sam Newman's distillation of everything that goes wrong in distributed systems down to three causes: (1) information takes time to travel, (2) the thing you want to talk to might not be there, (3) resource pools are not infinite. Borrowed into the opening chapter of *Building Resilient Distributed Systems* (2026) as the practical alternative to the eight fallacies of distributed computing that nobody can remember."
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

Sam Newman's three rules are a mnemonic for the irreducible physics of distributed computing:

1. **It takes time.** Information cannot move instantaneously between two points. A developer controls some of this (payload size, serialization, retry cadence); most of it is outside their control (cabling, BGP routing, public-internet behavior). Quantum entanglement does not change this — it's a read-only phenomenon and not a networking protocol.
2. **Sometimes the thing you want to talk to isn't there.** Even with multiple replicas behind a load balancer, the load balancer itself can fail. Uncontrollable physical events (SAN fires, rabbits chewing through networking ducting between office buildings) can take down any specific instance. You can reduce the probability, you cannot eliminate it.
3. **Resource pools are not infinite.** CPU, memory, IO, queue depth, connection counts — all finite. The vast majority of system outages come from a saturated resource somewhere, often downstream of a retry storm or a cascading dependency.

## Why these three

Newman deliberately contrasts with Sun's *Fallacies of Distributed Computing* (eight items, widely cited but rarely remembered). His claim: when you strip away the proliferation of named failure modes, almost everything collapses into one of these three categories. CAP, PACELC, Byzantine consensus, and other more elaborate frameworks all become easier to discuss once you have the three rules grounded.

## Practical implications

- **Rule 1 (it takes time)** forces you to put numbers on latency budgets, pick sensible timeouts, and accept that "it looks instant from the user" still has measurable floor cost.
- **Rule 2 (it might not be there)** is the basis for timeouts, circuit breakers, retries, and idempotency — none of which would be necessary if everything were reliable.
- **Rule 3 (resource pools are not infinite)** is the basis for back-pressure, load shedding, queue depth limits, and the entire field of capacity planning.

Newman emphasizes that the **most common cause of outages is rule 3**: a downstream component saturates (often because rule 2 caused a retry storm), which then cascades into the next layer.

## Related Concepts

- [[Concepts/fail-open-vs-fail-close]] — Rule 2 + Rule 3 is exactly when you have to choose how to degrade
- [[Concepts/thundering-herd-and-retry-storm]] — The classic Rule-3 cascade
- [[Concepts/idempotency-keys-vs-fingerprints]] — How to retry safely under Rule 2
- [[Concepts/production-is-truth]] — Why "did the request actually arrive?" requires instrumentation rather than assumption