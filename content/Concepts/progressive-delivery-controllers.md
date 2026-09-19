---
title: "Progressive Delivery Controllers"
details: "Architecture pattern that decouples deployment from release by orchestrating canary traffic shifting, evaluating runtime SLO metrics, and triggering automatic rollback — without requiring a new deployment commit when canary thresholds are breached."
tags:
  - concept
  - tooling
  - kubernetes
created: 2026-09-19
updated: 2026-09-19
type: concept
sources:
  - "[[Raw/devto-systems-for-modern-architectures-2026-09-19]]"
---

# Progressive Delivery Controllers

**Source:** [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
**Category:** Architecture Pattern
**Status:** Production-validated

---

## Overview

Progressive delivery is the pattern of separating *deployment* (the artifact is on a node and ready to serve) from *release* (real user traffic is routed to it), and using automated metric-driven analysis to shift traffic incrementally and roll back without a new commit when SLOs are violated.

## Core Content

### Mechanism

1. The new version is deployed alongside the stable version (canary + primary).
2. The controller shifts a small percentage of traffic to the canary (e.g., 10%), evaluates runtime metrics over an analysis interval.
3. If SLO metrics (success rate ≥ 99.5%, p99 latency ≤ 500 ms) hold, the controller increments traffic weight and re-evaluates.
4. If SLO metrics breach, the controller rolls traffic back to the primary without deploying anything new — the rollback is purely a routing decision.

### Example Specification (Flagger)

```yaml
apiVersion: flagger.app/v1beta1
kind: Canary
metadata:
  name: payment-processing-service
spec:
  analysis:
    interval: 30s
    threshold: 5
    maxWeight: 50
    stepWeight: 10
    metrics:
      - name: request-success-rate
        thresholdRange: { min: 99.5 }
      - name: request-duration
        thresholdRange: { max: 500 }
    webhooks:
      - name: load-test-trigger
        type: rollout
        url: http://flagger-loadtester.testing/
        metadata:
          cmd: "k6 run /scripts/payment-workload.js -q"
```

### Operational Characteristics

| Property | Value |
| --- | --- |
| Primary failure domain | Blast-radius expansion, faulty deploys |
| Architectural plane | Traffic Control Plane |
| Host boundary | Ingress / Service Mesh |
| State persistence | Key-Value configuration stores (etcd / Raft) |
| Network overhead | Low (header evaluation & routing) |

## Key Insights

1. Rollback is a routing decision, not a deployment decision — the bad version stays deployed (cheap) while traffic is shifted away (instant).
2. Metric thresholds are the contract — the controller cannot enforce a SLO the operator has not specified.
3. The analysis interval is the latency floor for bad-releases to be detected; sub-30-second detection requires a different control loop.

## Related Concepts

- [[Concepts/distributed-tracing-fabrics]] — the SLO signals the controller evaluates are typically derived from trace and metric pipelines.
- [[Concepts/distributed-load-testing-traffic-simulation]] — canary webhooks often trigger a load test as part of the analysis loop.

## References

- Raw Article: [[Raw/devto-systems-for-modern-architectures-2026-09-19]]
- Original: https://dev.to/wantsvibes/developer-tools-beyond-ides-10-systems-for-modern-architectures-1gn8