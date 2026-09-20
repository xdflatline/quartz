---
title: "Data Modeling Philosophy — Kent (1978)"
details: "Research synthesis of the foundational philosophy of data modeling as articulated by William Kent in Data and Reality (1978, reissued 1998). Five interrelated concepts — map vs. territory, three-worlds ontology with amorphous reality, models-as-tools, reconciliation by scope and purpose, and linguistic relativity of modelling — together form a coherent position: any data model is a partial, audience-specific, vocabulary-shaped tool whose adequacy depends on its purpose and the scope of its community."
tags:
  - research
  - knowledge-management
created: 2026-09-13
updated: 2026-09-13
type: research
sources:
  - "[[Raw/bkent-data-reality-excerpts-2026-09-13]]"
---

# Data Modeling Philosophy — Kent (1978)

**Updated:** 2026-09-13
**Source:** [[Raw/bkent-data-reality-excerpts-2026-09-13]] — William Kent, *Data and Reality*, 1978/1998

---

## Overview

This research index organises the philosophical foundations of data modeling as articulated by William Kent in *Data and Reality*. The book is short (~100 pages in the original North Holland edition) but unusually concentrated: Kent argues, with accumulated examples rather than formal proof, that **no data model is the territory it describes, that reality itself is amorphous and view-dependent, that data models are tools rather than theories, that the practicality of sharing a view depends on scope and purpose, and that the vocabulary of any modelling language shapes what is salient**.

The position is older than the relational debates of the 1980s and orthogonal to them. It is also orthogonal to most modern object-relational, graph, and document debates — Kent's claim is that all of these are maps of the same amorphous territory, and that the choice between them is a tool-selection question (cost vs. utility for a purpose), not a truth question.

The book's relevance today — to LLM-driven ontology construction, knowledge graphs, and AI-assisted data modernisation — is direct: the same problems Kent names (viewpoints, ambiguity, naming, amorphous reality) reappear at every level of automation.

## Concepts

### Foundational / metaphysical

- [[Concepts/map-vs-territory-data-modeling]] — "the map is not the territory" applied to data structures; every model is a partial approximation
- [[Concepts/three-worlds-ontology-amorphous]] — reality, language, and computer data as three nested layers; reality at bottom is amorphous
- [[Concepts/linguistic-relativity-of-modeling]] — vocabulary actively shapes which phenomena appear as singular entities or relationships

### Practical / epistemic

- [[Concepts/data-model-as-tool-not-theory]] — evaluate models as economic, incomplete, versatile tools rather than as theories with truth values
- [[Concepts/reconciliation-by-scope-and-purpose]] — the practicality of shared views depends on the number of people (scope) and breadth of the question (purpose)

## Tools & Projects

### People

- [[Entities/william-kent]] — author, database researcher; active in 1970s/1980s standards committees

### Books & Articles

- [[Entities/data-and-reality]] — *Data and Reality*, North Holland 1978, 1stBooks 1998 reissue

## Raw Sources

- [[Raw/bkent-data-reality-excerpts-2026-09-13]] — full excerpts from bkent.net: Preface (1978), Preface to the Second Edition (1998), Chapter 12: Philosophy (Reality and Tools, Points of View, A View of Reality), and contemporary review blurbs

## Key Threads / Sources Table

| Source | Topic | Date | Key Items |
|--------|-------|------|-----------|
| [[Raw/bkent-data-reality-excerpts-2026-09-13]] | Data modeling philosophy | 1978 (reissued 1998) | Map vs. territory; three-worlds ontology; tools vs. theories; reconciliation; linguistic relativity |
| Mike Senko | Blurb | 1978 | "All data base researchers should read this document" |
| Reiner Durcholz | Blurb | 1978 | "Frequently quoted", "penetration into major data base technology headaches" |
| G.M. Nijssen | Blurb | 1978 | "Highly recommended and even required reading for all DP people" |
| Datamation | Review | 1979 | "The most important things… are philosophical and go right to the heart" |
| Current Engineering Practice | Review | 1979 | "Equally important to systems analyst, database designer, system designer" |
| ACM Computing Reviews | Review | 1980 | "Critical, probing approach to the difficulties of modeling reality" |
| Quantitative Sociology Newsletter | Review | 1981 | "A book that poses problems and exposes contradictions" |
| European Journal of Operations Research | Review | 1981 | "Attacks the pseudo-exactness of existing data models" |
| Joe Celko | Letter | 1998 | "Using Data and Reality as research material" |
| Robert Meersman | Letter | 1998 | "Has a message even — or especially — for today's jaded information scientists" |
| Roger Burkhart | Letter | 1998 | "Issues still not being dealt with in our formalized information systems" |
| Haim Kilov | Letter | 1999 | "Foundational nature"; "essential component of our intellectual foundation" |
| Richard Soley (OMG) | Letter | 1999 | "A pleasure to have Bill's calming influence" |

## Cross-Cutting Themes

### 1. Ontology is necessarily partial

Kent's central move is to argue that no model — relational, hierarchical, network, object-oriented, ontological — captures the territory. The territory is amorphous. The map/territory distinction is therefore not a failing of one particular modelling tradition; it is a property of all of them. Modern ontology work (RDF, OWL, SKOS, LLM-assisted ontology construction) inherits the same constraint: every ontology is a map shaped by its vocabulary and its scope.

### 2. Tools are not theories; choose accordingly

A practical consequence: data modelling decisions should be evaluated on economic grounds (does the tool's problem-solving value exceed its production and maintenance cost?), not on truth grounds (is this the "correct" model?). Tools are orthogonal to problems — the same tool solves many problems, and many tools solve the same problem. This framework generalises beyond databases: any formalism (a programming language, an ontology language, a configuration schema) is a tool, and should be selected as one.

### 3. Brain-style and tribalism

Kent's speculation that the relational-vs-hierarchical-vs-network tribalism of the 1970s/80s may track cognitive style (visual / verbal / network-oriented thinkers) anticipates a recurring pattern: technology choices are often identity choices. The same dynamic appears in modern debates (relational vs. document, monorepo vs. polyrepo, REST vs. GraphQL). Kent's frame is sociological rather than technical: which model is "natural" depends on which brain is asking.

### 4. Viewpoint reconciliation degrades with scope and purpose

The most operational of Kent's claims: shared views are achievable for narrow purposes among few people; broad purposes across many people expose latent disagreements. This predicts that information systems succeed in their initial scope and tend to break as scope and purpose grow — which is the lived experience of nearly every enterprise system. Designing for declared scope and purpose is a partial mitigation; the deeper fix is to instrument reconciliation explicitly rather than assume it.

### 5. Vocabulary shapes what is modelled

Linguistic relativity in modelling means that the modeller's vocabulary pre-selects which phenomena are salient. If you do not have a word for a phenomenon, you will not model it as a thing. This is a soft constraint on every modelling effort, and it has a modern LLM analogue: prompting with a richer vocabulary produces richer outputs, because the model's responses are conditioned on the vocabulary you supplied.

## Next Research Directions

- [ ] **Compare Kent's reconciliation-by-scope-and-purpose with modern data fabric / data mesh governance models** — both attempt to make scope explicit; what is gained and lost?
- [ ] **Survey LLM-assisted ontology construction projects (cf. [[Concepts/ontology-llm-data-modernization]]) for linguistic-relativity effects** — does the LLM's vocabulary shape which ontologies are produced?
- [ ] **Read the rest of *Data and Reality* (Ch 1–11, not excerpted on bkent.net)** for the construct-by-construct analysis Kent applies to entities, names, relationships, attributes
- [ ] **Locate Mealy's "Another Look at Data"** — Kent cites it as a 10-year-old classic at the time of writing (1978); re-read with the benefit of 2026 hindsight
- [ ] **Survey Whorf's *Language, Thought, and Reality*** for the stronger version of linguistic relativity that Kent invokes
- [ ] **Compare Kent's "tools vs. theories" framing with Brian Cantwell Smith's *On the Origin of Objects* (1996)** and with Fred Brooks's "No Silver Bullet" — all attack pseudo-exactness from different angles
- [ ] **Compare Kent's framing with Reis's Mixed Model Arts (2026)** — see [[Research/mixed-model-arts-reis-2026]]. Reis explicitly re-articulates Kent for the modern data stack: MMA Belief 2 (model the territory, not the technology) restates the map/territory principle; MMA Belief 9 (avoid dogma, be pragmatic) restates the tools-vs-theories distinction; MMA Belief 5 (semantics as the universal interface) is the operational form of Kent's three-worlds ontology. The Agentic Era is the forcing function Reis names for unification.