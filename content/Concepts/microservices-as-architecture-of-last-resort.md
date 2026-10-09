---
title: "Microservices as Architecture of Last Resort"
details: "Sam Newman's strong claim that microservices are an architecture of last resort — they push you toward aggressive state distribution, so you adopt them only when the cost is justified by the benefit (most often: organizational autonomy). The term itself was coined at a ThoughtWorks architectural symposium in the English Lake District, around 2011–2012, by James Lewis (with Martin Fowler as co-author of the first paper)."
tags:
  - concept
  - software-engineering
  - architecture-pattern
created: 2026-10-09
updated: 2026-10-09
type: concept
sources:
  - Raw/pragmatic-engineer-resilient-systems-sam-newman-2026.md
---

## Definition

Microservices are an **opinionated style of SOA** characterized by two non-negotiables and one soft recommendation:

1. **Independent deployability** — the unit of deployment is a single microservice boundary. Deploying multiple services together makes it a monolith (or at least a mini-monolith).
2. **Default to business-domain boundaries** (not technical decomposition) — service boundaries follow the domain, not the n-tier layers.
3. (Soft) Domain-driven design is the natural toolkit for finding those boundaries, but it's optional.

Newman positions microservices as an **architecture of last resort**: aggressive distribution of state, increased surface area for failure, more moving parts. The only really good reason to accept those costs is **organizational autonomy** — teams that need to act independently. "Means to an end, not the end itself."

## Origin

Coined at a ThoughtWorks architectural symposium in the English Lake District, ~2011–2012. James Lewis named the pattern (originally calling them "micro apps", corrected to "services" by someone in the room — neither Newman nor Lewis remembers who). Most attendees were hungover. The first paper on Martin Fowler's website was co-authored by James Lewis and Martin Fowler.

## The Uber story (the cautionary tale)

Twan Palm (Uber's CTO at the time) told the Pragmatic Engineer podcast that Uber never wanted thousands of microservices. They had a slow monolith blocking delivery, so they imposed a hard rule: *everything new must be its own service.* The result — ~2 microservices per engineer — was the unintended consequence, not the goal. Years later, Uber is selectively re-merging based on business domain.

## When *not* to use microservices

- If your primary goal is **organizational autonomy** but you don't actually have the autonomy yet — building microservices won't create autonomy for you.
- If your domain is simple (most consumer-internet products start simple) — the operational cost is disproportionate.
- If your business processes are not yet stable — premature distribution locks in bad boundaries.
- If your team can't operate the platform you're committing to (deploy pipeline, observability, on-call) — microservices amplify every operational gap.

## What microservices actually were, pre-naming

- Netflix called theirs "fine-grained SOA" before the microservices label existed.
- REA (realestate.com.au) and Netflix were Newman's two case studies for the original book.
- The post-naming period saw "semantic diffusion" — every SOA project retroactively relabeled itself microservices.

## What Newman thinks microservices actually smuggle in

The 2010s microservices movement was, on Newman's reading, an exercise in **smuggling 1970s CS ideas back into the mainstream** — information hiding, coupling, cohesion, Parnas modules. The distributed-systems part is implementation; the modular-software-design part is the actual content.

## Related Concepts

- [[Concepts/thoughtworks]] — Where the term was coined
- [[Concepts/four-dimensions-of-resilience]] — Microservices amplify robustness concerns (more things that can fail) and require stronger rebound practice
- [[Concepts/three-rules-of-distributed-systems]] — Microservices make all three rules more present, not less