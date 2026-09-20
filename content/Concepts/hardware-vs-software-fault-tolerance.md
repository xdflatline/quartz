---
title: "Hardware vs Software Fault Tolerance"
details: "The architectural contrast between hardware-based fault tolerance (hot-swappable CPUs, specialized networking, co-located machines — reliable but expensive, narrow in scope, blind to software defects like kernel panics and divide-by-zero) and software-based fault tolerance (Durable Execution platforms — reliable against any failure source, deployable on commodity VMs/containers, cloud-native). Durable Execution is the explicit software-side successor to hardware fault tolerance and subsumes it: it survives both hardware crashes and software defects with the same mechanism."
tags:
  - concept
  - runtime
  - architecture-pattern
created: 2026-09-10
updated: 2026-09-10
type: concept
sources:
  - ".Raw/temporal-what-is-durable-execution-2026-09-10.md"
---

# Hardware vs Software Fault Tolerance

**Source:** Temporal Blog ([[Raw/temporal-what-is-durable-execution-2026-09-10]])
**Category:** Architecture Pattern
**Status:** Production-validated (hardware fault tolerance: decades; software fault tolerance via Durable Execution: 2019–)

---

## Overview

For decades, "reliable system" meant "expensive hardware": machines with hot-swappable CPUs and memory, specialized networking, physical co-location, redundant power supplies. This made sense when downtime cost more than the hardware. It also had two structural limits: hardware fault tolerance **cannot eliminate failure** (it can only reduce its likelihood) and **cannot protect against software defects** (a divide-by-zero or kernel panic kills the process regardless of how many CPUs are available to swap).

Durable Execution is the **software-side successor**. By virtualizing execution and reconstructing state in a fresh process on crash, the platform absorbs any failure source — hardware, OS bug, application bug, library bug, power outage — with the same mechanism. The hardware concern becomes irrelevant to the application's reliability story.

## Core Content

### Hardware fault tolerance: what it is and where it stops

| Property | Hardware fault tolerance | Software fault tolerance (Durable Execution) |
|---|---|---|
| Failure source covered | Hardware only | Hardware + OS + application + library |
| Failure elimination | Reduces likelihood; never eliminates | Eliminates *consequence* (crash-proof, not crash-free) |
| Required hardware | Hot-swappable CPUs/memory, redundant PSUs, co-located machines, specialized networking | Commodity VMs, containers, any cloud or on-prem |
| Cost model | Linear in downtime-avoidance value | Linear in platform usage; pays off when failure-handling code dominates |
| Scope of protection | Process-level hardware faults | All process-level faults equally |
| Cloud-native? | No — physical proximity required | Yes — works across data centers |

### Why hardware fault tolerance is incomplete

1. **Software defects are the dominant failure mode in modern systems.** Kernel panics, divide-by-zero, uncaught exceptions, library bugs, and memory corruption account for the majority of process crashes. None of these are helped by redundant hardware; the bug fires on every machine identically.
2. **Hardware fault tolerance is bounded by what can physically fail over.** Even the most redundant systems have a finite number of hot spares and a finite failover time. A software-defect crash that propagates before failover (e.g., a panic that takes down a kernel before a heartbeat is missed) defeats the hardware safety net.
3. **It scales badly.** Hot-swappable hardware is expensive, niche, and increasingly hard to source as commodity cloud dominates. Durable Execution platforms run on the same VMs and containers everyone else uses.

### What software fault tolerance buys you

A Durable Execution platform's virtualization of execution means the application does not care which process or machine the current step is running on. The platform can move work to a different machine for any reason — load balancing, hardware degradation, planned maintenance — and the application sees a single, continuous execution. The cost of a hardware failure is zero application-visible state.

This is not an incremental improvement; it is a **categorical change**. The application's reliability story becomes decoupled from its deployment topology.

### The complement, not replacement

Wheeler is explicit: there are still legitimate reasons to use an application database alongside Durable Execution (reporting, analytics, queries). The same logic applies to hardware redundancy for non-workflow workloads: databases, message brokers, and stateless services can still benefit from hot-spare hardware.

The shift is **where reliability is engineered**: from physical infrastructure → into the runtime, and only where the runtime is the natural home for it (i.e., long-running multi-step applications).

## Key Insights

1. **Hardware fault tolerance is a partial answer that dominated before software runtimes could own crash recovery.** Now that they can, the partial answer is obsolete for workflow-shaped workloads.
2. **The defining test for "is this durable execution" is software-defect coverage.** If a kernel panic kills your process and your application continues from reconstructed state, you have it. If the process simply dies, you do not — regardless of how many CPUs you have.
3. **Commodity hardware + Durable Execution platform > exotic hardware + classical app code** for almost every workflow-shaped workload. The cost crossover is well below typical enterprise downtime-avoidance thresholds.
4. **Hardware fault tolerance is not "wrong" — it is *narrow*.** Its correct scope is what cannot be virtualized: bare-metal boot firmware, network fabric, the storage substrate the Durable Execution platform itself sits on.

## Related Concepts

- [[Concepts/durable-execution]] — the umbrella pattern this contrast supports (characteristic #4)
- [[Concepts/durable-checkpoint-record-and-replay]] — Kitaru's software-side state preservation
- [[Concepts/durable-actor-session-sleep]] — AgentOS software-side durability across idle
- [[Concepts/graph-based-workflow-engine]] — graph-based workflow engine (composition; not durable by default)

## References

- Raw Article: [[Raw/temporal-what-is-durable-execution-2026-09-10]]
- Original: https://temporal.io/blog/what-is-durable-execution
