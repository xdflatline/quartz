---
title: "Graph-Shaped Observability"
details: "Graph engineering principle that a chat transcript is a terrible dashboard for a distributed system. Once a workflow is graph-shaped, the metrics must be graph-shaped too: critical-path latency, node failure rate, retry rate, verifier kill rate, fan-out efficiency, compression ratio, human intervention rate."
tags:
  - concepts
  - agent
  - orchestration
  - observability
created: 2026-09-02
updated: 2026-09-02
type: concept
sources:
  - .Raw/lunarresearcher-graph-engineering-2026-08-10.md
---

# Graph-Shaped Observability

**Source:** [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Proposed best practice

## Overview

A chat transcript is a terrible dashboard for a distributed system. Once a workflow becomes graph-shaped, the metrics must be graph-shaped too. The article names seven metrics; the list is a useful starting set, not a complete one.

## Core Content

### The Seven Metrics

**1. Critical-path latency**
How long is the longest dependency chain? This tells you where the actual waiting lives.

**2. Node failure rate**
Which workers fail most often? This catches brittle tools and bad prompts.

**3. Retry rate**
A graph that "succeeds" after four retries per node is not healthy.

**4. Verifier kill rate**
If the verifier rejects 0% of outputs, it may be useless. If it rejects 80%, your workers may be poorly scoped.

**5. Fan-out efficiency**
How many parallel workers produced unique useful information? This is your signal-to-width ratio.

**6. Compression ratio**
How much raw material is removed before final synthesis? If 200 outputs become 18 useful findings, the reducer is doing valuable work.

**7. Human intervention rate**
Where do people still need to rescue the system manually? Those are your next architecture targets.

### The Reframe

> You are no longer tweaking prompts based on vibes. You are optimizing a machine.

## Key Insights

1. **The dashboard is the graph, not the chat** — chat-shaped logs hide the structure.
2. **The metrics are simple but they are not the chat** — every one is a property of the topology, not of any single model.
3. **Human intervention rate is the leading indicator** — wherever humans are still rescuing the system, that is your next architecture target.

## Related Concepts

- [[Concepts/graph-engineering-discipline|Graph Engineering]] — umbrella
- [[Concepts/critical-path-latency|Critical Path Latency]] — the first metric
- [[Concepts/observational-memory-pattern|Observational Memory Pattern]] — adjacent observability pattern
- [[Concepts/compression-ratio|Compression Ratio]] — one of the seven metrics
- [[Concepts/fan-out-efficiency|Fan-out Efficiency]] — another of the seven

## References

- Raw Article: [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
- Original: https://lunarresearcher.substack.com/p/graph-engineering-the-complete-guide
