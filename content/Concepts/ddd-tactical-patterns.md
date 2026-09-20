---
title: "DDD Tactical Patterns"
details: "The within-context building blocks of Domain-Driven Design (Evans, 2003): entities (objects defined by identity, not attributes), value objects (immutable objects defined by their attributes, with no conceptual identity), aggregates (clusters of entities and value objects treated as a single unit for data changes, with a single root enforcing consistency), repositories (objects that retrieve domain objects from a data store), factories (objects that create domain objects), services (operations that don't belong to any object), and domain events (things that happened in the past that domain experts care about). Tactical patterns are the in-context vocabulary; the more important half of DDD is strategic design (boundaries, contexts, ubiquitous language)."
tags:
  - concept
  - software-engineering
  - architecture-pattern
created: 2026-09-18
updated: 2026-09-18
type: concept
sources:
  - "[[Raw/software-engineering-fundamentals-sources-2026-09-18]]"
---

# DDD Tactical Patterns

**Source:** [[Raw/software-engineering-fundamentals-sources-2026-09-18]] — Evans, *Domain-Driven Design*, Part II; Wikipedia *Domain-driven design*; Vaadin and DZone summaries.
**Category:** Architecture Pattern (within-context)
**Status:** Production-validated — the tactical vocabulary of DDD

---

## Overview

DDD's tactical patterns are the **building blocks used inside a single bounded context** to express the domain model in code. They are the vocabulary of class names and method names that the ubiquitous language is translated into.

The full tactical vocabulary includes:

- **Entity** — object defined by its identity, not its attributes.
- **Value object** — immutable object defined by its attributes, with no conceptual identity.
- **Aggregate** — a cluster of entities and value objects treated as a single unit for data changes.
- **Aggregate root** — the single entity that controls access to the rest of the aggregate.
- **Repository** — object that retrieves domain objects from a data store.
- **Factory** — object that creates domain objects.
- **Service** — operation that does not conceptually belong to any object.
- **Domain event** — something that happened in the past that domain experts care about.
- **Module** — a named container for related domain objects.

These are not "patterns to choose between." They are names for the kinds of objects you will inevitably create, with strong defaults attached. A `Customer` is usually an entity. A `Money` is usually a value object. A `Cart` is usually an aggregate with a single root. The patterns exist so the conversation can be precise.

Evans himself and the wider community emphasise: **tactical patterns matter less than strategic design.** A team that has the boundaries right but argues about entity vs. value object will succeed; a team that has the boundaries wrong but uses the perfect tactical vocabulary will fail. Tactical patterns are local; boundaries are system-level.

## Core Content

### Entity

> **Entity** — an object defined not by its attributes, but its identity. — Wikipedia

Example: most airlines assign a unique number to every seat on every flight. The seat's identity is its number; the attributes (location, class, occupied?) can change but the seat remains "the same seat".

Implementation: an entity has a stable ID, equality is by ID (not by attributes), and two entities with the same attributes but different IDs are different objects.

### Value object

> **Value object** — an immutable object that contains attributes but has no conceptual identity. — Wikipedia

Example: when people exchange business cards, they care about the information on the card (attributes) rather than trying to distinguish between each unique card. If two business cards have the same name, title, phone, and email, they are interchangeable.

Implementation: a value object has no ID; equality is by attribute comparison; value objects are immutable; if you want to "change" a value object, you create a new one.

The tactical default: prefer value objects over entities where possible. Value objects are simpler (no identity management, no mutable state), safer (immutable), and often more expressive (a `Money` is more meaningful than two related decimals).

### Aggregate

> **Aggregate** — a cluster of entities and value objects that are treated as a single unit for data changes. Every aggregate has a root entity (the Aggregate Root) that controls access to everything inside. — Wikipedia / Stackademic

Example: a car is an aggregate of several other objects (engine, brakes, headlights). The driver does not individually control each wheel; they drive the car. The aggregate root (the car) checks the consistency of changes inside the aggregate.

Tactical rules:

- **One aggregate root.** Every aggregate has exactly one entity designated as the root; references from outside the aggregate must go through the root.
- **Atomic consistency boundary.** All changes inside an aggregate are committed atomically; changes across aggregates are not.
- **No cross-aggregate transactions in the strong sense.** Different aggregates are eventually consistent.
- **Small aggregates.** Big aggregates mean big consistency boundaries, which means contention and slow operations. Default to small.

### Repository

> **Repository** — an object with methods for retrieving domain objects from a data store (e.g. a database). — Wikipedia

A repository's interface is in the domain language (`Customers.findByEmail(email)`), not in the storage technology (`SELECT * FROM customers WHERE email = ?`). The repository hides the persistence mechanism behind a domain-shaped interface.

One repository per aggregate root, not per entity. The aggregate is the unit of retrieval; partial aggregates are usually a smell.

### Factory

> **Factory** — an object with methods for directly creating domain objects. — Wikipedia

Used when the construction of an object is non-trivial — when the construction logic itself encodes domain knowledge. The factory may encapsulate invariant enforcement, default values, or complex assembly.

The most common case is aggregate construction: building an aggregate requires assembling the root, the value objects, and the initial state, and a factory encapsulates that.

### Service

> **Service** — when part of a program's functionality does not conceptually belong to any object, it is typically expressed as a service. — Wikipedia

A service is a stateless operation in the domain language. It is named after an activity (`TransferMoney`, `ApproveLoan`), not after an entity.

Tactical test: if the operation would naturally be a method on an entity, put it there. If it spans multiple aggregates, it is a service.

### Domain events

> **Domain event** — an event that domain experts care about. — Wikipedia

> **Domain events** signify important occurrences within a specific business domain. These events are restricted to a bounded context and are vital for preserving business logic. Typically, domain events have lighter payloads, containing only the necessary information for processing. — Yan Cui (via Wikipedia)

Examples: `OrderPlaced`, `PaymentReceived`, `LoanApproved`. Domain events are past-tense (they happened) and named in the ubiquitous language.

Yan Cui's distinction:

- **Domain events** — within a single bounded context; lighter payload; clear semantic.
- **Integration events** — across bounded contexts; richer payload; sometimes over-communicating for safety.

### Module

A **module** in DDD is a named container for related domain objects. Its purpose is **low coupling and high cohesion**: the names of modules reflect the ubiquitous language, and the dependencies between modules follow the same direction as the dependencies in the domain.

The tactical test: a module name should be a noun in the ubiquitous language, not a verb or a technical term. `Orders`, `Billing`, `Shipping` — not `OrderHandlers`, `BillingLogic`, `ShippingServices`.

### The decision order

Practitioners converge on this order:

1. **Identify the aggregate.** What is the unit of consistency? What is the root?
2. **Identify the value objects.** What state is immutable? What is defined by attributes?
3. **Identify the entities.** What has identity? What changes over time?
4. **Identify the events.** What do domain experts care about that already happened?
5. **Identify the services.** What operations span aggregates?
6. **Identify the repositories.** How do aggregates get retrieved?
7. **Identify the factories.** Where is construction non-trivial?

The order matters because the aggregate root is the unit of retrieval and consistency; everything else is sized to fit inside it.

### Connection to other fundamentals

- [[Concepts/ddd-bounded-context]] — tactical patterns operate *inside* a single bounded context.
- [[Concepts/ddd-ubiquitous-language]] — the tactical class names are drawn from the ubiquitous language.
- [[Concepts/ddd-strategic-design]] — strategic design is more important than tactical patterns.
- [[Concepts/deep-modules]] — a well-modelled aggregate is a deep module: small public interface, rich internal model.
- [[Concepts/software-engineering-fundamentals]] — tactical patterns are one of the named fundamentals.

### When NOT to use

Tactical patterns — especially aggregates and domain events — are expensive to retrofit. They are most valuable when the domain is complex enough to justify the discipline. For trivial CRUD applications, the tactical vocabulary is overhead.

## Key Insights

1. **Tactical patterns are the in-context vocabulary.** They give precise names to the kinds of objects you create.
2. **Strategic matters more than tactical.** Get the boundaries right; argue about entity vs. value object later.
3. **Prefer value objects over entities where possible.** Value objects are simpler, safer, and often more expressive.
4. **Aggregates are small and bounded.** One root, one atomic consistency boundary, no cross-aggregate strong transactions.
5. **Names come from the ubiquitous language.** `OrderPlaced`, not `OrderCreatedEvent`.

## Related Concepts

- [[Concepts/ddd-bounded-context]]
- [[Concepts/ddd-ubiquitous-language]]
- [[Concepts/ddd-strategic-design]]
- [[Concepts/deep-modules]]
- [[Concepts/software-engineering-fundamentals]]

## References

- Raw Article: [[Raw/software-engineering-fundamentals-sources-2026-09-18]]
- Original sources: Eric Evans, *Domain-Driven Design* (2003), Parts II–III; Vaughn Vernon, *Implementing Domain-Driven Design* (2013); Wikipedia *Domain-driven design*; Vaadin *DDD Part 2: Tactical Domain-Driven Design*; Stackademic *DDD in 20 Minutes*
