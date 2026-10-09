---
title: "Post-Incident Review Culture"
details: "The practice of conducting, sharing, and learning from incident reviews as a primitive of organizational resilience. Sam Newman's position: the only way to build resilient systems is to be honest about mistakes, share them publicly, and use the shared corpus (other companies' post-mortems, blameless retros, public incident write-ups) as ongoing learning material. Cloudflare's rapid, self-critical public write-ups are held up as a model; regulated-reporting regimes like DORA are accelerating the practice."
tags:
  - concept
  - software-engineering
  - infrastructure
created: 2026-10-09
updated: 2026-10-09
type: concept
sources:
  - Raw/pragmatic-engineer-resilient-systems-sam-newman-2026.md
---

## Definition

A post-incident review (PIR / post-mortem) is a structured write-up produced after a production incident: what happened, in what order, what was detected, what was done about it, what worked, what didn't, and what changes will prevent recurrence. **Post-incident review culture** is the set of organizational norms that determine whether these reviews happen at all, are honest, are shared externally, and result in actual change.

## Why it matters

Newman's claim: **without honest sharing of mistakes, you cannot build a resilient system in your company.** The reasoning is twofold:

1. **Internal honesty without external sharing** doesn't compound. The same lesson gets re-learned (or not learned) by every other company.
2. **External sharing without internal honesty** is marketing. Post-mortems that read like press releases teach nothing.

## Good vs bad practice

| Practice | Good | Bad |
|----------|------|-----|
| Timing | Within 24 hours while memory is fresh (Cloudflare). | Weeks later, with reconstructed timeline. |
| Tone | Self-critical, naming specific decisions that compounded the incident. | Defensive, vague ("a third-party provider had an issue"). |
| Audience | Anyone, written for the public. | Confined to internal Slack channel. |
| Distribution | Public blog post. | Only NDA-gated customer comms. |
| Follow-through | Linked action items with owners and dates. | Vague "we will improve our processes" closer. |

## Cultural substrate

Post-incident review culture collapses without **psychological safety** — the precondition for people raising issues, challenging post-mortem drafts, and admitting near-misses. Newman's argument: the *graceful extensibility* and *sustained adaptability* dimensions of the [[Concepts/four-dimensions-of-resilience]] both depend on this.

## Regulatory pressure

DORA (EU), and similar UK / European regimes, are turning what was previously discretionary into mandatory reporting for certain classes of incidents. Newman's view: this is good — it normalizes the practice and removes the "we're publicly traded so we can't share" excuse.

## Reading material outside your own incidents

Newman's recommendation: **when you don't have an incident, read other people's incident reports**. *The Void* (incident-report library) is his cited example. There's a small amount of schadenfreude and a large amount of compounding learning.

## Related Concepts

- [[Concepts/four-dimensions-of-resilience]] — Dimensions 3 (graceful extensibility) and 4 (sustained adaptability) both depend on this culture
- [[Concepts/production-is-truth]] — The premise that the post-mortem is for what the system actually did, not what the spec said