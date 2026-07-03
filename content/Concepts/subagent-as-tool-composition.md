---
title: "Subagent-as-Tool Composition"
detail: "Composition pattern where agents, workflows, and MCP servers are uniformly exposed to a parent agent as tools (named 'agent-<key>', 'workflow-<key>'), enabling recursive nesting — an agent can call agents that call agents."
details: "A composition pattern that unifies subagents, workflows, and MCP-loaded tools under the same tool representation. A parent agent's 'tools' slot accepts three kinds: createTool-built primitives, agents (auto-converted to 'agent-<key>'), and workflows (auto-converted to 'workflow-<key>'). The parent LLM sees a flat tool list and decides what to call. The pattern enables hierarchical agent systems (supervisor-of-supervisors) and clean reuse (a research workflow is callable from any agent that needs it)."
tags:
  - concepts
created: 2026-07-03
updated: 2026-07-03
type: concept
sources:
  - Raw/github-mastra-ai-framework-2026-07-03.md
---
# Subagent-as-Tool Composition

**Source:** [[Raw/github-mastra-ai-framework-2026-07-03]]
**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

A composition pattern that **unifies subagents, workflows, and MCP-loaded tools** under the same tool representation. A parent agent's `tools` slot accepts three kinds: `createTool`-built primitives, agents (auto-converted to `agent-<key>`), and workflows (auto-converted to `workflow-<key>`). The parent LLM sees a flat tool list and decides what to call.

## The Three Tool Kinds

| Kind | Configuration Key | Auto-generated Tool Name |
|------|-------------------|---------------------------|
| `createTool` primitive | `tools: { weatherTool }` | `weatherTool` (or as given) |
| Subagent | `agents: { writer }` | `agent-writer` |
| Workflow | `workflows: { researchWorkflow }` | `workflow-researchWorkflow` |

```ts
export const supervisor = new Agent({
  id: 'supervisor',
  model: 'openai/gpt-5.5',
  agents: { writer },                          // → tool 'agent-writer'
  workflows: { researchWorkflow },             // → tool 'workflow-researchWorkflow'
  tools: { weatherTool },                      // → tool 'weatherTool'
})
```

The parent LLM sees `agent-writer`, `workflow-researchWorkflow`, and `weatherTool` as three callable tools. It picks based on the user message, instructions, and each tool's description.

## Recursive Nesting

Because subagents are themselves agents, they can have their own subagents:

```
supervisor (top-level)
  ├── tools: { weatherTool }
  ├── agents: { writer }
  │     ├── tools: { spellCheckTool }
  │     └── agents: { editor }
  │           └── tools: { grammarTool }
  └── workflows: { publishWorkflow }
```

Hierarchical agent systems (supervisor-of-supervisors) emerge naturally. Each level's LLM sees its own flat tool list.

## The Description Field Becomes a Routing Protocol

For subagents and workflows, the `description` field is **read by the parent LLM to decide delegation**:

- For a subagent: "Drafts and edits written content"
- For a workflow: its `description` (set on `createWorkflow`)
- For a tool: its `description` (set on `createTool`)

The parent LLM routes on these descriptions exactly the way it routes on tool descriptions. This is why good descriptions are a non-obvious lever for multi-agent systems — see [[supervisor-agent-pattern]].

## Workflows as Tools Use Their Schemas

When a workflow is exposed as a tool, its `inputSchema` and `outputSchema` become the tool's parameter and return types. The parent agent sees the same Zod-style schema it would see for a regular tool.

```ts
export const researchWorkflow = createWorkflow({
  id: 'research',
  inputSchema: z.object({ topic: z.string() }),
  outputSchema: z.object({ summary: z.string() }),
  description: 'Research a topic and return a 3-paragraph summary',
})
  .then(researchStep)
  .commit()
```

The parent agent invokes `workflow-research` with `{ topic: '...' }` and receives `{ summary: '...' }`.

## MCP Tools Follow the Same Pattern

`MCPClient.listTools()` returns a tool map that can be passed directly to the agent's `tools` slot:

```ts
const agent = new Agent({
  id: 'test-agent',
  model: 'openai/gpt-5.5',
  tools: await testMcpClient.listTools(),
})
```

External MCP servers become first-class tools in the parent's flat tool list.

## Why This Pattern Works

### Uniform Mental Model
The parent agent doesn't distinguish "primitive tool" from "subagent" from "workflow" — they're all tools. One reasoning loop, one tool-call format.

### Reuse Without Coupling
A research workflow is callable from any agent that needs it, no import gymnastics. The same workflow is also runnable standalone (`mastra.workflows.researchWorkflow.execute(...)`).

### Hierarchical Composition Without New Abstractions
Supervisor-of-supervisors requires no new framework feature — just stack agents with subagents.

### Tool-First Means Audit-First
Because everything is a tool, observability (traces, token counts, latencies) is uniform across the call tree.

## Key Insights

1. **Subagents are tools, not a special primitive** — this is the move that makes hierarchical composition free.
2. **The description field is the routing protocol** — treat it as a load-bearing API contract, not a comment.
3. **Schemas flow through the composition** — a workflow's `inputSchema` is the parent's tool-call argument schema.
4. **MCP fits the same shape** — `listTools()` output drops into the `tools` slot, no adapter.
5. **The flat tool list is the agent's world model** — every level of recursion reduces to a single LLM choosing from a flat list.

## Related Concepts

- [[supervisor-agent-pattern]] — The pattern that uses subagent-as-tool composition
- [[graph-based-workflow-engine]] — Workflows that get exposed as tools
- [[typed-tool-creation]] — The primitive tool counterpart
- [[agent-composition-tree-mastra]] — How all three slots fit together
- [[Entities/mastra]] — Canonical implementation

## References

- Raw Article: [[Raw/github-mastra-ai-framework-2026-07-03]]
- Original: https://mastra.ai/docs/tools-mcp/overview
