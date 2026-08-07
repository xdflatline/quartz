---
title: Multi-Agent Orchestration Patterns

details: Production multi-agent AI workflows favor **custom orchestration layers** over off-the-shelf frameworks. The consensus is that existing frameworks ...
tags:
  - concepts
created: 2026-06-17
updated: 2026-06-17
type: concept
---
# Multi-Agent Orchestration Patterns

**Source:** HN Discussion (https://news.ycombinator.com/item?id=47660705)
**Category:** Architecture Pattern
**Status:** Production-validated community consensus

---

## Overview

Production multi-agent AI workflows favor **custom orchestration layers** over off-the-shelf frameworks. The consensus is that existing frameworks (LangChain, CrewAI, LangGraph, AGNO) are insufficient for serious production work.

---

## Core Patterns

### 1. Centralized Coordinator
- Single coordination endpoint routes tasks
- Chains agents sequentially or fans out in parallel
- Thin layer — agents own bounded tasks end-to-end

### 2. Explicit Task Graphs
- **Do not let agents pick subtasks**
- Define task graph explicitly at design time
- Agents restricted to "leaf nodes" only
- Coordinator handles routing based on reply classification

### 3. Agent Isolation
- Node.js/V8 isolates for sandboxing
- Git worktrees for code-agent isolation
- Prevents cross-contamination of state

---

## State Management

| Level | Persistence | Scope |
|-------|-------------|-------|
| Agent-level | Persists across runs | Individual agent memory |
| Swarm-level | One-run only | Ephemeral coordination state |

---

## Data Flow Infrastructure

- **Primary State:** Central DB (MongoDB/SQLite) — JSON documents linked by pipeline ID
- **Inter-agent Scratchpad:** Redis-backed for low-latency data passing
- **Context Recall:** Importance scoring to surface relevant history without context window bloat

---

## Trust & Safety

- **Confidence Calibration:** Agents flag ambiguity for human review
- **Reputation Gating:** Low-trust agents cannot delegate upward
- **Human-in-the-loop:** Full conversation thread as context for high-stakes domains

---

## Observability Requirements

- Log every run: input, output, tokens, latency
- Dedicated test abstractions and eval frameworks
- Production tools: Wayfound.ai

---

## Execution Models

- **Primary:** Webhooks and cron jobs
- **Secondary:** Manual triggering for specific tasks

---

## Related Concepts

- [[Agent Memory Layer Patterns]]
- [[Typed Knowledge Architecture]]
- [[Friction Logging for Agents]]

---

## References

- Raw Article: [[hn-multiagent-orchestration-production]]
- HN Thread: https://news.ycombinator.com/item?id=47660705