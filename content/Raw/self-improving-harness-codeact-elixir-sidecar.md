---
title: "Self-Improving Harness: CodeAct with an Elixir/BEAM Sidecar"
details: "Research notebook (Gemini share) on replacing sequential JSON tool schemas with a CodeAct architecture. Starts from Common Lisp runtime function definition as the homoiconic ideal, surveys runtime-code-generation support across eight languages, then designs a hybrid TypeScript harness plus Elixir/BEAM sidecar that hot-compiles LLM-written Agent.Skills.* modules at runtime."
tags:
  - raw
  - agent
  - elixir
created: 2026-10-18
updated: 2026-10-18
type: raw
source: https://share.gemini.google/dCxmI7hs2txa
---

# Self-Improving Harness: CodeAct with an Elixir/BEAM Sidecar

**Source:** Gemini shared conversation, "Dynamic Functions in Lisp", created 2026-10-20 (as dated in the source; ingested 2026-10-18).
**Original artifact:** A generated research notebook `Self-Improving-Harness.md` plus a PDF, produced via a Python/WeasyPrint script.

The notebook proposes moving AI agent tool calling away from brittle, sequential JSON schemas toward a **CodeAct** architecture powered by a runtime-extensible language. It starts from how Common Lisp defines and compiles functions at runtime, surveys modern language alternatives, and settles on a hybrid **TypeScript + Elixir (BEAM) sidecar**: the TypeScript harness keeps orchestration, LLM loop, UI and auth, while an isolated Elixir runtime owns multi-step tool composition and dynamic skill creation. Requests become Elixir pipelines for immediate execution, or get promoted into compiled, documented `.beam` modules (`Agent.Skills.*`) that permanently expand the agent's capabilities without a restart.

## Part 1 — Foundations: runtime function definition in Lisp

Lisp treats code and data as interchangeable structures (**homoiconicity**) and keeps its compiler and evaluator available for the whole life of a running program. There is no strict compile-time/runtime boundary.

### 1.1 Closures and anonymous functions

A `lambda` returned from a function captures its lexical environment in a closure. Because Common Lisp is a **Lisp-2** (functions and variables live in separate namespaces), calling a function held in a variable requires `funcall` or `apply`.

```lisp
(defun make-multiplier (factor)
  "Returns a new function at runtime that multiplies its input by FACTOR."
  (lambda (x) (* x factor)))

(defparameter *triple* (make-multiplier 3))
(funcall *triple* 10) ; => 30
(apply *triple* '(7)) ; => 21
```

### 1.2 Binding to a global function name

To call a generated function as an ordinary named function, assign the function object into a symbol's **function cell** with `symbol-function`:

```lisp
(setf (symbol-function 'quadruple) (make-multiplier 4))
(quadruple 5) ; => 20

(defun register-multiplier (name factor)
  (setf (symbol-function name) (make-multiplier factor)))

(register-multiplier 'times-ten 10)
(times-ten 4) ; => 40
```

### 1.3 Compiling code lists on the fly

When a function's shape isn't known until runtime, build an S-expression for a `lambda` and hand it to `compile`, which emits **native machine code in memory** (on SBCL).

```lisp
(defun build-polynomial (a b c)
  "Builds and compiles f(x) = ax^2 + bx + c into machine code at runtime."
  (let ((code `(lambda (x)
                 (+ (* ,a x x)
                    (* ,b x)
                    ,c))))
    (compile nil code)))

(defparameter *poly* (build-polynomial 2 3 5))
(funcall *poly* 4) ; => 49
```

### 1.4 Evaluating raw S-expressions

`eval` runs a raw S-expression list in the **null lexical environment** (global scope only). The notebook notes that production systems should prefer `compile` or lexical closures over `eval` for performance and lexical safety.

## Part 2 — Cross-language landscape for runtime code generation

| Language | Native closures | Structured code-as-data (AST) | Runtime native/JIT compilation | Key mechanism |
| --- | --- | --- | --- | --- |
| **Common Lisp / Clojure** | Yes | Yes (S-expressions) | Yes (`compile` / JVM JIT) | `(compile nil '(lambda ...))` |
| **Julia** | Yes | Yes (`Expr` objects) | Yes (LLVM JIT) | `@eval` with `:(...)` quoting and `$` splicing |
| **Elixir (BEAM)** | Yes | Yes (3-element quoted tuples) | Yes (BEAM bytecode / JIT) | `Code.eval_quoted/3`, `Code.compile_quoted/2` |
| **C# (.NET)** | Yes | Yes (`Expression<T>`) | Yes (`.Compile()` via CLR JIT) | `System.Linq.Expressions` |
| **Smalltalk (Pharo)** | Yes | Yes (live object graph) | Yes (VM bytecode/JIT) | `MyClass compile: '...'` in a live image |
| **Python** | Yes | Via `ast` stdlib module | Bytecode only (CPython) | `compile(ast_tree, filename, "exec")` |
| **JavaScript** | Yes | No (requires strings) | Yes (`new Function` via V8 JIT) | `new Function('a', 'b', 'return a + b')` |
| **Ruby** | Yes | No (`define_method` blocks) | Yes (YJIT) | `define_method(:name) { ... }` |

## Part 3 — Elixir as an internal action and skill language

### 3.1 Why Elixir + BEAM over JSON tool schemas or Python `exec`

1. **Pipeline composition (`|>`)** maps naturally to multi-step data transformations, eliminating multi-turn LLM roundtrips for intermediate filtering and mapping.
2. **Built-in concurrency (`Task.async_stream`)** lets agents fan out concurrent tool calls across cores and IO in a single expression, with built-in timeouts and backpressure.
3. **Pattern matching and `with` blocks** enforce structured handling of `{:ok, val}` / `{:error, reason}` tuples directly inside generated code.
4. **First-class bytecode documentation** (`@moduledoc`, `@doc`, `@spec`) is compiled into `.beam` chunks. The runtime can introspect loaded modules and auto-generate a compact LLM prompt catalog, claimed at roughly **70% fewer tokens than JSON Schema**.
5. **Preemptive scheduling and per-process memory caps.** Unlike Python or Node.js, BEAM can spawn an isolated process with `max_heap_size` and preemptive timeouts, so runaway agent code cannot starve the host.

### 3.2 Engineering traps and mitigations on the BEAM

- **Atom table exhaustion.** The BEAM atom table (roughly 1M entries) is not garbage-collected. *Mitigation:* avoid generating dynamic module names on ephemeral turns (`Code.eval_quoted/3`); restrict atom creation or validate ASTs before execution.
- **Module purge collisions.** BEAM holds two versions of a module (`current` and `old`). *Mitigation:* use ephemeral AST evaluation for one-off queries, and only compile named modules (`defmodule Agent.Skills.*`) when promoting a validated workflow to a persistent skill.
- **Dynamic dispatch bypass.** An LLM might escape static checks via `Kernel.apply/3`. *Mitigation:* walk the AST with `Macro.prewalk/3` and reject `apply`, `spawn`, `send`, `receive`, and unapproved module calls before evaluation.

## Part 4 — Hybrid TypeScript harness + Elixir sidecar prototype

### 4.1 Architecture

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

### 4.2 Standardized tool behaviour (`Agent.Tool`)

```elixir
defmodule Agent.Tool do
  @moduledoc """
  Behaviour and macro for all Agent-accessible Elixir tools and runtime skills.
  """

  @callback __tool_category__() :: :core | :learned_skill

  defmacro __using__(opts) do
    category = Keyword.get(opts, :category, :core)

    quote do
      @behaviour Agent.Tool
      @impl true
      def __tool_category__, do: unquote(category)
    end
  end
end
```

### 4.3 Example core tool (`Agent.Tools.CRM`)

```elixir
defmodule Agent.Tools.CRM do
  use Agent.Tool, category: :core

  @moduledoc "Query and update customer records and subscription tiers."

  @doc "Fetches a customer map by ID. Returns {:ok, customer} or {:error, :not_found}."
  @spec get_customer(String.t()) :: {:ok, map()} | {:error, atom()}
  def get_customer(customer_id) do
    {:ok, %{id: customer_id, name: "Acme Corp", is_vip: false, mrr: 1200}}
  end

  @doc "Lists all invoices for a given status (:overdue | :paid | :draft)."
  @spec list_invoices(atom()) :: {:ok, list(map())} | {:error, term()}
  def list_invoices(status) when status in [:overdue, :paid, :draft] do
    {:ok, [%{id: "inv_1", customer_id: "cust_99", amount: 450.0, status: status}]}
  end
end
```

### 4.4 Runtime prompt catalog introspector (`Agent.Introspector`)

Scans loaded BEAM modules, filters for `Agent.Tool` implementations, and renders their `@moduledoc`, `@doc`, and `@spec` into an LLM-ready string.

```elixir
defmodule Agent.Introspector do
  @doc """
  Scans all loaded BEAM modules, filters for Agent.Tool implementations,
  and formats their @moduledoc, @doc, and @spec into an LLM-ready prompt string.
  """
  def generate_prompt_catalog do
    :code.all_loaded()
    |> Enum.map(fn {mod, _path} -> mod end)
    |> Enum.filter(&implements_agent_tool?/1)
    |> Enum.map(&format_module_docs/1)
    |> Enum.join("\n\n")
  end

  defp implements_agent_tool?(module) do
    function_exported?(module, :__tool_category__, 0)
  end

  defp format_module_docs(module) do
    {:docs_v1, _, :elixir, _, %{"en" => moduledoc}, _, func_docs} = Code.fetch_docs(module)
    {:ok, specs} = Code.Typespec.fetch_specs(module)

    spec_map =
      Map.new(specs, fn {{name, arity}, [spec_ast | _]} ->
        {{name, arity}, Macro.to_string(Code.Typespec.spec_to_quoted(name, spec_ast))}
      end)

    functions_text =
      for {{:function, name, arity}, _, _signatures, %{"en" => doc}, _} <- func_docs do
        spec_str = Map.get(spec_map, {name, arity}, "#{name}/#{arity}")
        "  # #{String.replace(doc, "\\n", " ")}\n  @spec #{spec_str}"
      end
      |> Enum.join("\n\n")

    """
    ### #{inspect(module)} (#{module.__tool_category__()})
    # #{moduledoc}
    #{functions_text}
    """
  end
end
```

### 4.5 Dynamic skill compiler and loader (`Agent.SkillLoader`)

To let `Code.fetch_docs/1` read `@doc` chunks from dynamically compiled skills, the loader writes the in-memory `.beam` binary to an `ebin` path registered with `:code.add_patha/1`.

```elixir
defmodule Agent.SkillLoader do
  @skills_dir "/tmp/agent_skills_ebin"

  def init_code_path do
    File.mkdir_p!(@skills_dir)
    :code.add_patha(String.to_charlist(@skills_dir))
  end

  def compile_and_load_skill(elixir_source_code) do
    with {:ok, ast} <- Code.string_to_quoted(elixir_source_code),
         :ok <- Agent.Sandbox.verify_skill_ast(ast) do

      {compiled_modules, diagnostics} =
        Code.with_diagnostics(fn ->
          Code.compile_quoted(ast, "runtime_skill.ex")
        end)

      for {module_name, beam_binary} <- compiled_modules do
        beam_path = Path.join(@skills_dir, "#{module_name}.beam")
        File.write!(beam_path, beam_binary)
        :code.load_binary(module_name, String.to_charlist(beam_path), beam_binary)
      end

      {:ok, Enum.map(compiled_modules, &elem(&1, 0)), diagnostics}
    end
  end
end
```

### 4.6 AST security verifier and isolated process executor (`Agent.Sandbox`)

```elixir
defmodule Agent.Sandbox do
  @moduledoc """
  AST security verifier and isolated BEAM process executor for LLM-generated Elixir code.
  """

  @allowed_stdlib_modules [
    Enum, Map, MapSet, List, Keyword, String, Integer, Float,
    Date, Time, DateTime, NaiveDateTime, URI, Jason, Task, Stream, Access, Tuple
  ]

  @forbidden_local_calls [
    :apply, :spawn, :spawn_link, :spawn_monitor, :send, :receive, :exit, :throw,
    :import, :require, :use, :quote, :unquote, :unquote_splicing,
    :defmacro, :defmacrop, :defimpl, :defprotocol, :binding
  ]

  @default_timeout_ms 10_000
  @default_max_heap_words 2_500_000 # ~20 MB on 64-bit BEAM

  def eval_ephemeral(code_string, bindings \\ [], opts \\ []) do
    with {:ok, ast} <- parse_code(code_string, existing_atoms_only: false),
         :ok <- verify_ephemeral_ast(ast) do
      run_in_isolated_process(fn ->
        {result, _new_bindings} = Code.eval_quoted(ast, bindings)
        result
      end, opts)
    end
  end

  def verify_skill_ast({:defmodule, _meta, [{:__aliases__, _, [:Agent, :Skills, _skill_name]}, [do: body]]}) do
    verify_ast_nodes(body, :skill_mode)
  end

  def verify_skill_ast(_other) do
    {:error, "Skill code must be a single `defmodule Agent.Skills.<SkillName> do ... end` definition."}
  end

  def verify_ephemeral_ast(ast), do: verify_ast_nodes(ast, :ephemeral_mode)

  defp parse_code(code_string, opts) do
    case Code.string_to_quoted(code_string, opts) do
      {:ok, ast} -> {:ok, ast}
      {:error, {location, message, token}} ->
        {:error, "Syntax error at #{inspect(location)}: #{inspect(message)} #{inspect(token)}"}
    end
  end

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

  defp check_node({:use, _, [{:__aliases__, _, [:Agent, :Tool]} | _]}, :skill_mode), do: :ok

  defp check_node({:defmodule, _, _}, :ephemeral_mode) do
    {:error, "`defmodule` is not allowed in execute_elixir. Use `register_elixir_skill` to define a module."}
  end

  defp check_node({form, _meta, args}, _mode)
       when is_atom(form) and is_list(args) and form in @forbidden_local_calls do
    {:error, "Forbidden operation `#{form}` is not permitted in the sandbox."}
  end

  defp check_node({{:., _, [target, func]}, _, _args}, _mode) when is_atom(func) do
    case resolve_module_alias(target) do
      {:ok, module} ->
        if allowed_module?(module, func),
          do: :ok,
          else: {:error, "Disallowed call to `#{inspect(module)}.#{func}`."}
      :dynamic_target ->
        {:error, "Dynamic module dispatch is forbidden. Call known modules explicitly."}
    end
  end

  defp check_node({{:., _, [erlang_mod, _func]}, _, _}, _mode) when is_atom(erlang_mod) do
    {:error, "Direct calls to Erlang module `#{inspect(erlang_mod)}` are forbidden."}
  end

  defp check_node({:&, _, [{:/, _, [{{:., _, [target, func]}, _, _}, _arity]}]}, _mode) do
    case resolve_module_alias(target) do
      {:ok, module} ->
        if allowed_module?(module, func),
          do: :ok,
          else: {:error, "Disallowed function capture on `#{inspect(module)}.#{func}`."}
      :dynamic_target ->
        {:error, "Dynamic function captures are forbidden."}
    end
  end

  defp check_node(_other_node, _mode), do: :ok

  defp resolve_module_alias({:__aliases__, _, parts}) when is_list(parts) do
    if Enum.all?(parts, &is_atom/1), do: {:ok, Module.concat(parts)}, else: :dynamic_target
  end
  defp resolve_module_alias(_), do: :dynamic_target

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

  defp run_in_isolated_process(fun, opts) do
    timeout = Keyword.get(opts, :timeout, @default_timeout_ms)
    max_heap = Keyword.get(opts, :max_heap_words, @default_max_heap_words)
    caller = self()
    ref = make_ref()

    {pid, monitor_ref} =
      Process.spawn(
        fn ->
          if ctx = Keyword.get(opts, :context), do: Process.put(:agent_context, ctx)
          try do
            send(caller, {ref, {:ok, fun.()}})
          rescue
            e ->
              send(caller, {ref, {:runtime_error, Exception.format(:error, e, __STACKTRACE__)}})
          end
        end,
        [:monitor, max_heap_size: %{size: max_heap, kill: true, error_logger: true}]
      )

    receive do
      {^ref, result} ->
        Process.demonitor(monitor_ref, [:flush])
        result
      {:DOWN, ^monitor_ref, :process, ^pid, :killed} ->
        {:error, "Execution terminated: Exceeded maximum memory limit."}
      {:DOWN, ^monitor_ref, :process, ^pid, reason} ->
        {:error, "Execution process crashed: #{inspect(reason)}"}
    after
      timeout ->
        Process.exit(pid, :kill)
        Process.demonitor(monitor_ref, [:flush])
        {:error, "Execution timed out after #{timeout}ms."}
    end
  end
end
```

### 4.7 HTTP sidecar router (`Agent.Router`)

```elixir
defmodule Agent.Router do
  use Plug.Router

  plug :match
  plug Plug.Parsers, parsers: [:json], pass: ["application/json"], json_decoder: Jason
  plug :dispatch

  get "/catalog" do
    send_json(conn, 200, %{catalog: Agent.Introspector.generate_prompt_catalog()})
  end

  post "/execute" do
    %{"code" => code} = conn.body_params
    context = Map.get(conn.body_params, "context", %{})

    case Agent.Sandbox.eval_ephemeral(code, [context: context], context: context) do
      {:ok, result} -> send_json(conn, 200, %{status: "ok", result: result})
      {:runtime_error, trace} -> send_json(conn, 200, %{status: "runtime_error", error: trace})
      {:error, reasons} -> send_json(conn, 200, %{status: "sandbox_rejected", error: reasons})
    end
  end

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

  defp send_json(conn, status, body) do
    conn
    |> put_resp_content_type("application/json")
    |> send_resp(status, Jason.encode!(body))
  end
end
```

## Part 5 — Next research milestones

1. **Bidirectional TypeScript callback bridge.** Allow Elixir `Task.async_stream` pipelines to invoke legacy TypeScript tools over WebSockets / JSON-RPC.
2. **System prompt and Elixir agent cheat sheet.** Design a concise prompt block that steers LLMs toward immutable pipelines (`Enum`, `with`, pattern matching) and away from imperative habits.
3. **Skill versioning, testing and persistence.** Require LLM-submitted skills to include inline doctests or ExUnit assertions that pass before hot-loading into the catalog.

## Ingestion Notes

- The source conversation contains a failed first attempt at the notebook-generation script (`IndentationError: unexpected indent` on the `@moduledoc` body) followed by a corrected rewrite. Only the corrected markdown body is retained here.
- The source's own title, "Dynamic Functions in Lisp", describes the *conversation* topic; the notebook's subject is Elixir. This page is titled for its actual subject per the wiki's naming discipline.