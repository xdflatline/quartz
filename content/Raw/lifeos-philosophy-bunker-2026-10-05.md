---
title: "LifeOS: Bunker (Philosophy)"
details: "The universal application harness — every app sits in one chassis that supplies data, control, observability, identity, and security. An app declares a type, the harness lights up the planes that type needs, and the ISA becomes the test suite that runs forever."
tags:
  - raw
  - agent
  - tooling
source: https://ourlifeos.ai/philosophy/bunker/
created: 2026-10-05
updated: 2026-10-05
type: raw
---

# Bunker

**Source:** [https://ourlifeos.ai/philosophy/bunker/](https://ourlifeos.ai/philosophy/bunker/)
**Date Retrieved:** 2026-10-05
**Author:** Daniel Miessler (LifeOS)
**Publisher:** ourlifeos.ai (LifeOS — The universal AI Harness)
**Type:** Blog Post / Product Philosophy

---

# Bunker

The universal application harness — every app gets security, uptime, testing, and deployment from one shared chassis.


Fig. 09·Every app seated in one chassis; its services plug in

Bunker is the chassis every application sits inside. The app owns the experience — design, content, domain logic — and Bunker owns everything invisible underneath: data, deploys, health, identity, and security. Standardize the pipes, never the paint.

## Why it exists

Every app you ship needs the same things: a database with backups, a deploy path with rollback, health checks, uptime monitoring, auth, secrets handling, security headers, and someone watching the whole surface for exposure. Build ten apps and you either rebuild that layer ten times — each copy slightly different, each drifting on its own — or you skip pieces and find out which ones mattered when something breaks in public.

Bunker exists so that layer is built once. An app declares what kind of thing it is, and the harness supplies the machinery that kind of thing needs. New apps inherit the whole invisible layer on day one; fixes to the harness reach every app at once.

## How it works

An app declares a **type**, and that type selects which components turn on across six planes:

- **Data** — database and migrations, storage, backups, integrity invariants.

- **Control** — app registry, config, deploy and rollback.

- **Observability** — health dashboard, logs, uptime, cost, alerting.

- **Identity** — auth, roles, user store, audit trail.

- **Security** — secrets, scanning, rate limiting, headers and TLS.

- **Commerce** — payments, billing, and customer metrics, for apps that charge.


The spec is the test suite. Each app carries an [ISA](https://ourlifeos.ai/philosophy/the-isa) — its ideal state written as verifiable criteria — and every criterion names the probe that would falsify it. `bunker test` reads that file and runs every probe, so the document describing what the app should be is the same document that verifies what it is.

Ship daywhat registering an app actually looks like

DeployA new site goes live at its public URL.

→

Same motionIts ISA is adopted into the health plane; the app joins the security plane's watch list.

→

From then onAvailability and contract probes run continuously; the outside-in security scan covers it hourly.

**The criteria are the tests:** "the homepage loads," "the auth boundary holds," "the data endpoint requires a key" — each one a criterion in the ISA, each one probed on a schedule, forever.

Two planes run continuously in the cloud. The observability plane compiles every registered app’s probes into a site-health service, so availability and contract checks run without anyone asking. The security plane scans the full deployed surface every hour from the outside — auth boundaries, exposed secrets, headers, TLS, DNS — the way an attacker would look at it, not the way an insider hopes it looks.

Registration is part of shipping. The moment an app deploys to a public URL it registers in both planes, in the same motion as the deploy. There is no “deploy now, register later” — an unregistered app is invisible to the harness, which means no health contract and no hourly security assertion.

## Where it fits

Bunker is where the ISA System meets running software. [The Algorithm](https://ourlifeos.ai/philosophy/the-algorithm) climbs toward an ideal state during a build; Bunker keeps holding the app to that ideal state after the build ends, re-running its probes for as long as the app lives. “Add a feature” just means adding criteria to the app’s ISA that don’t hold yet.

It pairs with [Pulse](https://ourlifeos.ai/philosophy/pulse), which renders every registered app’s health, test results, and security grade on one dashboard — uptime, last check, green or red, on the card face.

## What it feels like

Shipping an app stops meaning assembling infrastructure. You build the part only you can build — what the thing looks like, what it says, what it does — and the harness supplies the rest. Every app you’ve ever shipped is being watched: probed hourly from the outside, tested against its own spec, reporting its health to one place. When something drifts or breaks, you find out from the system, not from a user.

[Full documentationBunker — the Universal Application Harness →](https://docs.ourlifeos.ai/Bunker__BunkerSystem)
