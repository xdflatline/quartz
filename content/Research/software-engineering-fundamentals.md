---
title: "Software Engineering Fundamentals — Research Index"
details: "Research synthesis of the canonical software-engineering reading list retained by the operator (0x1d): The Pragmatic Programmer (Hunt & Thomas, 1999/2019), Domain-Driven Design (Evans, 2003), and A Philosophy of Software Design (Ousterhout, 2018), together with the Wikipedia Software Rot article (covering software entropy and broken-windows theory). The three texts converge on a single discipline — managing complexity through deliberate design — and the index organises eight extracted concepts (Software Engineering Fundamentals, Software Entropy, Deep Modules, Bounded Context, Ubiquitous Language, DDD Strategic Design, DDD Tactical Patterns, Pragmatic Programmer Tips) and four canonical entities (the three books and three authors) into a connected graph. The grill-with-docs skill is the operational layer where this body of work meets the operator's daily practice."
tags:
  - research
  - software-engineering
created: 2026-09-18
updated: 2026-09-18
type: research
sources:
  - "[[Raw/software-engineering-fundamentals-sources-2026-09-18]]"
---

# Software Engineering Fundamentals — Research Index

**Updated:** 2026-09-18
**Source:** [[Raw/software-engineering-fundamentals-sources-2026-09-18]] — Hunt & Thomas (1999/2019), Evans (2003), Ousterhout (2018), Wikipedia *Software Rot*, Martin Fowler's *Bounded Context* and *Ubiquitous Language* write-ups.

---

## Overview

This research index organises the canonical software-engineering reading list retained by the operator (0x1d) as part of his named developer-reading-list-and-concepts-to-explore. The list comprises three books and four concepts to explore:

**Books**

- [[Entities/pragmatic-programmer-book]] — Hunt & Thomas, 1999 (20th-anniversary ed. 2019)
- [[Entities/domain-driven-design-book]] — Evans, 2003
- [[Entities/philosophy-of-software-design-book]] — Ousterhout, 2018

**Concepts to explore**

- Software Entropy — the first-order phenomenon the rest of the fundamentals exist to fight
- Software Engineering Fundamentals — the umbrella discipline
- Deep Modules — Ousterhout's primary prescription for module design
- (Operationalised through the operator's `grill-with-docs` skill)

The three books are independently sufficient; the value of reading all three is the **convergent diagnosis** of the same disease (complexity, decay, misnamed code, wrong boundaries) and the **complementary treatments** they prescribe. Read together, the operator gets a complete software-engineering discipline: a theory of complexity (Ousterhout), a theory of boundaries (Evans), and a theory of practice (Hunt & Thomas).

The `grill-with-docs` skill is the operational layer: it is during the grilling session that the operator and the assistant converge on the domain language, name the bounded contexts, and identify the deep modules — turning these concepts into daily practice rather than only references.

## Concepts

### The umbrella

- [[Concepts/software-engineering-fundamentals]] — the umbrella discipline; complexity management through deliberate design
- [[Concepts/software-entropy]] — software entropy, broken-windows theory, dormant vs. active rot
- [[Concepts/deep-modules]] — Ousterhout's deep-modules principle; small interface, powerful functionality
- [[Concepts/pragmatic-programmer-tips]] — the 70-tip Quick Reference from Hunt & Thomas

### Domain-Driven Design (Evans)

- [[Concepts/ddd-bounded-context]] — the central pattern of strategic design
- [[Concepts/ddd-ubiquitous-language]] — the practice that gives a bounded context its cohesion
- [[Concepts/ddd-strategic-design]] — the system-level discipline (context maps, subdomains, large-scale structure)
- [[Concepts/ddd-tactical-patterns]] — the within-context building blocks (entities, value objects, aggregates, repositories, factories, services, domain events)

### Cross-cutting: which book says what

| Concept | Hunt & Thomas | Evans | Ousterhout |
|---------|---------------|-------|------------|
| DRY | Tip 11 | — | — |
| Orthogonality | Tip 13 | Implicit (bounded context) | Implicit (deep modules) |
| Domain language | Tips 17, 54 | Ubiquitous Language | Implicit (naming) |
| Bounded context | — | Central pattern | — |
| Deep modules | Implicit (orthogonality, decoupling) | Implicit (aggregate as deep module) | Central pattern |
| Entropy / broken windows | Tip 4 | — | Strategic vs. tactical programming |
| Design by contract | Tip 26 | — | — |
| Tracer bullets | Tip 15 | — | — |
| Naming | Tips 44, 54 | Ubiquitous language | Chapter 13 |
| Ruthless testing | Tips 56–59 | — | — |
| Consistency | Implicit | — | Chapter 16 |

## Tools & Projects

### Books

- [[Entities/pragmatic-programmer-book]] — *The Pragmatic Programmer: From Journeyman to Master* (1999; 20th-anniversary ed. 2019)
- [[Entities/domain-driven-design-book]] — *Domain-Driven Design: Tackling Complexity in the Heart of Software* (2003)
- [[Entities/philosophy-of-software-design-book]] — *A Philosophy of Software Design* (2018)

### People

- [[Entities/andrew-hunt-dave-thomas]] — co-authors of *The Pragmatic Programmer*; co-founders of the Pragmatic Bookshelf; Agile Manifesto signatories
- [[Entities/eric-evans]] — author of *Domain-Driven Design*; founder of Domain Language, Inc.
- [[Entities/john-ousterhout]] — author of *A Philosophy of Software Design*; Stanford CS professor emeritus; creator of Tcl and Tk

### Operational skill

- `grill-with-docs` — operator's skill for establishing a shared domain language during grilling sessions (where the named fundamentals become daily practice)

## Raw Sources

- [[Raw/software-engineering-fundamentals-sources-2026-09-18]] — verbatim source bundle: full Pragmatic Programmer tip table, Wikipedia *Software Rot*, Matt Duck's detailed PoSD review, Martin Fowler's *Bounded Context* and *Ubiquitous Language* write-ups, Wikipedia *Domain-driven design*

## Key Threads/Sources Table

| Source | Topic | Date | Key items |
|--------|-------|------|-----------|
| [[Raw/software-engineering-fundamentals-sources-2026-09-18]] §1 — Hugo Matilla's reproduction | Pragmatic Programmer Quick Reference | 1999 (20th anniv. 2019) | 70 tips; broken windows (Tip 4); DRY (Tip 11); orthogonality (Tip 13); tracer bullets (Tip 15); domain languages (Tip 17); design by contract (Tip 26); project glossary (Tip 54); ruthless testing (Tips 56–59); sign your work (Tip 70) |
| [[Raw/software-engineering-fundamentals-sources-2026-09-18]] §2 — Wikipedia *Software Rot* | Software entropy / decay | Continuous | Bit rot; dormant vs. active rot; broken-windows metaphor; onceability; TLS apocalypse; Hunt & Thomas attribution |
| [[Raw/software-engineering-fundamentals-sources-2026-09-18]] §3 — Matt Duck review of PoSD | A Philosophy of Software Design | 2021 (book 2018) | Three faces of complexity; tactical vs. strategic programming; deep modules; pass-through antipatterns; pull complexity downwards; comments; naming; consistency; design it twice; TDD critique |
| [[Raw/software-engineering-fundamentals-sources-2026-09-18]] §4 — Wikipedia *Domain-driven design* | DDD overview | Continuous | Term coined by Evans 2003; ubiquitous language / strategic / tactical; entity / value object / domain event / aggregate / repository / factory / service; domain vs. integration events; 9 context-mapping patterns |
| [[Raw/software-engineering-fundamentals-sources-2026-09-18]] §4 — Martin Fowler, *Bounded Context* | DDD strategic-design | 2014 | Bounded context as the central DDD pattern; total unification not feasible; multiple canonical models; context maps; culture drives boundaries |
| [[Raw/software-engineering-fundamentals-sources-2026-09-18]] §4 — Martin Fowler, *Ubiquitous Language* | DDD foundational practice | 2006 | Common rigorous language between developers and users; based on the domain model; must evolve; the practice is the artefact |

## Cross-Cutting Themes

### 1. Three books, one discipline

The three canonical software-engineering texts of the practitioner canon — Hunt & Thomas (1999), Evans (2003), Ousterhout (2018) — agree on far more than they disagree. They describe a single underlying discipline whose central concern is the **management of complexity in software systems over time**.

| Book | Primary contribution |
|------|----------------------|
| Hunt & Thomas | Daily practice: DRY, orthogonality, tracer bullets, broken windows, design by contract, project glossary, pragmatic teams |
| Evans | Boundary discipline: ubiquitous language, bounded contexts, context maps, subdomains, tactical building blocks |
| Ousterhout | Theory of complexity: change amplification, cognitive load, unknown unknowns; deep modules vs. shallow modules |

Read together, the operator gets a complete software-engineering discipline: a theory of complexity, a theory of boundaries, and a theory of practice.

### 2. The convergence on five principles

All three books converge on a small number of principles:

1. **Complexity must be managed, not endured.** (All three.)
2. **Names and language are the design.** (Evans ubiquitous language; Hunt & Thomas project glossary; Ousterhout naming.)
3. **Boundaries matter.** (Evans bounded contexts; Ousterhout deep modules; Hunt & Thomas orthogonality.)
4. **Decay is real, and fighting it is the job.** (Hunt & Thomas broken windows; Wikipedia software rot; Ousterhout strategic programming.)
5. **Code is for readers.** (Hunt & Thomas communication; Ousterhout comments; Evans language-in-code.)

These five principles are the "software engineering fundamentals" the operator has asked about. They are not subject to fashion; they survive any change of language, framework, or methodology.

### 3. Strategic matters more than tactical

A cross-text lesson, particularly from Evans and reinforced by the practitioner consensus, is that **strategic design matters more than tactical design**. Getting the boundaries right is more important than the choice of entity vs. value object. Wrong boundaries are expensive to fix; wrong tactical patterns are cheap.

This is also a reminder that [[Concepts/deep-modules]] (Ousterhout) is a strategic decision, not a tactical one. The interface of a module is a strategic choice about what complexity to hide.

### 4. The lessons are layered, not exclusive

The three books layer:

- **Ousterhout** answers "what is the goal?" (manage complexity) and "what is the unit?" (the module).
- **Evans** answers "how do you draw boundaries between units?" (bounded contexts, ubiquitous language).
- **Hunt & Thomas** answer "what is the daily practice?" (DRY, orthogonality, tracer bullets, broken windows, project glossary).

You can read them in any order. You should read all three.

### 5. The grill-with-docs connection

The operator (0x1d) retains the `grill-with-docs` skill specifically to operationalise this body of work. During a grilling session, the operator and the assistant:

- Establish the ubiquitous language (Evans) for the work to be done.
- Identify the bounded contexts (Evans) — what is in scope, what is out of scope.
- Name the deep modules (Ousterhout) — the interfaces and their hidden complexity.
- Cite the relevant pragmatic-programmer tips (Hunt & Thomas) — Tip 4 (broken windows), Tip 11 (DRY), Tip 13 (orthogonality), Tip 17 (problem-domain), Tip 54 (project glossary).

The grilling session is the practice; the books are the reference; the wiki pages are the index.

## Connection to existing garden pages

The software-engineering-fundamentals body of work relates to several pre-existing pages in the garden:

- [[Concepts/pragmatic-anti-dogma-modeling]] — Reis's MMA Belief 9: "train everything, apply what works". Same anti-dogma posture as the software-engineering fundamentals: principles over tribal allegiance.
- [[Concepts/data-model-as-tool-not-theory]] — Kent's 1978 framing that data models are tools, not theories. Same shape as the deep-modules principle: evaluate models as economic, incomplete, versatile tools.
- [[Concepts/map-vs-territory-data-modeling]] — Kent's framing. Ousterhout's complexity-vs-simplicity argument is the system-design analogue.
- [[Entities/data-and-reality]] — Kent's book. Same era of foundational software-engineering thinking as Hunt & Thomas.

## Next Research Directions

- **Re-read the three books with the grill-with-docs skill in mind.** Treat the next grilling session for any non-trivial system-design work as a structured pass through the 70-tip Quick Reference and the strategic-design patterns.
- **Map each open-source project in ~/jin/ against the deep-modules principle.** Identify which modules are deep (large capability, small interface) and which are shallow (large interface, small capability). The shallow ones are the candidates for refactor.
- **Identify the bounded contexts in the Quartz wiki ingestion pipeline.** Treat the Raw/Concepts/Entities/Research tiers as separate bounded contexts with their own ubiquitous languages; identify any context-map relationships that need explicit anti-corruption layers.
- **Add an entity page for the `grill-with-docs` skill itself.** The skill is the operational layer where this body of work meets the operator's daily practice; it deserves its own index.
- **Build a personal "developer reading list" with progress tracking.** Three books in the canonical list, plus follow-on literature (Vernon's IDDD, Fowler's *Refactoring*, Beck's TDD by Example, Brooks's *Mythical Man-Month*).
