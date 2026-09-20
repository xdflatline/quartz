---
title: "DDD Strategic Design"
details: "The half of Domain-Driven Design (Evans, 2003) that operates above the level of any single bounded context: how an organisation draws boundaries between contexts, names the relationships between them, and aligns the team structure with the model. Strategic design is the book-level discipline: bounded contexts (with their ubiquitous languages), context maps showing how contexts relate, subdomains (core / supporting / generic), and the explicit patterns of integration (Partnership, Shared Kernel, Customer/Supplier, Conformist, Anti-Corruption Layer, Open-host Service, Published Language, Separate Ways). Strategic design is more important than tactical design: getting the boundaries right matters more than the choice of entity vs. value object."
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

# DDD Strategic Design

**Source:** [[Raw/software-engineering-fundamentals-sources-2026-09-18]] — Evans, *Domain-Driven Design*, Part IV; Wikipedia *Domain-driven design*; Martin Fowler.
**Category:** Architecture Pattern (system-level)
**Status:** Production-validated — primary lever for large-scale system design

---

## Overview

DDD divides into two halves:

- **Strategic design** — the system-level discipline. Where do the boundaries go? How do contexts relate? What is the core domain?
- **Tactical design** — the within-context discipline. How do we model entities, value objects, and aggregates inside a single context?

Both are part of the DDD canon, but the practitioner consensus — reinforced by Evans himself, Vernon, and the wider community — is that **strategic design matters more than tactical design**. Teams that get the boundaries right but disagree on entity vs. value object succeed; teams that obsess over tactical patterns while their boundaries are wrong fail.

Strategic design is the practice of making the large-scale decisions explicit: which contexts exist, what their ubiquitous languages are, how they integrate, and which is the **core domain** (the part of the system that justifies its existence). It is the answer to the question "what is this system?" — not "how is this module implemented?"

## Core Content

### The strategic-design toolkit

The strategic-design patterns can be grouped into four categories:

1. **Boundary patterns** — bounded context (with ubiquitous language), subdomain classification.
2. **Relationship patterns** — context map, partnership, shared kernel, customer/supplier, conformist, anti-corruption layer, open-host service, published language, separate ways.
3. **Core-domain patterns** — core domain (the part of the system that justifies its existence), supporting subdomain, generic subdomain, distilled core, segregated core.
4. **Large-scale structure patterns** — responsibility layers (separating the technical layers from the domain layers), knowledge level, pluggable component.

### Bounded context (recap)

The boundary within which a single, internally consistent domain model applies. Inside the boundary, the same word means the same thing; outside, it may mean something else. The most common reason for a boundary is human culture: different teams use different vocabularies. See [[Concepts/ddd-bounded-context]].

### Subdomain classification

Not all subdomains are equal. Evans distinguishes three kinds:

| Subdomain | What it is | Investment |
|-----------|------------|------------|
| **Core domain** | The part of the system that justifies its existence; what differentiates this product from competitors | Maximum investment: the best developers, the most rigorous design |
| **Supporting subdomain** | Necessary for the core to work, but not itself differentiating | Solid investment but not best-in-class |
| **Generic subdomain** | Could be bought off the shelf (authentication, billing, search) | Buy or build minimally; do not invest in differentiation |

The strategic discipline is to identify the core domain and **focus the best design effort there**. Generic subdomains are often outsourced (Stripe for billing, Auth0 for auth, Algolia for search) precisely because they are not where differentiation happens.

### Context maps and relationship patterns

Evans originally defined seven patterns for the relationships between contexts (with Wikipedia adding an eighth, *Big Ball of Mud*, as the pattern for when there are no real boundaries):

| Pattern | Direction | When to use |
|---------|-----------|-------------|
| **Partnership** | Bidirectional | Two teams succeed or fail together; coordinated planning |
| **Shared Kernel** | Bidirectional | A small, deliberately shared subset of the domain model |
| **Customer/Supplier** | Upstream / downstream | One team serves the other's needs; clear contracts |
| **Conformist** | Downstream conforms to upstream | Custom interface unlikely; translation cost too high |
| **Anti-Corruption Layer (ACL)** | Downstream isolates itself | Upstream model is unstable, poorly designed, or in vendor terms |
| **Open-host Service** | Upstream exposes a stable protocol | One subsystem integrates with many others |
| **Published Language** | Bidirectional, formal | Cross-industry interchange; a documented shared language as the medium |
| **Separate Ways** | No relationship | Integration cost not worth it; each context solves its own problem |
| **Big Ball of Mud** | Boundary around the entire mess | No real boundaries in a legacy system; at least make the boundary explicit |

The pattern's purpose is to **make the relationship between contexts explicit**. Implicit integration produces the kind of confusion Evans's bounded-context pattern exists to avoid.

### Distillation and segregation (managing the core)

Two further strategic patterns refine the core-domain concept:

- **Core domain** — the part of the system that justifies its existence. Must be the best-designed part of the system.
- **Distilled core** — the abstract core of the core domain, expressed as a small set of concepts. The distilled core is what the most talented designers work on.
- **Segregated core** — when parts of the core are mixed with other concerns, the core is separated (segregated) into its own bounded context.
- **Generic subdomain** — capabilities that exist in many systems; buy or build minimally.

### Why strategic matters more than tactical

> Strategic design matters more than tactical patterns. Getting your bounded contexts right is more important than debating Entity vs. Value Object. — Stackademic, *DDD in 20 Minutes*

The reason is operational: tactical patterns are local. A team can rename an entity from `Customer` to `CustomerAccount` next sprint without breaking the system. A wrong boundary, by contrast, may require a year of refactoring to fix — and during that year, the cost of every change is inflated.

### The decision order

The pragmatic order for a team adopting DDD:

1. **Identify the subdomains.** What are the major capabilities the system needs?
2. **Classify them.** Which are core, which are supporting, which are generic?
3. **Draw the bounded contexts.** Where do the languages diverge? Where do the teams live?
4. **Map the relationships.** Which patterns apply to each pair of contexts?
5. **Decide the core investment.** Where do the best designers spend their time?
6. **Then** design the tactical building blocks within each context.

Teams that start with tactical patterns ("should this be an entity or a value object?") without having done the strategic work are solving the wrong problem.

### Connection to other fundamentals

- [[Concepts/ddd-bounded-context]] — the unit of strategic design.
- [[Concepts/ddd-ubiquitous-language]] — what gives each bounded context its cohesion.
- [[Concepts/ddd-tactical-patterns]] — what goes *inside* a bounded context.
- [[Concepts/deep-modules]] — Ousterhout's prescription at the module scale is the same shape; strategic design applies it at the system scale.
- [[Concepts/software-engineering-fundamentals]] — strategic design is one of the named fundamentals.

### When NOT to use strategic design

Strategic design is **expensive**. Context maps, anti-corruption layers, and shared kernels are all ongoing maintenance. For a small CRUD application, the cost is not justified. Microsoft's recommendation: use DDD (and therefore strategic design) only for **complex domains** where the model provides clear benefits.

## Key Insights

1. **Strategic design is about boundaries.** Where do contexts begin and end? How do they relate?
2. **Strategic design matters more than tactical design.** Wrong boundaries are expensive to fix; wrong tactical patterns are cheap.
3. **Identify the core domain and invest the best design effort there.** Generic subdomains should be bought, not built.
4. **Make the relationships between contexts explicit.** Implicit integration produces confusion.
5. **Order matters.** Identify subdomains, classify them, draw boundaries, map relationships, then design tactically. Don't start with entity vs. value object.

## Related Concepts

- [[Concepts/ddd-bounded-context]]
- [[Concepts/ddd-ubiquitous-language]]
- [[Concepts/ddd-tactical-patterns]]
- [[Concepts/deep-modules]]
- [[Concepts/software-engineering-fundamentals]]

## References

- Raw Article: [[Raw/software-engineering-fundamentals-sources-2026-09-18]]
- Original sources: Eric Evans, *Domain-Driven Design* (2003), Part IV (Strategic Design); Vaughn Vernon, *Implementing Domain-Driven Design* (2013); Wikipedia *Domain-driven design*; Martin Fowler, *Bounded Context*; Kong To, *Domain-Driven Design — The Strategic Design*
