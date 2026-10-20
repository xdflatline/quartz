---
title: "BEAM Sidecar Runtime for AI Agents"
details: "Deployment topology where a BEAM/Elixir process runs alongside an existing agent harness and owns tool execution and skill compilation, communicating over HTTP, JSON-RPC, or MCP. Motivated by process isolation, memory caps, and preemptive scheduling unavailable on Python or Node."
tags:
  - concept
  - runtime
  - elixir
created: 2026-10-18
updated: 2026-10-18
type: concept
sources:
  - Raw/self-improving-harness-codeact-elixir-sidecar.md
---

# BEAM Sidecar Runtime for AI Agents

A **sidecar** here is a separate runtime process — Elixir on the BEAM — that owns tool execution and dynamic skill compilation for an agent harness written in another language. The harness keeps what it is already good at: orchestration, the LLM loop, UI, auth, and integration with existing TypeScript tooling. The sidecar keeps what BEAM is uniquely good at: cheap process isolation, memory caps, preemption, hot code loading, and bytecode-resident documentation.

## Architecture

```
┌──────────────────────────────────────────────────────────────┐
│ TypeScript Agent Harness (Orchestrator, LLM Loop, UI/Auth)   │
│                                                              │
│  1. Fetches tool signatures from Elixir via GET /catalog     │
│  2. Injects Elixir Module Signatures into System Prompt      │
│  3. Exposes 2 Meta-Tools to LLM:                             │
│     • execute_elixir(code)                                   │
│     • register_elixir_skill(module_code)                     │
└──────────────┬────────────────────────────────▲──────────────┘
               │ HTTP / JSON-RPC / MCP          │ Structured JSON
               ▼                                │ Result + New Specs
┌───────────────────────────────────────────────┴──────────────┐
│ Elixir BEAM Sidecar (Stateful Tool & Skill Runtime)          │
│                                                              │
│  • Base Tools:      Agent.Tools.CRM, Agent.Tools.HTTP, ...   │
│  • Learned Skills:  Agent.Skills.* (Compiled into RAM/Disk)  │
│  • Introspector:    Reads @moduledoc, @doc, @spec from BEAM  │
│  • AST Sandbox:     Validates & runs LLM code in isolated    │
│                     processes with max_heap_size & timeout   │
└──────────────────────────────────────────────────────────────┘
```

Only two meta-tools cross the boundary in the model-facing direction. Everything else is an implementation detail of the sidecar, which is what keeps the harness's tool surface small.

## The interface

A `Plug.Router` with three endpoints:

- `GET /catalog` — returns the introspected prompt catalog, see [[bytecode-self-documenting-tool-catalog]].
- `POST /execute` — runs ephemeral code; returns `status` of `ok`, `runtime_error`, or `sandbox_rejected`.
- `POST /skills` — hot-loads a module; returns loaded module names, compiler diagnostics, and the **regenerated catalog** so the new tool is usable on the next turn.

```elixir
post "/skills" do
  %{"module_code" => module_code} = conn.body_params

  case Agent.SkillLoader.compile_and_load_skill(module_code) do
    {:ok, modules, diagnostics} ->
      send_json(conn, 200, %{
        status: "ok",
        loaded_modules: Enum.map(modules, &inspect/1),
        diagnostics: diagnostics,
        updated_catalog: Agent.Introspector.generate_prompt_catalog()
      })
    {:error, reason} ->
      send_json(conn, 200, %{status: "error", error: reason})
  end
end
```

Returning a rejected run with HTTP 200 and a `status` field is a deliberate choice: a rejected program is a *normal outcome* the model should read and learn from, not a transport error.

## Why BEAM specifically

**Memory caps and preemption.** A process spawned with `max_heap_size` is killed by the VM when it exceeds the limit, and wall-clock timeouts are enforced by the scheduler rather than cooperatively:

```elixir
{pid, monitor_ref} =
  Process.spawn(fn -> ... end,
    [:monitor, max_heap_size: %{size: max_heap, kill: true, error_logger: true}])
```

`kill: true` means an out-of-control process is terminated immediately. Python and Node offer neither a hard per-execution memory cap nor preemptive timeout — a runaway `while True` there cannot be stopped without killing the host. This is the single strongest reason for choosing BEAM over more obvious hosts.

**Concurrency as an expression.** `Task.async_stream` fans out concurrent tool calls across cores and IO in one construct, with timeouts and backpressure built in — see [[codeact-executable-tool-calling]].

**Isolation is the default, not a sandbox.** BEAM processes are cheap and isolated by design. The "sandbox" is not an emulation layer bolted on; it is the runtime's ordinary execution model. See [[sandboxed-execution-for-ai-agents]].

**Hot code loading.** New capabilities are compiled and loaded without a restart — see [[runtime-skill-hotloading]].

## The hazards

These are the reasons the design is a research prototype rather than a production recipe.

**Atom table exhaustion.** The BEAM atom table (roughly 1M entries) is **not garbage-collected**. An atom is created whenever an unknown module or function name appears in generated code. A model that invents module names on every turn will exhaust the table and take down the VM, with no way to recover. *Mitigation:* never generate module names on ephemeral turns; parse ephemeral code with `existing_atoms_only: true` where possible; validate before evaluation.

**Module purge collisions.** BEAM retains two versions of a module (`current` and `old`) during code transitions. Overwriting a skill's `.beam` while the old version is still referenced can produce two live versions of the same module. *Mitigation:* use ephemeral evaluation for one-off work; compile named modules only for promoted skills; version skill filenames deliberately.

**Dynamic dispatch escape.** A model can reach anything through `Kernel.apply/3` or a computed module alias, bypassing any allowlist. *Mitigation:* AST walking before evaluation — see [[ast-sandbox-verification]].

**In-process boundaries.** A sidecar in the same VM shares fate with the runtime. `:erlang` and BIF-level access defeat application-level allowlists; the allowlist must be written so no prefix match reaches Erlang internals.

## Open problems

The source notebook's own milestone list:

1. **Bidirectional callback bridge** — letting Elixir `Task.async_stream` pipelines call back into legacy TypeScript tools over WebSockets/JSON-RPC, so the sidecar is not a one-way sink.
2. **Prompt engineering for idiomatic pipelines** — steering the model toward `Enum`, `with`, and pattern matching rather than imperative habits. The language's idioms are an advantage only if the model writes them idiomatically.
3. **Skill verification before promotion** — requiring inline doctests or ExUnit assertions to pass before a skill enters the catalog, so the catalog does not accumulate unverified modules.

## Related Concepts

- [[codeact-executable-tool-calling]] — the pattern the sidecar serves
- [[sandboxed-execution-for-ai-agents]] — BEAM process isolation as containment
- [[ast-sandbox-verification]] — the security gate on the sidecar
- [[runtime-skill-hotloading]] — how capabilities grow
- [[bytecode-self-documenting-tool-catalog]] — how `/catalog` is produced
- [[homoiconic-runtime-extensibility]] — the property BEAM inherits from Lisp