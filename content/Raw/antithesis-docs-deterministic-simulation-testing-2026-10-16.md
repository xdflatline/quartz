---
title: "Antithesis Docs — Deterministic Simulation Testing"
details: "Antithesis's documentation page introducing deterministic simulation testing (DST) as an advanced testing technique that places software under test in a simulated, deterministic environment. Explains what DST is, how it works (virtualized stack plus seeded entropy plus state-space exploration plus invariant checking), how to implement it (pluggable nondeterminism vs deterministic hypervisor), its strengths and limitations, and the kinds of systems that benefit most (distributed databases, financial engines, infrastructure, blockchains, microservice applications, asynchronous workflows). Anchors the practice at FoundationDB and AWS's internal lock service around 2010, with Will Wilson's 2014 Strange Loop talk as one of the earliest public discussions."
tags:
  - raw
  - documentation
source: https://antithesis.com/docs/resources/deterministic_simulation_testing/
created: 2026-10-16
updated: 2026-10-16
type: raw
---

# Antithesis Docs — Deterministic Simulation Testing

**Source:** [Antithesis Docs](https://antithesis.com/docs/resources/deterministic_simulation_testing/) — *Deterministic simulation testing - how it works and when to use it*
**Retrieved:** 2026-10-16

---

Deterministic simulation testing (DST) is an advanced approach to software testing that enables developers to find and reliably reproduce complex bugs in distributed systems, e.g. bugs caused by concurrency, multi-threading, and timing issues. These types of bugs are notoriously difficult to detect and fix using conventional example-based tests. Of course, DST catches simpler bugs as well!

This article explores how deterministic simulation testing works, how to implement it effectively, and which kinds of systems benefit most from it.

## What is deterministic simulation testing?

Deterministic simulation testing (DST) involves placing software under test in a simulated, deterministic environment.

Simulation testing simulates some or all of a distributed system under test, rather than running the test on real hardware, networks, operating systems, etc. This allows the test harness to control phenomena like the occurrence of faults, on the simulated layers. Simulation testing almost always involves running tests multiple times with different seeds.

In DST, some or all layers of the testing stack are made deterministic, including sources of non-determinism like clocks, thread interleaving, and system-provided sources of randomness (among others). This means bugs can be reliably reproduced, making debugging much easier.

DST is often paired with property-based testing / fuzzing and fault injection.

Practical adoption of this approach was pioneered at FoundationDB and Amazon Web Services around 2010, and seems to have been a case of simultaneous invention, or rather, implementation, since the idea itself predates both these instances. One of the earliest recorded discussions of how to implement DST is Will Wilson's talk at the Strange Loop conference in 2014.

FoundationDB built a simulation-first testing framework to validate the correctness of their distributed database — the first to be consistent, highly-available, and partition-tolerant. That framework became the backbone of the technology at Antithesis.

At Amazon Web Services, Al Vermeulen introduced the approach to test early implementations of AWS' internal lock service.

## How does deterministic simulation testing work?

Deterministic simulation testing relies on:

- Running the system in an entirely virtual environment to allow deterministic execution and replay for debugging purposes.
- Carefully feeding the system entropy such that the system and workload can still appear to have random behavior, while at the same time being perfectly reproducible.
- Exploring the state space of the system — a wide range of inputs and system faults should be simulated to ensure a vast number of possible states are encountered.
- Checking system behaviors and invariants — to determine if the system behaves as expected.

## How do I implement deterministic simulation testing?

One approach, popularized by FoundationDB, is to design the system under test so that all nondeterministic components are pluggable.

Since this requires the system and all its dependencies to be built with deterministic simulation testing in mind, this approach is generally impractical for systems already in production.

Another approach is to run regular non-deterministic software inside a deterministic hypervisor, using a system like Antithesis.

While building a fully deterministic system is often viewed as the main technical challenge, achieving thorough and efficient exploration of the state space – which in most software systems is extremely large – is a complex undertaking as well. This is why DST is often paired with property-based testing / fuzzing and fault injection.

## What are the strengths and limitations of deterministic simulation testing?

Deterministic simulation testing saves developer time and increases engineering productivity, because:

- Bugs found via DST are a lot easier to debug, as execution can be rolled back and inspected at multiple points in time. Compare this to the same test running outside a DST environment: we may see an error, have no information on how to reproduce it, and never see it again.
- DST prevents production outages, war rooms, and emergency triage. Compare the above scenario – being able to fix a rare bug – to one where the bug is observed but allowed to enter production because it's impossible to reproduce. A stitch in time saves nine.
- Even if DST is not paired with a full property-based testing approach, DST can find bugs that software developers don't anticipate. An example-based test in a normal testing environment execute a single code path, but that same test, running in a simulation environment with different seeds, may explore different paths.

However, DST can be challenging to implement.

- Setting up a deterministic simulation environment is a complex, resource-intensive undertaking.
- Not every system can be designed in a way that enables DST to be built around it.
- DST platforms like Antithesis enable most types of software to be tested using DST, but still require external dependencies to be mocked or otherwise plugged to ensure determinism.

## What kinds of systems benefit most from DST?

DST is applicable to any kind of software, but particularly excels at testing complex distributed systems where concurrency, state, and coordination matter. These include:

- Distributed databases (e.g. FoundationDB, MongoDB, and TigerBeetle)
- Financial transaction engines (Formance)
- Distributed systems infrastructure (e.g., WarpStream, Resonate, and Rising Wave).
- Blockchains and consensus protocols (like Sui, developed by Mysten Labs)
- Microservice applications
- Asynchronous workflows
- Any complex business system built on distributed infrastructure.

Bugs in such systems tend to be difficult to detect and replicate with manually written, example-based tests.

## Conclusion

Deterministic simulation testing isn't about writing more tests. In fact, fewer simple tests may end up covering more timelines than many narrow traditional tests. It's about building a testing system that makes even the rarest bugs become fully observable, reproducible, and fixable.

While implementing this approach can be challenging, the return on investment is significant in terms of uptime, peace of mind, and engineering productivity.
