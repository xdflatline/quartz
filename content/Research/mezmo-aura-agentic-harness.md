---
title: "Research Index: Agentic Harnesses for SRE Work"

details: "Research synthesis of github.com/mezmo/aura — Mezmo's Apache 2.0 Rust agentic harness for running LLM-powered SRE agents in production. Covers the agentic-harness architecture pattern, coordinator/worker task-DAG orchestration, disk-backed scratchpad for oversized tool outputs, human-in-the-loop approval gates, OpenAI-compatible API serving, on-demand skills catalog, MCP tool integration, A2A protocol interop, multi-provider LLM support, and multi-pod Redis session storage. Aims to capture the features and capabilities of the project as a reusable pattern catalog for any self-hosted, declarative-config agent runtime."
tags:
  - research
  - agent
  - harness
  - runtime
created: 2026-07-25
updated: 2026-07-25
type: research
source: https://github.com/mezmo/aura
---

# Research Index: Agentic Harnesses for SRE Work

**Updated:** 2026-07-25
**Source:** AURA project README + docs (https://github.com/mezmo/aura)

---

## Overview

Synthesis of [Mezmo's AURA project](https://github.com/mezmo/aura) as a concrete instance of the **agentic-harness** pattern: a deployable runtime that turns an LLM into a reliable, autonomous service for executing real SRE work. This index groups the project's features and capabilities into reusable concept patterns so other agent runtimes (or custom builds) can compare against the same taxonomy.

The original research question: *what does a production-grade, self-hosted, MCP-compatible agent runtime for SRE work look like in mid-2026?* AURA is one well-engineered answer, and its feature surface is the basis for the catalog below.

## Concepts

### Architecture Patterns

- [[Concepts/agentic-harness-architecture]] — the deployment-runtime layer that wraps an LLM with API server, auth, streaming, state, observability, and tool integration.
- [[Concepts/coordinator-worker-task-dag-orchestration]] — multi-agent pattern with planner coordinator + specialist workers running DAG tasks in parallel waves.
- [[Concepts/openai-compatible-agent-serving]] — exposing every agent as a model on the OpenAI `/v1/models` and `/v1/chat/completions` contract.
- [[Concepts/on-demand-skills-catalog-pattern]] — Agent Skills format, catalog-in-system-prompt, `load_skill` on demand.

### Safety and Context Management

- [[Concepts/scratchpad-context-window-management]] — disk-park oversized tool outputs and give the LLM 8 read-only exploration tools (`head`, `slice`, `grep`, …) to pull in only what it needs.
- [[Concepts/hitl-approval-gates-for-tool-calls]] — per-tool glob-based approval gates routed to a webhook or in-conversation flow before sensitive tool calls execute.

## Tools & Projects

### Agent Runtimes

- [[Entities/mezmo-aura]] — Apache 2.0 Rust agentic harness, MCP-compatible, multi-provider LLM, multi-agent orchestration, HITL, scratchpad, OpenAI-compat, A2A, 236 GitHub stars.

### Companies

- [[Entities/mezmo]] — observability vendor (formerly LogDNA) that builds and open-sources AURA.

## Raw Sources

- [[Raw/github-mezmo-aura-readme-2026-07-25]] — full AURA README (628 lines), preserved verbatim with frontmatter.

## Feature and Capability Matrix

| Feature | AURA Implementation | Notes |
|---------|---------------------|-------|
| **Self-hosted / air-gap** | Single Rust binary, no cloud deps | Optional Redis/Valkey for multi-pod |
| **Multi-provider LLM** | OpenAI, Anthropic, Bedrock, Gemini, Ollama, OpenRouter | Per-agent and per-worker override |
| **MCP tool integration** | HTTP streamable (recommended), SSE, STDIO | Tool names not namespaced across servers; first-loaded wins on collision |
| **Multi-agent orchestration** | Coordinator plans DAG → workers in parallel waves → consolidate → replan/clarify | `max_planning_cycles`, `duplicate_call_nudge_threshold`, `duplicate_call_block_threshold` |
| **Per-worker isolation** | Filtered MCP tools, filtered vector stores, isolated context, optional own LLM | `[orchestration.worker.<name>]` blocks |
| **Scratchpad** | Disk-park large tool outputs, 8 read-only exploration tools | BPE tokenization via `tiktoken-rs`; per-tool glob thresholds |
| **Context budget** | `ContextBudget` per agent, fed by LLM-reported token usage | `context_safety_margin` reserves headroom |
| **HITL approval** | Tool-name globs, webhook or conversational route | Orchestration workers only; cross-pod via Redis session store |
| **Vector search** | Qdrant, AWS Bedrock Knowledge Base | Per-worker `vector_stores` filter |
| **On-demand skills** | Agent Skills format directory; catalog in system prompt | `load_skill` + `read_skill_file` (path-escape check) |
| **A2A protocol** | Agent card + REST + JSON-RPC | Opt-in via `--enable-a2a` (off by default) |
| **OpenAI-compatible API** | `/v1/models` + `/v1/chat/completions` | LibreChat/OpenWebUI work unchanged; three `TOOL_RESULT_MODE`s |
| **Multi-pod session** | Redis/Valkey session store | Required for cross-pod A2A and HITL approval |
| **Observability** | OpenTelemetry + OpenInference semantic convention | Native Phoenix compatibility |
| **Client-side tools** | Opt-in per agent (`enable_client_tools = true`) | Passthrough mode; `finish_reason: "tool_calls"` |
| **Aliases / hidden agents** | `alias` (stable ID), `hidden` (excluded from /v1/models) | Aliases must be unique |
| **Telemetry** | Opt-out anonymous CLI telemetry | Three-state consent model |

## Cross-Cutting Themes

### 1. Declarative Configuration as the Production Contract

A single `config.toml` (or directory of TOMLs, one per agent) declares everything: agent identity, LLM, MCP servers, vector stores, HITL gates, orchestration workers, skills, scratchpad, per-worker overrides. The harness is configured, not coded — operators edit TOML and restart. This is the same pattern Kubernetes adopted with `Deployment` manifests: a declarative artifact replaces imperative glue code.

### 2. Open Standards as Interop Levers

AURA does not invent a tool layer (it uses MCP), does not invent an agent-to-agent protocol (it uses A2A), and does not invent an API contract (it adopts OpenAI's chat-completion spec). The result is that an existing client ecosystem — LibreChat, OpenWebUI, every OpenAI SDK — works without modification. The cost is compliance with the specs; the benefit is the entire client ecosystem on day one.

### 3. Safety as Defense-in-Depth

Three independent safety layers stack:

1. **Turn-depth and duplicate-call caps** (always on) — prevent unbounded tool-call loops.
2. **Scratchpad** (always-on when enabled) — prevent context-window floods from large tool outputs.
3. **HITL approval gates** (opt-in per agent) — prevent destructive tool calls without human sign-off.

Plus opt-in safeguards (client-side tools, A2A endpoints, Redis session store) that are explicitly disabled by default because they expand the attack surface.

### 4. Context as a First-Class Resource

Context windows are not just a model property; they are a runtime resource. AURA's `ContextBudget` is updated with LLM-reported token usage, the scratchpad uses BPE tokenization (not byte heuristics), and the artifact-threshold / summary-length split creates a memory hierarchy (full result on disk → summary to coordinator → read-back on demand). This is the same insight that [[Concepts/agent-memory-layer-patterns]] captures for the broader memory design space.

### 5. Per-Worker Cost and Capability Overrides

In orchestration, the coordinator can run on a frontier model while a worker on a cheap model handles high-volume tool calls. The override is per-worker (not global), and it must be a complete LLM config (not a partial) — a forcing function that prevents subtle auth drift. The cost lever is the design.

## Next Research Directions

- [ ] **Evaluate AURA on a real SRE workload** — spin up the K8s SRE example on KIND and run a representative incident-response scenario. Measure wall-clock latency, MCP tool-call count, and scratchpad-trigger frequency.
- [ ] **Compare AURA with library-style agent frameworks** (Mastra, LangGraph) on the same task — measure deployment complexity, observability story, and the cost of breaking the OpenAI-compat contract.
- [ ] **Test the Redis session-store mode** — verify A2A `subscribe`/`cancel` and HITL cross-pod approval under a 2-3 pod deployment behind a load balancer.
- [ ] **Compare scratchpad with a vector-store-based RAG approach** — does the disk-park + read-tools pattern actually beat RAG for tool-output-heavy tasks like log exploration?
- [ ] **Audit the OpenInference span layout** — verify that AURA's `llm.*` / `tool.*` spans are sufficient for Phoenix-side debugging of orchestration runs, especially the parallel-wave execution path.
- [ ] **Benchmark the duplicate-call nudge/block thresholds** — what is the right `duplicate_call_nudge_threshold` for K8s SRE tasks where the same `list_pods` call may legitimately repeat?

## References

- AURA repository: https://github.com/mezmo/aura
- AURA quickstart: https://github.com/mezmo/aura/blob/main/docs/quickstart.md
- AURA K8s SRE example: https://github.com/mezmo/aura/blob/main/examples/quickstart-k8s-sre/README.md
- AURA orchestration example: https://github.com/mezmo/aura/blob/main/examples/quickstart-orchestration-math/README.md
- AURA HITL docs: https://github.com/mezmo/aura/blob/main/docs/hitl.md
- Agent Skills specification: https://agentskills.io/specification
- A2A protocol: https://github.com/a2a-protocol
- OpenInference semantic convention: https://github.com/Arize-ai/openinference/tree/main/spec
