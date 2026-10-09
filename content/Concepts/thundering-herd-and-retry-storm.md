---
title: "Thundering Herd and Retry Storm"
details: "A failure mode where recovery from one outage causes the next one: a saturated dependency returns, every queued retry hits it simultaneously, and the dependency is taken down again. Newman's chapter in *Building Resilient Distributed Systems* partitions these into malicious (DDoS), self-inflicted (cache collapse), and product-too-successful (Twitter launch, healthcare.gov). Each category calls for a different mitigation; horizontal scaling helps one and makes another more expensive."
tags:
  - concept
  - software-engineering
  - infrastructure
created: 2026-10-09
updated: 2026-10-09
type: concept
sources:
  - Raw/pragmatic-engineer-resilient-systems-sam-newman-2026.md
---

## Definition

A **thundering herd** is any situation where capacity demand far outstrips capacity supply. The "thundering" is the many-requests-for-few-resources asymmetry. Newman treats this as a direct expression of [[Concepts/three-rules-of-distributed-systems#definition|rule 3 (resource pools are not infinite)]].

A **retry storm** is the canonical mechanism by which a thundering herd forms: a downstream fails, clients retry (often with no backoff), and the volume of retries exceeds the capacity that the downstream needs to recover. Recovery time extends; the herd persists.

## Categories of thundering herd

| Category | Cause | Example | Mitigation |
|----------|-------|---------|------------|
| **Malicious** | External adversary. | DDoS attack. | CDN / edge protection (Fastly, Cloudflare). Horizontal scaling makes it worse — "distributed denial of cash". |
| **Self-inflicted (cache collapse)** | Cache restart or eviction storm → origin gets all the misses simultaneously. | Restarting a service with a cold cache. | Snapshot cache to disk before restart; keep services off until cache refills. |
| **Self-inflicted (retry storm)** | A failed dependency is hit immediately by many concurrent retries. | **Square (2017)** — Multipass auth restarted, pulled state from Redis, retry loop had no backoff and a 500-retry limit, smashed Redis repeatedly. | Sensible retry policy, externalized retry config, jittered backoff. |
| **Legitimate load** | Real users, more than expected. | **Twitter launch**, **healthcare.gov** going live in 36 states at once. | Constrained signups (invite codes), staged rollout, product-side throttling. |

## Key insight from Newman

Although all four categories *look* the same downstream (saturated resource, rule 3 violation), **the right mitigation is category-specific**:

- Malicious → CDN, not horizontal scaling.
- Cache collapse → snapshotting + controlled restart.
- Retry storm → retry policy + jitter + backoff.
- Legitimate load → staged rollout + product-side throttling.

Tossing the same fix at all four is wrong. A horizontal-scaling response to a DDoS is the "distributed denial of cash" trap: you spend more money to stay just as down.

## Diagnosis checklist

When you suspect thundering herd:

1. Is this a sudden burst, or sustained growth? Burst → retry storm / cache collapse. Sustained → legitimate load or DDoS.
2. Does the recovery curve look right? Service should drain the backlog, not re-collapse. If it does, retry policy is the issue.
3. Is there a non-uniform retry pattern across clients? Look for one misconfigured client hammering the system.

## Related Concepts

- [[Concepts/three-rules-of-distributed-systems]] — Rule 3 is exactly this
- [[Concepts/idempotency-keys-vs-fingerprints]] — Idempotency is what makes retry storms survivable for write-side operations
- [[Concepts/four-dimensions-of-resilience]] — Rebound (dimension 2) is what breaks first when a thundering herd hits