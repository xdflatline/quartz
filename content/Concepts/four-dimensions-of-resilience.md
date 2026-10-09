---
title: "The Four Dimensions of Resilience (David Woods)"
details: "David Woods' four-part framework for resilience engineering — robustness, rebound, graceful extensibility, sustained adaptability — adopted by Sam Newman as the spine of *Building Resilient Distributed Systems*. Most engineering effort goes to dimension 1 (robustness), but the other three are equally required; the latter two depend on people, culture, and psychological safety."
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

David Woods' framework partitions resilience into four overlapping capabilities:

| # | Name | One-line gloss | Time horizon |
|---|------|----------------|--------------|
| 1 | **Robustness** | Absorb *known* perturbations. | Before incident |
| 2 | **Rebound** | Recover from failure quickly. | During incident |
| 3 | **Graceful extensibility** | Deal with *surprise* — what you didn't model. | During incident |
| 4 | **Sustained adaptability** | Learn from what happened and change the system. | After incident, ongoing |

## Why the four, not one

Newman's warning: **most engineers focus entirely on robustness**. Kubernetes replacing a failed pod is robustness — known perturbation, automated response, done. The danger is that the measures you add for robustness (Kubernetes, multi-region, multi-cloud) **expand the surface area for new failure modes**. Robustness is necessary but never sufficient.

Rebound requires admitting failure will happen — you can't recover from what you won't admit. The practice that supports it is **simulation** (Chaos Monkey, Uptime Labs incident training, regular game days). Doing it once isn't enough because the system keeps changing.

Graceful extensibility is about the things you *couldn't* model. This is fundamentally about people, not technology. Hierarchical organizations with narrow job descriptions deal with surprise badly because the structure itself is built around the known. Drills (Google's "Wheel of Misfortune") and physical-access edge cases (the Meta BGP outage that required physically breaking into the data center because the door-lock was tied to the domain that was down) are the canonical examples.

Sustained adaptability is the long horizon: read other people's incident reports even when you don't have an incident of your own. Newman cites *The Void* (a curated incident-report library). This dimension collapses if you don't have **psychological safety** — if people can't raise issues, you never get the data you need to learn.

## Operational consequences

- Robustness investments need a **trade-off table** — every layer of redundancy adds a new class of failure.
- Rebound requires **destructive testing** of on-call rotations, escalation paths, and runbooks. Scheduled, not improvised.
- Graceful extensibility is the case for **drills** and for not over-coupling physical security / operational tooling to your own software domain.
- Sustained adaptability is the case for **public post-mortems**, blameless retros, and a culture where surfacing problems is rewarded.

## Related Concepts

- [[Concepts/post-incident-review-culture]] — The cultural substrate of dimensions 3 and 4
- [[Concepts/thundering-herd-and-retry-storm]] — A failure mode that breaks dimension 2 if not practiced
- [[Concepts/three-rules-of-distributed-systems]] — The physical layer the four dimensions operate on top of