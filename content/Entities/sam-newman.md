---
title: "Sam Newman"
details: "British software engineer and independent consultant, author of *Building Microservices* (2015, 2nd ed. 2021) and *Building Resilient Distributed Systems* (2026). Was in the room when the term microservices was coined at a ThoughtWorks Lake District symposium (~2011–12); wrote the first microservices book extending the continuous-delivery practice he ran at ThoughtWorks Europe. Worked at ThoughtWorks for over a decade, including an embedded year and a half at Google with Mike Bland's team teaching Googlers how to write testable code."
tags:
  - entity
  - software-engineering
created: 2026-10-09
updated: 2026-10-09
type: entity
sources:
  - Raw/pragmatic-engineer-resilient-systems-sam-newman-2026.md
---

# Sam Newman

**Source:** [samnewman.io](https://samnewman.io/)
**Books:** *Building Microservices* (O'Reilly, 2015 / 2nd ed. 2021), *Building Resilient Distributed Systems* (O'Reilly, 2026)
**YouTube:** [Modern Software Engineering channel](https://www.youtube.com/@ModernSoftwareEngineering) with Dave Farley
**Category:** Engineer / Author / Independent Consultant

## Overview

Sam Newman is a British software engineer and independent consultant best known for two things: coining the modern framing of microservices (alongside James Lewis and Martin Fowler) and authoring the canonical practitioner book on the topic. His second major work, *Building Resilient Distributed Systems* (2026), applies resilience-engineering concepts — including David Woods' four-dimensions framework — to the operational reality of distributed systems.

## Career path

- **De Montfort University (Leicester)** — Software Engineering degree via the "sandwich course" model (two years study, one paid year in industry, final year). His year-in-industry was at GEC Alstom, building Fortran 77 for the European Space Agency and gas/steam turbines. His earliest memorable programming moment: refactoring a Fortran 77 codebase's 99,999-iteration loop-break limits via regex, after his boss handed him the *sed and awk* book.
- **ThoughtWorks** — Joined when the company was ~400 people, left when ~4,000. Ran the continuous-delivery practice for Europe. Worked alongside Martin Fowler, Dave Farley (his first tech lead), and Jez Humble (whom he interviewed to backfill his role at AOL). Spent ~18 months embedded at Google as a ThoughtWorks consultant, working with Mike Bland's team, Industrial Logic, and pre-acquisition Pivotal to teach Googlers how to write testable code.
- **Three startups** — All failed for different reasons. He declines to give startup advice as a result.
- **Independent consultant** — Based back in the UK after a stint in Australia. Works with clients globally; contact at samnewman.io.

## The microservices origin story

At a ThoughtWorks architectural symposium in the Lake District (~2011–12), James Lewis pitched a pattern he was initially calling "micro apps". Someone in the (mostly hungover) room of ~10 people corrected it to "services". James and Martin Fowler wrote the first paper on Fowler's website. Newman was working in parallel on continuous-delivery and infrastructure automation; his first microservices book (2015) was an extension of that lens.

## Resilience and the second book

The roots of *Building Resilient Distributed Systems* go back to a Velocity conference paper by **David Woods** on resilience engineering that Newman admits he couldn't read for years ("not written for computer scientists"). Over time the framework's four dimensions — robustness, rebound, graceful extensibility, sustained adaptability — became the spine of the book.

## Recurring themes in his work

- **Information hiding and modules** — Newman frames microservices as "smuggling 1970s concepts (Parnas modules, coupling, cohesion) back into the mainstream."
- **Production is truth** — A mantra he borrows from Charity Majors. Specs and code are intentions; production is reality.
- **Be multi-vendor / multi-model when hedging AI bets** — Cited as a 2026 resilience posture.
- **Architecture as a skill learned through modules** — Recommends Vlad Khononov's *Balanced Coupling*, Neal Ford & Mark Richards' *Software Architecture Fundamentals*, and David Parnas' original 1971/72 papers.

## Selected references in the source

- [samnewman.io](https://samnewman.io/) — personal site
- [Building Microservices (O'Reilly)](https://www.oreilly.com/library/view/building-microservices-2nd/9781492034018/) — 2nd edition
- *Building Resilient Distributed Systems* (O'Reilly, 2026)
- Pragmatic Engineer podcast episode (2026-10-08) — full transcript in [[Raw/pragmatic-engineer-resilient-systems-sam-newman-2026]]

## Related Concepts

- [[Concepts/microservices-as-architecture-of-last-resort]] — Newman's strong claim about why microservices are a means to an end, not an end in themselves
- [[Concepts/three-rules-of-distributed-systems]] — Newman's distillation of distributed-systems failure modes
- [[Concepts/four-dimensions-of-resilience]] — David Woods' framework as adopted by Newman
- [[Entities/thoughtworks]] — Formative employer