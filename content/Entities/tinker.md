---
title: "Tinker"
details: "Thinking Machines Lab's platform for hosted inference, fine-tuning and a model playground, used to serve and customize the Inkling model family. Positioned alongside open-source runtimes rather than replacing them: the same open weights run on Tinker or locally via Ollama, SGLang, vLLM and GGUF builds."
tags:
  - entity
  - inference
  - tooling
  - fine-tuning
created: 2026-11-22
updated: 2026-11-22
type: entity
sources:
  - "Raw/inkling-2-mini-thinking-machines-2026-11-20"
---

# Tinker

**Category:** Hosted inference / fine-tuning platform
**Vendor:** [[Entities/thinking-machines-lab]]
**Status:** Active (2026)

## Overview

Tinker is Thinking Machines Lab's hosted platform for running and customizing its models. For [[Entities/inkling-2-mini|Inkling 2 Mini]] it provides:

- **Inference** — API access to the released model.
- **Fine-tuning** — customization and RL fine-tuning support.
- **Playground** — chat with the model and try it before integrating.

## Relationship to local deployment

Tinker is the managed path; the open weights are the escape hatch. The same model is published for local and open-source runtimes — Ollama on Mac, GGUF via Unsloth/llama.cpp, SGLang, vLLM, NVIDIA Dynamo, TokenSpeed and Llama App — plus RL fine-tuning support on SkyRL, Miles and NVIDIA AutoModel.

This dual distribution is notable for open-weights releases: the hosted platform competes on convenience and customization, not on exclusive access.

## Related

- [[Entities/thinking-machines-lab]] — parent lab
- [[Entities/inkling-2-mini]] — the model served
- [[Entities/huggingface-inference-endpoints]] — an alternative hosted-inference surface

## References

- Raw: [[Raw/inkling-2-mini-thinking-machines-2026-11-20]]
- Playground: https://tinker.thinkingmachines.ai/playground
