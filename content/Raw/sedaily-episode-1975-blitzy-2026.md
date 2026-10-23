---
title: "Software Engineering Daily — Episode 1975: Blitzy (Raw Transcript)"
details: "Verbatim transcript of SED episode 1975 (host Kevin Ball, guest Sid Pardeshi, CTO and co-founder of Blitzy), captured 2026-10-23. Blitzy is an enterprise-only autonomous software development platform that pre-builds a knowledge graph of an entire codebase (24-48 hour reverse-engineering pre-run) so agents can query it, then runs multi-coordinator agent swarms through pre-planned, checkpointed review stages to produce a reviewable pull request. Covers: (1) why large codebases break today's coding agents (context window effective limits, ~30k lines); (2) the graph database as shared source of truth and agent-recruited scope; (3) multi-coordinator swarms without a single orchestrator; (4) the agent action plan as reviewable spec; (5) multi-model routing with cross-model tiebreaking for scope convergence; (6) billing on final lines of code; (7) autonomous product operation against metrics; (8) harness-enforced security as the control point for LLM-written code."
tags:
  - raw
  - agent
  - coding-agent
  - orchestration
created: 2026-10-23
updated: 2026-10-23
type: raw
source: https://softwareengineeringdaily.com/wp-content/uploads/2026/10/SED1975-Blitzy.txt
---

# Software Engineering Daily — Episode 1975: Blitzy

**Source:** [Software Engineering Daily — Episode 1975](https://softwareengineeringdaily.com/wp-content/uploads/2026/10/SED1975-Blitzy.txt)
**Date Retrieved:** 2026-10-23
**Type:** Podcast transcript
**Host:** Kevin Ball (KBall) — VP of Engineering at Mento
**Guest:** Sid Pardeshi — CTO and co-founder of [[Entities/blitzy]]
**Topic:** Autonomous software development at enterprise codebase scale via a knowledge graph and multi-coordinator agent swarms
**Mentioned entities:** [[Entities/blitzy]], [[Entities/sid-pardeshi]], [[Entities/kevin-ball-kball]], [[Entities/claude-code]], [[Entities/codex-cli]], [[Entities/nvidia]]

---

## [INTRODUCTION]

**ANNOUNCER:** Codebases and enterprise organizations often span hundreds of thousands or even millions of lines of code. In many cases, changes must follow established patterns precisely, or risk introducing costly security or operational issues. A common challenge with AI coding tools is that they struggle at this scale. LLM context windows cover only a fraction of a large codebase, and output quality degrades the longer an agent runs.

Blitzy is an autonomous software development platform for the enterprise. It starts by understanding your entire codebase, building a knowledge graph that acts as a shared source of truth. From a well-defined spec that engineers review and approve, it orchestrates specialized agents that work in parallel to build, review, and test code autonomously at scale. The result is a pull request that engineers can then review and merge.

Sid Pardeshi is the CTO and co-founder of Blitzy, and he previously worked at NVIDIA. In this episode, he joins Kevin Ball to discuss why large codebases break today's coding agents, how a knowledge graph extends what models can reason about, how a reviewable plan keeps specialized agents aligned, and where autonomous software development is headed.

Kevin Ball, or KBall, is the Vice President of Engineering at Mento and an independent coach for engineers and engineering leaders. He co-founded and served as CTO for two companies, founded the San Diego JavaScript Meetup, and organizes the AI in Action discussion group through Latent Space. Check out the show notes to follow KBall on Twitter or LinkedIn, or visit his website, kball.llc.

---

## [INTERVIEW]

### 0:01:56 — Background: from NVIDIA to Blitzy

> KB: Sid, welcome to the show.
>
> SP: Hey, KBall. Thank you for having me. Just to quickly introduce myself, I'm Sid Pradeshi, CTO, co-founder of Blitzy. I've been at NVIDIA since 2016, back when NVIDIA's adjusted market price was a few cents. And it was not the trillion-dollar company that it is. It was nowhere near that. And when I told people I work at NVIDIA, they said NV Media. You didn't get a job at Google, huh?

NVIDIA operated so much like a startup, and it was a fun journey. I lived through - I saw the AI wave happen and I lived through it. And I saw how Jensen was a visionary. During that wave, I realized what an incredible opportunity this is for applying AI to the world of software development, particularly autonomous software development. And that's how Blitzy was born and that's why I'm here.

### 0:02:50 — What Blitzy does: enterprise-only, one-shot delivery

> KB: Well, let's give us a little bit of an overview of Blitzy. What do you all do? And what's the - don't give me all the secret sauce, but what's the unique take?
>
> SP: Yeah. Blitzy is an autonomous software development platform. So people are used to platforms like [[Entities/claude-code]], [[Entities/codex-cli]], which are more tools or even tools like Devin or Factory. The way we're different is that we specialize on very large enterprise jobs. Unlike the other platforms, we are enterprise only. And we have enterprises designing their entire SDLC around us.

So what happens with the other tools is that they're really great at taking bite-sized chunks of work that humans can delegate to, right? They give them tasks. Many of them position themselves as junior engineers or interns, like Devin, for example, right? Claude Code, for example, is a terminal tool that you can run micro projects with. But the vast majority of the work at the enterprise, about 80% of it, is well-defined work, especially with legacy enterprises, with very large-scale enterprises. It's very well-defined work that was reviewed by a designer, that was reviewed by an architect, was documented. It's ready to pick up exactly what the acceptance criteria is, exactly what the process is to get from development all the way into production, right? And it's just sitting there waiting to be done.

And the humans that need to work on it, they're juggling across models. It's so unpredictable. Opus 5.5 just released yesterday, and it solved some of the problems that Opus 5 had. But opus 5, a lot of people struggled to work with it. It changed so many things about the model. GPT on the other hand has a different product, right? What you have is engineers find themselves optimizing their prompts, building their skills, hopping between tools, trying out the different models that come out, finding new ways to work with them, finding fit between the features and the prompts and the tools and workflows, etc.

The other tools, they've changed what engineers are doing, but they haven't changed the fact that engineers still have to do things and sit there and babysit the tools and the agents to get work done. Where we're fundamentally different is you take that spec you have, you give it to Blitzy, you press build, and you're done. You go and do other things. You go and use the other tools, you go and do other more important things. And Blitzy does all of the work for you correctly, exactly as a person who's been on your team for like 30 years has been doing. It understands exactly the right way you implement things because it does this batch learning across your entire codebase when you're onboard, understanding and mapping out all of the patterns, relationships, identities across the entire codebase, and then applying those at runtime using the right model for the right time.

We use Opus, we use GPT, we use a large variety of models and model sizes. And we always deploy the right model for the right job. It's all about - for us, we're not optimizing for cost. We're optimizing for quality. What we want to do is when you get the PR back, it is correct. It is as close to correct as possible. And what our customers have seen is that majority of the times we are at least - we've saved 80% of the time that you needed on the project to get to production. And the remaining 20% is often because we didn't have some access. You're not comfortable giving us that level of access. We didn't support some integration. Or there's just other processes or policies that your team follows before you get something to production. We map against production. We're enterprise only. And we focus on doing all of the work one shot. That's how we're different.

### 0:06:26 — What "enterprise only" means: size, standards, stakes

> KB: Awesome. I want to dig into a few pieces of that. But first, let me say I love the focus on quality. This is the thing I constantly challenge my team on in my day job of like, hey, a lot of folks are using these tools to pump out a lot of things faster, but at a lower level of quality. How do we do the same amount of work at a higher level of quality? What do we do to up the level with it?

Let's maybe start a little bit with what the enterprise only ends up meaning what you get to do differently because of that, right? If you look at an enterprise customer, what differentiates them from selling to a developer or a small company?

> SP: Yeah, very good question. So I would say there's two fundamental things, and we'll talk through more as we identify them. One is that the challenges and the kinds of code bases an enterprise is looking at are very fundamentally different than someone who's working on a hobby project or vibe coding. One is the size. Two is the expectations and the standards, right. If I don't follow a style guide on a hobby project, that's fine as long as it works. I'm not going to complain on a day-to-day basis.

And the enterprise, if I make a mistake in the style pattern or if I make a reckless change that ignores a pattern that's well-established and required, or I make a compliance error, or I introduce a security vulnerability that doesn't take into account all of the constraints you have, or even a load balancing defect, or a performance concern, that item, if I introduce that with my shortcutting and not following standards, that means material cost in dollars as the code progresses through steps, right? Someone has to spend more time reviewing it. Someone has to spend more time testing it. And then, ultimately, if it gets to production and the customer is impacted, the business has lost dollars.

The stakes are really, really high. The complexity is high. You're not looking at a 10,000 line codebase or 20,000 line codebase. You're looking at at least hundreds of thousands of lines for a small enterprise and tens of millions of lines for the largest enterprises just for a single product. They have multiple code bases at that scale that they are actively maintaining with hundreds of committers and thousands of committers.

The scale, the complexity, the standards, they're all really high. The sizes of the projects and the features you're building are also very high, but it's a very high tax. For example, if I have to make a 20-line change in a codebase, I may think that I could get away with, let's say, a simple agent that maybe sets thinking to medium and gets the job done. But the requirements of that enterprise is that we've already added the libraries or the logic that does this. And that logic or that pattern is buried deep into millions of lines of code. And we don't want you reinventing the wheel for that.

So finding that just at the right moment and then doing it exactly the right way, that's the hard part, right? That's the big challenge that we're pushing ourselves to solve day and night and we've solved to the most extent.

### 0:09:44 — The context-wall problem and the knowledge graph

> KB: That problem is hard for humans, right, to map out millions of lines of code and understand where it is. Let's talk then about the start of the process, right. Because you mentioned a little bit, hey, we go and we ingest a lot of what's going on so that you know, oh, what is that one library off in the weeds that should be used for this? So what does that look like at Blitzy?
>
> SP: Yeah, so if you look at how far models have come, right. Models are really intelligent these days. But where do they fall down? They fall down at the context level. They have 1 million tokens of context, which maps to about 100,000 lines of code. But here's the kicker, every token in the context window needs to map to every other token by a dot product in the matrix. And there's no amount of compute or trick that you can apply that does this effectively across the entire context window.

Most of the model providers that you have, Anthropic, OpenAI, they have the effective context up to less than 300,000 tokens, right? And they're applying techniques like sparse attention, sliding window attention or something else across the rest of the window. This is also why, for example - now this is not the official reason. But if OpenAI has a pricing differential at 272, 000 tokens, when you send more than that, it's a long context request. You get charged more.

But because of that fundamental gap, as soon as you send more than 30, 000 tokens, more than 300,000 tokens in the request, which maps to 30,000 lines, intelligence degrades. That's why as you run these single-agent tools, for example, the CLI tools or the single-agent persona tools, quality degrades as they are more long-running, right? The encouragement from all the providers is to do short-running jobs.

Now, the way we solved this is that we invented a graph database system that maps your entire codebase by identifying its relationships and understanding what every file in the codebase is doing. And understanding the structure, like, okay, this code base has 20,000 files, but here are the modules that are structured, right? Here's what this file is doing in this module. Here are the features that live in different parts of the codebase, right?

If I'm looking for authentication, these are the functions and these are the patterns that the enterprise is using across the entire codebase. And we do that free run in about 24 to 48 hours when you start working with us. So it's not like you turn on the terminal and you start working just like Claude Code. There is a cost and there is a pre-run. You have to go through that pre-run. But the benefit is we've now mapped out the entire codebase and represented it structurally.

For example, let's say you want to find a pattern in a codebase that's 30 million lines, and there's tons of products, there's so much noise. Claude Code, Cursor, any other tool, they're going to try to use grep or some variant of grep and try and find it, but there's so much noise. So the agent is going to burn tokens and hopefully find the right one. But what we've seen in many of these code bases is sometimes there's deprecated stuff in there that's not even marked deprecated.

How do you know that you found the right item without actually profiling the code, without actually running the code, without having reverse engineered the entire codebase? That's exactly what Blitzy does first. But reverse engineering it and saving those markers in the graph database is contextualized. Even memory, for example, right? Memory for the other tools are files strewn across the codebase. You don't see it because it's in Claude's projects folder, but you can go and see it if you like.

But then finding the right memory for the right module or file at the right moment, that's the hardest part, right? By having the graph database represent that structurally, semantically, and naturally, you have a massive advantage. The magic of Blitzy is really just making it easier, drastically easier for these models to operate within their effective context window effectively.

### 0:13:56 — Signals beyond AST: building and running the code

> KB: Yeah. No, I'd love to dig in one level deeper without asking for any secret sauce on this. But I think I've been experimenting with an open source graph database tool for my coding agents, and it does make a huge impact. Thinking about that, you sort of alluded to it's not just the structure. You could use a deterministic tool, compile this to an AST, map the dependencies and have that surface that up. But there's more that you're talking about here because you were talking about, oh, we're putting some weights on this. We're saying, oh, this one's actually - it's not marked deprecated, but it's not actually used. What are the different signals you're looking at and how do you expose those to the agent?
>
> SP: We're actually trying to build and run the code, right? And we're actually mapping out what is the piece of code that's used based on what the agent can observe. We're looking at not one file, but the entire codebase. And at that scale, when you have like 20,000 files, identifying which file is relevant and which is not, it's hard, right? There are, for example, graph database solutions. There are even open source versions of those implementations. But it's really, really hard to solve for the entire codebase. And that is what we've invented and solved, right.

Inventing and solving and building a system that is reliable at scale and works for any language and is actually able to pull that context reliably and make it helpful for the agent and not actually distract it, that is the hard part.

### 0:15:23 — The agent's interface to the graph

> KB: Oh, absolutely. That's what I'm wondering about. And as I said, without going into secret sauce, what does that query approach look like? Are you exposing a full graph language? Is it a sort of semantic tool? What does the agent actually interact with?
>
> SP: So the agent has tools that let it search the graph database. For example, we also employ semantic summarization. We save embeddings of summaries and let agents search that. The agent is writing cipher queries that is traversing the graph. It's identifying what is the best way to query this. The agent has an understanding of the graph database's schema, right? And it knows the kind of information that it can get and the kind of information it can save in case it finds an inconsistency. If something changes, what happens? How do you update the graph? That kind of stuff. Giving the agent access to the schema as well as access to the kinds of queries it can make and tools it can call, that's what makes all the difference at inference time, right?

### 0:16:31 — Memory that was earned from someone else's mistakes

> KB: Yeah, awesome. All right. Anything else interesting from the kind of ingestion process? How are you pre-processing this code to give your agent full knowledge that we should talk about?
>
> SP: I think memory, as I said, is one of the most important items. What happens with memory is - in today's world, memory has to be earned. So you have to have used the product to be able to earn that memory, right? And then save it. And so you have to get hurt to know how not to get hurt that way. But magic happens when you're not able to get hurt in the first place because you learned from someone else's memories, right.

A few ways we approach this. One, when we look at the commit history and we try to understand what journey has this code been through in getting here, right? And how can we imbibe that and follow that process so that when we write something, it lands on the same planet that the customer expects, right?

The other is the customers often use agents.md, skills.md, Claude, et cetera. Learn from those, apply those. But again, identify the context of when they're actually relevant, right? So saving that information, understanding the tech stack, summarizing that, compounding that over multiple levels, that starts paying dividends as you start going, right? You can make fewer mistakes with the customer's input. Because, to be fair, humans and/or users are not the best at giving it the most clear instructions, right? So to really deliver value, you need to be able to understand and interpolate instructions that were never provided.

### 0:18:11 — One graph, not many: contextualizing commits, patterns and tasks

> KB: Yeah. That's super interesting. I've done some amount of like, oh, let's analyze my previous sessions. What do I get out of that? Things like that. But you're looking across essentially their entire history of this project and saying, oh, where were the things that had to be reverted? What were the missteps? What was the journey?

During that process, can we talk a little bit about what does the - are there like certain sets of signals you're looking for? What does the compiled version of this look like? Is it coming down to a set of guidelines, or is this another graph of searchable practices? Or what does this look like?

> SP: We're embedding this into the actual graph. So we try to replicate the structure of the entire codebase. And the problem that you have is, as you correctly described, you can create multiple graphs, right? You can create a graph of the commits, commit history. You can create a graph of the file structure. You can create a graph of the folders, et cetera. But the problem is, how do you tie all that information together? And then how do you provide that to the agents in a digestible format where they can operate efficiently, quickly?

What we're doing is we use a structure that maps to the structure of the codebase. And then we actually process all of those commits as much as we identify are relevant. And we apply the learnings from those commits to the nodes of the graph. So you don't have multiple graphs that you're trying to deal with. You have all the information contextualized.

And another unique aspect, something that we perfected really early on where the rest of the industry has yet to catch up, it's not even being discussed, is running agent swarms without a coordinator. The existing model is you can run swarms with there's one coordinator and tens of agents. In fact, research, current research has proven that if you run multiple agents in parallel, it's really hard to ground them and to get them to not overlap and do things - solve the shared goal, because the other agents can have multiple opinions.

We run all of this processing in parallel and use multiple coordinators at different levels to achieve the shared goal consistently and reliably. There's a different agent, for example, that's focused on crawling the graph. There's another agent that's focused on integrating that just in the right place and handing off to the next agent at the right point. So that, I think, is one of the hardest problems that we have to solve early.

### 0:20:42 — The graph as the coordination substrate: scope documents and agent recruitment

> KB: Yeah, so let's dig into that a little bit. Because, as you highlight, you can have a single centralized orchestrator, but that breaks down fairly quickly. How do you deal with collisions, ownership, handoffs? What does that look like in your agent swarm?
>
> SP: We use the graph database as the source of truth because that changes everything. What happens is you can use, for example, disk - but disk is volatile. As soon as I change the folder, as soon as I kill the pod or destroy the location, it's gone. You can use git, but you could destroy the beauty of the commit history and you can have a very cluttered workspace that makes it incredibly hard to find information. It's one thing to dump information. It's another completely different to retrieve it intelligently, right? The graph database helps you do both by structuring it on the graph, by contextualizing it at runtime and then structuring it on the graph. What you can now do is use that structure to recruit agents.

For example, if your graph is based on folders, you can assign agents to folders and limit scope. Once you have a scope document, you can break down the scope and then distribute it based on a structure that's anchored on the graph. What that does is it couples us to the graph, right? Whatever we do has to be on the graph, which is a trade-off. But the benefit is that you can run as many agents as you like. There is no theoretical limit to how many agents you can run in parallel as long as you solve the compute behind it.

### 0:22:16 — The synchronization primitive: claimable nodes and dependency ordering

> KB: Let me dig into that a little bit more. We already talked about when you do your analysis of history and things like that, you're attaching that to the graph. I'm assuming that's some sort of either metadata or a distinct type of node attached to the code node in some form. Now you're saying, okay, we're going to also attach tasks or desired transformations or something like that also to the graph. And now those are claimable. And agents can just come in and say, oh, I can do this part. I can navigate this. Does this require you to deal - what is the synchronization primitive? Oh, I have a dependency here. I need this part of the graph to be complete before that can go. Does that mean I have to claim this whole piece or does that mean I do this and then someone else can claim that? What does that end up looking like?
>
> SP: That is another hard problem we had to solve. So we have dedicated steps for synchronization, where if you've completed - all of this is pre-planned. When you're running a job, first figure out what is the review process. For example, with any other tool, you have to - Claude just finished working on the tool. Now let me do a code review. And then, okay, the code review is done, let me do a security review. Security is done, let me run a test agent that tests everything. I have to ask it to do this every time. It's not going to do it on its own.

For us, we do that out of the box by default. You don't have to ask Blitzy to test what it did. And again, whether or not it needs testing is completely dynamic. That is also agent determined. By deciding what is the path to production, by being an enterprise only product, what you can now do is just focus on production. And then you decide what the checkpoints are, what the stages are for synchronization, when you should do it, what you should be checking at that point, and what are the expectations and acceptance criteria at each of those stages. And then you can just drive the agents through it until you have something that is shippable, at which point you can hand off to the human.

### 0:24:12 — Reconciling the graph with the SCM

> KB: Yeah. So let's walk through that process a little bit more, right. If I think about - and because I'm not deeply familiar with Blitzy, I'm mapping this to my mental model of an orchestrator. Let's use the example you use. I have an orchestrator handing things off to Claude Code. It says, hey, go and implement this. Okay, I got back. It's implemented. Hand it to a reviewer. What does that review phase look like for you? Is it also somehow tied into the graph? Do you have to have versions of your graph? Because now you're saying, oh, this is in this branch. It's still under review. What does that end up looking like?
>
> SP: Yeah, so we anchor on the SCM for progress. And so that is the progress in terms of the work done. And there's the agent work stream that is in flight, right? And there's a scope of the review based on the expectation of what should be complete at this point. So the review as a process is anchored on the graph, the results of which are committed onto the SCM. And so throughout the process, when you have a workflow that needs to be run by the agents, that is mapped and tracked onto the graph. And again, the results are captured into the SCM. In case you pause the system at any point, you can reconcile both and know exactly where you are in the overall journey.

### 0:25:34 — Security review as a default stage

> KB: And does that then continue on through - you mentioned security review. What does security review look like in this context?
>
> SP: Security review, the thing is you don't want to be writing any code that introduces security vulnerabilities, right? With the Mythos scare that everyone had, especially because we're working with banks, you have to guarantee that the code that Blitzy writes is free from issues. By default, you have another set of agents watch the works that are being done, catch security issues, and schedule security checkpoints to make sure that - let's say those issues were temporary, maybe it was a scratch that the agent wrote, and it lasts, we discard that later. So let's make sure that happens and that gap doesn't make it into production. Or two, when we plan this feature, you're introducing a new API. I got to make sure that it follows the existing authentication patterns, that it follows load balancing and follows all of the core items that you follow, not just from security, but also from a housekeeping standpoint.

Let's do that testing. Let's do adversarial testing. Let's try to break the system and product before someone else tries to do it. And let's flag that. Maybe there's a design gap that no one else saw. It's Blitzy's job to make sure that it exposes that. If that item is out of scope, it documents that. If it considers that this should be addressed as part of the same job in scope, it would go ahead and adjust that.

### 0:26:58 — Out-of-scope findings: document, don't explode the surface

> KB: Documenting is interesting. I think one thing to map back to a human process, as you're doing work, you often uncover future work. You're like, oh, this is out of scope for this project. I don't want to explode my scope. I don't want to explode my surface area. But I found this. We should really fix this. Does that end up getting resurfaced to a human to decide? Does Blitzy schedule itself future work to do those cleanups? What does that end up looking like?
>
> SP: Yeah, you're onto something here. So we're working on the ability for Blitzy to file tickets and schedule itself and to be given a goal and recursively self-improve itself to achieve that goal. But what we do at the moment is at the end of Blitzy's work stream, we have two things. One, a project guide that documents all the work that Blitzy did and all the work that it could not or decided not to, right? So that includes these findings. And that also affects the completion percentage if it was an in-scope item.

The second item is the PR review experience where it walks you through all the changes that it did but just focuses on the key changes so you don't have to review 500 files. You can review like 50 files and you understand the work that was done. Because if I have 100 files just with unit tests and you know they're all green and you know how they were written, you don't need to review my unit tests, right? You're focused on getting this to production. Using those two items, a user is able to feel more confident while approving the changes, reviewing it and move faster to the review process.

### 0:28:31 — Keeping human mental models current: docs-first crawl-walk-run

> KB: So that kind of raises another interesting question. I feel like one of the things that many of us are struggling with right now with AI-generated code is how do we keep our mental models of our systems up to date, right? It's great to have it working. But if I want to understand how I can evolve the system well, I need to understand the underlying structures.

And I think in an enterprise setting, you have a lot of existing structures. Highlight Blitzy is very good to kind of respecting those, but sometimes things need to evolve. Sometimes things need to change. And especially if you have a long-lived codebase, there may be pieces in there where like, hey, this is hairy. We don't want to build in - even though everything is depending on that, new code should not look like that. We want to shift our model. We want to do things. Kind of how do you handle keeping the brains of the humans up to date with what Blitzy is doing for them?
>
> SP: Yeah, there's multiple strategies. So for example, especially we run into that use case a lot where I have this, but don't do that. That was a dark past. Don't follow that. So again, even when we look at comments, it's about recency. You may have one pattern earlier on, maybe years ago, and you maybe have moved on to a new pattern or a new technology framework more recently. Recency is weighed into the factorings of that agent that applies patterns.

But other than that, we have knowledge base, which is one of the features. As you onboard and give Bitsy more code, it documents all of those branches and its understanding of those branches via Xpec, right? So it's a living document of what that code contains. So you can look at it. And as you update and resync code, that document gets updated.

If you need to understand what any branch in your entire codebase does, you can look at that knowledge base and you can understand it. And then the more tactical items that our forward deploy engineers work with customers on is creating documentation and keeping that documentation up to date using Blitzy, right. What is the current state? What are the best practices? Before running a massive project, what makes the most sense is we follow this crawl, walk, run approach where we suggest that you start with documentation.

Let Blitzy confirm its understanding of your entire codebase. Let us reverse engineer and let us show you what that looks like. Move on to adding testing, right? Because how do you validate the work that Blitzy did or anyone else did, right? Let's increase test coverage, and let's add that.

And then what those two things do is now it's much easier to describe acceptance criteria, right? It's much easier to explain to a human what that code does. And it's much easier even for Blitzy once the human has actually reviewed the documentation to validate its understanding and make sure it's on the right track.

So by doing that - and then again, if there are any caveats by capturing that in the agent action plan, sometimes there are conflicts to what the human thinks is in the code and what they asked us to do, or even in their own prompt. So flagging that early and making sure that's addressed. Those are some of the tactical things that you can do to make sure that the cost of this item is reduced.

### 0:31:42 — Legacy code as the beloved customer

> KB: Yeah, that makes sense. Well, and it's interesting, again, with the enterprise context, because long-lived companies often have parts of their codebase that are poorly understood at best. Maybe behave in odd and unexpected ways, but then there's downstream dependencies. I think my favorite definition of legacy code is untested code, right? And so this idea of, hey, first, let's validate our understanding, both with documentation. But you may not have anyone who can verify that documentation. So let's write tests that show what the system actually does.
>
> SP: Yeah, I think our favorite moments and the customers that love us most are the ones who have a lot of legacy code and a few people who can understand it. It feels amazing when you have architects who have been there for like 35 years, you have COBOL developers who no longer write that, and having them validate the code and really express satisfaction that Blitzy is able to understand and operate in a way that they would. I think that's the best part of building and working with Blitzy.

### 0:32:49 — Course correction: resuming from the graph, not the transcript

> KB: Let's talk about another thing you mentioned here, which is how course corrections happen, right? No matter how good the system is, there will be mistakes, there will be stuff, and you have this human review process to check and verify. Let's say something goes wrong. What does the correction structure look like? How does that get parsed, represented, et cetera?
>
> SP: Yeah, so I think you bring up a very important point. And part of my frustration with working with other tools has been that you blew up all of the context writing the project. It's like 700K tokens, and it's done the work. And now, to do the next task, let's say you have to compact. So what happens is that it forgets many times the work that it is. Even though you have the plan, right? The plan is like a two-pager. The work is maybe tens of thousands of lines, if not hundreds of thousands of lines. How do you reconcile that, right?

So again, because all of the work that Blitzy does follows the graph, right? The graph that it updated on the fly corresponding to the branch, we have a massive advantage. The way we operate is you saw the PR. We found some gaps. We have a workflow called Refine PR. And what that does is that it resumes the process, including the graph. It preserves the history, preserves the history from both the graph and the SCM and addresses your feedback. And the best part is that we bill on lines of code, right? So we don't charge you for mistakes that we make. Everything that you give us feedback on is a mistake.

What that means is if by addressing your items, lines of code in your resulting PR went down, you will only be charged for the final lines of code. So let's say Blitzy went off and wrote 500,000 lines of code and when you were only expecting 300,000 and then -

> KB: Sounds like a Claude project.
>
> SP: Yeah, recent Claude project. Although, I hope they fixed it with the recent models. You found that 200,000 lines were just comments and fluff that you don't agree with that you didn't ask for. Fine, you can ask it to clean that up and then you only get billed for the correct answer. That I think is very unique and special for Blitzy, and I think is the right model for the enterprise because there's a lot of token anxiety these days. The tokenomics and the fluff of let it rip, burn all you can is all gone, right? Enterprises know that they need to be cost conscious with these things. Because if you let it run wild, the wheels are going to skyrocket. And I believe we position our product and our pricing exactly with that idea in mind.

### 0:35:25 — The convergence problem and cross-model tiebreaking

> KB: Yeah, I like that a lot because it aligns all of your incentives towards let's write the right code, not all the possible code. A couple of things that that actually brings to mind. So one is sort of the convergence problem. And this is a problem that Anthropic models have been more vulnerable to, but I've seen it on GPT models as well and other things, which is agents love to find one more thing to do. So you go, you build a thing, review it, oh, you haven't thought about this thing. Okay, right. Okay, I'm going to go and build it. Okay, you haven't thought about this. And eventually it's like telling you, hey, once every Tuesday in July, this is going to break in this way. How do you within Blitzy say this is the line? This is what's enough. We're done.
>
> SP: I think you highlighted a very, very important problem. It's not just Anthropics. It's a problem with a wide variety of models. And people believe it can be solved. Prior art thinks that you can tweak it with, let's say, prompt tuning or with effort tuning. Hey, if you think it's doing too much, just drop the effort level. But it doesn't really solve the problem, right? Because the way these models work, if there's one thought in there that is going to let it think about finding new problems or have it document one thing it found, you can't go back and change that unless you really edit the conversation, which is not something a regular user does. It's a really hard problem.

But the way we solve it is, at any point of time, we use different models. The beauty of using different models is that you get fresh perspectives and you can align on the stronger model to be the tiebreaker. We have internal evals and benchmarks. We know which model is relatively stronger for decision making or which model is relatively stronger for front end and then so on and so forth.

By applying that at runtime, so even if Claude thinks that two things worth flagging or this item is load bearing in typical Claude speak, you have GPT come in and check and say, nope, that's not in scope. That's not what the agent action plan says. And GPT is more effective because it's doing less. Claude has the burden here of implementing everything. It has blown up its context. It's operating probably in the ineffective side of its context window, right? It's loaded up with more than 300k tokens.

GPT in this case was only looking at the AAP. And because it had to deal with much less constraints, it did a more effective job of identifying the scope. This is a very vague example, not what we actually do, but we do something very similar across many models. And we arrive at the correct answer to what the scope should be.

Before the user sees it, that job has been seen by at least eight different models. And all of those models are specialized at the task that they do. And they've been proven to be the best at that particular task, right? So imagine switching across eight different products locally to do one task, right? That's painful. It's not something you want to do. And you're going to have to maintain your environment and prompts and instructions for all of them. You don't have to do that because you use Blitzy.

### 0:38:38 — Choosing models: internal evals, tag-ranked ladders, runtime routing

> KB: So that is interesting and a nice segue into another question I had. So you're multi-model, which is great. I think that's definitely an advantage being independent from the - right now, a lot of the harnesses are tied to a particular model set and things like that. Being independent, letting you pick and choose is phenomenal. How do you decide which models to use for what? I think you mentioned internal evals. What does that process look like and how does it evolve?
>
> SP: Yeah, so we work very closely with labs, model providers, inference providers. And whenever a model is launched, we run it internally, benchmark it. We run it in the platform. We test how it's doing. We score it. And then we apply those learnings to decide which is the tiebreaker. But at runtime, the process is entirely dynamic. We have these ladders and rungs. We have dynamic selection of the models. We have switches and routing in place based on capacity, based on intelligence, based on task specificity. And the agent chooses the LLM for the next agent based on the task. It chooses the system prompt. It chooses the tools. This is literally agent designed by agents.

And what happens is as the agents and the models get better, it pays dividends because they're more precise. They're more effective at selecting the right model for the right job. So to build that engine, it took us years. Now we've perfected it. It's really, really good at defining even the guardrails, right? Here's what's out of scope. And here's where you can check with me if you have questions, right? The agents are trained to go back to the human to ask questions, but adding this framework in there just helps us do autonomous work, right? We don't have to go back to the human.

### 0:40:22 — Describing models to the deciding agent

> KB: Yeah, so that's interesting. I'm curious about that, having the agent choose the model, which I think is a really nice self-improving approach. But what do you use to describe the models to give the agent dimensions on which to choose? If I just say, hey, your options are Opus 5.5 or GPT 5.6, it doesn't know what those are. Maybe it does, but what are the features that you're calling out about those models for the deciding agents?
>
> SP: Yeah. So we ignore all the fluff that the labs claim about the model. One lab may think, model X or XYZ is amazing at something, right? Or the benchmarks may say one thing. So that's why you don't rely on web search for something like this. But instead, all of the results of the benchmarking and the evals that we had internally that identifies the strong points, you distill that into tags, right? And you rank the tags.

For example, front end, you have a ranked ladder of which models to choose based on complexity. So front end, very complex, choose this model. Front end, low complexity, choose this model. It's good enough, right? And then so on. Because you're optimizing for quality and speed, right? You need to choose the fastest model that gives you the best quality, right? For that, we've built our system to be intelligent enough to make the right decision at runtime.

### 0:41:43 — The private sandbox tier

> KB: That's really nice. So you're kind of mapping out what is that Pareto frontier along a number of dimensions. I think, yeah, front end, back end, language, complexity, those make sense. Okay, awesome. Is there anything that we haven't talked about Blitzy today that we're missing that would be worth talking through?
>
> SP: Yeah, let's talk about sandbox, which is the new plan we have. So we wanted to make it more accessible to enterprises, and which is why private sandbox is what we've introduced. And what that means is if a company has more than 250 employees and you sign up with your work email, you automatically get access to Blitzy with a set quota and a significant amount of lines of code to go reverse engineer and to write. It's a decent code. I don't have the numbers handy and they keep changing, so I won't cite them. But it's decent enough to do a small to medium-sized project depending on what you scope it.

And you could use that to build a completely new product, which is very easy to get started. You don't have to code your environment in or try to get it to understand your code. But there's no waiting. Just get started right away. Can easily evaluate how good Blitzy is. Or bring in a piece of your codebase. We don't train on any of it. We have very strict data retention policies and all of that. It's an enterprise-grade platform. We're not doing anything sketchy. Your code is owned by you, etc. We don't store any of it.

You can run that project through Blitzy and experience the value when you get the PR, when you go through the review experience. It's an it's a quick way to expedite the process where you don't need someone to handhold you. You can experience the value and then speak to our team if you'd like to move forward. I think it's a very generous offer. I don't think that's available with any other tool So we really hope that a lot of other enterprises get to experience the value. And we're really confident about that, which is why we're doing it.

### 0:43:33 — The frontier: two visions

> KB: That's awesome. So let's maybe now shift and look forward a little bit, right. So we've talked a lot about what Blitzy does. I think there's a lot of interesting things to pull out of that, whether you're in an enterprise where you can apply Blitzy now or considering or trying to think about how you're managing your own tools. What's like the frontier? What are the things coming down the pipe?
>
> SP: Well, I think the frontier is there's two wild visions of the frontier, two broad buckets. I think there's some people who think that what's going to happen going away is code review as a process is going away. Software engineering is dying. We're not going to be writing any code. We're not going to be reviewing anything. We're just going to ship. I find that personally outrageous, especially when you're talking about the enterprise. I don't think that's the speed at which the compliance frameworks evolve or that level of comfort is what the architects who actually use the models on a day-to-day basis have, right? I think they have a much stronger and clearer understanding of what the models are and are not.

And to be fair, they're on the spectrum of glorified autocomplete to AGI. They're not on either end. They're somewhere in the middle. At the end of the day, there are sequence-to-sequence models that are predicting the next token, right? But they're really, really good at real-world use cases, right?

Where does that leave us? If you go back to the beginning where I said most enterprise work is very highly defined and can be captured in a spec. And that's how enterprises have been building software for generations, right? We see the opportunity for the enterprise to hand off that work, submit the job, do something else, do more complex discovery work, do more complex research work that you cannot hand off. The requirements are not clearly defined. And the models are amazing at that, right? So the tools that you have, Claude Code, Codex, et cetera, they're amazing at helping you do that work, right? And the well-defined work gets done by autonomous tools like Blitzy.

And these tools, the next frontier is recursive self-improvement. So you can set an autonomous system perfect something. I want to ensure that performance for my e-commerce website, my page always loads in less than a second. I have a very large team. They're all shipping tons of commits every single day, but I cannot regress on this one metric. And it's very hard for me to enforce this with every single committer. What I do is I set the system behind it, and this system monitors and makes updates every single day, floating up for human review dynamically when it needs it, but it achieves that goal, right.

And we see that growing into not just distinct goals within the enterprise, but to entire products, right? If you can capture the product objectives, and the metrics, and the standards that you want to maintain and achieve, then what you can have is autonomous systems like Blitzy run these products that are very well defined that only need human supervision once in a while, and that can be easily managed. At the same time, shift the human attention to more complex items to products that need to be far more dynamic, where you cannot trust an LLM, where you need research and you need to do a lot more auditing and compliance checks, et cetera, and focus the humans on that.

It's an incredible opportunity for every player in the system because the market is big enough to accommodate everyone. Software engineering is such a huge, huge market with such an elastic demand that it's a really incredible time to be alive and be an engineer in the space.

### 0:47:20 — Runtime environments, logs, and observability feedback

> KB: Yeah. No, absolutely. Actually, one thing you mentioned there that I want to dig a little bit. So in this view of almost self-managing or autonomously managed projects, where do things like runtime environments and logs end up? We didn't end up talking about that for Blitzy, but are you feeding back operational data in? How does that end up working?
>
> SP: Yes. So Blitzy is connected to the cloud, your cloud, essentially, AWS, GCP, whatever that is. Blitzy has its own environment. Typically, when we work with customers, we have them capture the environment variables, secrets, configurations, instructions into Blitzy's environment, and then Blitzy replicates that environment across projects. You can have micro environments. You can share environments across projects, et cetera.

And for the vision that I talked about, that is the first step of getting to work with the system, right? Get it access to your development environment. It operates like an independent engineer, so have it recreate its environment, make sure it's good at that. And our environment is completely dynamic. There's no static item, right? The agents set up the environment every single time they operate. They do it dynamically. And they maintain that, right?

Once you've solved that environment problem, once you've given it access to observability, logs, and once you've set goals, guardrails, boundaries, the agents are incredibly good at optimizing all of those simultaneously to making sure they do the right thing. And if they're unable to do that, to escalate to a human at the right step, to stop and get the humans in, right?

We do that internally, and we've been successful at getting customers to trust us and to deliver value by doing that. And so therefore, we believe that is the place where the industry is going.

### 0:49:04 — Security: the harness is the control point

> KB: Yeah, I really like that. And also thinking about things like security, vulnerability updates, all these different things. LLMs have increased the pace of vulnerabilities being found, but I think autonomous systems like this can also then increase the pace of reacting to and fixing those issues.
>
> SP: Yeah, I think the biggest problem that people don't realize with LLMs is that LLMs have increased the pace of vulnerabilities being found, but they've also drastically increased the pace of vulnerabilities being introduced. And that's because you have to prompt an LLM to write secure code. You don't have to prompt a human, right? A human learns it and remembers that LLMs don't learn things until they're trained, right?

And I'm sure the labs will continue to work and get LLMs to write better code, more secure code. Because LLMs get much better at writing code, it's not a lever that you can control. There's not like write secure code optimized to 0.99. So this is always write secure. You can't do that, right? Training is very dynamic. You can only control some other variables that are not this.

Because of that, it's on the harness and it's on the system to enforce security, right? Which is why we take that very, very seriously. And we have an entire team dedicated to this. And we have entire workflows within Blitzy. We factor this into the design of how all lines of code are built. Because once you solve that, once you help the customers get comfort about security, compliance, the guardrails, code quality, that's when you can move to the next level and actually bring in this transformation that you're thinking about.

---

## [END]
