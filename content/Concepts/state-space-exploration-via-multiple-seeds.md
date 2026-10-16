---
title: "State-Space Exploration via Multiple Seeds"
details: "The strategy that gives deterministic simulation testing its coverage: the same test (workload + invariants) is run many times against a total-stack-deterministic simulation, each run driven by a different seed that controls entropy, fault schedules, and scheduling choices. A small number of well-chosen properties, exercised across a large number of seeds, covers orders of magnitude more timelines than hand-written example tests. Independent of which property-based testing / fuzzing framework is used for input generation, but typically paired with one — the seed supplies the input-side non-determinism that the framework needs."
tags:
  - concept
  - testing
created: 2026-10-16
updated: 2026-10-16
type: concept
sources:
  - .Raw/antithesis-docs-deterministic-simulation-testing-2026-10-16.md
---

# State-Space Exploration via Multiple Seeds

**Source:** Antithesis Docs ([[Raw/antithesis-docs-deterministic-simulation-testing-2026-10-16]])
**Category:** Testing Strategy
**Status:** Production-validated

---

## Overview

State-space exploration via multiple seeds is how DST achieves coverage without writing thousands of tests. The same test — a workload + a set of invariants — is run repeatedly against a total-stack-deterministic simulation, each iteration driven by a different seed that determines entropy, fault schedules, and scheduling choices. A handful of well-chosen invariants, evaluated across a large number of seeds, covers far more timelines than a much larger number of hand-written example tests could. Every counterexample the system finds comes with the seed and the timeline that produced it — reproducing the bug is just rerunning the simulator with the same seed.

## Why example tests cannot do this

A conventional example test is a single point in the state space. Even a thousand example tests cover a thousand points — still effectively one point each relative to the size of a typical distributed-system state space, which is astronomical. Bugs that depend on a rare interleaving (one particular scheduler choice, one particular network reorder) almost never get exercised by hand-picked examples; they show up in production under load, weeks or months after deploy.

DST's claim: write the invariants correctly once, and let the multi-seed run cover the space for you. The article phrases it as "even if DST is not paired with a full property-based testing approach, DST can find bugs that software developers don't anticipate. An example-based test in a normal testing environment execute a single code path, but that same test, running in a simulation environment with different seeds, may explore different paths."

## How the seed is structured

A DST seed is not a single RNG number. It typically determines:

- The seeded entropy the SUT and the workload consume (random choices the SUT makes)
- The fault schedule (when partitions happen, when a node is killed, when a disk is slow)
- The scheduling and timing choices inside the simulator
- Any input choices the fuzzer / property-based generator makes

Together these dimensions describe a point in the state space. With three seeds covering different subsets of these dimensions, two runs sharing one seed but differing on another reproduce or diverge in predictable ways.

## What the harness does between runs

Between seeds the simulation framework:

- Restores a known-clean state of the SUT (the virtual stack reset, caches flushed)
- Drives the workload with the new seed
- Logs any invariant violations, with the seed and a timeline attached
- Sometimes shrinks counterexamples — given a failing seed, search a neighborhood of similar seeds to find the smallest still-failing variant, because a minimal reproducer is more useful than a maximal one

Minimization is what makes "I have a bug, here is the seed" useful. A minimal seed that still triggers the failure is small enough to commit alongside the fix and run in CI as a regression test going forward.

## How many seeds is "enough"

The article flags state-space exploration as a first-class challenge: "achieving thorough and efficient exploration of the state space – which in most software systems is extremely large – is a complex undertaking as well." Two common answers:

- **Time-bounded fuzzing.** Run for a fixed wall-clock time (hours, days), accept whatever coverage you got.
- **Coverage-guided seeding.** Bias seeds toward runs that reach new code coverage, like a coverage-guided fuzzer. The simulator tracks the coverage each seed achieved and prefers unexplored regions.

Both are usually paired with property-based testing or fuzzing to drive the input side of the exploration. DST provides the substrate (determinism + reproducibility); the fuzzer provides the strategy (which seed to try next).

## The bug-finding contract

When an invariant violation is found under seed `S`:

1. The seed `S` and the full timeline are saved.
2. The bug is reproducible by re-running with seed `S`.
3. A regression test can be added that runs the simulator with seed `S` as a small, fast unit test — the *workflow* is reproducible, not just the *behavior*.
4. The fix is verified by rerunning the same regression test.

This is the structural reason DST finds and fixes bugs that conventional testing cannot: the reproducer is part of the bug report.

## Trade-offs and limits

- **Seed distribution matters.** A naïve multi-seed strategy can waste seeds on inputs the SUT never reaches; the art is in seed scheduling.
- **False positives.** Invariants written too aggressively (e.g., asserting an ordering the system does not guarantee) produce many "bugs" that are actually spec questions. Invariant authoring is itself a skill.
- **Coverage ≠ correctness.** A million seeds that exercise the same code path prove nothing about the paths not exercised. Coverage-guided seeding helps but does not solve the underlying problem.

## Related Concepts

- [[Concepts/deterministic-simulation-testing]] — the umbrella technique this strategy belongs to
- [[Concepts/property-based-testing-paired-with-dst]] — how property-based testing pairs with multi-seed exploration
- [[Concepts/total-stack-determinism-via-virtualization]] — the substrate that makes multiple seeds meaningfully different

## References

- Raw Article: [[Raw/antithesis-docs-deterministic-simulation-testing-2026-10-16]]
- Original: https://antithesis.com/docs/resources/deterministic_simulation_testing/
