---
title: "Native Shell Reactive Rendering"
details: "NSH is retained state with declarative construction, on Solid's model. A component body describes its part of the tree once; only the bindings that read a changed signal run again. Choosing between a plain function and a retained component, and reading props where they are used, is what keeps the common path inexpensive."
tags:
  - concept
  - desktop
  - architecture-pattern
  - software-engineering
created: 2026-10-30
updated: 2026-10-30
type: concept
sources:
  - Raw/nsh-coding-guides.md
---
# Native Shell Reactive Rendering

**Source:** [[Raw/nsh-coding-guides]]
**Category:** Architecture Pattern
**Status:** Normative (NSH coding guide)

## The Runs-Once Model

NSH is **retained state with declarative construction**, on Solid's model. A signal survives across updates; a component body describes its part of the tree once, when it is created. Keeping that distinction explicit is the single most important thing to internalize before writing NSH code.

| You write | Runs | Runs again when |
|---|---|---|
| A component body | Once, when it is created | Never |
| A binding: a closure (Rust) or an expression that calls or reads a property (TSX) where a value goes | Once | A signal it read changes; only that prop or child updates |
| `computed(fn)` | When created | A signal it read changes |
| `effect(fn)` | After the elements of the pass exist | A signal it read changes |
| A row of `each` / `<Each>` | When its key first appears | Never; its item and index signals change |
| A cell of `virtual_list` / `<List>` | Once per cell | Never; the cell is given other rows |

The design principle that follows: **make the common path inexpensive.** Developers should be able to build and reuse UI without adding a cache at every call site. The reactive graph, the renderer, layout and lists are native, and one turn of the app's code becomes one batch of native operations. Small costs still multiply across elements and updates — above all in TSX, whose own code runs in an interpreter — so measure exceptional hot paths before adding caches.

## Choosing the Right Unit

**Use a plain function for value-like elements.** The caller supplies current props and handlers, the function returns elements, and nothing of it remains but the bindings it made.

```rust
fn empty_state(title: impl Into<SharedString>) -> impl IntoElement {
    view()
        .gap_2()
        .items_center()
        .child(text(title.into()).text_color(move || theme().muted_foreground))
}
```

**Use a component for retained behavior.** A `#[component]` (or a TSX component that creates signals) is for a piece of UI that owns persistent state or an independent lifecycle: signals, effects, async work, timers, key bindings. Create that state in the component body, once, never inside a binding.

```rust
#[component]
pub fn Search(props: SearchProps) -> impl IntoElement {
    let query = signal(String::new());
    input()
        .value(move || query.get())
        .on_change(move |text: &str| query.set(text.to_owned()))
        .placeholder(move || props.placeholder.get().to_string())
}
```

Do not turn every visual fragment into a component. Component boundaries have lifecycle and coordination costs; use them where retained identity matters.

## Owner, Context, Scope, Refs

- The component that runs is the **owner**: effects, computed values, tasks, timers, key bindings and cleanups created while it runs belong to it and are disposed with it.
- **Context** (`provide_context` / `use_context`, `context()` and `<Ctx.Provider>`) gives a subtree a value without implying that the elements reading it own it.
- A Rust component's **`Scope`** (`cx`) emits its events and reads the insets it is given.
- **Refs** (`element_ref()`, `ref`) name a host element for imperative calls (`focus()`, `scroll_to()`, `measure()`).
- Layout and measurement are later, native phases; use `onLayout` and `measure()` only when resolved geometry is genuinely required.

Never read a context in an event handler or a timer, where there is no component to look it up from: read it in the body and keep what it gave. Retain typed handles (signals, resources, refs, domain ids), which are `Copy` in Rust and stop doing anything once their owner is gone.

## Ownership Links Are Bounded

A component owns what it creates, and everything it created goes away with it: when its `<If>` branch hides, its row is removed, or its page is popped. In Rust, tasks, timers and intervals (`spawn`, `set_timeout`, `set_interval`) and key bindings (`on_key`) end with the owner they were made under; in TSX, register the stop with `cleanup` or return it from the effect.

When something keeps running unexpectedly, inspect first:

- effects and computed values created **outside** a component (in an event handler or a timer callback they have no owner and live forever);
- listeners registered without their stop;
- work started from a store that no component owns.

A dropped `resource` load is aborted; it does not keep its component alive.

**Do not write a signal merely because a value was read or derived.** Avoid unconditional writes from a binding or an effect that reads the same signal: it runs itself again until NSH stops it with an error. A value computed from other state is a `computed`, not an effect that writes a second signal.

## Avoid State Feedback Loops

Text input, selection, filters and controlled popups commonly have two paths: an external owner updates the value, and user interaction requests a new value. Do not send an owner-supplied value back through the user callback during sync.

Read the owner's current value **untracked** when handling the user's act (`props.value.get_untracked()` in Rust; a TSX event handler is already untracked) and compare it with the next one, so each logical change is reported once. Make callbacks re-entrancy-safe when a callback can synchronously close, replace or update the component that invoked it.

## Stable Identity

A key is part of behavior. It gives a row, a page or a repeated control stable identity, and decides which one keeps its state, its focus and its measurements when the data changes.

- Use stable **domain ids** for rows, tabs, pages and repeated controls: `each(projects, |p| p.id, ..)`, `<Each of={projects()} key={(p) => p.id}>`, a list's `keyExtractor`.
- Namespace test ids with their owning object when the same control repeats (`delete-${project.id}`).
- Never derive identity from a translated label or a mutable list index when items can be inserted or reordered.
- Do not generate a fresh random key or id while rendering.

The same rule applies to navigation routes, list keys, storage keys and test ids. A route that stays in `setRoutes` keeps its page and its state; if two independently retained behaviors share a key, they can overwrite each other's state; if one behavior changes keys every update, it never accumulates state.

## Reading Props Where They Are Used

Reading a prop or a signal in a component body and expecting it to update is a listed failure mode. The component body runs once; the *binding* is what re-runs.

## Performance Rules

- Do not write state unconditionally from a binding or an effect that reads it.
- Avoid creating signals, effects, key bindings and expensive data structures inside bindings or row functions.
- Read signals in bindings, so a coherent change updates the narrowest part of the tree.
- Use `List` for long collections and render only the visible range.
- Avoid cloning large strings or collections solely to satisfy a closure; capture `Copy` handles or shared data (`SharedString`, `Rc`).
- Keep TSX handlers and computed values light; move heavy work off the interaction path or into Rust.
- Measure with `nsh test --trace` before adding caches. A cache must have a clear invalidation owner.
- Keep animation work bounded: animated values on the UI thread rather than signals written every frame, `scrollValue` rather than a scroll listener, and honor reduced motion.

## Related Concepts

- [[Concepts/native-shell-state-ownership|Native Shell State Ownership]] — the narrowest-owner rule that state follows from this model
- [[Concepts/native-shell-architecture|Native Shell Architecture]] — the layer boundaries this model runs inside
- [[Concepts/behavior-presentation-boundary|Behavior Presentation Boundary]] — which layer owns which part of a component
