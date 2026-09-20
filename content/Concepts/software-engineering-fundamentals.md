---
title: "Software Engineering Fundamentals"
details: "The umbrella discipline that asks not how to write code but how to design software systems that remain understandable, modifiable, and trustworthy over years of evolution. Distilled from the three canonical 1999–2018 texts — The Pragmatic Programmer (Hunt & Thomas), Domain-Driven Design (Evans), and A Philosophy of Software Design (Ousterhout) — the fundamentals reduce to a small number of principles that recur across all three: minimise complexity, manage dependencies, keep the interface simple relative to its capability, name things after the domain, treat decay as a first-class concern, and write code for the reader rather than the writer."
tags:
  - concept
  - software-engineering
created: 2026-09-18
updated: 2026-09-18
type: concept
sources:
  - "[[Raw/software-engineering-fundamentals-sources-2026-09-18]]"
---

# Software Engineering Fundamentals

**Source:** [[Raw/software-engineering-fundamentals-sources-2026-09-18]] — distilled from Hunt & Thomas (*The Pragmatic Programmer*, 1999), Evans (*Domain-Driven Design*, 2003), and Ousterhout (*A Philosophy of Software Design*, 2018).
**Category:** Software engineering philosophy (umbrella concept)
**Status:** Fundamental — the cross-text principles below are not subject to fashion

---

## Overview

The three canonical software-engineering texts of the practitioner canon — Hunt & Thomas's *Pragmatic Programmer*, Evans's *Domain-Driven Design*, and Ousterhout's *A Philosophy of Software Design* — agree on far more than they disagree. Read together, they describe a single underlying discipline whose central concern is the management of **complexity** in software systems over time.

Software engineering fundamentals are the foundational principles that recur across all three books, the principles that distinguish professional software from one-off scripts. They are not the latest framework, not the latest methodology, and not tied to any particular language. They are the principles a programmer can rely on twenty years from now.

The recurring core is small:

1. **Complexity is the enemy.** All three books treat complexity — change amplification, cognitive load, and unknown unknowns — as the primary force to manage. Code is read more often than written; entropy accumulates; tactical shortcuts compound.
2. **Design is the lever.** Software design — the deliberate arrangement of modules, names, interfaces, and dependencies — is the primary tool for managing complexity.
3. **Names are load-bearing.** Code, classes, methods, and APIs are named in the language of the domain, and the words matter.
4. **Decay is a first-class concern.** Software rots, drift compounds, and small tactical decisions accumulate. Entropy must be fought actively, not denied.
5. **The reader matters more than the writer.** Code is for humans; comments and abstractions exist to communicate to the next reader.

## Core Content

### The three pillars of the canon

| Book | Year | Core contribution |
|------|------|-------------------|
| *The Pragmatic Programmer* (Hunt & Thomas) | 1999 (20th-anniversary ed. 2019) | A working philosophy: DRY, orthogonality, tracer bullets, broken-windows, design-by-contract, project glossary, pragmatic teams |
| *Domain-Driven Design* (Evans) | 2003 | A discipline for placing the domain at the centre of the design through ubiquitous language, bounded contexts, and a tactical building-block vocabulary (entities, value objects, aggregates) |
| *A Philosophy of Software Design* (Ousterhout) | 2018 | A theory of complexity: change amplification, cognitive load, unknown unknowns; deep modules vs. shallow modules; pull complexity downwards |

Each book is independently sufficient; the value of reading all three is the **convergent diagnosis** of the same disease (complexity, decay, misnamed code, wrong boundaries) and the **complementary treatments** they prescribe.

### The converging principles

#### 1. Complexity must be managed, not endured

All three books agree that the cost of software is overwhelmingly in change, not in first write. Ousterhout names the three faces of complexity explicitly: **change amplification** (a simple change touches many places), **cognitive load** (the developer must know many things to make a change), and **unknown unknowns** (the developer does not know what they do not know).

Hunt & Thomas tackle the same phenomenon through **orthogonality** (Tip 13: eliminate effects between unrelated things) and **DRY** (Tip 11: every piece of knowledge has a single, unambiguous, authoritative representation). Evans tackles it through **bounded contexts** (each context has a model that is internally consistent and free of contradictions). The three formulations are the same insight: complexity grows when unrelated things become coupled, when the same knowledge lives in multiple places, or when one model tries to satisfy multiple audiences.

#### 2. Names and language are the design

Evans's **ubiquitous language** and Hunt & Thomas's **project glossary** (Tip 54) are the same idea from different angles: the vocabulary of the code must be the vocabulary of the domain, and the vocabulary must be maintained as a single source of truth. Ousterhout's chapter on naming makes the same point at the unit level: names are a form of documentation, and a single bad name is harmless but a program full of poorly-named components is unusable.

#### 3. Boundaries matter

Evans: bounded contexts, with explicit relationships between them (shared kernel, customer/supplier, anti-corruption layer, conformist, separate ways).
Ousterhout: deep modules, with simple interfaces relative to powerful functionality.
Hunt & Thomas: orthogonality, decoupling, and the Law of Demeter (Tip 26).

All three say the same thing: **the boundary of a module is the most consequential design decision you make.** Get the boundary wrong and no amount of internal quality rescues you; get it right and complexity becomes tractable.

#### 4. Decay is real, and fighting it is the job

Software entropy, broken windows, dormant vs. active rot — these are the names Hunt & Thomas, Wikipedia, and the Wikipedia article all give to the same observable phenomenon: software degrades over time, even when nothing has changed. The books differ in metaphor (entropy vs. rot vs. broken windows) but agree on the prescription: invest in the codebase, fix the small things immediately, treat tactical shortcuts as technical debt with interest, do not be like the boiled frog.

#### 5. Code is for readers

Hunt & Thomas's Tip 10 ("it's both what you say and the way you say it"), Ousterhout's chapter on comments ("if someone says your code is not obvious, then it isn't"), Evans's insistence that the ubiquitous language must be used in conversations *and* in code — all three place the reader of the code as the primary audience.

### The principles that do not appear in the canon

The canon is also defined by what it does **not** say. None of the three books privileges a particular language, framework, IDE, or methodology. None of them argues for a particular SDLC (waterfall vs. agile vs. lean). None of them treats unit testing, type systems, or code review as the primary lever — they all are means to a deeper end. The fundamentals are orthogonal to fashion.

### How the principles interlock

The three books do not overlap so much as **layer**:

- **Ousterhout** answers "what is the goal?" (manage complexity) and "what is the unit?" (the module).
- **Evans** answers "how do you draw boundaries between units?" (bounded contexts, ubiquitous language).
- **Hunt & Thomas** answer "what is the daily practice?" (DRY, orthogonality, tracer bullets, broken windows, project glossary).

Read together, the operator gets a complete software-engineering discipline: a theory of complexity, a theory of boundaries, and a theory of practice.

## Key Insights

1. The three canonical texts converge on a single discipline: **complexity management through deliberate design.**
2. The recurring vocabulary — DRY, orthogonality, bounded context, ubiquitous language, deep modules, broken windows — are not independent ideas; they are different framings of the same anti-complexity program.
3. Software engineering fundamentals are the **layer below** frameworks, languages, and methodologies. They survive any of those changing.
4. The fundamentals are also **above** the level of style: consistent indentation does not save an architecture that does not understand its bounded contexts.
5. The fundamentals are operationalised through the operator's `grill-with-docs` skill — domain language is established during the grilling session itself, not only cited in code.

## Related Concepts

- [[Concepts/software-entropy]] — software entropy and broken windows as the first-order phenomenon the fundamentals exist to fight
- [[Concepts/deep-modules]] — Ousterhout's primary prescription for module design
- [[Concepts/ddd-bounded-context]] — Evans's primary prescription for boundary design
- [[Concepts/ddd-ubiquitous-language]] — Evans's primary prescription for naming and vocabulary
- [[Concepts/ddd-strategic-design]] — the larger-scale patterns Evans prescribes (context maps, shared kernels, anti-corruption layers)
- [[Concepts/ddd-tactical-patterns]] — the in-context building blocks (entities, value objects, aggregates, repositories, factories)
- [[Concepts/pragmatic-programmer-tips]] — the Quick-Reference table of practical rules drawn from Hunt & Thomas
- [[Entities/andrew-hunt-dave-thomas]] — authors of *The Pragmatic Programmer*
- [[Entities/eric-evans]] — author of *Domain-Driven Design*
- [[Entities/john-ousterhout]] — author of *A Philosophy of Software Design*

## References

- Raw Article: [[Raw/software-engineering-fundamentals-sources-2026-09-18]]
- Original sources: Hunt & Thomas (1999/2019); Evans (2003); Ousterhout (2018); Wikipedia *Software rot*; Martin Fowler, *Bounded Context* and *Ubiquitous Language*
