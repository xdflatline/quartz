---
title: "Framework-Agnostic Runtime Decorators"
detail: "Runtime primitives expressed as decorators on ordinary Python functions, so durability attaches to a harness-agnostic boundary instead of any one framework's worldview."
details: "Framework-agnostic runtime decorators are the pattern by which a record-and-replay runtime attaches durability to ordinary Python function boundaries, independent of the harness. In Kitaru the surface is @flow (the outer durable boundary) and @checkpoint (the unit of work inside it). Because the decorators wrap Python functions rather than nodes in a graph or steps in a framework-specific DSL, the same primitives work with PydanticAI, OpenAI Agents, Claude Agent SDK, LangGraph, or raw Python. Adapters sit at the framework's exposed seam (KitaruAgent for PydanticAI, KitaruRunner for OpenAI Agents, KitaruClaudeRunner for Claude Agent SDK, KitaruGraphRunner for LangGraph) so per-call granularity is available where the framework exposes the seam cleanly, and a coarser boundary is used otherwise. Tradeoff: more flexible than framework-bound runtimes, but the user (or the adapter) decides where the recording seam goes."
tags:
  - concepts
source: https://docs.zenml.io/kitaru
created: 2026-07-10
updated: 2026-07-10
type: concept
sources:
  - .Raw/docs-zenml-kitaru-2026-07-10.md
---

# Framework-Agnostic Runtime Decorators

**Source:** Kitaru Docs ([[Raw/docs-zenml-kitaru-2026-07-10]])
**Category:** Architecture Pattern
**Status:** Production-validated

---

## Overview

Framework-agnostic runtime decorators are the surface pattern of a record-and-replay runtime that keeps its primitives as decorators on ordinary Python functions. The runtime does not require the agent to be a graph, a state machine, or a framework-specific DSL — it wraps Python function boundaries and the user (or a framework-specific adapter) decides where the recording seam goes.

## Core Content

### Why decorators

A graph-based runtime (LangGraph with its StateGraph) makes the graph the unit of durability; a decorator-based runtime makes the function the unit. Decorators win on portability: the same `@flow` and `@checkpoint` work whether the harness is PydanticAI, OpenAI Agents, Claude Agent SDK, LangGraph, or raw Python. A platform team supporting multiple harnesses across an org can standardize durability, replay, and execution metadata on one runtime primitive.

### Three integration levels

The user can pick the depth that fits:

**Level 0 — Black-box harness.** Wrap the entire agent run as one checkpoint.
- Fastest integration
- Framework-agnostic
- Replay boundary is coarse (one per agent run)

**Level 1 — Coarse workflow checkpoints.** Add checkpoints around the phases that matter.
- Useful replay points
- Better audit trail
- User decides where the boundaries go

**Level 2 — Framework-aware adapter.** Use an adapter that tracks the framework's internals as child events under the enclosing checkpoint.
- Richer introspection
- Per-call replay fidelity
- Tighter developer experience
- Adapters are per-framework and need maintenance

### Adapters and replay granularity

Adapters expose the framework's recording seam at the right granularity:

| Framework | Adapter | Replay boundary (finest) |
|-----------|---------|--------------------------|
| PydanticAI | `KitaruAgent` | Per model/tool/MCP call, or one turn |
| OpenAI Agents SDK | `KitaruRunner` | Per call, or one runner-call |
| Claude Agent SDK | `KitaruClaudeRunner` | One completed Claude invocation |
| LangGraph | `KitaruGraphRunner` | One graph call, or middleware-wrapped model/tool calls |
| Gemini Interactions | (adapter) | Stable Interactions / Antigravity |
| Google ADK | (adapter, experimental) | Whole-runner turn, or explicit ADK model/tool objects |

If call-level replay fidelity is the priority, prefer PydanticAI or OpenAI calls mode — both can record every model and tool call as its own checkpoint. The Claude Agent SDK adapter currently checkpoints at the invocation boundary. LangGraph's per-call granularity depends on middleware wrapping the model/tool calls.

### The honesty boundary

Adapters record work that passes through the seam, not work the framework hides inside itself. If a framework makes an internal model call, shell command, or tool call without exposing it, the runtime cannot replay that hidden step — it can only save the result that comes back out. "Record at the boundary you control, and what you record replays faithfully."

This is why Kitaru's adapter page states plainly that faithful replay is bounded by what the framework exposes. Replaying hidden internals would be eval-style output re-scoring, not faithful replay.

### The wait() rule

`kitaru.wait()` belongs at flow scope, not inside a checkpoint body. If a harness adapter creates granular tool checkpoints, configure wait-bearing tools so the adapter keeps the wait outside the synthetic checkpoint wrapper. The human-in-the-loop rule is one of the few hard architectural constraints: putting a wait inside a checkpoint can leave the run waiting for input while the checkpoint is marked failed.

## Key Insights

1. Decorators on ordinary Python functions = portability across harnesses; the alternative (graph-based runtimes) is more powerful inside the graph model but less portable
2. Three integration levels let users pick the depth: black box for fastest start, coarse checkpoints for balance, framework-aware adapter for full per-call replay
3. The honesty boundary matters: a runtime that claims to replay hidden internals it never saw is doing eval-style output re-scoring, not faithful replay
4. Per-call replay fidelity is a function of the framework's exposed seam, not the runtime's willpower — pick the adapter that exposes what you need

## Related Concepts

- [[Concepts/durable-checkpoint-record-and-replay]] — the recording layer
- [[Concepts/faithful-replay-with-isolated-change]] — what the framework-agnostic surface enables
- [[Concepts/agent-stack-layers]] — where the runtime sits in the stack
- [[Entities/kitaru]] — the canonical implementation with the most adapters

## References

- Raw Article: [[Raw/docs-zenml-kitaru-2026-07-10]]
- Original: https://docs.zenml.io/kitaru
