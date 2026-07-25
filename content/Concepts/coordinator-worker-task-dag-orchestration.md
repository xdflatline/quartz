---
title: "Coordinator/Worker Task-DAG Orchestration"
detail: "Multi-agent pattern where a coordinator decomposes a request into a task DAG, runs dependency-ready tasks in parallel across specialist workers, and consolidates the results."
details: "A multi-agent orchestration pattern implemented in AURA (mezmo/aura): one coordinator agent plans a task DAG from the user request, then waves of worker agents run in parallel on dependency-ready tasks. Each worker has isolated context, filtered MCP tools, and optionally its own LLM. The coordinator consolidates worker outputs, decides on final response / replan / clarification, and repeats up to max_planning_cycles. Workers can be hidden or visible via /v1/models."
tags:
  - concepts
created: 2026-07-25
updated: 2026-07-25
type: concept
source: https://github.com/mezmo/aura
---

# Coordinator/Worker Task-DAG Orchestration

**Source:** [[Raw/github-mezmo-aura-readme-2026-07-25]]
**Category:** Architecture Pattern
**Status:** Production-validated (AURA, OpenMontage, and other DAG-style orchestrators)

---

## Overview

A multi-agent pattern where one **coordinator** agent decomposes a user request into a directed acyclic graph (DAG) of tasks, then dispatches them to a set of **worker** agents. Workers with no remaining dependencies run in parallel waves. The coordinator consolidates worker outputs, decides whether to deliver a final response, replan, or ask the user for clarification, and the loop repeats up to a configured cap.

The pattern is the standard answer to "one LLM agent is not enough" — the coordinator is a planner/router, the workers are specialists with focused context and tool access.

## Core Content

### The Plan → Execute → Continue Loop

| Phase | Responsibility |
|-------|---------------|
| **Plan** | Coordinator decomposes the user request into a task DAG (JSON). Retries up to `max_plan_parse_retries` if JSON is unparseable. |
| **Execute** | Dependency-ready tasks run in parallel waves on worker agents. Each worker has its own filtered MCP tool list, vector stores, LLM, and skill sources. |
| **Continue** | Coordinator consolidates worker outputs, then routes to: final response, replan (if more decomposition is needed), or clarification (if the user must disambiguate). |

### Worker Isolation Properties

- **Isolated task context window.** Each worker has its own context budget; the LLM-reported token usage feeds back into a per-worker `ContextBudget`.
- **Filtered MCP tools** via `mcp_filter` glob. Omitted = all tools; empty list = none. Allows least-privilege tool access per worker.
- **Filtered vector stores** via `vector_stores` list.
- **Optional per-worker LLM** — a cheaper, faster, or larger-context model can replace the coordinator's LLM. Required to be a **complete** `[orchestration.worker.<name>.llm]` block, not a partial override.
- **Per-worker `turn_depth`** overrides the global cap.
- **Per-worker `scratchpad`** overrides the global scratchpad config.
- **Per-worker `skills`** can disable skills entirely via an explicit empty list.

### Planning Visibility Controls

The `tools_in_planning` field controls how much the coordinator sees about worker tools during the planning step:

| Value | Coordinator Sees |
|-------|-----------------|
| `"none"` | No tool info (coordinator plans blind) |
| `"summary"` | Tool names only |
| `"full"` | Names and descriptions |

### Loop Controls and Anti-Spin Safeguards

- `max_planning_cycles` — caps the number of plan→execute→continue iterations.
- `max_tools_per_worker` — caps the number of MCP tools exposed to each worker.
- `duplicate_call_nudge_threshold = 3` — appends a guidance annotation after 3 consecutive identical tool calls.
- `duplicate_call_block_threshold = 5` — appends an abort annotation and sets an escalation flag after 5 consecutive identical tool calls.
- `timeouts.per_call_timeout_secs` — per-tool-call timeout in seconds (0 = disabled).

### Direct Answer and Clarification

The coordinator can short-circuit the DAG in two cases:
- `allow_direct_answers = true` — the coordinator can answer simple queries directly without dispatching to workers.
- `allow_clarification = true` — the coordinator can ask the user for clarification instead of guessing.

### Result Artifacts

When a worker's result exceeds `result_artifact_threshold` (default 4000 chars), it is saved to an artifact file under `{memory_dir}/{run_id}/artifacts/`. The coordinator receives only a `result_summary_length`-character summary. The full artifact is then read back via `read_artifact`, which applies the same scratchpad budget rules — large artifacts become scratchpad pointers the coordinator explores in place (the coordinator has no scratchpad, so its `read_artifact` always returns inline content).

### Example Configuration

```toml
[orchestration]
enabled = true
max_planning_cycles = 3
tools_in_planning = "summary"
allow_direct_answers = true
allow_clarification = true

[orchestration.worker.operations]
description = "Operational analysis and diagnostics"
preamble = "You are an operations specialist."
mcp_filter = ["ops_*"]
vector_stores = []

[orchestration.worker.knowledge]
description = "Documentation and procedures"
preamble = "You are a knowledge specialist."
mcp_filter = []
vector_stores = ["docs"]

[orchestration.worker.formatting.llm]
provider = "anthropic"
api_key = "{{ env.ANTHROPIC_API_KEY }}"
model = "claude-haiku-4-5-20251001"
context_window = 200000
```

## Key Insights

1. **Coordinator is a planner, workers are specialists.** The coordinator never executes tools directly; it plans, dispatches, and consolidates. The workers have the actual MCP access. This concentrates blast radius: the coordinator cannot accidentally invoke a destructive tool.
2. **Workers are independent contexts.** A worker's tool calls, token usage, and errors do not contaminate the coordinator's context or other workers' contexts. Per-worker `turn_depth` and `scratchpad` enforce isolation at the budget level too.
3. **Mixing LLM providers per worker is the cost-optimization lever.** A coordinator on Claude Opus can dispatch read-heavy workers to Haiku (Anthropic) or local Ollama models. The `[orchestration.worker.<name>.llm]` block must be complete (not partial), which is a deliberate forcing function — partial overrides lead to subtle auth drift.
4. **The DAG is parsed JSON, not free text.** The coordinator emits structured plan JSON. Parse failures retry up to `max_plan_parse_retries`, then the run fails cleanly. This is the difference between a DAG orchestrator and a "just let the model think" supervisor.
5. **Result artifacts are the memory hierarchy.** Large worker results land on disk, summaries go to the coordinator, and `read_artifact` brings them back through the same budget rules. This is the multi-agent analog of [[Concepts/scratchpad-context-window-management]] for a single agent.

## Related Concepts

- [[Concepts/agentic-harness-architecture]] — the broader pattern AURA is an instance of
- [[Concepts/scratchpad-context-window-management]] — context management for individual workers
- [[Concepts/hitl-approval-gates-for-tool-calls]] — per-worker approval gates
- [[Concepts/multi-agent-orchestration-patterns]] — the broader design space of multi-agent patterns
- [[Entities/mezmo-aura]] — concrete implementation

## References

- Raw Article: [[Raw/github-mezmo-aura-readme-2026-07-25]]
- Original: https://github.com/mezmo/aura
- Example: https://github.com/mezmo/aura/blob/main/configs/example-math-orchestration.toml
