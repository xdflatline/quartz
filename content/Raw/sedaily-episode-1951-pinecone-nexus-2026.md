---
title: "Software Engineering Daily — Episode 1951: Pinecone Nexus (Raw Transcript)"
details: "Verbatim transcript of SED episode 1951 (host Kevin Ball, guest Jörg Schad of Pinecone), captured 2026-09-05. Nexus is a 'knowledge engine' that reframes agent context as a first-class precomputed asset — a versioned artifact with its own schema, metadata, permissions, and lineage, analogous to a database materialized view. Covers: (1) RAG's limits (irrelevant retrieval, repeated work, inconsistent answers); (2) the materialized-view analogy — what it buys you (reproducibility, audit, permissions, aggregation); (3) the composition of a Nexus context (vector index + structured schema + knowledge graph + metadata + permissions); (4) semantic-layer integration for term definitions; (5) dynamic tool descriptions that update with each context version; (6) two curation modes (general-purpose vs question-focused); (7) NoQL as the emerging query/response standard; (8) outlook on standards, vertical-integration vs abstraction, and use-case diversity after two months of general availability."
tags:
  - raw
  - rag
  - context-engineering
  - agent
created: 2026-09-05
updated: 2026-09-05
type: raw
source: https://softwareengineeringdaily.com/wp-content/uploads/2026/08/SED1951-Pinecone_2026.txt
---

# Software Engineering Daily — Episode 1951: Pinecone Nexus

**Source:** [Software Engineering Daily — Episode 1951](https://softwareengineeringdaily.com/wp-content/uploads/2026/08/SED1951-Pinecone_2026.txt)
**Date Retrieved:** 2026-09-05
**Type:** Podcast transcript
**Host:** Kevin Ball (KBall) — VP of Engineering at Mento
**Guest:** Jörg Schad — VP of Engineering at Pinecone
**Topic:** Pre-compiled context as a first-class asset for AI agents via Pinecone Nexus
**Mentioned entities:** [[Entities/pinecone]], [[Entities/joerg-schad]], [[Entities/kevin-ball-kball]], [[Entities/arango]], [[Entities/mesosphere]]

---

## [INTRODUCTION — 0:00:00]

**ANNOUNCER:** Retrieval has become one of the central problems in building useful AI systems. The standard approach to grounding a model in one's own data has been Retrieval-Augmented Generation or RAG, where an agent searches a vector database for relevant information at query time. That pattern works, but it has limitations such as retrieving information that's not truly relevant, repeating the same lookup work on every query, and producing inconsistent answers to the same question.

Pinecone is a vector database that's widely used to power semantic search and RAG at scale. The team recently developed Nexus, which is a knowledge engine that reframes context as a first-class precomputed asset rather than something reassembled on the fly. The approach borrows the database concept of a materialized view and curates context once into a versioned artifact that carries its own schema, metadata, permissions, and lineage.

Jörg Schad is the VP of Engineering at Pinecone. In this episode, he joins Kevin Ball for an in-depth conversation about the frontier of retrieval technology. They discuss pre-compiled context, how context artifacts are curated and versioned, much like code, how metadata and semantic layers help agents choose the right information, and much more.

Kevin Ball or KBall is the Vice President of Engineering at Mento and an independent coach for engineers and engineering leaders. He co-founded and served as CTO for two companies, founded the San Diego JavaScript Meetup, and organizes the AI in Action discussion group through Latent Space.

---

## [INTERVIEW]

### 0:02:00 — Background: How Schad ended up at Pinecone

> JS: I was really lucky I could follow my passion, which is probably database systems, where I started out what almost 20 years ago with grad school. Worked on distributed query optimization back in those Hadoop days.
>
> I was over at SAP working on HANA in the early days. And then at some point figured out that large enterprises, maybe they're fun for a while but not for the rest of my life. And joined this startup back then called [[Entities/mesosphere]]. So Apache Mesos. It was like an open-source project somewhere in between open source version of Google's Borg system, their internal cluster scheduler, and kind of like pre-Kubernetes. Built a lot of large scale systems across like Twitter, Netflix, Airbnb.
>
> Went back into the database space. Was a CTO at [[Entities/arango]], which is kind of like a graph database. Interestingly, also worked on early GraphRAG, graph retrieval when that kind of started up. We even built like our own vector store in that where we can maybe come back to a bit later when we're talking about vectors.
>
> And then I've been over at Nextdata also working on how can we connect large scale enterprises with data mesh, with data products to AI and agents.
>
> And I feel now this is actually all coming together in this one role, right? All those passions from data systems, over infrastructure management, over actually connecting creating end user value from agentic systems by combining it with data.

### 0:04:16 — What is Nexus? The "knowledge engine" framing

> KB: Today we want to talk about Nexus and kind of the patterns behind Nexus. How we are designing data, data retrieval, data in different ways for agentic systems. But let's maybe start with just kind of the big overview of what Nexus is solving. What is Nexus? I saw it's described as a knowledge engine. But what does that actually mean?

> JS: If we think about it, knowledge has always been kind of like an after-thought or like an extension of data and databases. The same with actually retrieval — it has always been kind of like in the sense of, okay, I have some data, I want to retrieve something from it. And these things have kind of been auxiliary to actually like main database systems or data systems or whatever.
>
> And I think what we're seeing now, especially with agents, is that retrieval becomes kind of like first-class. It becomes the most important thing. And not only retrieval, but also the knowledge, like the curation of knowledge, how we make that available to agents becomes crucial.
>
> And we kind of took an inspiration from databases — specifically, materialized views. Which is a concept I really like and which is from like, "How can I do something once and reuse it many times? And in particular, it gives me the ability to have like a consistent view on the data and the system over time, basically a snapshot of certain state." And I think there's a lot of similarities when we think about knowledge in agentic systems.
>
> So Nexus is, at the end of the day, a knowledge engine. So we kind of view knowledge as a first-class citizen and then also context as a first-class citizen. And a context in Nexus is — it's like a versioned artifact. It carries its own schema. It has its own metadata. Permissions, which I'll come back to. And also lineage, so I can trace back which dataset version this particular context was built from.

### 0:06:30 — Why "first-class citizen" matters: reproducibility

> KB: Why is it important that context be a first-class citizen? What are the things that having it be its own thing enables?

> JS: I think the most important thing — and the one I personally care a lot about — is reproducibility. If we go back to what we said about RAG, if I'm doing that at each individual query, I'm doing it over and over again. And LLMs or agents therefore, they are just probabilistic systems. They are choosing something on the fly. If I actually care about reproducible results... I really want a consistent answer over time.
>
> If I'm asking my data body a question, "What has been the revenue last year?" I really want a consistent answer over time. I don't want it to be like fluctuating depending on which conditions are being used or what value is being taken for yearly revenue. So that's kind of like the reproducibility aspect.
>
> The second aspect — and the one we already kind of touched on — is more like the efficiency aspect. I don't want to do the same lookup over and over again. I want to do that once and then have it be ready for all my agents. So that's clearly an efficiency benefit.

### 0:08:00 — Permissions, audit, aggregation

> JS: Then there's some other properties. Permissions are a really important one. When we talk about enterprise use cases, we have like highly sensitive data. Maybe I have personal context, like my context. Maybe I have department-level context. Maybe I have company-wide context. And the same approach — for all of those different contexts, I want to have different access controls. Like who has access to which ones, which agent can read which context. And if I make context a first-class object, I can just attach permissions to it, and they can be very different depending on which context we're looking at.
>
> And then there's lineage and audit trails. If I make a decision based on a certain context, I want to be able to trace that back. Okay, what was in that context? Where did that come from? Which dataset version, which permissions, all of that.
>
> And then finally, aggregation. Maybe I want to combine different contexts into one meta-context, which is what I'm using for a particular task. And that's kind of like a really powerful concept.

### 0:09:30 — What does a context actually contain?

> KB: When we talk about a context, what does that actually mean? What is composed inside a context?

> JS: Knowledge context is not like a necessarily single representation. It can be a combination of vector. It can be a combination of structured fields. It can be then also... a knowledge graph... It can contain multiple modalities of data and potentially even the same information in different modalities depending on to support different query patterns.

| Component | Purpose |
|---|---|
| **Vector index** | Similarity search over unstructured content |
| **Structured fields / schema** | Fixed schema for known entities (e.g. customer, product) |
| **Knowledge graph elements** | Relationships between entities — described as a "cheap version of knowledge graphs" |
| **Metadata** | Freshness, lineage, semantic-layer references |
| **Permissions** | Access control at personal / department / company level |

> JS: And I think one thing which is maybe important to mention here — we can also make those descriptions dynamic. So if you think about it, the description of a context can also change with each version. So if I'm an agent and I'm looking at different contexts, I might want to see, "Oh, this context is using this dataset version." Or "this context has a certain freshness."
>
> That helps me as an agent to decide whether to use this context or not.

### 0:12:00 — Tool discovery and dynamic descriptions

> KB: How does the agent know which contexts to pull? Is there a tool discovery mechanism?

> JS: LLMs in general, they are great planners. You give them a tool, and that tool is being described that I can do this. And then if you're not giving them too many tools, they are pretty good at discovering the right tool to use for the right job.
>
> So we have a few tools. For example, "list contexts" is a tool that says, "Hey, I can list all the contexts I have access to." And then "read context" is a tool where I can actually read a specific context. And then maybe also tools that are more fine-grained.
>
> And again, the descriptions of those tools are dynamic. So they update with each context version.

### 0:13:30 — Semantic layer integration

> KB: What about semantic layers?

> JS: Yeah, semantic layers. I think this is a really, really interesting one, and I'm kind of like, I want to see more development in that space. So the thing is, if I'm asking a question, I want to give the agent the right context. But also, I might want to give the agent the right definition of what I'm asking.
>
> For example, if I'm asking, "What is the revenue last year?" The agent should know, okay, what does yearly mean? Is it calendar year, is it fiscal year? And that definition, we think, should be part of the context. Or if not part of the context, then it should at least reference a semantic layer. So that we have like a well-defined understanding of what we're talking about.
>
> I would say right now, we do that internally. So a lot of these definitions are like, baked into the context itself. But I think there's going to be a lot of iteration on how that semantic layer integration works. And it's interesting because this is something that the traditional data warehouse space has dealt with for decades. And now we're kind of like rediscussing those same problems.

### 0:16:00 — Curation: two modes

> JS: There's kind of like two flavors or two modes in which we can curate a context. One is, we have a dataset and we just want to create a general-purpose context from it. So we look at the dataset, we look at the data, we look at what kind of entities are there, and we extract them. We extract maybe knowledge graph elements. We do all of that automatically. We create a structured view on top of it with a fixed schema. And that's kind of like the general-purpose approach.
>
> The other approach is a bit more focused. If I know certain questions upfront, then I can actually create the context specifically for those questions. So I can, for example, take some sample queries and then curate the context based on those sample queries. And then I can also test the context against those sample queries to see if it works well.
>
> And that's a really powerful concept because it allows me to focus on what actually matters for my use case.

### 0:18:00 — Code-like version control

> KB: I'm curious about the version aspect. You mentioned it's versioned. How does versioning work?

> JS: Yeah, so versioning is really similar to how we version code. So we have a version number. We have a description of the changes. And then we have the actual artifact. And then we can roll back to a previous version if we want to. And we can also branch off from a previous version.
>
> So it's very much like a Git workflow. And I think that's a really powerful concept because it allows me to track changes over time. It allows me to roll back if something goes wrong. And it allows me to experiment with different versions.

### 0:20:00 — NoQL: the query language

> JS: One of the things that we've been working on is a query language. We call it NoQL. And it's basically a query language for knowledge contexts. So it's similar to SQL in the sense that it's a declarative language. But it's specifically designed for knowledge contexts.
>
> So if I have a context, I can query it. I can say, "Hey, give me all the customers that have bought product X in the last 30 days." And then the query engine will go and find those customers and return them to me.
>
> And what's interesting is that the query engine itself — and this kind of like again goes back to the materialized view concept — the query engine has a lot of information about the context. It knows the schema. It knows the metadata. It knows the permissions. And so it can make a lot of optimizations.

### 0:24:00 — Vector store vs knowledge graph trade-offs

> KB: In some ways, you've kind of got a vector store, you've kind of got a knowledge graph. How do you decide where each piece goes?

> JS: Yeah, that's a really good question. I think the way we think about it is, we have like a spectrum. On one end of the spectrum, we have like a pure vector store. On the other end of the spectrum, we have like a pure knowledge graph. And then we have like everything in between.
>
> And I think the way we think about it is, we want to make it as easy as possible for the user to express what they want. So if they have like a very structured use case, then a knowledge graph might be the right tool. If they have a very unstructured use case, then a vector store might be the right tool. And if they have something in between, then we can kind of like combine the two.
>
> And I think the way we think about it is, we want to make it as easy as possible for the user to express what they want. And then we can kind of like figure out the best way to actually implement that.

### 0:30:00 — Use cases (two months post-launch)

> JS: We launched Nexus two months ago. And already, we have seen so many different interesting use cases which actually also helped us shape some of the internal implementation. I think that has been a super interesting learning experience for us.
>
> Some of the most interesting use cases we've seen:
>
> - **Customer support**: companies are using Nexus to give their support agents access to a curated context of customer information. So instead of doing a RAG lookup every time, they have a pre-compiled context that they can just read from.
> - **Code understanding**: developers are using Nexus to give their coding agents access to a curated context of their codebase. So instead of doing a search every time, they have a pre-compiled context that they can just read from.
> - **Data analysis**: analysts are using Nexus to give their data analysis agents access to a curated context of their data. So instead of doing a SQL query every time, they have a pre-compiled context that they can just read from.

### 0:42:00 — Standards and vertical integration

> KB: All of this we're kind of talking about a layer that is developing now that is on top of these graph databases, like Pinecone originally was. Or we talked about being on top of a relational database or something like that. Do you see this as being a separated abstract layer that there's going to be a set of different options out there in the world? Or is this something that's going to be tightly integrated and vertically stacked with these kind of underlying data stores?

> JS: I think for us, it's actually we benefit a lot from owning the entire stack. If I look at our implementation at least, we benefit a lot from owning that end-to-end because we can just expose metadata. Freshness metadata for the underlying vector datasets, we know how to get them. We don't have to duplicate that potentially getting out of sync.
>
> Maybe just to give one example. I think for us, we actually benefit from implementing it really end-to-end, and I think this is giving us better performance. I think the other aspect where it's going to come in is governance. We talked about different access, permission levels, different service accounts having access to different things. In theory, yes, you can definitely develop an abstraction layer over that.
>
> I think that will take quite some time to identify what do we all need to expose there. What I would imagine is probably, at the beginning, different people will develop different solutions. And then certain standards are going to evolve. How we're thinking about, I think, for us, the layer which probably is going to standardize first is going to be a little bit on this query front. Of course, the NoQL.
>
> And then from there, let's see where it takes us, right? We can also probably standardize some of the knowledge definition, the knowledge spec. But I said, right now, also just from like a governance perspective, keeping track of lineage. It is a very beneficial for us controlling the entire stack. I would at least give it another two years of iteration. And then maybe we have identified all the patterns, and we can drive that out into a general spec.

> KB: We're very much in this phase of the tech isn't actually good enough yet. And so there's a lot of benefits to squeeze out every piece from that vertical integration. And we'll get to a place where, "Oh, okay. Now we've overserved that. And it benefits us to split it apart and optimize different pieces."

> JS: I think it's going to start at the query front. With query, I mean, actually query and response, right? That kind of format. And then it's probably going to go down to that stack. It's just going to make I think some of the benefits you get from that. Except lineage is I think it's something super helpful to be able to trace it back to the initial days. That's going to get a bit tough if we go into a general abstraction to just get that through these different systems. But who knows, lads? I'm looking forward to talking to you in a year again and see how we've evolved then.

### 0:50:31 — Outlook

> JS: I think the outlook where this is going to grow is we're going to see more and more use of integrations with different semantic layers. I said, right now, we do that internally. We're going to see a lot of iterations.
>
> And I think the other side which we're going to see grow is just more people using it. And I think that's again when we said, "Well, let's talk again in a year." I'm really curious what use cases we'll have discovered in a year.

> KB: It's fascinating how we're all kind of trying to rediscover how do we package data for agents as a primary consumer. And we've talked about a bunch. I think, honestly, the coexistence with the metadata and having that be key both on the definition and retrieval side or query and retrieval, and how all of that tracks, that's a huge step forward. And we talked about semantic layers. I'm hearing all sorts of people were talking about, "Oh, we need much better semantics for agents," because people just put that in their heads, but agents need it right there. Yeah, discovering these patterns of what needs to be collocated now and what needs to be described. It's a fun time.

---

## [END — 0:53:16]

## Key Concepts

- **Materialized view analogy** — pre-compile context once, reuse it many times; snapshot of state rather than a fresh retrieval per query.
- **Context as versioned artifact** — like Git for code: version number, change description, rollback, branching.
- **Composition** — vector index + structured schema + knowledge graph + metadata + permissions, in one context.
- **Permissions as a first-class property** — personal / department / company, attached to the context object.
- **Lineage / audit trail** — every context carries the dataset version and parameters used to build it.
- **Aggregation** — multiple contexts can be combined into a "meta context" for a task.
- **Dynamic tool descriptions** — the agent's tool descriptions update with each context version, so freshness and lineage inform tool selection.
- **Semantic layer integration** — term definitions (e.g. "yearly revenue") attached to or referenced from the context.
- **Two curation modes** — general-purpose (analyze dataset, extract entities, build schema) vs question-focused (build to sample queries, test against them).
- **NoQL** — declarative query language for knowledge contexts.
- **Use cases after two months** — customer support, code understanding, data analysis.

## Related Pages

- [[Concepts/context-as-materialized-view]] — the central pattern (extracted)
- [[Concepts/multi-modal-context-composition]] — the composition of vector + structured + KG + metadata + permissions (extracted)
- [[Entities/pinecone]] — vendor
- [[Entities/joerg-schad]] — guest bio
- [[Entities/kevin-ball-kball]] — host
- [[Entities/arango]] — graph DB where Schad worked on early GraphRAG
- [[Entities/mesosphere]] — Apache Mesos, pre-K8s cluster scheduler
- [[Research/pinecone-nexus-precomputed-context]] — research index synthesizing this episode