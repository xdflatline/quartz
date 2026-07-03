---
title: "Observational Memory Pattern"
detail: "Three-tier long-context memory (recent messages + observations + reflections) where two background agents (Observer, Reflector) compress old messages into dense observations, achieving 5-40x context compression while keeping the prompt prefix cacheable."
details: "A memory architecture for long-running agent conversations. Replaces raw message history with a dense observation log maintained by two background agents: an Observer that writes observations when recent message tokens exceed a threshold (default 30k), and a Reflector that condenses observations when observation tokens exceed a threshold (default 40k). The agent sees: (1) recent messages exact, (2) observations (concise notes), (3) reflections (condensed observations). Yields 5-40x compression, zero context rot, and a stable append-only prompt prefix that keeps prompt caches warm."
tags:
  - concepts
created: 2026-07-03
updated: 2026-07-03
type: concept
sources:
  - Raw/github-mastra-ai-framework-2026-07-03.md
---
# Observational Memory Pattern

**Source:** [[Raw/github-mastra-ai-framework-2026-07-03]]
**Category:** Architecture Pattern
**Status:** Production-validated (shipped in Mastra `@mastra/memory@1.1.0`)

## Overview

A long-context memory architecture where **two background agents** (an Observer and a Reflector) compress a growing conversation into a dense observation log, replacing raw message history with three tiers: **recent messages** (exact), **observations** (concise notes), and **reflections** (condensed observations). The result is **5–40× context compression** with a stable, append-only prompt prefix that keeps prompt caches warm.

## The Problem

Agent conversations grow. Naive approaches carry the full message history plus tool results until the context window fills. Three consequences:

1. **Context rot** — performance degrades as the window fills with noise
2. **Context waste** — most historical tokens are irrelevant to the current turn
3. **Cache invalidation** — new tokens break prompt prefix caches, multiplying cost

## The Three-Tier Cache

```
+--------------------------------+
|  Tier 1: Recent messages       |  exact, in-order
+--------------------------------+
|  Tier 2: Observations          |  written by Observer
|  (trigger: messageTokens > N)  |
+--------------------------------+
|  Tier 3: Reflections           |  written by Reflector
|  (trigger: observationTokens > M) |
+--------------------------------+
```

### Tier 1 — Recent Messages
Exact conversation history for the current task. Includes user messages, agent replies, and tool results. Only the most recent N tokens (default 30,000) sit at this tier; older content is promoted down.

### Tier 2 — Observations
Concise notes written by the **Observer** background agent when message-token count exceeds the threshold. Observations track the current task and a suggested response, allowing the agent to resume smoothly.

The Observer sees readable placeholders like `[Image #1: reference-board.png]` and forwards actual attachment parts alongside text. Image-like `file` parts are upgraded to image inputs when possible.

### Tier 3 — Reflections
Condensed observations written by the **Reflector** background agent when observation tokens exceed their threshold. Reflections combine related items and reflect on patterns across the observation log.

## Triggers and Thresholds

| Phase | Trigger | Default |
|-------|---------|---------|
| **Observation** | `messageTokens` | 30,000 |
| **Reflection** | `observationTokens` | 40,000 |

**Early activation** — force buffering before the threshold is reached:
- `activateAfterIdle` — `'auto'`, `'5m'`, `'10m'`, or `false`
- `activateOnProviderChange` — when switching model providers
- `bufferOnIdle` — observe short turns immediately on agent idle (default off; separate from `bufferTokens`)

**Temporal gap markers** — insert a reminder before a new user message when ≥10 minutes have elapsed since the last turn. Off by default; useful for UIs to recognize resumed conversations.

## Why It Works

### Prompt Caching Wins
The OM context (observations + reflections + system prompt) is **stable and appends over time**. The prompt prefix stays cacheable, dramatically reducing per-turn cost in production.

### Compression
Raw message history and tool results compress into a dense observation log — typically **5–40×** compression. Smaller context means faster responses and longer coherent conversations.

### Zero Context Rot
The agent sees relevant information instead of noisy tool calls and irrelevant tokens. The Observer selectively preserves what matters, the Reflector condenses patterns.

## Implementation Reference (Mastra)

```ts
import { Memory } from '@mastra/memory'
import { Agent } from '@mastra/core/agent'

export const agent = new Agent({
  id: 'my-agent',
  model: 'openai/gpt-5-mini',
  memory: new Memory({
    options: {
      observationalMemory: {
        model: 'google/gemini-2.5-flash',  // default OM model
        temporalMarkers: true,
        activateAfterIdle: 'auto',
        activateOnProviderChange: true,
      },
    },
  }),
})
```

### Storage
OM currently supports only three backends: `@mastra/pg`, `@mastra/libsql`, `@mastra/mongodb`.

### Client-Side Warning
When using OM with a client app, send **only the new message** from the client — not the full conversation history. Sending full history is redundant and can cause timestamp-based message ordering bugs.

## Key Insights

1. **Background agents are a memory primitive** — not just a generation primitive. The Observer/Reflector are full LLMs running async, compressing on their own clock.
2. **Stable prefix = cacheable prefix** — the OM context grows by append, so the cache hit rate is high.
3. **Compression ratios (5–40×) come from semantic summarization** — keyword summarization or fixed-window truncation cannot match Observer/Reflector quality.
4. **The three tiers map to memory theory** — recent = sensory, observations = working, reflections = long-term / episodic.
5. **Thresholds are not free** — every observation/reflection costs an LLM call; choose thresholds based on the model's prompt-cache TTL and the user's idle behavior.

## Related Concepts

- [[agent-memory-layer-patterns]] — Broader memory pattern landscape
- [[hindsight-memory-architecture]] — Alternative memory architecture
- [[agent-composition-tree-mastra]] — Where memory slots into the agent stack
- [[Entities/mastra]] — Canonical implementation

## References

- Raw Article: [[Raw/github-mastra-ai-framework-2026-07-03]]
- Original: https://mastra.ai/docs/memory/observational-memory
