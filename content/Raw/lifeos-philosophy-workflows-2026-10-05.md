---
title: "LifeOS: Workflows (Philosophy)"
details: "Work with known steps, written down as one YAML graph and run on your machine or in the cloud. Each step names an executor (Code, Judgment, Model, Human, or another Workflow); data flows through declared JSON-Schema-checked mappings; deterministic where possible, bounded where not."
tags:
  - raw
  - agent
  - orchestration
  - tooling
source: https://ourlifeos.ai/philosophy/workflows/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# Workflows

**Source:** [https://ourlifeos.ai/philosophy/workflows/](https://ourlifeos.ai/philosophy/workflows/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# Workflows

Work with known steps, written down once as a typed graph and run on your machine or in the cloud.


Fig. 08·Single-purpose units, chained, started by a trigger

Workflows is the LifeOS system for work that follows known steps. A workflow is a small graph written down as one YAML file: what starts it, what each step does and who does it, what each step hands the next, and what the whole thing returns. The same definition runs on your machine or on [Cloudflare Workers](https://workers.cloudflare.com/). It takes [the Unix idea](https://danielmiessler.com/blog/the-unix-philosophy) seriously: small units with clear jobs, composed through a shared contract, leaving work visible enough to inspect.

## Why it exists

Useful work often starts as a one-off: collect something, check it, make a decision, put the result where it belongs. Repeating that by hand is wasteful, and handing it to an unconstrained agent is worse. The missing middle is a system that runs when it should, does only the work it was designed to do, and makes its result easy to check.

Seen this way, [a company, or a life, is a graph of algorithms](https://danielmiessler.com/blog/companies-graph-of-algorithms). Writing the graph down is what makes it possible to run it on time, check it, and improve it.

## How it works

Every step names who does it. There are five kinds of executor:

The executorswho does each step

CodeAn action or a command with a typed input and output.

→

JudgmentOne typed question to [Glance](https://ourlifeos.ai/philosophy/glance), answered with a probability and a verdict.

→

Model or agentA model call or an agent session, held to an output schema.

→

HumanA decision by a person, returned as approved or not, with a note.

A fifth kind of step runs **another workflow** as a single step.

Data moves between steps only through declared mappings, each checked against a [JSON Schema](https://json-schema.org/). Before anything runs, the definition is validated: the graph has no cycles, every reference points at a real earlier step, and every connection between steps fits. The graph stays deterministic even when a step is not. A model can decide what a summary says, but it cannot decide what shape the next step receives.

A workflow starts on request, on a schedule, once at a set time, every N minutes, on a named event, or after another workflow finishes. When one workflow follows another, the first one’s output has to fit the second one’s input, or validation fails and names both.

The smallest unit is an **action**: one job with a narrow input and output contract, small enough to understand without reading the rest of the system. In the cloud, actions run as their own Workers, and flows own a source, a schedule and a destination. The flows hand-code their orchestration today; the migration moves it into typed definitions.

## Deterministic work and judgment

Most operational work should be deterministic: apply rules, validate, route, store, check. The same input should produce the same behavior, with a result you can inspect later.

Some work genuinely needs a model. Workflows keeps that bounded too: a model step names its input, its lane and the schema its output must fit. Over time steps should move toward code. A human step becomes a judgment, a model step becomes a rule, and the mix of executors on the dashboard is how that drift is measured.

A real shapea reading digest as one workflow

CodeFetch new items from the sources you follow.

→

CodeValidate and de-duplicate, deterministic and inspectable.

→

ModelScore each item against your stated interests, held to a schema: classify and rank, nothing more.

→

CodeDeliver the top items to your dashboard and store the rest.

**A schedule trigger** runs it every morning. Every run writes one line to the run ledger: what came in, what was kept, what the model decided, and whether it succeeded.

## Where it fits

Workflows also keeps the inventory of every piece of work LifeOS already runs, wherever it runs: background services, scheduled agent jobs, cloud Workers, project crons and typed definitions. It checks what is declared against what is installed and what actually ran, and draws the result on [Pulse](https://ourlifeos.ai/philosophy/pulse). Each entry carries a card with six answers: what it does, what it reads, its steps and who does them, the procedure it follows, what it produces, and where that goes.

[The Algorithm](https://ourlifeos.ai/philosophy/the-algorithm) defines and verifies what done means; Workflows runs bounded pieces of that work when their trigger arrives. [Vigil](https://ourlifeos.ai/philosophy/vigil) reads the expected cadences to notice when something stops running, and [Bunker](https://ourlifeos.ai/philosophy/bunker) is the harness the shipped apps run in.

## What it feels like

Work you used to redo by hand starts arriving already done, and you can still see inside it. When a result looks off, you read the run: which step, which input, which decision. Fixing it means changing one step, not re-prompting a black box and hoping. Over time you build up a shelf of small, trusted machines, each one boring in exactly the way infrastructure should be.
