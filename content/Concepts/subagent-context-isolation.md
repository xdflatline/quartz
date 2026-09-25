---
title: "Subagent Context Isolation"
details: "Architecture pattern where a subtask (order lookup, document retrieval, research facet) runs in a separate LLM agent with its own clean conversation history, returning only a compact summary (50–100 tokens) to the main agent instead of dumping the full tool result into shared context. The main mechanism by which multi-agent systems protect context from pollution."
tags:
  - concept
  - multi-agent
  - orchestration
  - context-engineering
source: "[[Raw/claude-building-multi-agent-systems-2026-01-23]]"
created: "2026-09-25"
updated: "2026-09-25"
type: concept
---

# Subagent Context Isolation

**Source:** [[Raw/claude-building-multi-agent-systems-2026-01-23]] — Anthropic Claude blog, "Building multi-agent systems: When and how to use them" (Jan 23, 2026)
**Category:** Architecture Pattern
**Status:** Production-validated (Anthropic engineering recommendation)

---

## Overview

A subagent runs a subtask in a **separate conversation history**, returning only a compact summary to the caller. The main agent's context stays clean because the heavy tool output (order history, full document, raw search results) is consumed inside the subagent's own context window and never enters the main conversation. This is the canonical implementation of Anthropic's "context protection" benefit of multi-agent systems.

## When it works

The pattern is most effective when **all three** conditions hold:

- Subtasks generate high context volume (>1000 tokens) but most of that information is irrelevant to the main task
- The subtask is well-defined with clear criteria for what information to extract
- It's a lookup or retrieval operation that requires filtering before use

## Canonical shape (Anthropic example)

```python
class OrderLookupAgent:
    def lookup_order(self, order_id: str) -> dict:
        # Separate agent with its own context
        messages = [{"role": "user", "content": f"Get essential details for order {order_id}"}]
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=messages,
            tools=[get_order_details_tool]
        )
        return extract_summary(response)  # ~50-100 tokens back

class SupportAgent:
    def handle_issue(self, user_message: str):
        if needs_order_info(user_message):
            order_summary = OrderLookupAgent().lookup_order(extract_order_id(user_message))
            context = f"Order {order_id}: {order_summary['status']}, purchased {order_summary['date']}"
        messages = [{"role": "user", "content": f"{context}\n\nUser issue: {user_message}"}]
        return client.messages.create(model="claude-sonnet-4-5", max_tokens=2048, messages=messages)
```

The `OrderLookupAgent` consumes 2000+ tokens of order history; only the 50–100 token summary enters the `SupportAgent` context.

## Alternatives to consider first

Context isolation via subagents is not free — **3–10x more tokens** than a single-agent approach for equivalent tasks (each agent has its own context, plus coordination messages, plus summary-stitching). Before reaching for subagents:

- **Try better prompting first.** Anthropic reports teams that built elaborate multi-agent architectures only to discover that improved prompting on a single agent achieved equivalent results.
- **Try compaction / context management.** Recent advances like Anthropic's [compaction](https://platform.claude.com/cookbook/tool-use-automatic-context-compaction) let a single agent maintain effective memory across longer horizons.
- **Try a subagent only for the high-volume subtask.** Don't split a workflow into 4–5 agents — split off the one subtask whose context volume is the actual bottleneck.

## Distinction from related patterns

- **[[Concepts/parallel-subagent-process-manager]]** — runs multiple subagents *concurrently* for parallel coverage; isolation is a side effect.
- **[[Concepts/subagent-as-tool-composition]]** — composes subagents as callable tools (Mastra, Anthropic SDK tool-use); isolation is again a side effect.
- **[[Concepts/working-memory-preservation-subagent-purpose]]** — keeps the main agent's purpose-anchored memory stable while delegating bulk work; isolation is the mechanism, working-memory preservation is the goal.

The defining feature of this pattern is **deliberate context segregation as the primary design goal**, not as a side effect of parallelism or tool composition.

## Key insights

1. **Context isolation is the most common legitimate reason to use multi-agent.** It is more often worth the overhead than parallelization or specialization, because the cost of context pollution is paid on every single turn rather than just at task boundaries.
2. **The summary API is the contract.** A bad summary returns too much (pollutes the caller's context) or too little (caller can't reason about the result). Treat `extract_summary()` as a critical API surface.
3. **Isolation ≠ independence.** A lookup subagent still consumes tokens for its own context window — you're paying the isolation tax in a different agent's budget.

## Related Concepts

- [[Concepts/context-centric-decomposition]] — when to split work between agents (this pattern is the unit being split)
- [[Concepts/verification-subagent-pattern]] — another reason for subagent isolation: blackbox verification needs zero implementation context
- [[Concepts/multi-agent-decision-framework]] — the parent decision rule for when multi-agent is worth it

## References

- Raw article: [[Raw/claude-building-multi-agent-systems-2026-01-23]]
- Original: <https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them>