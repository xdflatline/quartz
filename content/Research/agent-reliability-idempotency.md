---
title: "Agent Reliability: Idempotency and the Read/Write Asymmetry"
detail: Research index on making write-capable AI agents safe against network failures through idempotency boundaries borrowed from payments infrastructure.
details: Research index covering the argument that most production AI agent failures are reliability failures (duplicate writes on retry) rather than reasoning failures. The core insight is the read/write asymmetry -- read retries are free, write retries are double-actions. The solution is an idempotency boundary (derived from Stripe's Idempotency-Key pattern) that collapses duplicate executions into replays, keyed on the content of the intended action. Smarter models exacerbate the problem by retrying more aggressively.
tags:
  - research
created: 2026-07-01
updated: 2026-07-01
type: research
sources:
  - Raw/devto-ai-agent-idempotency-2026.md
---

## Agent Reliability: Idempotency and the Read/Write Asymmetry

### Thesis

Most production AI agent failures are not reasoning failures. They are infrastructure failures -- specifically, the read/write asymmetry where retries are free for read-only agents but catastrophic for write-capable agents. The fix is not a smarter model; it is an idempotency boundary.

### Core Concepts

- [[Concepts/idempotency-for-ai-agents|Idempotency for AI Agents]] -- the pattern of wrapping side-effecting calls in a deduplication store keyed on intent content
- [[Entities/stripe-idempotency-key|Stripe Idempotency-Key]] -- the origin pattern from payments infrastructure

### Key Arguments

1. **Intelligence != Reliability**: The model can reason perfectly and still cause double-charges. These are orthogonal problems.
2. **Smarter models make it worse**: More capable agents retry more aggressively, amplifying the double-write problem.
3. **The boundary is the fix**: Safety lives at the infrastructure boundary, not in the model's judgment.
4. **Deterministic key derivation**: For autonomous agents (no human clicks), the idempotency key must be derived from intent content, not randomly generated.

### Failure Modes

| Mode | Description |
|------|-------------|
| False duplicate | Distinct actions hash to same key; legitimate action dropped |
| Missed duplicate | Retries hash to different keys; double-write passes through |

### Open Questions

- How to define "same action" for complex multi-step agent plans?
- Should idempotency be per-tool or per-plan?
- Interaction with [[Concepts/multi-agent-orchestration-patterns|multi-agent orchestration]] -- who owns the idempotency boundary?
- TTL tuning: 24h (Stripe) may be too short for long-running agent workflows

### Sources

- [[Raw/devto-ai-agent-idempotency-2026]] -- primary article
