---
title: "Zod to CLI Flag Mapping"

details: "Zod schema fields map deterministically to kebab-case CLI flags: strings take `--name value`, numbers take `--name 42`, booleans toggle with `--flag` / `--no-flag`, enums take `--name a`, arrays repeat the flag. Optional fields (`.optional()`) become optional flags. Required fields are enforced at validation time. Use `.describe()` on Zod fields to generate useful `--help` output. Field names convert from `camelCase` to `kebab-case`. This pattern lets schema-driven tools (AgentOS bindings, code-mode agents) avoid hand-written CLI parsing."
tags:
  - concepts
  - cli
  - schema
created: 2026-07-19
updated: 2026-07-19
type: concept
source: "[[Raw/agentos-sdk-dev-docs-2026-07-19]]"
---

# Zod to CLI Flag Mapping

**Source:** Documentation bundle ([[Raw/agentos-sdk-dev-docs-2026-07-19]])
**Category:** Technical Reference
**Status:** Production-validated

## Overview

The deterministic rules by which a Zod schema becomes a CLI surface. Used by AgentOS bindings and similar code-mode agent tools. Field names convert from `camelCase` to `kebab-case`; types map to specific flag syntaxes; optional fields become optional flags; descriptions populate `--help` text.

## Core Content

### Type-to-Flag Mapping

| Zod type | CLI syntax | Example |
| --- | --- | --- |
| `z.string()` | `--name value` | `--path /tmp/out.png` |
| `z.number()` | `--name 42` | `--limit 5` |
| `z.boolean()` | `--flag` / `--no-flag` | `--full-page` |
| `z.enum(["a","b"])` | `--name a` | `--format json` |
| `z.array(z.string())` | `--name a --name b` | `--tags foo --tags bar` |

### Modifiers and Constraints

- **Optional fields** (`.optional()`) become optional flags
- **Required fields** are enforced at validation time
- Use **`.describe()`** on Zod fields to generate useful `--help` output

### Naming Convention

- Field names convert from `camelCase` to `kebab-case`
- `userId` → `--user-id`
- `maxRetries` → `--max-retries`

### AgentOS Binding Usage Example

```typescript
import { z } from "zod";

const weatherBindings = {
  name: "weather",
  description: "Weather data bindings",
  bindings: {
    forecast: {
      description: "Get the weather forecast for a city",
      inputSchema: z.object({
        city: z.string().describe("City name"),
        days: z.number().optional().describe("Number of days"),
      }),
      execute: async (input: { city: string; days?: number }) => { /* ... */ },
    },
  },
};
```

Becomes the CLI:

```bash
agentos-weather forecast --city Paris --days 3

# Inline JSON
agentos-weather forecast --json '{"city":"Paris","days":3}'

# JSON from a file
agentos-weather forecast --json-file /tmp/input.json
```

### Output Format

- **Success** — exits 0, writes JSON envelope to stdout: `{"ok":true,"result":{...}}`
- **Failure** — exits non-zero, writes error message to stderr

## Key Insights

1. **Schema is the source of truth** — no hand-written CLI parsing; one place to update
2. **`--no-flag` for booleans** is the right convention — explicit negation vs. presence
3. **Repeat flags for arrays** is more shell-friendly than comma-separated values (no escaping issues)
4. **`.describe()` populates `--help`** — investing in descriptions pays off in agent discoverability
5. **JSON escape hatch** (`--json` / `--json-file`) handles complex inputs without schema explosion

## Related Concepts

- [[Concepts/binding-cli-shim-pattern]] — the AgentOS pattern that uses this mapping
- [[Concepts/standard-json-schema-tool-contracts]] — related tooling approach (existing concept, contrast)

## Related Entities

- [[Entities/agentos]] — the canonical implementation

## References

- Raw Documentation: [[Raw/agentos-sdk-dev-docs-2026-07-19]]
- Bindings docs: https://agentos-sdk.dev/docs/bindings
