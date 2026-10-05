---
title: "Structured TELOS File for Durable Intent"
details: "An architectural pattern for carrying durable intent across sessions: a structured file that holds your mission, goals, values, strategies, narratives, and challenges. The agent reads it on every prompt, so the work is always pointed at what you actually want rather than a stateless read of the latest message. The shape (not just the contents) is what matters: the system reasons against *all* of it — the largest mission, the concrete goals, the strategies, the narratives you're living out, and the named challenges — so a request gets handled in the context of your whole life, not just the words you typed."
tags:
  - concept
  - architecture-pattern
  - agent
  - memory
created: 2026-10-05
updated: 2026-10-05
type: concept
source: "[[Raw/lifeos-philosophy-telos-2026-10-05]]"
---

# Structured TELOS File for Durable Intent

**Source:** [[Raw/lifeos-philosophy-telos-2026-10-05]] (LifeOS / Daniel Miessler)
**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

A TELOS file is where your ideal state lives. It holds your mission, your goals, your values, your strategies, your narratives, and the challenges standing in your way. The agent reads it on every task, so the work is always pointed at what you actually want.

A system that doesn't know your goals can only react. You ask, it answers, it forgets. That is a tool. To move you toward an ideal state, a system has to know what that state is, and it has to keep knowing it across every session and every task. Without durable intent, "better" has no meaning. The system could finish a thousand tasks and none of them would add up, because nothing would tell it which direction counts as up.

## What the file holds

- **Mission** — the largest frame; the thing all of it is in service of.
- **Goals** — the concrete targets under the mission; the ones with a finish line.
- **Strategies** — how you've decided to get there.
- **Narratives** — the stories you're living out, in your own words.
- **Challenges** — what keeps getting in the way — named, so the system can route around it.

Values and strategies shape *how* you get there. Narratives are the stories you're living out, in your own words. Challenges name what keeps getting in your way. The system reasons against all of it, so a request gets handled in the context of your whole life, not just the words you typed into it.

## Why it isn't just a goals list

A goals list names what you want. A TELOS file names *all* the layers that need to be in tension when a real decision lands: which strategy you're using, which narrative you're living out, what keeps tripping you up. Most tools treat every request as if it came from nobody. You ask, they answer, and the answer would read the same for anyone who typed the same words. You spend half your effort explaining who you are before you can get anything useful back.

Same question, with and without TELOS"should I take this podcast invite?"

**No TELOS.** A balanced list of pros and cons that would read the same for anyone. Reach, time cost, audience fit — generic, and yours to sort out.

**Against your TELOS.** Weighed against your real goals: it feeds the audience you're trying to grow this year, and costs a morning you'd guard for deep work. A recommendation, not a menu.

## The line between a chatbot and an assistant

A stateless helper answers the question in front of it and moves on. An assistant carries your mission from one task to the next, so the goal-awareness never resets. TELOS is what it carries. The structured file is what makes the goal-awareness *survive* between sessions rather than being rebuilt every prompt.

## Connection to other patterns

- [[Concepts/append-only-amber-ledger-capture]] — the input side; new signals get graded against TELOS before being routed
- [[Concepts/ideal-state-artifact-isa]] — the task intent (ISA) is derived from the durable intent (TELOS); the ISA is the per-task instance
- [[Concepts/intent-engineering-as-productization]] — TELOS is the durable-intent layer of the intent stack
- [[Concepts/euphoric-surprise-as-success-metric]] — the bar against which TELOS-shaped work is scored

## Key Insights

1. **The shape matters, not just the contents.** A bullet list of goals is *a* goal. A structured file with mission/strategies/narratives/challenges is a state the system can reason against.
2. **The agent reads it on every prompt.** That's the whole point: durable intent means it travels.
3. **Mission is larger than goals.** Goals are sub-targets; mission is the frame that ranks them when they conflict.
4. **Named challenges get routed around.** Vague callouts are ignored. Concrete naming is what the system can act on.

## Related Concepts

- [[Concepts/ideal-state-artifact-isa]] — the per-task instance of durable intent
- [[Concepts/intent-engineering-as-productization]] — TELOS is the durable layer of intent engineering
- [[Concepts/append-only-amber-ledger-capture]] — the input side that grades against TELOS
- [[Entities/lifeos]] — primary productization

## References

- Raw: [[Raw/lifeos-philosophy-telos-2026-10-05]]
- Standalone project: https://github.com/danielmiessler/Telos