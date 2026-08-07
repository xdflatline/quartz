---
title: "Session Event Durability Levels"

details: "AgentOS events are a flat discriminated union with a `durability: 'ephemeral' | 'durable'` field. Ephemeral events (live agent-message or thought deltas) are not sequenced or stored. Durable events (completed/coalesced message chunks, permission request/response records) have a session sequence and are emitted only after their SQLite transaction commits. Consumers deduplicate live durable delivery by `(sessionId, sequence)`. This dual-layer model lets agents stream live deltas to UIs while keeping replayable history in SQLite."
tags:
  - concepts
  - runtime
created: 2026-07-19
updated: 2026-07-19
type: concept
source: "[[Raw/agentos-sdk-dev-docs-2026-07-19]]"
---

# Session Event Durability Levels

**Source:** Documentation bundle ([[Raw/agentos-sdk-dev-docs-2026-07-19]])
**Category:** Architecture Pattern / Technical Reference
**Status:** Production-validated

## Overview

AgentOS events are a flat discriminated union with a `durability` field. Two levels: `ephemeral` (live deltas, not persisted) and `durable` (sequenced, committed to SQLite before emission). The model lets agents stream live deltas to UIs while keeping replayable history in SQLite.

## Core Content

### The Flat Discriminated Union

`sessionEvent` is a flat discriminated union. The top-level `type` is the native ACP `SessionUpdate.sessionUpdate` value, with ACP payload fields (`content`, `toolCallId`, `entries`, etc.) sitting directly beside the durability envelope. There is **no nested `update` wrapper**.

### Two Durability Levels

| Level | Behavior |
|-------|----------|
| `durability: "ephemeral"` | Live agent-message or thought delta. **Not sequenced or stored.** |
| `durability: "durable"` | Has a session sequence. Emitted **only after** its SQLite transaction commits. Completed/coalesced message chunks are durable. |

Permission request/response lifecycle variants use the same flat shape with top-level `options`, `toolCall`, or `outcome` fields.

### Subscription Pattern

```typescript
const conn = agent.connect();

// Subscribe before sending the prompt
conn.on("sessionEvent", (event) => {
  console.log(`[${event.sessionId}]`, event.durability, event);
});

await agent.openSession({ ... });
await agent.prompt({ content: [{ type: "text", text: "..." }] });
```

For Core (no actor): `vm.onSessionEvent((event) => { ... })` — register before prompting to receive live deltas.

### History Reading

`readHistory({ sessionId, before, after, limit })`:
- Reads **only SQLite** and never starts an adapter
- `before` and `after` are **exclusive and mutually exclusive**
- Consumers deduplicate live durable delivery by `(sessionId, sequence)`

### Critical Behaviors

- **Delivery guarantees:** AgentOS commits the complete user message before dispatching and **never automatically replays** a prompt whose delivery may have reached the adapter
- **Idempotency:** Use an `idempotencyKey` when the caller may retry. Reusing a key with different content fails. If the first call is still active, the retry waits behind that turn and receives its committed result
- **Concurrent prompt serialization:** AgentOS automatically serializes concurrent prompts targeting the same session — no application queue needed
- **Bounded by VM limits:** `limits.acp.maxPromptBytes`, `limits.acp.maxPromptBlocks`, and history byte/event budgets. An oversized batch is rejected before it changes history

### Limits (Bounded by VM Configuration)

- `limits.acp.maxPromptBytes`
- `limits.acp.maxPromptBlocks`
- History byte budget
- History event budget
- `limits.acp.maxFallbackContinuationBytes` (for session restoration)

Limit errors name the exact field to raise. A durable update batch must also fit the configured history byte and event budgets; an oversized batch is rejected before it changes history.

## Key Insights

1. **Flat shape, not nested** — top-level fields, no `update` wrapper, so consumers don't have to unwrap
2. **Durability tells you what survives sleep** — ephemeral deltas vanish, durable records persist
3. **Sequence-based dedup** is the contract — consumers must dedup by `(sessionId, sequence)` to handle re-delivery
4. **Idempotency key** solves the "did my prompt actually reach the adapter?" problem — AgentOS never auto-replays
5. **Auto-serialization of concurrent prompts** removes the need for an application queue for same-session calls
6. **Bounded by VM config** is the design choice — limits are predictable and documented, not "best effort"

## Related Concepts

- [[Concepts/durable-actor-session-sleep]] — what survives vs. is lost across sleep
- [[Concepts/in-process-vm-agent-runtime-agentos]] — the runtime hosting the events

## Related Entities

- [[Entities/agentos]] — the canonical implementation

## References

- Raw Documentation: [[Raw/agentos-sdk-dev-docs-2026-07-19]]
- Sessions docs: https://agentos-sdk.dev/docs/sessions
- ACP spec: https://agentclientprotocol.com/
