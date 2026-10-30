---
title: "Native Shell State Ownership"
details: "Every piece of state belongs to the narrowest owner that can keep it correct: domain state to the store, transient view state to the component that renders it, reusable behavioral state to the component designed for it, shared subtree state to a context, and durable state to storage or a server. Controlled values are preferred over callbacks that create a second hidden source of truth."
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
# Native Shell State Ownership

**Source:** [[Raw/nsh-coding-guides]]
**Category:** Architecture Pattern
**Status:** Normative (NSH coding guide)

## The Narrowest Owner

Put each state in the **narrowest owner that can keep it correct**:

| Kind of state | Owner |
|---|---|
| Domain state | The store (`store.ts`) or the app's crate |
| Transient view state | The component that renders it, as a signal |
| Reusable behavioral state | The component designed for it (a `Menu` or `Popover` without `open` keeps its own) |
| State a subtree shares | A signal provided through context |
| What outlives a run | Storage or a server |

## Controlled Values Over Callbacks

Prefer **controlled values** for ordinary selection and toggles: pass the current value into the component, receive a requested change, update the owner, and the bindings follow. A callback reports intent; it should not create a second hidden source of truth.

```rust
switch()
    .checked(show_hidden)
    .on_change(move |next: &bool| show_hidden.set(*next))
    .child(text("Show hidden files"))
```

There is nothing to notify: writing a signal updates exactly the bindings that read it. A Rust component emits a semantic event that its owner should handle with `cx.emit(..)`; an effect follows a signal for as long as its owner lives. Write several fields that form one invariant in one `batch`, so effects and computed values see them at once.

The pattern holds for the app's own controlled components — a quantity stepper written once in Rust and placed from Rust and TSX:

```rust
#[derive(Debug, Clone, PartialEq, Event)]
pub enum QuantityStepperEvent {
    /// The user asked for another quantity; the owner sets `value`.
    Change(u32),
}
```

The owner sets the value; the stepper reports the request. The stepper reads the current value **untracked** when handling the user's act (`props.value.get_untracked()`), so each logical change is reported once and the callback never feeds the owner-supplied value back through itself.

## Text: `SharedString` for Retained UI Text

In Rust, **must prefer `SharedString`** for UI text retained across updates or callback closures, including component labels, titles and placeholders: props take it (`Prop<SharedString>`), and cloning it into a binding does not copy the text.

- For a mutable editing buffer or text being assembled with formatting, use `String` and convert when the result is ready.
- For temporary read-only access during one call, use `&str`.
- In TSX, strings are the app's own values; keep text computed from state in a `computed` or a closure instead of rebuilding it in several places.

For immutable response text that the UI will retain, keep the received value intact and put derived or formatted presentation text in a separate domain value instead of rewriting the response.

## Props Are Decisions, Not Callbacks

**The main thread never waits for app code.** When the system needs an answer on the spot (may this page pop, may this sheet or popover close, may this text change), NSH answers natively from props mounted beforehand, and an event tells the app afterwards.

So a decision the system needs on the spot is a **prop set as soon as it is known**, not a callback that returns true or false: `popOnBack={!dirty()}` with `onBackPress` to confirm, `closeOnEscape` and `closeOnBackdropPress` with `onCancel` to hear the attempt, `maxLength` on an input, `disabled` on a button.

## Async Work and Explicit States

Start asynchronous work from an event, an effect or a `resource`, **not** as an unconditional side effect of a component body. An effect tracks only what it reads synchronously: read the signals first, then start the work.

Represent async operations with explicit states: a resource's `state()` is `unresolved`, `pending`, `ready`, `refreshing` or `errored`. Preserve usable previous data during refresh — a resource keeps its value while it loads again.

```rust
let results = resource(
    move || {
        let q = query.get();
        (!q.is_empty()).then_some(q)
    },
    |q, _info| async move {
        let response = fetch(format!("https://api.example.com/search?q={q}")).await?;
        if !response.ok() {
            return Err(format!("HTTP {}", response.status()));
        }
        Ok(response.text())
    },
);
```

A dropped load is aborted. Results can arrive after the query, the page or the selection has changed: a resource drops superseded loads, and work of your own attaches a revision or an identity and rejects stale results rather than applying them to new state.

Keep recurring work under an owner so its going away cancels it. A one-shot task that must finish independently can be started from the store, but it gives up that cancellation.

## Common Failure Modes in State

- one signal containing the app's unrelated state;
- duplicated local state that drifts from a controlled value;
- effects that copy one signal into another, and writes that loop through a binding;
- per-row state in signals created inside a `List` row;
- business logic and network requests embedded in a long component body.

## Related Concepts

- [[Concepts/native-shell-reactive-rendering|Native Shell Reactive Rendering]] — the runs-once model this ownership rule is built on
- [[Concepts/native-shell-architecture|Native Shell Architecture]] — the layer boundaries the store sits in
- [[Concepts/stable-domain-identity|Stable Domain Identity]] — why keys are domain ids, not indices
