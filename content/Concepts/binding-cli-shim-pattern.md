---
title: "Binding CLI-Shim Pattern"

details: "AgentOS bindings: a server-side function definition (description, Zod inputSchema, execute handler, optional examples and timeout) becomes a CLI shim installed at `/usr/local/bin/agentos-{name}` inside the VM. Zod fields are mapped to kebab-case CLI flags (string -> --name value, boolean -> --flag/--no-flag, array -> repeated flag). The shims are injected into the agent's system prompt and can be called in scripts for code-mode token savings (up to 80% reduction). Direct host function calls with near-zero latency — no network hop, no auth config."
tags:
  - concepts
  - cli
  - tooling
created: 2026-07-19
updated: 2026-07-19
type: concept
source: "[[Raw/agentos-sdk-dev-docs-2026-07-19]]"
---

# Binding CLI-Shim Pattern

**Source:** Documentation bundle ([[Raw/agentos-sdk-dev-docs-2026-07-19]])
**Category:** Architecture Pattern / Technical Reference
**Status:** Production-validated

## Overview

A pattern where server-side host functions are exposed to in-VM agents as auto-generated CLI commands, derived from Zod input schemas. The shims are installed at `/usr/local/bin/agentos-{name}`, injected into the agent's system prompt, and callable in scripts for code-mode token savings. Direct host function calls with near-zero latency and no auth config.

## Core Content

### Required per Binding

- `description` — short, keep concise to save tokens
- `inputSchema` — Zod schema; field names convert `camelCase` to `kebab-case` for CLI
- `execute` — async function on the host
- Optional: `examples` (sample inputs), `timeout` (ms; no timeout by default)

### Zod to CLI Mapping

| Zod type | CLI syntax | Example |
| --- | --- | --- |
| `z.string()` | `--name value` | `--path /tmp/out.png` |
| `z.number()` | `--name 42` | `--limit 5` |
| `z.boolean()` | `--flag` / `--no-flag` | `--full-page` |
| `z.enum(["a","b"])` | `--name a` | `--format json` |
| `z.array(z.string())` | `--name a --name b` | `--tags foo --tags bar` |

Optional fields (`.optional()`) become optional flags. Required fields are enforced at validation time. Use `.describe()` on Zod fields to generate useful `--help` output.

### Agent Commands (Auto-Generated)

```bash
# List all available binding collections
agentos list-bindings

# List bindings in a specific group
agentos list-bindings weather

# Get help for a binding
agentos-weather forecast --help

# Call a binding with flags
agentos-weather forecast --city Paris --days 3

# Call a binding with inline JSON
agentos-weather forecast --json '{"city":"Paris","days":3}'

# Call a binding with JSON from a file
agentos-weather forecast --json-file /tmp/input.json
```

### Output Format

- **Success** — exits 0, writes JSON envelope to stdout: `{"ok":true,"result":{...}}`
- **Failure** — exits non-zero, writes error message to stderr

### Bindings vs. MCP Servers

| | Bindings | MCP Servers |
| --- | --- | --- |
| **How it works** | Call JS functions on host directly | Connect to a standard MCP server |
| **Authentication** | None — direct binding | Custom per-server auth config |
| **Code mode** | Built-in (up to 80% token reduction) | Requires extra work |
| **Latency** | Near-zero (bound to host process) | Extra network hop |
| **Setup** | Define in actor code with Zod | Configure any standard MCP server |

Use bindings for your own JS functions. Use MCP servers for existing third-party services.

### Security Model

- Binding calls from the agent securely invoke `execute()` functions on the host
- Credentials stay on the host — bindings run server-side; agents see only inputs and outputs
- Mandatory for any agent that needs first-party access to your backend

## Key Insights

1. **Code-mode token savings** (up to 80%) come from letting the agent chain `agentos-*` commands in shell scripts instead of round-tripping tool calls
2. **Zod-derived CLIs** eliminate hand-written CLI parsing — schema is the source of truth
3. **No auth config** is a non-obvious win — direct binding means no per-server auth setup, but it also means bindings only work for first-party code you control
4. **Injected into system prompt** means the agent knows what's available without you telling it
5. **JSON envelope on stdout** is a clean contract — easy for agents to parse, easy for you to debug

## Related Concepts

- [[Concepts/zod-cli-flag-mapping]] — the type-to-flag conversion rules
- [[Concepts/in-process-vm-agent-runtime-agentos]] — the runtime that hosts the shims
- [[Concepts/standard-json-schema-tool-contracts]] — related tooling approach (existing concept, contrast)

## Related Entities

- [[Entities/agentos]] — the canonical implementation
- [[Entities/rivet]] — the actor that hosts the bindings

## References

- Raw Documentation: [[Raw/agentos-sdk-dev-docs-2026-07-19]]
- Bindings docs: https://agentos-sdk.dev/docs/bindings
- Example: https://github.com/rivet-dev/agentos/tree/main/examples/bindings
