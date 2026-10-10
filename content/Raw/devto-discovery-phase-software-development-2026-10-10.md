---
title: "Discovery phase in software development: steps, deliverables, cost"
details: "dev.to blog post by Oleksandr Tytarenko covering the purpose, steps, roles, deliverables, week-by-week plans, cost, red flags, and FAQs of the upfront discovery phase in software projects."
tags:
  - raw
  - blog-post
  - software-engineering
created: 2026-10-10
updated: 2026-10-10
type: raw
source: https://dev.to/oleksandr_tytarenko/discovery-phase-in-software-development-steps-deliverables-cost-dcf
---

# Discovery phase in software development: steps, deliverables, cost

**Source:** dev.to (https://dev.to/oleksandr_tytarenko/discovery-phase-in-software-development-steps-deliverables-cost-dcf)
**Date Retrieved:** 2026-10-10
**Author:** Oleksandr Tytarenko

---

A discovery phase is the short stage at the start of a software project, before design and development, in which the client and the delivery team agree what problem they are solving, for whom, what the product must do and whether it can be built within the budget. It usually takes two to eight weeks. It ends with a written set of deliverables (goals, requirements, architecture, wireframes, a roadmap with ranged estimates and a risk list) and a decision: build, build something smaller, or stop.

This guide covers the steps in order, who takes part, the ten deliverables, week-by-week plans, how long it takes, what it costs, and how to read a discovery proposal before you sign one.

## Discovery phase at a glance

Most discoveries follow the same sequence, even when the names differ. Each step answers one question and leaves something on paper.

| Step | Question it answers | What you have at the end |
| --- | --- | --- |
| 1. Frame | Why are we doing this, and who decides? | Stakeholder list, background, first problem statement |
| 2. Research | Who has the problem, and how is the work done today? | Interview notes, users and actors, current journeys |
| 3. Goals and scope | What does success look like, and what is out? | Goals with metrics, an in/out scope list |
| 4. Requirements | What must the product do? | Prioritized, testable requirements |
| 5. Technical exploration | Can it be built, and on what? | Architecture diagrams, integration list, decision records |
| 6. Screens | What will people actually see? | Wireframes of the key screens |
| 7. Plan and estimate | How long, how much, and what could go wrong? | Milestones with low-high estimates, assumptions, risks |
| 8. Decide | Build, change course or stop? | Executive summary and a signed-off first-release scope |

## What a discovery phase is (and what it is not)

A discovery phase is a time-boxed piece of work with a fixed end and a decision at that end. Its job is to reduce the biggest unknowns while they are still cheap to change: on paper, not in code. The UK government's Service Manual puts it plainly: discovery is about understanding the problem before you commit to building anything, and you should not start building the service during it ([GOV.UK Service Manual](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works)). Nielsen Norman Group defines it from the design side as researching the problem space, framing the problems to be solved and gathering enough evidence to decide what to do next ([NN/g](https://www.nngroup.com/articles/discovery-phase/)).

The word "discovery" is used for several different things, and they are easy to mix up:

- **Product discovery** is the ongoing habit of a product team deciding what to build next, through user research and experiments. It never ends. A discovery phase is a one-off project stage with a deadline.
- **Inception** (a term common in agile consultancies) is usually a short, workshop-heavy kickoff that aligns a team on vision, scope and a first backlog. It overlaps heavily with discovery; a long inception is a discovery by another name.
- **Scoping** is narrower: deciding what is in and out and pricing it. It is one output of discovery, often the input to a statement of work.
- **Legal e-discovery** is the exchange of electronic evidence in a lawsuit and has nothing to do with software projects.

What a discovery phase is not: a sales meeting, a free estimate, a design sprint that ends with polished mockups, or a 100-page specification. If it does not end with a decision and a scope that the people paying for the build agree with, it has not done its job.

## Why a discovery phase matters

Early in a project, nobody knows enough to estimate it well. Steve McConnell's "cone of uncertainty" describes this: at the initial-concept stage, a software estimate can plausibly be off by a factor of four in either direction, and the range narrows only as requirements and design decisions are actually made ([Construx white paper](https://www.construx.com/wp-content/uploads/2019/02/CxWhitePaper_ConeOfUncertainty.pdf)). The cone is a best case, and time alone does not narrow it; decisions do. A discovery phase is where those first decisions get made on purpose instead of by accident halfway through the build.

In practice, a good discovery gives you four things:

1. **A shared problem.** The sponsor, the users and the team describe the same problem in the same words.
2. **A scope you can price.** Requirements are specific enough that two vendors would estimate roughly the same thing.
3. **Known risks.** Integrations, data, compliance and adoption risks are named, with an owner, before money is committed.
4. **A cheap exit.** If the idea does not hold up, you learn it after a few weeks instead of after a few months of development.

The last point is underrated. A discovery that ends with "do not build this yet" has saved money, not wasted it.

## The steps of a discovery phase, in order

The steps overlap in real projects, and later ones often send you back to earlier ones. The order still matters: requirements written before the problem is agreed tend to describe someone's favourite solution.

### 1. Frame the problem and the decision

Start with the decision the discovery must support ("build a first release for two regions or not") and the people who will make it. Collect what already exists: decks, earlier specs, support tickets, analytics, contracts with current vendors. Write a first problem statement and list the hard constraints: budget ceiling, deadline, regulation, systems that cannot change. GOV.UK's advice to reframe a predetermined solution as a problem to be solved applies to most commercial projects too.

### 2. Research users and the current process

Interview the people who will use the product, not only the people who pay for it. Watch the current process if you can. Map who the users are, what they are trying to do and where they get stuck today. Gather evidence for the problem: numbers, complaints, observed workarounds.

### 3. Set goals and scope

Turn the problem into two or three goals, each with a metric, a current value, a target and a date. Then write down what is out of scope. An explicit "not in the first release" list prevents more arguments than any other single page.

### 4. Write the requirements

Describe what the product must do in short, testable statements. Give each a type (functional, non-functional or constraint), a priority (MoSCoW: Must, Should, Could, Won't), acceptance criteria for the Musts, and a link to the goal it supports. Do not forget non-functional needs: performance, security, availability, accessibility, data residency.

### 5. Explore the technical options

Check every integration: who owns it, whether its API exists, whether it is documented and what it can actually do. Draw a context diagram and a component diagram. Record each significant choice as a short decision record: the question, the options compared, the choice and its consequences. Spike anything that the estimate depends on and nobody has tried.

### 6. Sketch the key screens

Wireframe the three to five screens users will meet most. They exist to settle disagreements and expose missing requirements, not to finalize the visual design. Check them with a few real users if you can.

### 7. Plan, estimate and list the risks

Split the work into milestones that each deliver something usable. Estimate each as a low-high range in person-weeks and write down the assumptions the range relies on. Keep a single log of risks, blockers and open questions, each with an owner and a next step.

### 8. Decide and sign off

Write the executive summary last and present it to the decision maker. The meeting should end with one of three outcomes: build the agreed first release, change the scope or approach, or stop. Agree the first-release scope in writing.

## Who takes part and what each person owes

A discovery team is small. In an NN/g survey of UX teams, a discovery had about four people working on it full time on average, most often a designer, a researcher and a product or project manager ([NN/g](https://www.nngroup.com/articles/discoveries-in-industry-revealed/)). For software projects, the roles below are typical; one person often covers two of them.

| Role | Side | What they owe the discovery |
| --- | --- | --- |
| Sponsor / decision maker | Client | Goals, budget range, constraints, decisions on time, final sign-off |
| Product owner or client PM | Client | Day-to-day answers, access to people, data and documents, priorities |
| Users and subject-matter experts | Client | Interviews, walkthroughs of the current process, review of journeys and screens |
| Client IT / security | Client | System access, API documentation, security and compliance rules |
| Business analyst | Delivery team | Interviews, requirements, traceability to goals, the open-questions log |
| UX / product designer | Delivery team | Journeys, flows, wireframes, quick checks with users |
| Solution architect / tech lead | Delivery team | Integration checks, architecture, decision records, feasibility, estimates |
| Delivery or project manager | Delivery team | Plan and timebox, risk log, roadmap, the final readout |
| QA engineer (optional) | Delivery team | Testable acceptance criteria, test strategy for risky areas |

The client side is where discoveries most often stall. If the sponsor cannot give a few hours a week and the users cannot be reached, extend the timeline or shrink the scope, but do not let the delivery team guess.

## Deliverables: what you should hold at the end

A finished discovery leaves ten documents (or ten sections of one document), plus a risk log. They are the same ten sections as the [discovery phase template](https://discoveryphaseai.com/resources/discovery-phase-template).

| Deliverable | What it contains | Done when |
| --- | --- | --- |
| Stakeholders | Name, role, what they need, influence, open disagreements | You know who signs off and who can say no |
| Background | Business, current process and tools, past attempts, hard constraints | A new team member could start with it on day one |
| Executive summary | Problem, proposed solution, outcome, scope, timeline and cost range, the decision needed | The sponsor can read it in two minutes and decide |
| Problem statement | Who is affected, what goes wrong, how often, what it costs, the evidence | It names no solution and everyone agrees with it |
| Goals and success metrics | Two or three goals, each metric with today's value, target and date, KPIs to watch | Every goal can be judged later |
| User experience | Users and actors, journeys step by step, key flows as diagrams | The main journey of each user is mapped |
| Requirements | Testable items with type, MoSCoW priority, acceptance criteria, linked goal, owner | Every Must has acceptance criteria and traces to a goal |
| Architecture | Context and component diagrams, integrations, decision records | Every integration is checked and every big choice recorded |
| UI screens | Wireframes of the main screens, which requirements each covers | Stakeholders agree on what users will see |
| Roadmap and estimates | Milestones, dates, low-high person-week ranges, dependencies, assumptions | Each estimate states what it assumes |
| Risks, blockers and open questions | Each item with likelihood, impact, owner and next step | Nothing known is left unowned |

## Week-by-week plans for a 2-, 4- and 6-week discovery

These plans assume a core team of two to four people and a client who can give interviews within the first week. Treat them as starting points, not fixed recipes.

### Two-week discovery

For a small MVP or a single workflow, with one or two integrations and a team that knows the domain.

| When | Focus | Output |
| --- | --- | --- |
| Days 1-2 | Kickoff, existing material, stakeholder interviews | Stakeholders, background, draft problem statement |
| Days 3-5 | User interviews, current process, goals | Journeys, goals with metrics, in/out scope |
| Days 6-8 | Requirements, integration check, key screens | Prioritized requirements, context diagram, wireframes |
| Days 9-10 | Estimate, risks, readout | Roadmap with ranges, risk log, executive summary, decision |

### Four-week discovery

For a typical new product or a significant rebuild: several user types, a few integrations, some unknowns.

| Week | Focus | Output |
| --- | --- | --- |
| Week 1 | Kickoff, stakeholder interviews, existing material, constraints | Stakeholders, background, problem statement, research plan |
| Week 2 | User research, current-process mapping, goals | Users and journeys, goals and metrics, scope list |
| Week 3 | Requirements, architecture options, integration checks, first wireframes | Requirements with acceptance criteria, diagrams, decision records |
| Week 4 | Wireframe review, estimates, risks, readout | Roadmap with ranges and assumptions, risk log, executive summary, sign-off |

### Six-week discovery

For complex or regulated work: several departments, legacy systems, data migration or compliance review.

| Week | Focus | Output |
| --- | --- | --- |
| Week 1 | Kickoff, stakeholder map, existing systems and documents | Stakeholders, background, constraints, research plan |
| Week 2 | User and stakeholder research across groups | Interview findings, users and actors, current journeys |
| Week 3 | Problem, goals and scope; compliance and data review | Agreed problem statement, goals and metrics, data and compliance notes |
| Week 4 | Requirements; architecture options; technical spikes on the riskiest integrations | Requirements draft, diagrams, spike results |
| Week 5 | Wireframes and user checks; decision records; requirement review with the client | Wireframes, decision records, reviewed requirements |
| Week 6 | Estimates, roadmap, risk review, readout | Milestones with ranges, assumptions, risk log, executive summary, decision |

## How long a discovery phase takes

There is no standard length. GOV.UK says there is no set time period and that around four to eight weeks is typical for public services, with a well-understood problem needing less. For commercial software projects, these ranges are a reasonable rule of thumb, not a measured average:

- **One to two weeks**: a small MVP, one main user type, few integrations, a client who answers fast.
- **Three to six weeks**: a typical product with several user types, a few integrations and some open technical questions.
- **Six to twelve weeks**: regulated domains, many stakeholders, legacy replacement or data migration.

What actually sets the length: how many distinct user groups you must hear from, how many integrations you must verify, how quickly the client can make decisions, and whether a compliance review is involved. Calendar time is usually lost waiting for interviews and answers, not doing analysis. Time-box the phase anyway; an open-ended discovery tends to drift into design or build.

## What a discovery phase costs

The honest way to price a discovery is in person-weeks:

**cost = people on the team × weeks × their blended weekly rate**

| Discovery | Typical team (rule of thumb) | Effort |
| --- | --- | --- |
| Two weeks | 2 people (BA or PM, plus an architect part-time) | about 3-4 person-weeks |
| Four weeks | 3 people (BA, designer, architect) | about 8-12 person-weeks |
| Six weeks | 3-4 people, plus specialists for security or data | about 15-24 person-weeks |

Multiply the effort by the rates you or your vendor charge. For example, at an illustrative blended rate of $4,000 per person-week (use your own figure), a four-week discovery of about 10 person-weeks costs about $40,000; at $1,500 per person-week, the same work costs $15,000. That spread is why quoted prices differ so much between agencies and countries.

Another common rule of thumb, mostly from agency guides, puts discovery at roughly 5-15% of the total build budget. Treat that as a sanity check rather than a fact: on a large project the share falls, and on a small, risky one it can be higher.

What pushes cost up: more user groups to research, integrations with poor documentation, regulated data, many decision makers, and requests for high-fidelity design inside discovery. What brings it down without skipping the work: sending existing material before kickoff, booking interviews in advance, one decision maker with real authority, and reusing a standard structure such as the [discovery phase checklist](https://discoveryphaseai.com/resources/discovery-phase-checklist) instead of inventing one.

## Discovery in agile and waterfall projects

In a **waterfall** project, discovery is a gate. Its output is a complete specification, a fixed scope and often a fixed price, and changes after it go through change control. The risk is spending weeks specifying details that will change anyway.

In an **agile** project, discovery sets direction rather than every detail. It produces the goals, the first-release scope, a prioritized backlog with the Musts detailed and the rest rough, an architecture that will not need to be thrown away, and a ranged estimate. Detailed discovery then continues in each sprint for the next items. The risk here is the opposite one: calling the first sprint "discovery" and never writing down goals, scope or risks at all.

Most teams land in between: a time-boxed upfront discovery that is thorough on goals, scope, integrations and risks, and deliberately light on anything the team will learn faster by building.

## Red flags in a discovery proposal

Whether you are buying a discovery or writing one, check the proposal for these:

- **No list of deliverables.** "Workshops and alignment" without named documents means you cannot tell when it is finished.
- **A fixed build price before discovery starts.** If the vendor already knows the price, the discovery is either unnecessary or a formality.
- **No time with real users.** Only the sponsor is interviewed.
- **No technical person.** Nobody checks integrations, so the estimate is a guess.
- **Single-number estimates.** Any estimate made before the build should be a range with its assumptions written down.
- **The deliverables are not yours.** You should own the documents and be free to take them to another team.
- **No end date and no decision meeting.** Time and materials with no time-box tends to grow.
- **Heavy visual design inside discovery.** Polished screens look like progress but do not answer the risky questions.
- **The technology is chosen before the problem is understood.** A recommended stack in the proposal itself is a warning sign.

## Common mistakes

- **Starting from the solution.** "We need an app" is not a problem statement. Reframe it before researching.
- **Talking only to the buyer.** The people who pay for software are rarely the people who use it every day.
- **Writing a document nobody reads.** Ten clear sections beat a long specification. The executive summary must stand on its own.
- **Skipping non-functional requirements.** Performance, security, offline use and data residency change architecture and cost more than most features.
- **Estimating without assumptions.** An estimate without its assumptions cannot be checked or defended later.
- **Leaving open questions unowned.** Each needs a name and a date, or it will still be open at the start of the build.
- **Letting the documents drift apart.** When a goal or requirement changes late, the architecture, screens and estimate that depend on it must change too.
- **Not involving the people who will build it.** Developers who were absent from discovery will rediscover it, at build rates.

## When a discovery phase is not worth it

Skip a formal discovery, or shrink it to a day or two, when:

- the change is small and well understood, and a few tickets describe it fully;
- you are building a throwaway prototype to test an idea, so the prototype is the discovery;
- the same team has built the same kind of thing for the same client and little has changed;
- the scope is fixed by someone else (a regulator or a contract) and the only open question is effort.

A useful test: if the discovery would cost more than the mistake it could prevent, keep it light. Even then, write down the problem, the goals, the Musts, the integrations and the top risks. That takes hours, not weeks, and it is the part that saves projects.

## FAQ

### How long does a discovery phase take?

Usually two to eight weeks. As a rule of thumb, one to two weeks for a small MVP, three to six for a typical product, and six to twelve for regulated or legacy-heavy work. The number of user groups, integrations and decision makers matters more than the size of the idea.

### How much does a discovery phase cost?

Work it out as people × weeks × rate. A two-week discovery is roughly 3-4 person-weeks of effort, a four-week one roughly 8-12, a six-week one roughly 15-24. Your price is that effort times your rates. Agency guides often quote 5-15% of the build budget as a rough check.

### Is the discovery phase paid, and who pays?

Usually yes, and the client pays, either as a fixed fee for a fixed time-box or as time and materials with a cap. Some vendors credit the fee against the build if you continue with them. A "free" discovery is either short or paid for later inside the build estimate. Whatever the model, make sure you own the deliverables.

### Who takes part in a discovery phase?

On the client side: a sponsor who decides, a product owner, real users and someone from IT. On the delivery side: a business analyst, a designer, a solution architect or tech lead and a project manager. A core team of three to five people is common (a rule of thumb; an NN/g survey of UX teams found about four full-time people on average).

### What is the difference between discovery, inception and scoping?

Discovery is the full upfront stage: problem, users, requirements, architecture, estimate and decision. Inception is usually a shorter, workshop-based kickoff for an agile team and overlaps with discovery. Scoping is one output of discovery: what is in, what is out and what it costs.

### Can AI help with a discovery phase?

Yes, with the writing and checking, not with the decisions. AI is good at turning interview transcripts, decks and old specs into first drafts of requirements, journeys or a problem statement, and at spotting gaps and contradictions between sections. It cannot interview your users, judge which stakeholder is right or own a risk. [Discovery Phase AI](https://discoveryphaseai.com/), for example, drafts the first stages (background, problem, stakeholders, goals, users and journeys, requirements) from documents, decks, transcripts and images you already have, helps you write and score the rest stage by stage, and you review every draft before anything is saved.

## Disclosure and a sample

The author builds [Discovery Phase AI](https://discoveryphaseai.com/), a tool aimed at the writing-and-assembling side of discovery: it drafts the early stages from the decks, documents and call transcripts you already have, and exports one report. Your team still runs the interviews, reviews every draft and makes the decisions.

The original of this post is on the [author's blog](https://discoveryphaseai.com/blog/discovery-phase-in-software-development).
