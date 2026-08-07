---
title: "Typed Tool Creation (createTool Pattern)"

details: "A tool definition pattern that mandates a factory function (createTool from @mastra/core/tools) over plain object literals. The factory ensures tools carry a stable id, a description (read by the LLM to decide when to call), validated inputSchema and outputSchema (Standard JSON Schema: Zod, Valibot, or ArkType), and an execute() body receiving validated input plus a context object (requestContext, tracingContext, abortSignal). Plain object tool definitions silently fail to execute because the runtime has no schema to validate against. toModelOutput separates the app-facing tool result from the model-facing summary."
tags:
  - concepts
  - tooling
created: 2026-07-03
updated: 2026-07-03
type: concept
sources:
  - Raw/github-mastra-ai-framework-2026-07-03.md
---
# Typed Tool Creation (`createTool` Pattern)

**Source:** [[Raw/github-mastra-ai-framework-2026-07-03]]
**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

A tool definition pattern that **mandates a factory function** (`createTool`) over plain object literals. The factory ensures every tool carries: a stable `id`, a `description` (read by the LLM to decide *when* to call), validated `inputSchema` and `outputSchema` (Standard JSON Schema: Zod, Valibot, or ArkType), and an `execute()` body receiving validated input plus a context object. Plain object tool definitions **silently fail** because the runtime has no schema to validate against.

## The Silent Failure Problem

A naive agent framework might accept:
```ts
const weatherTool = {
  name: 'get_weather',
  description: 'Get weather',
  parameters: { type: 'object', properties: { location: { type: 'string' } } },
  execute: async (args) => { ... }
}
```

Mastra rejects this silently — the agent's tool calls appear to do nothing. The fix: a factory that the runtime recognizes as a tool:

```ts
import { createTool } from '@mastra/core/tools'
import { z } from 'zod'

export const weatherTool = createTool({
  id: 'get-weather',
  description: 'Fetches weather for a location',
  inputSchema: z.object({ location: z.string() }),
  outputSchema: z.object({ weather: z.string() }),
  execute: async inputData => {
    return { weather: 'sunny' }
  },
})
```

The factory injects the runtime hooks (validation, execution, tracing) that the agent loop calls.

## The `execute()` Signature

`execute()` receives **two parameters**:

1. **Validated input data** — the parsed result of `inputSchema`
2. **Execution context** — `{ requestContext, tracingContext, abortSignal, ... }`

```ts
execute: async ({ location }, { requestContext, abortSignal }) => {
  const response = await fetch(`https://wttr.in/${location}?format=3`, { signal: abortSignal })
  return { weather: await response.text() }
}
```

The context object is the integration point for cross-cutting concerns: cancellation, request-scoped state, trace IDs.

## Schema Library Interop

Tools support any library implementing [Standard JSON Schema](https://standardschema.dev/json-schema):

| Library | Adapter |
|---------|---------|
| **Zod** | `z.object({ ... })` directly |
| **Valibot** | `toStandardJsonSchema(v.object({ ... }))` |
| **ArkType** | `type({ ... })` directly |

This decoupling means the user picks their validation library without changing the tool contract.

## The `description` Field Is the LLM Contract

The `description` is **read by the LLM at every turn** to decide whether to call the tool. Recommendations:

- **Keep descriptions concise and focused on the primary use case** — long descriptions dilute the signal
- **Descriptive schema names guide the agent** — `location: z.string().describe('City name')` helps the model map user intents
- **Treat descriptions like API documentation** — they're load-bearing for agent routing

## `toModelOutput` — Shape Output for the Model

When a tool returns rich structured data for the **application** but you want the model to see a smaller or multimodal representation, use `toModelOutput`:

```ts
execute: async ({ location }) => {
  const data = await fetchFullWeatherData(location)
  return {
    location,
    temperature: data.temp_F,
    condition: data.weather,
    // ... lots of fields
    toModelOutput: () => ({
      type: 'content',
      value: [{ type: 'text', text: `${data.temp_F}°F, ${data.weather}` }],
    }),
  }
}
```

The full result is preserved in your app; the model sees a compact summary. This is the mechanism for keeping model context focused while preserving app-side fidelity.

## Tool Composition

Tools are first-class — agents and workflows are themselves tools:

| Kind | Configuration Key | Tool Name |
|------|-------------------|-----------|
| Subagent | `agents: { writer }` | `agent-writer` |
| Workflow | `workflows: { researchWorkflow }` | `workflow-researchWorkflow` |

The agent's tool list and the subagent's tool list share the same representation, so a subagent can have its own subagents (recursive composition).

## Multiple Tools

An agent can have many tools; the LLM picks based on user message, instructions, and tool descriptions/schemas. The tool list is passed as an object:

```ts
tools: { weatherTool, hazardsTool, searchTool }
```

## Key Insights

1. **Silent failure is worse than throwing** — a missing factory is invisible until production. The factory pattern moves the failure to definition time.
2. **Schema validation runs at the runtime boundary** — the LLM is untrusted input. Validation prevents hallucinated args from reaching your business logic.
3. **Description is a routing protocol** — see [[capability-first-tool-design]] for the design discipline.
4. **`toModelOutput` separates app context from model context** — preserve app fidelity, shrink model context.
5. **Tools compose recursively** — agents and workflows are tools, so a hierarchy of agents-with-agents is expressible in one API.

## Related Concepts

- [[capability-first-tool-design]] — Tool description discipline
- [[agent-composition-tree-mastra]] — Where tools slot in
- [[graph-based-workflow-engine]] — The workflow counterpart of the tool contract
- [[standard-json-schema-tool-contracts]] — Interop across validation libraries
- [[subagent-as-tool-composition]] — Recursive tool composition
- [[Entities/mastra]] — Canonical implementation

## References

- Raw Article: [[Raw/github-mastra-ai-framework-2026-07-03]]
- Original: https://mastra.ai/docs/tools-mcp/overview
