---
title: "Bytecode-Self-Documenting Tool Catalogs"
details: "Pattern where a runtime's tool catalog is generated from documentation embedded in compiled artifacts rather than hand-maintained in a schema file, so the API surface cannot drift from the implementation and prompt tokens are spent only on what is callable."
tags:
  - concept
  - agent
  - elixir
created: 2026-10-18
updated: 2026-10-18
type: concept
sources:
  - Raw/self-improving-harness-codeact-elixir-sidecar.md
---

# Bytecode-Self-Documenting Tool Catalogs

In a JSON-schema agent, the tool catalog is a separate artifact from the tool implementations. Someone maintains a schema file; the code and the schema drift apart; the prompt pays for descriptions that may no longer be true.

A **bytecode-self-documenting catalog** inverts this: documentation lives in the compiled artifact, and the catalog is *derived* from loaded modules at runtime. The schema cannot drift, because it is not a schema — it is a projection of the code.

## Why Elixir fits

`@moduledoc`, `@doc`, and `@spec` are compiled into `Docs` and `Dbgi` chunks inside the `.beam` binary. Any process can read them back:

- `Code.fetch_docs/1` — returns `{:docs_v1, _, :elixir, _, moduledoc_map, _, function_docs}`
- `Code.Typespec.fetch_specs/1` + `spec_to_quoted/3` — recovers `@spec` as a stringable AST
- `:code.all_loaded/0` — enumerates every module currently in the VM
- `Module.__info__/1` — introspects loaded modules

That combination is what makes the pattern possible without any runtime being language-aware.

## The introspector

```elixir
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
```

The `Agent.Tool` behaviour makes discovery a predicate check rather than convention:

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

Implementation modules then declare themselves in one line — `use Agent.Tool, category: :core` — and the category flows into the rendered catalog:

```
### Agent.Tools.CRM (core)
# Query and update customer records and subscription tiers.
  # Fetches a customer map by ID. Returns {:ok, customer} or {:error, :not_found}.
  @spec get_customer(String.t()) :: {:ok, map()} | {:error, atom()}

  # Lists all invoices for a given status (:overdue | :paid | :draft).
  @spec list_invoices(atom()) :: {:ok, list(map())} | {:error, term()}
```

Note what the model gets: the return-shape union (`{:ok, _} | {:error, _}`) comes straight from the `@spec`. In a JSON schema this information usually has to be restated in prose because the schema type system cannot express tagged unions.

## The token claim

The source notebook claims roughly **70% fewer prompt tokens than JSON Schema**. Treat that as a source-side estimate rather than a measurement: the comparison depends entirely on which tools are in the catalog, how verbose their JSON schemas are, and whether the pipeline flattens documentation well. The *direction* is well-founded — a rendered `@doc` line plus a `@spec` is far denser than a JSON object with `type`, `properties`, `required`, and nested `items` — but the specific figure is not established.

The stronger argument for the pattern is correctness, not token count: a catalog derived from loaded modules cannot describe a tool that does not exist or misdescribe one that does.

## The disk requirement

`Code.fetch_docs/1` reads from a `.beam` **file** located through the code path. A module compiled purely in memory has no readable docs. This makes writing the binary to a registered `ebin` directory a hard requirement, not an optimization — see [[runtime-skill-hotloading]] for the loader.

## Failure modes

- **Missing docs are invisible.** A tool without `@moduledoc`/`@doc` is callable but absent from the catalog. There is no error; the model simply never learns it exists.
- **Stale code path.** Modules loaded without `:code.add_patha/1` registration will not resolve, and the catalog silently omits them.
- **`{:docs_v1, ...}` pattern matches are brittle.** The tuple shape is a format detail; a hard match on all seven elements breaks on a format revision. A defensive implementation matches more loosely.
- **Only loaded modules appear.** A tool in the source tree but never loaded is invisible — which is why the catalog must be regenerated *after* a skill loads, not before.

## Related Concepts

- [[runtime-skill-hotloading]] — how a new skill enters the catalog
- [[codeact-executable-tool-calling]] — why the catalog is smaller than a schema set
- [[ast-sandbox-verification]] — catalog entries and executable code must agree
- [[beam-sidecar-runtime-for-agents]] — the VM these chunks live in