---
title: "Resilient Distributed Systems — Synthesis Index (Newman 2026)"
details: "Synthesis of Sam Newman's *Building Resilient Distributed Systems* (2026) and the related Pragmatic Engineer podcast interview. Pairs Newman's pragmatic distributed-systems engineering with David Woods' resilience-engineering framework and the contemporary AI / cognitive-debt concerns surfaced in the same conversation. Connects Newman's three rules and four dimensions to existing wiki concepts (idempotency for AI agents, spec-driven development, fail-open/fail-close, thundering herd)."
tags:
  - research
  - software-engineering
  - infrastructure
created: 2026-10-09
updated: 2026-10-09
type: research
sources:
  - Raw/pragmatic-engineer-resilient-systems-sam-newman-2026.md
---

# Resilient Distributed Systems — Synthesis Index (Newman 2026)

This page is a synthesis of Sam Newman's second book (*Building Resilient Distributed Systems*, O'Reilly 2026) and his [Pragmatic Engineer podcast appearance](https://newsletter.pragmaticengineer.com/p/building-resilient-systems-with-sam) (full transcript preserved in [[Raw/pragmatic-engineer-resilient-systems-sam-newman-2026]]).

The book is a practitioner's bridge between two bodies of work:

1. **Classical distributed-systems engineering** — timeouts, idempotency, observability, CAP, PACELC, retries, thundering herds, post-mortems.
2. **Resilience engineering** (David Woods' framework) — robustness, rebound, graceful extensibility, sustained adaptability. Originally a safety-critical-systems vocabulary; Newman translates it for software practitioners.

Newman's stance throughout: production is truth ([[Concepts/production-is-truth]]), and resilience is a *degree*, not a binary. Most engineers over-invest in dimension 1 (robustness) and under-invest in dimensions 3 and 4 (which depend on culture, not technology).

## Source decomposition

- **Source:** Pragmatic Engineer Podcast, "Building resilient systems with Sam Newman" (2026-10-08). Hosted by [[Entities/gergely-orosz]].
- **Guest:** [[Entities/sam-newman]].
- **Original URL:** https://newsletter.pragmaticengineer.com/p/building-resilient-systems-with-sam?showTranscript=true
- **Full transcript:** [[Raw/pragmatic-engineer-resilient-systems-sam-newman-2026]]
- **Adjacent primary source:** *Building Resilient Distributed Systems* (O'Reilly, 2026).

## Conceptual map (Newman's spine)

### The three rules — the irreducible physics

| Rule | Domain | What it produces |
|------|--------|------------------|
| 1. It takes time. | Network latency, serialization, BGP. | Forces timeouts. |
| 2. Sometimes the thing you want to talk to isn't there. | Unreachable peers. | Forces retries, idempotency, circuit breakers. |
| 3. Resource pools are not infinite. | CPU, memory, queues, connections. | Forces back-pressure and load shedding. |

See [[Concepts/three-rules-of-distributed-systems]]. Newman claims **rule 3 is the cause of most outages** — typically a downstream resource saturates, retries stack on top, and the cascade kills something upstream.

### The four dimensions — what to invest in

| Dimension | Time horizon | Practice |
|-----------|--------------|----------|
| Robustness | Pre-incident | Known perturbation handling. |
| Rebound | During incident | Detection, recovery, drill. |
| Graceful extensibility | During incident (surprise) | Drills, broad decision authority. |
| Sustained adaptability | After / ongoing | Post-mortems, blameless retros, reading others' incidents. |

See [[Concepts/four-dimensions-of-resilience]]. Newman notes that the **last two are fundamentally about people and culture**, not technology.

### The fail-open / fail-close axis

Per-feature, time-dependent, business-driven. Newman uses the e-commerce vs concert-ticket contrast as the canonical example. The same company (Uber) flipped from fail-open to fail-close for payment-related failures as it shifted from growth to profitability.

See [[Concepts/fail-open-vs-fail-close]].

### Idempotency — the safe-retry mechanism

Newman's prescription: idempotency keys for new APIs (Stripe/Adyen/AWS pattern); fingerprints for retrofit (with awareness of false negatives on legitimate duplicates). Both is best.

See [[Concepts/idempotency-keys-vs-fingerprints]] — and the related wiki page [[Concepts/idempotency-for-ai-agents]], which is the AI-tool-call specialization of the same pattern.

See [[Concepts/thundering-herd-and-retry-storm]] for the failure mode that emerges when retries aren't bounded by idempotency, backoff, and jitter.

### Observability, SLOs, SLIs

Newman treats observability as a property of a system, not a tool stack. Observability is the raw stream of structured events; SLIs are the binary (good/bad) judgements made over that stream; SLOs are the commitments built from SLIs. The implicit chain is: events → SLIs → SLOs → user experience.

### The AI / cognitive dimension

Newman's position on AI and resilience has three layers:

1. **Macro** — LLM providers don't have a viable financial path to sustainability ($2.6T needed by 2030 per *The Economist*, vs. a $1.4T software market). This isn't solvable by individual engineering teams; it shapes the resilience posture (be multi-vendor, multi-model).
2. **Meso** — LLMs are not world models. They have no causal model. Guardrails are a stopgap; the long-term answer is world models or bounded delegation.
3. **Micro** — Tactical hedging: be multi-vendor, be multi-model, swap deterministic code in where you can, modularize so AI runs inside safe boundaries and humans think about the gaps.

Newman's two AI-related failure modes are [[Concepts/cognitive-depth-vs-cognitive-surrender]]: the slow erosion of human ability to evaluate output, and the acute LGTM-pattern approval without engagement.

The on-ramp to handing work to agents is [[Concepts/lit-where-good-looks-like]]: (1) define what good looks like as a spec, (2) prove the system actually meets that good.

## How this fits the existing wiki graph

This ingestion creates bidirectional links with several pre-existing concepts:

- **[[Concepts/idempotency-for-ai-agents]]** — already in the wiki (added 2026-07-01). The new [[Concepts/idempotency-keys-vs-fingerprints]] page treats Newman's general-purpose framing and cross-links into the AI-specific page. The AI page should also reference the Newman one (bidirectional). *Action: see "Pending cross-references" below.*
- **[[Concepts/spec-driven-development-sdd-2026]]** — already in the wiki (Diaz et al., 2026). Newman's "start with a spec" on-ramp is consistent with the SDD paper's framing; the new [[Concepts/lit-where-good-looks-like]] page cross-links into it.
- **[[Concepts/observational-memory-pattern]]** — adjacent; Newman's "stream of structured events" is the producer side of any observational memory.
- **[[Entities/thoughtworks]]** — Sam Newman's formative employer. Newman page cross-links into it.

## Pending cross-references

The following pre-existing wiki pages should gain a one-line reference to this research page under "Related Research" / "Next Research Directions" to complete the bidirectional graph. *Not done automatically — listed here for the operator to decide whether to edit them.*

- `Concepts/idempotency-for-ai-agents.md` — add a line under "Related Concepts" pointing here.
- `Concepts/spec-driven-development-sdd-2026.md` — add a line noting that Newman's "define what good looks like" gate is consistent with SDD's spec-as-substrate stance.
- `Entities/thoughtworks.md` — already references Sam Newman's name in passing (per the search match); could add a backlink to [[Entities/sam-newman]] and this research page.

## Reading list (Newman-recommended)

- *Building Resilient Distributed Systems* — Newman (2026) — the source
- *Building Microservices* — Newman (2015 / 2nd ed. 2021) — the precursor
- *Software Architecture Fundamentals* — Neal Ford & Mark Richards — Newman: "good read, but I don't agree with everything"
- *Balanced Coupling* — Vlad Khononov — Newman's strongest recommendation for modularity
- *Growing Object-Oriented Software Guided by Tests* — Freeman & Price — the London XP/GOOS tradition
- *Tidy First?* — Kent Beck — "software design is an exercise in human relationships"
- David Parnas' original 1971/1972 papers on information hiding / modularity
- David Woods' original resilience-engineering paper (cited as impenetrable-but-essential)

## Key Insights

1. **Most outages trace back to rule 3** (resource saturation), usually amplified by rule 2 (unreachable peer) producing a retry storm.
2. **Resilience has four orthogonal dimensions** — and engineers systematically under-invest in dimensions 3 and 4 because they require culture, not technology.
3. **Fail-open vs fail-close is a per-feature, time-dependent business decision** — not a system-wide policy, not a one-time choice.
4. **Idempotency keys > fingerprints**, but fingerprints are the right answer when you can't change the client; both-together is best.
5. **Production is truth** — specs and code are intentions; production is reality.
6. **LLMs are not world models** — guardrails are a stopgap; the long-term answer is bounded delegation with verification against production.
7. **Cognitive surrender > cognitive depth** as the acute AI risk; the antidote is keeping humans in the loop on what matters.
8. **Define what good looks like** — Newman's gate for handing work to agents. Without both halves (define + prove), you can't safely automate.

## Related Concepts

- [[Concepts/three-rules-of-distributed-systems]]
- [[Concepts/four-dimensions-of-resilience]]
- [[Concepts/fail-open-vs-fail-close]]
- [[Concepts/idempotency-keys-vs-fingerprints]]
- [[Concepts/cognitive-depth-vs-cognitive-surrender]]
- [[Concepts/post-incident-review-culture]]
- [[Concepts/production-is-truth]]
- [[Concepts/microservices-as-architecture-of-last-resort]]
- [[Concepts/thundering-herd-and-retry-storm]]
- [[Concepts/lit-where-good-looks-like]]
- [[Concepts/idempotency-for-ai-agents]] — pre-existing AI-specialization page
- [[Concepts/spec-driven-development-sdd-2026]] — pre-existing SDD concept page

## Related Entities

- [[Entities/sam-newman]]
- [[Entities/gergely-orosz]]
- [[Entities/james-lewis-microservices]]
- [[Entities/charity-majors-honeycomb]]
- [[Entities/david-woods-resilience-engineering]]
- [[Entities/martin-fowler]]
- [[Entities/thoughtworks]]