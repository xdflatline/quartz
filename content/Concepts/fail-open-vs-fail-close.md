---
title: "Fail Open vs Fail Close"
details: "When a downstream dependency is unavailable or untrusted, the choice to serve the request anyway (fail open) or to refuse it (fail close) is a business decision, not a technical one. The same outage produces opposite policies for an e-commerce inventory lookup and a concert-ticket sale, because the cost of a false-positive differs by orders of magnitude. The choice can also change over time within a single company as business priorities shift."
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

When a system can't reach a downstream component it depends on (rule 2 of the three rules), it has to choose between two failure policies:

- **Fail open** — serve the request anyway, optimistically. Accept that some fraction of those requests will turn out to be wrong (chargebacks, refunds, sold-out tickets). Optimise for the customer-visible success rate.
- **Fail close** — refuse the request. Optimise for correctness; the customer sees a 5xx or a graceful-degradation page.

## The same problem, opposite policies

Newman's canonical examples:

| Domain | Downstream unknown | Default policy | Why |
|--------|--------------------|----------------|-----|
| E-commerce inventory lookup | "Do we have this item?" | **Fail open** | Customer can be refunded if not; back-order is cheap; missing the sale is the bigger loss. |
| Concert ticket sale | "Can we issue this ticket?" | **Fail close** | Tickets can't be back-ordered; downstream ramifications (flights, hotels) are non-refundable; customer's blast radius is large. |
| Uber rides, 2015 (growth era) | "Did the payment clear?" | **Fail open** | Growth matters more than unit economics; a few fraudulent rides are acceptable. |
| Uber rides, 2020+ (profitability era) | "Did the payment clear?" | **Fail close** | Unit economics matter; giving away free rides is no longer acceptable. |

The **same company** can shift the policy for the **same question** purely because the business priority changed. The policy is per-feature and time-dependent — *not* per-system.

## When to choose which

Newman's heuristic: **what's the cost of being wrong?** If the cost of a false-positive (serving an invalid request) is recoverable on the business side (refund, back-order, customer-support outreach), fail open. If the cost is irreversible or externalised to the customer in a way that destroys trust (booked flights, hospital appointments), fail close.

## Anti-pattern

Treating fail-open/fail-close as a single system-wide policy. Different features within the same product have different blast radii. A $10 taxi ride and a $1,000 taxi ride can reasonably have different failure policies.

## Related Concepts

- [[Concepts/three-rules-of-distributed-systems]] — Fail open/close is the answer when rule 2 fires
- [[Concepts/four-dimensions-of-resilience]] — Sustained adaptability requires revisiting these choices as the business changes