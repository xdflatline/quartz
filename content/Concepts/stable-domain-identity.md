---
title: "Stable Domain Identity"
details: "A key is part of behavior, not a rendering detail. Stable domain ids decide which row, page or repeated control keeps its state, focus and measurements when data changes. Random or index-based keys destroy retained state; translated labels cannot identify a reorderable item."
tags:
  - concept
  - desktop
  - software-engineering
  - architecture-pattern
created: 2026-10-30
updated: 2026-10-30
type: concept
sources:
  - Raw/nsh-coding-guides.md
---
# Stable Domain Identity

**Source:** [[Raw/nsh-coding-guides]]
**Category:** Architecture Pattern
**Status:** Normative (NSH coding guide)

## A Key Is Part of Behavior

A key gives a row, a page or a repeated control **stable identity**, and decides which one keeps its state, its focus and its measurements when the data changes. In NSH's retained-state model, this is not a rendering optimization — it is the mechanism by which memory survives a reorder.

- Use **stable domain ids** for rows, tabs, pages and repeated controls: `each(projects, |p| p.id, ..)`, `<Each of={projects()} key={(p) => p.id}>`, a list's `keyExtractor`.
- **Namespace test ids** with their owning object when the same control repeats (`delete-${project.id}`).
- **Never** derive identity from a translated label or a mutable list index when items can be inserted or reordered.
- **Do not** generate a fresh random key or id while rendering.

```rust
each(projects, |p| p.id, move |project, _index| {
    let id = project.get_untracked().id;
    button()
        .on_press(move || delete(id))
        .child(text("Delete").test_id(&format!("delete-{id}")))
})
```

```tsx
<Each of={projects()} key={(p) => p.id}>
  {(project) => (
    <Button onPress={() => remove(project().id)}>
      <Text testID={`delete-${project().id}`}>Delete</Text>
    </Button>
  )}
</Each>
```

**A changed key means a changed UI identity.** Treat that reset as deliberate.

## The Rule Extends Everywhere

The same rule applies to navigation routes, list keys, storage keys and test ids:

- A route that stays in `setRoutes` keeps its page and its state.
- If two independently retained behaviors share a key, they can overwrite each other's state.
- If one behavior changes keys every update, it never accumulates state.

This is the structural reason NSH distinguishes **index** (a position) from **id** (an identity), and warns against persisting or keying reorderable data by index.

## Why Virtualization Makes It Load-Bearing

In a `List` / `virtual_list`, a row function runs once per cell and **cells are reused for other rows**. Two consequences make identity load-bearing rather than cosmetic:

- per-item state must live in **data keyed by id**, not in a signal created inside the row — a signal created in the row travels with the cell to the next item;
- the item must be **read where it is used**, in bindings — a value copied at the top of the row function belongs to the first row the cell showed.

Virtualization is a behavioral contract, not just a performance switch.

## Related Concepts

- [[Concepts/native-shell-state-ownership|Native Shell State Ownership]] — where per-item state must live
- [[Concepts/native-shell-reactive-rendering|Native Shell Reactive Rendering]] — the runs-once model identity protects
- [[Concepts/native-shell-ui-language|Native Shell UI Language]] — why translated labels cannot be identifiers
