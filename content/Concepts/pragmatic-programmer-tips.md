---
title: "Pragmatic Programmer Tips (Quick Reference)"
details: "The 70 practical rules distilled from Andrew Hunt & David Thomas's The Pragmatic Programmer (1999, 20th-anniversary edition 2019), forming the daily-practice half of the operator's named software-engineering fundamentals. Organised by chapter — Pragmatic Philosophy (care about craft, broken windows, knowledge portfolio), Pragmatic Approach (DRY, orthogonality, tracer bullets, domain languages), Basic Tools (plain text, shell, source control), Pragmatic Paranoia (design by contract, dead programs, assertive programming), Bend or Break (decoupling, Law of Demeter, metaprogramming), While Coding (program deliberately, refactor), Before the Project (requirements pit, specification trap), and Pragmatic Projects (pragmatic teams, ruthless testing, document as you write, sign your work). The list is the operator's working definition of what it means to be a pragmatic software engineer."
tags:
  - concept
  - software-engineering
created: 2026-09-18
updated: 2026-09-18
type: concept
sources:
  - "[[Raw/software-engineering-fundamentals-sources-2026-09-18]]"
---

# Pragmatic Programmer Tips (Quick Reference)

**Source:** [[Raw/software-engineering-fundamentals-sources-2026-09-18]] — full Quick-Reference table from Hunt & Thomas, *The Pragmatic Programmer* (1999; 20th-anniversary ed. 2019).
**Category:** Reference (practical rules)
**Status:** Production-validated — 25+ years of practitioner consensus

---

## Overview

The Pragmatic Programmer's Quick Reference is a table of **70 tips** that summarise the practical half of Hunt & Thomas's software-engineering philosophy. Each tip is one or two sentences, and most are operational: they tell you what to do tomorrow, not what the universe is for.

The tips are organised by chapter:

1. **A Pragmatic Philosophy** (Tips 1–6) — care, responsibility, entropy, change, scope, knowledge.
2. **A Pragmatic Approach** (Tips 7–18) — DRY, orthogonality, reversibility, tracer bullets, prototyping, domain languages, estimating.
3. **The Basic Tools** (Tips 19–25) — plain text, shells, source control, debugging, text manipulation, code generators.
4. **A Pragmatic Paranoia** (Tips 26–30) — design by contract, dead programs, assertive programming, exception discipline.
5. **Bend or Break** (Tips 31–36) — decoupling, Law of Demeter, metaprogramming, temporal coupling, blackboards.
6. **While You Are Coding** (Tips 37–45) — programming deliberately, algorithm speed, refactoring, testable code, evil wizards.
7. **Before the Project** (Tips 46–50) — requirements pit, impossible puzzles, not until you're ready, specification trap, circles and arrows.
8. **Pragmatic Projects** (Tips 51–70) — pragmatic teams, ubiquitous automation, ruthless testing, document as you write, sign your work.

The list below is the operator's working definition of what it means to be a pragmatic software engineer.

## Core Content

### Chapter 1: A Pragmatic Philosophy

- **Tip 1: Care About Your Craft.** Why spend your life developing software unless you care about doing it well?
- **Tip 2: Think! About Your Work.** Turn off the autopilot and take control. Constantly critique and appraise your work.
- **Tip 3: Provide Options, Don't Make Lame Excuses.** Instead of excuses, provide options. Don't say it can't be done; explain what can be done to salvage the situation.
- **Tip 4: Don't Live with Broken Windows.** Don't mess up the carpet when fixing the broken window.
- **Tip 5: Be a Catalyst for Change.** Most software disasters start out too small to notice, and most project overruns happen a day at a time.
- **Tip 6: Remember the Big Picture.** Don't be like the frog in the warming water.

### Chapter 2: A Pragmatic Approach

- **Tip 7: Make Quality a Requirements Issue.** The scope and quality of the system you produce should be specified as part of that system's requirements.
- **Tip 8: Invest Regularly in Your Knowledge Portfolio.** Serious investors invest regularly — as a habit.
- **Tip 9: Critically Analyze What You Read and Hear.** The knowledge in your portfolio must be accurate and unswayed by vendor or media hype.
- **Tip 10: It's Both What You Say and the Way You Say It.** Know your audience (WISDOM acrostic), choose your moment, choose a style.
- **Tip 11: DRY — Don't Repeat Yourself.** Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.
- **Tip 12: Make It Easy to Reuse.**
- **Tip 13: Eliminate Effects Between Unrelated Things.** Two things are orthogonal if changes in one do not affect the other.
- **Tip 14: There Are No Final Decisions.** Be prepared for changes.
- **Tip 15: Use Tracer Bullets to Find the Target.** Lean-but-complete code that forms the skeleton of the final system, developed end-to-end.
- **Tip 16: Prototype to Learn.** Prototype anything that carries risk.
- **Tip 17: Program Close to the Problem Domain.** Use the vocabulary of the domain.
- **Tip 18: Estimate to Avoid Surprises.** Scale time estimates properly (days / weeks / months / think hard).

### Chapter 3: The Basic Tools

- **Tip 19: Keep Knowledge in Plain Text.**
- **Tip 20: Use the Power of Command Shells.**
- **Tip 21: Use a Single Editor Well.**
- **Tip 22: Always Use Source Code Control.**
- **Tip 23: Fix the Problem, Not the Blame.** It doesn't really matter whether the bug is your fault or someone else's; fix it.
- **Tip 24: Don't Panic When Debugging.** Take a deep breath and THINK! about what could be causing the bug.
- **Tip 25: Select Is Not Broken.** It is reported that the "select is broken" bug fix has a success rate of about 0%.

### Chapter 4: A Pragmatic Paranoia

- **Tip 26: Design by Contract.** Each routine is a contract; preconditions, postconditions, invariants are checked.
- **Tip 27: Dead Programs Tell No Lies.** When in doubt, crashing is better than corrupting state.
- **Tip 28: Use Assertive Programming.** If it can't happen, use assertions to ensure that it won't.
- **Tip 29: How to Balance Resources.** Manage resources (memory, file handles, locks) with discipline.
- **Tip 30: Don't Outrun Your Headlights.** Take small, verifiable steps; you can always grow a working program.

### Chapter 5: Bend, or Break

- **Tip 31: Decouple Your Code.** Keep things loosely coupled.
- **Tip 32: Tell, Don't Ask.** Don't ask an object for its data and then act on it; tell the object what to do.
- **Tip 33: Replace Inheritance with Delegation Where Appropriate.**
- **Tip 34: Use Blackboards to Coordinate Workflow.** A blackboard is a shared data structure that workers read and write.
- **Tip 35: Separate Views from Models.** Build the model first, then present it in multiple views.
- **Tip 36: Use Blackboards to Coordinate Workflow.**

### Chapter 6: While You Are Coding

- **Tip 37: Program Deliberately.** Stay aware of what you're doing; don't code blindfolded.
- **Tip 38: Don't Program by Coincidence.** Rely only on reliable things; don't code on top of lucky accidents.
- **Tip 39: Estimate the Order of Your Algorithms.** Get a feel for O(n).
- **Tip 40: Test Your Estimates.** Run tests; don't assume.
- **Tip 41: Refactor Early, Refactor Often.** The boy scout rule: leave the campground cleaner than you found it.
- **Tip 42: Design to Test.** Write code that is testable.
- **Tip 43: Don't Live with Broken Windows.** (Repeated intentionally.) Fix the small things.
- **Tip 44: Use a Project Glossary.** Single source of all terms and vocabulary.
- **Tip 45: Don't Think Outside the Box — Find the Box.** Identify the real constraints when faced with an impossible problem.

### Chapter 7: Before the Project

- **Tip 46: The Requirements Pit.** Don't gather requirements — dig for them. The hard part is finding what the user really needs.
- **Tip 47: Work with a User to Think Like a User.** Identify the real user; understand the user's mental model.
- **Tip 48: Use a Project Glossary.**
- **Tip 49: Abstractions Live Longer than Details.** Invest in abstractions; details come and go.
- **Tip 50: Don't Use Manual Procedures.** A shell script or batch file will execute the same instructions, in the same order, time after time.

### Chapter 8: Pragmatic Projects

- **Tip 51: Organize Around Functionality, Not Job Functions.** Build teams the way you build code.
- **Tip 52: Don't Use Manual Procedures.** (Repeated.) Automate.
- **Tip 53: Ubiquitous Automation.** Scripts everywhere.
- **Tip 54: Use a Project Glossary.**
- **Tip 55: Ruthless Testing.** Test state coverage, not code coverage.
- **Tip 56: Test Early. Test Often. Test Automatically.**
- **Tip 57: Coding Ain't Done 'Til All the Tests Run.**
- **Tip 58: Use Saboteurs to Test Your Testing.** Introduce bugs on purpose to verify the tests catch them.
- **Tip 59: Find Bugs Once.** Once a human tester finds a bug, it should be the last time a human tester finds that bug.
- **Tip 60: Build Documentation In, Don't Bolt It On.**
- **Tip 61: Gently Exceed Your Users' Expectations.** Come to understand your users' expectations, then deliver just that little bit more.
- **Tip 62: Sign Your Work.** Craftsmen of an earlier age were proud to sign their work. You should be, too.

### The cross-cutting themes

The 70 tips reduce to a smaller number of cross-cutting themes:

| Theme | Strongest tips |
|-------|----------------|
| Care about your craft | Tip 1, Tip 2 |
| Take responsibility | Tip 3, Tip 23 |
| Don't live with broken windows | Tip 4, Tip 43 |
| DRY — every knowledge has one home | Tip 11 |
| Orthogonality | Tip 13, Tip 31, Tip 32 |
| Tracer bullets, prototyping | Tip 15, Tip 16 |
| Design by contract | Tip 26, Tip 28 |
| Communicate | Tip 10, Tip 67 |
| Ruthless testing | Tip 56, Tip 57, Tip 58, Tip 59 |
| Automate | Tip 50, Tip 52, Tip 53 |
| Refactor continuously | Tip 41 |
| Invest in your knowledge portfolio | Tip 8 |
| Pragmatic teams | Tip 51, Tip 60 |
| Sign your work | Tip 62 |

### How to use this list

The list is a reference, not a curriculum. The strongest practitioners keep the entire list in their working memory and reach for the relevant tip in context. The operator's practice is to **cite tips by number** during grilling sessions — "Tip 4: don't live with broken windows" is shorthand for the entire broken-windows argument.

### Connection to other fundamentals

- [[Concepts/software-engineering-fundamentals]] — the Pragmatic Programmer is one of the three pillars of the umbrella.
- [[Concepts/software-entropy]] — Tip 4 (broken windows), Tip 5 (catalyst for change), Tip 41 (refactor early, refactor often).
- [[Concepts/ddd-ubiquitous-language]] — Tip 17 (program close to the problem domain), Tip 54 (project glossary).
- [[Concepts/deep-modules]] — Tip 13 (orthogonality), Tip 26 (design by contract), Tip 31 (decoupling).
- [[Entities/andrew-hunt-dave-thomas]] — authors.

## Key Insights

1. **70 tips, but a small number of cross-cutting themes.** The list is a mnemonic, not a checklist.
2. **The tips are operational.** Each is something to do tomorrow, not something to believe.
3. **Tip numbers are shared shorthand.** "Tip 4" or "Tip 11" carries the entire concept.
4. **The most-cited tips are about entropy, DRY, orthogonality, and testing.** These are the strongest cross-text patterns with Evans and Ousterhout.
5. **Sign your work.** The book ends on craftsmanship, not on technology.

## Related Concepts

- [[Concepts/software-engineering-fundamentals]]
- [[Concepts/software-entropy]]
- [[Concepts/ddd-ubiquitous-language]]
- [[Concepts/deep-modules]]
- [[Entities/andrew-hunt-dave-thomas]]

## References

- Raw Article: [[Raw/software-engineering-fundamentals-sources-2026-09-18]]
- Original source: Andrew Hunt & David Thomas, *The Pragmatic Programmer*, Addison Wesley (1999; 20th-anniversary ed. 2019); Hugo Matilla's reproduction on GitHub
