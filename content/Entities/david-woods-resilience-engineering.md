---
title: "David Woods — Resilience Engineering"
details: "Resilience-engineering researcher whose four-dimensions framework (robustness, rebound, graceful extensibility, sustained adaptability) is the spine of Sam Newman's *Building Resilient Distributed Systems*. Newman cites the original Woods paper (pointed out to him by John Allspaw at Velocity) as something he found impenetrable for years before finally being able to read it. Woods' work originates in safety-critical systems thinking, which Newman had to translate into software-practitioner terms."
tags:
  - entity
  - software-engineering
created: 2026-10-09
updated: 2026-10-09
type: entity
sources:
  - Raw/pragmatic-engineer-resilient-systems-sam-newman-2026.md
---

# David Woods

**Source:** Sam Newman interview — Woods' original paper was pointed out to Newman at Velocity by John Allspaw.
**Category:** Resilience Engineering Researcher

## Overview

David Woods is a resilience-engineering researcher whose framework — **four dimensions of resilience** — Newman adopts as the conceptual backbone of his second book. The framework partitions resilience into:

1. **Robustness** — absorbing known perturbations.
2. **Rebound** — recovering from failure.
3. **Graceful extensibility** — dealing with surprise.
4. **Sustained adaptability** — learning and changing over longer timescales.

The framework originates in safety-critical-systems thinking (aviation, nuclear, healthcare), which Newman found inaccessible at first read. His adaptation for software practitioners — and the resulting *Building Resilient Distributed Systems* — is in part a translation of Woods' safety-engineering vocabulary into a form software engineers can use.

## Newman's framing of the translation problem

From the interview:

> "And the paper was utterly baffling to me, in absolutely no sense to me. But it was all, because it's not, yeah, because it's just, it's not written for computer scientists to read. And I'm not even a computer scientist, so I was really in trouble."

Newman admits to re-reading the paper every six months for years before it clicked. The book's structure (easy introductory chapters on timeouts and OTEL before the resilience-engineering core) is in part an answer to this translation challenge.

## Related Concepts

- [[Concepts/four-dimensions-of-resilience]] — The wiki page that applies Woods' framework
- [[Concepts/post-incident-review-culture]] — Sustained adaptability in practice
- [[Entities/sam-newman]] — Adopter

## References

- Cited in [[Raw/pragmatic-engineer-resilient-systems-sam-newman-2026]]
- Original paper originally pointed out by John Allspaw at Velocity.