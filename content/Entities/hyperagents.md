---
title: "Hyperagents"
detail: "Zhang et al. 2026. The follow-up to DGM — introduces a meta-agent to control how to modify existing task agents to create new ones. Addresses the open question of which modification strategy to use."
details: "DGM leaves one question open: how should the agent decide *what kind* of edit to make? Hyperagents introduces a **meta-agent that learns a modification policy** over the population. The meta-agent decides whether the next modification should be a refactor, a parameter tweak, a tool addition, or a structural rewrite."
tags:
  - entities
created: 2026-08-07
updated: 2026-08-07
type: entity
source: https://arxiv.org/abs/2603.19461
---

# Hyperagents

**Source:** Zhang et al., "Hyperagents," arXiv:2603.19461, 2026.

## Overview

The follow-up to [[Entities/darwin-godel-machine]]. Introduces a **meta-agent to control how to modify existing task agents to create new ones**. Addresses the open question of which modification strategy to use.

## The Open Question It Answers

DGM's loop has a single mutation operator: the LLM edits the harness. But what kind of edit? A refactor? A parameter tweak? A tool addition? A structural rewrite? DGM leaves this to the LLM's own judgment; Hyperagents externalizes it as a **learned policy**.

## The Meta-Agent

A second-level agent that observes the current population of task agents and decides what modification to apply next. The meta-agent's policy is itself learned, so the search over modification strategies is automated too.

## Related

- [[Entities/darwin-godel-machine]] — the parent
- [[Concepts/darwin-godel-machine]] — the concept
- [[Concepts/meta-harness-outer-loop]] — concurrent related work
- [[Raw/lilianweng-harness-engineering-2026-07-04]] — the source
