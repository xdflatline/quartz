---
title: "Building a Multi-Agent System: 3 Patterns, Explained Simply"
details: "Verbatim source: Kadharmoideen Fadurudeen argues from his own projects that most agent work should stay single-agent, then lays out pipeline, orchestrator, and blackboard patterns with a four-question selection ladder. Closes with five failure lessons from Stormwise, a two-stage Claude weather assistant evaluated on 117 real National Weather Service alert cases."
tags:
  - raw
  - multi-agent
  - orchestration
  - blog-post
created: 2026-11-26
updated: 2026-11-26
type: raw
source: "https://kadhar.dev/blog/multi-agent-systems-from-scratch"
---

# Building a Multi-Agent System: 3 Patterns, Explained Simply

**Source:** Kadharmoideen Fadurudeen, kadhar.dev (https://kadhar.dev/blog/multi-agent-systems-from-scratch)
**Date Retrieved:** 2026-11-26
**Type:** Blog Post

---

Most of the AI agents I've built were just one agent.

Earlier this year I built a dinner recommender. You tell it where you are, it checks the weather, and it suggests food that fits. On a rainy evening in Chennai that means hot tea with vada or bajji. On a hot afternoon, buttermilk or tender coconut water. Under the hood it was one model with three tools (location, weather and restaurant search) and a cap on how many steps it could take. It worked. Splitting it into several agents would have made it slower and more expensive, for nothing.

So this isn't a "you need multi-agent" post. It's about when splitting a job across agents actually helps, the three ways people usually do it, and what goes wrong. I'll use that same dinner question all the way through, because it's small enough to follow, and you can play with it below.

## What a multi-agent system is

An **agent** is an AI model that can use tools and decide its own next step. A **multi-agent system** is several of those, each with a narrower job, passing work between them.

Think of a kitchen. One cook can make a whole meal. A busy restaurant splits it up: someone on the grill, someone on sauces, a head chef calling the orders. That's great on a Friday night with fifty tables. For one dinner at home, it's overkill.

Splitting helps when…

- Parts of the job need very different instructions or tools.
- Parts can run at the same time, like searching five topics at once.
- You want to test each part on its own.

Stay with one agent when…

- One agent with good tools already does the job.
- Speed and cost matter more than structure.
- You can't yet say what each agent would own.

## Pattern 1: Pipeline

An assembly line. Each agent does one step and hands the result to the next, always in the same order.

Weather (rain, 26°C) → Food ideas (hot snacks, tea) → Places (3 open nearby) → Checker (still open?) → Reply. Each step only talks to the next one. No going back.

**Use it when** you could write the steps down as a checklist before you start. It's the easiest pattern to test, because every step has a clear input and output.

**Watch out:** it's rigid. If step three sometimes needs to go back to step one, you'll start bolting on special cases until it quietly becomes the next pattern.

## Pattern 2: Orchestrator

The head chef. A lead agent reads the request, decides what help it needs, sends out the work and puts the answers together. The helpers only talk to the lead, never to each other.

Lead agent (plans + combines) → Weather, Places, Food ideas. The lead sends work out and gets answers back. Helpers never talk to each other.

This is the pattern behind the "deep research" features in tools like Claude and ChatGPT: a lead agent plans, several helpers search different angles at the same time, and the lead writes the report.

**Use it when** you know what *kinds* of help a request needs, but the details depend on the request.

**Watch out:** everything flows through the lead. If it plans badly, every helper inherits the mistake.

## Pattern 3: Blackboard

A shared whiteboard. There's no boss. Agents read what's on the board, add what they know, and step in when they have something useful.

Shared board (rain, 26°C · try vada & tea / 3 places · one closes soon) ↔ Weather, Food ideas, Places, Critic.

**Use it when** nobody can know the steps in advance. Debugging is the classic case: one agent suggests a cause, another looks for evidence, a third pokes holes, and what happens next depends on what they find.

**Watch out:** no one owns the plan. That makes it the hardest pattern to test and the easiest to get stuck in a loop.

## Try it: run the same dinner request three ways

> [Interactive playground on the source page — a scripted walkthrough, not live AI. Pick a pattern (pipeline / orchestrator / blackboard), then optionally break something: bad data upstream (the weather agent returns an old reading), agents can hand work back (one agent asks another for help, and it asks right back), guardrails on (a checker at handoffs, a hop limit and a budget per request). It steps through 9 scripted steps showing model-call counts.]

## What actually breaks: lessons from Stormwise

My other project, Stormwise, is a severe-weather assistant built on Claude. At its core it's a pipeline: get the official alerts, then let the model answer your question with them in hand. I evaluated it against 117 cases built from real National Weather Service alerts ([the full write-up is on arXiv](https://arxiv.org/abs/2611.05290)). Only two stages, and it still taught me most of what I know about how these systems fail.

**1. Bad data travels, and arrives looking like fact**

Weather services publish *test* alerts. My pipeline took some of them in as real warnings, and the model, reasonably, believed them. The model didn't make the mistake; the step before it did. With several agents this is the default: agent B can't tell agent A's guess from a fact. Check data at every handoff, in plain code.

**2. The right data beats a clever prompt**

Without access to alerts, the assistant told people conditions were calm during an active warning in 26 of 69 cases (38%). Adding an instruction to admit it couldn't see official alerts made it worse: 31 of 69 (45%). With the real alerts and a plain prompt: zero. Getting the right information to the right step fixed it. Prompting didn't.

**3. Budgets break on the hardest cases**

A token budget that was fine for everyday questions failed on complex cases, which in a storm are the ones that matter most. You need budgets, but decide in advance what happens when one runs out: a short, safe answer, not a half-finished one.

**4. Your automatic checker can be wrong too**

I first measured false reassurance with a simple pattern-matching script. It missed 53 of the 57 real cases and pointed to the opposite conclusion, so I ended up reading and labelling all 342 responses by hand. If one agent checks another, check the checker.

Two more you'll meet in anything where agents can hand work back: loops and cost. Loops are what you saw in the playground, where every agent is behaving sensibly and the system still goes in circles. Cost is quieter. My dinner agent had a step limit from day one and never ran away, yet I still took it offline, because the API bills were more than a side project could justify. More agents means more calls, every time.

## The guardrails I'd add on day one

None of these are clever. They're plain code that sits outside the agents.

- **Check every handoff.** Validate what one agent passes to the next: format, freshness, and whether it makes sense.
- **Limit the hops.** If a task has bounced between agents a few times, stop and ask a person.
- **One budget per request.** Track it in one place, not per agent, and decide the fallback answer in advance.
- **Log every message between agents.** When a run goes wrong, you'll want to replay it step by step.
- **Test with real cases.** Build a set of real examples, and spot-check your automatic scoring by hand.

## A quick way to choose

- Can one agent with tools do it? → **Use one agent. Stop here.**
- Can you write the steps as a checklist? → **Pipeline.**
- Do you know the kinds of help, but not the details? → **Orchestrator.**
- Does the next step depend on what you discover? → **Blackboard, with strict limits.**

## Frequently Asked Questions

### What is a multi-agent system?

A multi-agent system is several AI agents, each with a narrower job, passing work between them. An agent is a model that can use tools and decide its next step. Instead of one agent doing everything, you might have one that gathers information, one that checks it, and one that writes the final answer.

### When should I use multiple agents instead of one?

Start with one agent. Split only when parts of the job need clearly different instructions or tools, when parts can run at the same time, or when you need to test pieces separately. Every extra agent adds model calls, cost and new ways to fail.

### What are the main multi-agent patterns?

Pipeline (agents run in a fixed order, like an assembly line), orchestrator-worker (a lead agent hands out tasks and combines the results), and blackboard (agents read and write a shared workspace until the answer is ready). Pipelines are easiest to test; blackboards are the most flexible and the hardest to control.

### What usually goes wrong in multi-agent systems?

Bad data from one agent being treated as fact by the next, agents handing work back and forth in a loop, costs growing with every extra call, and budgets or automatic checks failing on the hardest cases. These are fixed with plain code around the agents: checks at every handoff, hop limits, a budget per request and real evaluation.

## The short version

Start with one agent. Split only when a part clearly needs its own instructions, tools or speed. Then put most of your effort into the boring parts: handoff checks, limits and real evaluation. That's where my systems actually failed, and where yours will too.

---

## Related Pages

- [[Concepts/blackboard-agent-coordination]]
- [[Concepts/handoff-contract-validation]]
- [[Concepts/grounding-over-honesty-prompting]]
- [[Entities/stormwise]]
- [[Research/multi-agent-pattern-selection-and-failure-lessons-2026]]
