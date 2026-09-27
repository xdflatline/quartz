---
title: "Provider-Native Compaction"
details: "Compaction that delegates summarization to the model provider's own endpoint instead of running a local LLM call — OpenAI Responses compact (V1 /responses/compact, V2 streaming with retained-message budget), Anthropic server-side compaction (compact-2026-01-12 beta), and a custom /chat/completions shim for llama.cpp/vLLM. The provider's output becomes the durable history; local LLM summarization is skipped entirely."
tags:
  - concept
  - context-engineering
  - architecture-pattern
created: 2026-09-27
updated: 2026-09-27
type: concept
sources:
  - .Raw/github-oh-my-pi-compaction-docs-2026-09-27.md
---

# Provider-Native Compaction

**Source:** [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
**Category:** Architecture Pattern
**Status:** Production-validated (multi-provider: OpenAI + Anthropic)

## Overview

When `remote` is the first entry in `compaction.methodOrder`, oh-my-pi delegates compaction to the model provider's own endpoint — OpenAI Responses compact, Anthropic's server-side `compact-2026-01-12` beta, or a custom OpenAI-compatible endpoint (llama.cpp, vLLM). The provider returns a structured replacement-history payload (Codex-style retained tail + compaction item, or Anthropic's `compaction` block) which is stored under `CompactionEntry.preserveData.openaiRemoteCompaction` or `preserveData.anthropicCompaction`. Local LLM summarization is skipped entirely on success.

## Core Content

### Three remote lanes (consulted in order)

1. **V2 streaming Responses compaction** — tried first, on by default via `compaction.remoteStreamingV2Enabled`.
2. **V1 native `/responses/compact`** — fallback for OpenAI/OpenAI Codex models when V2 did not run (ineligible or failed).
3. **Anthropic server-side compaction** (`compact-2026-01-12` beta) — fallback when remote is enabled and no OpenAI lane applies.
4. **Custom remote endpoint** — last fallback if `compaction.remoteEndpoint` is set.

### V2 streaming Responses compaction (default-on)

- Eligibility: `shouldUseCompactionV2Streaming(...)` requires `openai-responses`, `azure-openai-responses`, or `openai-codex-responses` APIs with `remoteCompaction.v2StreamingEnabled` and a resolvable Responses endpoint.
- Forwards the full conversation including provider-native tool-call history replay, with a trailing `compaction_trigger` input item.
- Requires exactly one streamed `compaction` output item.
- Carries session routing and prompt-cache identifiers (routing/session-id headers plus `prompt_cache_key`) and resolves the model's reasoning effort the same way a normal turn does.
- Replacement history is Codex-style: retained real user messages within `compaction.v2RetainedMessageBudget` (default `64000`, clamped to that ceiling) followed by the compaction item.
- Stored in `preserveData.openaiRemoteCompaction` with version `"v2"`.
- Transient stream errors retry up to `V2_COMPACTION_MAX_RETRIES` (2) times with exponential backoff under a 3-minute timeout (`V2_COMPACTION_TIMEOUT_MS`); user aborts are never retried.

### V1 native `/responses/compact`

- Used when V2 is ineligible or failed.
- Preserves provider replacement history in `preserveData.openaiRemoteCompaction` (version "v1").
- A native failure surfaces its transport error instead of silently switching to generic summarization — unless `compaction.remoteEndpoint` is set, in which case it falls through.

### Anthropic server-side compaction

- Eligibility: `compat.supportsServerCompaction` (catalog rule: Opus 4.6+, Sonnet 4.6+, Fable/Mythos 5) **and** `shouldUseAnthropicNativeCompaction` (URL must resolve to the official endpoint — a Foundry or `ANTHROPIC_BASE_URL` reroute is excluded; other Anthropic-compatible routes opt in with `remoteCompaction.enabled`).
- Issues the **live turn's own request** — same system prompt, tools, and message history, so it reads the prompt cache the last turn wrote — plus the `compact_20260112` edit with `pause_after_compaction`, a trigger at the API's 50k floor, and the harness summary prompt as `instructions`.
- The instructions name where the retained tail begins, so the summary covers only the history the rebuilt context drops.
- The API answers with a `compaction` block surfaced as `anthropicCompaction` payload. Its plain-text summary becomes the entry `summary` (plus the file-operation list) **and** `preserveData.anthropicCompaction`.
- Later Anthropic requests on a compaction-capable endpoint replay it as a leading assistant `compaction` block — folded into the retained assistant turn when the tail starts with one — and carry the beta plus a never-firing edit (the API drops everything before the block and requires the strategy to be present).
- Every other provider (and a rerouted Anthropic session) reads the summary text instead.
- A context below `ANTHROPIC_COMPACTION_MIN_CONTEXT_TOKENS` (55k) summarizes locally because the request could not trigger.
- A response without a summary (the API answers the prompt when input never reached the trigger, or returns an empty block when the model called a tool during summarization) is a native failure, like the OpenAI lanes.

### Custom remote endpoint

If `compaction.remoteEndpoint` is set and remote compaction is enabled, local summary generation POSTs one of two wire formats:

- **Custom omp summarizer endpoints**: `{ systemPrompt, prompt }` → JSON `{ summary }`.
- **OpenAI-compatible `/chat/completions` endpoints**: `{ model, messages, stream: false }` with one system prompt and one user prompt. Summary read from `choices[0].message.content` — this lets llama.cpp and vLLM act as remote compactors without a separate summarizer shim.

### Native-replay boundaries

For speculative native compaction, `providerReplayThroughEntryId` records the snapshot's **last entry**, not the later commit position. Context rebuilding and the next compaction preparation both include messages appended between those positions, followed by post-commit messages. The native payload and uncovered interval are replayed once each; `/clear` discards both when it supersedes that compaction.

Native replay also requires a matching provider and a Responses-family API on the active model. A separate native compaction endpoint does not give a Chat Completions or Anthropic encoder the ability to consume its output. Disabling future native compaction does **not** disable normal replay of an existing payload.

### Advisor runtimes

Advisor runtimes retain native `preserveData` for subsequent maintenance and attach its provider payload to the in-memory compaction summary for the next model request. Native replay already contains the retained tail, so advisors do not also append that tail as raw messages. Local summaries still keep recent messages separately. Advisor requests use the shared message converter so both textual compaction summaries and native payloads reach the provider.

## Key Insights

1. **Provider-native beats local LLM summarization on prompt cache.** Anthropic's lane in particular issues the **live turn's own request** — same system prompt, tools, and message history — so it reads the cache the last turn wrote. A local summary path can't read that cache.
2. **Dual-track payloads survive provider switching.** The textual `summary` is always populated (Anthropic's plain-text fallback for non-replaying providers); the structured `preserveData` carries the native payload. One entry works for any provider on the next turn.
3. **Different failure semantics per lane.** V2 retries 2× transient; user aborts never retry. Anthropic treats an empty block or an under-trigger input as a native failure (not silent fallback). A custom endpoint errors fall through to local summarization only if `remoteEndpoint` is set.
4. **Handoff is **not** allowed for overflow recovery.** If the active path is overflow (`reason: "overflow"`, `willRetry: true`), handoff is skipped because its request would reuse the overflowing input. Same input → same overflow.

## Related Concepts

- [[Concepts/snapcompact-bitmap-archival]] — alternative offline archival
- [[Concepts/handoff-document-generation]] — uses a similar live-cache-preserving trick
- [[Concepts/async-speculative-compaction]] — pre-computes native summaries on a side session
- [[Concepts/compaction-trigger-taxonomy]] — which triggers each lane applies to

## References

- Raw Article: [[Raw/github-oh-my-pi-compaction-docs-2026-09-27]]
- Original: https://github.com/can1357/oh-my-pi/blob/main/docs/compaction.md#summary-generation