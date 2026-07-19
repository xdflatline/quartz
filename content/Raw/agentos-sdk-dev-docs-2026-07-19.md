# AgentOS Documentation

**Source:** agentOS official docs + GitHub README (https://agentos-sdk.dev/docs/)
**Date Retrieved:** 2026-07-19
**Type:** Documentation Bundle

**Repository:** https://github.com/rivet-dev/agentos (3.9k stars, Apache-2.0, v0.2.7 Jul 7 2026)

---

## Why AgentOS

A portable open-source operating system for AI agents. Near-zero cold starts (~6 ms), up to 32× cheaper than traditional sandboxes. Built-in ACP agents: Pi, Claude Code, OpenCode. Deny-by-default permissions. Direct host bindings, no network hops. Single `npm install` deploys to laptop, Rivet Cloud, Railway, Vercel, Kubernetes, or any container platform.

> "agentOS runs AI agents and untrusted code safely inside fully virtualized Linux VMs. Nothing the guest does touches your host directly: there is no real host filesystem, no real host network socket, and no real host process. Every guest operation is serviced by a kernel that agentOS owns."

## Benchmarks (March 2026, Intel i7-12700KF, 10000 runs)

### Cold Start

| Percentile | agentOS | Fastest Sandbox (E2B) | Speedup |
|---|---|---|---|
| p50 | 4.8 ms | 440 ms | **92×** |
| p95 | 5.6 ms | 950 ms | **170×** |
| p99 | 6.1 ms | 3,150 ms | **516×** |

### Memory per Instance

| Workload | agentOS | Cheapest Sandbox (Daytona) | Reduction |
|---|---|---|---|
| Full coding agent (Pi + MCP + FS) | ~131 MB | ~1,024 MB | **8×** |
| Simple shell command | ~22 MB | ~1,024 MB | **47×** |

### Cost per Second (Self-Hosted, 70% utilization)

| Hardware | agentOS | vs Sandbox |
|---|---|---|
| AWS ARM | $0.0000032/s | 6× cheaper |
| AWS x86 | $0.0000053/s | 3× cheaper |
| Hetzner ARM | $0.0000011/s | 17× cheaper |
| Hetzner x86 | $0.0000013/s | 14× cheaper |

---

## Architecture: 3 Roles

| Role | What it is | Key trait |
|------|-----------|-----------|
| **App (Client)** | Your code (TypeScript or Rust) | Trusted caller; never runs guest code |
| **Server (Sidecar)** | Trusted core hosting VMs | Owns every kernel; brokers all syscalls |
| **VM** | Isolated Linux environment | Fully virtualized; unit of isolation |

- App drives agentOS over the wire — creating VMs, opening sessions, sending prompts.
- The sidecar manages many VMs side by side; a crash in one never affects another.
- Two VMs share nothing: each has its own filesystem, process table, and network policy.

## Anatomy of a Linux VM

Every VM has two halves separated by a security boundary:

### Kernel (Trusted Core, written primarily in Rust)

- **Virtual filesystem** — per-VM VFS; guest I/O never hits host disk
- **Process table** — kernel-managed, no real host processes spawned
- **Socket table & DNS** — virtual network stack; outbound traffic gated by network allowlist
- **Pipes / PTYs** — kernel-owned IPC/terminals for real Linux shell behavior
- **Policy & limits** — permission policy, network allowlist, resource limits enforced on every request

### Executor (Untrusted)

- **JavaScript Acceleration** — Guest JS runs on native V8 with full JIT inside an isolate; native speed with normal Node.js semantics
- **WASM** — Shell (`sh`), coreutils, and custom modules run as WebAssembly
- **Native binaries** — Mounted tools run inside the same boundary
- **No host fallthrough** — executor holds no capability of its own; every operation is a syscall serviced by the kernel

### Processes & Shell

- `exec()` / `run()` start fresh guest processes; `spawn` for long-running; interactive shells supported
- Each `exec()` / `run()` starts a brand new guest process — in-memory state never leaks between runs
- stdio bridged through kernel-owned pipes and PTYs

### Virtual Filesystem

- **Layered engines:** root layer (snapshot) + overlay (guest writes) + grafted mount points
- **Host-backed mounts:** Guest paths can map to host directories, S3, or cloud stores
- **Confinement:** Kernel restricts I/O to mount root, defeating symlink and `..` tricks
- **Persistence:** `/home/agentos` survives sleep/wake

### Networking

- One authoritative transport. Guest `fetch()`, `node:http`, `node:net`, WASM sockets all target the same kernel socket table
- Egress gated by network allowlist; loopback stays confined to the VM
- Guest servers exposable via signed preview URLs

## Sidecar Process Architecture (Core Package)

- Every VM runs inside a shared sidecar process (the `default` pool), not its own OS process
- Each additional VM adds only marginal cost — V8 isolate + kernel state
- Per-VM memory: tens of MB
- Warm VM creation: single-digit milliseconds
- Disposing a VM tears down only that VM; the shared sidecar stays alive for the host process lifetime
- Explicit sidecar option isolates a group of VMs in their own process for advanced use

---

## Agents & Sessions

- **Sessions via ACP (Agent Communication Protocol):** universal transcript format across all agents
- Built-in agents: **Pi**, **Claude Code**, **OpenCode**; **Codex** is installable as registry software
- Bring your own agent by speaking ACP inside the VM
- Long-lived sessions survive across many prompts (unlike one-shot `exec()`)
- Real-time `sessionEvent`s streamed to your app
- agentOS prepends a system prompt describing the VM environment, commands, and bindings

## Session Durability

- **Durable semantic events** — completed ACP updates and permission request/response records sequenced in SQLite
- **Streaming message deltas** — live-only, not persisted
- **Durable files** — `/home/agentos` persists via sidecar's direct SQLite-over-UDS connection
- `sessionId` is stable across VM sleep and adapter restarts; adapter's private ACP session ID is internal
- `openSession` is idempotent; repeating is safe; changing immutable options for an existing ID returns `session_conflict`
- After VM sleep, the next `prompt` transparently starts the adapter using a three-tier fallback:
  1. Preferred: native ACP `session/resume`
  2. Fallback: stable `session/load`
  3. Final fallback: fresh private ACP session with bounded continuation context from AgentOS history
- Fallback transcript bounded by `limits.acp.maxFallbackContinuationBytes`
- Adapter replay emitted during load is suppressed because SQLite is the sole history source of truth

## Event Durability Levels

| Level | Behavior |
|-------|----------|
| `durability: "ephemeral"` | Live agent-message or thought delta. Not sequenced or stored. |
| `durability: "durable"` | Has a session sequence. Emitted only after SQLite transaction commits. Completed/coalesced chunks are durable. |

`sessionEvent` is a flat discriminated union. The top-level `type` is the native ACP `SessionUpdate.sessionUpdate` value, with ACP payload fields sitting directly beside the durability envelope. There is no nested `update` wrapper.

## SQLite-Only Reads (no adapter spin-up)

- `getSession`
- `listSessions`
- `readHistory`
- `getSessionConfig`
- `getSessionCapabilities`
- `getSessionAgentInfo`

`readHistory({ sessionId, before, after, limit })` reads only SQLite; `before` and `after` are exclusive and mutually exclusive. Consumers deduplicate live durable delivery by `(sessionId, sequence)`.

## Permissions & Approvals

Two independent layers:
1. **Permission policy** — kernel-enforced on every syscall; nothing allowed until opted in
2. **Approvals** — agent-level "ask before using a tool"

Policies: `allow_all`, `reject_all`, or `"ask"` (human-in-the-loop via session-event stream). `"ask"` requests never expire; they block the active turn until answered or a lifecycle transition wins the race.

## System Prompt Injection

- agentOS automatically injects a system prompt describing the VM environment, available commands, and bindings
- The base prompt is embedded in the sidecar (not written to a file inside the VM)
- Additive — never replaces the agent's own instructions (CLAUDE.md, AGENTS.md, etc.)
- `additionalInstructions` appends session-specific text after the base OS prompt and before the generated binding docs
- `skipOsInstructions` suppresses the base OS prompt while still injecting the generated binding docs

---

## Bindings

Bindings expose custom host JavaScript functions to agents as auto-generated CLI commands installed at `/usr/local/bin/agentos-{name}` inside the VM. Injected into the agent's system prompt; callable in scripts for code-mode token savings (up to 80% token reduction).

### Required per binding

- `description`
- `inputSchema` (Zod)
- `execute` handler
- Optional: `examples`, `timeout` (ms; no timeout by default)

### Zod to CLI Mapping

| Zod type | CLI syntax | Example |
| --- | --- | --- |
| `z.string()` | `--name value` | `--path /tmp/out.png` |
| `z.number()` | `--name 42` | `--limit 5` |
| `z.boolean()` | `--flag` / `--no-flag` | `--full-page` |
| `z.enum(["a","b"])` | `--name a` | `--format json` |
| `z.array(z.string())` | `--name a --name b` | `--tags foo --tags bar` |

Optional fields (`.optional()`) become optional flags. Field names convert from `camelCase` to `kebab-case`. Use `.describe()` for useful `--help` output.

### Output Format

- Success — exits 0, writes JSON envelope to stdout: `{"ok":true,"result":{...}}`
- Failure — exits non-zero, writes error message to stderr

### Bindings vs. MCP Servers

| | Bindings | MCP Servers |
| --- | --- | --- |
| **How it works** | Call JS functions on host directly | Connect to a standard MCP server |
| **Authentication** | None — direct binding | Custom per-server auth config |
| **Code mode** | Built-in (up to 80% token reduction) | Requires extra work |
| **Latency** | Near-zero (bound to host process) | Extra network hop |
| **Setup** | Define in actor code with Zod | Configure any standard MCP server |

Use bindings for your own JS functions. Use MCP servers for existing third-party services.

---

## Orchestration: Rivet Actors

The `agentOS()` actor wraps the raw VM in a Rivet Actor, which adds durable state, scheduling, and orchestration.

### Actor Properties

- **Durable server objects** — reach by name: `vm.getOrCreate("my-agent")`
- **Stateful by default** — persists filesystem, actor state, durable session metadata, completed ACP history
- **Portable runtime** — consistent across infrastructures

### Cron

- Schedule shell commands or agent sessions via cron expressions
- Overlap control: `allow` (default), `skip`, or `queue`
- Observable via `cronEvent`s
- Jobs keep the actor alive during execution; actor sleeps between runs
- Custom `id` at creation for easier management
- List and cancel via API

### Workflows

- Wrap the actor's `run` handler in `workflow()`; each `ctx.step()` is recorded, retried, and resumed independently

### Agent-to-Agent

- One agent calls another through a binding
- The caller gets a binding it invokes itself, which bridges into another agent's isolated VM

### Multiplayer

- Multiple clients observe/collaborate with the same agent session in real time
- Events broadcast to all connected clients

---

## Persistence & Sleep

agentOS persists `/home/agentos` filesystem, durable session catalog, and completed session history across actor sleep. A later client call wakes a fresh VM. Adapter processes, running commands, shells, live subscriptions, and in-progress ACP deltas do not survive VM shutdown.

### What Persists

| Data | Persists? |
|------|-----------|
| Files in `/home/agentos` | **Yes** (Actor SQLite over UDS) |
| Preview URL tokens | **Yes** |
| Session catalog and configuration | **Yes** |
| Completed ACP session history | **Yes** |
| Live ACP adapter process | No (restored lazily) |
| In-progress message deltas | No |
| Cron job definitions | No |
| Running processes / active shells | No |
| In-memory mounts | No |

The native sidecar reads/writes filesystem chunks directly through the actor's authenticated SQLite Unix socket. File contents never pass through the TypeScript or JavaScript actor layer. VM creation supplies one SQLite descriptor shared by filesystem metadata, filesystem blocks, and core session persistence.

### Sleep Configuration

- **Default idle sleep timeout:** 30 seconds
- **Graceful shutdown budget:** 15 minutes
- **Action timeout:** 2,147,483,647 ms (~24.8 days) — prevents human permission review from being cut off
- All configurable via actor's `options` configuration

An active prompt turn uses RivetKit's keep-awake scope through the terminal SQLite commit. An idle durable session does not keep the actor awake.

### VM Lifecycle Events

- `connection.on("vmBooted", ...)` and `connection.on("vmShutdown", ...)` via native RivetKit subscriptions
- Hosting events, intentionally absent from Core

---

## Webhooks

Trigger agent sessions from external webhooks via a lightweight HTTP server (e.g. Hono). Critical behavior: **AgentOS automatically serializes concurrent prompts** targeting the same session — no application queue needed. Durable session history remains in SQLite, but AgentOS never automatically replays a prompt whose delivery was uncertain.

---

## Deployment

agentOS is powered by Rivet, an open-source actor platform, and runs as Rivet Actors. Three production paths:

1. **Rivet Cloud** — fully managed (Rivet Compute, or bring your own cloud), zero-ops
2. **Self-hosted** — open-source Rivet platform on your own infrastructure (Kubernetes, Hetzner, VMs, etc.) for full control
3. **agentOS Core** — embed `@rivet-dev/agentos-core` directly in any Node.js backend, no platform required

### Deploy Targets

- **Rivet Compute** (fully managed)
- **Vercel** (serverless)
- **Railway** (cloud infrastructure)
- **Kubernetes** (self-hosted on your cluster)
- **AWS ECS**
- **Google Cloud Run**
- **Hetzner**
- **VM & Bare Metal**
- **Custom Platform**

### Kubernetes Deployment (Rivet)

Prerequisites: Kubernetes cluster with `kubectl` access (EKS, GKE, k3s, etc.), container registry credentials, RivetKit app, Rivet Cloud account or self-hosted Rivet Engine.

1. **Package your app** — Dockerfile:
   ```
   FROM node:20-alpine
   WORKDIR /app
   COPY package*.json ./
   RUN npm ci --omit=dev
   COPY . .
   ENV PORT=8080
   CMD ["node", "server.js"]
   ```

2. **Build and push the image:**
   ```
   docker build -t registry.example.com/your-team/rivetkit-app:latest .
   docker push registry.example.com/your-team/rivetkit-app:latest
   ```

3. **Set environment variables** — from the Rivet dashboard after creating the project with Kubernetes provider: `RIVET_ENDPOINT`, `RIVET_PUBLIC_ENDPOINT`. Secret manifest:
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

4. **Deploy** — Deployment manifest with `terminationGracePeriodSeconds: 2100` (35 min) for graceful actor shutdown (Rivet runner waits up to 30m for actors to finish, plus shutdown overhead):
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
         terminationGracePeriodSeconds: 2100
         containers:
           - name: rivetkit-app
             image: registry.example.com/your-team/rivetkit-app:latest
             envFrom:
               - secretRef:
                   name: rivetkit-secrets
   ```
   Apply: `kubectl apply -f rivetkit-secrets.yaml && kubectl apply -f deployment.yaml`

5. **Connect to Rivet** — add Service and Ingress to expose the app externally (e.g. `my-app.example.com`). On the Rivet dashboard, paste the domain with `/api/rivet` path. **Critical:** raise Ingress/load-balancer idle/read/send timeouts to at least 1 hour (3600s) — default 30-60s timeouts drop long-lived WebSocket connections and cause reconnect storms. Examples:
   - **NGINX Ingress:** `nginx.ingress.kubernetes.io/proxy-read-timeout: "3600"`, `proxy-send-timeout: "3600"`
   - **AWS ALB:** `alb.ingress.kubernetes.io/load-balancer-attributes: idle_timeout.timeout_seconds=3600`
   - **GCE Ingress (GKE):** `timeoutSec: 3600` on the `BackendConfig` referenced by the Service

6. **Verify:** `kubectl get pods -l app=rivetkit-app` — app should appear as connected on the Rivet dashboard

### Scaling Agents (Architecture-Level)

AgentOS inherits Rivet Actor semantics for scaling. Each `vm.getOrCreate("name")` is a durable, named server object. Multiple replicas of the RivetKit pod form a pool; the Rivet engine (cloud or self-hosted) routes clients to the right actor. Key scaling behaviors:

- **In-process VM density** — V8 isolates + kernel state in tens of MB per VM; thousands of VMs per host
- **Actor pool** — RivetKit pod replicas form a stateless worker pool; `replicas: N` is the unit of horizontal scaling for the request-handling layer
- **Stateful actor hosting** — actors (and their `/home/agentos` SQLite-backed FS) are placed by Rivet Engine; the engine handles distribution
- **Sidecar pool** — each Node process hosts a sidecar that runs many VMs; explicit-sidecar option lets you isolate groups of VMs in their own process
- **Sleep/wake** — actors sleep after configurable idle timeout (default 30s); next prompt transparently restores the VM, so idle agents consume near-zero resources
- **Workflow primitive** — wrap `run` handler in `workflow()`; each `ctx.step()` is recorded, retried, and resumed independently (durable step-level retries)
- **Keep-awake** — active turns use RivetKit's keep-awake scope through terminal SQLite commit, so an in-progress turn cannot be killed by sleep
- **Self-hosted Rivet Engine** — runs the orchestration plane; engine itself is the unit you scale (cluster mode); the docs reference Kubernetes, Hetzner, VM, and bare-metal as supported engines

---

## Integrations (Registry)

### Agents

- **Pi** — lightweight, fast execution coding agent
- **Claude Code** (Beta) — full tool access, file editing, shell execution
- **Codex** (Beta) — OpenAI's coding agent
- **OpenCode** — open-source coding agent
- **Custom Agent** — bring your own by speaking ACP inside the VM

### File Systems

- **Host Directory** — projects a real host directory into the VM (Docker-style); guest sees only the mounted subtree
- **S3** — S3-compatible bucket; chunked into S3 objects
- **Google Drive** — mount a Google Drive folder
- **In-Memory** — ephemeral scratch, discarded on destroy
- **Sandbox** — mount a sandbox filesystem + process management bindings (any Sandbox Agent provider)

### Browsers

- **Browserbase** (Beta) — `browse` CLI for cloud browser, no sandbox required

### Sandbox Mounting (9 providers, all Beta)

- **Local** — on the local machine for dev/test
- **Docker** — isolated local containers
- **E2B** — cloud infrastructure
- **Daytona** — managed dev environments
- **Modal** — serverless cloud
- **Cloudflare** — Sandbox SDK containers on global network
- **Vercel** — edge and serverless
- **ComputeSDK** — compute provider
- **Sprites** — cloud sandbox infrastructure

### Software (28 WASM packages)

**Meta-packages:** `everything`, `build-essential` (common + git + curl), `common` (coreutils + sed + grep + gawk + findutils + diffutils + tar + gzip)

Individual packages: git, ripgrep, jq, sqlite3, duckdb, vim, tar, ssh (with strict known_hosts + RSA/ECDSA/Ed25519/DH/ECDH/ChaCha20/AES), wget, curl, coreutils (sh, cat, ls, cp, mv, rm, sort, 80+ POSIX), grep, sed, fd, tree, gawk, findutils, zip, unzip, envsubst, gzip, diffutils, yq, file, Codex CLI.

### Custom Software

Package your own agents, command packages, and WASM commands. Compile WASM commands from source in the `secure-exec` registry (https://github.com/rivet-dev/secure-exec).

---

## Core vs. Actor

| Feature | Core (`@rivet-dev/agentos-core`) | Actor (`@rivet-dev/agentos`) |
| --- | --- | --- |
| **Persistence** | In-memory by default (pluggable via mounts) | Persistent filesystem and sessions |
| **Distributed state** | Manage yourself | Built-in |
| **Stateful VMs** | Complex to run yourself | Built into Rivet |
| **Sleep/wake** | Manual `dispose()` / `create()` | Automatic |
| **Events** | Direct callbacks | Broadcast to all connected clients |
| **Preview URLs** | None | Built-in signed URL server |
| **Multiplayer** | N/A | Multiple clients on same actor |
| **Orchestration** | N/A | Workflows, queues, cron |
| **Agent-to-agent** | Custom | Built into Rivet Actors |
| **Authentication** | Set up yourself | Built-in |

`agentOS()` returns an ordinary TypeScript Rivet actor definition. AgentOS actions and events are merged automatically; their names are reserved. After wake, the actor lazily creates the core SDK VM on the first AgentOS action and disposes it on sleep.

### Core Quick Start

```bash
npm install @rivet-dev/agentos-core
```

```typescript
import { AgentOs } from "@rivet-dev/agentos-core";
import pi from "@agentos-software/pi";

const vm = await AgentOs.create({ software: [pi] });
const result = await vm.exec("echo hello");
console.log(result.stdout); // "hello\n"
```

---

## Security Model (Summary)

- **Deny-by-default** for filesystem, network, process, and environment access
- **Programmatic network control** — allow, deny, or proxy any outbound connection
- **Resource limits** — CPU and memory caps per agent
- **VM isolation** — each agent in its own VM, no shared state
- **Two permission layers** — kernel-enforced policy + agent-level approvals
- **Credentials stay on host** — bindings run server-side; agents see only inputs/outputs
- **Coarse-grained container boundaries not needed** — security is enforced at the kernel-syscall level, not at the container level

---

## Tech Stack

- **Primary language:** Rust (kernel, sidecar, secure-exec)
- **JavaScript runtime:** V8 (JIT-compiled, full Node.js semantics)
- **WASM:** shell, coreutils, custom command packages
- **Native binaries:** mounted tools run inside the same boundary
- **SDK languages:** TypeScript (primary client/server), Rust
- **Protocol:** ACP (Agent Communication Protocol) — universal transcript format
- **HTTP framework (webhooks):** Hono (example)
- **Database:** SQLite over Unix Domain Socket (UDS) — actor SQLite shared by filesystem, blocks, and session metadata
- **Built-in JS validation:** Zod for binding input schemas
- **Actor runtime:** Rivet / RivetKit (portable, deploy-anywhere actor model)
- **Package registry:** npm (`@rivet-dev/agentos`, `@rivet-dev/agentos-core`, `@agentos-software/*`)

---

## License & Status

- **License:** Apache-2.0
- **Status:** Preview (v0.2.7 as of Jul 7, 2026); API subject to change
- **GitHub:** https://github.com/rivet-dev/agentos (3.9k stars, 192 forks, 21 releases, 16 contributors)
- **Docs:** https://agentos-sdk.dev/docs/
- **Report issues:** https://github.com/rivet-dev/rivet/issues
- **Discord:** https://rivet.dev/discord
