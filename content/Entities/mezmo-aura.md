---
title: "AURA (mezmo/aura)"

details: "AURA is Mezmo's Apache 2.0 open-source project that turns LLM models into a reliable, autonomous service for executing real SRE work. Self-hosted, MCP-compatible, multi-provider (OpenAI, Anthropic, Bedrock, Gemini, Ollama, OpenRouter), with coordinator/worker multi-agent orchestration, disk-backed scratchpad for oversized tool outputs, human-in-the-loop approval gates, vector search grounding, on-demand skills, A2A protocol interop, and an OpenAI-compatible API surface so LibreChat/OpenWebUI work unchanged. 236 GitHub stars, 21 forks, built in Rust 1.85+."
tags:
  - entities
created: 2026-07-25
updated: 2026-07-25
type: entity
source: https://github.com/mezmo/aura
---

# AURA (mezmo/aura)

**Source:** [[Raw/github-mezmo-aura-readme-2026-07-25]]
**Category:** Tool / Open-Source Project
**Repository:** https://github.com/mezmo/aura
**Website:** https://github.com/mezmo/aura
**Vendor:** Mezmo
**License:** Apache 2.0
**Language:** Rust 1.85+

---

## Overview

AURA is an **agentic harness** — a production-grade runtime that wraps an LLM with the guardrails, API server, state management, auth, streaming, error handling, and tool integrations required to run AI SRE agents safely in production. Where most agent frameworks ship a library you embed in your own app, AURA ships a standalone server (plus a CLI) that you deploy alongside your infrastructure, configure in a single TOML file, and integrate with any OpenAI-compatible client.

The project originates from Mezmo (the log-observability vendor) and targets the SRE use case specifically: Kubernetes ops, incident response, log analysis, and runbook automation. The K8s SRE example on KIND plus the bundled Prometheus MCP server are the canonical deployment story.

## Key Details

### Capabilities

- **Self-hosted / air-gap friendly** — runs entirely on your own infrastructure, no required cloud dependency.
- **Multi-provider LLM** — OpenAI, Anthropic, AWS Bedrock, Google Gemini, Ollama, OpenRouter. Per-agent and per-worker LLM override means a coordinator can run on Claude while a cheap worker runs on Haiku/Ollama.
- **MCP tool integration** — any MCP server (HTTP streamable, SSE, or STDIO). Tool names are not namespaced across servers; first-loaded wins on collision ([#186](https://github.com/mezmo/aura/issues/186)).
- **Multi-agent orchestration** — coordinator plans a task DAG, runs workers in parallel waves, consolidates results. Workers can be filtered (`mcp_filter` glob) to a subset of tools and a different LLM.
- **Scratchpad (context-window management)** — large MCP tool outputs intercepted and parked on disk; agent gets a summary plus 8 read-only exploration tools (`head`, `slice`, `grep`, `schema`, `item_schema`, `get_in`, `iterate_over`, `read`) to pull in only the slices it needs. Uses real BPE tokenization via `tiktoken-rs`.
- **Human-in-the-loop approval gates** — `[hitl]` with tool-name globs; approval routes to a webhook or in-conversation. Currently scoped to orchestration workers.
- **Vector search grounding** — Qdrant, AWS Bedrock Knowledge Base.
- **On-demand skills** — Agent Skills format directory layout; agent sees only a catalog and calls `load_skill` on demand.
- **A2A protocol** — agent card + REST/JSON-RPC endpoints, opt-in via `--enable-a2a` (off by default).
- **OpenAI-compatible API** — every agent is addressable as a model via `model` field; LibreChat/OpenWebUI work unchanged.
- **Multi-pod / durable session** — optional Redis/Valkey session store for A2A tasks, parked HITL approvals, etc., behind a load balancer.
- **OpenTelemetry / OpenInference** — native span emission compatible with Phoenix and other OpenInference-aware tools.

### Configuration Model

A single `config.toml` (or a directory of TOML files, one per agent) declares everything: agent identity, LLM, MCP servers, vector stores, HITL gates, orchestration workers, skills, scratchpad. Workers inherit `[agent.llm]` unless they override with a complete `[orchestration.worker.<name>.llm]` block.

```toml
[agent]
name = "Assistant"
alias = "my-assistant"
system_prompt = "You are a helpful assistant."
turn_depth = 2

[agent.llm]
provider = "openai"
api_key = "{{ env.OPENAI_API_KEY }}"
model = "gpt-5.2"
context_window = 128000

[mcp.servers.my_server]
transport = "http_streamable"
url = "http://localhost:8081/mcp"
```

### Installation

```bash
curl -fsSL https://raw.githubusercontent.com/mezmo/aura/main/scripts/install.sh | bash
```

Installs `aura` (CLI) and `aura-web-server` for Linux/macOS on amd64/arm64. Both binaries validate the config at startup and exit with a clear error before binding any port.

### Server Surface

- `GET /health` — health check (reports session-store backend and ping latency)
- `GET /v1/models` — list loaded agents (respects `hidden = true`)
- `POST /v1/chat/completions` — OpenAI-compatible chat completion (streaming and non-streaming)
- `GET /.well-known/agent-card.json` — A2A agent card (only with `--enable-a2a`)
- `POST /a2a/v1/message:send` — A2A REST message send
- `POST /a2a/v1/rpc` — A2A JSON-RPC transport
- `POST /v1/approvals/{id}` — resolve parked HITL approvals across pods (Redis mode)

### Notable Defaults and Guardrails

- `turn_depth` (default 2) prevents unbounded tool-call loops. `nudge_last_turn` and `nudge_turns_remaining` add wrap-up warnings before the cap.
- `duplicate_call_nudge_threshold = 3` / `duplicate_call_block_threshold = 5` block runaway repeated tool calls.
- `context_safety_margin = 0.20` reserves 20% of context for reasoning/output.
- Client-side tools (`enable_client_tools = true`) are **disabled by default** — the README carries a hard "USE AT YOUR OWN RISK" callout because the LLM can issue `Shell("rm -rf ...")` with the client's full host privileges.
- A2A endpoints are **off by default** — no routes registered unless `--enable-a2a` is set.
- The session store defaults to in-process memory; Redis/Valkey is an opt-in feature flag (`session-store-redis`).

### Observability

- OpenTelemetry by default (`otel` feature on both binaries).
- Spans use the **OpenInference** semantic convention (`llm.*`, `tool.*`, `input.*`, `output.*`) — `gen_ai.*` from underlying Rig.rs is auto-translated.
- Traces land natively in [Arize Phoenix](https://github.com/Arize-ai/phoenix) (the docker-compose quickstart bundles Phoenix on port 6006).
- Custom SSE events: `aura.*` (opt-in via `AURA_CUSTOM_EVENTS=true`) and `aura.reasoning` (opt-in via `AURA_EMIT_REASONING=true`).

### Status (as of 2026-07-25)

- **Stars:** 236
- **Forks:** 21
- **License:** Apache 2.0
- **MCP compatibility:** yes
- **Rust:** 1.85+
- **Most recent breaking config changes:** 2026-04-21 (LLM moved under `[agent.llm]`, per-worker LLM override), 2026-04-10 (field migrations to `[llm]`, Ollama params consolidated).

## Related Concepts

- [[Concepts/agentic-harness-architecture]] — the broader pattern AURA instantiates
- [[Concepts/coordinator-worker-task-dag-orchestration]] — multi-agent orchestration model
- [[Concepts/scratchpad-context-window-management]] — disk-park large outputs pattern
- [[Concepts/hitl-approval-gates-for-tool-calls]] — human approval gates for sensitive tool calls
- [[Concepts/openai-compatible-agent-serving]] — OpenAI-API surface as the integration contract
- [[Concepts/on-demand-skills-catalog-pattern]] — skills catalog + `load_skill` tool pattern
- [[Entities/mezmo]] — the vendor behind AURA

## References

- Raw Article: [[Raw/github-mezmo-aura-readme-2026-07-25]]
- Original: https://github.com/mezmo/aura
- Quickstart: https://github.com/mezmo/aura/blob/main/docs/quickstart.md
- K8s SRE example: https://github.com/mezmo/aura/blob/main/examples/quickstart-k8s-sre/README.md
- Orchestration example: https://github.com/mezmo/aura/blob/main/examples/quickstart-orchestration-math/README.md
- Apache 2.0 License: https://github.com/mezmo/aura/blob/main/LICENSE
