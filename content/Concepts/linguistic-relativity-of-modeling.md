---
title: "Linguistic Relativity of Modelling"
details: "William Kent's application of the Sapir-Whorf hypothesis to data modeling: the vocabulary of a language (including any modelling vocabulary) actively shapes which phenomena are perceived as singular entities or relationships. Languages with more nouns or more verbs for a phenomenon produce models that treat it as discrete; the absence of a word renders the thought diffuse."
tags:
  - concept
  - knowledge-management
  - architecture-pattern
created: 2026-09-13
updated: 2026-09-13
type: concept
sources:
  - "[[Raw/bkent-data-reality-excerpts-2026-09-13]]"
---

# Linguistic Relativity of Modelling

**Source:** William Kent, *Data and Reality* (1978/1998), Chapter 12: "A View of Reality" ([[Raw/bkent-data-reality-excerpts-2026-09-13]])
**Category:** Architecture Constraint (cognitive / linguistic)
**Status:** Fundamental

---

## Overview

Building on Benjamin Lee Whorf and Edward Sapir, Kent argues that language is not a passive vehicle for thought — it actively organises perception. For data modeling, the consequence is that **vocabulary determines which phenomena appear as singular entities, which as relationships, and which as diffuse background**.

A language with a noun for "schedule" makes a train-time connection easy to model as a thing; the absence of a noun for the person-salary connection makes that same kind of relationship diffuse and hard to model. A language that has the verb "weighs" makes the weight relationship salient as its own thing; the absence of an analogous verb for colour keeps colour's relational nature hidden.

## Core Content

### Whorf and Sapir, as Kent quotes them

> "Human beings do not live in the objective world alone, nor alone in the world of social activity as ordinarily understood, but are very much at the mercy of the particular language which has become the medium of expression for their society. […] The fact of the matter is that the 'real world' is to a large extent unconsciously built up on the language habits of the group. […] We see and hear and otherwise experience very largely as we do because the language habits of our community predispose certain choices of interpretation." — Sapir, via Whorf

> "Hopi has one noun that covers every thing or being that flies, with the exception of birds […] The Hopi actually call insect, airplane, and aviator all by the same word, and feel no difficulty about it. […] To an Eskimo, [our all-inclusive word 'snow'] would be almost unthinkable; he would say that falling snow, slushy snow, and so on, are sensuously and operationally different, different things to contend with." — Whorf

### The modelling implication

> "We are more ready to perceive things as entities when our language happens to have nouns for them. […] The accidents of vocabulary: we are most prepared to identify as entities or relationships those things for which our vocabulary happens to contain a word."

Kent's examples:

| Phenomenon | Has a noun/verb in English? | Modelling consequence |
|------------|----------------------------|----------------------|
| Connection between a train and a time | Yes ("schedule") | Easy to model as a singular entity |
| Connection between a person and a salary | No | Diffuse, hard to model discretely |
| "Has weight" relationship | Has a verb ("weighs") | Easy to treat as a distinct relationship |
| "Has colour" relationship | No analogous verb | Diffuse; lumped with "has" |
| "Has height" relationship | No analogous verb | Diffuse |

### Why this is a problem for data modelling

If modelling vocabulary precedes the phenomena, the model will be biased toward what is easy to name and away from what is hard to name. Two equally real phenomena can be modelled at very different levels of fidelity, not because one is more important but because one is easier to verbalise.

The reverse problem: a language (or modelling vocabulary) that splits a phenomenon into many fine-grained nouns (Eskimo words for snow) will tend to produce models that reify distinctions that a language with a single noun would flatten. Neither is "correct"; both shape what is salient.

### Relationship to brain-style preference for data models

Kent speculates (in *Points of View*) that the relational-vs-hierarchical-vs-network tribalism of database research may track cognitive style — visual, verbal, network-oriented thinkers prefer different models. The linguistic-relativity principle extends this: each modelling vocabulary selects for the cognitive style that finds it natural.

## Key Insights

1. **Modelling vocabulary is not neutral.** It predetermines which phenomena are salient.
2. **The absence of a word is as consequential as the presence of one.** Diffuse phenomena get modelled diffusely.
3. **Verbs matter as much as nouns.** Verbs make relationships salient as their own things; their absence collapses relationships into "has".
4. **No modelling vocabulary is correct, only more or less suited to the purpose.** Whorfian relativity implies that even a perfect grammar of reality would still leave out something another grammar would capture.
5. **The model is partly a measure of the modeller's language.** When two teams produce different models of the same domain, the difference is partly the difference in their modelling vocabulary.

## Related Concepts

- [[Concepts/map-vs-territory-data-modeling]] — the underlying claim that motivates linguistic relativity in modelling
- [[Concepts/three-worlds-ontology-amorphous]] — the three-worlds framing places language as a layer between reality and computer
- [[Concepts/data-model-as-tool-not-theory]] — models are tools; linguistic relativity shapes the tool
- [[Concepts/reconciliation-by-scope-and-purpose]] — disagreements between teams may partly be disagreements about vocabulary

## Related Entities

- [[Entities/william-kent]]
- [[Entities/data-and-reality]]

## References

- Raw Article: [[Raw/bkent-data-reality-excerpts-2026-09-13]]
- Original: https://bkent.net/Doc/darxrp.htm#A%20View%20of%20Reality