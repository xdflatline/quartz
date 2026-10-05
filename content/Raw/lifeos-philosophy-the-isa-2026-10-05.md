---
title: "LifeOS: ISA System (Philosophy)"
details: "The Ideal State Artifact — one document in 12 fixed sections (Problem, Vision, Out of Scope, Principles, Constraints, Goal, Criteria, Test Strategy, Features, Decisions, Changelog, Verification) that captures what 'done' looks like before work starts and is the test harness that closes it."
tags:
  - raw
  - agent
  - evaluation
source: https://ourlifeos.ai/philosophy/the-isa/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# ISA System

**Source:** [https://ourlifeos.ai/philosophy/the-isa/](https://ourlifeos.ai/philosophy/the-isa/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# ISA System

One document that captures what 'done' looks like — the testable spec the Algorithm climbs toward.


Fig. 07·Ordered sections around a grid of criteria

Before LifeOS builds anything hard, it writes down what done looks like. That document is the ISA, the [Ideal State Artifact](https://danielmiessler.com/blog/ai-ideal-state-articulation). It holds the [ideal state](https://ourlifeos.ai/philosophy/current-to-ideal-state) of whatever you’re working on, in enough detail that you can test whether you got there.

## Why it exists

Most work fails at the definition, not the doing. “Done” lives in your head as a vague picture, so you and a tool can both think you’re finished and mean two different things. Nothing catches the gap until it’s already shipped.

The ISA drags that picture into the open before any work starts. It writes the ideal state as a [hard-to-vary explanation](https://danielmiessler.com/blog/conversation-with-claude-on-deutsch-and-the-pai-algorithm): every part does a job, and removing or weakening any part changes what done means. A vague spec lets you wiggle out of it later. A hard-to-vary one doesn’t, which is the whole reason it’s worth the effort.

## How it works

The ISA is one document with twelve sections in a fixed order, running from Problem and Vision at the top down through Goal, Criteria, and finally Verification. That order is fixed on purpose. You state what’s wrong and what right looks like, then what you’re deliberately leaving out, all before you name the goal.

The twelve sectionsfixed order, top to bottom

- 1 · ProblemWhat's actually wrong.
- 2 · VisionWhat right looks like — and what [euphoric surprise](https://ourlifeos.ai/philosophy/euphoric-surprise) would be here.
- 3 · Out of ScopeWhat you're deliberately not doing.
- 4 · PrinciplesHow the system may think about it.
- 5 · ConstraintsWhat the solution may not do.
- 6 · GoalThe one-line target — named only after all of the above.
- 7 · CriteriaThe ISCs — the testable heart of the document.
- 8 · Test StrategyThe single probe behind each criterion.
- 9 · FeaturesThe work, tracked against the criteria.
- 10 · DecisionsWhy the calls were made.
- 11 · ChangelogWhat happened, in order.
- 12 · VerificationThe evidence that every criterion passed.

**The order is the discipline:** you state the problem and what "right" means before you're allowed to name the goal.

The heart of it is the Criteria section: the ISCs. Each is a single condition you check with one probe, phrased so it comes out either true or false, and they are [the tests themselves](https://ourlifeos.ai/philosophy/assay) with no separate acceptance suite bolted on later. The task is done when every ISC passes, so progress is something the document computes rather than something you assert.

Two more things keep it honest. Principles bind how the system thinks and Constraints bind what the solution may do, while anti-criteria turn the things you ruled out into testable proof that they stayed out. And ISC IDs never renumber once written, so a criterion you point at today still means the same thing three edits from now.

That’s why one document does several jobs at once: the written articulation of done, the test harness while you build, the done condition when you finish, and the long-lived record afterward. Read it through whatever lens the current phase needs. The ideal state and the test that proves it are the same object, so nothing drifts between what you meant and what you actually check.

## Where it fits

Every [Algorithm](https://ourlifeos.ai/philosophy/the-algorithm) run binds to an ISA. The run reads and writes it the whole way through, from the first scaffold to the evidence checked in at close. The Algorithm is the motion; the ISA is the thing that persists after the motion stops.

It lives in one of two homes. Work with a lasting identity (an app, a library, your blog, the Algorithm itself) keeps a project ISA in its repo that grows across every session. One-shot work gets a task ISA under a work folder, created when the job starts and archived when it’s done.

## What it feels like

You start a real piece of work and the first thing that exists is a checklist of what would make it right, written before any guessing begins. As the work goes, you watch boxes flip from open to done, each with its proof sitting next to it. When it’s over, you don’t have to wonder whether it’s over. The document already knows, because every criterion it holds is checked and every check has evidence behind it.

A real ISA, mid-buildthe actual criteria checklist from a live LifeOS run


**The document computes "done" — you don't assert it.** This is an actual ISA from a LifeOS migration run: 20 criteria passed with evidence, 15 still pending, 6 anti-criteria guarding what must not happen.

[Full documentationThe ISA — Ideal State Articulation →](https://docs.ourlifeos.ai/ISA__ISASystem)
