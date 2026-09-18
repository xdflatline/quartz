---
title: "Software Engineering Fundamentals — Source Bundle (Pragmatic Programmer, DDD, Wikipedia Software Rot, PoSD Review)"
details: "Verbatim source excerpts for the Software Engineering Fundamentals research index. Combines the canonical software-engineering reference material into a single Raw page: the full Pragmatic Programmer tip table (Hunt & Thomas, 1999, 20th-anniversary 2019), the Wikipedia Software Rot article (covering software entropy and broken-windows theory), Matt Duck's book review of A Philosophy of Software Design (Ousterhout, 2018), and Martin Fowler's canonical write-ups of Bounded Context and Ubiquitous Language (the two most-cited DDD patterns). Each section preserves the original phrasing so that the synthesised concept pages can be cross-checked against the source."
tags:
  - raw
  - software-engineering
  - philosophy
source: "https://github.com/HugoMatilla/The-Pragmatic-Programmer ; https://en.wikipedia.org/wiki/Software_rot ; https://www.mattduck.com/2021-04-a-philosophy-of-software-design ; https://martinfowler.com/bliki/BoundedContext.html ; https://martinfowler.com/bliki/UbiquitousLanguage.html ; https://en.wikipedia.org/wiki/Domain-driven_design"
created: 2026-09-18
updated: 2026-09-18
type: raw
---

# Software Engineering Fundamentals — Source Bundle

> Verbatim source material for the [[Research/software-engineering-fundamentals]] research index.
> Composed of excerpts from four canonical software-engineering references:
>
> 1. **The Pragmatic Programmer** (Hunt & Thomas, 1999; 20th-anniversary ed. 2019)
> 2. **Software Rot** (Wikipedia) — covering software entropy & broken-windows theory
> 3. **A Philosophy of Software Design** (Ousterhout, 2018) — reviewed in detail by Matt Duck
> 4. **Domain-Driven Design** (Evans, 2003) — strategic-design patterns via Martin Fowler's write-ups of Bounded Context and Ubiquitous Language, plus the Wikipedia overview of DDD.

---

## 1. The Pragmatic Programmer (Hunt & Thomas)

**Source:** Hugo Matilla's summary on GitHub, [HugoMatilla/The-Pragmatic-Programmer](https://github.com/HugoMatilla/The-Pragmatic-Programmer), which reproduces the full Quick Reference from *The Pragmatic Programmer*, Andrew Hunt & David Thomas, Addison Wesley (1999; 20th Anniversary Edition 2019). Copyright 2000 Addison Wesley Longman, Inc.

### Software Entropy (Chapter 1, Section 2)

> One broken window, left unrepaired for any substantial length of time, instills in the inhabitants of the building a sense of abandonment—a sense that the powers that be don't care about the building. So another window gets broken. People start littering. Graffiti appears. Serious structural damage begins. In a relatively short space of time, the building becomes damaged beyond the owner's desire to fix it, and the sense of abandonment becomes reality.

**Tip 4: Don't Live with Broken Windows**
Don't mess up the carpet when fixing the broken window.

### The Evils of Duplication (Chapter 2, Section 7)

> The problem arises when you need to change a representation of things that are across all the code base.
> Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

**Tip 11: DRY—Don't Repeat Yourself**

Types of duplication:

- **Imposed duplication** Developers feel they have no choice—the environment seems to require duplication.
- **Inadvertent duplication** Developers don't realize that they are duplicating information.
- **Impatient duplication** Developers get lazy and duplicate because it seems easier.
- **Interdeveloper duplication** Multiple people on a team (or on different teams) duplicate a piece of information.

### Orthogonality (Chapter 2, Section 8)

> Two or more things are orthogonal if changes in one do not affect any of the others. Also called *cohesion*. Write "shy" code.

**Tip 13: Eliminate Effects Between Unrelated Things**

### Tracer Bullets (Chapter 2, Section 10)

> In new projects, your user's requirements may be vague. Use of new algorithms, techniques, languages, or libraries unknowns will come. An environment will change over time before you are done.
> We're looking for something that gets us from a requirement to some aspect of the final system quickly, visibly, and repeatably.

**Tip 15: Use Tracer Bullets to Find the Target**

### Domain Languages (Chapter 2, Section 12)

**Tip 17: Program Close to the Problem domain**

### Design by Contract (Chapter 4, Section 21)

Hunt & Thomas's framing of Eiffel-style DbC: each routine is a contract between caller and callee; preconditions, postconditions, and invariants are checked at runtime.

### Decoupling and the Law of Demeter (Chapter 5, Section 26)

> An object's method should call only methods belonging to:
>
> - Itself
> - Any parameters passed in
> - Objects it creates
> - Component objects

### Tips 30–46 (selected, from the Quick Reference)

**Tip 30: Transform Programming into Writing Code**

**Tip 33: Refactor Early, Refactor Often**

**Tip 37: Design with Contracts** *(also known as Design by Contract)*

**Tip 38: Use Assertions to Prevent Impossible Situations**

**Tip 39: Finish What You Start**

**Tip 42: Ubiquitous Automation**

**Tip 43: Ruthless Testing**

**Tip 44: It's All Writing** — "Write documents as you would write code."

**Tip 53: When it Has to Work, Don't Trust Your Instincts**

**Tip 54: Use a Project Glossary**
> Create and maintain a single source of all the specific terms and vocabulary for a project.

**Tip 55: Don't Think Outside the Box – Find the Box**
> When faced with an impossible problem, identify the real constraints. Ask yourself: "Does it have to be done this way? Does it have to be done at all?"

**Tip 60: Organize Teams Around Functionality**

**Tip 62: Test Early. Test Often. Test Automatically**

**Tip 65: Test State Coverage, Not Code Coverage**

**Tip 70: Sign Your Work**
> Craftsmen of an earlier age were proud to sign their work. You should be, too.

### Summary themes

The Pragmatic Programmer distils a working philosophy:

1. **Pragmatic philosophy** — care about your craft, think about your work, take responsibility, provide options rather than excuses, fight entropy, invest in your knowledge portfolio.
2. **Pragmatic approach** — DRY (don't repeat yourself), orthogonality, reversibility, tracer bullets, prototyping, domain languages, estimating.
3. **Basic tools** — plain text, shells, source-code control, debugging, text manipulation, code generators.
4. **Pragmatic paranoia** — design by contract, dead programs tell no lies, assertive programming, balanced resource management.
5. **Bend or break** — decoupling, metaprogramming, temporal coupling, blackboards.
6. **While coding** — program deliberately (not by coincidence), algorithm speed, refactoring, code that's easy to test, avoid evil wizards.
7. **Before the project** — avoid the requirements pit, work on impossible puzzles, not until you're ready, avoid the specification trap, circles and arrows.
8. **Pragmatic projects** — pragmatic teams, ubiquitous automation, ruthless testing, it's all writing, great expectations.

---

## 2. Software Rot (Wikipedia)

**Source:** [Wikipedia, *Software rot*](https://en.wikipedia.org/wiki/Software_rot). Retrieved 2026-09-18.

> **Software rot** ( **bit rot**, **code rot**, **software erosion**, **software decay**, or **software entropy**) is the degradation, deterioration, or loss of the use or performance of software over time.

The *Jargon File*, a compendium of hacker lore, defines "bit rot" as a jocular explanation for the degradation of a software program over time even if "nothing has changed"; the idea behind this is almost as if the bits that make up the program were subject to radioactive decay.

### Causes

Several factors are responsible for software rot, including changes to the environment in which the software operates, degradation of compatibility between parts of the software itself, and the emergence of bugs in unused or rarely used code.

- **Environment change.** When changes occur in the program's environment, particularly changes which the designer of the program did not anticipate, the software may no longer operate as originally intended.
- **Onceability.** Information architect Jonas Söderström has named this concept *onceability*, and defines it as "the quality in a technical system that prevents a user from restoring the system, once it has failed".
- **Unused code.** Infrequently used portions of code, such as document filters or interfaces designed to be used by other programs, may contain bugs that go unnoticed.
- **Rarely updated code.** When a program contains multiple parts which *function at arm's length* from one another, failing to consider how changes to one part affect the others may introduce bugs.
- **Online connectivity.** Modern commercial software often connects to an online server for license verification and accessing information. If the online service powering the software is shut down, it may stop working.

### Classification

Software rot is usually classified as being either "dormant rot" or "active rot".

- **Dormant rot.** Software that is not currently being used gradually becomes unusable as the remainder of the application changes.
- **Active rot.** Software that is being continuously modified may lose its integrity over time if proper mitigating processes are not consistently applied. […] In practice, adding new features may be prioritized over updating documentation; without documentation, however, it is possible for specific knowledge pertaining to parts of the program to be lost. […] Active software rot slows once an application is near the end of its commercial life and further development ceases.

### Broken Windows (Hunt & Thomas reference)

> "broken windows as a metaphor for avoiding software entropy in software development" — Hunt & Thomas, *The Pragmatic Programmer*, pp. 4–6.

---

## 3. A Philosophy of Software Design (Ousterhout, 2018)

**Source:** Matt Duck, [*A philosophy of software design*](https://www.mattduck.com/2021-04-a-philosophy-of-software-design), 2021-04-07. Detailed book-review notes from John Ousterhout's 2018 book.

### Summary

> When building software systems, the core challenge is managing **complexity**. Complexity makes it more difficult for a programmer to understand and change software, it increases the rate of errors, it slows development velocity, and has other negative affects.
>
> Software design is one of the key tools for managing complexity. Ousterhout discusses the different types and causes of complexity, and then various software design considerations and their relationship to complexity — patterns, antipatterns, questions to ask, etc.

### The Nature of Complexity

> Ultimately, complexity makes it more expensive to modify a program: changes are more difficult, take longer, and are more likely to introduce errors to a program.

Ousterhout identifies three general ways that complexity manifests itself:

1. **Change amplification** — where a seemingly simple change requires code modifications in many different places.
2. **Cognitive load** — where a developer needs to know a large number of things in order to complete a task.
3. **Unknown unknowns** — where it's unclear what to do, or whether a proposed solution will even work.

> The overall complexity of a system can be determined by the complexity of each part, weighted by the fraction of time developers spend working on that part. **If you isolate complexity in a place where it will never be seen, then that's almost as good as eliminating it entirely.**

### Causes of Complexity

1. **Dependencies** between software components, which can lead to change amplification and a high cognitive load.
2. **Obscurity** — when important information is not obvious. This creates unknown unknowns, and also contributes to cognitive load.

### Tactical vs Strategic Programming

> Ousterhout advocates for a strategic approach to software development, rather than a wholly tactical approach. This essentially just means ongoing, regular investment of some of your development time towards system design, rather than just working code.
>
> One pitfall is that complexity in software development is incremental. A single shortcut or tactical decision that adds complexity won't have much impact, but small decisions can accumulate to dozens or hundreds of things that do have an impact. Then refactoring becomes a big task that you can't easily schedule with the business, so you look for quick patches, and this creates yet more complexity, which requires more patches, and so forth.
>
> Once a codebase gets complex enough, it is nearly impossible to fix, and you will probably pay high development costs for the rest of its life.

> "Agile" and similar approaches to software development tend to be focused on small, tactical changes. It's easy in this environment to forget about investing in the codebase, especially in startup companies that have a lot of pressure to deliver features.

### Deep Modules

> A software system is usually decomposed into a collection of modules that are relatively independent. Modules inevitably have dependencies between them — they work together by calling each other, and therefore must know about each other. In order to manage these dependencies, we think about a module in two parts: an *interface* (what the module does), and an *implementation* (how it does it).
>
> The idea of *abstraction* is closely related to modules. An abstraction is a simplified view of an entity which omits unimportant details, making it easier for us to think about and manipulate complex things.
>
> Ousterhout argues that the best modules are those that provide powerful functionality, but have a simple interface. He describes these as *deep* modules, in contrast to *shallow* modules, which have a complex interface but not much functionality, thereby not hiding significant complexity.

> The file I/O interface provided by Unix is a good example of a deep interface — the API only has a few system calls (`open`, `read`, `write`, `seek`, `close`), but hides a huge amount of complexity around implementation of files, directories, permissions, concurrent access, etc.

> Ousterhout says that the conventional wisdom is to write *small* components (keeping the LoC low in each method) rather than deep components, but this results in large numbers of shallow classes and methods, which add to overall system complexity.

### Other design rules

- **Write code for the reader, not the writer.** "If someone says your code is not obvious, then it isn't."
- **General-purpose modules are deeper.** "If you reduce the number of methods in an API without reducing its overall capabilities, then you are probably creating more general-purpose methods."
- **Pass-through variables add complexity.** They force intermediate methods to be aware of their existence.
- **Pass-through methods are shallow and add complexity.** Often an indication of confusion over the division of responsibility between modules or classes.
- **Pull complexity downwards.** It's more important for a module to have a simple interface than a simple implementation.
- **Define errors out of existence.** "Exception handling is one of the worst sources of complexity in software systems."
- **Comments should describe things that aren't obvious from the code.** "Developers should be able to understand the abstraction provided by a module without reading any code other than its externally visible declarations."
- **Naming is important.** Good names are precise, consistent, and not overly-general.
- **Consistency is important.** Minimises complexity because it provides cognitive leverage.
- **Implementation inheritance increases complexity.** Composition can be a less-complex alternative.
- **Event-driven programming makes code less obvious.** It is hard to follow the flow of control.
- **Design it twice.** Multiple options for each major design decision yields a better result.

### TDD

> "The problem with test-driven development is that it focuses on getting specific features working, rather than finding the best design." Ousterhout argues that the unit of development should be abstractions rather than features.

---

## 4. Domain-Driven Design (Evans, 2003) — via Martin Fowler and Wikipedia

### Wikipedia overview

**Source:** [Wikipedia, *Domain-driven design*](https://en.wikipedia.org/wiki/Domain-driven_design). Retrieved 2026-09-18.

> **Domain-driven design** (DDD) is a software design approach that focuses on modeling software to match a domain according to input from that domain's experts. DDD is against the idea of having a single unified model; instead it divides a large system into bounded contexts, each of which have their own model.

> Under domain-driven design, the structure and language of software code (class names, class methods, class variables) should match the business domain. For example: if software processes loan applications, it might have classes like "loan application", "customers", and methods such as "accept offer" and "withdraw".

Three pillars: **ubiquitous language**, **strategic design**, **tactical design**.

### Kinds of models (from Wikipedia)

- **Entity** — defined not by its attributes, but its identity. (Airlines assign a unique number to seats on every flight.)
- **Value object** — immutable, contains attributes, no conceptual identity. (Business cards.)
- **Domain event** — something that happened in the past. Domain experts care about it.
- **Aggregate** — cluster of entities and value objects treated as a single unit for data changes. Objects outside the aggregate are allowed to hold references to the root but not to any other object of the aggregate. The aggregate root checks the consistency of changes.
- **Repository** — object with methods for retrieving domain objects from a data store.
- **Factory** — object with methods for directly creating domain objects.
- **Service** — when part of a program's functionality does not conceptually belong to any object.

### Event types

- **Domain events** — important occurrences within a specific business domain; restricted to a bounded context; vital for preserving business logic; lighter payloads.
- **Integration events** — communicate changes across different bounded contexts; ensure data consistency throughout the entire system; more complex payloads.

### Context Mapping patterns (Evans)

- **Partnership** — "forge a partnership between the teams in charge of the two contexts. Institute a process for coordinated planning of development and joint management of integration."
- **Shared Kernel** — "Designate with an explicit boundary some subset of the domain model that the teams agree to share. Keep this kernel small."
- **Customer/Supplier Development** — "Establish a clear customer/supplier relationship between the two teams."
- **Conformist** — "Eliminate the complexity of translation [...] choosing conformity enormously simplifies integration."
- **Anticorruption Layer** — "Create an isolating layer to provide your system with functionality of the upstream system in terms of your own domain model."
- **Open-host Service** — "a protocol that gives access to your subsystem as a set of services."
- **Published Language** — "a well-documented shared language that can express the necessary domain information as a common medium of communication."
- **Separate Ways** — "a bounded context [with] no connection to the others at all, allowing developers to find simple, specialized solutions within this small scope."
- **Big Ball of Mud** — "a boundary around the entire mess" when there are no real boundaries to be found when surveying an existing system.

### Martin Fowler — Bounded Context

**Source:** [Martin Fowler, *Bounded Context*](https://martinfowler.com/bliki/BoundedContext.html), 15 January 2014.

> Bounded Context is a central pattern in Domain-Driven Design. It is the focus of DDD's strategic design section which is all about dealing with large models and teams. DDD deals with large models by dividing them into different Bounded Contexts and being explicit about their interrelationships.
>
> DDD is about designing software based on models of the underlying domain. A model acts as a *Ubiquitous Language* to help communication between software developers and domain experts. It also acts as the conceptual foundation for the design of the software itself — how it's broken down into objects or functions. To be effective, a model needs to be unified — that is to be internally consistent so that there are no contradictions within it.
>
> As you try to model a larger domain, it gets progressively harder to build a single unified model. Different groups of people will use subtly different vocabularies in different parts of a large organization. The precision of modeling rapidly runs into this, often leading to a lot of confusion. Typically this confusion focuses on the central concepts of the domain.
>
> In those younger days we were advised to build a unified model of the entire business, but DDD recognizes that we've learned that "total unification of the domain model for a large system will not be feasible or cost-effective". So instead DDD divides up a large system into Bounded Contexts, each of which can have a unified model — essentially a way of structuring Multiple Canonical Models.
>
> Various factors draw boundaries between contexts. Usually the dominant one is human culture, since models act as Ubiquitous Language, you need a different model when the language changes. You also find multiple contexts within the same domain context, such as the separation between in-memory and relational database models in a single application. This boundary is set by the different way we represent models.

### Martin Fowler — Ubiquitous Language

**Source:** [Martin Fowler, *Ubiquitous Language*](https://martinfowler.com/bliki/UbiquitousLanguage.html), 31 October 2006.

> Ubiquitous Language is the term Eric Evans uses in *Domain Driven Design* for the practice of building up a common, rigorous language between developers and users. This language should be based on the Domain Model used in the software — hence the need for it to be rigorous, since software doesn't cope well with ambiguity.
>
> Evans makes clear that using the ubiquitous language in conversations with domain experts is an important part of testing it, and hence the domain model. He also stresses that the language (and model) should evolve as the team's understanding of the domain grows.
>
> By using the model-based language pervasively and not being satisfied until it flows, we approach a model that is complete and comprehensible, made up of simple elements that combine to express complex ideas.
>
> Domain experts should object to terms or structures that are awkward or inadequate to convey domain understanding; developers should watch for ambiguity or inconsistency that will trip up design. — Eric Evans

---

## 5. The grill-with-docs skill

The operator (0x1d) has retained that this body of work should be approached through the `grill-with-docs` skill: a structured grilling session that establishes a shared domain language between the assistant and the operator before diving into implementation work. The intent is that concepts like *bounded context*, *ubiquitous language*, *deep modules*, *broken windows*, and *DRY* should be operationalised during grilling rather than only cited.
