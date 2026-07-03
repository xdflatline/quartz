---
title: "Agent Composition Tree (Mastra)"
detail: "Layered composition pattern in Mastra where every concern (model, tools, workflows, memory, voice, subagents, MCP, observability) is a slot on a central Agent or Mastra instance, with subagents and workflows themselves exposed as tools for recursive nesting."
details: "A composition pattern specific to Mastra's architecture. The Agent class is the primary unit and owns orthogonal slots for model (via the bundled router), tools (createTool), memory (4 tiers), voice, workflows (as tools), subagents (as tools), and delegation hooks. The Mastra instance composes agents, workflows, MCP servers, storage, and observability. Storage is pluggable per concern (libSQL/Postgres/MongoDB for memory; DuckDB/ClickHouse for observability). The three tool-kinds (primitives, agents, workflows) share a flat tool representation, which is the move that enables recursive composition (supervisor-of-supervisors)."
tags:
  - concepts
created: 2026-07-03
updated: 2026-07-03
type: concept
sources:
  - Raw/github-mastra-ai-framework-2026-07-03.md
---
# Agent Composition Tree (Mastra)

**Source:** [[Raw/github-mastra-ai-framework-2026-07-03]]
**Category:** Architecture Pattern
**Status:** Production-validated (Mastra canonical implementation)

> Note: This page describes Mastra's specific composition tree. The general "agent-first pipeline architecture" pattern (no central orchestrator; agent reads manifests and skills) is a separate concept — see [[agent-first-pipeline-architecture]] for the OpenMontage variant.

## Overview

Mastra organizes an AI application as a **layered stack with a central composition root**. The `Agent` class is the primary unit; it owns slots for model, tools, memory, voice, workflows (as tools), agents (as tools/subagents), and delegation hooks. The `Mastra` instance composes agents, workflows, MCP servers, storage, and observability. Storage is pluggable per layer. The pattern is what makes a multi-provider, multi-tool, multi-agent system feel like a single coherent product.

## The Composition Tree

```
Mastra (composition root)
├── agents: { weatherAgent, supervisor }
│     ├── Agent (reasoning layer)
│     │     ├── model: 'openai/gpt-5.5'        ← Bundled Model Router
│     │     ├── instructions: '...'
│     │     ├── tools: { weatherTool }         ← Typed Tool Creation
│     │     ├── workflows: { researchWorkflow } ← Subagent-as-Tool
│     │     ├── agents: { writer }             ← Subagent-as-Tool
│     │     ├── memory: Memory                 ← Observational Memory
│     │     ├── voice: OpenAIVoice             ← Voice Layer
│     │     └── delegation: { onDelegationStart, onDelegationComplete }
│     └── Agent ...
├── workflows: { publishWorkflow }              ← Graph-Based Workflow Engine
├── mcpServers: { testMcpServer }               ← MCP Server class
├── storage: LibSQLStore                        ← Pluggable Storage
├── observability: Observability                ← Traces + Logs + Metrics
└── deployer: Hono adapter                      ← Runtime
```

## The Agent as the Primary Unit

```ts
export const weatherAgent = new Agent({
  id: 'weather-agent',
  name: 'Weather Agent',
  instructions: '...',
  model: 'openai/gpt-5.5',              // Bundled Model Router slot
  tools: { weatherTool },                // Typed Tool Creation slot
  memory: new Memory({ ... }),           // Memory slot
  voice: new OpenAIVoice(),              // Voice slot
  workflows: { researchWorkflow },       // Workflows-as-tools slot
  agents: { writer },                    // Subagents slot
})
```

Each slot is independent and orthogonal: swap the model, swap the memory backend, swap the voice provider — none of the others need to change.

## The Workflow as the Control-Flow Unit

```ts
export const publishWorkflow = createWorkflow({
  id: 'publish',
  inputSchema: z.object({ topic: z.string() }),
  outputSchema: z.object({ url: z.string() }),
  stateSchema: z.object({ trace: z.array(z.string()) }),
})
  .then(researchStep)
  .parallel([draftStep, imageStep])
  .then(reviewStep)
  .commit()
```

Workflows are first-class citizens on the same level as agents: they live in `Mastra.workflows`, can be invoked standalone, or can be exposed as tools to an agent.

## The Storage Layer Is Pluggable Per Concern

| Concern | Storage Options |
|---------|-----------------|
| **Memory** | libSQL, PostgreSQL, MongoDB |
| **Observability metrics** | DuckDB (dev), ClickHouse (prod) |
| **Composite routing** | `MastraCompositeStore` routes different domains to different backends |

```ts
storage: new MastraCompositeStore({
  default: new LibSQLStore({ url: 'file:./mastra.db' }),
  domains: { observability: await new DuckDBStore().getStore('observability') },
})
```

This is the right shape for production: hot data in OLTP stores, cold analytics data in OLAP stores.

## The Observability Layer Auto-Collects

Every agent run, workflow step, tool call, and model interaction produces a span. The runtime **auto-extracts duration, token counts, and cost** from each span — no extra instrumentation. Traces, logs, and metrics share correlation IDs.

```ts
observability: new Observability({
  configs: {
    default: {
      serviceName: 'mastra',
      exporters: [
        new MastraStorageExporter(),    // persist locally
        new MastraPlatformExporter(),   // send to Mastra cloud
      ],
      spanOutputProcessors: [new SensitiveDataFilter()],
    },
  },
})
```

## The MCP Layer Connects the System to the World

- `MCPClient` — connect to external MCP servers (stdio `npx` packages or HTTP endpoints)
- `MCPServer` — expose Mastra primitives as MCP resources to any MCP-compatible client
- **Static tools** (`listTools()`) for single-user apps; **dynamic tools** (`listToolsets()`) for multi-user SaaS with per-request credentials

## The Runtime Layer Targets Node, Bun, Deno, and Cloudflare

```bash
mastra build  # produces a Hono server
```

Server adapters exist for Hono, Express, Fastify, and Koa. Cloud deployers are built-in for Vercel, Netlify, and Cloudflare. Workflows can be deployed to Inngest for managed orchestration.

## Why This Architecture

### One Mental Model
Every layer is a slot on the same composition tree. New developers learn the slots, not the framework's internal abstractions.

### Layered Orthogonality
Swapping any one layer (model, memory, voice, storage) doesn't disturb the others. Production hardening can be applied per-layer.

### Subagent-as-Tool is the Composition Lever
Recursive composition (supervisor-of-supervisors) requires no new abstraction. Adding a subagent to an Agent is a single config key.

### Persistent Run State Enables Human-in-the-Loop
Workflows persist execution state at every step boundary. Suspend and resume indefinitely; the runtime restores context from storage.

### Observability is Day-One
The framework ships with auto-derived traces, metrics, and logs correlated by ID. Production teams don't have to retrofit observability.

## Key Insights

1. **The Agent is the unit, the Mastra is the composition root** — a clear hierarchy maps to clean code organization.
2. **Each slot is orthogonal** — the design respects the principle of independent layers.
3. **Storage is per-concern, not per-app** — composite stores let you mix OLTP and OLAP without code changes.
4. **Observability is auto-derived** — you don't write tracing code; you write business code.
5. **Subagent-as-tool + workflow-as-tool + MCP-as-tool** — the three tool kinds share the same flat representation, which is what enables recursive composition.

## Related Concepts

- [[agent-first-pipeline-architecture]] — The general "no central orchestrator" pattern (different concept, see warning above)
- [[bundled-model-router]] — The model slot
- [[typed-tool-creation]] — The tools slot
- [[graph-based-workflow-engine]] — The workflows slot
- [[observational-memory-pattern]] — The memory slot
- [[supervisor-agent-pattern]] — The agents slot, with hooks
- [[subagent-as-tool-composition]] — Why the three tool kinds share a shape
- [[standard-json-schema-tool-contracts]] — Why the schemas are interchangeable
- [[Entities/mastra]] — Canonical implementation

## References

- Raw Article: [[Raw/github-mastra-ai-framework-2026-07-03]]
- Original: https://mastra.ai/docs
