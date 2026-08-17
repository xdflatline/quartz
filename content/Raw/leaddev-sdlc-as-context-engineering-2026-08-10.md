---
title: "Your SDLC is Your Context Engineering — Daniel Kravets, LeadDev"
details: "Full raw text of Daniel Kravets' LeadDev article (Aug 10, 2026) arguing that the SDLC itself — not AGENTS.md files — is the agent's real context layer, with a detailed account of how Vendict rebuilt their development process around agent usability, including monorepo structure, four execution lanes, test-design subagent isolation, builder-reviewer separation at task granularity, and the devcontainer-as-execution-boundary pattern."
tags:
  - raw
  - agent
  - context-engineering
created: 2026-08-17
updated: 2026-08-17
type: raw
source: "https://leaddev.com/software-quality/your-sdlc-is-your-context-engineering"
---

# Your SDLC is Your Context Engineering

**Source:** LeadDev (https://leaddev.com/software-quality/your-sdlc-is-your-context-engineering)
**Author:** Daniel Kravets, Founding Engineer at Vendict
**Date Published:** August 10, 2026
**Date Retrieved:** 2026-08-17
**Reading Time:** ~18 minutes
**Type:** Industry article / engineering leadership write-up

---

August 10, 2026

**Key takeaways:**

- The **SDLC** is an **agent's real context**, not just AGENTS.md files.
- Separate **builder and reviewer** at task level, not just PR level, or agents rationalize their own failures.
- Most critical issues **trace back to planning, not code**.

File-level context engineering has won. Open any modern repository that adopted AI tooling, and you will find an AGENTS.md file steering the tools: Cursor, Claude Code, CodeRabbit all read it. I have spent the last year perfecting these file-level instructions, and by any reasonable measure the approach worked.

However, it is still not enough.

You can write the cleanest AGENTS.md imaginable, and the agent still will not know what "done" actually means for the feature it is building. It does not know which critical paths are strictly off-limits. It cannot decide when a large change should be sliced into smaller, safer pieces and when it should ship whole. It does not know when to escalate an edge case to a human instead of quietly fixing it in place, and it has no idea which kind of test belongs to which kind of behavior.

That operational context is not stored in a markdown file. It is embedded in your software development lifecycle (SDLC): how work gets specified, reviewed, tested, and shipped.

At Vendict, a lean third-party risk management (TPRM) startup, we rebuilt our engineering process around one thesis: in the agentic era, the SDLC is the context. The same structure that lets 10 human engineers coordinate is what lets the 11th contributor – an AI agent – operate reliably.

My team is small, and the redesign took us roughly a month. In this article, I will break down what we built and why each piece is shaped specifically for agents, walk through the decisions that go against the standard advice, and name the problems I deliberately left out for now.

## What we wanted, and why now

The motivation is simple. Teams now ship at speeds that were difficult to imagine two years ago. Frontier labs state openly that the majority of their code is AI-authored. Anthropic's Mike Krieger has noted that 90 to 95% of changes to Claude Code's own codebase are written by Claude Code itself. That pace is no longer reserved for the largest companies. At a small startup, the magnitude is different, but the direction is the same.

Velocity is no longer a function of human typing speed. It is a function of how reliably agents can participate in the development process: understand what is being built, what constraints apply, what done looks like, and when to stop and ask. All of that lives in the process itself. So when we sat down to rebuild, we set five goals upfront and evaluated everything downstream against them.

- **Velocity:** we want to ship substantially faster than we did a year ago, and not by 50%. That only becomes possible when agents take on a meaningful share of the work.
- **Mainline safety:** the constraint that keeps velocity sustainable – "main" stays deployable at all times. Otherwise the speed we gain in feature work we lose back in coordination overhead and emergency rollbacks.
- **Agent usability as a first-class concern:** we are not designing for humans and then adapting for agents; we design for both from the start. Agents need stable context, stable commands, hard boundaries, and a way to verify themselves. Humans need a system they can still operate inside without becoming the bottleneck.
- **Operational clarity:** anyone reading the system should see what is live, what is planned, what is experimental, and which session changed what. The faster you move, the more this matters.
- **Incremental adoption:** we could not stop product work for a month to rebuild the SDLC from scratch. The new system had to be adoptable in days, hardened over weeks, and forgiving when something needed adjustment in flight.

Four of these goals will look familiar from the research on high-performing teams by DevOps Research and Assessment (DORA): small batches, trunk-based development, fast recovery, low change failure rate.

The fifth is new for 2026: agent usability. It changed the shape of everything else, so I want to name the four standard ones and the one new one before getting into how the system is actually shaped.

## The shape of the system

A note on language: a "lane" here is just a designated path a change moves through, with the gates attached. Lane A is the standard lane with standard review. Lane B adds a spec-and-plan step because the change has meaningful design surface. Lane C is reserved for sensitive changes – control-plane paths, CI configuration, anything touching auth or data access. Lane D is for experiments: isolated, clearly scoped changes. The same word will appear in the Makefile targets, the CodeRabbit config, the AGENTS.md files, and human review checklists.

We work out of a monorepo. Ownership, build, deploy, and infrastructure state live in separate systems that reference the repo, but the shared context boundary is the monorepo itself. The agent sees the full codebase, the engineer does too, and CI sees the affected artifacts and the deployers see release candidates per environment. This is not novel – Google runs it at two billion lines of code – but it is worth naming because the principle still holds at any scale: one place where the code lives, separate places where it is owned and shipped.

Three document lifecycles, not one. Anything that lives in `docs/` is the current merged truth on main, no future state. Anything that lives in `plans/` is the future and active work – it is execution material, not truth. Anything that lives in `docs/adr/` is a durable decision in the form of an Architecture Decision Record (ADR), and ADRs are never deleted, only superseded. The three directories have different review rules, different readers, and different staleness budgets.

Agents need to know which document to trust. Mixing current-state and future-state documentation is a failure mode of the human process; for an agent it is the direct path to hallucinating on top of a plan that was abandoned months ago. The split between `docs/`, `plans/`, and `docs/adr/` is what stops that.

The system has a known side effect: it can make agents stricter than necessary. Even when a change is approved, a Lane A agent reviewing the change can warn "this file wasn't supposed to change" if the plan did not include it. That is still better than the opposite problem.

The endgame, to my mind, is reviewing documentation instead of code, and keeping documentation precise enough that both agents and humans can act on it without asking.

## Three design choices that need explaining

### 1. Test files do not count toward pull request size limits

The obvious objection to size limits on a pull request (PR) in an AI-heavy team is that AI reviewers can absorb diffs a human could not. The data says otherwise. Across tens of thousands of pull requests, defect detection drops from 87% on small diffs to 28% on diffs over a thousand lines. AI-review attention degrades in much the same way human attention does. So the size rule stays. At Vendict, the caps are a soft 500 lines and a hard 1,000. The interesting question is not whether to limit PR size, but what should count toward the limit.

Agents generate tests aggressively, which is exactly what we want. If tests count toward size pressure, the agent learns to either write fewer tests or split implementation from tests into separate PRs. Both outcomes are strictly worse than what the rule was trying to buy: fast review of a focused implementation diff. So tests are excluded from the cap, and test design is handled by a separate subagent that has no line limit at all.

The separate subagent solves a different problem than the size exemption does. It reads the acceptance criteria and the plan's Goals and Design sections, then plans a broader test set: edge cases, error paths, regression risks, failure modes the spec did not enumerate. Crucially, it works in isolation from the implementation agent's reasoning context, so the implementation agent cannot quietly drop an acceptance criterion and then write a test that conveniently verifies the behavior it actually shipped.

On top of this we use CodeRabbit as a review layer, though the methodology does not depend on that particular tool: it checks whether tests are meaningful, flags tests that are effectively mocked into passing, asks for non-mocked smoke tests when a major change occurs, and catches assertions that do not prove anything. The whole separation is cheap to set up and disproportionately valuable, because it removes the single biggest agent failure mode I know of: post-hoc rationalization of a missing case.

### 2. Builder-reviewer separation enforced at task granularity, not PR granularity

Standard advice says the agent that wrote the code should not review the code. Necessary, but insufficient when one coding session spans implementation, tests, verification, and lint. The same context that decided "this implementation is correct" has every incentive to decide "this test is wrong" – and believe me, given the chance, it will.

The plan-implementer skill spawns four separate subagents over a single feature: test designer, failure analyzer, verifier, and linter. Each runs in its own context. When tests fail, a separate subagent classifies each failure as TEST_ISSUE, IMPL_ISSUE, DOC_ISSUE, or UNCLEAR. The implementing agent acts on the classification but does not get to choose it. UNCLEAR is written into the policy and escalated to a human instead of being resolved on the spot.

Circuit breakers exist for the moment when the loop stops getting better. The agent gets three test-fix cycles and two verification cycles; after that, the task stops and escalates. It does not get to keep trying forever just because it "feels" close.

Builder-reviewer separation has to live at the task level because a single agent session today can be the size of what used to be a full PR a couple of years ago. The human reviewer and CodeRabbit both read from the same canonical rubric in `docs/standards/code-review-rubric.md`. The separation is grounded in the workflow, not in a rule that asks anyone to behave.

### 3. spec and plan as separate artifacts, but shared context

`spec.md` and `plan.md` ship together in one PR, yet they are separate artifacts with separate review surfaces, stored together in the monorepo where both humans and agents can read them. The spec defines the intended behavior and is reviewed from the product or system side. The plan describes execution and the more localized technical detail, and is reviewed from the R&D side.

Keeping them separate prevents review from collapsing into one ambiguous conversation where product intent, implementation strategy, and approval authority blur together. Keeping them in the monorepo gives both humans and agents the same durable context package: what we agreed to build, how we intend to build it, and where the external references live when markdown is not enough.

Humans often survive scattered context by remembering meetings or asking a quick question in Slack. Agents act only on the artifacts they can see. So the SDLC has to make those artifacts visible, connected, and approved before implementation starts.

## One source of truth, many consumers

The SDLC shows up most clearly in `docs/standards/`: a directory of profiles, one per concern, that every other artifact references. Profiles do not embed each other and do not name their consumers. When a new agent tool joins the stack, it learns the ropes by reading profiles.

Standards should be authored once and consumed many times. Agents, CI, review tools, dev environments, and humans all need the same operating context, but they should not each maintain their own version of it.

The diagram shows the consumption model. The next question is what the standards layer actually contains, and how it avoids turning into yet another pile of duplicated instructions.

## The shape of the standards layer

The profiles cover four areas: per-language quality standards for each language in the stack, cross-cutting concerns that apply regardless of language, document shape rules for every artifact type we produce, and templates for each of those artifact types. Every concern is defined exactly once.

Two authoring rules make the layer hold together. First, each profile owns its concern: cross-language rules live in `code-review-rubric.md`, and language profiles cite that file rather than duplicating it; test-substance rules live in `testing-profile.md`, and the rubric refers to it. Second, profiles cite by path and never restate. Adding a new rule means editing one file, not five.

This also matters for tool portability. AI-coding agents and review tools are a competitive market, and every vendor has an incentive to pull you into its own knowledge base. If the rules live in version-controlled markdown, the accumulated learning stays with the repository instead of the vendor.

## The consumers

The AGENTS.md hierarchy spans roughly 19 files across root, app, and submodule levels. Each file names the deny-list paths relevant to its scope and links to the profiles that govern it. Cursor, Claude Code, Codex, and CodeRabbit all read it. A note on tooling: everything named here is what I use today; swap any tool for whatever fits your context.

The Makefile is the verification interface. Every artifact in the repo answers to `make ci`, `test`, `lint`, `fmt`, `build`, and `run`. `make lint` is deliberately non-mutating – auto-fix lives under `make fmt`, never under lint or CI. The agent self-verifies with one command; CI runs the same command; a new engineer onboarding runs the same command. Same interface across Go Lambda functions, Python ECS services, and the TypeScript/Vue frontend.

The CodeRabbit configuration is thin because the rules do not live in YAML. The file is mostly path routing: for files matching this pattern, review against `docs/standards/python-profile.md` and `docs/standards/code-review-rubric.md`. Lane-aware escalation is part of the same layer: if a PR is marked as Lane A but touches a Lane B or Lane C surface, it is escalated instead of being treated as a standard change.

Agent skills reference profiles by path in their prompts, so agents and human reviewers are anchored to the same source of truth: the same document, in the same version.

## 4 principles in the rubric calibrated for agent-heavy review

Some principles in `code-review-rubric.md` are calibrated specifically for AI-heavy review, where the failure modes differ from a human-only team's.

### 1. Verify before flagging

Reviewers, human or AI, must verify a claim against the file at HEAD before filing the finding. If the claim cannot be verified from the current state, it is filed as a question. AI reviewers often do not ground their findings, and this rule is the false-positive killer. It is an iterative process: part of the review resolution is responding to comments, and that human feedback becomes a signal for improving the reviewer's instruction itself. False positives cannot be eliminated completely, but they can be gradually reduced. Today our false positive rate is around 10%, down from approximately 30% at the initial stage.

### 2. Documentation inconsistencies are at least Medium severity, never Minor

Agentic development depends on docs being trustworthy. A stale doc is not a minor annoyance – it can mislead every future agent session that reads it.

### 3. Design decisions must be cross-read before filing "this seems redundant" or "this seems fragile"

Forcing an AI reviewer to check `design-decisions.md` and the relevant ADRs first turns "documented design – see ADR-042" into a valid drop. Without this rule, AI reviewers pattern-match without project context.

### 4. Tests are reviewed against the spec's acceptance criteria, not line coverage

A new feature whose tests exercise only one acceptance criterion is a Major finding. This anchors test review to the work the spec was approved for, not to a number.

## The devcontainer as execution boundary

The devcontainer exists to limit what the agent can access or exfiltrate from the host machine. That is a different threat model, and it leads to different choices.

The agent inside does not see SSH keys. It can use git, but only against the project's repositories. It can use Amazon Web Services (AWS), but only through time-scoped credentials with limited access – the agent cannot delete a database, for example. We use Docker-outside-of-Docker so the agent can run artifacts (frontend, services, databases) in sibling containers.

What the devcontainer deliberately does not restrict is outbound network access. At Vendict, we considered locking egress and rejected it: the cost was too high. A meaningful share of what agents do well today is research-shaped – searching for API contracts, reading third-party READMEs, looking up Terraform module examples. Lock egress, and you neutralize that. We chose to close the credential surface and leave the network surface open.

The boundary is shaped deliberately, for one specific threat, and it is visible to both humans and the agent itself. An agent reading the devcontainer config can see what it is allowed to do. A human reviewing a Lane C PR that touches `.devcontainer/` knows exactly what is at stake. And since every consumer reads the same standards by path, the agent's PR, the CodeRabbit review, and the human reviewer stay aligned on the same rules.

## What's next?

Some areas I deliberately left out of scope. Knowing what is out of scope is itself part of the discipline.

Firstly, observability beyond CloudWatch and alerts – tracing, service level objectives (SLOs), on-call structure. I suggest deferring it until the new SDLC reveals where opacity actually hurts. There is no need to design a stack for problems you have not seen yet.

Secondly, product-side AI safety is a different problem entirely. Prompt injection, customer-behavior evals, and model rollout policy all deserve their own piece. This article is about agents working on our startup's code; how customer-facing agents behave in the product is its own conversation.

Finally, I intentionally left production agent safety out of scope: sandboxing, credential scoping, network policy, and runtime governance for agents that actually serve customers. That is the operational story, and probably the topic of the next article.

## The lessons of the first month

A month of real load teaches you mostly what you over-engineered and what you underestimated. First of all, our weekly sync strategy turned out to genuinely help engineers adapt during the integration of AI agents. We run demo sessions a few times a week, and the rule is simple: describe only what you shipped and only what you learned by doing it, and avoid industry takes.

The merge queue, however, is already shaping up as the next problem to solve. And one thing stands out across all the reviews so far: almost every critical issue comes from the specification itself and from insufficiently thoughtful planning, not from the code.

Two meta-lessons matter more than any specific configuration choice.

The SDLC did not have to be perfect before we adopted it. As a founding engineer, I did not set out to design this perfectly in advance. The goal was clear enough that we could tune the system in flight, and that turned out to be the right call. Almost a month in, the core patterns have largely held up, and the parts we need to revise are now visible without us having had to predict them upfront. Designing the perfect SDLC in advance would have cost more than it saved.

Some engineers prefer a worked example before adopting a new pattern themselves. They have demanding work in front of them, and they would rather see one exemplary plan or PR done right than extract behavior from a process document. Templates and the first end-to-end Lane B feature carry rollout weight that documentation alone cannot.

None of the above required an enterprise platform. We assembled the pieces ourselves and now calibrate as we go. The SDLC itself is the context, and that context is what makes agents reliable contributors rather than unpredictable autocomplete.

## The next bottleneck

Code review velocity is the next bottleneck. Previously the constraint was implementation speed; now it has clearly shifted to review throughput and human review capacity. Small-PR culture only works if review throughput keeps up, and the rule itself creates the pressure: agents produce more focused PRs faster, which means more incoming review requests, more context-switching, and more human attention split across more diffs.

The standards layer helps make reviews consistent, since every reviewer, human or AI, calibrates against the same rubric. Velocity remains the bottleneck because the process still depends on humans. The direction the industry is moving toward seems clear: humans review intent – the specification, the plan, and the acceptance criteria – while automation and AI reviewers increasingly cover the code itself. Code quality becomes more of a tooling concern; design judgment stays with humans.

For now, human review still includes code. We are not yet at the point where we are comfortable removing human eyes from the diff entirely, and the active challenge is building enough confidence in the tooling to make that call.

The key point, though, is that the critical issues we see come from insufficiently thoughtful planning and underspecified requirements. The real problem is not only how agents write code, but how clearly humans define the work before the code is written.