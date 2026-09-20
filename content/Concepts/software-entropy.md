---
title: "Software Entropy (Broken Windows)"
details: "The tendency of software systems to accrue disorder, technical debt, and compounding complexity over time — even when no code is changed. Coined in Object-Oriented Software Engineering (Jacobson et al., 1992) by analogy with thermodynamic entropy; popularised by Hunt & Thomas in The Pragmatic Programmer (1999) through the broken-windows metaphor, in which one unrepaired small defect signals abandonment and accelerates further degradation. Classified by Wikipedia into dormant rot (unused code) and active rot (code under continuous modification), and is the first-order phenomenon that the rest of the software-engineering fundamentals exist to fight."
tags:
  - concept
  - software-engineering
created: 2026-09-18
updated: 2026-09-18
type: concept
sources:
  - "[[Raw/software-engineering-fundamentals-sources-2026-09-18]]"
---

# Software Entropy (Broken Windows)

**Source:** [[Raw/software-engineering-fundamentals-sources-2026-09-18]] — Hunt & Thomas (Tip 4); Wikipedia *Software Rot*; thevaluable.dev synthesis.
**Category:** Software engineering phenomenon / decay
**Status:** Fundamental — recognised across the canon and the industry

---

## Overview

Software entropy is the observation that **software systems, like physical systems, trend toward disorder over time**, even when nothing in the code itself has changed. The name was borrowed from the second law of thermodynamics — entropy in a closed system does not decrease — and applied to code by Jacobson et al. in *Object-Oriented Software Engineering* (1992). Hunt & Thomas gave the phenomenon its most-cited operational form in *The Pragmatic Programmer* (1999) through the **broken-windows** metaphor: one unrepaired broken window signals that no one cares about the building, and the rate of vandalism accelerates.

Software entropy is not just metaphor. It is the empirical observation that any code that is not actively maintained degrades: dependencies rot, unused paths harbour bugs, naming drifts, and small tactical shortcuts compound into large architectural problems. The rest of software-engineering fundamentals — DRY, orthogonality, deep modules, bounded contexts — exist because complexity is inevitable and entropy is real. The choice is not whether to fight entropy, but how.

## Core Content

### Definition

> **Software entropy** (also *bit rot*, *code rot*, *software erosion*, *software decay*, *software rot*) is the degradation, deterioration, or loss of the use or performance of software over time. — Wikipedia, *Software Rot*

The *Jargon File* defines "bit rot" jocularly as the explanation that a software program degrades over time "even if 'nothing has changed'" — as if the bits were subject to radioactive decay.

### The Broken-Windows metaphor

From Hunt & Thomas, *The Pragmatic Programmer*, Tip 4:

> One broken window, left unrepaired for any substantial length of time, instills in the inhabitants of the building a sense of abandonment — a sense that the powers that be don't care about the building. So another window gets broken. People start littering. Graffiti appears. Serious structural damage begins. In a relatively short space of time, the building becomes damaged beyond the owner's desire to fix it, and the sense of abandonment becomes reality.

> Don't mess up the carpet when fixing the broken window.

The metaphor's operational lesson: **fix the small things immediately.** A workaround, a duplicate, a poorly-named variable, a skipped test — each is a broken window. Leave one and the next developer will assume the codebase is already abandoned, and will add their own.

### Classification (Wikipedia)

Software rot is usually classified into two kinds:

- **Dormant rot** — Software that is not currently being used gradually becomes unusable as the remainder of the application changes. Infrequently used portions of code may harbour bugs that go unnoticed; when user requirements change, this code may be exercised, exposing the bugs.
- **Active rot** — Software that is being continuously modified may lose its integrity over time if proper mitigating processes are not consistently applied. Adding new features may be prioritised over updating documentation, and the program drifts from its original engineered design.

Active rot is the more common failure mode of long-lived commercial software. It slows once the application reaches the end of its commercial life and further development ceases — at which point the bugs become stable.

### Causes

| Cause | Mechanism |
|-------|-----------|
| Environment change | The platform, libraries, protocols (e.g. TLS 1.0/1.1 deprecation), or upstream APIs change in ways the original designer did not anticipate |
| Onceability | A system is configured by trial and error in a way the next user cannot reproduce (lost passwords, undocumented setup, no recovery path) |
| Unused code | Defensive or compatibility code is written, falls behind, and contains latent bugs that surface when conditions change |
| Rarely updated code | When parts of a system function at arm's length from each other, changes to one may silently break another |
| Online connectivity | License servers and certificate authorities disappear, leaving otherwise-functional software unable to start |
| Documentation rot | New features are added without updating documentation, so knowledge is gradually lost |

### Why entropy is irreducible

The entropy of any closed system does not decrease. The software analogue: even if you never modify your software, the world around it changes — third-party libraries need security updates, CPUs change, browsers deprecate TLS versions, OSes reach end-of-life. If you keep your libraries up to date, you introduce change and complexity. If you don't, security and compatibility decay.

The real question is **not** whether to fight entropy, but how to slow it.

### How to fight entropy

Drawing from Hunt & Thomas, Wikipedia, and the practitioner literature:

1. **Don't live with broken windows.** (Tip 4.) Fix small defects immediately. The cost of fixing one broken window is small; the cost of fixing a building full of them is overwhelming.
2. **Fix the root cause, not the symptom.** The most common technical debts are introduced during debugging — by *adding* a workaround instead of *changing* or *deleting* the broken code. The bug is still there; it's just harder to trigger.
3. **Write automated tests.** Manual testing cannot keep up with the rate of change. Tests are the only durable mechanism to assert that today's behaviour is preserved tomorrow.
4. **Refactor continuously.** Refactor when you develop other features; do not make refactoring a separate task. "Refactor small chunks of code at a time and run your tests often." — thevaluable.dev
5. **Maintain a project glossary.** (Hunt & Thomas Tip 54.) A single source of truth for vocabulary prevents naming drift from compounding.
6. **Adopt strategic programming.** (Ousterhout.) Tactical decisions accumulate; the cost of refactoring eventually exceeds the cost of scheduled feature work, and the codebase becomes nearly impossible to fix.
7. **Document as you write.** "Documentation created separately from code is less likely to be correct and up to date." (Hunt & Thomas Tip 68.) Documentation rot is itself a form of entropy.
8. **Share knowledge.** Pair programming, code review, internal articles — when knowledge leaves with a single person, the system loses the ability to maintain itself.

### Connection to software-engineering fundamentals

Software entropy is the **first-order phenomenon** that the rest of the fundamentals exist to fight:

- **DRY** (Hunt & Thomas) prevents the same knowledge from living in multiple places, where each copy can drift.
- **Orthogonality** (Hunt & Thomas) limits the blast radius of any one change.
- **Bounded contexts** (Evans) prevent the model itself from drifting across team boundaries.
- **Deep modules** (Ousterhout) hide implementation details so that the public surface area that must be kept consistent is small.
- **Strategic programming** (Ousterhout) refuses the tactical-shortcut treadmill.

None of these guarantees immunity from entropy. All of them slow it.

## Key Insights

1. **Entropy is not a metaphor.** Software systems, like physical systems, trend toward disorder; the rate can be slowed but the direction cannot be reversed.
2. **Small defects compound.** The broken-window effect is empirically observable: one unrepaired small defect increases the rate of subsequent defects.
3. **Refactoring is not a separate task.** It is part of writing every feature.
4. **Unused code rots first.** Dormant rot is more dangerous than active rot because it is invisible.
5. **Tests are the only durable mechanism for keeping behaviour.** Without automated tests, refactoring is reckless and entropy wins.

## Related Concepts

- [[Concepts/software-engineering-fundamentals]] — the umbrella discipline; entropy is what they exist to fight
- [[Concepts/deep-modules]] — Ousterhout's prescription for keeping the public surface small enough to maintain
- [[Concepts/ddd-bounded-context]] — Evans's prescription for keeping models coherent across organisational boundaries
- [[Concepts/pragmatic-programmer-tips]] — the daily-practice table from Hunt & Thomas

## References

- Raw Article: [[Raw/software-engineering-fundamentals-sources-2026-09-18]]
- Original sources: Hunt & Thomas, *The Pragmatic Programmer*, pp. 4–6 (Tip 4); Wikipedia, *Software Rot*; Jacobson et al., *Object-Oriented Software Engineering* (1992); thevaluable.dev, *Fighting Software Entropy* (2019)
