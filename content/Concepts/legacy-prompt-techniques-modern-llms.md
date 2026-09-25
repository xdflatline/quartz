---
title: "Legacy Prompt Techniques and Modern LLMs"
details: "Two prompt-engineering techniques popular with earlier LLMs that are now less necessary with Claude 4.x+: XML tags for structure (modern models parse prose structure well) and heavy role prompting ('you are a world-renowned expert...'). Modern alternatives exist for both. Knowing what to STOP doing is as important as knowing what to start."
tags:
  - concept
  - prompt-engineering
  - llm
source: "[[Raw/claude-best-practices-prompt-engineering-2025-11-10]]"
created: "2026-09-25"
updated: "2026-09-25"
type: concept
---

# Legacy Prompt Techniques and Modern LLMs

**Source:** [[Raw/claude-best-practices-prompt-engineering-2025-11-10]] — Anthropic Claude blog (Nov 10, 2025)
**Category:** Learning Mechanism
**Status:** Production-validated (Anthropic "techniques you might have heard about" section)

---

## Overview

Two techniques that were popular with earlier LLMs and are now **less necessary with models like Claude 4.x+**: XML tags for structure, and heavy role prompting. Modern models handle both scenarios without explicit scaffolding, and the scaffolding can actively hurt in some cases.

Knowing what to **stop doing** is as important as knowing what to start. Modern prompt engineering is partly subtraction — removing the boilerplate that earlier-generation models needed.

## XML tags for structure

XML tags were once a recommended way to add structure and clarity to prompts, especially when incorporating large amounts of data.

```
<athlete_information>
- Height: 6'2"
- Weight: 180 lbs
- Goal: Build muscle
- Dietary restrictions: Vegetarian
</athlete_information>

Generate a meal plan based on the athlete information above.
```

### When XML tags might still be helpful

- You're working with extremely complex prompts mixing multiple types of content
- You need to be absolutely certain about content boundaries
- You're working with older model versions

### Modern alternative

For most use cases, **clear headings, whitespace, and explicit language** ("Using the athlete information below...") work just as well with less overhead. Modern models parse prose structure well; the XML scaffolding is redundant.

### When XML tags actually help

Despite the "less necessary" framing, there are cases where structured delimiters are useful:

- **Programmatic injection of variable data** — when you template-insert sections, XML tags make the boundary explicit on both ends
- **Distinguishing multiple injected blocks** of the same type — `<source_1>...</source_1>` vs `<source_2>...</source_2>` is clearer than prose headers
- **Parsing output back** — when downstream code needs to extract structured sections from the model's response

These are not "the model needs help parsing it" cases; they're "humans and downstream code need help tracking it" cases.

## Heavy role prompting

Role prompting defines expert personas in how you phrase your query.

**Example**: "You are a financial advisor. Analyze this investment portfolio..."

### The over-constraint problem

> "You are a helpful assistant" is often better than "You are a world-renowned expert who only speaks in technical jargon and never makes mistakes."

Overly specific roles can limit the AI's helpfulness. The model may follow the role literally and refuse to give the kind of answer the user actually needs ("I'm a world-renowned expert, so I only discuss this at a PhD level...").

### When role prompting might help

- You need consistent tone across many outputs (a chatbot persona)
- You're building an application that requires a specific persona (a pirate-themed game character)
- You want domain expertise framing for complex topics

### Modern alternative

Often, **being explicit about what perspective you want** is more effective than assigning a role:

> "Analyze this investment portfolio, focusing on risk tolerance and long-term growth potential"

Rather than:

> "You are a financial advisor. Analyze this investment portfolio."

The first version names the perspective (risk tolerance, long-term growth) directly. The second version hopes the role ("financial advisor") implies the right perspective.

## Connection to other principles

Both legacy techniques are forms of *implicit* instruction — XML tags implicitly say "this is structured data," role prompting implicitly says "act like X." Modern models respond better to [[Concepts/explicit-instruction-over-implicit-inference|explicit instruction]] ("use the athlete information below to generate a meal plan") than to implicit scaffolding that the model has to interpret.

## Anti-patterns to avoid

- Wrapping every block of injected data in `<xml_tag>` for no reason
- "You are a world-renowned expert with 30 years of experience who..."
- Role + instruction redundancy ("As a senior Python developer, write a Python function that...")
- "You MUST" without context — the word "MUST" by itself is just emphasis; needs the explicit reason to be useful

## When to keep the legacy approach

- **You're integrating with a system that requires it.** Some pipelines template in XML tags; matching the format is correct.
- **You're targeting multiple model versions.** If your prompt is consumed by both Claude 4.x and an older model, the XML scaffolding may still help the older one without hurting the newer one significantly.
- **You genuinely want the persona behavior.** A pirate chatbot needs the pirate persona; that's the point.

## Key insights

1. **Modern Claude is robust to natural prose structure.** Don't add scaffolding the model doesn't need.
2. **The role-prompting over-constraint is a real failure mode.** Over-specified roles can make the model LESS helpful, not more.
3. **Subtraction is part of prompt engineering.** A cleaned-up prompt without legacy scaffolding is often better than the original.

## Related Concepts

- [[Concepts/explicit-instruction-over-implicit-inference]] — the principle that explains why these legacy techniques are less necessary
- [[Concepts/specificity-in-prompt-engineering]] — what to do instead when you need to be specific

## References

- Raw article: [[Raw/claude-best-practices-prompt-engineering-2025-11-10]]
- Original: <https://claude.com/blog/best-practices-for-prompt-engineering>