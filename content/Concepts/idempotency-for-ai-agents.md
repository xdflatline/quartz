---
title: Idempotency for AI Agents
detail: Applying idempotency keys to write-capable AI agents so that retries and network failures produce exactly one real-world side effect per logical intent.
details: Applying idempotency keys to write-capable AI agents so that retries and network failures produce exactly one real-world side effect per logical intent. Borrowed from payments infrastructure (Stripe Idempotency-Key), the pattern wraps side-effecting tool calls in a store keyed on intent content, collapsing duplicate executions into replays. The read/write asymmetry is central -- read retries are free, write retries are double-actions.
tags:
  - concepts
source: https://dev.to/gs_sanjana_3e822112e14f8/your-ai-agent-doesnt-need-to-be-smarter-it-needs-to-be-idempotent-2736
created: 2026-07-01
updated: 2026-07-01
type: concept
sources:
  - Raw/devto-ai-agent-idempotency-2026.md
---

## Overview

Idempotency for AI agents is the practice of wrapping side-effecting tool calls (sending emails, creating records, moving money) in a deduplication boundary keyed on the content of the intended action. When the network fails mid-response and the agent retries, the idempotency store returns the original result instead of executing the action again. The pattern is borrowed directly from payments infrastructure ([[Entities/stripe-idempotency-key|Stripe Idempotency-Key]]).

## Core Principle: Read/Write Asymmetry

The fundamental insight driving the pattern:

- **Read-only agents**: retries are free. Re-fetching data has no side effects.
- **Write-capable agents**: retries are second irreversible actions. A timeout followed by a retry can create two invoices, two charges, two emails.

A smarter model makes this **worse**, not better -- more capable agents are more aggressive about recovering from apparent failures. The intelligence layer and reliability layer are separate problems; you cannot prompt your way out of a network partition.

## Pattern: IdempotentStore

Wrap every side-effecting action in a store that:

1. Derives a deterministic key from the tool name + parameters (intent content)
2. Checks if the key has been seen before
3. If yes: returns the stored result (replay)
4. If no: executes the action, stores the result, returns it

```python
def intent_key(tool_name, params):
    payload = json.dumps({"tool": tool_name, "params": params}, sort_keys=True)
    return hashlib.sha256(payload.encode()).hexdigest()[:16]
```

## Key Design Pitfalls

| Problem | Cause | Result |
|---------|-------|--------|
| False duplicate | Distinct actions hash to same key | Legitimate action silently dropped |
| Missed duplicate | Retries hash to different keys | Double-write passes through |

Common traps: non-deterministic parameters (timestamps, UUIDs generated per-attempt), floating point precision differences, dict ordering variance, timezone handling.

## Production Requirements

- **Persistence**: Redis or Postgres with unique constraint on key (concurrent worker safety)
- **TTL**: Keys expire after ~24 hours (Stripe's window)
- **Replay fidelity**: Store enough of the response to replay faithfully
- **Boundary placement**: Safety guarantee lives at the boundary, not in the model's judgment

## Category

Architecture Constraint

## Status

Production-validated (payments industry, 10+ years)

## Key Insights

1. Most production AI agent failures are infrastructure failures, not reasoning failures
2. The fix predates LLMs -- borrow from payments, not from ML research
3. The agent is allowed to be flaky; the boundary is what makes flakiness safe
4. Key derivation from intent content (not random IDs) is what makes the pattern work for autonomous agents
5. Smarter models exacerbate the problem by retrying more aggressively

## Related Concepts

- [[Concepts/ai-agents|AI Agents]] -- the systems this pattern protects
- [[Concepts/multi-agent-orchestration-patterns|Multi-Agent Orchestration Patterns]] -- orchestration layers that must handle retry semantics
- [[Entities/stripe-idempotency-key|Stripe Idempotency-Key]] -- the origin pattern

## References

- Raw Article: [[Raw/devto-ai-agent-idempotency-2026]]
- Original: https://dev.to/gs_sanjana_3e822112e14f8/your-ai-agent-doesnt-need-to-be-smarter-it-needs-to-be-idempotent-2736
