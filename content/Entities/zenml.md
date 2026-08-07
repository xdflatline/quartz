---
title: "ZenML"

details: "ZenML is the open-source framework for production ML and LLM pipelines that Kitaru is built on and runs alongside. The two projects work independently — you can use Kitaru without ZenML, or use ZenML without Kitaru — and compose when used together: a Kitaru flow is a dynamic ZenML pipeline under the hood, so agents and ML pipelines share stacks, artifact stores, server, and dashboard. ZenML provides the orchestration substrate (steps, pipelines, stacks, server, dashboard) that Kitaru extends with durable checkpoints, replay, diff, and the agent runtime primitives."
tags:
  - entities
source: https://docs.zenml.io/kitaru
created: 2026-07-10
updated: 2026-07-10
type: entity
sources:
  - .Raw/docs-zenml-kitaru-2026-07-10.md
---

# ZenML

**Source:** Kitaru Docs ([[Raw/docs-zenml-kitaru-2026-07-10]])
**Category:** Platform
**Repository:** https://github.com/zenml-io/zenml
**Website:** https://zenml.io / https://docs.zenml.io

---

## Overview

ZenML is the open-source MLOps/LLMOps framework on which Kitaru is built. Kitaru's documentation explicitly positions it as a sibling project: each works on its own, but they compose when used together. A Kitaru flow is, under the hood, a dynamic ZenML pipeline — the runner, server, stacks, artifact store, and dashboard are all shared.

## Why this entity matters for Kitaru

The Kitaru "agent runs on the same stacks, same server, same dashboard as your ZenML pipelines" claim is meaningful because:

- Any stack that works for a ZenML pipeline (Kubernetes, Vertex AI, SageMaker, AzureML) works for a Kitaru flow with no new infra to operate
- Artifact lineage, versioned outputs, and the metadata store are inherited from ZenML rather than reinvented
- The ZenML Helm chart is the deployment path for the Kitaru server
- The `zenmldocker/kitaru` image is the officially supported runtime that enables snapshot-backed invocation via the workload manager

## Related Concepts

- [[Concepts/agent-stack-layers]] — Kitaru vs. ZenML's positioning
- [[Entities/kitaru]] — the agent runtime built on ZenML

## References

- Raw Article: [[Raw/docs-zenml-kitaru-2026-07-10]]
- Project: https://zenml.io
- Docs: https://docs.zenml.io
