---
title: "AST Sandbox Verification for Model-Generated Code"
details: "Security pattern where a model's generated program is parsed into an AST and walked before execution to reject forbidden operations, dynamic dispatch escapes, and calls to unapproved modules. Validation happens on structure, not on text."
tags:
  - concept
  - tooling
  - software-engineering
created: 2026-10-18
updated: 2026-10-18
type: concept
sources:
  - Raw/self-improving-harness-codeact-elixir-sidecar.md
---

# AST Sandbox Verification for Model-Generated Code

When an agent may write programs rather than select from a fixed tool list, the containment boundary moves from *call validation* to *program validation*. Instead of checking each tool call as it arrives, the entire generated program is parsed into an AST and inspected before a single instruction executes.

## Why text matching is not enough

A regex denylist over the source string is trivially escaped — variable indirection, computed module names, and function references passed as values all evade substring matching. Walking the parsed tree closes those holes because it operates on what the compiler will actually see.

This is also why the choice of execution language matters: a language with no inspectable AST (JavaScript's `new Function`, Ruby blocks) can only be validated textually. See [[homoiconic-runtime-extensibility]] for the full comparison.

## The verification walk

On BEAM, `Macro.prewalk/3` traverses every node, accumulating rejection reasons rather than failing on the first — the model then gets the complete list of problems in one error instead of discovering them one round-trip at a time.

```elixir
defp verify_ast_nodes(ast, mode) do
  {_ast, errors} =
    Macro.prewalk(ast, [], fn node, acc ->
      case check_node(node, mode) do
        :ok -> {node, acc}
        {:error, reason} -> {node, [reason | acc]}
      end
    end)

  case Enum.reverse(errors) do
    [] -> :ok
    reasons -> {:error, Enum.uniq(reasons)}
  end
end
```

## What gets rejected

**Forbidden local calls.** Process primitives and metaprogramming forms are blocked outright:

```elixir
@forbidden_local_calls [
  :apply, :spawn, :spawn_link, :spawn_monitor, :send, :receive, :exit, :throw,
  :import, :require, :use, :quote, :unquote, :unquote_splicing,
  :defmacro, :defmacrop, :defimpl, :defprotocol, :binding
]
```

`:apply` is the critical entry: it is the standard escape hatch that lets a program invoke an arbitrary function by computed name, bypassing any static check.

**Dynamic module dispatch.** A call target must resolve to a concrete alias; a computed target is a rejection, not a warning:

```elixir
defp resolve_module_alias({:__aliases__, _, parts}) when is_list(parts) do
  if Enum.all?(parts, &is_atom/1), do: {:ok, Module.concat(parts)}, else: :dynamic_target
end
defp resolve_module_alias(_), do: :dynamic_target
```

**Direct Erlang module calls.** Bypassing the Elixir layer entirely is refused, so the allowlist cannot be sidestepped through the underlying runtime.

**Function captures.** `&Module.fun/arity` is checked with the same allowlist as a direct call, since a capture is a deferred invocation.

**Direct Erlang module calls.** Bypassing the Elixir layer entirely is refused, so the allowlist cannot be sidestepped through the underlying runtime.

## Capability allowlisting

Resolution alone is not permission. Each resolved `module`/`function` pair is checked against a capability table:

```elixir
defp allowed_module?(module, func) do
  cond do
    func in [:apply, :spawn, :spawn_link, :exit] -> false
    module == Task -> func in [:async_stream, :async, :await, :await_many]
    module in @allowed_stdlib_modules -> true
    String.starts_with?(Atom.to_string(module), "Elixir.Agent.Tools.") -> true
    String.starts_with?(Atom.to_string(module), "Elixir.Agent.Skills.") -> true
    true -> false
  end
end
```

Note the structure: a small pure-stdlib allowlist, `Task` narrowed to just the concurrency primitives, and prefix matching for the agent's own tool and skill namespaces. The final `true -> false` is the load-bearing default — anything not explicitly permitted is denied.

## Two modes, one verifier

The same walk serves two different gates with different rules:

- **Ephemeral mode** (`execute_elixir`) — rejects `defmodule` outright. One-off code may not define modules; that is the registrar's job.
- **Skill mode** (`register_elixir_skill`) — requires the code to be *exactly one* `defmodule Agent.Skills.<Name>` block, and permits `use Agent.Tool` where ephemeral mode does not.

Separating the modes means a model cannot promote arbitrary code by simply switching to the other endpoint.

## Verification is necessary, not sufficient

A clean AST walk proves the program does not call anything forbidden. It does not bound what the program costs. That is the job of process isolation — memory caps, wall-clock timeouts, and preemption — documented in [[sandboxed-execution-for-ai-agents]]. A well-behaved infinite loop passes every AST check and is only stopped by the timeout.

## Known limits

- **The allowlist is the policy.** Validation is only as good as the capability table; a too-broad prefix match reopens the hole.
- **Resource-exhaustion patterns that need no forbidden call** (huge list comprehensions, exponential string building) still require the memory cap to stop.
- **Transitive effects.** If an allowed `Agent.Tools.*` function itself performs arbitrary IO, the sandbox inherits that capability. Verification is local to the AST, not to the reachable behaviour.
- **Erlang's `:erlang` module** is a persistent escape route if any prefix match is written carelessly.

## Related Concepts

- [[codeact-executable-tool-calling]] — why programs need validating at all
- [[sandboxed-execution-for-ai-agents]] — the containment layer AST checks cannot provide
- [[homoiconic-runtime-extensibility]] — structured code-as-data is the precondition
- [[beam-sidecar-runtime-for-agents]] — where this verifier runs
- [[runtime-skill-hotloading]] — the second gate that shares this verifier