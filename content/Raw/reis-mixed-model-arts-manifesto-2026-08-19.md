---
title: "The Mixed Model Arts Manifesto — Joe Reis"
details: "Full text of Joe Reis's Substack manifesto (Aug 19, 2026) calling for Mixed Model Arts (MMA): a unified, first-principles discipline of data modeling that spans OLTP and OLAP, rejects the Kimball/Inmon and normalized/denormalized tribalisms, treats models as evolving lifecycles rather than deliverables, and is explicitly designed for both humans and AI agents. The article introduces the metaphor (mixed martial arts settled \"my style beats your style\" by unifying all styles around fundamentals) and enumerates nine core beliefs: modeling is one discipline; model the territory not the technology; intent drives structure; time is non-negotiable; semantics are the universal interface; simplicity is a discipline; designed for humans, engineered for agents; modeling is a lifecycle; avoid dogma, be pragmatic."
tags:
  - raw
  - knowledge-management
source: "https://practicaldatamodeling.substack.com/p/the-mixed-model-arts-manifesto"
authors:
  - "Joe Reis"
publication: "Practical Data Modeling (Substack), 2026-08-19"
created: 2026-09-14
updated: 2026-09-14
type: raw
---

# The Mixed Model Arts Manifesto

**Author:** Joe Reis
**Published:** 2026-08-19 on *Practical Data Modeling* (Substack)
**Source:** https://practicaldatamodeling.substack.com/p/the-mixed-model-arts-manifesto
**Subtitle:** A Unified Discipline for Modeling Systems, Data, and Meaning in the Age of AI

*Note:* "A historically accurate image of Martin Luther nailing his manifesto to the door." — original article caption

---

## A Call for Practical, Cross-Disciplinary Data Modeling

In an era when data proliferation outpaces our ability to derive meaning, traditional data silos - application development versus analytics, rigid normalization versus flexible denormalization, etc. - have become liabilities. We are drowning in data yet starving for knowledge, with a widening chasm between the inputs we record and the insights needed to act on them.

The Mixed Model Arts (MMA) Manifesto is more than a technical framework. It marks a critical evolution in how we construct our digital reality in the Agentic Era. As AI agents increasingly participate in reasoning and decision-making, our data models must move beyond serving human consumption alone. They must become durable, semantic foundations that machines and humans can trust and use.

This MMA Manifesto matters because it shifts the focus from ephemeral tools and methodology wars to first principles, treating data modeling as a single, continuous, and essential discipline that bridges raw data and actionable intelligence. It provides the clarity needed to fight technical debt, reconcile our fragmented practices, and design systems that can thrive in an autonomous age where both humans and machines produce and consume all forms of data across a variety of use cases.

## Data Modeling Is a House Divided

We are still fighting battles from decades ago: Kimball vs. Inmon, normalized versus denormalized, and application models versus analytical models.

Developers throw data over the wall to analysts and data scientists. Established modeling practices are dust in the wind, forgotten to the void of time. Convenience outlasts expertise. The same ideas are reinvented in isolation, often for no good reason.

The result is a widening gulf between data (the recorded inputs) and knowledge (the meaning required to understand and act on them).

In the age of Agents, that gulf must close.

Mixed Model Arts (MMA) is the unified practice of modeling across all systems, all forms of data, all data shapes, and all use cases. It grounds data modeling and first principles rather than tools, platforms, or methodological camp.

### Why "Mixed Model Arts"?

In the 1990s, mixed martial arts settled centuries of "my style beats your style" arguments. The answer wasn't one discipline. Instead, it was all of them, unified by fundamentals and adapted to context.

Data modeling is having its MMA moment.

The old wars are over. Train everything. Apply what works.

## Core MMA Beliefs

1. **Modeling is One Discipline.** We reject the artificial wall between siloes, such as application development and analytics. Whether OLTP or OLAP, code or warehouse, the foundations remain the same: entities, relationships, identity, grain, time, and semantics. Different contexts, unified physics.

2. **Model the Territory, Not the Technology.** We model the business reality first, and the technology implementation second. Tables, streams, and graphs are just implementation details. The model must reflect the real-world entities, attributes, relationships, and events.

3. **Intent Drives Structure**. Data is not static; it has a job to do. Models must explicitly encode Operational Intent (how the business acts) and Analytical Intent (how the business learns). A model without clear intent is just technical debt in waiting.

4. **Time is Non-Negotiable.** Everything is temporal. State is an illusion; change is the reality. Ignoring time creates chaos; modeling time creates coherence. If you cannot answer "when" and "in what order," you cannot understand "why."

5. **Semantics are the Universal Interface.** Meaning makes models durable. Meaning enables interoperability. Meaning is the only thing that allows humans and AI to communicate without hallucination. It is the bedrock of organizational memory.

6. **Simplicity is a Discipline.** Complexity is the default state of entropy; a good model fights entropy to deliver clarity. We do not simplify by removing necessary detail, but by organizing it so that the complex becomes intuitive.

7. **Designed for Humans, Engineered for Agents.** The era of humans-only consumption is over. We now model for human cognition *and* agentic reasoning. Models must provide the context machines need to take autonomous, reliable action.

8. **Modeling is a Lifecycle.** No model is "finished." We iterate, refactor, and evolve in real-time alongside the business. Modeling is not a phase; it is a continuous practice of aligning systems with reality.

9. **Avoid Dogma. Be Pragmatic.** Understand the various data modeling approaches, why they're used and where they're applicable. Pick what works for your situation.

## The Mission

Mixed Model Arts reunites the fragmented craft of data modeling and gives practitioners a shared discipline spanning all use cases for humans and machines.

Mixed Model Arts isn't just a framework. It's where we train modelers, design systems, and turn data into durable knowledge.

This is where the next generation of modeling begins.

— Joe Reis

---

## Selected Comments

### Larry Burns (Aug 25, 2026)

> All this makes sense, and echoes many points I've made in my own writings on data modeling. To me, the biggest sea change that is occurring is where semantics (i.e., meaning) lies. In the past, we might capture semantic data in our data modeling tool as part of our modeling efforts, but it was never used. All the semantics, all the meaning of the data, resided inside the application code. The data model was only used to generate the physical persistence schema, and perhaps some covering views.
>
> Now, in the age of Agentic AI, semantic data (or metadata as we might call it) must exist independently of both the database schema and the application code, so that it can be consumed mechanically. This, I think, represents a real opportunity for the modeling community. If our modeling tools can be somehow enabled to accommodate both data requirements and data meaning, if our tools could generate both persistence schemas and ontology documents, then a single modeling exercise could generate all the artifacts needed to create data that can be consumed by both human and AI agents.
>
> Data modelers and tool vendors alike need to become aware of these opportunities, and strive to take advantage of them!

### Guy Kerem (Aug 24, 2026)

> Amen. Care to expand on "Semantics are the Universal Interface"? Would you say demand leads to new popular interoperable ontologies emerging?

*(9 more comments in the original thread — not captured here.)*
