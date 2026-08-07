---
title: "Sandbox Mounting Extension Pattern"

details: "AgentOS hybrid model: agents run in the lightweight in-process VM by default (fast, granular permissions, host bindings) and spin up a full sandbox (E2B, Daytona, Modal, Cloudflare, Vercel, ComputeSDK, Sprites, Local, Docker) on demand for workloads that need a real Linux kernel. The sandbox filesystem is mounted into the VM as a native directory, and the agent reads/writes it the same way it reads local files. Process management is exposed via host bindings. 9 providers supported, all in Beta as of v0.2.7."
tags:
  - concepts
  - runtime
  - agent
created: 2026-07-19
updated: 2026-07-19
type: concept
source: "[[Raw/agentos-sdk-dev-docs-2026-07-19]]"
---

# Sandbox Mounting Extension Pattern

**Source:** Documentation bundle ([[Raw/agentos-sdk-dev-docs-2026-07-19]])
**Category:** Architecture Pattern
**Status:** Production-validated (9 providers, all Beta as of v0.2.7)

## Overview

AgentOS's hybrid model: agents run in the lightweight in-process VM by default (fast startup, granular permissions, host bindings) and spin up a full sandbox (E2B, Daytona, Modal, Cloudflare, Vercel, ComputeSDK, Sprites, Local, Docker) on demand for workloads that need a real Linux kernel. The sandbox filesystem is mounted into the VM as a native directory.

## Core Content

### When to Use Each

| | agentOS VM | Full Sandbox |
| --- | --- | --- |
| **Cost** | Very low (in-process) | Pay per second of uptime |
| **Startup** | ~6 ms | Seconds |
| **Backend integration** | Direct (bindings) | Indirect (network calls) |
| **Credentials** | Stay on host | Must be injected into environment |
| **Permissions** | Granular, deny-by-default | Coarse-grained (container-level) |
| **Infrastructure** | `npm install` | Vendor account + API keys |
| **Best for** | Coding, file manipulation, scripting, API calls, orchestration | Browsers, desktop automation, native compilation, dev servers |

### When to Use agentOS VM

- Coding and file editing
- Running scripts and CLI tools
- Calling APIs and services via bindings
- Multi-agent orchestration and workflows
- Tasks where backend integration matters (permissions, tool access, LLM routing)

### When to Use Full Sandbox

- Browsers and desktop automation (Playwright, Puppeteer, Selenium)
- Heavy compilation and native toolchains
- Dev servers with hot reload, databases, system ports
- GUI applications and VNC sessions

### Both Together

Use agentOS with sandbox mounting for workflows that need both:

- Agent runs in the agentOS VM with full access to bindings and permissions
- Sandbox spins up on demand for heavy tasks
- Sandbox filesystem is mounted into the VM as a native directory
- Agent reads and writes sandbox files the same way it reads local files
- Process management exposed via host bindings

### Supported Providers (9, all Beta)

| Provider | Environment |
|----------|-------------|
| **Local** | Directly on the local machine for dev/test |
| **Docker** | Isolated local containers |
| **E2B** | E2B's cloud infrastructure (secure, ephemeral) |
| **Daytona** | Daytona's managed development environments |
| **Modal** | Modal's serverless cloud infrastructure |
| **Cloudflare** | Sandbox SDK containers on global network |
| **Vercel** | Edge and serverless platform |
| **ComputeSDK** | ComputeSDK compute provider |
| **Sprites** | Sprites' cloud sandbox infrastructure |

### Cloud Browser (Standalone)

- **Browserbase** (Beta) — the `browse` CLI lets agents browse the web with a cloud browser, no sandbox required

## Key Insights

1. **You don't have to choose** — agentOS is explicitly designed to pair with full sandboxes, not replace them
2. **Mounting makes the boundary invisible** — agent reads sandbox files the same way it reads local files
3. **9 providers** means lock-in is avoidable — switch providers without rewriting agent code
4. **Local + Docker** as first-tier providers means dev/test works without external accounts
5. **Process management via bindings** is the bridge — sandbox processes get exposed to the agent as host-defined commands

## Related Concepts

- [[Concepts/in-process-vm-agent-runtime-agentos]] — the VM being extended
- [[Concepts/kernel-syscall-isolation-vm]] — when isolation is enough
- [[Concepts/binding-cli-shim-pattern]] — how sandbox process management is exposed

## Related Entities

- [[Entities/agentos]] — the canonical implementation
- [[Entities/browserbase]] — the cloud browser alternative

## References

- Raw Documentation: [[Raw/agentos-sdk-dev-docs-2026-07-19]]
- Versus sandbox: https://agentos-sdk.dev/docs/versus-sandbox
- Registry: https://agentos-sdk.dev/registry
