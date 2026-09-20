---
title: "Deep Modules (Ousterhout)"
details: "A module design principle from John Ousterhout's A Philosophy of Software Design (2018): the best modules provide powerful functionality behind a simple interface, hiding substantial complexity from the caller. A deep module contrasts with a shallow module, which exposes a complex interface relative to the functionality it provides. The Unix file I/O API (open/read/write/seek/close) is the canonical example of a deep module; a one-line wrapper around a one-line function is the canonical example of a shallow one. The principle is one of the operator's named software-engineering fundamentals."
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

# Deep Modules (Ousterhout)

**Source:** [[Raw/software-engineering-fundamentals-sources-2026-09-18]] — Matt Duck's detailed review of Ousterhout's *A Philosophy of Software Design*, 2018.
**Category:** Architecture Pattern (module design)
**Status:** Proposed best practice with strong community traction (and known critics)

---

## Overview

A **deep module** is a module that hides a great deal of complexity behind a simple interface. A **shallow module** is one whose interface is not much simpler than its implementation. The principle, named and formalised by John Ousterhout in *A Philosophy of Software Design* (2018), is one of the strongest cross-language prescriptions in the software-engineering canon: the best modules hide the most while exposing the least.

The canonical example is the Unix file I/O API: five system calls (`open`, `read`, `write`, `seek`, `close`) hide enormous internal complexity — filesystems, directories, permissions, concurrent access, buffering, crash recovery, network filesystems, journaling, and so on. The caller does not see any of this. By contrast, a typical OOP wrapper class that exposes one method per backing function — and whose method signatures are nearly identical to the underlying implementation — is shallow.

The principle is more than aesthetic. A deep module **reduces cognitive load** (the caller needs to know less) and **limits change amplification** (changes inside the module do not affect callers). It is one of the operator's named software-engineering fundamentals.

## Core Content

### Definition (Ousterhout via Matt Duck)

> Ousterhout argues that the best modules are those that provide powerful functionality, but have a simple interface. He describes these as *deep* modules, in contrast to *shallow* modules, which have a complex interface but not much functionality, thereby not hiding significant complexity.

A software system is decomposed into modules that are relatively independent. Each module has two parts: an **interface** (what the module does, what the caller needs to know) and an **implementation** (how it does it). An **abstraction** is a simplified view of an entity that omits unimportant details.

The depth of a module is roughly the ratio of capability to interface size. A Unix I/O module: huge capability, tiny interface → very deep. A typical OOP data-class with one method per field: small capability, large interface → very shallow.

### The visual

```
   DEEP MODULE                        SHALLOW MODULE
  ┌────────────┐                    ┌────────────┐
  │            ├─────► Interface   │            ├─────► Interface
  ├────────────┤                    ├────────────┤
  │            │                    │            │
  │            │                    │            │
  │            │                    │            │
  │            ├─────►              ├────────────┤
  │            │  Implementation    │            ├─────►
  │            │                    │            │  Implementation
  │            │                    │            │
  │            │                    │            │
  └────────────┘                    └────────────┘
```

A deep module has a small interface relative to a large implementation. A shallow module has a large interface relative to a small implementation.

### Examples

| Module | Interface | Implementation | Depth |
|--------|-----------|----------------|-------|
| Unix file I/O | 5 syscalls | Filesystems, permissions, caching, locking, journaling, network FS | Very deep |
| `git`'s porcelain | `add`, `commit`, `push`, `pull`, ... | Object database, packs, refs, index, hooks, merge algorithms, network protocols | Deep |
| A typical "Manager" wrapper class | `getThing`, `setThing`, `getAllThings`, `addThing`, `removeThing`, ... | Direct field access on an internal collection | Shallow |
| Java I/O streams | Many overlapping `Reader`/`Writer`/`InputStream`/`OutputStream` classes, each with small additions | Mostly direct field reads | Shallow (commonly cited) |

### The rule and its motivation

> If you reduce the number of methods in an API without reducing its overall capabilities, then you are probably creating more general-purpose methods. — Ousterhout

The motivation is operational: complexity in software compounds. A single shallow module is harmless; a system of shallow modules means every caller carries the cognitive load of every interface. By contrast, a system of deep modules means each caller's cognitive load is bounded by the public surface of the modules they use.

This is Ousterhout's **three faces of complexity** in operation:

- **Change amplification** is reduced: a deep module can change its implementation without affecting callers.
- **Cognitive load** is reduced: the caller only needs to know the small interface.
- **Unknown unknowns** are reduced: the implementation details that the caller might worry about are hidden.

### Shallow-module antipatterns

Drawing from Ousterhout and the practitioner literature:

- **Pass-through methods.** Methods that exist only to forward to another method with a similar signature. Indication of confusion over the division of responsibility between modules. (Decorators are sometimes shallow pass-throughs.)
- **Pass-through variables.** Variables that intermediate methods must accept and forward even though those methods have no use for them. Force every layer in between to know about them. Ousterhout's preferred fix is the **context object** — a single object that holds state shared across the system.
- **Implementation inheritance.** Creates dependencies between the parent class and each subclass, results in information leakage between the parent and child, and makes it hard to modify one class without looking at the other. Composition can be a less-complex alternative.
- **"Classitis."** Decomposition of a routine into many small functions for the sake of "easier to read" or to lower cyclomatic-complexity scores, when those functions end up on the public API.
- **Event-driven programming** in excess: the flow of control becomes hard to follow because handler invocation depends on which handlers were registered at runtime.
- **Moving complexity upward** (instead of downward). Configuration parameters as a way of pushing the burden of choosing a value onto the caller, rather than computing a reasonable default internally.

### Critique

The principle has known critics. Path-Sensitive (a blog review): Ousterhout's specific instance of the principle in Java is misapplied; advice derived from "deep modules" is sometimes unreliable. The general direction — prefer simple interfaces and powerful functionality — survives the critiques, but the specific implementation rules (e.g. "comments should not exist when they describe implementation") are debated.

### How to write deeper modules

| Move | Effect |
|------|--------|
| Reduce the number of methods in the API | Smaller interface, more capability per method |
| Default the values that callers would otherwise have to pass | Pulls configuration complexity downward |
| Compute rather than ask | `retry_interval = measured_rtt * factor` is better than `retry_interval = config.retry_interval_ms` |
| Hide library complexity behind a domain wrapper | A leaky abstraction becomes a clean abstraction |
| Combine related operations into a single method | Replaces many narrow methods with one general-purpose one |
| Use composition over inheritance | Limits information leakage across the boundary |
| Pull exception handling into the module | Defines errors out of existence, raises fewer exceptions to callers |
| Make the abstract type match its purpose, not its storage | `Money` rather than `Decimal` |

### Connection to software-engineering fundamentals

- [[Concepts/software-engineering-fundamentals]] — the umbrella; deep modules is one of the named fundamentals.
- [[Concepts/software-entropy]] — deep modules are a primary defence against entropy because they limit the surface area that must be kept consistent.
- [[Concepts/ddd-bounded-context]] — Evans's prescription at the system-of-systems scale is the same shape: small interface, large coherent model.
- [[Concepts/pragmatic-programmer-tips]] — Hunt & Thomas's orthogonality and decoupling (Tip 13, Tip 26) are the daily-practice expression of the same principle.

## Key Insights

1. **Deep modules hide complexity; shallow modules expose it.** The depth ratio (capability / interface size) is the unit of measure.
2. **The Unix file I/O API is the canonical deep module.** Five syscalls hide an enormous implementation.
3. **"Small modules" is a misconception.** Conventional wisdom that small classes/methods are better leads to classitis — many shallow modules that collectively carry more cognitive load than one deep one.
4. **Pull complexity downwards.** It's more important for a module to have a simple interface than a simple implementation.
5. **Define errors out of existence.** Exceptions are a major source of shallow-module leakage; one of Ousterhout's strongest prescriptions.
6. **Composition over inheritance.** Implementation inheritance is one of the most reliable sources of shallow modules.

## Related Concepts

- [[Concepts/software-engineering-fundamentals]]
- [[Concepts/software-entropy]]
- [[Concepts/ddd-bounded-context]]
- [[Concepts/pragmatic-programmer-tips]]

## References

- Raw Article: [[Raw/software-engineering-fundamentals-sources-2026-09-18]]
- Original source: John Ousterhout, *A Philosophy of Software Design* (2018); Matt Duck's review; Wikipedia *Software rot* (for the entropy/anti-entropy framing); Path-Sensitive critique
