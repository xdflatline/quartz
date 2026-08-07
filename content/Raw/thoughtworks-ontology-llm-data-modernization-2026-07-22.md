---
title: "Closing the context gap: An ontology + LLM approach to data modernization"
details: "Thoughtworks blog post by Zichuan Xiong (2026-07-22) proposing a six-step agentic loop that pairs per-source ontologies with LLM-driven semantic analysis to find and classify context gaps in enterprise data modernization. Illustrated with a customer-churn use case over billing and support systems."
tags:
  - blog-post
  - llm
  - agent
  - knowledge-management
created: 2026-08-07
updated: 2026-08-07
type: raw
source: "https://www.thoughtworks.com/insights/blog/legacy-modernization/an-ontology-LLM-approach-to-data-modernization"
author: "Zichuan Xiong"
published: 2026-07-22
---

# Closing the context gap: An ontology + LLM approach to data modernization

**Source:** [Thoughtworks Blog](https://www.thoughtworks.com/insights/blog/legacy-modernization/an-ontology-LLM-approach-to-data-modernization) ([Zichuan Xiong](https://www.thoughtworks.com/profiles/z/zichuan-xiong))
**Date Retrieved:** 2026-08-07
**Type:** Blog Post

---

Enterprise data modernization aims to turn a tangled data landscape into domain-driven capabilities the business can build on. Yet many modernization programs stall long before delivery because teams spend months trying to understand what their data actually means.

The data strategist connects business intent to a modern data architecture. Their work spans the full lifecycle: navigating a complex enterprise data landscape, designing and prioritizing use cases, identifying gaps between business needs and the available data, delivering the new capabilities and continuously discovering.

The challenge is that much of an enterprise's knowledge is scattered across systems or exists only in the heads of subject matter experts. As a result, discovery becomes slow, manual and difficult to scale.

## The ontology + LLM approach

Our first instinct is to point an LLM straight at the problem: feed it the source systems, describe the use case and ask it to find the gaps. It is a reasonable starting point, and it exposes a real limitation.

Without explicit semantic context, the LLM must infer relationships from schemas, column names and sample values. Those inferences can be useful, but they are difficult to verify consistently at enterprise scale. So we asked: can ontology help here?

To answer that question, we first need to understand what an ontology contributes that raw schemas cannot.

## What is an ontology?

An ontology is a schema of meaning: it defines the entities that exist, their attributes, the relationships between them and the rules that govern them. Instead of meaning living tacitly in an SME's head or being inferred on the fly, an ontology gives computers a way to reason about a domain in a logical, consistent and controlled way. It is the schema layer of a knowledge graph, before any instances, such as entities as nodes, relationships as edges, etc populate it. The whole artifact is both human- and machine-readable: editable, auditable and able to be kept under source control.

## Why does combining ontology and LLMs matter?

Ontology and LLMs cover each other's weaknesses. The ontology grounds reasoning in explicit semantics, making outputs more explainable, consistent and easier to verify. The LLM, in turn, does the work that would otherwise make ontologies are tedious to build by hand: reading source systems, aligning synonyms, proposing reconciliations, spotting mismatches.

Ontology without AI is a modeling exercise that still costs months of manual analysis; an LLM without ontology is fast but unreliable. Together, the strategist can express intent and supply as structure and have an agent find the gap between them — quickly, and in a form the strategist can trust and verify.

## A step-by-step example

The approach becomes much clearer when viewed as a repeatable workflow. Rather than treating discovery as a one-off exercise, it continuously enriches enterprise context with every new use case. In practical terms, this method operates as an agentic loop consisting comprised of six distinct steps (Figure 1.). To illustrate, we can apply this agentic workflow to a common data use case, forecasting customer churn, leveraging data from two source systems.

### Step 1: Build ontological context per source

The first step is to make each source system's meaning explicit. We provide sample files for each system and extract its context through an AI agent: entities, attributes, relationships and the rules that govern them.

The agent reads across signals in each file: schema and data types, foreign keys and join patterns, sample values and any comments or documentation, then infers a candidate ontology and flags low-confidence guesses for an SME to confirm. The output is a machine-readable, auditable artifact, not a slide.

In this case, let's assume the two source systems (billing and support) exposed the following ontological context:

```
# --- Source System 1: Billing System ---
Account -Subscribes to-> Plan
Account -Billed by-> Invoice
Account -Has status-> BillingStatus
Account -Has email-> EmailAddress

# --- Source System 2: Support Ticketing System ---
Customer -Raises-> Ticket
Ticket -Assigned to-> Agent
Ticket -Has status-> TicketStatus
Customer -Has email-> EmailAddress
```

### Step 2: Curate context across sources, then reconcile

In reality, context must be reconciled across multiple sources. Reconciling multiple ontologies highlights inconsistencies such as duplicate identities, conflicting definitions and overlapping concepts that would otherwise remain hidden. These require a human expert to recommend and resolve.

In the same case, the context curated from the two source systems surfaces three potential gaps (Figure 2.) to close:

- EmailAddress is shared by two ontologies.
- Account and Customer may be the same real-world entity.
- BillingStatus and TicketStatus share the type Status.

These gaps are use-case agnostic. They exist in the landscape whether or not any use case cares about them, which is precisely why a human expert or an AI agent can be made aware of them up front.

### Step 3: Compare the design context against the curated (reconciled) context

Source systems are only one side of the equation. Business use cases also have an implicit understanding of the entities and relationships they require. Representing that intent as an ontology allows the two to be compared directly. Let's use a churn-forecasting use case as an example:

> For each customer, predict the likelihood they will stop paying for the service in the next billing cycle, so the retention team can intervene before the customer leaves.

To do this, the model needs a single, unambiguous Customer entity that unifies a person's commercial relationship (what plan they are on, whether their payments are current, how long they have been a customer) with their behavioral signals (how recently they have logged in, how many support tickets they have raised and whether those tickets were resolved) — all keyed to one resolved identity and observed over time.

In ontology terms, the design context is a Customer carrying churnRisk, joined to Subscription, Invoice, and support-interaction history, all resolved to one identity and observed over time.

By matching this design context against the curated, reconciled context from Step 2, the previously use-case-agnostic gaps become practical.

### Step 4: Identify the gaps

Now we can read what each gap actually means to the churn use case:

- Gap 1: EmailAddress shared across ontologies. For churn, email is the join key that stitches billing and support histories to one customer. This isn't noise, it's the reconciliation the model depends on. It becomes an identity-resolution requirement.
- Gap 2: Account vs. Customer. The use case depends on whether these represent the same business entity. Resolving that question determines both the target of prediction and the underlying data model.
- Gap 3: BillingStatus and TicketStatus sharing type Status. A shared type does not mean shared meaning. Status = closed is a healthy outcome for a ticket and a churn signal for billing. Collapsing them into a single concept would corrupt the label. This is a semantic-collision gap: the same type, opposite implications.

Once the strategist understands what the gaps mean to the targeted use case, they can take action.

### Step 5: Take actions

Gap analysis will decide the action.

- Gap 1 is an internal reconciliation: define email as the resolved identity key and curate the join. Fast and internal.
- Gap 2 requires an SME decision on the customer grain, then a modeling change to the curated Customer entity. Low engineering cost, but it needs human judgment before code.
- Gap 3 is resolved by disambiguating the shared type into distinct, context-qualified concepts (BillingStatus vs. TicketStatus as separate meanings) so the churn label isn't polluted.

The "three gaps" resolve into three genuinely different plans: a reconciliation rule, an SME grain decision and a semantic disambiguation, with different costs, different owners and a dependency order between them. The strategist knows all of this before committing a quarter to the build.

While AI can identify and classify potential gaps, governance remains essential. Business owners and domain experts are responsible for validating entity definitions, resolving semantic conflicts and approving changes that affect enterprise-wide data models.

### Step 6: Update the source context and loop

Once actions are taken, the enterprise's understanding itself changes. Context is not static: schemas evolve, new systems come online, definitions drift and the actions from Step 5 themselves change the landscape. So this is never a one-off exercise. When a strategist closes a gap and delivers the use case, that change in context must be captured. Here, resolving EmailAddress into a shared identity key, unifying Account and Customer, and disambiguating Status, all mutate the curated context, which becomes the new baseline, the next use case and the next agent to inherit rather than rediscover. Re-running the diff confirms the churn gaps are closed; if a source changed or a new gap surfaced, the loop continues from the new state.

This is why context must be managed as a service at the landscape level, not a document or one-time snapshot. Rather than documenting enterprise knowledge in static design documents, organizations can maintain it as a living, version-controlled semantic asset that every future project and AI agent can reuse.

The arc is the whole thesis in miniature: explicit context in, a classified and traced gap out, an action attached, the context updated and a landscape left more capable than before.

## Summary

A data strategist's job in a modernization program is to navigate a complex data landscape, design and prioritize use cases, find the gap between each use case and the available data, close those gaps and deliver durable capabilities in a modern architecture.

The hardest and slowest part is the middle: building a reconciled understanding of scattered, tacit meaning and analyzing gaps by hand, and it is where programs lose months and credibility.

The ontology + LLM approach attacks exactly that middle. Ontology makes meaning explicit and gives context a graph structure; the LLM reasons over that structure to find gaps in a form the strategist can verify rather than trust on faith. The result is an agentic loop: context per source, curated context across sources, comparison against the use-case design, classified gaps, traced actions, update and repeat. It can significantly reduce the manual effort required for discovery by automating large parts of semantic analysis while leaving business decisions to human experts.

As organizations adopt AI across the enterprise, success increasingly depends on providing systems with trusted business context rather than simply more data. Combining ontologies with LLMs offers a practical way to make that context explicit, reusable and continuously improving, allowing data modernization efforts to deliver value faster while building a stronger semantic foundation for future AI initiatives.

*Disclaimer: The statements and opinions expressed in this article are those of the author(s) and do not necessarily reflect the positions of Thoughtworks.*
