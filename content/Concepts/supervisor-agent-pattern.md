---
title: "Supervisor Agent Pattern"

details: "A multi-agent coordination pattern where a single supervisor agent owns the orchestration loop and treats specialized subagents as tools. Subagents are configured on the supervisor's 'agents' property and exposed as tools named 'agent-<key>'. The supervisor decides when to delegate using its own instructions plus each subagent's description. Two delegation hooks enable runtime control: onDelegationStart (proceed/reject, modify prompt, cap max steps) and onDelegationComplete (inject feedback, bail out). By default, subagents see a fresh thread per delegation but a stable resource ID derived from the parent."
tags:
  - concepts
created: 2026-07-03
updated: 2026-07-03
type: concept
sources:
  - Raw/github-mastra-ai-framework-2026-07-03.md
---
# Supervisor Agent Pattern

**Source:** [[Raw/github-mastra-ai-framework-2026-07-03]]
**Category:** Architecture Pattern
**Status:** Production-validated (shipped in Mastra `@mastra/core@1.8.0`)

## Overview

A multi-agent coordination pattern where a **single supervisor agent owns the orchestration loop** and treats specialized subagents as tools. The supervisor decides when to delegate using its own instructions plus each subagent's `description`, and exposes two runtime hooks — `onDelegationStart` and `onDelegationComplete` — to intercept, modify, or reject delegations and inject feedback into its own memory.

## Core Mechanics

### Subagent-as-Tool
Subagents configured on the supervisor's `agents` property are **converted to tools** named `agent-<key>`. The supervisor's LLM sees these as ordinary tool definitions and decides when to call them. The same mechanism applies to workflows (`workflow-<key>`).

```ts
const researchAgent = new Agent({
  id: 'research-agent',
  description: 'Gathers factual information and returns bullet-point summaries.',
  model: 'openai/gpt-5-mini',
})

const supervisor = new Agent({
  id: 'supervisor',
  instructions: `Delegate to research-agent for facts, then writing-agent for content.`,
  model: 'openai/gpt-5.5',
  agents: { researchAgent, writingAgent },
})
```

### The `description` Field Is the Delegation Contract
A subagent's `description` is what the supervisor reads to decide *when* to delegate. Vague descriptions lead to misrouted or unrouted tasks. This is a non-obvious lever — invest in descriptions like you invest in tool descriptions.

## Delegation Hooks

### `onDelegationStart`
Called before delegating to a subagent. Return an object to control behavior:

| Return Key | Effect |
|---|---|
| `proceed: true` | Allow delegation (default) |
| `proceed: false` | Reject with a `rejectionReason` |
| `modifiedPrompt` | Rewrite the prompt sent to the subagent |
| `modifiedMaxSteps` | Cap the subagent's iteration count |

**Context:** `primitiveId`, `prompt`, `iteration`

```ts
delegation: {
  onDelegationStart: async context => {
    if (context.iteration > 8) {
      return { proceed: false, rejectionReason: 'Max iterations — synthesize now.' }
    }
    return { proceed: true, modifiedPrompt: `${context.prompt}\n\nFocus on 2024-2025.` }
  },
}
```

### `onDelegationComplete`
Called after a delegation finishes. Return `{ feedback: '...' }` to inject into the supervisor's memory for subsequent iterations. Call `context.bail()` to stop the supervisor loop immediately.

```ts
delegation: {
  onDelegationComplete: async context => {
    if (context.error) {
      context.bail()
      return { feedback: `Delegation to ${context.primitiveId} failed.` }
    }
  },
}
```

## Memory Isolation in Subagent Delegation

When a supervisor delegates, Mastra automatically isolates subagent memory:

| Aspect | Behavior |
|--------|----------|
| **Thread ID** | Fresh unique ID per delegation. Subagent starts with a clean history every time. |
| **Resource ID** | Deterministic: `{parentResourceId}-{agentName}`. Stable across delegations, so **resource-scoped memory persists** between calls by the same user. |
| **Memory Instance** | If subagent has no memory configured, it inherits the supervisor's `Memory` instance. |

This is the **default isolation model**: subagents get a clean slate per delegation, but the supervisor's view of "this user" is consistent.

## Message Filtering

By default, subagents receive the **full conversation context**. Use `messageFilter` to limit or sanitize what is shared:

```ts
messageFilter: ({ messages, primitiveId, prompt }) => {
  return messages
    .filter(msg => !JSON.stringify(msg.content).includes('confidential'))
    .slice(-10)  // last 10 only
}
```

## Subagent Result Context

By default, **only the subagent's text response** is added to the supervisor model context in later iterations. Nested tool calls and subagent metadata (thread/resource IDs) are excluded — keeping the supervisor's context lean.

To include nested tool results:
```ts
includeSubAgentToolResultsInModelContext: true
```

## When to Use Supervisor vs. Workflow

| Need | Use |
|------|-----|
| Multi-step, fixed graph | **Workflow** — `.then` / `.parallel` / `.branch` |
| Open-ended, expertise per step, dynamic delegation | **Supervisor agent** — LLM decides who runs |
| Mixed (workflow that calls an agent, agent that calls a workflow) | **Both** — workflows and agents are interoperable tools in Mastra |

## Key Insights

1. **Description is a routing protocol** — subagent descriptions are read by another LLM to decide delegation, not by humans. Treat them as load-bearing API contracts.
2. **Hooks turn delegation into observable, controllable flow** — `onDelegationStart` is a guardrail; `onDelegationComplete` is a feedback channel.
3. **Resource-stable, thread-fresh is the right default** — subagents get a clean slate per task, but the user identity is preserved across delegations.
4. **The subagent-as-tool composition is recursive** — a subagent can itself have subagents, building a hierarchy of supervisors.
5. **The supervisor pattern complements the workflow engine** — workflows for fixed graphs, supervisors for open-ended expertise routing. They share the same tool representation.

## Related Concepts

- [[multi-agent-orchestration-patterns]] — Broader multi-agent landscape (HN, LangGraph, CrewAI)
- [[graph-based-workflow-engine]] — The fixed-graph counterpart
- [[subagent-as-tool-composition]] — How subagents become tools (lower-level mechanism)
- [[agent-composition-tree-mastra]] — Where the supervisor slots into the agent stack
- [[Entities/mastra]] — Canonical implementation

## References

- Raw Article: [[Raw/github-mastra-ai-framework-2026-07-03]]
- Original: https://mastra.ai/docs/agents/supervisor-agents
