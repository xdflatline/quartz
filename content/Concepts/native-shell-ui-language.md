---
title: "Native Shell UI Language"
details: "Words are part of the interface architecture. Context economy, one product lexicon, writing each locale rather than translating its shape, concise result-named button labels, sentence case, single-ellipsis convention, and semantic role discipline - Button for application actions, link for external resources only."
tags:
  - concept
  - desktop
  - architecture-pattern
created: 2026-10-30
updated: 2026-10-30
type: concept
sources:
  - Raw/nsh-design-guides.md
  - Raw/nsh-coding-guides.md
---
# Native Shell UI Language

**Source:** [[Raw/nsh-design-guides]], [[Raw/nsh-coding-guides]]
**Category:** Architecture Pattern
**Status:** Normative (NSH design and coding guides)

## Words Are Part of the Interface Architecture

Write the vocabulary for a feature as a system — destinations, objects, commands, states, and outcomes — not as isolated translations of implementation features. Prefer the shortest wording that remains accurate in its actual context.

## Let Context Carry Context

Do not repeat information the surrounding surface already establishes. A sidebar destination is usually the object or domain itself: use `Users`, not `User Management`; `Shortcuts`, not `Shortcut Configuration Management`. A column whose rows already contain actions can omit a generic `Operation` heading. A dialog titled `Delete "Roadmap"?` does not need body text that asks the same question again.

This is context economy, not deletion for its own sake. Add text when it changes the decision: identify the affected scope, an irreversible consequence, an unusual prerequisite, or a way to recover.

Use **nouns** for destinations and objects (`Users`, `Appearance`, `Orders`), **verbs** for commands (`Save`, `Duplicate`, `Export`), and **adjectives or short phrases** for states (`Offline`, `Up to date`, `Pending review`). Avoid wrappers such as `Management`, `Module`, `Page`, `Function`, `Operation`, and `System` unless the word distinguishes a real domain concept.

## Write Each Language, Do Not Translate Its Shape

Start from shared intent, hierarchy, and terminology, then compose each locale as natural interface language. Do not preserve the source language's word order, number of words, politeness filler, or grammatical category.

Remove words supplied by the enclosing information architecture. Inside a `Settings` surface, a destination is often simply `Account`, not `Account Settings` and never the unnatural singular `Account Setting`.

Maintain a small **product lexicon** for recurring objects, commands, and states. Use the same term in the toolbar, menu, context menu, dialog, shortcut search, and documentation unless the context genuinely changes its meaning.

Translation keys describe stable intent (`dialog.deleteProject.title`), not a source-language sentence or a screen coordinate. Never assemble a sentence from translated fragments. **Localize intent, not syntax**: give every locale control over word order, pluralization, punctuation, and the amount of context it needs.

In documentation, use the exact English name for a named API, component, source file, or guide in link text. Keep API identifiers in their original form and format them as code.

## Buttons and Confirmation Dialogs

Button labels are short by default — usually one or two words — and describe **the result, not the gesture or the component**. Prefer `Save`, `Move`, or `Delete` to `Click to save`, `Perform move`, or `Confirm deletion`. Use `Cancel` consistently for the action that leaves without committing. Reserve `OK` for acknowledging purely informational content.

Short is a default, not a character limit. A deliberately longer label is better when its words expose a consequence or distinguish choices users could otherwise confuse.

| Context | Weak | Prefer |
|---|---|---|
| Delete dialog | `Yes`, `Sure`, `Confirm deletion` | `Delete` |
| Unsaved changes | `Confirm`, `Yes` | `Discard changes` |
| Pure acknowledgement | `Confirm operation` | `OK` or `Done` |
| Complex consent whose result has no clear verb | `Yes` | `Confirm` |

A confirmation dialog forms one compact decision: title (the decision or condition), body (only new scope, consequence, or recovery information), actions (`Cancel` and the result), and destructive styling applied to the destructive result rather than substituted for precise wording.

Avoid generic titles such as `Notice`, `Warning`, `Error`, and `Confirmation` when the actual condition can be named. Avoid ritual phrases such as "Are you sure you want to…" and "successfully" when the structure or state already communicates them.

## Capitalization, Punctuation, and Symbols

Use **sentence case** for English UI by default: `Reset layout`, not `Reset Layout` or `RESET LAYOUT`. Preserve proper nouns and established acronyms.

ALL CAPS can provide restrained typographic emphasis for very short section labels, eyebrows, statuses, established acronyms, and code-like identifiers. It does not belong on buttons, long headings, sentences, or dense lists. Do not combine uppercase, strong color, and bold weight in the same region.

Labels, buttons, menu items, tabs, headings, placeholders, and short states do not take a final period. Complete explanatory, warning, and error sentences do.

Use the **single ellipsis character** (`…`), not three periods. Append it to every button or menu item that opens a dialog, sheet, or separate window, and to a command that requires more input or choices before it can complete, such as `Settings…` or `Export…`. An immediately executed command does not take an ellipsis.

Errors should say what happened and, when useful, the next recovery action. Prefer `Couldn't save. Check your connection and try again.` to a technical code or a long apology.

## Button Means Application Action; Link Means External Resource

Use a `Button` when activation changes application state, confirms a decision, opens a tool, submits data, or runs a command. Use an **underlined link** (`role="link"`) only for an external resource target: a URL, web page, online documentation, or email address.

Do not use link styling to make a functional command look quiet. A link-shaped Delete, Save, Refresh, Add, Open-menu, or in-app navigation action hides the control's affordance and exposes the wrong accessibility role. "View" does not make an in-app destination a link — a full report, analysis, details panel, or local record still opens through a button, row, card, tab, or disclosure control.

All internal navigation — sidebar rows, tabs, breadcrumbs, list items, opening a local view, or switching workspaces — must use the navigation stack, a `Button`, or the corresponding component.

## Vocabulary Is Part of the API

The same word means the same concept across components. Before naming a prop or an event, look for the term in NSH's own API, then in GPUI Kit's `gpui-base`, GPUI and `gpui-component`, then in the platforms' controls.

Precise domain words matter:

- **selected** is membership or the current item; **checked** and **pressed** are the value of a checkbox or a toggle; **focused** is the keyboard's target; **hovered** is the pointer's presence.
- **open / close** is an overlay's state; **show / hide** a transient request; **expand / collapse** structure.
- **disabled** blocks interaction; **readonly** allows selecting and navigating but not editing; **loading** prevents duplicate work while an operation runs.
- **press** is activation by any input (`onPress`); **click** is a mouse's.
- **index** is a position; **id** is identity. Do not persist or key reorderable data by index.
- **value** is controlled domain data; **state** is retained behavior.
- **src** is the resource an element shows; any other address is a **url**.
- **role** says what a choice means (`"cancel"`, `"destructive"`); a look is the app's.

Avoid vague names such as `data`, `item2`, `handleAction`, `updateUi`, `process`, `manager` or `config` when a narrower domain term exists.

## Related Concepts

- [[Concepts/native-shell-design-system|Native Shell Design System]] — the visual language these words serve
- [[Concepts/native-shell-api-widening|Native Shell API Widening]] — why vocabulary discipline is part of a public API contract
