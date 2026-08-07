---
title: "Research Index: Mastra Framework — TypeScript AI Agent Stack"

details: "This research index covers the Mastra framework — a modern TypeScript framework for AI agents, workflows, RAG, voice, MCP, and observability — extracted from its GitHub repository and official documentation (2026-07-03). It synthesizes the framework's eight architectural patterns, four memory tiers, three tool-kinds, and the layered composition model. Useful for evaluating Mastra against LangGraph, CrewAI, CopilotKit, AutoGen, and Claude Code; for deciding when to use an agent vs a workflow; and for understanding how its pieces fit together."
tags:
  - research
created: 2026-07-03
updated: 2026-07-03
type: research
sources:
  - Raw/github-mastra-ai-framework-2026-07-03.md
---
# Research Index: Mastra Framework — TypeScript AI Agent Stack

**Updated:** 2026-07-03
**Source:** [GitHub mastra-ai/mastra](https://github.com/mastra-ai/mastra) + [mastra.ai/docs](https://mastra.ai/docs) + [Developers Digest comparison](https://www.developersdigest.tech/guides/ai-agent-frameworks-compared) (2026-06-10)

## Overview

Mastra is a modern TypeScript framework for building AI agents and applications. It bundles a model router, an agent abstraction, a graph-based workflow engine, typed tools, multi-tier memory, RAG, MCP, voice, observability, and a standalone Hono server into a single pnpm monorepo (Apache 2.0 core, 25.8k stars, 543 contributors, 99 releases). It is the closest TypeScript-native competitor to LangGraph + CrewAI, with first-class observability, MCP, RAG, and a bundled model gateway.

This index covers:
1. The framework's eight architectural patterns
2. The four memory tiers (and why Observational Memory is the marquee feature)
3. The three tool-kinds and how they enable recursive composition
4. The layered composition model (Agent slots + Mastra composition root)
5. Comparison with other agent frameworks
6. Decision criteria: agent vs. workflow

## Concepts

### Architecture Patterns
- [[agent-composition-tree-mastra]] — Layered stack with central composition root; Agent as the unit, Mastra as the composer
- [[graph-based-workflow-engine]] — `.then` / `.parallel` / `.branch` / `.map` workflow composition with persistent run state
- [[supervisor-agent-pattern]] — Subagent delegation with `onDelegationStart` / `onDelegationComplete` hooks and stable-resource memory isolation
- [[subagent-as-tool-composition]] — Agents, workflows, and MCP tools share a flat tool representation
- [[observational-memory-pattern]] — Three-tier (recent + observations + reflections) long-context memory with 5–40× compression
- [[bundled-model-router]] — Single `'provider/model'` string resolves 3000+ models across 40+ providers
- [[typed-tool-creation]] — `createTool()` factory pattern; plain object tools silently fail
- [[standard-json-schema-tool-contracts]] — Zod / Valibot / ArkType interop via the Standard JSON Schema spec

### Memory and Reasoning
- [[agent-memory-layer-patterns]] — Broader memory pattern landscape (from prior research)
- [[hindsight-memory-architecture]] — Alternative memory architecture (from prior research)

## Tools & Projects

### Agent Frameworks
- [[Entities/mastra]] — Canonical implementation of every concept in this index
- [[Entities/memori-memory-layer]] — Dual-mode (SQL FTS) memory layer (comparable alternative)
- [[Entities/wayfound-ai]] — Production observability for AI agents (comparable alternative)

## Raw Sources

- [[Raw/github-mastra-ai-framework-2026-07-03]] — Verbatim extraction of GitHub README, agent/tool/workflow/memory/RAG/voice/deployment/observability docs, plus comparison table

## Key Sources Table

| Source | Topic | Date | Key Items |
|--------|-------|------|-----------|
| [GitHub mastra-ai/mastra](https://github.com/mastra-ai/mastra) | Repository overview, monorepo structure, recent changes | 2026-07-03 | 25.8k stars, 543 contributors, 99 releases, TS 6.0.3, Tailwind v4 |
| [mastra.ai/docs](https://mastra.ai/docs) | Quickstart and manual setup | 2026-07-03 | `npm create mastra@latest`, Studio at :4111, manual setup with `createTool` and `Agent` |
| [mastra.ai/docs/agents/overview](https://mastra.ai/docs/agents/overview) | Agent abstraction | 2026-07-03 | Agent constructor, model router, tools, instructions |
| [mastra.ai/docs/workflows/overview](https://mastra.ai/docs/workflows/overview) | Workflow engine | 2026-07-03 | `createStep`, `createWorkflow`, `.commit()`, state, suspend/resume |
| [mastra.ai/docs/workflows/control-flow](https://mastra.ai/docs/workflows/control-flow) | Control flow primitives | 2026-07-03 | `.then`, `.parallel`, `.branch`, `.map` with schema rules |
| [mastra.ai/docs/tools-mcp/overview](https://mastra.ai/docs/tools-mcp/overview) | Tools and agents-as-tools | 2026-07-03 | `createTool`, `toModelOutput`, agent/workflow-as-tool |
| [mastra.ai/docs/agents/supervisor-agents](https://mastra.ai/docs/agents/supervisor-agents) | Multi-agent supervisor | 2026-07-03 | Added in `@mastra/core@1.8.0`; `onDelegationStart`, `onDelegationComplete` |
| [mastra.ai/docs/memory/overview](https://mastra.ai/docs/memory/overview) | Memory features | 2026-07-03 | Message history, working memory, semantic recall, observational memory |
| [mastra.ai/docs/memory/observational-memory](https://mastra.ai/docs/memory/observational-memory) | Observational Memory | 2026-07-03 | Three-tier cache, Observer + Reflector, 5–40× compression, prompt cache win |
| [mastra.ai/docs/rag/overview](https://mastra.ai/docs/rag/overview) | RAG | 2026-07-03 | `MDocument`, chunking strategies, `ModelRouterEmbeddingModel`, vector stores |
| [mastra.ai/docs/voice/overview](https://mastra.ai/docs/voice/overview) | Voice | 2026-07-03 | 11 TTS, 8 STT, OpenAI Realtime |
| [mastra.ai/docs/deployment/overview](https://mastra.ai/docs/deployment/overview) | Deployment | 2026-07-03 | Standalone, monorepo, Mastra Platform, Vercel/Netlify/Cloudflare, Inngest |
| [mastra.ai/docs/observability/overview](https://mastra.ai/docs/observability/overview) | Observability | 2026-07-03 | OpenTelemetry traces, auto-derived metrics, correlated logs, composite storage |
| [mastra.ai/docs/mcp/overview](https://mastra.ai/docs/mcp/overview) | MCP | 2026-07-03 | `MCPClient`, `MCPServer`, static vs dynamic tools |
| [Developers Digest comparison](https://www.developersdigest.tech/guides/ai-agent-frameworks-compared) | Framework comparison | 2026-06-10 | Mastra vs LangGraph, CrewAI, CopilotKit, AutoGen, Claude Code |

## Cross-Cutting Themes

### 1. Composition Over Configuration
Mastra's design follows a single principle: every layer in the AI stack is a **slot on a uniform composition tree**. The `Agent` class has slots for model, tools, memory, voice, workflows, subagents, and delegation hooks. The `Mastra` instance composes agents, workflows, MCP servers, storage, and observability. Subagents and workflows are themselves tools. There are no "exceptions" to the rule — every primitive fits the same shape.

### 2. Schema-Validated Boundaries
Every interaction between layers is mediated by a schema. Tool calls have `inputSchema` and `outputSchema` (Standard JSON Schema). Workflow steps must match adjacent schemas. Subagent delegation passes typed prompts. The LLM is untrusted input; schemas are the validation boundary that prevents hallucinated args from reaching business logic.

### 3. The Three Tool Kinds Share a Shape
Tools, subagents, and workflows all appear in the same flat `tools` slot — `weatherTool`, `agent-writer`, `workflow-researchWorkflow`. The parent LLM sees a uniform tool list and routes on descriptions. This is the move that makes recursive composition (supervisor-of-supervisors) a one-line change rather than a new framework feature.

### 4. Memory as a First-Class Production Concern
The Observational Memory pattern (Observer + Reflector + three-tier cache) is the framework's most distinctive technical contribution. It solves the three failures of naive long-context agents: context rot, context waste, and cache invalidation. The 5–40× compression and stable prompt prefix translate directly to lower cost and longer coherent conversations.

### 5. Observability is Day-One, Not Retrofitted
Spans, metrics, and logs are auto-generated from the same runtime traces. Token usage and cost are auto-derived. Storage is composable (OLTP for memory, OLAP for metrics). `SensitiveDataFilter` redacts secrets. External exporters (Langfuse, Datadog, OTEL) plug in. The framework treats observability as a slot, not a feature.

### 6. The TypeScript Wedge
Mastra is the first major agent framework to commit fully to TypeScript with a modern stack (TS 6.0.3, ESM-only, Node 22+). This is a deliberate positioning against LangGraph (Python-first) and CrewAI (Python-only). The `model-router` + `MCP` + `voice` coverage in TypeScript is hard to match.

## Decision Criteria: When to Use Mastra

### Use Mastra when:
- You need a **TypeScript-native** agent framework (not Python)
- You need **multiple AI providers** without installing their SDKs
- You need **observability** out of the box (traces, metrics, logs, cost)
- You need **MCP** as a first-class interop layer (both client and server)
- You need **graph-based workflows** with persistent state and suspend/resume
- You need **multi-agent** coordination with runtime hooks
- You need to deploy to **Vercel / Netlify / Cloudflare / Inngest**

### Consider alternatives when:
- **LangGraph** — if you need Python or explicit graph state machines
- **CrewAI** — if you want role-based "crew" patterns and Python
- **CopilotKit** — if you need an in-app copilot UI (Mastra is the backend; CopilotKit is the frontend)
- **AutoGen** — if you need Python multi-agent chat (GroupChat pattern)
- **Claude Code** — if you need an agentic terminal/code generation tool

## Decision Criteria: Agent vs Workflow (within Mastra)

| Need | Use |
|------|-----|
| Open-ended task; LLM decides steps | **Agent** |
| Predetermined multi-step process; explicit control flow | **Workflow** |
| Multi-step, fixed graph + agents at certain steps | **Workflow with `createStep` calling `agent.generate()`** |
| Open-ended delegation to specialists with feedback | **Supervisor agent** |
| Recursive composition (supervisor-of-supervisors) | **Subagent-as-tool** |

## Next Research Directions

- [ ] **Benchmark Mastra vs LangGraph** on a stateful workflow (e.g., a research pipeline with branches, parallel agents, and human-in-the-loop approval) — measure developer ergonomics, latency, and observability quality
- [ ] **Evaluate Observational Memory in production** — measure prompt cache hit rates, compression ratios, and cost savings vs naive message history
- [ ] **Prototype a supervisor-of-supervisors** — build a 3-level agent hierarchy using subagent-as-tool composition and measure delegation quality
- [ ] **Compare Mastra's MCP server to a standalone MCP server** — measure latency and observability for an in-app tool
- [ ] **Test the bundled model router** — verify provider switching is frictionless and that token/cost reporting is uniform across vendors
- [ ] **Evaluate the workflow engine's parallel-step failure semantics** — determine if the "whole block fails" default is the right design for fan-out workloads

## References

- Raw Article: [[Raw/github-mastra-ai-framework-2026-07-03]]
- Original: https://github.com/mastra-ai/mastra
