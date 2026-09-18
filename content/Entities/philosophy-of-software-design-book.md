---
title: "A Philosophy of Software Design (John Ousterhout)"
details: "A Philosophy of Software Design, by John Ousterhout (Self-published, 2018). A concise software-design textbook whose central thesis is that software design's primary purpose is to manage complexity, which manifests in three ways: change amplification (a simple change touches many places), cognitive load (the developer must know many things to make a change), and unknown unknowns (the developer does not know what they do not know). The book's most-cited contribution is the deep-modules principle: the best modules provide powerful functionality behind a simple interface. The book also covers strategic vs. tactical programming, design-it-twice, pull-complexity-downwards, naming, comments, consistency, and the failure modes of implementation inheritance. The book is one of three the operator has named as the canonical software-engineering reading list, alongside The Pragmatic Programmer and Domain-Driven Design."
tags:
  - software-engineering
  - reference
created: 2026-09-18
updated: 2026-09-18
type: entity
sources:
  - "[[Raw/software-engineering-fundamentals-sources-2026-09-18]]"
---

# A Philosophy of Software Design (John Ousterhout)

**Source:** [[Raw/software-engineering-fundamentals-sources-2026-09-18]]
**Category:** Book / Reference
**Original publication:** Self-published (Lulu), 2018; ISBN 978-1-7321522-0-2
**Author:** [[Entities/john-ousterhout]]

---

## Overview

*A Philosophy of Software Design* is John Ousterhout's 2018 software-design textbook. The book argues that the primary purpose of software design is to manage **complexity**, which manifests in three observable forms: **change amplification** (a simple change touches many places), **cognitive load** (the developer must know many things to make a change), and **unknown unknowns** (the developer does not know what they do not know). The book's most-cited contribution is the **deep-modules principle**: the best modules provide powerful functionality behind a simple interface, hiding substantial complexity from the caller.

The book is one of three the operator has named as the canonical software-engineering reading list, alongside Hunt & Thomas's *The Pragmatic Programmer* and Evans's *Domain-Driven Design*.

## Key Details

### Structure

The book is divided into four parts:

1. **Intrinsic complexity** — the nature and causes of complexity.
2. **Strategic vs. tactical programming** — why incremental tactical decisions compound into intractable codebases.
3. **Modules** — the deep-modules principle, general-purpose modules, pull-complexity-downwards, error definition, comments, naming.
4. **Style** — consistency, design-it-twice, and the failure modes of implementation inheritance and event-driven programming.

### The deep-modules principle

The book's most-cited contribution is the **deep-modules principle**:

> The best modules are those that provide powerful functionality, but have a simple interface. They are called *deep* modules, in contrast to *shallow* modules, which have a complex interface but not much functionality, thereby not hiding significant complexity.

The canonical example is Unix file I/O: five system calls (`open`, `read`, `write`, `seek`, `close`) hide enormous internal complexity. A typical OOP wrapper class with one method per field is shallow. See [[Concepts/deep-modules]].

### Other design rules

- **Tactical vs. strategic programming.** Tactical decisions compound; once a codebase is complex enough, it is nearly impossible to fix.
- **Pull complexity downwards.** It's more important for a module to have a simple interface than a simple implementation.
- **Define errors out of existence.** Exceptions are a major source of shallow-module leakage.
- **Comments should describe things that aren't obvious from the code.**
- **Naming is important.** Good names are precise, consistent, and not overly-general.
- **Consistency is important.** Consistency minimises complexity because it provides cognitive leverage.
- **Implementation inheritance increases complexity.** Composition can be a less-complex alternative.
- **Design it twice.** Multiple options for each major design decision yields a better result.

### Reception

The book is widely cited and has a strong following, especially among engineers who appreciate its directness. It has known critics (most notably Path-Sensitive), who argue that Ousterhout's specific instance of the deep-modules principle is misapplied in some cases and that advice derived from it is sometimes unreliable.

### Reception within the operator's canon

The book is one of three the operator has named as the canonical software-engineering reading list. The deep-modules principle is the operator's preferred operationalisation of "good module design", and is referenced alongside Hunt & Thomas's orthogonality (Tip 13) and Evans's bounded contexts.

### Status

In print since 2018. Available at leanpub and other channels. Recommended by practitioners including Charity Majors and others. The book is the most recent of the three canonical software-engineering texts the operator has named.

## Related Concepts

- [[Concepts/deep-modules]] — the book's central contribution
- [[Concepts/software-engineering-fundamentals]] — the umbrella
- [[Concepts/software-entropy]] — the phenomenon the book argues against
- [[Entities/john-ousterhout]] — author

## References

- Raw Article: [[Raw/software-engineering-fundamentals-sources-2026-09-18]]
- Original: <https://web.stanford.edu/~ouster/cgi-bin/book.php>
