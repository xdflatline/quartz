---
title: "Mastra"
detail: "TypeScript framework for AI agents, workflows, RAG, voice, and MCP. 25.8k stars, pnpm monorepo, Apache 2.0 core, 3000+ models via bundled gateway."
details: "Mastra is a modern TypeScript framework for building AI-powered applications and agents. It bundles a model router (3000+ models from 40+ providers via a single 'provider/model' string), a graph-based workflow engine (.then/.parallel/.branch/.map), an agent abstraction with subagent delegation, typed tools (Zod/Valibot/ArkType), four-tier memory (message history, working memory, semantic recall, observational memory with Observer+Reflector background agents), RAG with pluggable vector stores, MCP client and server support, 11 TTS + 8 STT voice providers, OpenTelemetry-aligned observability, and a Hono-based standalone server. Apache 2.0 core."
tags:
  - entities
created: 2026-07-03
updated: 2026-07-03
type: entity
sources:
  - Raw/github-mastra-ai-framework-2026-07-03.md
---
# Mastra

**Source:** GitHub ([mastra-ai/mastra](https://github.com/mastra-ai/mastra)) + mastra.ai/docs
**Category:** Tool / Open Source Framework
**Repository:** https://github.com/mastra-ai/mastra
**Website:** https://mastra.ai
**License:** Apache 2.0 (core)

## Overview

Mastra is a **modern TypeScript framework for building AI-powered applications and agents**. It provides a single integrated stack: a bundled model gateway, an agent abstraction, a graph-based workflow engine, typed tools, multi-tier memory, RAG, MCP, voice, observability, and a standalone Hono server — all in one pnpm monorepo. It targets Node.js 22.18+, Bun, Deno, and Cloudflare.

## Key Details

### Repository Stats (as of 2026-07-03)
- 25.8k stars
- 2.3k forks
- 543 contributors
- 99 releases (latest 2026-07-01)
- 1.9k+ dependent projects
- TypeScript 99.3%

### Core Packages (Monorepo)
| Directory | Purpose |
|-----------|---------|
| `packages/` | Core framework (agent, workflow, tool, memory, rag, voice, mcp) |
| `server-adapters/` | Hono, Express, Fastify, Koa |
| `stores/` | LibSQL, PostgreSQL, MongoDB, DuckDB, Upstash, composite |
| `deployers/` | Cloud deployer integrations |
| `auth/` | RBAC, sessions, SSO (new) |
| `observability/` | Tracing, logging, metrics |
| `voice/` | 11 TTS + 8 STT providers, OpenAI Realtime |
| `browser/` | Browser automation |
| `integrations/` | Third-party connectors |

### Quick Start
```bash
npm create mastra@latest
npx bgproc start -n <project-name> -w -- npm run dev
# Mastra Studio: http://localhost:4111
```

### Runtime Support
- Node.js v22.13.0+ (v22.18.0+ to run TS files directly)
- Bun
- Deno
- Cloudflare

### Deployment Options
1. **Mastra Server** — Hono-based standalone (`mastra build`)
2. **Monorepo** — Co-deploy with another package
3. **Mastra Platform** — Hosted Observability + Studio + Server
4. **Cloud Providers** — Built-in deployers for Vercel, Netlify, Cloudflare
5. **Web Framework Integration** — Next.js, Astro

## Feature Matrix

| Layer | Capability |
|-------|-----------|
| **Model Routing** | 40+ providers, 3000+ models via `'provider/model'` string |
| **Agents** | Open-ended task solver; tool use; iteration loop; subagent delegation |
| **Workflows** | Graph-based composition: `.then()`, `.parallel()`, `.branch()`, `.map()` |
| **Human-in-the-loop** | Suspend/resume workflows indefinitely via storage |
| **Tools** | `createTool()` with Zod/Valibot/ArkType; agents and workflows as tools |
| **MCP** | Client + Server classes; static and dynamic tool loading |
| **Memory** | Message history, working memory, semantic recall, observational memory |
| **RAG** | `MDocument` with chunking strategies; 4+ vector stores |
| **Voice** | 11 TTS + 8 STT providers; OpenAI Realtime STS |
| **Observability** | OpenTelemetry traces, auto-derived metrics, correlated logs |
| **Auth** | RBAC, sessions, SSO, credentials, ACL (new) |

## Recent Development Highlights

- **TypeScript 6.0.3 Upgrade** — preparation for Go-based TS 7
- **Tailwind v4 Migration** — Playground UI
- **Consolidated AI Assistant Commands** — `.mastracode/commands/` with symlinks
- **Auth & RBAC** — New `@mastra/core/auth` export
- **Observational Memory** (`@mastra/memory@1.1.0`) — Observer + Reflector background agents
- **Supervisor Agents** (`@mastra/core@1.8.0`) — Subagent delegation with `onDelegationStart`/`onDelegationComplete` hooks

## Status

- Active development, monthly releases
- Production-grade (Apache 2.0 core, large contributor base, hosted platform available)
- Backed by Y Combinator (the "modern TypeScript stack" pitch is a developer-ecosystem wedge)

## Related Concepts

- [[graph-based-workflow-engine]] — Mastra's `.then`/`.parallel`/`.branch` pattern
- [[observational-memory-pattern]] — Three-tier message compression
- [[supervisor-agent-pattern]] — Subagent delegation with hooks
- [[typed-tool-creation]] — Why `createTool()` is mandatory
- [[bundled-model-router]] — Single-string `'provider/model'` gateway
- [[multi-agent-orchestration-patterns]] — Comparison with LangGraph, CrewAI
- [[agent-composition-tree-mastra]] — Mastra's layered slot-based composition model
- [[capability-first-tool-design]] — Tool descriptions and schema as agent guidance

## References

- Raw Article: [[Raw/github-mastra-ai-framework-2026-07-03]]
- GitHub: https://github.com/mastra-ai/mastra
- Docs: https://mastra.ai/docs
- Comparison: https://www.developersdigest.tech/guides/ai-agent-frameworks-compared
