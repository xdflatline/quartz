---
title: "FoundationDB"
details: "An open-source distributed database originally developed by FoundationDB Inc., acquired by Apple in 2015, designed as the first distributed database that is consistent, highly-available, and partition-tolerant (CAP-theorem-respecting). The simulation testing framework FoundationDB built to validate the database's correctness — making every source of non-determinism pluggable so the system could be tested deterministically — became the backbone of the technology at Antithesis. One of the two simultaneous-invention sites of practical DST circa 2010, alongside AWS's internal lock service."
tags:
  - entity
  - database
  - testing
created: 2026-10-16
updated: 2026-10-16
type: entity
sources:
  - .Raw/antithesis-docs-deterministic-simulation-testing-2026-10-16.md
---

# FoundationDB

**Source:** Antithesis Docs ([[Raw/antithesis-docs-deterministic-simulation-testing-2026-10-16]])
**Category:** Project / Tool
**Status:** Production-validated (originally FoundationDB Inc.; since 2015 Apple)

---

## Overview

FoundationDB is an open-source distributed database that bills itself as the first to be consistent, highly-available, and partition-tolerant — resolving the CAP theorem by maintaining strict consistency in the presence of partitions and recovering after the partition heals. It was originally developed by FoundationDB Inc., acquired by Apple in 2015, and is now maintained as an open-source project under Apple.

For this garden, the relevant fact is not the database itself but the **simulation testing framework FoundationDB built to validate the database's correctness**. That framework is the canonical example of the pluggable-non-determinism approach to DST: every source of non-determinism the database depends on (clock, RNG, network, scheduler, disk) is hidden behind an interface so the test harness can substitute deterministic implementations. The same article that introduces DST names FoundationDB as one of the two 2010-era pioneers of the practice — and as the lineage from which Antithesis descends.

## The simulation framework

The FoundationDB testing documentation (`apple.github.io/foundationdb/testing.html#simulation`) describes the framework's structure: the SUT is built so that all non-deterministic components are pluggable; the simulation driver provides deterministic implementations under seed; the workload exercises the database across many schedules; properties (invariants) are checked at every step.

The article's wording: "One approach, popularized by FoundationDB, is to design the system under test so that all nondeterministic components are pluggable."

## Why FoundationDB matters to DST

Three reasons:

1. **It is the original production instance.** The framework was built to make FoundationDB testable, and the lessons learned there are the lessons in the Antithesis docs.
2. **It demonstrates pluggable non-determinism at scale.** A real distributed database, not a toy example.
3. **It is the lineage of Antithesis.** "FoundationDB built a simulation-first testing framework to validate the correctness of their distributed database... That framework became the backbone of the technology at Antithesis."

## Relevant facts at a glance

- **Acquisition:** Apple, 2015
- **CAP position:** consistent, available, partition-tolerant (post-partition healing)
- **DST lineage:** the simulation framework is the origin of Antithesis's technology
- **Open source:** yes, under Apple
- **Documentation pointer:** https://apple.github.io/foundationdb/testing.html#simulation

## Related Concepts

- [[Concepts/deterministic-simulation-testing]] — the umbrella technique FoundationDB pioneered
- [[Concepts/simulation-vs-pluggable-nondeterminism]] — the approach FoundationDB canonically implements
- [[Concepts/total-stack-determinism-via-virtualization]] — the substrate DST depends on
- [[Entities/antithesis]] — the commercialized descendant of FoundationDB's framework

## References

- Raw Article: [[Raw/antithesis-docs-deterministic-simulation-testing-2026-10-16]]
- Original: https://antithesis.com/docs/resources/deterministic_simulation_testing/
- Simulation testing framework: https://apple.github.io/foundationdb/testing.html#simulation
- Project home: https://www.foundationdb.org/
