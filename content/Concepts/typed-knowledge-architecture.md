---
title: Typed Knowledge Architecture

details: "Alternative to flat-text memory: structure knowledge into typed buckets with distinct retrieval strategies. Prevents context pollution by injecting..."
tags:
  - concepts
  - memory
  - architecture-pattern
created: 2026-06-17
updated: 2026-06-17
type: concept
---
# Typed Knowledge Architecture

**Source:** HN Discussion (https://news.ycombinator.com/item?id=46742800)
**Category:** Architecture Pattern
**Status:** Proposed best practice for agent memory systems

---

## Overview

Alternative to flat-text memory: structure knowledge into typed buckets with distinct retrieval strategies. Prevents context pollution by injecting only relevant memory types per task.

---

## Three-Tier Type System

### 1. Constraints (Tier 1 — Always Inject)
- **Scope:** Project-wide, non-negotiable
- **Retrieval:** Always injected into context
- **Examples:**
  - Coding standards (naming, architecture)
  - Security requirements
  - Dependency policies
  - "Never commit directly to main"

### 2. Decisions (Tier 2 — Similarity Retrieval)
- **Scope:** Historical choices with rationale
- **Retrieval:** Vector/semantic similarity to current task
- **Structure:** `{ decision, context, rationale, outcome }`
- **Examples:**
  - "Chose PostgreSQL over MongoDB because ACID transactions required for billing"
  - "Avoided library X — caused memory leaks in v2.3"

### 3. Heuristics (Tier 3 — Ambiguity Fallback)
- **Scope:** Soft preferences, style guides
- **Retrieval:** Only when task ambiguity is high
- **Examples:**
  - "Prefer composition over inheritance"
  - "Default to REST over GraphQL for simple APIs"

---

## Retrieval Algorithm

```
1. Inject ALL constraints (unconditional)
2. Retrieve TOP-K decisions by similarity to current task
3. IF ambiguity_score > threshold:
     Inject relevant heuristics
```

---

## Benefits

| Benefit | Mechanism |
|---------|-----------|
| **No Context Pollution** | Only relevant types injected |
| **Traceability** | Decisions carry "why" for future reasoning |
| **Adaptability** | Heuristics don't constrain clear-cut tasks |
| **Auditability** | Clear separation enables review |

---

## Implementation Notes

- Store as structured records (not prose)
- Version decisions (track superseded decisions)
- Tag with task embeddings for similarity search
- Deduplication: hash by `(topic, decision_type)`

---

## Related Concepts

- [[Agent Memory Layer Patterns]]
- [[Friction Logging for Agents]]
- [[Multi-Agent Orchestration Patterns]]

---

## References

- HN Thread: https://news.ycombinator.com/item?id=46742800
- Parent Article: [[hn-memory-ai-coding-agents]]