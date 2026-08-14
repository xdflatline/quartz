---
title: "ESP-Claw"
details: "Espressif's C-implemented Chat Coding AI agent framework for ESP32-series IoT devices, combining an LLM agent loop with dynamic Lua scripting, MCP integration, and IM chat frontends."
tags:
  - entity
  - agent
  - agentic-system
  - iot
  - open-source
created: 2026-08-14
updated: 2026-08-14
type: entity
source: "https://github.com/espressif/esp-claw"
---

# ESP-Claw

**Source:** [[Raw/github-esp-claw-overview-2026-08-14]]
**Category:** Project (Open-source framework)
**Repository:** https://github.com/espressif/esp-claw
**Website:** https://esp-claw.com/
**License:** Apache-2.0
**Latest Release:** v0.1.0 (2026-06-12)

## Overview

ESP-Claw is Espressif's reference implementation of a "Chat Coding" agent runtime targeting ESP32-series microcontrollers. It positions the chip as an active decision-maker rather than a passive network endpoint, completing the full sense → think → act loop locally. The framework is written in C (≈84% of the codebase) with Lua for dynamic behavior and small amounts of TypeScript/Python for tooling.

The project explicitly credits [[Entities/openclaw|OpenClaw]] (the upstream concept) and [[Entities/mimiclaw|MimiClaw]] (a related ESP32 agent implementation by Memovai) as inspirations.

## Key Details

### Hardware Targets

| Chip | Status |
|------|--------|
| ESP32-S3 | Supported |
| ESP32-P4 | Supported |
| ESP32-C5 | Supported |
| ESP32-S31 | Supported |

Boards (e.g. M5Stack CoreS3, generic breadboard variants) under `application/edge_agent/boards/` can be flashed directly via browser — no local toolchain required ([online flasher](https://esp-claw.com/en/flash/)).

### LLM Provider Support

Supports both OpenAI-style and Anthropic-style APIs. Native adapters for OpenAI, Alibaba Bailian (Qwen), Anthropic, DeepSeek, plus a custom-endpoint path. Self-programming capability is gated on models with strong tool-use/instruction-following — the README recommends `gpt-5.4`, `qwen3.6-plus`, `claude4.6-sonnet`, `deepseek-v4-pro` or comparable.

### IM Frontends

Telegram, QQ, Feishu, WeChat, plus an extension hook for additional platforms. Chat is the primary user-facing control surface — behavior is defined through conversation rather than code.

### Core Capabilities

- **Agent Loop on-device** — LLM reasoning, tool use, and execution run on the ESP32 itself; latency budget is milliseconds.
- **Dynamic Lua** — user-supplied or agent-generated Lua scripts define device behavior without firmware rebuilds.
- **MCP integration** — acts as both MCP server and client, talking to standard MCP devices.
- **Structured Memory** — memory is organized on-device; no cloud round-trip required for state.
- **Component trimming** — every module is optional, enabling footprint tuning per use case.

### Repository Layout

```
application/        # application code (edge_agent lives here)
components/         # reusable components
docs/               # documentation
pages/simulator/    # web simulator (Lua + LVGL)
tools/              # build/development tooling
.agents/, AGENTS.md, CLAUDE.md   # agent-facing instructions
```

The presence of `AGENTS.md` and `CLAUDE.md` at the repo root signals the project is itself agent-friendly — coding agents are expected collaborators, not visitors.

## Related Concepts

- [[Concepts/on-device-llm-agent-runtime]] — the architectural pattern ESP-Claw instantiates
- [[Concepts/dynamic-lua-scripting-for-device-behavior]] — Lua-as-programmable-behavior surface
- [[Concepts/im-as-agent-frontend]] — chat as the primary device control plane

## Related Entities

- [[Entities/espressif]] — the chip vendor and project steward
- [[Entities/openclaw]] — upstream concept and naming origin
- [[Entities/mimiclaw]] — sibling ESP32 agent implementation

## References

- Raw article: [[Raw/github-esp-claw-overview-2026-08-14]]
- Repository: https://github.com/espressif/esp-claw
- Website: https://esp-claw.com/
- Online flasher: https://esp-claw.com/en/flash/
