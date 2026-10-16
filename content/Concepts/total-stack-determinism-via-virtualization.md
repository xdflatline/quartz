---
title: "Total-Stack Determinism via Virtualization"
details: "The foundational mechanism of deterministic simulation testing: every source of non-determinism the system under test depends on — hardware clocks, thread scheduling, system entropy, network timing, disk ordering — is replaced by a virtualized counterpart that the test harness can control. The same seed then produces the exact same execution; bugs are reproducible from seed + timeline alone. Built into FoundationDB's simulation framework and into Antithesis as a deterministic hypervisor. Distinct from partial-determinism approaches (record-and-replay) which capture determinism only at explicit boundaries."
tags:
  - concept
  - architecture-pattern
created: 2026-10-16
updated: 2026-10-16
type: concept
sources:
  - .Raw/antithesis-docs-deterministic-simulation-testing-2026-10-16.md
---

# Total-Stack Determinism via Virtualization

**Source:** Antithesis Docs ([[Raw/antithesis-docs-deterministic-simulation-testing-2026-10-16]])
**Category:** Architecture Pattern
**Status:** Production-validated

---

## Overview

Total-stack determinism is the mechanism that makes deterministic simulation testing actually deterministic. The system under test does not run on real hardware, OS scheduling, OS entropy, real networking, or real disk; it runs on virtual counterparts at every layer the SUT touches. The hypervisor (or simulation framework) produces the same execution for the same seed, by construction. The effect is that any bug found during a DST run is reproducible from the seed and the timeline — there is no need to reproduce the field conditions, the network was never real.

## What gets virtualized

| Layer | Real source of non-determinism | Virtualized counterpart |
|-------|--------------------------------|--------------------------|
| Hardware | Wall-clock time, interrupt timing, NUMA effects | Virtual clock / TSC |
| Kernel | Thread scheduling, syscall ordering | Deterministic scheduler |
| System library | `getrandom`, `/dev/urandom`, `time()` | Seeded entropy from harness |
| Network | Packet timing, loss, reorder, partition | Virtual network under harness control |
| Disk | I/O ordering, latency, partial writes | Virtual block device, ordered, replayable |

The article's framing: "Running the system in an entirely virtual environment to allow deterministic execution and replay for debugging purposes." The word *entirely* is the load-bearing one — every layer that the SUT touches must be virtualized, otherwise the same seed does not reproduce the same execution.

## Why it has to be total

If any layer remains real, the seed is no longer a sufficient description of execution. To reproduce a bug you would also need to reproduce the wall-clock time, the kernel's scheduler state, the `/dev/urandom` output, the network's atmospheric conditions. The test would no longer be self-contained; runs would diverge.

Concretely: a real network reorders packets nondeterministically. If only one layer of the stack is virtualized and the network is real, the same seed can produce different orderings of messages on different runs — the bug appears on Tuesday, disappears on Thursday. Total-stack virtualization removes that risk by making the network part of the determinism contract.

## Seeded entropy, not zero entropy

A common misconception: "deterministic" means "no randomness." It does not. The SUT and the workload still need to consume randomness — clocks drift, fuzzers generate inputs, thread interleavings are sampled, fault schedules are picked. What changes is *where that randomness comes from*: it is fed from the seed rather than from the OS, so the randomness still produces varied behavior across runs (many seeds) while remaining exactly reproducible within a run (one seed).

The Antithesis article phrases it precisely: "Carefully feeding the system entropy such that the system and workload can still appear to have random behavior, while at the same time being perfectly reproducible."

## How total-stack determinism is achieved

Two paths:

1. **Pluggable non-determinism in the SUT.** FoundationDB built its SUT with every non-deterministic source behind an interface. Tests inject deterministic versions. The determinism is engineered into the SUT.
2. **Deterministic hypervisor around ordinary SUT.** Antithesis runs regular, unmodified software inside a hypervisor that virtualizes the entire stack. The determinism lives in the hypervisor; the SUT does not change.

Path 1 is more invasive but lighter-weight per test; path 2 is what makes DST retrofittable to systems that were not designed for it. The two are not mutually exclusive — a FoundationDB-style SUT can still benefit from running inside a hypervisor for finer isolation.

## Trade-offs

- **Build cost.** Either you rewrite the SUT to expose interfaces (path 1), or you build and maintain a deterministic hypervisor (path 2). Both are heavy lifts.
- **External dependencies.** A distributed SUT talks to other services, to databases, to message brokers. Those have to be virtualized too, or the determinism contract breaks at the boundary.
- **Performance.** A simulated stack runs slower than bare metal. The article acknowledges that DST is "a complex, resource-intensive undertaking."
- **Compatibility.** Some software depends on real-hardware behavior (e.g., RDMA, GPU drivers) that cannot easily be virtualized. DST may not be a fit there.

## Relationship to other techniques

- vs. **Record-and-replay (Kitaru, Temporal).** Replay runtimes record execution at explicit seam points (LLM calls, tool calls, function checkpoints) and replay serves the recorded outputs. DST virtualizes the whole stack. They solve overlapping problems with different costs: DST is heavier to set up but covers more bugs without needing the engineer to identify the seams in advance.
- vs. **Hypervisor-level snapshotting.** Snapshot-and-restore (Firecracker, qemu snapshot) captures system state but not determinism — restoring from a snapshot at a later wall-clock time gives different results if anything real changed. DST extends the snapshot idea to make the *entire reproduction* deterministic, not just the state at one point.
- vs. **Sandboxes (Firecracker, gVisor).** Sandboxes isolate but do not determinize. DST uses the same mechanism (a virtual machine) but with time, scheduling, and entropy under harness control.

## Related Concepts

- [[Concepts/deterministic-simulation-testing]] — the umbrella technique that total-stack determinism enables
- [[Concepts/simulation-vs-pluggable-nondeterminism]] — the two implementation paths
- [[Concepts/deterministic-first-architecture]] — an adjacent rule about minimizing non-determinism in an architecture

## References

- Raw Article: [[Raw/antithesis-docs-deterministic-simulation-testing-2026-10-16]]
- Original: https://antithesis.com/docs/resources/deterministic_simulation_testing/
- FoundationDB's pluggable approach: https://apple.github.io/foundationdb/testing.html#simulation
