---
title: LLM Dataset Creation

details: Processing raw data for training and fine-tuning LLMs.
tags:
  - concepts
created: 2026-06-17
updated: 2026-06-17
type: concept
---
# LLM Dataset Creation

Dataset creation is the process of converting raw unstructured or semi-structured data into formats suitable for Language Model training.

## Ingestion & Parsing
For domain-specific tasks, such as creating a Rust coding agent from EPUB books, the initial step involves:
1. **Extraction**: Converting EPUB chapters into raw Markdown files.
2. **Chunking**: Splitting Markdown into logical units (e.g., by headers or code blocks) that fit within the model's context window.

## Formats

### 1. Continued Pretraining
Used for teaching a model a new language or syntax (e.g., Rust syntax, idioms). Data is usually raw text chunks separated by `<|endoftext|>` tokens.
[Unsloth Continued Pretraining](https://unsloth.ai/docs/basics/continued-pretraining)

### 2. Supervised Fine-Tuning (SFT)
Requires pairs of Instructions and Responses.
```json
{"instruction": "Write a Rust function to reverse a string.", "output": "fn reverse_string(s: &str) -> String { s.chars().rev().collect() }"}
```

### Unsloth Data Recipe
Tools like [Unsloth Studio Data Recipe](https://unsloth.ai/docs/new/studio/data-recipe) allow visual or YAML-based mapping of raw data to specific ChatML or Alpaca formats, simplifying formatting issues and ensuring tokenizer compatibility.
