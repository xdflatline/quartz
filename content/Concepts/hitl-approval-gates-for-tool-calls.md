---
title: "HITL Approval Gates for Tool Calls"

details: "Human-in-the-loop approval gates intercept sensitive tool calls before execution, returning a blocked-action result to the worker if denied. AURA (mezmo/aura) implements this as [hitl] with tool-name globs and a [hitl.route] choosing between webhook and conversational modes. Approval lifecycle SSE events are emitted regardless of AURA_CUSTOM_EVENTS; conversational mode also emits aura.approval_pending and requires stream=true plus an Aura-aware client. Cross-pod resolution works in Redis session-store mode."
tags:
  - concepts
created: 2026-07-25
updated: 2026-07-25
type: concept
source: https://github.com/mezmo/aura
---

# HITL Approval Gates for Tool Calls

**Source:** [[Raw/github-mezmo-aura-readme-2026-07-25]]
**Category:** Architecture Pattern
**Status:** Production-validated (AURA, plus broader industry adoption in agent frameworks)

---

## Overview

A **human-in-the-loop (HITL) approval gate** is a guardrail that intercepts sensitive tool calls before they execute, asks a human for permission, and either runs the tool (approved) or returns a blocked-action result to the agent (denied) without invoking the tool at all.

For SRE agents — which can issue `k8s_apply_*`, `restart_*`, `delete_*`, and similar destructive operations — the gate is the difference between "the agent has a production shell" and "the agent can only do what a human signs off on." The pattern is the standard answer to the prompt-injection / hallucination risk that all tool-using agents share.

## Core Content

### Configuration

```toml
[hitl]
require_approval = ["k8s_apply_*", "restart_*", "delete_*"]

[hitl.route]
mode = "webhook"                              # or "conversational"
url = "https://approvals.example.com/aura"    # webhook mode only
timeout_secs = 300
```

- `require_approval` — list of glob patterns matched against tool names. Empty = no gating. Patterns like `k8s_apply_*` cover a class of operations rather than enumerating them.
- `[hitl.route]` — the destination for approval requests.
- `mode = "webhook"` — the harness POSTs the proposed tool call to the webhook URL; the responder returns approve/deny.
- `mode = "conversational"` — the harness emits an SSE event and the client (must be an Aura-aware client with `stream=true`, e.g. the AURA CLI in HTTP mode) renders the approval UI inline in the chat session.

### Behavior

| Outcome | What Happens |
|---------|--------------|
| Approved | Tool call runs normally; worker sees the result as if it had called the tool directly. |
| Denied | Tool call does not run. Worker receives a structured "blocked-action" result. The worker can then explain to the user why the action was denied or propose an alternative. |
| Timeout | Treat as denied (configurable). |
| Webhook unreachable | Treat as denied, surface a clear error. |

### Approval Lifecycle Events

Approval lifecycle SSE events are emitted **regardless of `AURA_CUSTOM_EVENTS`**. The base `aura.*` events are turned off by default for OpenAI-spec compliance, but approval events are always on because clients need them to render the gate UI.

Conversational mode additionally emits `aura.approval_pending` and requires `stream=true` plus an Aura-aware client (the AURA CLI in HTTP mode is the reference implementation). Plain HTTP clients without approval handling will stall at the pending event.

### Cross-Pod Approval Resolution

In multi-pod deployments (Redis/Valkey session store), the approval can be resolved on a different pod than the one that parked it. The flow is:

1. Pod A executes the orchestration run and calls `require_approval` for tool `X`.
2. The approval is parked in the shared Redis session store with ID `Y`.
3. Pod B receives a `POST /v1/approvals/Y` request from the human approver.
4. Pod B looks up the parked approval, records the decision in Redis, and emits the result.
5. Pod A picks up the decision from Redis and continues execution.

This is the same cross-pod pattern that A2A `subscribe`/`cancel` uses — one shared session store, any pod can serve any request.

### Current Scope and Limits

- **Orchestration workers only.** Single-agent configs do not have HITL gates wired in this phase. The reason is partly historical (HITL was added with the worker model) and partly architectural (single-agent flows terminate the SSE stream with `finish_reason: "tool_calls"` for client-side tool passthrough, which doesn't compose well with parked approvals).
- **Aura-aware client required for conversational mode.** Plain `curl` against the chat completions endpoint cannot resolve conversational approvals — it will hang at `aura.approval_pending` until the SSE timeout.
- **Tool-name globs only.** There is no per-argument gating, no per-tenant policy, no "approval required only if arg matches pattern." Operators that need that level of control implement it in the approval service behind the webhook.

## Example Walkthrough

A worker is asked to scale a deployment. The MCP server exposes `k8s_apply_deployment`. The HITL config has `require_approval = ["k8s_apply_*"]`.

1. Worker calls `k8s_apply_deployment(name="api", replicas=10)`.
2. The harness matches `k8s_apply_*`, intercepts the call.
3. Webhook mode: harness POSTs the proposed call to the approvals URL. Operator clicks "Approve."
4. Harness executes the tool call. Worker continues with the result.
5. Worker reports "Scaled `api` to 10 replicas" to the user.

Without approval, the tool call is a single LLM decision. With approval, it is a two-party decision: the model proposes, the human disposes.

## Key Insights

1. **Glob patterns are the right unit of policy.** Enumerating every individual tool name is brittle; matching on `k8s_apply_*` or `delete_*` covers the operation class and survives tool-server renames.
2. **The approval event is always on, even when custom events are off.** Approval is a protocol concern (the client must render the gate), not a UX enhancement. The harness surfaces it unconditionally so that "AURA_CUSTOM_EVENTS=false" clients still get the gate.
3. **Conversational mode is the UX win, webhook is the integration story.** A conversational gate inside a CLI chat feels native; a webhook gate lets a third-party approval system (PagerDuty action, Slack workflow, custom portal) implement the policy.
4. **Cross-pod approval depends on the session store.** The Redis backend is what makes "approve in pod B" resolve a request parked in pod A. In-memory store means single-pod only.
5. **HITL is a defense-in-depth layer, not a security boundary.** Per-agent `client_tool_filter` and approval gates reduce blast radius but cannot prevent a determined prompt-injection attack — the model can still be coaxed into proposing a destructive call. The human approver is the last line.

## Related Concepts

- [[Concepts/agentic-harness-architecture]] — broader pattern this is a guardrail in
- [[Concepts/coordinator-worker-task-dag-orchestration]] — workers are the primary HITL scope
- [[Concepts/scratchpad-context-window-management]] — the other major safety component
- [[Entities/mezmo-aura]] — concrete implementation

## References

- Raw Article: [[Raw/github-mezmo-aura-readme-2026-07-25]]
- Original: https://github.com/mezmo/aura
- Docs: https://github.com/mezmo/aura/blob/main/docs/hitl.md
