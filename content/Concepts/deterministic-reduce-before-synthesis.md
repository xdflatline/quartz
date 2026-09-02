---
title: "Deterministic Reduce Before Synthesis"
details: "Graph engineering anti-pattern to avoid: many workers feeding one giant synthesis prompt. The synthesis model becomes a garbage collector reading, deduplicating, formatting, ranking, and inferring. Instead, run a deterministic code-based reducer (dedupe, sort, group, filter, count, normalize) before the reasoning node. Use models for ambiguity, code for plumbing."
tags:
  - concepts
  - agent
  - orchestration
  - deterministic-first
created: 2026-09-02
updated: 2026-09-02
type: concept
sources:
  - .Raw/lunarresearcher-graph-engineering-2026-08-10.md
---

# Deterministic Reduce Before Synthesis

**Source:** [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
**Category:** Architecture Pattern
**Status:** Proposed best practice

## Overview

One of the most expensive architecture mistakes in agent systems: dumping all worker outputs into a single synthesis prompt, forcing the smartest model to act as a garbage collector. The fix is a **deterministic reducer** — code, not another agent — that runs before the reasoning node.

## Core Content

### The Anti-Pattern

```
20 workers
    ↓
one giant synthesis prompt
```

The final node has to:
- read everything
- remove duplicates
- resolve formatting
- notice contradictions
- rank findings
- infer missing fields
- then write the answer

You have turned your smartest model into a garbage collector.

### The Fix: Reducer Before Synthesis

```
workers
   ↓
deterministic reduce
   ↓
reasoning / synthesis
```

The reducer should remove work that does not require judgment:

```
deduplicate IDs
sort by timestamp
group by source
drop malformed records
count votes
normalize labels
remove exact duplicates
```

**Most of that should be plain code. Not another agent.**

Then your expensive reasoning node receives a smaller, cleaner set.

### The Slogan

> **Use models for ambiguity. Use code for plumbing.**

## Key Insights

1. **Synthesis is not the right place to dedupe** — that is a code operation, not a judgment operation.
2. **A reducer is a cost optimization, not just a cleanup** — it makes the final reasoning cheaper, faster, and more accurate.
3. **Deterministic > probabilistic for plumbing** — the moment the operation is unambiguous, the model should not be in the loop.

## Related Concepts

- [[Concepts/graph-engineering-discipline|Graph Engineering]] — umbrella
- [[Concepts/parallelism-width-budget|Parallelism Width Budget]] — width creates merge pressure; this is the relief
- [[Concepts/deterministic-first-architecture|Deterministic-First Architecture]] — broader principle: code for what is deterministic
- [[Concepts/compression-ratio|Compression Ratio]] — observability metric for how much the reducer actually removed
- [[Concepts/observational-memory-pattern|Observational Memory Pattern]] — adjacent pattern where summarization replaces raw history

## References

- Raw Article: [[Raw/lunarresearcher-graph-engineering-2026-08-10]]
- Original: https://lunarresearcher.substack.com/p/graph-engineering-the-complete-guide
