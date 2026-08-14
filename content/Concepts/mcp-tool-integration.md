---
title: "MCP Tool Integration"
details: "Use of the Model Context Protocol (MCP) as the standard tool-integration surface for an LLM agent, including tool discovery, tool calling, and resource access from both server and client roles."
tags:
  - concepts
  - mcp
  - agent
  - protocol
created: 2026-08-14
updated: 2026-08-14
type: concept
---

# MCP Tool Integration

**Source:** [[Raw/github-esp-claw-overview-2026-08-14]]

## Definition

**MCP tool integration** is the architectural choice to use the [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) as the standard surface by which an LLM agent discovers, calls, and exposes tools. In MCP terms, an agent runtime can act as:

- **MCP server** — exposing its own tools (e.g. read a sensor, toggle a GPIO, run a Lua script) to an MCP-aware client such as a cloud agent or another device.
- **MCP client** — consuming tools exposed by an MCP server, letting the agent drive peripherals or external services through the protocol rather than ad-hoc APIs.

## Why MCP on a Microcontroller

On resource-constrained IoT hardware ([[Concepts/on-device-llm-agent-runtime]]), MCP provides three concrete wins:

1. **Standardization** — the agent loop does not need to invent a tool-calling convention; MCP already defines tools, resources, prompts, and sampling.
2. **Interoperability** — the same device can be discovered and used by any MCP-aware client (cloud agents, other devices, dashboards).
3. **Symmetry** — the device is a **peer**, not a downstream consumer. [[Entities/esp-claw|ESP-Claw]] explicitly supports both server and client roles, which means the device can drive a desktop MCP server just as easily as a desktop agent can drive the device.

## Key Properties

- **Discovery** — clients list tools/resources via the MCP protocol, no out-of-band registration.
- **Typed schemas** — tool inputs/outputs are JSON Schema, validated at the protocol layer.
- **Sampling** — the server can request the client to run an LLM completion, enabling bidirectional agency.
- **Transport-agnostic** — stdio, HTTP+SSE, or custom transports; the protocol layer does not depend on the wire format.

## Use Cases on IoT Devices

| Role | Example |
|------|---------|
| Server | ESP-Claw exposes `read_temperature`, `toggle_relay`, `run_lua_snippet` as MCP tools; a cloud agent calls them. |
| Client | ESP-Claw calls an MCP-exposed weather API or a remote camera, then incorporates the result into its reasoning. |
| Both | Two ESP-Claw devices discover each other and exchange sensor data via MCP, with each running its own agent loop. |

## Tradeoffs

| Pro | Con |
|-----|-----|
| Standard protocol, broad client compatibility | Adds a transport layer on top of the C runtime |
| Symmetric server/client roles | MCP transports (especially HTTP+SSE) heavier than raw RPC |
| Typed tool schemas reduce agent errors | Resource budget on small chips — every byte counts |
| Tool discovery is dynamic | Less control than hand-rolled RPC |

## Related Concepts

- [[Concepts/on-device-llm-agent-runtime]] — the runtime layer that hosts MCP on the device
- [[Concepts/dynamic-lua-scripting-for-device-behavior]] — Lua scripts typically call MCP tools to extend behavior
- [[Concepts/im-as-agent-frontend]] — IM messages often trigger MCP tool calls

## Related Entities

- [[Entities/esp-claw]] — implements MCP as both server and client on ESP32

## References

- [[Raw/github-esp-claw-overview-2026-08-14]]
- https://modelcontextprotocol.io/
