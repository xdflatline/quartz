---
title: "Durable Actor Session Sleep"

details: "AgentOS actors sleep after a configurable idle timeout (default 30s), preserving `/home/agentos` filesystem, durable session catalog, and completed session history across the sleep. A later client call wakes a fresh VM over the same actor SQLite database. Adapter processes, running commands, shells, live subscriptions, and in-progress ACP deltas do not survive — they are restored lazily on the next prompt. A three-tier fallback (native ACP session/resume → session/load → fresh session with bounded continuation context) handles agent-specific resume semantics."
tags:
  - concepts
  - runtime
created: 2026-07-19
updated: 2026-07-19
type: concept
source: "[[Raw/agentos-sdk-dev-docs-2026-07-19]]"
---

# Durable Actor Session Sleep

**Source:** Documentation bundle ([[Raw/agentos-sdk-dev-docs-2026-07-19]])
**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

Rivet's sleep/wake model for AgentOS actors: after an idle timeout, the VM shuts down, but filesystem, session catalog, and completed history are persisted to SQLite-over-UDS. The next prompt transparently wakes a fresh VM over the same database. Idle agents consume near-zero resources, and the next interaction is seamless.

## Core Content

### What Persists Across Sleep

| Data | Storage | Persists? |
|------|---------|-----------|
| Files in `/home/agentos` | Actor SQLite over UDS | **Yes** |
| Preview URL tokens | Actor SQLite | **Yes** |
| Session catalog and configuration | Actor SQLite over UDS | **Yes** |
| Completed ACP session history | Actor SQLite over UDS | **Yes** |
| Live ACP adapter process | VM memory | **No** — restored lazily |
| In-progress message deltas | Live event stream | **No** |
| Cron job definitions | VM memory | **No** |
| Running processes / active shells | VM kernel | **No** |
| In-memory mounts | VM memory | **No** |

The native sidecar reads/writes filesystem chunks directly through the actor's authenticated SQLite Unix socket. File contents never pass through the TypeScript or JavaScript actor layer. VM creation supplies one SQLite descriptor shared by filesystem metadata, filesystem blocks, and core session persistence.

### Idle Flow

```
Actor becomes idle -> idle timeout -> actor sleeps and the VM shuts down

listSessions/readHistory -> actor wakes -> VM boots -> SQLite is read without starting an adapter

prompt -> actor wakes -> VM boots -> adapter is restored lazily -> turn runs
```

### Timing & Configuration

- **Default idle sleep timeout:** 30 seconds
- **Graceful shutdown budget:** 15 minutes
- **Action timeout:** 2,147,483,647 ms (~24.8 days) — prevents human permission review from being cut off
- All configurable via the actor's `options` configuration

An active prompt turn uses RivetKit's keep-awake scope through the terminal SQLite commit. An idle durable session does not keep the actor awake.

### Session Restoration (Three-Tier Fallback)

After VM sleep, the next `prompt` transparently starts the adapter:

1. **Preferred:** Native ACP `session/resume`
2. **Fallback:** Stable `session/load`
3. **Final fallback:** Fresh private ACP session with bounded continuation context from AgentOS history

Adapter replay emitted during load is suppressed because SQLite is the sole history source of truth. Fallback transcript is bounded by `limits.acp.maxFallbackContinuationBytes`.

### SQLite-Only Reads (no adapter spin-up)

- `getSession`
- `listSessions`
- `readHistory`
- `getSessionConfig`
- `getSessionCapabilities`
- `getSessionAgentInfo`

`readHistory({ sessionId, before, after, limit })` reads only SQLite; `before` and `after` are exclusive and mutually exclusive. Consumers deduplicate live durable delivery by `(sessionId, sequence)`.

### VM Lifecycle Events

```typescript
const conn = client.vm.getOrCreate("my-agent").connect();

conn.on("vmBooted", () => {
  console.log("VM is ready");
});

conn.on("vmShutdown", (payload) => {
  console.log("VM shutdown reason:", payload.reason);
  // reason: "sleep" | "destroy" | "error"
});
```

These are hosting events, intentionally absent from Core.

## Key Insights

1. **SQLite over UDS** is the durable substrate — not a separate database for filesystem, blocks, and sessions, but one shared descriptor
2. **Sleep is the default** — idle agents consume near-zero resources
3. **Three-tier resume** handles agents with different ACP support levels without code changes
4. **Adapter replay suppression** is critical — if not suppressed, the load process would duplicate the SQLite history in the event stream
5. **Action timeout of 24.8 days** solves a real problem: human-in-the-loop permission review cannot be cut off by the prior 15-minute bound

## Related Concepts

- [[Concepts/in-process-vm-agent-runtime-agentos]] — the runtime that hosts sleep/wake
- [[Concepts/kernel-syscall-isolation-vm]] — isolation preserved across wake
- [[Concepts/session-event-durability-levels]] — what survives vs. what is lost
- [[Concepts/rivet-actor-deployment-kubernetes]] — K8s-specific shutdown config (`terminationGracePeriodSeconds: 2100`)

## Related Entities

- [[Entities/agentos]] — the canonical implementation
- [[Entities/rivet]] — the actor runtime that implements sleep/wake

## References

- Raw Documentation: [[Raw/agentos-sdk-dev-docs-2026-07-19]]
- Persistence docs: https://agentos-sdk.dev/docs/persistence
- Sessions docs: https://agentos-sdk.dev/docs/sessions
