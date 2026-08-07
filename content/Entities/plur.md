---
title: PLUR

details: "Entities: PLUR."
tags:
  - entities
created: 2026-05-21
updated: 2026-05-21
type: entity
---
# PLUR

[PLUR](https://github.com/plur-ai/plur) is a persistent, local-first memory system for AI agents, designed to store corrections, preferences, and conventions that persist across sessions, tools, and machines.

## Key Features

- **Engrams**: Typed assertions (learned knowledge) with temporal decay and hierarchical scoping.
- **Episodes**: Timestamped event records for operational history.
- **Hybrid Search**: BM25 + Embeddings + Reciprocal Rank Fusion.
- **Local-first**: Plain YAML storage, zero cloud dependencies.

## Ecosystem

- **Engine**: `@plur-ai/core`
- **MCP**: `@plur-ai/mcp` (Used by Claude Code, Cursor, Windsurf)
- **Plugin**: `@plur-ai/claw` (OpenClaw)
- **Plugin**: `plur-hermes` (Hermes Agent)

## Links

- [Official Website](https://plur.ai)
- [GitHub Repository](https://github.com/plur-ai/plur)
