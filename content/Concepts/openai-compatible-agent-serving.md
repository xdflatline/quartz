---
title: "OpenAI-Compatible Agent Serving"

details: "A deployment contract: an agent runtime exposes each configured agent as a model on a /v1/models endpoint, and chat completions are served at /v1/chat/completions with OpenAI's request/response shape. AURA (mezmo/aura) is a concrete instance. Agents are addressable by alias or name via the model field; clients like LibreChat and OpenWebUI work unchanged; per-agent alias, model_owner, and hidden flags control the model-picker presentation."
tags:
  - concepts
created: 2026-07-25
updated: 2026-07-25
type: concept
source: https://github.com/mezmo/aura
---

# OpenAI-Compatible Agent Serving

**Source:** [[Raw/github-mezmo-aura-readme-2026-07-25]]
**Category:** Architecture Pattern
**Status:** Production-validated (AURA, plus the de facto standard for any LLM agent runtime that wants to plug into existing UIs)

---

## Overview

An API contract pattern: an agent runtime exposes every configured agent as a **model** on an OpenAI-shaped `/v1/models` endpoint, and chat completions are served at `/v1/chat/completions` with OpenAI's request/response shape. Agents are addressable by alias or name via the `model` field, so existing clients — LibreChat, OpenWebUI, the AURA CLI, custom OpenAI SDK code — work without modification.

The pattern is the single biggest interoperability lever in the agent-runtime space. A new agent runtime that adopts the contract immediately gains the entire OpenAI-client ecosystem as a UI.

## Core Content

### The Contract

| OpenAI Endpoint | Runtime Implementation |
|-----------------|------------------------|
| `GET /v1/models` | List loaded agents. Each agent's `name` is the model ID. `alias` is a stable client-facing ID. `model_owner` overrides the `owned_by` field. `hidden = true` excludes from the list. |
| `POST /v1/chat/completions` | Standard chat completion. `messages`, `tools`, `stream`, `temperature`, `max_tokens`, etc. The `model` field selects which agent handles the request. |
| `POST /v1/chat/completions` (streaming) | SSE stream. Standard OpenAI event names plus optional `aura.*` events when `AURA_CUSTOM_EVENTS=true`. |

### Agent Addressability

Every loaded TOML config is one agent. Clients select an agent by passing its identifier in the `model` field:

```bash
# By alias (preferred — stable across renames)
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "devops", "messages": [{"role": "user", "content": "Hello"}]}'

# By name (display name, may change)
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "DevOps Assistant", "messages": [{"role": "user", "content": "Hello"}]}'
```

When no `model` is specified, the server resolves the agent via the `DEFAULT_AGENT` env var, or automatically when only one config is loaded.

### Per-Agent Presentation Controls

```toml
[agent]
name = "DevOps Assistant"
alias = "devops"             # clients send "model": "devops"
system_prompt = "You are a DevOps expert."
model_owner = "mezmo"        # override owned_by in /v1/models (defaults to LLM provider)
hidden = false               # true = excluded from /v1/models and CLI /model list
```

- `name` — display name (used in UI lists, logs, A2A agent card).
- `alias` — stable client-facing identifier. Survives renames. Must be unique across loaded configs.
- `model_owner` — overrides the `owned_by` field in `/v1/models`. Default is the LLM provider name (e.g. `openai`, `anthropic`).
- `hidden` — excludes the agent from the model list but keeps it callable by exact name/alias. Useful for development, internal-only, or restricted agents.

### Tool Result Modes (for OpenAI-client compat)

The OpenAI spec is strict about where tool results appear in the response. AURA offers three modes via `TOOL_RESULT_MODE`:

| Mode | Behavior | Use Case |
|------|----------|----------|
| `none` (default) | Spec-compliant. Tool results only in model summary. | Strict OpenAI clients. |
| `open-web-ui` | Emit tool results through `tool_calls` for OpenWebUI compatibility. | OpenWebUI and similar. |
| `aura` | Emit via `aura.tool_complete` events. | Aura-aware clients (CLI in HTTP mode). |

`TOOL_RESULT_MAX_LENGTH` (default 1000) caps the char count for the `aura` event mode.

### Client-Side Tools (the one non-OpenAI extension)

AURA's **client-side tools** (`enable_client_tools = true`) extend the OpenAI surface with a passthrough mode: when enabled, the server does not execute the tool server-side; instead, the SSE stream terminates with `finish_reason: "tool_calls"` and the client is expected to execute the tool locally and submit the result back as a `role: "tool"` follow-up.

This is the only meaningful deviation from strict OpenAI-compat, and it is **opt-in per agent**. The default is strict OpenAI behavior with the server executing MCP tools itself.

## Key Insights

1. **Compatibility is the unlock.** Adopting the OpenAI shape immediately plugs the runtime into LibreChat, OpenWebUI, the AURA CLI, every OpenAI SDK, every "model picker" UI, and every prompt-engineering tool that targets the OpenAI spec. No new client to write.
2. **The `model` field becomes the agent router.** Instead of a separate agent-selection endpoint, the existing `model` parameter on chat completions does the routing. This is invisible to OpenAI clients — they think they are picking a model, but they are actually picking an agent (which is itself a configuration of model + tools + prompt + guardrails).
3. **Aliases are the contract for clients; names are the contract for humans.** Aliases are stable across renames, must be unique, and are what clients hard-code. Names are display strings that humans see in UIs. Separating the two is the same lesson as stable API IDs vs. display names in REST.
4. **Hidden agents are still callable.** Setting `hidden = true` removes the agent from `/v1/models` and the CLI `/model` list, but the agent is still accessible when targeted by exact name or alias. This is the right pattern for development agents, internal-only agents, and agents that should not appear in customer-facing UIs.
5. **Tool-result-mode is a compatibility shim.** Strict OpenAI clients expect tool results only in the model summary. Real-world UIs (OpenWebUI) want to render the tool call inline. Exposing the mode via env var is the minimal way to support both without forking the spec.

## Related Concepts

- [[Concepts/agentic-harness-architecture]] — broader pattern this is a component of
- [[Concepts/coordinator-worker-task-dag-orchestration]] — orchestrator surfaces a single agent via this contract; workers are internal
- [[Entities/mezmo-aura]] — concrete implementation
- [[Entities/openai]] — the spec the contract emulates

## References

- Raw Article: [[Raw/github-mezmo-aura-readme-2026-07-25]]
- Original: https://github.com/mezmo/aura
- OpenAI Chat Completions spec: https://platform.openai.com/docs/api-reference/chat
