---
title: "Deployment Versioning and Tag Routing"

details: "Kitaru deployment model: a flow source is the recipe; a deployment version is one immutable saved copy; an invocation starts a fresh execution from that copy. Versions auto-increment per flow (v1, v2, ...). Tags are human-readable selectors that point at versions: exclusive tags (default, stable, prod) point at one version at a time and move when re-attached; shared tags (experiment, team-a, benchmark) can point at multiple versions but invoke requires single resolution. The 'default' tag is reserved, always exclusive, auto-assigned to the first deployment, and cannot be removed. There is no per-deployment token — auth uses the workspace/service-account credentials the CLI/SDK/MCP already use. Invocations are serverless (no long-lived per-version service); a deployment requires a remotely-executable stack. This is a clean producer/consumer split: the producer owns source + deploys + moves tags, the consumer only needs a flow name + selector."
tags:
  - concepts
source: https://docs.zenml.io/kitaru
created: 2026-07-10
updated: 2026-07-10
type: concept
sources:
  - .Raw/docs-zenml-kitaru-2026-07-10.md
---

# Deployment Versioning and Tag Routing

**Source:** Kitaru Docs ([[Raw/docs-zenml-kitaru-2026-07-10]])
**Category:** Architecture Pattern
**Status:** Production-validated

---

## Overview

The deployment model is a serverless, versioned, tag-routed invocation layer on top of the durable-execution runtime. The flow source is the recipe; a deployment version is one immutable saved copy; an invocation starts a fresh execution from that copy. The producer/consumer split is clean: producers own the source and the tags, consumers only need a flow name and a selector.

## Core Content

### What gets saved

A deployment is a Kitaru-managed saved snapshot. The runtime treats it as immutable. It records:

- Public flow name
- Integer version (auto-assigned)
- Representative deployment-time input values
- Deploy-time image config (when provided)
- The stack context
- Public routing tags

Deployment-time inputs should be representative — they let the runtime prepare the saved snapshot for flows whose shape depends on concrete parameters. Later invocations can override those values by passing new inputs, but they cannot rewrite the deployment image.

### Auto-versioning

Kitaru assigns deployment versions automatically per flow:

- First deployment of `research_agent` becomes version `1`
- Next becomes `2`
- Each flow has its own independent version sequence

Internally the runtime injects the version into the backend snapshot name (`v1`, `v2`, ...) and scans existing snapshots to allocate the next version. If two deploys race, the runtime retries with the next available version.

### Tag modes

| Mode | Behavior | Example use |
|------|----------|-------------|
| Exclusive | Tag points at exactly one version; adding it to a new version moves it away from older versions | `default`, `stable`, `prod` |
| Shared | Tag can point at multiple versions; invoking by the tag requires single resolution | `experiment`, `team-a`, `benchmark` |

The `default` tag is special:

- Reserved by the runtime
- Always exclusive, even if you pass `exclusive=False`
- Auto-assigned to the first deployment of a flow
- Cannot be removed

A deployment that still has any exclusive tag cannot be deleted. Because `default` cannot be removed, the operator moves it to another version before deleting the old default version.

### Routing story (concrete)

1. Deploy `research_agent` for the first time → runtime creates `v1` and tags it `default`
2. Deploy a candidate with `--tag canary --exclusive` → runtime creates `v2` and tags it `canary`
3. Invoke `kitaru invoke research_agent --tag canary` to test `v2`
4. When satisfied, move the stable route: `kitaru flow tag research_agent --tag stable --version 2 --exclusive`

### Invocation model

`kitaru invoke` is the primary CLI verb. Omit both `--version` and `--tag` and the runtime tries the implicit `default` route. If no deployment exists, it errors clearly. If deployments exist but none is currently `default`, invoke with an explicit tag or version, or move `default` first.

In Python, `.invoke()` is the remote invocation verb for deployed flows:

```python
flow_name.invoke(input=...)               # default route
flow_name.invoke(version=2, input=...)    # pin to a version
flow_name.invoke(tag="stable", input=...) # by tag
```

The active Kitaru project is set by `kitaru login --project ...`, `kitaru project use ...`, or `KITARU_PROJECT` for headless environments. Deployments are created in the active project; switching projects reroutes the same commands.

### Serverless routing

Invoking a deployment starts a new durable execution from a saved version. It does not call a long-lived Python process owned by the producer, and does not create an always-on service per version. The route is: flow name + tag/version selector.

- Consumer invokes `research_agent` + `stable`
- Runtime resolves the route to the saved snapshot for the selected deployment version
- Runtime starts a normal execution from that saved snapshot and returns a normal execution handle

No long-lived per-version service, no per-deployment token.

### Authentication

Deployments have no per-deployment tokens. Access is controlled by the same active Kitaru server connection the CLI / SDK / MCP server already use. For a remote Kitaru server: authenticate once, choose the project. For headless environments: configure with environment variables. For automation: `KITARU_AUTH_TOKEN` is normally a service-account API key created with `kitaru auth service-accounts create` and `kitaru auth api-keys create`.

For shell scripts or CI, `kitaru flow deployments curl FLOW` generates a copy-pasteable curl command. The generator calls `kitaru auth token` to fetch a short-lived bearer token from the active connection (it does not inline real token values). The bearer is temporary; long-lived automation credentials come from `kitaru auth api-keys`.

When a curl is generated from a tag like `default` or `stable`, it is pinned to the deployment version that tag resolved to at generation time. Regenerate the command if the producer moves the tag later.

### Stack requirement

Deployment creation is only supported for stacks that the Kitaru server can execute remotely from a saved snapshot. Local stacks are rejected (CLI, SDK, MCP). Snapshot-backed invocation depends on server workload-manager support; the official `zenmldocker/kitaru` image enables this. Custom images or plain ZenML server setups need workload-manager support preserved (e.g. via `ZENML_SERVER_WORKLOAD_MANAGER_IMPLEMENTATION_SOURCE`).

## Key Insights

1. The model is a clean producer/consumer split — producer owns source + deploys + moves tags, consumer only needs a flow name and a selector
2. Exclusive vs. shared tags express the deployment intent (`default` is exclusive by design, `experiment` is shared so you can compare versions)
3. `default` cannot be removed → to delete a version, move `default` first
4. No per-deployment token removes a class of operational pain; the tradeoff is that the auth model is the same workspace/service-account boundary used for everything else

## Related Concepts

- [[Concepts/agent-stack-layers]] — the platform vs. runtime split that this model respects
- [[Concepts/three-plane-agent-runtime]] — the planes that execute the deployment's invocations
- [[Entities/kitaru]] — the canonical implementation

## References

- Raw Article: [[Raw/docs-zenml-kitaru-2026-07-10]]
- Original: https://docs.zenml.io/kitaru/core-concepts/deployments
