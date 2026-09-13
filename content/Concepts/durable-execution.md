---
title: "Durable Execution"
details: "Crash-proof execution: a runtime abstraction that insulates application code from process, machine, and software failures by virtualizing execution across processes and machines, transparently resuming after crashes with reconstructed state. Originated and named by Temporal; the term generalizes to any platform (Temporal, Kitaru, AgentOS sleep/wake) that delivers crash-proof execution as a first-class abstraction rather than asking developers to engineer retry/state-save/resume logic themselves."
tags:
  - concepts
  - runtime
  - architecture-pattern
  - durable-execution
created: 2026-09-10
updated: 2026-09-10
type: concept
sources:
  - ".Raw/temporal-what-is-durable-execution-2026-09-10.md"
---

# Durable Execution

**Source:** Temporal Blog ([[Raw/temporal-what-is-durable-execution-2026-09-10]])
**Category:** Architecture Pattern
**Status:** Production-validated (Temporal since 2019; generalized framing 2025-2026)

---

## Overview

Durable Execution is **crash-proof execution**: a runtime abstraction that insulates application code from process, machine, and software failures so that a developer writes code for the goal rather than for every failure mode that might occur along the way. The term originates with Temporal, but the underlying pattern — durable state + automatic resume + record/replay — appears in several distinct runtimes (Temporal Workflows, Kitaru's `@flow`/`@checkpoint`, AgentOS actor sleep/wake, Microsoft Orleans virtual actors, AWS Step Functions, Inngest). What unifies them is that **the runtime owns crash recovery**, not the application code.

The Wikipedia article on software fault tolerance cites Flaviu Cristian's estimate that failure-handling code accounts for **more than two-thirds** of the code in a production system. Durable Execution's central economic claim is that this ratio flips: the developer writes goal-shaped code, and the runtime absorbs the other two-thirds.

> Failures are inevitable. Durable Execution makes them inconsequential. — Tom Wheeler, Temporal

## Core Content

### The Definition

> Durable Execution is crash-proof execution. — Wheeler, 2026-05-06

A crash *can* still happen. The claim is that the crash is **inconsequential** — the application's externally-observable progress is unaffected. Analogy: a waterproof watch does not prevent you from falling into a swimming pool; it guarantees the watch continues running despite it.

### A Durable Execution Platform

A platform delivers this abstraction through one core runtime primitive, usually called a **workflow** (the term is universal but not universal in name — some platforms say "flow," "function," "actor"). Importantly, **most systems called "workflow engines" are *not* Durable Execution platforms** — they manage step ordering but do not guarantee crash-proof resume. The defining test: if the host process crashes mid-workflow, does execution transparently resume from the recorded state, or does the developer have to write recovery code?

### The Four Universal Characteristics

Wheeler argues that platforms vary in implementation but the user-facing contract has exactly four characteristics. All four apply to every Durable Execution platform.

#### 1. Virtualized execution

Execution is decoupled from any single process or machine. A single logical execution can span many physical processes on different machines. If the current process crashes, work resumes transparently in a new process with **the same variable values** it had at the crash point — including the results of steps that already completed. The developer does not write recovery code; the runtime reconstructs state and continues.

This is the load-bearing characteristic. Without it, none of the others are possible.

#### 2. Time independence

A single execution can run for seconds, hours, days, or years. The runtime handles long sleeps natively: a `sleep(Time.days(180))` call suspends the workflow without holding a process, and the platform wakes it when the timer fires. This replaces the external-scheduler-plus-application-database pattern that developers otherwise reach for to express "do X in 6 months."

API calls within the workflow can also await external results for arbitrarily long periods without consuming resources.

#### 3. Automatic state preservation

All variables in the application — including local variables, not just persisted records — are durable across crashes. Developers do not write code to copy values into a database and load them back later. The runtime captures state at the boundaries of side-effecting operations and replays it on resume.

The platform replaces the *crash-protection use* of an application database. A database may still be used for legitimate reasons (reporting, analytics, queries), but it is no longer needed as a defensive state-store for the running workflow.

#### 4. Hardware agnosticism

Reliability is built into the **software**, not the hardware. Applications run on commodity VMs, containers, or any cloud environment. The platform does not require hot-swappable CPUs, specialized networking, co-located hardware, or any specific topology. Crashes from software defects (divide-by-zero, kernel panic) are handled identically to crashes from hardware failures (power outage, disk failure).

This is in deliberate contrast to traditional fault-tolerant systems that achieved reliability through exotic hardware with limited ability to handle software-induced failures.

### The Three Developer Benefits

| Benefit | Mechanism |
|---|---|
| **Reliability** | Fault tolerance is provided by the runtime, not engineered case-by-case |
| **Code simplification** | Goal-shaped code replaces retry/timeout/save-load/scheduler plumbing |
| **Velocity** | No need to write, test, or maintain the defensive failure-handling code |

### Where The Boundary Is

Durable Execution is **not** the same as:
- **Hardware fault tolerance** — it subsumes it; hardware is one of many possible failure sources.
- **A workflow engine** — most workflow engines provide step ordering without crash-proof resume.
- **An event-sourcing / CQRS architecture** — those store events for replay/audit; Durable Execution stores state for crash-resume. The primitives overlap conceptually but the user contract differs.
- **A database** — a database persists data; Durable Execution persists *execution*. The two coexist and complement each other.

## Key Insights

1. **The platform owns crash recovery, not the developer.** This is the architectural inversion that defines the pattern. The cost-of-ownership math follows from it: if failure-handling is two-thirds of code, removing it from the developer is a 3x productivity lever.
2. **Crash-proof ≠ crash-free.** Crashes still happen; they are simply unobservable to the application. The runtime absorbs them.
3. **All four characteristics are load-bearing together.** Virtualization without time-independence forces the developer back to external schedulers. Time-independence without automatic state forces them to manually save/load. Either alone gives back some of the two-thirds.
4. **The "workflow" name is implementation detail.** Some platforms call the primitive a flow (Kitaru), an actor (Orleans), or a function (Step Functions). The defining test is the four-characteristic contract, not the vocabulary.
5. **Durable Execution ≠ persistence of application data.** Reporting, analytics, queries still need a database. The pattern removes the database's *crash-protection* role, not all of its roles.

## Related Concepts

- [[Concepts/durable-checkpoint-record-and-replay]] — Kitaru's specific realization of characteristic #3, with explicit `@checkpoint` decorator for fail-as-data semantics
- [[Concepts/graph-based-workflow-engine]] — Mastra's graph-based workflow engine (composition primitives, not durable by default)
- [[Concepts/durable-actor-session-sleep]] — AgentOS's actor sleep/wake model: durable filesystem + history across idle timeouts
- [[Concepts/hardware-vs-software-fault-tolerance]] — the architectural contrast characteristic #4 makes
- [[Concepts/faithful-replay-with-isolated-change]] — what recording enables once state is automatic
- [[Concepts/coordinator-worker-task-dag-orchestration]] — orchestration topology that durable execution can host

## Related Entities

- [[Entities/temporal]] — the platform that named and popularized the pattern

## References

- Raw Article: [[Raw/temporal-what-is-durable-execution-2026-09-10]]
- Original: https://temporal.io/blog/what-is-durable-execution
- Wheeler's talk at Replay '25 London: https://temporal.io/resources/on-demand/durable-execution-this-changes-everything
- Cristian, F. *Reliable Computer Systems* — cited for the "two-thirds of code is failure-handling" estimate
