---
title: "Scratchpad Context-Window Management"

details: "A context-window management pattern for tool-using agents: large MCP tool outputs (Kubernetes listings, log exports) are intercepted above a per-tool token threshold and stored on disk. The agent receives a summary plus 8 read-only exploration tools (head, slice, grep, schema, item_schema, get_in, iterate_over, read) to selectively pull in only the data it needs. A per-agent ContextBudget is updated with LLM-reported token usage as ground truth. Implemented in AURA (mezmo/aura) as [agent.scratchpad]."
tags:
  - concepts
  - context-engineering
  - agent
created: 2026-07-25
updated: 2026-07-25
type: concept
source: https://github.com/mezmo/aura
---

# Scratchpad Context-Window Management

**Source:** [[Raw/github-mezmo-aura-readme-2026-07-25]]
**Category:** Architecture Pattern
**Status:** Production-validated (AURA, also surfaced in Memori-style memory layers)

---

## Overview

**Scratchpad** is a context-window management pattern for tool-using agents. When an MCP tool returns a response far larger than the LLM's context window (a single Kubernetes workload listing or log export can be tens of thousands of tokens), the harness intercepts it, stores the raw output on disk, and gives the agent a summary plus a small set of read-only exploration tools. The agent can then pull in only the slices it actually needs instead of letting the response flood the context and degrade reasoning quality.

The pattern is the disk-backed analog of "park a large file and grep it" — applied to the LLM's tool-call pipeline.

## Core Content

### Trigger and Threshold

Scratchpad interception is configured at `[mcp.servers.<server>.scratchpad]`. Keys are **glob patterns** (default threshold `5_120` tokens if omitted) matched against tool names:

```toml
[mcp.servers.k8s-sre.scratchpad]
"*_list_*"                  = { min_tokens = 512 }   # broad
"k8s_list_service_monitors" = { min_tokens = 384 }   # specific override
"*"                         = { min_tokens = 4096 }  # catch-all
```

Pattern resolution: when multiple patterns match the same tool, the **longest (most specific) pattern wins**; on length ties, the smallest threshold wins. Token counting uses real BPE tokenization via `tiktoken-rs`, not byte/character heuristics, so `min_tokens` reflects actual model token cost.

### The Eight Read-Only Exploration Tools

When scratchpad is enabled, the agent receives these tools:

| Tool | Purpose |
|------|---------|
| `head` | First N tokens/lines of the parked output |
| `slice` | Arbitrary offset+length slice |
| `grep` | Filter to lines matching a pattern |
| `schema` | Top-level structure of a JSON/structured output |
| `item_schema` | Schema of a single element in a list |
| `get_in` | Navigate a nested structure by path |
| `iterate_over` | Iterate over a collection with a callback-style query |
| `read` | Read a range in plain-text mode |

### ContextBudget

Each agent (single-agent or orchestration worker) gets a **fresh `ContextBudget`** scoped to that agent's effective LLM `context_window`. LLM-reported per-turn token counts feed back into the budget as ground truth:

- Orchestration: tokens reported via `StreamItem::TurnUsage`.
- Single-agent: tokens reported via the streaming hook.

A per-agent `aura.scratchpad_usage` SSE event is emitted when the agent finishes — the same event name fires for both single-agent and worker contexts (it lives in the base `aura.*` namespace, not `aura.orchestrator.*`).

### Configuration Fields

```toml
# Top-level — required when scratchpad is enabled. Shared by single-agent
# scratchpad and orchestration persistence.
memory_dir = "/tmp/aura"

[agent.scratchpad]
enabled = true
context_safety_margin = 0.20          # 20% of context reserved for reasoning/output
max_extraction_tokens = 10_000        # cap per extraction tool call
turn_depth_bonus = 6                  # extra ReAct turns when scratchpad is active

[orchestration.worker.data-explorer.scratchpad]
# Override just for this worker
max_extraction_tokens = 5_000
```

- `context_safety_margin` — fraction of context reserved for reasoning/output, not for tool results. Default 0.20.
- `max_extraction_tokens` — cap per single extraction tool call. Default 10_000.
- `turn_depth_bonus` — extra ReAct turns granted when scratchpad is active, because exploration may need more turns than a direct answer. Default 6.
- Per-worker override at `[orchestration.worker.<name>.scratchpad]`.

### Per-Call Extraction Limit

Every exploration tool checks the size of its result before returning. If a single call would exceed `max_extraction_tokens` (or the cumulative `ContextBudget`), the tool returns a structured JSON error like:

```json
{"error": "head_too_large", "estimated_tokens": 12345, "suggestions": [...]}
```

instead of the content. The LLM sees this as a successful tool result and retries with smaller params — each retry consumes a turn, which is why `turn_depth_bonus` exists.

### Storage Location

| Mode | Path |
|------|------|
| Single-agent | `{memory_dir}/scratchpad/` |
| Orchestration | `{memory_dir}/{run_id}/iteration-{n}/scratchpad/` (legacy `[orchestration.artifacts].memory_dir` still works as a fallback) |

### Read-Back in Orchestration

In orchestration, large task results are saved to **artifact files** under `{memory_dir}/{run_id}/artifacts/`. When a worker reads one back with `read_artifact`, the same budget rules apply:

- An artifact that fits is returned inline.
- An artifact that exceeds the limit comes back as a scratchpad pointer the worker explores in place with the read tools (`head`, `grep`, `slice`, …).
- The artifact is read directly from the artifacts directory — it is never copied into the scratchpad.
- The coordinator has no scratchpad, so its `read_artifact` always returns inline content.

## Key Insights

1. **BPE-tokenized thresholds, not character counts.** `tiktoken-rs` means `min_tokens = 512` actually costs ~512 tokens in the model's tokenizer. Byte-based heuristics (which some frameworks use) over- or under-estimate wildly depending on the data.
2. **Glob-based per-tool thresholds.** Different tools have different size profiles — a `*_list_*` is broader, so a smaller threshold makes sense; a specific override like `k8s_list_service_monitors = { min_tokens = 384 }` lets you tighten high-cost tools. The "longest pattern wins" rule is the same as nginx location matching.
3. **Structured errors are not failures.** When `head` returns `{"error": "head_too_large", ...}`, the LLM sees a successful tool result, not a crash. It can read the suggestions and try smaller params. The error envelope is the contract.
4. **Per-worker overrides matter for cost.** A "data-explorer" worker that touches large logs can be capped at 5_000 extraction tokens while other workers get the full 10_000. The override is the cost lever.
5. **The orchestrator-coordinator has no scratchpad.** Coordinators consolidate, they do not explore. So coordinator `read_artifact` always inlines; the exploration layer lives on the workers. This is a deliberate complexity reduction: only the entities that actually do tool calls have to manage a budget.

## Related Concepts

- [[Concepts/agentic-harness-architecture]] — broader pattern this is a component of
- [[Concepts/coordinator-worker-task-dag-orchestration]] — orchestrator-side read-back of artifacts
- [[Concepts/agent-memory-layer-patterns]] — broader memory-tiering pattern
- [[Entities/mezmo-aura]] — concrete implementation

## References

- Raw Article: [[Raw/github-mezmo-aura-readme-2026-07-25]]
- Original: https://github.com/mezmo/aura
- Docs: https://github.com/mezmo/aura/blob/main/docs/quickstart.md
