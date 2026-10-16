---
title: "Simulation vs Pluggable Non-determinism"
details: "The two implementation approaches to deterministic simulation testing. Pluggable non-determinism (FoundationDB approach): engineer the system under test so every source of non-determinism (clock, RNG, network, scheduler) sits behind an interface the test can stub; the test harness controls non-determinism by injecting deterministic implementations. Deterministic hypervisor / simulation (Antithesis approach): run ordinary, unmodified software inside a simulator that virtualizes time, scheduling, and I/O and exposes deterministic counterparts under harness control. The first is more invasive but lighter-weight per test; the second is retrofittable to systems not designed with pluggable interfaces, at the cost of building and maintaining the simulator. Not mutually exclusive — a pluggable SUT can still benefit from a deterministic hypervisor."
tags:
  - concept
  - architecture-pattern
created: 2026-10-16
updated: 2026-10-16
type: concept
sources:
  - .Raw/antithesis-docs-deterministic-simulation-testing-2026-10-16.md
---

# Simulation vs Pluggable Non-determinism

**Source:** Antithesis Docs ([[Raw/antithesis-docs-deterministic-simulation-testing-2026-10-16]])
**Category:** Architecture Decision
**Status:** Production-validated

---

## Overview

The Antithesis article names two distinct ways to make a system deterministic for testing. They differ on **where the determinism lives**: in the SUT's interfaces, or in the layer outside the SUT. Both can achieve DST; they have opposite trade-offs on invasiveness, build cost, and retrofittability.

## Pluggable non-determinism (the FoundationDB approach)

Every source of non-determinism the SUT depends on is hidden behind an interface:

- Clock source → `Clock` interface (real `MonotonicClock`, test `DeterministicClock`)
- Entropy source → `Rng` interface (real `OsRng`, test `SeededRng`)
- Network → `Transport` interface (real TCP, test `DeterministicTransport`)
- Scheduler / I/O → `Executor` interface (real OS, test `DeterministicExecutor`)

In production, the SUT wires in the real implementations. In tests, the harness wires in deterministic implementations driven by a seed. Because the SUT itself does the abstraction, it knows exactly which non-determinism it consumes — and tests can stub exactly those seams.

**Strengths**
- Lighter-weight per test: the simulator is a thin layer inside the SUT, not a hypervisor outside it
- Tests run fast (no full OS-level virtualization)
- Determinism is enforced by construction: if the SUT only consumes non-determinism through the interfaces, it is deterministic by construction
- The SUT becomes testable in isolation — no need for a full deployment

**Weaknesses**
- Invasive: requires the SUT to be *designed* with these interfaces in mind
- Generally impractical for systems already in production: every dependency has to expose a pluggable interface, or be replaced with a deterministic double
- Incomplete: anything the SUT depends on but does not abstract (a third-party library, an OS syscall not behind an interface) re-introduces non-determinism
- Drift: a new dependency added without an interface breaks the determinism contract silently

## Deterministic hypervisor / simulation (the Antithesis approach)

The SUT runs unmodified on top of a deterministic simulation of the underlying stack. The simulator virtualizes the wall clock, thread scheduling, network, disk, and entropy; the test harness controls each layer. The Antithesis article states it as: "Another approach is to run regular non-deterministic software inside a deterministic hypervisor, using a system like Antithesis."

**Strengths**
- Retrofittable: existing production codebases can be brought under DST without rewriting
- Total coverage: every layer the SUT touches is virtualized, so no implicit source of non-determinism can leak in
- Consistent across languages and frameworks: the SUT does not need to be DST-aware
- Independent of SUT choice: switching frameworks or languages does not require re-engineering the determinism layer

**Weaknesses**
- Heavy build cost: building and maintaining a deterministic hypervisor is one of the most expensive engineering tasks in the industry
- Performance: a simulated stack runs slower than bare metal
- Compatibility: some hardware-specific behaviors (RDMA, GPU drivers) are difficult or impossible to virtualize
- External dependencies: a service that talks to a real database is still bounded by the real database; DST only covers the layer that runs inside the simulator

## How to choose

| Situation | Prefer |
|-----------|--------|
| Greenfield project, will ship to production | Pluggable non-determinism. Get the abstractions right at design time; the cost is amortized across the codebase. |
| Existing production system, no DST support | Deterministic hypervisor. The retrofittability outweighs the build cost. |
| Library or framework consumed by others | Pluggable non-determinism. You do not control the deployment; abstractions are the only way. |
| Large, distributed system with many internal non-deterministic sources | Deterministic hypervisor. Even a well-pluggable SUT will leak non-determinism through some path; the hypervisor closes the gap. |
| Small, focused test surface | Pluggable non-determinism. The hypervisor cost is unnecessary for a small surface area. |

The article's own framing: FoundationDB's pluggable approach is "generally impractical for systems already in production." That is why Antithesis exists — to bring DST to systems for which the pluggable approach was not an option.

## The two are not mutually exclusive

A pluggable SUT can still run inside a deterministic hypervisor. The pluggable interfaces give the test harness fine-grained control (this call to the clock returned this value); the hypervisor ensures anything the SUT missed (a kernel-level timer, a syscall the abstraction did not cover) is also deterministic. The two stack; they do not compete.

Most mature DST deployments use both: pluggable for the things they identified during design, and the hypervisor as the safety net for the things they did not.

## Related Concepts

- [[Concepts/deterministic-simulation-testing]] — the umbrella technique
- [[Concepts/total-stack-determinism-via-virtualization]] — the substrate the hypervisor provides
- [[Concepts/dependency-test-edge]] — what to do about the external dependencies a hypervisor cannot reach
- [[Concepts/tla-plus]] — a complementary technique: spec-level proofs of invariants the SUT must preserve

## References

- Raw Article: [[Raw/antithesis-docs-deterministic-simulation-testing-2026-10-16]]
- Original: https://antithesis.com/docs/resources/deterministic_simulation_testing/
- FoundationDB's pluggable testing framework: https://apple.github.io/foundationdb/testing.html#simulation
