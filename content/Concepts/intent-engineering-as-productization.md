---
title: "Intent Engineering — Conveying the WHAT, Productized"
details: "An architectural pattern for AI agent interaction: instead of telling the model *how* to do something (prompt engineering), carry *what* you ultimately want into every interaction, so the model can pick the right how on its own. Lives at several scales: durable intent (mission, goals, beliefs) in a structured file like TELOS; task intent in a structured spec like an ISA; situational intent (who you are, what you own, what you've decided) in memory and context; closure intent in verification against the stated goal. Distinct from prompt engineering, which is the mechanism's instruction; intent engineering is the goal's instruction. Coined by Daniel Miessler as the defining job of the LifeOS platform."
tags:
  - concept
  - architecture-pattern
  - agent
  - prompt-engineering
created: 2026-10-05
updated: 2026-10-05
type: concept
source: "[[Raw/lifeos-philosophy-intent-engineering-2026-10-05]]"
---

# Intent Engineering — Conveying the WHAT, Productized

**Source:** [[Raw/lifeos-philosophy-intent-engineering-2026-10-05]] (LifeOS / Daniel Miessler)
**Category:** Architecture Pattern
**Status:** Active research area (paired with prompt and context engineering)

## Overview

The number one problem with AI systems is direction, not execution. Models are already extraordinary at *doing*; what they almost never get is clear instruction on *what* to do — so they build the wrong thing brilliantly. Intent engineering is the practice of capturing what you're ultimately trying to achieve, conveying it to your AI on every task, and verifying the output against it.

## The intent stack, top to bottom

Intent lives at several scales, and a good system carries all of them:

- **Durable intent** — your mission, goals, problems, strategies. The why behind every what. Lives in [[Concepts/structured-telos-file-for-durable-intent|TELOS]] (or any structured "ideal state" file).
- **Task intent** — what "done" looks like for the task, as binary tests. Lives in an [[Concepts/ideal-state-artifact-isa|ISA]].
- **Situational intent** — who you are, what you own, what you've already decided. Lives in memory + context.
- **Closure intent** — the result is checked against the stated intent, never against vibes. Lives in verification.

When you ask for something, the system doesn't just relay your words. It assembles what you ultimately want *around* them, and the work is judged against that assembled whole.

The same ask, twicewhat intent conveyance actually changes

**Words only**

> "Make me a landing page for the course."

The model picks a framework, invents a tone, guesses at an audience, and ships something generic. Competent execution, random direction. You spend the next hour steering it back toward what you meant.

**Intent conveyed**

The same sentence — but the system already knows the goal this course serves, who it's for, the voice you write in, and the stack you ship on.

Done gets written down as criteria before work starts: makes the argument, sounds like you, loads fast, links resolve. The output is checked against those, not against vibes.

The prompt didn't get longer. The system around it got smarter about what you ultimately want — that's the productization.

## The stack: intent → context → prompt

Intent engineering extends rather than replaces prompting. It is still technically prompt engineering — what changes is the thing being articulated: not *how* something should be done, but *what* should be done.

- **Prompt engineering** — how to convey intent in the moment (the technique)
- **Context engineering** — fill the model's window with the right information for the step
- **Intent engineering** — know what you actually want before any context gets assembled (the tier above)

## Why intent matters more as models get better

Every model generation makes execution cheaper and direction more valuable. As capability grows, the bottleneck moves upstream from "can it do what I say" to "do I know what I want and we don't mean the same thing." Intent engineering is the layer that addresses that bottleneck.

## Connection to related patterns

- **Durable intent** → the [[Concepts/structured-telos-file-for-durable-intent|TELOS file pattern]] (mission, goals, values, strategies, narratives, challenges)
- **Task intent** → the [[Concepts/ideal-state-artifact-isa|ISA pattern]] (Ideal State Criteria before work)
- **Verification against intent** → the [[Concepts/four-tier-verification-stack|four-tier check stack]] (code / glance / assay / human)
- **Plain-language intent triggers** → the [[Concepts/self-activating-skill-libraries|skill trigger pattern]] ("USE WHEN" matched by meaning, not exact words)

## Key Insights

1. **The long version lives somewhere else.** A short prompt is fine if the long version is on file. The productization is the system that pulls the long version in.
2. **Intent is verifiable, vibes aren't.** The contract is that the result improves as a number you can check, not as a feeling you can't.
3. **Direction scales with capability.** The better the model, the more valuable intent conveyance becomes — the work that mattered at GPT-3 becomes the bottleneck at GPT-5.

## Related Concepts

- [[Concepts/ideal-state-artifact-isa]] — the task-intent document
- [[Concepts/generalized-hill-climbing-llm-tasks]] — the loop that runs the intent
- [[Concepts/euphoric-surprise-as-success-metric]] — the success metric for whether the intent landed
- [[Concepts/structured-telos-file-for-durable-intent]] — the durable-intent file pattern

## References

- Raw: [[Raw/lifeos-philosophy-intent-engineering-2026-10-05]]
- Origin essay: [Intent Engineering](https://danielmiessler.com/blog/intent-engineering)