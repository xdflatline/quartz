---
title: "Fault Injection in Simulation"
details: "A DST-internal technique in which faults (process crashes, network partitions, packet loss and reorder, slow disks, partial writes, clock skew) are injected into the simulation under harness control rather than occurring naturally. Because the whole stack is deterministic, an injected fault is reproducible: the same seed reproduces the same crash at the same point. Fault injection in DST is more powerful than chaos engineering (real production systems) because it is exhaustive (every fault schedule is reachable) and reproducible (every discovered misbehavior is a seed-replayable artifact). The article groups fault injection with property-based testing / fuzzing as the two techniques DST is paired with."
tags:
  - concept
  - testing
created: 2026-10-16
updated: 2026-10-16
type: concept
sources:
  - .Raw/antithesis-docs-deterministic-simulation-testing-2026-10-16.md
---

# Fault Injection in Simulation

**Source:** Antithesis Docs ([[Raw/antithesis-docs-deterministic-simulation-testing-2026-10-16]])
**Category:** Testing Technique
**Status:** Production-validated

---

## Overview

Fault injection in simulation is the practice of injecting faults — process crashes, network partitions, packet loss and reorder, slow disks, partial writes, clock skew — into the deterministic simulation under harness control, rather than letting them happen naturally. Because the simulation stack is deterministic, the injected fault is reproducible from the seed: the same crash happens at the same point in the same timeline. The article groups fault injection with property-based testing / fuzzing as the two techniques DST is paired with; together they turn DST into an exhaustive fault-finding system rather than a reproducibility tool.

## What counts as a fault in DST

Anything that would happen in a real production distributed system but is hard to provoke on demand:

- Process kill / restart of any node
- Network partition between any pair of nodes, with arbitrary duration and heal schedule
- Packet loss, duplication, reorder between any pair of nodes
- Slow disk / slow network / slow CPU on a specific node
- Partial writes (a subset of replicas written before the rest)
- Clock skew, leap, or freeze on a specific node
- Erroneous or stale responses from a peer

Each of these is a fault schedule: a timeline of (when, where, what) events. The schedule is part of what the seed parameterizes.

## Why inject faults under DST rather than wait

In production, faults happen at unknown times in unknown orders. Engineers either observe them after the fact (worst case: data loss in production) or run chaos engineering against real systems, which is expensive and risky. DST's claim: provoke the same faults under controlled conditions where a bug is observable, debuggable, and reproducible.

The article makes the productivity case: bugs found in DST prevent "production outages, war rooms, and emergency triage" — they are fixed in the simulator instead of in the alert rotation.

## How fault injection differs in DST vs chaos engineering

| Property | Chaos engineering (production) | Fault injection in DST |
|----------|--------------------------------|------------------------|
| System under test | Production | Simulation |
| Fault trigger | Operator-initiated, often during a controlled window | Driven by the seed, runs every iteration of multi-seed exploration |
| Risk to users | Real | None (no users) |
| Coverage | Whatever the operator remembers to run | Every seed explores a different fault schedule |
| Reproducibility | Sometimes (if a record survives) | Always (the seed is the reproducer) |
| Cost | High (engineer time, risk budgets) | Compute time only |

This is why the article says DST is a complementary shift: not "do DST *or* chaos engineering" but "DST finds what chaos engineering would have caused, before it would have."

## How fault injection composes with property-based testing

Fault injection supplies the *bad events*; property-based testing / fuzzing supplies the *workload that reaches them*. A typical DST run:

1. Property-based framework draws an input (operations to perform)
2. The simulator executes them against the SUT
3. Faults are injected on the schedule
4. Invariants are checked at every step

The bug surface is the intersection: the workload that exposed the system (chosen by the fuzzer / property-based generator) plus the fault that destabilized it (chosen by the harness). Either alone is less powerful — bare workload without faults exercises the happy path; bare faults without a meaningful workload exercise nothing.

## What kind of bug fault injection catches

The article's case for DST — and for fault injection in DST specifically — is distributed-systems bugs whose root cause is a rare ordering:

- "Split brain" recoveries where two nodes briefly both believe they are primary
- Lost writes when one replica ack'd before another crashed mid-write
- Data loss when a partition heals and two divergent histories try to merge
- Stale reads from a node that has not caught up
- Liveness failures where a quorum protocol hangs because the bad partition was the wrong size

Each of these requires a specific fault *plus* a specific workload to trigger; the multi-seed + property-based pairing is what reaches them.

## Limits of fault injection in simulation

- **Faithful fault model.** The injected faults have to match what real systems actually do. A "kill process" that does not flush buffers first tests a different failure mode than a real SIGKILL.
- **Fault coverage.** Even with comprehensive fault models, the *schedule* matters; an unrealistically aggressive fault schedule will not exercise real-world recoveries.
- **Invariant authoring.** The faults only help if invariants catch the misbehavior. A missing invariant is a missed bug.
- **Performance.** The simulation runs slower than bare metal and slower than a chaos experiment that touches real systems. Each faulted run costs compute time.

## Related Concepts

- [[Concepts/deterministic-simulation-testing]] — umbrella technique fault injection lives inside
- [[Concepts/total-stack-determinism-via-virtualization]] — the substrate that makes injected faults reproducible
- [[Concepts/property-based-testing-paired-with-dst]] — the partner technique that supplies the workload
- [[Concepts/hardware-vs-software-fault-tolerance]] — the framing fault injection in DST is a software-fault-tolerance approach
## References

- Raw Article: [[Raw/antithesis-docs-deterministic-simulation-testing-2026-10-16]]
- Original: https://antithesis.com/docs/resources/deterministic_simulation_testing/
- Predecessor: https://www.usenix.org/legacy/event/nsdi09/tech/full_papers/yang/yang.pdf (NSDI 2009, fault injection in MapReduce)
