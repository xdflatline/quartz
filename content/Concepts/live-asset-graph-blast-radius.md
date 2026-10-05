---
title: "Live Asset Graph with Built-In Blast Radius"
details: "An architectural pattern for asset inventory in security and ops: instead of a list of assets (a spreadsheet, a wiki page), build a *graph* where edges name the real relationships — this worker serves that domain, this key unlocks that account, this app writes to that database. Built-in graph queries answer questions a list cannot: owns (what does this thing hold), blast (if this were compromised, what's reachable from it, one hop and every hop after), and unregistered (what exists in the world that the graph doesn't know about yet — usually where the risk lives). The graph stays current via collectors that read from the systems that already know the truth, rather than relying on someone remembering to update a spreadsheet."
tags:
  - concept
  - architecture-pattern
  - cybersecurity
  - knowledge-management
created: 2026-10-05
updated: 2026-10-05
type: concept
source: "[[Raw/lifeos-philosophy-atlas-2026-10-05]]"
---

# Live Asset Graph with Built-In Blast Radius

**Source:** [[Raw/lifeos-philosophy-atlas-2026-10-05]] (LifeOS / Daniel Miessler, building on [Continuous Asset Management Security](https://danielmiessler.com/blog/continuous-asset-management-security))
**Category:** Architecture Pattern
**Status:** Production-validated

## Overview

Most people cannot answer basic questions about their own estate. What domains do I have. What is running on that server. Which accounts hold a key that still works. *If this one credential leaked, what would it reach.* The reason is not carelessness. It is that the answer lives in a dozen places — a registrar, a cloud console, a password manager, three config files, and memory — and no single place holds the relationships. So the questions go unasked until something breaks or something leaks, which is the worst possible moment to start an inventory.

## The graph, not the lists

The pattern is to build a *graph* rather than a *list*. Assets are nodes; the edges are the relationships that actually matter. Because it is a graph, it answers questions a list cannot:

- **owns** — what does this thing actually hold? A server's apps, a domain's services, an account's keys.
- **blast** — if this were compromised, what's reachable from it — one hop and every hop after.
- **unregistered** — what exists in the world that the graph doesn't know about yet. The gap is where risk hides.

```
bun ~/.claude/LIFEOS/ATLAS/Atlas.ts owns <key>
bun ~/.claude/LIFEOS/ATLAS/Atlas.ts blast <key>
bun ~/.claude/LIFEOS/ATLAS/Atlas.ts unregistered
```

## A blast-radius walkone key, followed through the graph

**Asset.** An API key for your email service, created two years ago.

**Unlocks.** Sending as you, from any machine that holds it.

**Reachable.** The newsletter platform wired to that address, and its subscriber list.

The question that matters — *if this leaked, what would it reach?* — is answered by walking edges, not by remembering. A list of assets can't do this walk; a graph does it in one query.

## How the graph stays current

Collectors keep it current from the systems that already know the truth, so it reflects reality instead of the last time someone remembered to update a spreadsheet. The implication is architectural — the *right place* for the truth about an asset is wherever the asset is managed, and the collectors are the contract that brings it into the graph. Drift in the source systems surfaces as drift in the graph; drift in the graph means you can ask *what's drifted?* and find out.

## Why graph for blast radius specifically

The blast question is a graph traversal: from a node, follow every edge that represents a *can affect, a given compromise*. Lists cannot do this — by the time you've enumerated "what this key unlocks," you're enumerating relationships, not catching them. A graph makes the question O(graph-size) rather than O(human-memory).

This matters most during an incident. When something leaks or breaks, the first hour is usually spent building the inventory you should have had; with the graph already current, scoping a compromise starts from the traversal, not from archaeology.

## Connection to other patterns

- [[Concepts/append-only-amber-ledger-capture]] — the graph could be assembled from collectors that emit to an amber ledger, with the graph as the indexed view
- [[Concepts/four-tier-verification-stack]] — the unregistered query is a check: it's the question "what does the system not yet see?"
- [[Concepts/deterministic-hook-guardrails]] — collectors are scheduled or hook-triggered refreshes

## Key Insights

1. **Graph, not list.** Lists can't answer blast; graphs can.
2. **Edges are the relationships that actually matter.** Not "asset X is a kind of Y" — "asset X unlocks asset Y."
3. **Built-in queries, not afternoon-long research.** `owns`, `blast`, `unregistered` should be one-liners.
4. **Collectors keep it current.** The graph reflects the truth at the source, not the truth at last audit.
5. **Unregistered is where risk lives.** What the graph doesn't know is what an attacker can find first.

## Related Concepts

- [[Entities/lifeos]] — primary productization (the Atlas component)

## References

- Raw: [[Raw/lifeos-philosophy-atlas-2026-10-05]]
- Origin essay: [Continuous Asset Management Security](https://danielmiessler.com/blog/continuous-asset-management-security)