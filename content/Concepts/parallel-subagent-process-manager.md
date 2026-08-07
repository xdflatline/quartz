---
title: "Parallel Sub-agent Process Manager"
detail: "Pattern 3 from Weng's harness taxonomy: harness spawns multiple sub-agents in parallel for hypothesis search, concurrent experiments, and isolated subtasks, with the parent acting as a small process manager that launches jobs, inspects logs, cancels failures, and merges results."
details: "Parallelism in agent harnesses is explicit and inspectable: sub-agent outputs must land in files, logs, and status records so the model can recover after interruptions and reason over its own execution history. The pattern enables hypothesis search (run N attempts in parallel and pick the best), experiment concurrency (run multiple ablations simultaneously), and context isolation (delegate subtasks to a sub-agent so the main thread stays clean). The parent agent's role is process-manager-scale: small surface area, no business logic."
tags:
  - concepts
created: 2026-08-07
updated: 2026-08-07
type: concept
source: https://lilianweng.github.io/posts/2026-07-04-harness/
---

# Parallel Sub-agent Process Manager

**Source:** [[Raw/lilianweng-harness-engineering-2026-07-04]]
**Category:** Architecture Pattern
**Status:** Production-validated (Claude Code, Codex, AIDE, AFLOW)

---

## Overview

A harness spawns **multiple sub-agents in parallel** to execute isolated tasks — multiple hypotheses, concurrent experiments, delegated subtasks — and the **parent agent acts as a small process manager**: launch jobs, inspect logs, cancel failed runs, merge results. The defining property is that parallelism is **explicit and inspectable**: sub-agent outputs land in files and status records, not transient chat context, so the model can recover after interruptions and reason over its own execution history.

## Core Content

### When to Spawn Sub-agents

| Use case | Why parallel helps |
|----------|---------------------|
| Hypothesis search | Run N candidate solutions in parallel; pick the best by eval score |
| Experiment concurrency | Run multiple ablations / seeds / hyperparam trials simultaneously |
| Context isolation | Delegate subtasks to a fresh-context sub-agent so the main thread stays clean |
| I/O concurrency | Parallel web fetches, file reads, browser operations |
| Risk isolation | Try a destructive operation in a sandboxed sub-agent first |

### Parent-Agent Process Manager Responsibilities

The parent is intentionally **small** (a process manager, not a controller). Surface area:

1. **Launch** — write a launch record (task spec, sub-agent ID, expected output path) to disk; spawn the sub-agent.
2. **Poll / inspect** — `tail -f` log files, `grep` for completion markers, read status records.
3. **Cancel** — `kill <pid>` or signal the sub-agent to stop; record the cancellation reason.
4. **Merge** — read each sub-agent's output file, synthesize, decide next step.
5. **Recover** — on crash or interruption, the launch record + log files are enough to resume.

### Tool Group: Agent Delegation

Weng's coding-agent tool taxonomy groups the delegation primitives together:

| Tool | Purpose |
|------|---------|
| `spawn_agent` | Launch a sub-agent with a task spec and fresh context |
| `resume_agent` | Re-enter an existing sub-agent's context (e.g., to continue work) |
| `wait_agent` | Block until one or more sub-agents complete (with timeout) |
| `list_agents` | Enumerate live and finished sub-agents and their status |
| `close_agent` | Finalize a sub-agent, freeing its context |
| `interrupt_agent` | Send a stop signal (soft cancellation) |

### Why Outputs MUST Be Files, Not Context

If sub-agent outputs only live in a transient chat context, they become **obsolete and hidden** the moment the parent moves on. By writing outputs to files, the parent can:

- Pick back up after its own context was evicted or compressed
- Re-merge results across iterations
- Inspect intermediate state for debugging
- Hand off to a human reviewer mid-flow
- Mine failure patterns across many rollouts (see Self-Harness, AHE)

### The Sub-agent / MCP Boundary

Sub-agents are **in-process or sandboxed sibling agents**, not remote services. For external tool use, the harness instead talks to **MCP servers** (model context protocol). The two are complementary: sub-agents for parallelism within a task, MCP for tool access to the world.

## Key Insights

1. **The parent is a process manager, not a coordinator.** The mental model is `init.d`, not `airflow`. Keep the surface tiny.
2. **All sub-agent state must be file-backed.** Otherwise the parallelism is performative — useful for a single rollout, lost on the next.
3. **Sub-agents are not MCP.** Sub-agents are isolated contexts that share the harness; MCP servers are external tool providers.
4. **The pattern composes with evolutionary search.** AlphaEvolve, AFlow, and DGM all use a parallel-sub-agent foundation under their respective optimization loops.

## Related Concepts

- [[Concepts/harness-as-runtime-os-analog]] — the parent acts as scheduler, like a kernel
- [[Concepts/file-system-as-agent-memory]] — outputs land in files
- [[Concepts/coordinator-worker-task-dag-orchestration]] — the multi-agent version
- [[Concepts/subagent-as-tool-composition]] — sub-agents as a tool for the parent
- [[Concepts/three-plane-agent-runtime]] — broader runtime plane decomposition
- [[Concepts/evolutionary-search-for-harnesses]] — parallel sub-agents underpin most evolutionary loops

## References

- Raw Article: [[Raw/lilianweng-harness-engineering-2026-07-04]]
- Original: <https://lilianweng.github.io/posts/2026-07-04-harness/>
