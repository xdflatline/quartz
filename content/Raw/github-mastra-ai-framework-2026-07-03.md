---
title: "Mastra Framework — TypeScript AI Agents (GitHub Repository + Docs)"
detail: "Raw extraction of the Mastra framework's repository and documentation: capabilities, core abstractions, and how they are implemented."
details: "Verbatim extraction of the Mastra framework's GitHub README, agent/workflow/tool/memory/RAG/voice/deployment/observability documentation, plus a comparative framing against LangGraph, CrewAI, CopilotKit, AutoGen, and Claude Code. Captures the core abstractions (Agent, createTool, createStep, createWorkflow, Memory, Observational Memory, RAG, MCP, Voice), the model router, the workflow control-flow primitives, and the multi-agent supervisor pattern."
tags:
  - raw
created: 2026-07-03
updated: 2026-07-03
type: raw
source: "https://github.com/mastra-ai/mastra"
---

# Mastra Framework — TypeScript AI Agents (GitHub Repository + Docs)

**Source:** GitHub (https://github.com/mastra-ai/mastra) and mastra.ai/docs
**Date Retrieved:** 2026-07-03
**Type:** Repository + Documentation

---

## Repository Summary

**Repository:** [mastra-ai/mastra](https://github.com/mastra-ai/mastra)
**Description:** The modern TypeScript framework for AI-powered applications and agents.
**Stats:** 25.8k stars | 2.3k forks | 96 watchers | 99 releases (latest: July 1, 2026) | 543 contributors | 1.9k+ dependents
**Language:** TypeScript 99.3%

> "Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack. It includes everything you need to go from early prototypes to production-ready applications."

It integrates with React, Next.js, and Node, or deploys as a standalone server.

## Key Features

| Feature | Description |
|---------|-------------|
| **Model Routing** | Connect to 40+ providers (OpenAI, Anthropic, Gemini, Groq, Google, Cerebras, Mistral, etc.) through one standard interface. The model router exposes 3000+ models. |
| **Agents** | Autonomous agents that use LLMs and tools to solve open-ended tasks, reasoning about goals and iterating until completion. |
| **Workflows** | Graph-based workflow engine with intuitive control flow: `.then()`, `.branch()`, `.parallel()`. |
| **Human-in-the-loop** | Suspend agents/workflows and await user input/approval before resuming. Uses storage to remember execution state indefinitely. |
| **Context Management** | Conversation history, RAG data retrieval, and Observational Memory for coherent agent behavior. |
| **Integrations** | Bundle into React/Next.js/Node apps or ship as standalone endpoints. Compatible with Vercel AI SDK UI and CopilotKit. |
| **MCP Servers** | Author Model Context Protocol servers, exposing agents/tools/resources via the MCP interface. |
| **Production Essentials** | Built-in evals and observability for continuous observation, measurement, and refinement. |

## Quick Start

```bash
npm create mastra@latest
```

Post-install:
```bash
npx bgproc start -n <project-name> -w -- npm run dev
# Mastra Studio: http://localhost:4111
```

## Repository Structure (Monorepo)

pnpm monorepo with the following key areas:

| Directory | Purpose |
|-----------|---------|
| `packages/` | Core framework packages |
| `agent-sdks/` / `client-sdks/` | SDKs for agents and clients |
| `deployers/` | Deployment tooling |
| `server-adapters/` | Server framework integrations (Hono, Express, Fastify, Koa) |
| `stores/` | Storage backends |
| `auth/` | Authentication and authorization |
| `observability/` | Telemetry and tracing tools |
| `voice/` | Voice/TTS capabilities |
| `browser/` | Browser automation |
| `workflows/` | Workflow engine |
| `integrations/` | Third-party integrations |
| `signals/` | Signal providers (e.g., GitHub signals) |
| `pubsub/` | Pub/sub messaging |
| `channels/slack/` | Slack channel integration |
| `embedders/voyageai/` | Embedding providers |
| `examples/` / `templates/` / `explorations/` | Sample code and templates |
| `docs/` | Documentation source |
| `e2e-tests/` | End-to-end tests |
| `mastracode/` | MastraCode web UI and tooling |

## Recent Development Highlights (as of 2026-07)

### Infrastructure & Tooling
- **TypeScript 6.0.3 Upgrade** — Monorepo upgraded from 5.9.3 to 6.0.3 to prepare for the eventual Go-based TS 7 migration. Removed deprecated `baseUrl` options, switched root `moduleResolution` to `"bundler"`, and patched `tsup` for compatibility.
- **Tailwind CSS v4 Migration** — Playground UI fully migrated to Tailwind v4 with CSS-first `@theme` configuration, removing legacy `tailwind.config.ts` and PostCSS setups.
- **Consolidated AI Assistant Commands** — All slash commands centralized in `.mastracode/commands/` with symlinks from `.claude/`, `.cursor/`, and `.opencode/`.
- **Lint/Format Unification** — `pnpm lint` runs ESLint and Prettier concurrently via Turbo; `pnpm format` runs them sequentially to avoid file-write collisions.

### Core Framework & Features
- **Auth & RBAC** — New `@mastra/core/auth` export with interfaces for RBAC, sessions, SSO, credentials, ACL, and user management. Server adapters (Hono, Express, Fastify, Koa) integrated.

---

## Agents Overview

Agents use LLMs and tools to solve open-ended tasks. They reason about goals, decide which tools to use, retain conversation memory, and iterate internally until the model emits a final answer or an optional stop condition is met. Agents produce structured responses you can render in your UI or process programmatically. Use agents directly or compose them into workflows or multi-agent systems.

### Minimal Agent Example

```ts
// src/mastra/agents/weather-agent.ts
import { Agent } from '@mastra/core/agent'
import { weatherTool } from '../tools/weather-tool.ts'

export const weatherAgent = new Agent({
  id: 'weather-agent',
  name: 'Weather Agent',
  instructions: `...`,
  model: 'openai/gpt-5.5',
  tools: { weatherTool },
})
```

**Model format rules:**
- Use the Mastra model router format: `'provider/model'`
- Use `/` (not `:`) to separate provider and model
- It's a bundled model gateway — do not install any `ai-sdk` package unless Mastra's documentation explicitly says otherwise

### Agents vs Workflows

- **Use agents** when the task is open-ended and the steps aren't known in advance. An agent decides which tools to call, how many times to loop, and when to stop. You provide the goal and constraints instead of defining each step.
- **Use workflows** for predetermined, multi-step processes with explicit control flow.

---

## Tools (createTool)

Plain object tool definitions **silently fail**. Tools **MUST** be defined via `createTool()` from `@mastra/core/tools` with `id`, `description`, `inputSchema` (Zod), and `execute()`.

`execute()` receives two parameters:
1. The validated input data (based on `inputSchema`)
2. An optional execution context object containing `requestContext`, `tracingContext`, `abortSignal`, and other execution metadata

```ts
import { createTool } from '@mastra/core/tools'
import { z } from 'zod'

export const weatherTool = createTool({
  id: 'get-weather',
  description: 'Get current weather for a location',
  inputSchema: z.object({ location: z.string().describe('City name') }),
  outputSchema: z.object({ output: z.string() }),
  execute: async ({ location }) => ({ output: `The weather in ${location} is sunny` }),
})
```

### Schema Library Support
Tools support any library implementing [Standard JSON Schema](https://standardschema.dev/json-schema): **Zod**, **Valibot**, **ArkType**.

### Agents as Tools (Subagents)
Add subagents through the `agents` configuration to create a supervisor. Mastra converts each subagent to a tool named `agent-<key>`. Include a `description` on each subagent so the supervisor knows when to delegate.

```ts
export const supervisor = new Agent({
  id: 'supervisor',
  agents: { writer }, // toolName: "agent-writer"
})
```

### Workflows as Tools
Add workflows through the `workflows` configuration. Mastra converts each to a tool named `workflow-<key>`, using the workflow's `inputSchema` and `outputSchema`.

### Shape Output for the Model
Use `toModelOutput` when a tool returns rich structured data for your application, but you want the model to receive a smaller or multimodal representation. Preserves full tool result in your app while keeping model context focused.

---

## Workflows (createStep / createWorkflow)

Workflows define complex, multi-step task sequences with explicit control over execution order and data flow. They run on Mastra's built-in execution engine by default, or deploy to workflow runners like Inngest for managed infrastructure.

### Core Principles
- **Steps**: Define with `createStep` — specify input/output schemas and business logic
- **Composition**: Chain steps with `createWorkflow` to define execution flow
- **Execution**: Run the full sequence with built-in support for **suspension, resumption, and streaming**

### Creating a Step

```ts
import { createStep } from '@mastra/core/workflows'
import { z } from 'zod'

const step1 = createStep({
  id: 'step-1',
  inputSchema: z.object({ message: z.string() }),
  outputSchema: z.object({ formatted: z.string() }),
  execute: async ({ inputData }) => ({ formatted: inputData.message.toUpperCase() }),
})
```

### Creating a Workflow

```ts
import { createWorkflow, createStep } from "@mastra/core/workflows";

export const testWorkflow = createWorkflow({
  id: "test-workflow",
  inputSchema: z.object({ message: z.string() }),
  outputSchema: z.object({ output: z.string() })
})
  .then(step1)
  .commit();
```

### Control Flow

#### `.then()` — Sequential
```ts
.then(step1)
.then(step2)
```

#### `.parallel()` — Concurrent
```ts
.parallel([step1, step2])
.then(step3)
```
Output is an object keyed by each step's `id`. If any parallel step throws, the entire block fails (handle errors inside the step with `try/catch`).

#### `.branch()` — Conditional
```ts
.branch([
  [async ({ inputData: { value } }) => value > 10, stepA],
  [async ({ inputData: { value } }) => value <= 10, stepB],
])
```
Only one branch executes based on the first condition that evaluates to true. Use optional fields in the next step's `inputSchema` to handle multiple possible branches.

#### `.map()` — Input Data Mapping
When output of one step doesn't match the schema of the next, use `.map()` to transform data inline.

### Workflow State
Share values across steps without threading them through every `inputSchema`/`outputSchema`. Use `stateSchema` with `state` and `setState` for tracking progress, accumulating results, or sharing configuration.

```ts
const step1 = createStep({
  stateSchema: z.object({ counter: z.number() }),
  execute: async ({ inputData, state, setState }) => {
    setState({ ...state, counter: state.counter + 1 })
    return { formatted: inputData.message.toUpperCase() }
  },
})
```

### Workflows as Steps (Nesting)
Nest workflows to reuse logic inside larger compositions. Child workflows follow the same schema rules. `cloneWorkflow()` creates an independent copy under a new ID, tracked separately in logs and observability.

---

## Memory

Memory enables agents to remember **user messages, agent replies, and tool results across interactions**, maintaining consistency, conversation flow, and improving answers over time.

### Memory Features

| Feature | Purpose |
|---------|---------|
| **Observational Memory** *(Recommended)* | Background agents compress old messages into dense observations, keeping the context window small while preserving long-term memory. |
| **Working Memory** | Persistent, structured user data such as names, preferences, and goals. |
| **Semantic Recall** | Retrieves relevant past messages by semantic meaning rather than exact keywords. |
| **Multi-User Threads** | Shares one thread between multiple users. |

If combined memory exceeds the model's context limit, **memory processors** filter, trim, or prioritize content. Results are stored in configured **storage providers**.

### Message History
Pass a `memory` object with `resource` and `thread` to track history:
- `resource` — Stable identifier for the user or entity
- `thread` — ID that isolates a specific conversation or session

> Each thread has an owner (`resourceId`) that **cannot be changed** after creation. Avoid reusing the same thread ID for threads with different owners.

### Observational Memory (OM)
For long-running conversations, raw message history grows until it fills the context window, degrading performance. Observational Memory solves this by running background agents that compress old messages into dense observations.

Two background agents — an **Observer** and a **Reflector** — watch conversations and maintain a dense observation log that replaces raw message history as it grows.

**Three-Tier System:**
1. **Recent messages:** Exact conversation history for the current task.
2. **Observations:** Concise notes written by the Observer when message history exceeds a threshold (default `messageTokens` = 30,000).
3. **Reflections:** Condensed observations written by the Reflector when observations grow too long (default `observationTokens` = 40,000).

**Benefits:**
- **Prompt caching:** OM's context is stable and appends over time, keeping the prompt prefix cacheable and reducing costs.
- **Compression:** Raw message history and tool results compress into a dense observation log (typically **5–40×** compression).
- **Zero context rot:** The agent sees relevant information instead of noisy tool calls.

**Early Activation:** Activate buffered observations before the token threshold is reached (e.g., prompt caches expiring, switching model providers). Per-phase control for observations and reflections.

**Temporal Gap Markers:** Insert a reminder before a new user message when enough time has passed (≥10 minutes). Off by default.

**Supported storage:** `@mastra/pg`, `@mastra/libsql`, `@mastra/mongodb` (only).

### Memory in Multi-Agent Systems
When a supervisor agent delegates to a subagent, Mastra isolates subagent memory automatically:
- **Thread ID** — Fresh unique ID per delegation
- **Resource ID** — Deterministic: `{parentResourceId}-{agentName}`. Stable across delegations, so resource-scoped memory persists
- **Memory Instance** — Subagent inherits the supervisor's `Memory` instance (if no own config)

---

## RAG (Retrieval-Augmented Generation)

Mastra's RAG system provides standardized APIs to process and embed documents, support for multiple vector stores, chunking and embedding strategies, and observability for tracking embedding and retrieval performance.

### Minimal RAG Example

```ts
import { embedMany } from 'ai'
import { PgVector } from '@mastra/pg'
import { MDocument } from '@mastra/rag'
import { z } from 'zod'

// 1. Initialize document
const doc = MDocument.fromText(`Your document text here...`)

// 2. Create chunks
const chunks = await doc.chunk({ strategy: 'recursive', size: 512, overlap: 50 })

// 3. Generate embeddings
const { embeddings } = await embedMany({
  values: chunks.map(c => c.text),
  model: new ModelRouterEmbeddingModel('openai/text-embedding-3-small'),
})

// 4. Store in vector database
const pgVector = new PgVector({ id: 'pg-vector', connectionString: process.env.POSTGRES_CONNECTION_STRING })
await pgVector.upsert({ indexName: 'embeddings', vectors: embeddings })

// 5. Query similar chunks
const results = await pgVector.query({ indexName: 'embeddings', queryVector, topK: 3 })
```

### Document Processing
Documents are chunked using various strategies (recursive, sliding window, etc.) and enriched with metadata.

### Vector Storage
Mastra supports multiple vector stores: pgvector, Pinecone, Qdrant, MongoDB.

---

## Voice

Mastra's Voice system provides a **unified interface** for voice interactions: text-to-speech (TTS), speech-to-text (STT), and real-time speech-to-speech (STS).

### TTS Providers (11 total)
OpenAI, Azure, ElevenLabs, PlayAI, Google, Cloudflare, Deepgram, Inworld, Speechify, Sarvam, Murf.

### STT Providers (8 total)
OpenAI, Azure, ElevenLabs, Google, Cloudflare, Deepgram, Inworld, Sarvam.

### STS / Realtime
OpenAI Realtime supported. Lifecycle: instantiate → `connect()` → listen for events → `speak()` → `send(micStream)`.

---

## Deployment

### Runtime Support
- **Node.js** v22.13.0+ (Node 22.18.0+ required to run TypeScript files directly)
- **Bun**
- **Deno**
- **Cloudflare**

### Deployment Options
1. **Mastra Server (Standalone)** — Hono-powered server. Build: `mastra build`. Use when you need full control, long-running processes, or WebSocket connections.
2. **Monorepo** — Deploy a Mastra server as part of a monorepo setup.
3. **Mastra Platform** — Hosted products:
   - **Observability** — Searchable traces, logs, metrics
   - **Studio** — Hosted visual environment for testing agents/workflows/traces
   - **Server** — Production deployment target
4. **Cloud Providers** — Built-in deployers for Vercel, Netlify, Cloudflare. Also: Amazon EC2, AWS Lambda, Azure App Services, Digital Ocean.
5. **Web Framework Integration** — Deploys alongside Next.js or Astro using the framework's standard process.

### Workflow Runners
- **Default:** Mastra's built-in execution engine
- **Production:** Deploy to specialized platforms like **Inngest** (step memoization, automatic retries, real-time monitoring)

---

## Observability

Mastra's observability system provides visibility into every **agent run**, **workflow step**, **tool call**, and **model interaction** through three complementary signals: **traces**, **logs**, and **metrics**.

### Core Documentation Areas
- **Configuration** — One-time setup for traces, logs, metrics
- **Storage** — Backend selection for persisted signals
- **Tracing** — Hierarchical timeline of spans (OpenTelemetry-aligned)
- **Logging** — Structured log forwarding correlated to traces
- **Metrics** — Auto-extraction of duration, token usage, cost
- **Integrations** — Exporters for Studio, Mastra platform, Langfuse, Datadog, OpenTelemetry-compatible

### Unified Correlation
All three signals share correlation IDs: `trace ID`, `span ID`, `entity type`, `entity name`. Jump between a metric spike, the traces behind it, and the logs within those traces.

### Storage Backend Requirements
| Signal | Backend Requirements |
|--------|----------------------|
| **Traces** | Work with most backends |
| **Metrics & Logs** | Require an **OLAP-capable** store (DuckDB for dev, ClickHouse for prod) |

### Composite Storage
Route different observability domains to different stores via `MastraCompositeStore`:
```ts
storage: new MastraCompositeStore({
  default: new LibSQLStore({ url: 'file:./mastra.db' }),
  domains: { observability: await new DuckDBStore().getStore('observability') },
})
```

---

## MCP (Model Context Protocol)

Mastra supports MCP — agents can call tools regardless of language or hosting environment. Mastra can also **author MCP servers**, exposing agents, tools, workflows, prompts, and resources to any MCP-compatible client.

### Core Classes
| Class | Purpose |
|-------|---------|
| **`MCPClient`** | Connects to external MCP servers (local `npx` packages or remote HTTP(S) endpoints) |
| **`MCPServer`** | Exposes Mastra primitives to MCP-compatible clients |

### Tool Approval
Require human approval before execution using `requireToolApproval`. Integrates with the existing human-in-the-loop approval flow. Also supports a function for dynamic per-call decisions.

### Static vs. Dynamic Tools
| Feature | Static (`await mcp.listTools()`) | Dynamic (`await mcp.listToolsets()`) |
|---------|----------------------------------|------------------------------------|
| **Use Case** | Single-user, static config | Multi-user, dynamic config (SaaS) |
| **Configuration** | Fixed at agent initialization | Per-request, dynamic |
| **Credentials** | Shared across all uses | Can vary per user/request |

---

## Supervisor Agents (Multi-Agent)

**Added in:** `@mastra/core@1.8.0`

A supervisor agent coordinates multiple subagents using `Agent.stream()` or `Agent.generate()`. Subagents configured on the supervisor's `agents` property are exposed as tools (named `agent-<key>`). The supervisor uses its own `instructions` plus each subagent's `description` to decide when and how to delegate.

### Common Use Cases
- Research and writing workflows
- Multi-step tasks needing different expertise at each stage
- Fine-grained control over delegation behavior

### Delegation Hooks
- **`onDelegationStart`** — Return `{ proceed: true|false, modifiedPrompt, modifiedMaxSteps, rejectionReason }` to intercept/modify/reject delegations. Context: `primitiveId`, `prompt`, `iteration`.
- **`onDelegationComplete`** — Return `{ feedback }` to inject into supervisor memory, or call `context.bail()` to stop the supervisor loop immediately.

### Message Filtering
`messageFilter` limits or sanitizes what is shared with subagents (default: full conversation context).

### Subagent Result Context
By default, only the subagent's **text response** is added to the supervisor model context in later iterations. `includeSubAgentToolResultsInModelContext: true` to include nested tool calls and metadata.

---

## Comparative Framing (Developers Digest, 2026-06-10)

| Framework | Language | Architecture | Multi-agent | Tool Definition | State Mgmt | Streaming | Best For |
|-----------|----------|--------------|-------------|-----------------|------------|-----------|----------|
| **Mastra** | TypeScript | Agents + typed workflows | Supervisor agents + workflows | Typed tools, MCP tools | Memory + persisted workflow state | Agent and workflow streaming | TypeScript agent products |
| **LangGraph** | Python, JS/TS | Graph-based state machine | Manual graph wiring | Annotated functions | Explicit graph state | Full support | Complex stateful workflows |
| **CrewAI** | Python | Role-based crews | Built-in crew system | Decorated functions | Automatic crew state | Limited | Team simulations, content pipelines |
| **CopilotKit** | React, Angular, TS runtime | Frontend + runtime + AG-UI agent backend | Connects to backend agent frameworks | Frontend tools, backend tools, MCP apps | Shared app-agent state over AG-UI | AG-UI event stream | In-app copilots and generative UI |
| **AutoGen** | Python, .NET | Conversation-based groups | GroupChat pattern | Function schemas | Conversation history | Limited | Research, multi-agent chat |
| **Claude Code** | TypeScript SDK / CLI | Agentic loop + sub-agents | Sub-agent spawning | MCP servers + built-in tools | Conversation context + memory | Full support | Code generation, dev automation |

> **Key clarification:** Mastra and CopilotKit are not the same category. Mastra = TypeScript **backend** framework. CopilotKit = **Frontend/runtime layer** for bringing agents into an application.

> **Mastra is the closest TypeScript-native competitor to LangGraph + CrewAI**, with first-class observability, MCP, RAG, voice, and a bundled model router.

---

## Architecture Summary (Implementation Patterns)

### Model Router (Bundled Gateway)
A single `'provider/model'` string is resolved against a bundled gateway that exposes 3000+ models from 40+ providers. Environment variables (e.g., `OPENAI_API_KEY`) are automatically inferred from the provider name. Internal abstraction means the user never imports a provider SDK directly (in normal usage).

### Agents as the Reasoning Layer
- `Agent` class wraps an LLM, system prompt (`instructions`), tool set, optional `voice`, optional `memory`, optional `workflows`, optional `agents` (subagents), optional `delegation` hooks.
- Internal agentic loop: model emits → tool calls executed → results fed back → repeat until stop condition.
- `maxSteps` caps iterations.

### Workflows as the Control-Flow Layer
- `createStep` (atomic unit) and `createWorkflow` (composer) form a directed graph.
- Composition primitives: `.then()`, `.parallel()`, `.branch()`, `.map()`, `.commit()`.
- State is orthogonal to input/output: `stateSchema` + `setState` allow cross-step shared mutable state.
- Built-in execution engine supports **suspension, resumption, and streaming** by persisting run state to a storage backend.
- Optional deploy target: Inngest (managed runner with step memoization + retries).

### Tools as the Side-Effect Layer
- `createTool` is mandatory (plain objects silently fail).
- Schemas are Standard JSON Schema compatible (Zod, Valibot, ArkType).
- `toModelOutput` separates app-facing tool result from model-facing summary.
- Subagents and workflows are themselves exposed as tools (`agent-<key>`, `workflow-<key>`), enabling recursive composition.

### Memory as the Context Layer
- Four orthogonal capabilities: message history, working memory, semantic recall, observational memory.
- **Observational Memory is the marquee feature** — a two-agent (Observer + Reflector) background system that compresses old messages into observations, then reflections, in a three-tier cache. Achieves 5–40× compression while keeping the prompt prefix cacheable.
- Storage is pluggable (libSQL, PostgreSQL, MongoDB), with composite routing for hybrid observability.

### RAG as the Knowledge Layer
- `MDocument` is a first-class document abstraction.
- Chunking strategies: recursive, sliding window, etc.
- Embeddings use `ModelRouterEmbeddingModel` (same router as agents).
- Vector stores: pgvector, Pinecone, Qdrant, MongoDB.

### MCP as the Interop Layer
- `MCPClient` consumes external MCP servers (stdio `npx` packages or HTTP endpoints).
- `MCPServer` exposes Mastra primitives as MCP resources.
- **Static vs Dynamic tools** map cleanly to single-user CLI vs. multi-user SaaS — credentials can be per-request via `listToolsets()`.

### Observability as the Production Layer
- OpenTelemetry-aligned spans for every agent run, workflow step, tool call, model interaction.
- **Traces + Logs + Metrics** are auto-correlated via shared IDs.
- Metrics are auto-derived (duration, token count, cost) — no extra instrumentation.
- Exporters: `MastraStorageExporter` (local), `MastraPlatformExporter` (Mastra cloud), Langfuse, Datadog, any OTEL-compatible.
- `SensitiveDataFilter` redacts secrets from spans.

### Voice as the Multimodal Layer
- `voice` property on `Agent` enables TTS, STT, or STS.
- 11 TTS providers, 8 STT providers, OpenAI Realtime for STS.
- `playAudio`/`getMicrophoneStream` utilities from `@mastra/node-audio`.

### Deployment as the Runtime Layer
- Build: `mastra build` produces a Hono server.
- Adapters for Hono, Express, Fastify, Koa.
- Hosted: Mastra Platform (Observability + Studio + Server).
- Cloud deployers for Vercel, Netlify, Cloudflare.
- Specialized: Inngest for workflow orchestration.

---

## Notable Implementation Details

### Critical Implementation Rules (from docs)

1. **Tools MUST use `createTool()`** — Plain object tool definitions **silently fail** to execute.
2. **Model format uses `/`, not `:`** — `openai/gpt-5.5` not `openai:gpt-5.5`.
3. **Do not install `ai-sdk`** unless explicitly told — Mastra bundles its own gateway.
4. **Always include file extensions** in local imports (Node 22.18+ runs TS directly).
5. **Each thread has an immutable owner** (`resourceId`) — never reuse thread IDs across different owners.
6. **For Observational Memory clients** — send only the new message, not the full conversation history, to avoid timestamp conflicts.
7. **Parallel step failures** — Any throw fails the whole block; handle inside the step with `try/catch` and return typed results.
8. **Schema mismatches in pipelines** — Use `.map()` between steps to transform output to the next step's `inputSchema`.

### TypeScript Conventions

- ESM-only (`"type": "module"` in `package.json`).
- TS 6.0.3 with `moduleResolution: "bundler"`.
- `allowImportingTsExtensions: true` for direct Node 22 TS execution.
- Strict mode, `skipLibCheck: true`.

### Storage Backends

- `LibSQLStore` (file-based SQLite, also `:memory:` for tests)
- `PgVector`, `MongoDB`, `Upstash` (vector stores)
- `DuckDBStore` (OLAP, for observability metrics)
- `MastraCompositeStore` (multi-backend routing)

### Authentication (New)

`@mastra/core/auth` (recent addition) — interfaces for RBAC, sessions, SSO, credentials, ACL, user management. Server adapters (Hono, Express, Fastify, Koa) integrated.
