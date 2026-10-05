---
title: "LifeOS: Glance (Philosophy)"
details: "The judgment system: every fuzzy call the code makes, asked as one small typed question with a probability back in about a tenth of a second. Backed by Jev, a model that answers decisions instead of generating text — 18 small questions routing every prompt, calibrated against 1,000 real conversations."
tags:
  - raw
  - agent
  - evaluation
source: https://ourlifeos.ai/philosophy/glance/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# Glance

**Source:** [https://ourlifeos.ai/philosophy/glance/](https://ourlifeos.ai/philosophy/glance/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# Glance

Every fuzzy call the code makes, asked as one small typed question with a probability back.


Fig. 10·Six questions, one batch, one threshold

Glance is the judgment system. Anywhere code has to make a fuzzy call, like whether a message is urgent, whether a prompt is a correction, or which model should take a piece of work, it asks Glance one typed question. It gets back a probability and a plain answer to “may I act on this?”

## Why it exists

Code handles exact questions well and fuzzy ones badly. The usual fix is to send the fuzzy question to a language model with a long prompt and parse whatever text comes back. That’s slow, it costs real money per call, and it’s hard to test: one big prompt carries a dozen instructions at once, and when the answer is wrong there’s no single part to fix.

Glance turns each fuzzy call into the smallest question that can be asked about it, answered with a number, in about a tenth of a second. A small question can be tested on its own. When one gets an answer wrong, you sharpen that question or add another one, the same way you fix a bug.

## How it works

The engine underneath is [Jev](https://typesafe.ai/), a model that returns decisions instead of text. Every question takes [one of three shapes](https://danielmiessler.com/blog/jev-choice-vs-score). A noul asks whether something is true and returns the probability that it is. A choice picks one option from a set that has no order. A score places the answer on an ordered ladder, like low, medium, high.

Glance owns everything around the engine that makes an answer safe to use:

- A registry lists every caller, its questions, and the threshold each answer has to clear before the caller may act.

- A daily budget per caller caps how much each one can spend.

- A ledger gets one line for every call, including failed ones. It never stores the question’s input or the key.

- Many items are asked in parallel as a batch, never one by one in a loop.


A new caller starts in shadow. Its answers are logged next to what actually happened, and it always gets “do not act,” so an agreement rate builds up before anything relies on it. A caller moves to enforce only through a registry row that records the agreement rate, the date, and the Jev model it was measured on. If that model changes, the row goes back to shadow on its own.

One prompt, routedeighteen small questions instead of one big one

AskedThe prompt and the end of the last reply, with eighteen yes/no questions about the work, the effort, and the follow-up.

→

AnsweredEighteen probabilities in one call, about a third of a second.

→

ComposedTwo small learned models turn them into a lane and an effort.

**Measured on 1,000 real prompts:** its lane matched a three-model answer key on 90.1% of them, against 75.2% for a single frontier-model call reading the same rules, scored on conversations it never trained on.

## Routing every prompt: model and effort

The biggest Glance caller is [the router](https://danielmiessler.com/blog/glance-routes-model-and-effort). Every prompt gets two separate decisions before any work starts: which model should do it, and how hard that model should think. The smartest model isn’t always the one that needs to think hardest, so the two are picked independently.

The model is the lane:

| Lane | Model | What it gets |
| --- | --- | --- |
| Inline | the current session | Work that needs this conversation’s context, or is quick |
| Luna | OpenAI, light | Super basic tasks a script could almost do |
| Terra | OpenAI, mid | A decided approach with only small local choices left |
| Sol | OpenAI, heavy | Settled work whose pass/fail test you could write before starting |
| Opus | Anthropic, workhorse | Most work, including max-level work at xhigh effort |
| Fable | Anthropic, top | Second opinions on max-level work |
| Astra | OpenAI, flagship | Exhaustive coverage and needle-in-a-haystack searches |

Effort is the second pick, and it measures how hard the task needs thinking, never how big it is:

- low→ mechanical work with no deliberation. rename, reformat
- medium→ routine work that needs ordinary care. the default
- high→ real reasoning: several considerations, or correctness that's easy to get subtly wrong. hard problems
- xhigh→ the hardest judgment: strategy, architecture, security-sensitive design, or your own depth words. max

Every model-and-effort pair maps to something that actually runs it. The OpenAI lanes take effort per call, as a flag on `Worker.ts <lane>`. The Anthropic agents take it from their definition, so each routed effort has its own generated agent:

| Model | low | medium | high | xhigh |
| --- | --- | --- | --- | --- |
| Opus | Opus | OpusMedium | Opus | OpusXHigh |
| Fable | not routed | not routed | FableHigh | Fable |
| Astra, Sol, Terra, Luna | `--effort low` | `--effort medium` | `--effort high` | `--effort xhigh` |
| Inline | stays in the session | stays in the session | stays in the session | stays in the session, and the turn enters the full loop |

A few guardrails sit on top of the matrix. Deploys, secrets, auth, migrations and irreplaceable data never go below Sol. Your own depth words (“think deeply”, “go deep”) mean Opus at xhigh plus the thinking skills. And a task only goes to Sol, Terra or Luna when its brief names what done looks like and which files to touch; otherwise it goes up a rung.

### How the router asks

Glance asks Jev eighteen yes/no questions about each prompt, with the end of the previous reply as context, in one call. Nine are about the work: does it change something, does it need exhaustive coverage, does it touch deploys or secrets, is it a review, could a script do it, is the approach decided, does it need real reasoning, is taste the heart of it, would an expert find it hard. Five are about effort, and four are about how the prompt relates to the last reply: approving it, only reacting, correcting it, or starting something new.

Two small learned models turn those eighteen probabilities, plus whether the prompt uses depth words, how long it is, and whether there was a previous reply, into a lane and an effort. Work leaves the session only when the chance of a hand-off is at least 50%. A frontier-model classifier remains as the fallback, used only when Jev can’t answer.

### How it was tested

- 57%→ one big seven-way choice question agreed with the classifier then in use on only 57% of live prompts. too big a question
- 85.3%→ nine small questions and a learned combiner on 144 hand-written test prompts. looked great
- 42.6%→ the same model on real prompts, which are mostly short follow-ups like "do it." the wrong test set
- 76.3%→ three blind labelers (Opus, Fable, Astra) agreed on only 51.8% of real prompts until three rule ambiguities were settled. the rules were the ceiling
- 90.1%→ eighteen questions on 1,000 real prompts, scored only on conversations the model never trained on. shipped

| 1,000 real prompts | Glance | Frontier-model classifier | Always stay inline |
| --- | --- | --- | --- |
| Lane | **90.1%** | 75.2% | 83.9% |
| Stay in session vs. hand off | **91.0%** | 77.3% | 83.9% |
| Effort | 70.0% | 72.5% | n/a |
| Handed off when the key says stay | **22** of 113 | 199 of 334 | 0 |
| Time per prompt | **about 0.3 s** | about 3.3 s | none |

The answer key comes from three models from two vendors, Opus, Fable and Astra, each labeling every prompt blind; a prompt’s key is the lane at least two of them chose. Every percentage in the table is how often a picker matched that key. Glance’s lead over the always-inline baseline holds up in a paired test at more than five standard errors, and its lead over the classifier at more than nine. Effort is a tie. The weakest number is naming the right model once work should leave the session, where Glance gets 52.6%, because only 156 of the prompts were real hand-offs.

## Where it fits

Glance is the second of four [verification tiers](https://ourlifeos.ai/philosophy/assay) LifeOS uses. Every check sits on the lowest tier that can honestly answer it:

- code→ a tool that exits zero or doesn't. The only tier allowed to block a deploy. exact
- glance→ one typed question, answered with a probability in about a tenth of a second. fast judgment
- assay→ a model reading an output against written levels, in seconds to minutes. See [Assay](https://ourlifeos.ai/philosophy/assay). slow judgment
- human→ you, recognizing the thing when you see it. taste

Checks move down the tiers as they earn labels. A human check becomes a Glance question once there are labels to calibrate it against, and a Glance question becomes code once it is sharp enough to be a tool.

## What it feels like

On a busy day the system makes more than a thousand of these calls, and none of them hold anything up. The router decides where your prompt should go before the reply starts. A mail sweep checks a hundred messages in under a second. And when one of those calls is wrong, the fix is a specific question with a specific test, which is a lot better than editing a paragraph of prompt text and hoping.
