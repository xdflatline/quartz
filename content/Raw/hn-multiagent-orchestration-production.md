---
title: "Ask HN: How are you orchestrating multi-agent AI workflows in production?"
detail: This thread discusses production orchestration patterns for multi-agent AI workflows. The consensus among experienced builders is that **rolling yo...
details: This thread discusses production orchestration patterns for multi-agent AI workflows. The consensus among experienced builders is that **rolling yo...
tags:
  - raw
created: 2026-06-13
updated: 2026-06-13
type: raw
---
# Ask HN: How are you orchestrating multi-agent AI workflows in production?

**Source:** Hacker News (https://news.ycombinator.com/item?id=47660705)
**Date Retrieved:** 2025-06-13
**Type:** Community Discussion

---

## Summary

This thread discusses production orchestration patterns for multi-agent AI workflows. The consensus among experienced builders is that **rolling your own orchestration layer** is often preferred over off-the-shelf frameworks for serious production work.

---

## Core Architectural Patterns

### Orchestration Strategy
- **Centralized Coordination:** Use a "coordinator" endpoint that chains agents sequentially or fans them out in parallel
- **Task Definition:** Avoid letting agents define their own subtasks. Define the task graph explicitly and restrict agents to handling "leaf nodes"
- **Isolation:** Some developers use Node.js/V8 isolates or git worktrees to keep agents isolated

### Data Passing
- **Shared State:** Use a central database (MongoDB or SQLite) to store JSON documents that link pipeline IDs
- **Memory Management:** Implement session state that persists across turns. For long-running conversations, use "importance scoring" to recall relevant context without bloating the context window
- **Infrastructure:** Redis-backed scratchpads are commonly used for inter-agent data flow

---

## Key Insights & Best Practices

### 1. Trust and Safety
- **Confidence Calibration:** Agents should flag ambiguous situations for human review rather than guessing
- **Reputation-based Gating:** Implement logic to prevent low-trust agents from delegating tasks upward to higher-privilege agents
- **Human-in-the-loop:** In high-stakes environments, treat the entire conversation thread as the context window

### 2. Observability
- **Logging:** Log every agent run, including input, output, token usage, and latency
- **Evaluation:** Use dedicated test abstractions and evaluation frameworks
- **Tools:** Some teams use specialized platforms like Wayfound.ai for production observability

---

## Notable Quotes

> "The pattern that has held up: agents own clearly bounded tasks end to end (research, draft, send, parse reply), with a thin orchestration layer that routes based on reply classification." — hirewilliam

> "Biggest takeaway: don't let agents pick their own subtasks. Define the task graph yourself: agents only handle the leaf nodes." — Chepko932

> "I roll my own, there's absolute 0 framework out there that's good enough for serious work." — segmondy

> "The naive approach is stateless. Each reply gets processed independently. This breaks down fast when a prospect says 'as I mentioned before' and the agent has no memory of what they mentioned before." — hirewilliam

---

## Tools & Frameworks Mentioned
- **Frameworks:** LangChain, CrewAI, LangGraph, AGNO
- **Infrastructure:** Node.js, MongoDB, SQLite, Redis
- **Observability:** Wayfound.ai

---

## Operational Modes
- **Execution:** Most production agents triggered via webhooks or cron jobs; manual execution common for specific tasks
- **State Management:**
  - Agent-level: Persists across runs
  - Swarm-level: One-run only