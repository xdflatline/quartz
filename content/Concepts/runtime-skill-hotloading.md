---
title: "Runtime Skill Hotloading: Turning One-Off Code into Permanent Capability"
details: "Pattern where an agent validates a generated module, compiles it to bytecode at runtime, registers it in the code path so documentation remains readable, and adds it to the tool catalog — permanently extending the agent without a restart."
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

# Runtime Skill Hotloading: Turning One-Off Code into Permanent Capability

A self-improving agent needs two different operations, and conflating them is the main design error:

- **Execute** a pipeline now, forget it afterwards. Cheap, safe, no lasting effect.
- **Install** a workflow so every future turn can call it. Expensive, validated, permanent.

Hotloading is the second. It is what makes "self-improving" literal rather than aspirational: the agent's tool namespace grows at runtime, without a redeploy or restart.

## The ephemeral / persistent split

The distinction maps onto BEAM's two compilation paths, and the choice is not arbitrary:

| | Ephemeral | Persistent skill |
| --- | --- | --- |
| Entry point | `execute_elixir(code)` | `register_elixir_skill(module_code)` |
| Compilation | `Code.eval_quoted/3` | `Code.compile_quoted/2` |
| Shape | any expression | exactly one `defmodule Agent.Skills.*` |
| Catalog effect | none | appears in `/catalog` |
| Verification mode | `verify_ephemeral_ast` | `verify_skill_ast` |

Ephemeral work never creates atoms for module names and never touches the module namespace — which is why it avoids the two hazards described in [[beam-sidecar-runtime-for-agents]]. Only a *validated, promoted* workflow earns the cost and risk of a named module.

## The non-obvious part: writing the .beam to disk

Compiling in memory is not sufficient, and this is the step most implementations miss. `Code.fetch_docs/1` and the whole documentation-introspection path in [[bytecode-self-documenting-tool-catalog]] read the `Docs` chunk from a `.beam` **file** found via the code path. A module that exists only as an in-memory binary has no readable docs, so it would be compiled but invisible to the catalog — permanently present, permanently uncatalogued.

The fix is to materialize the binary into an `ebin` directory registered with the code loader:

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

`Code.with_diagnostics/1` wraps compilation so warnings come back to the caller as data — the model gets compiler feedback in the same turn rather than a silently degraded skill.

## Order of operations

The sequence is a security boundary, not an implementation detail:

1. **Parse** the source to an AST — nothing has run.
2. **Verify** the AST — see [[ast-sandbox-verification]]. This must happen *before* compilation, not after.
3. **Compile** with diagnostics.
4. **Write** the `.beam` to the registered `ebin` path.
5. **Load** the binary into the VM.
6. **Regenerate** the catalog and return it to the harness, so the new tool is immediately usable.

Compiling before verifying would mean model-authored code is compiled on every attempt, including rejected ones — spending the expensive step on inputs that are about to be refused, and risking side effects from macro expansion at compile time.

## The payoff: catalog grows automatically

Because step 6 returns a freshly regenerated catalog, the harness can inject the new skill into its next system prompt without any schema maintenance. A skill that ships with proper `@moduledoc`, `@doc`, and `@spec` is self-describing by construction. A skill missing them is merely callable and invisible — the documentation *is* the API surface.

## Operational consequences

- **The `ebin` directory is durable state.** It outlives the VM. Restart policy, disk growth, and cleanup are now the operator's problem, not the agent's.
- **Version collisions are real.** BEAM keeps `current` and `old` versions of a module; overwriting a skill's `.beam` while the old version is still referenced yields two live versions. See [[beam-sidecar-runtime-for-agents]].
- **Promoted code is permanent and deserves permanent scrutiny.** Ephemeral execution can be treated as disposable. A skill that gets loaded stays loaded, so its AST gate should be at least as strict as for ephemeral code — arguably stricter, since it outlives the turn.
- **Testing before promotion is the missing piece.** The source notebook flags inline doctests or ExUnit assertions that must pass before hot-loading as an open milestone. Without it, the catalog accumulates modules no one has verified beyond static safety checks.

## Related Concepts

- [[codeact-executable-tool-calling]] — the ephemeral/persistent split originates here
- [[ast-sandbox-verification]] — the gate between parse and compile
- [[bytecode-self-documenting-tool-catalog]] — why the `.beam` must be written to disk
- [[beam-sidecar-runtime-for-agents]] — atom-table and module-purge hazards
- [[homoiconic-runtime-extensibility]] — the underlying Lisp-derived capability