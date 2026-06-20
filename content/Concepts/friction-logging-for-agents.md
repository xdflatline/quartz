---
title: Friction Logging for Agents
detail: "Since AI agents lack human emotional experience (the \"pain\" of bad hygiene, debugging nightmares), use quantitative **friction metrics** as a proxy..."
details: "Since AI agents lack human emotional experience (the \"pain\" of bad hygiene, debugging nightmares), use quantitative **friction metrics** as a proxy..."
tags:
  - concepts
created: 2026-06-17
updated: 2026-06-17
type: concept
---
# Friction Logging for Agents

**Source:** HN Discussion (https://news.ycombinator.com/item?id=46742800)
**Category:** Learning Mechanism
**Status:** Proposed proxy for agent "experience"

---

## Overview

Since AI agents lack human emotional experience (the "pain" of bad hygiene, debugging nightmares), use quantitative **friction metrics** as a proxy loss function. Enables agents to "learn" from expensive mistakes without human intervention.

---

## Metrics Hierarchy

### Primary: Human Correction Rate (Highest Signal)
- **Definition:** Frequency of human interventions correcting agent output
- **Why it works:** Direct evidence of "wrong path"
- **Collection:** Log every human edit/override of agent work
- **Weight:** Highest in memory retrieval scoring

### Secondary: Iteration Count (Noisy)
- **Definition:** Number of attempts to complete a task
- **Caveat:** High iterations may indicate task difficulty, not agent failure
- **Use:** Weak signal, combine with correction rate

### Secondary: Revert Frequency (Noisy)
- **Definition:** How often agent's changes are reverted (git revert, manual undo)
- **Caveat:** May reflect changing requirements, not agent error
- **Use:** Weak signal, combine with correction rate

---

## Implementation

### Logging
```python
# Per-task friction record
{
    "task_id": "uuid",
    "task_embedding": [...],  # for similarity matching
    "friction_score": 0.73,   # weighted composite
    "human_corrections": 3,
    "iterations": 5,
    "reverts": 1,
    "timestamp": "2025-06-13T..."
}
```

### Retrieval Weighting
- When retrieving memories for a new task, boost entries from **low-friction** historical tasks
- Deprioritize patterns from **high-friction** tasks
- Enables "learning" without gradient updates

---

## Why This Works

> "LLMs struggle with the nuance of software development because they lack the emotional experience of 'bad hygiene' (the pain of fixing bugs). Using friction metrics acts as a proxy for this experience."

- Human corrections = explicit negative reward signal
- Accumulates institutional knowledge of "what causes pain"
- Transfers across agents via shared memory layer

---

## Challenges

| Challenge | Mitigation |
|-----------|------------|
| **Noisy secondary metrics** | Weight human corrections 10x higher |
| **Attribution difficulty** | Log at task granularity, not step |
| **Cold start** | Bootstrap with synthetic friction from known anti-patterns |
| **Gaming** | Audit trail; human review of high-friction patterns |

---

## Related Concepts

- [[Agent Memory Layer Patterns]]
- [[Typed Knowledge Architecture]]
- [[Multi-Agent Orchestration Patterns]]

---

## References

- HN Thread: https://news.ycombinator.com/item?id=46742800
- Parent Article: [[hn-memory-ai-coding-agents]]