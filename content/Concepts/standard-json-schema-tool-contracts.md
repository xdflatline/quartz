---
title: "Standard JSON Schema Tool Contracts"
detail: "Schema interop pattern that lets tools accept any Standard JSON Schema-compliant validator (Zod, Valibot, ArkType), so the developer picks the validation library without changing the tool contract."
details: "A schema interop pattern built on the Standard JSON Schema spec (standardschema.dev/json-schema). Tools and workflows declare inputSchema and outputSchema using any compliant library — Zod objects directly, Valibot via toStandardJsonSchema(), ArkType types directly. The runtime normalizes to a single JSON Schema representation for LLM tool-call generation. This decoupling means the framework can adopt new validation libraries as the ecosystem evolves, and developers can mix and match within a single codebase."
tags:
  - concepts
created: 2026-07-03
updated: 2026-07-03
type: concept
sources:
  - Raw/github-mastra-ai-framework-2026-07-03.md
---
# Standard JSON Schema Tool Contracts

**Source:** [[Raw/github-mastra-ai-framework-2026-07-03]]
**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

A schema interop pattern built on the [Standard JSON Schema](https://standardschema.dev/json-schema) spec. Tools and workflows declare `inputSchema` and `outputSchema` using **any compliant library** — Zod objects directly, Valibot via `toStandardJsonSchema()`, ArkType types directly. The runtime normalizes to a single JSON Schema representation for LLM tool-call generation.

## The Three Supported Libraries

### Zod (no adapter)
```ts
import { z } from 'zod'

inputSchema: z.object({
  location: z.string(),
  unit: z.enum(['celsius', 'fahrenheit']).optional(),
}),
```

### Valibot (with adapter)
```ts
import * as v from 'valibot'
import { toStandardJsonSchema } from '@valibot/to-json-schema'

inputSchema: toStandardJsonSchema(
  v.object({
    location: v.string(),
    unit: v.picklist(['celsius', 'fahrenheit']),
  })
),
```

### ArkType (no adapter)
```ts
import { type } from 'arktype'

inputSchema: type({
  location: 'string',
  unit: '"celsius" | "fahrenheit"',
}),
```

## Why Standard JSON Schema

The spec defines a **common interface** that validators can implement. Rather than pick a winner (Zod is the most popular, but Valibot is smaller, ArkType is faster), the framework accepts any compliant library. The runtime walks the spec's `~standard` properties to extract the JSON Schema, which is what the LLM actually sees in the tool definition.

## Same Pattern Applies to Workflows

```ts
const step1 = createStep({
  inputSchema: z.object({ message: z.string() }),  // Zod
  outputSchema: toStandardJsonSchema(v.object({ formatted: v.string() })),  // Valibot
  execute: async ({ inputData }) => ({ formatted: inputData.message.toUpperCase() }),
})
```

A workflow can mix libraries across steps — the runtime doesn't care.

## LLM Tool-Call Generation

The reason the framework cares about JSON Schema at all: **the LLM needs a JSON Schema to generate structured tool calls**. Most providers (OpenAI, Anthropic, Google) accept JSON Schema for `tools[i].parameters`. By normalizing all validators to JSON Schema, the agent framework can:

1. Generate provider-specific `tools` arrays from any Zod/Valibot/ArkType definition
2. Validate the LLM's tool-call response against the same schema
3. Reject malformed calls before they reach `execute()`

## Key Insights

1. **Spec-based interop beats feature parity** — supporting one spec lets the framework adopt new validators as they appear (e.g., Effect Schema, Typia) without code changes.
2. **Library choice is a developer-experience decision, not a framework one** — the framework shouldn't lock users into Zod (or any other library) when the underlying contract is the same JSON Schema.
3. **The runtime boundary is JSON Schema, not the validator** — the LLM sees JSON Schema; the user sees Zod (or Valibot or ArkType). Both are correct views of the same contract.
4. **Mixing libraries is supported** — Zod in one step, Valibot in another. The framework treats both as JSON Schema.
5. **Validation runs at the runtime boundary** — the LLM is untrusted input. Standard JSON Schema lets the framework validate regardless of which library the developer chose.

## Related Concepts

- [[typed-tool-creation]] — Where these contracts are defined
- [[graph-based-workflow-engine]] — Where these contracts are also enforced
- [[agent-composition-tree-mastra]] — How schemas propagate through the stack
- [[Entities/mastra]] — Canonical implementation

## References

- Raw Article: [[Raw/github-mastra-ai-framework-2026-07-03]]
- Original: https://mastra.ai/docs/tools-mcp/overview
- Standard JSON Schema: https://standardschema.dev/json-schema
