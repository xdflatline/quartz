---
title: "CodeAct: Executing Tool Calls as Code Instead of JSON Schemas"
details: "Agent architecture pattern where the model writes executable code that composes multiple tool calls in one step, rather than emitting one structured tool call per round-trip. Reduces LLM turns and lets control flow live in code the model already knows how to write."
tags:
  - concept
  - agent
  - agentic-system
created: 2026-10-18
updated: 2026-10-18
type: concept
sources:
  - Raw/self-improving-harness-codeact-elixir-sidecar.md
---

# CodeAct: Executing Tool Calls as Code Instead of JSON Schemas

**CodeAct** is an agent architecture pattern in which the model is given a small set of *meta-tools* — typically a code executor and a tool/skill registrar — and writes actual program text that invokes tools, rather than emitting one structured JSON object per tool call.

## The problem it solves

A JSON-schema agent loop is inherently sequential and expensive:

1. The model emits one tool call.
2. The harness executes it and returns the result.
3. The model reasons over that result and emits the next call.

Filtering a list, mapping over it, and aggregating the result — work that takes three lines of code — costs three full LLM round-trips. Each round-trip pays for re-sending context and re-deriving state the model already knows.

With CodeAct, the same work is one code block:

```elixir
{:ok, customers}
|> Agent.Tools.CRM.list_invoices(:overdue)
|> Enum.filter(&(&1.amount > 100))
|> Enum.map(& &1.customer_id)
|> Enum.uniq()
```

The intermediate filter and map happen *inside* the execution, not across three model turns.

## Why it needs a runtime-extensible language

CodeAct only pays off if the execution language is cheap to write in and cheap to constrain. The candidate languages were surveyed in [[Raw/self-improving-harness-codeact-elixir-sidecar|Raw/self-improving-harness-codeact-elixir-sidecar]]; the ones that support all three of the following are viable hosts:

- **Closures** — capture values at runtime.
- **Structured code-as-data** — an AST you can inspect *before* executing, not just a string. Python needs the `ast` module to get this; JavaScript and Ruby largely do not have it.
- **Runtime compilation** — so a validated program can be promoted to a permanent, fast, compiled artifact rather than re-interpreted on every turn.

Elixir/BEAM satisfies all three (`Code.eval_quoted/3` for ephemeral, `Code.compile_quoted/2` for promoted). See [[homoiconic-runtime-extensibility]] for the underlying Lisp-derived framing.

## The two meta-tools

The architecture that instantiates this exposes exactly two tools to the model:

- `execute_elixir(code)` — run a pipeline now, return the result. Sandbox-enforced; nothing persists.
- `register_elixir_skill(module_code)` — promote a validated workflow to a compiled, documented module that becomes part of the agent's permanent tool catalog.

The split matters: **ephemeral execution is cheap but forgets everything; skill registration is expensive but accumulates**. A self-improving agent needs both, and needs to know which one it is calling. See [[runtime-skill-hotloading]].

## Where the safety boundary goes

CodeAct inverts the usual shape of a sandbox. Instead of validating individual calls, the boundary is drawn around a *whole program* before it runs. Three layers, in order:

1. **AST validation** — walk the parsed tree, reject forbidden calls and dynamic dispatch. See [[ast-sandbox-verification]].
2. **Process isolation** — run the program in a fresh BEAM process with `max_heap_size` and a wall-clock timeout, so runaway code is killed rather than starving the host. See [[sandboxed-execution-for-ai-agents]].
3. **Capability restriction** — an allowlist of callable modules and functions, checked per resolved call site.

## The token argument

JSON schemas must describe every tool's parameters in the prompt. Elixir compiles `@moduledoc`, `@doc`, and `@spec` into `.beam` bytecode chunks that the runtime reads back at runtime, so the catalog can be *generated from the loaded modules* rather than hand-maintained in a schema file. The source notebook claims roughly 70% fewer prompt tokens; see [[bytecode-self-documenting-tool-catalog]] for the mechanism and the caveat that this number is a source-side estimate, not measured.

## Trade-offs

- **Security surface is much larger.** A model that can write arbitrary code within a capability sandbox can attempt far more than a model constrained to a fixed tool list.
- **Debugging is harder.** A failed pipeline reports one error, not a trace of which tool call went wrong.
- **Requires a good runtime.** No `max_heap_size` and no preemptive timeout means no meaningful containment — this is why BEAM specifically is chosen over Python or Node.
- **Language fit matters.** Steering a model toward idiomatic pipelines (`Enum`, `with`, pattern matching) instead of imperative habits is a distinct prompt-engineering problem the source flags as unsolved.

## Related Concepts

- [[homoiconic-runtime-extensibility]] — the Lisp-derived property that makes code-as-data possible
- [[ast-sandbox-verification]] — validating generated code before it executes
- [[runtime-skill-hotloading]] — promoting ephemeral code to permanent compiled capability
- [[bytecode-self-documenting-tool-catalog]] — generating the prompt catalog from loaded modules
- [[beam-sidecar-runtime-for-agents]] — the deployment topology this pattern assumes
- [[tool-calling-llm]] — the structured-output baseline CodeAct replaces
- [[sandboxed-execution-for-ai-agents]] — containment via memory caps and preemption