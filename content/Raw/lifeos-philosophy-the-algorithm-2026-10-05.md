---
title: "LifeOS: The Algorithm (Philosophy)"
details: "The unified thinking system: a loop that routes each ask to the right intelligence, articulates it as binary testable criteria, climbs toward them, verifies each on real tool evidence, and reflects on what worked. Effort scales from a typo fix to a company launch."
tags:
  - raw
  - agent
  - orchestration
source: https://ourlifeos.ai/philosophy/the-algorithm/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# The Algorithm

**Source:** [https://ourlifeos.ai/philosophy/the-algorithm/](https://ourlifeos.ai/philosophy/the-algorithm/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# The Algorithm

One loop that routes each ask to the right intelligence, turns it into a testable spec, and climbs toward it.


Fig. 06·Route once, then climb: criteria close one way, on evidence

Most tools do what you ask and stop. [The Algorithm](https://danielmiessler.com/blog/the-last-algorithm) does something more disciplined: it takes a vague request, turns it into a spec you can test, and climbs toward that spec one checked step at a time. It runs at every scale, from a typo fix up to a company launch, because the shape of the work is always the same.

## Why it exists

A request is almost never as clear as it sounds. “Make the page faster” hides a dozen questions: faster for whom, measured how, at what cost, judged against what baseline. Skip past those and start building, and you build the wrong thing well.

The Algorithm forces the questions first. It reverse-engineers what you actually want into [Ideal State Criteria](https://danielmiessler.com/blog/ai-ideal-state-articulation) — small, binary criteria that are each either true or false. Once done is written down that way, it can’t drift. You either meet the criteria or you don’t, with no room to call something finished because you got tired of it.

That discipline covers the whole range of work. When the result is checkable (a code change, a deploy), the criteria are literal tests. When it’s a judgment call or a piece of writing, the criteria describe what a right answer would have to do, so even soft work gets a hard target.

## How it works

The Algorithm is one loop, not a fixed sequence of phases: write down what done means, then [climb toward it on evidence](https://ourlifeos.ai/philosophy/hill-climbing), reshaping the spec as the work teaches you.

The loopwhat every run does, at any scale

1. RouteRead the ask and pick who carries it — a light worker model, or the strongest model available when the work is hard.
2. ArticulateReverse-engineer the request into Ideal State Criteria — done, written down before building.
3. Name the probeEvery criterion states the evidence that would prove it false.
4. ClimbDo the work; a criterion closes only on real tool evidence — never "should work."
5. Fold inWhat the work reveals reshapes the spec: criteria added, split, tightened, or killed.
6. LearnReflect on what worked and feed the lesson to the next run.

Every run also carries a checklist of its own quality. The criteria have to be granular enough that each maps to a single probe, and harder work demands more of them before the build can start. Under-specified work doesn’t proceed; it goes back and gets split until each piece is one testable thing.

Effort scales to the task—discovered from the work itself, never predicted from a label. A quick lookup finishes in seconds on almost nothing; a hard cross-system design pulls in agents, audits, stronger models, and hours. Your plain-language steer (“go heavy,” “quick pass”) outranks everything else.

[Verification](https://ourlifeos.ai/philosophy/assay) is where most tools cheat and this one won’t. Every criterion marked done needs a live probe behind it: command output, an HTTP response, a screenshot, a diff. “Should work” counts as a failure, and on high-stakes work a model from another vendor reads the work too, since same-family models share the same blind spots.

Worked example"make the settings page faster," run through the engine

The request"Make the settings page faster." Four words, a dozen buried questions.

↓

The ask becomes criteriaThe vague request becomes binary criteria, each with one probe that comes out true or false.

- ✓Largest contentful paint under 1.2s on a cold load — 0.9s, Lighthouse trace
- ✓Layout shift stays below 0.05 — measured 0.01
- ✓Every existing settings test still passes — 48/48 green
- ✗JavaScript bundle stays under 180 KB — 214 KB, over budget, back to work

**The point:** that fourth box can't be argued past. Until it's green with evidence beside it, the task isn't done — however good the first three look.

## Routing: who does the work

Before the loop starts, every request is routed once. The Algorithm reads your words and how hard the work looks, then picks the level of intelligence it needs. Settled, mechanical work goes down to cheaper worker models, and hard analysis or creative judgment goes to the strongest model available. If you say “think deeply” or “max intelligence,” that choice is binding: the hard core of the work goes to the top model, along with the thinking tools that fit it.

Every agent is named for the model it runs, so naming an agent names the model. The models themselves live in one registry, which means a new model lineup is a one-line change that every part of the system picks up. After each handoff, the trail shows what actually ran next to what was asked for.

## Where it fits

This is the engine at the center. [Current State to Ideal State](https://ourlifeos.ai/philosophy/current-to-ideal-state) is the idea; the Algorithm is how that idea happens on a given task — intent engineering in motion, task by task. Everything else in LifeOS exists to serve it: [skills](https://ourlifeos.ai/philosophy/skill-system) give it capabilities, hooks hold it to the rules, memory carries what it learned.

Each run binds to an [ISA](https://ourlifeos.ai/philosophy/the-isa), the one document that holds the ideal state and its test criteria, plus the running record of everything that happened. And every run makes the next one better. [What the system learns](https://ourlifeos.ai/philosophy/learning) about your work and about itself gets captured and fed back, so the Algorithm keeps upgrading its own behavior.

## What it feels like

You ask for something fuzzy, and instead of a fast guess you get a short list of exactly what the answer has to satisfy. Then the work comes back with each box checked and the evidence attached, so you read the proof instead of taking “done” on faith. On the hard stuff it feels less like handing a task to a tool and more like working with something that won’t call a job finished until it actually is.

[Full documentationThe Algorithm — the LifeOS Thinking System →](https://docs.ourlifeos.ai/Algorithm__AlgorithmSystem)
