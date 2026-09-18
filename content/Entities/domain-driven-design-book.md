---
title: "Domain-Driven Design (Eric Evans)"
details: "Domain-Driven Design: Tackling Complexity in the Heart of Software, by Eric Evans (Addison-Wesley Professional, 2003). The canonical book that named and formalised Domain-Driven Design (DDD), a software design approach focused on modeling software to match a domain according to input from that domain's experts. The book's three pillars are ubiquitous language (a common rigorous language between developers and domain experts), strategic design (the discipline of drawing boundaries between bounded contexts), and tactical design (the within-context building blocks: entities, value objects, aggregates, repositories, factories, services, domain events). The book is one of three the operator has named as the canonical software-engineering reading list, alongside The Pragmatic Programmer and A Philosophy of Software Design."
tags:
  - software-engineering
  - reference
created: 2026-09-18
updated: 2026-09-18
type: entity
sources:
  - "[[Raw/software-engineering-fundamentals-sources-2026-09-18]]"
---

# Domain-Driven Design (Eric Evans)

**Source:** [[Raw/software-engineering-fundamentals-sources-2026-09-18]]
**Category:** Book / Reference
**Original publication:** Addison-Wesley Professional, 2003
**Author:** [[Entities/eric-evans]]

---

## Overview

*Domain-Driven Design: Tackling Complexity in the Heart of Software* is Eric Evans's 2003 book that named and formalised the discipline of Domain-Driven Design (DDD). Subtitled "Tackling Complexity in the Heart of Software", the book argues that the primary challenge of large software systems is complexity, and that the only sustainable response is to model the software to match the underlying domain, in close collaboration with domain experts, using a shared rigorous language.

The book is one of three the operator has named as the canonical software-engineering reading list, alongside Hunt & Thomas's *Pragmatic Programmer* and Ousterhout's *A Philosophy of Software Design*.

## Key Details

### Structure

The book is divided into four parts:

1. **Putting the Domain Model to Work** — the core thesis: complex domain code requires a domain model, an ubiquitous language, and tight feedback between the model and the code.
2. **The Building Blocks of a Model-Driven Design** — the tactical patterns: entities, value objects, domain events, aggregates, repositories, factories, services, modules.
3. **Refactoring Toward Deeper Insight** — the practice of distilling the model: breakthrough moments, making implicit concepts explicit, refactoring toward deeper insight.
4. **Strategic Design** — the system-level discipline: bounded contexts, context maps, subdomains (core/supporting/generic), large-scale structure, distillation.

The book's three pillars — **ubiquitous language**, **strategic design**, and **tactical design** — are distributed across the parts, with strategic design (Part IV) being the most influential and the most-cited contribution.

### Three pillars

- **Ubiquitous Language** — the common rigorous language between developers and domain experts, used in conversation and in code. See [[Concepts/ddd-ubiquitous-language]].
- **Strategic Design** — the system-level discipline of drawing boundaries, naming relationships, classifying subdomains. See [[Concepts/ddd-strategic-design]] and [[Concepts/ddd-bounded-context]].
- **Tactical Design** — the within-context building blocks: entities, value objects, aggregates, repositories, factories, services, domain events. See [[Concepts/ddd-tactical-patterns]].

### Reception

The book was difficult reading when first published (2003), and remains so; Vernon and others have written more accessible treatments. The strategic-design chapter (Part IV) is the most-cited contribution and the one that has most shaped the industry (it is the foundation of the microservices movement, of modular monolith design, and of most modern large-scale system design).

Critics argue that DDD requires a great deal of isolation and encapsulation to maintain the model as a useful construct, and Microsoft recommends DDD only for complex domains where the model provides clear benefits.

### Follow-on literature

- Vaughn Vernon, *Implementing Domain-Driven Design* (2013) — more accessible treatment; focuses on strategic design from the outset.
- Vaughn Vernon, *Domain-Driven Design Distilled* (2016) — a brief overview.
- Eric Evans, *Domain-Driven Design Reference* (2015) — a free PDF summary of definitions and pattern summaries.
- Wlaschin, *Domain Modeling Made Functional* (2018) — DDD applied in F#.
- Khononov, *Learning Domain-Driven Design* (2021).

### Status

The book is still the canonical reference. The 2015 DDD Reference PDF is freely available on domainlanguage.com. The book is one of the operator's named canonical reading list.

## Related Concepts

- [[Concepts/ddd-bounded-context]] — the strategic-design pattern that opens Part IV
- [[Concepts/ddd-ubiquitous-language]] — the foundational practice
- [[Concepts/ddd-strategic-design]] — Part IV of the book
- [[Concepts/ddd-tactical-patterns]] — Part II of the book
- [[Concepts/software-engineering-fundamentals]] — the umbrella
- [[Entities/eric-evans]] — author

## References

- Raw Article: [[Raw/software-engineering-fundamentals-sources-2026-09-18]]
- Original: <https://www.amazon.com/gp/product/0321125215/>
- Free DDD Reference PDF: <https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf>
