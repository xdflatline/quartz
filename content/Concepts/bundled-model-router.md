---
title: "Bundled Model Router"
detail: "Gateway pattern where a single 'provider/model' string resolves to one of 3000+ models from 40+ providers via an internal router. The user never imports provider SDKs; environment variables are inferred from the provider name."
details: "A model-access pattern that hides provider SDKs behind a single string identifier ('openai/gpt-5.5', 'anthropic/claude-sonnet-4-6', 'google/gemini-2.5-flash'). The router internally resolves the string to the right provider, infers the API key from environment variables (e.g., 'openai/*' requires OPENAI_API_KEY), and exposes a uniform interface to the agent. Users do not install provider packages (notably no 'ai-sdk' packages). The pattern is what makes a multi-provider framework feel like a single-vendor API."
tags:
  - concepts
created: 2026-07-03
updated: 2026-07-03
type: concept
sources:
  - Raw/github-mastra-ai-framework-2026-07-03.md
---
# Bundled Model Router

**Source:** [[Raw/github-mastra-ai-framework-2026-07-03]]
**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

A model-access pattern that **hides provider SDKs behind a single string identifier** (`'openai/gpt-5.5'`, `'anthropic/claude-sonnet-4-6'`, `'google/gemini-2.5-flash'`). The router internally resolves the string to the right provider, infers the API key from environment variables, and exposes a uniform interface to the agent. Users do **not** install provider packages.

## The Identifier Format

The format is `'provider/model'`, using `/` (not `:`) as the separator. The provider is the routing key, the model is the specific identifier:

| String | Provider | Model |
|--------|----------|-------|
| `'openai/gpt-5.5'` | OpenAI | gpt-5.5 |
| `'openai/gpt-5-mini'` | OpenAI | gpt-5-mini |
| `'anthropic/claude-sonnet-4-6'` | Anthropic | claude-sonnet-4-6 |
| `'anthropic/claude-opus-4-7'` | Anthropic | claude-opus-4-7 |
| `'anthropic/claude-haiku-4-5'` | Anthropic | claude-haiku-4-5 |
| `'google/gemini-2.5-flash'` | Google | gemini-2.5-flash |

40+ providers and 3000+ models are exposed through the same identifier format.

## The No-SDK Rule

Mastra's documentation explicitly warns:

> **Do not** install any `ai-sdk` package unless Mastra's documentation explicitly says otherwise.

The router bundles its own provider integrations. Installing a competing gateway or provider SDK creates version conflicts and dual-billing risks.

## Environment Variable Inference

The router infers the required environment variable from the provider name:

| Provider | Required Env Var |
|----------|-----------------|
| OpenAI | `OPENAI_API_KEY` |
| Anthropic | `ANTHROPIC_API_KEY` |
| Google | `GOOGLE_API_KEY` |

This is automatic — no configuration object is needed. The same `Agent({ model: 'openai/gpt-5.5' })` works locally with `OPENAI_API_KEY` set and in production with the same variable configured.

## Embedding Models

The router extends to embeddings via `ModelRouterEmbeddingModel`:

```ts
import { ModelRouterEmbeddingModel } from '@mastra/core/llm'

const { embeddings } = await embedMany({
  values: chunks.map(c => c.text),
  model: new ModelRouterEmbeddingModel('openai/text-embedding-3-small'),
})
```

The same `'provider/model'` string identifies the embedding model.

## Why This Pattern Works

### Provider Portability
Switch from OpenAI to Anthropic by changing one string. The agent code, the tool definitions, and the observability stay the same.

### Single Configuration Surface
Authentication is environment-driven. No `LLMProviderConfig` object, no per-provider constructor — just the API key in `.env`.

### Vendor Bundling
The router's bundled providers are version-tested together. Upgrading the framework upgrades the providers in lockstep, removing the "works on my machine" failure mode that plagues AI apps using multiple SDKs.

### Hidden Cost Surface
Because the router is the single chokepoint, observability (token usage, cost estimation) is collected once and reported uniformly across all providers.

## Key Insights

1. **A string is the API** — the identifier is the only thing the developer types, which is the smallest possible coupling.
2. **Environment-driven config is the right default** — no per-instance provider setup, just `.env` files.
3. **The no-SDK rule is non-negotiable** — installing parallel gateways creates silent double-billing and version drift.
4. **Embeddings share the same router** — one mental model for both generation and embedding.
5. **The router is the observability chokepoint** — uniform token/cost reporting across vendors is a side-effect of having one gateway.

## Related Concepts

- [[agent-composition-tree-mastra]] — Where the router fits in the agent stack
- [[observational-memory-pattern]] — Example: OM defaults to a router-resolved model (`google/gemini-2.5-flash`)
- [[Entities/mastra]] — Canonical implementation

## References

- Raw Article: [[Raw/github-mastra-ai-framework-2026-07-03]]
- Original: https://mastra.ai/docs
