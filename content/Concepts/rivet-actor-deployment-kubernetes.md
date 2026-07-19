---
title: "Rivet Actor Deployment on Kubernetes"
detail: "Procedure for deploying AgentOS / RivetKit apps to Kubernetes with the right graceful-shutdown, Ingress timeout, and secret settings."
details: "AgentOS deploys to Kubernetes via RivetKit. Required: Node 20-alpine Dockerfile; container registry push; Rivet Cloud (or self-hosted Rivet Engine) account; `RIVET_ENDPOINT` and `RIVET_PUBLIC_ENDPOINT` secrets; Deployment with `terminationGracePeriodSeconds: 2100` (35 min) to cover the Rivet runner's 30 min actor-graceful-shutdown budget; Service and Ingress with proxy read/send/connect timeouts raised to at least 3600 seconds (1 hour) to keep long-lived WebSocket connections alive — default 30-60s timeouts cause reconnect storms."
tags:
  - concepts
created: 2026-07-19
updated: 2026-07-19
type: concept
source: "[[Raw/agentos-sdk-dev-docs-2026-07-19]]"
---

# Rivet Actor Deployment on Kubernetes

**Source:** Documentation bundle ([[Raw/agentos-sdk-dev-docs-2026-07-19]])
**Category:** Architecture Pattern / Technical Reference
**Status:** Production-validated

## Overview

The procedure for deploying AgentOS / RivetKit apps to Kubernetes. Three things will silently break the deployment if missed: short `terminationGracePeriodSeconds`, default Ingress idle timeouts, and missing Rivet endpoint secrets. This concept captures the working recipe.

## Core Content

### Prerequisites

- A Kubernetes cluster with `kubectl` access (EKS, GKE, k3s, etc.)
- Container registry credentials (Docker Hub, GHCR, GCR, etc.)
- Your RivetKit app (or use the [Quickstart](https://rivet.dev/docs/actors/quickstart))
- Access to [Rivet Cloud](https://dashboard.rivet.dev/) or a [self-hosted Rivet Engine](https://rivet.dev/docs/general/self-hosting)

### Step 1: Package Your App

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
ENV PORT=8080
CMD ["node", "server.js"]
```

### Step 2: Build and Push

```bash
docker build -t registry.example.com/your-team/rivetkit-app:latest .
docker push registry.example.com/your-team/rivetkit-app:latest
```

### Step 3: Provision Environment Variables

From the Rivet dashboard, create a project with Kubernetes as the provider. You get `RIVET_ENDPOINT` and `RIVET_PUBLIC_ENDPOINT`. Store in a Secret:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: rivetkit-secrets
type: Opaque
stringData:
  RIVET_ENDPOINT: <your-rivet-endpoint>
  RIVET_PUBLIC_ENDPOINT: <your-rivet-public-endpoint>
```

### Step 4: Deploy

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rivetkit-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: rivetkit-app
  template:
    metadata:
      labels:
        app: rivetkit-app
    spec:
      # Allow enough time for actors to gracefully stop on SIGTERM.
      # The runner waits up to 30m for actors to finish.
      # Add buffer for runner shutdown overhead after actors stop.
      terminationGracePeriodSeconds: 2100
      containers:
        - name: rivetkit-app
          image: registry.example.com/your-team/rivetkit-app:latest
          envFrom:
            - secretRef:
                name: rivetkit-secrets
```

Apply:

```bash
kubectl apply -f rivetkit-secrets.yaml
kubectl apply -f deployment.yaml
```

### Step 5: Expose and Connect to Rivet

1. Add a Service and Ingress to expose the app externally (e.g. `my-app.example.com`)
2. On the Rivet dashboard, paste the domain with the `/api/rivet` path (e.g. `https://my-app.example.com/api/rivet`)
3. Click "Done"

**Critical:** Rivet envoys connect to your app over long-lived WebSockets, and your app's clients (browsers, SDKs) do the same. Default Ingress and load-balancer idle timeouts (typically 30-60 seconds) drop these connections and cause reconnect storms.

Raise the idle / read / send timeout on every Ingress and load balancer in front of your app to at least 1 hour (3600 seconds):

- **NGINX Ingress:** `nginx.ingress.kubernetes.io/proxy-read-timeout: "3600"` and `proxy-send-timeout: "3600"`
- **AWS Load Balancer Controller (ALB):** `alb.ingress.kubernetes.io/load-balancer-attributes: idle_timeout.timeout_seconds=3600`
- **GCE Ingress (GKE):** set `timeoutSec: 3600` on the `BackendConfig` referenced by the Service

### Step 6: Verify

```bash
kubectl get pods -l app=rivetkit-app
```

App should appear as connected on the Rivet dashboard once the pod is ready.

## How AgentOS Scales on Kubernetes

- **Stateless worker pool** — RivetKit pod replicas form a pool; `replicas: N` is the unit of horizontal scaling for the request-handling layer
- **Stateful actor hosting** — actors (and their `/home/agentos` SQLite-backed FS) are placed by Rivet Engine; the engine handles distribution
- **In-process VM density** — V8 isolates + kernel state in tens of MB per VM; thousands of VMs per pod
- **Sleep/wake** — actors sleep after configurable idle timeout (default 30s); next prompt transparently restores the VM, so idle agents consume near-zero resources
- **Workflow primitive** — wrap `run` handler in `workflow()`; each `ctx.step()` is recorded, retried, resumed independently (durable step-level retries)
- **Self-hosted Rivet Engine** — runs the orchestration plane; engine itself is the unit you scale (cluster mode); supported on Kubernetes, Hetzner, VM, and bare metal

## Key Insights

1. **`terminationGracePeriodSeconds: 2100` is non-obvious** — comes from the Rivet runner's 30 min actor-shutdown budget plus shutdown overhead. Default 30s K8s gives would SIGKILL active actors
2. **Ingress timeouts are the most common silent failure** — WebSockets drop every 30-60s, dashboard shows reconnects but agents seem to work
3. **Engine scaling is orthogonal to actor scaling** — the engine is its own workload; agents inside actors are ephemeral, the engine is durable
4. **Rivet Cloud is the zero-ops path** — self-hosted engine is for compliance-sensitive or cost-optimized deployments

## Related Concepts

- [[Concepts/in-process-vm-agent-runtime-agentos]] — the runtime deployed via this procedure
- [[Concepts/durable-actor-session-sleep]] — graceful-shutdown math derives from actor sleep semantics
- [[Concepts/sandbox-mounting-extension-pattern]] — extension to full sandboxes from inside the actor

## Related Entities

- [[Entities/agentos]] — the deployed workload
- [[Entities/rivet]] — the platform and engine being deployed

## References

- Raw Documentation: [[Raw/agentos-sdk-dev-docs-2026-07-19]]
- Rivet K8s docs: https://rivet.dev/docs/deploy/kubernetes
- Self-hosting guide: https://rivet.dev/docs/general/self-hosting
- Quickstart: https://rivet.dev/docs/actors/quickstart
