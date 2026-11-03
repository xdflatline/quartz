---
title: "Auto Ontology (NVIDIA)"
details: "NVIDIA's Apache-2.0 Python framework for building a semantic, graph-based reasoning layer over enterprise data and exposing it to agent harnesses through MCP, CLI, and API. Ships a Next.js/FastAPI/Postgres-pgvector stack, a nine-tool read-only MCP server, three agent skills (setup, management, query), and NIM-based text-to-SQL. Public repository with roughly 1.1k stars as of November 2026; external contributions are closed."
tags:
  - entity
  - llm
  - agent
  - mcp
  - schema
  - tooling
created: 2026-11-03
updated: 2026-11-03
type: entity
sources:
  - "Raw/nvidia-auto-ontology-2026-11-03.md"
---

# Auto Ontology (NVIDIA)

**Source:** [[Raw/nvidia-auto-ontology-2026-11-03]]
**Category:** Open-source framework / semantic layer
**Repository:** https://github.com/NVIDIA/auto-ontology
**License:** Apache-2.0

---

## Overview

Auto Ontology is a Python framework that builds a semantic, graph-based reasoning layer over enterprise data and serves it to agents. Its pitch is reliability rather than capability: agents can already retrieve and query, but a fast wrong number is worse than a slow right one, so the framework concentrates on telling an agent what data means, whether it may be used, how it is derived, and where it came from.

Functionally it does five things: **discover** an ontology from existing metadata (or connect an existing ontology or semantic model), **ground** business meaning for metrics and entities, **validate** generated queries against certified definitions and lineage, **expose** the layer over MCP, CLI, and API, and **learn** by folding certified corrections back into the ontology.

## Technical Shape

| Component | Technology | Role |
|---|---|---|
| Frontend | Next.js 16 (React 19, TypeScript, Tailwind 4), Better Auth, Prisma | Web UI, authentication, API gateway |
| Backend | FastAPI (Python 3.12+), LangChain | Chat / NL-to-SQL, catalog, datasource APIs |
| Ingestion worker | FastAPI (Python 3.12+) | Ingests tabular data, writes embeddings |
| Postgres + pgvector | Relational DB | App metadata, catalog/ontology, vector store |
| HashiCorp Vault | Optional | Connection credential storage |

Inference runs on NVIDIA NIM (hosted API catalog or self-hosted), configured as model *triplets* — `<PREFIX>_ENDPOINT` / `_API_KEY` / `_MODEL` for `DEFAULT_MODELS`, `REASONING`, `NON_REASONING`, `EMBED`, and `RERANK`. Defaults in the repository point at Nemotron models (`nvidia/nemotron-3-nano-30b-a3b` for chat, `nvidia/nemotron-3-embed-1b` for embeddings, `nvidia/llama-nemotron-rerank-vl-1b-v2` for reranking).

Deployment is Helm on Kubernetes (the official path) or Docker Compose for a single machine. Source connectors named in the docs are Databricks, Postgres, Snowflake, and DuckDB.

## Agent Surfaces

- **MCP server** (`mcp/`) — an HTTP client of the public API that holds no credentials. Nine read tools: `ask_question`, `check_answerable`, `check_readiness`, `search_terms`, `get_term`, `get_term_columns`, `get_term_sql_attributes`, `get_sql_attribute`, `describe_table`. No schema-browsing tool, by design. OAuth sign-in is handled by the product; the server itself has no token.
- **REST** — authenticated Next.js gateway (`POST /api/chat/completions`, SSE with `step`/`result`/`error` events then `[DONE]`). FastAPI on `:3001` is a trusted internal boundary and must not be exposed, because it trusts the `x-auto-ontology-user-id` header.
- **API tokens** — `x-api-key`, stored as SHA-256 hashes, acting as their owner's permissions; tokens cannot mint tokens.
- **Agent skills** — three shipped under `skills/`: `nvidia-ontology-setup`, `nvidia-ontology-management`, `nvidia-ontology-query`. They are mirrored to `nvidia/skills` and build.nvidia.com/skills, with CI-generated benchmark and signature files.

## Status and Provenance

- Public repository, created 2026-04-27, ~1,352 commits and roughly 1,140 stars as of 2026-11-03. Languages: Python 63.9%, TypeScript 19.8%, PL/pgSQL 15.5%.
- Twelve listed contributors, several with `-nv` handles; `claude` appears in the contributor list.
- **External contributions are closed** — issues and pull requests from outside the maintainer team are explicitly not reviewed.
- The architecture diagram in `docs/assets/arch.png` is titled "NVIDIA AI-Q Agent Harness Architecture", and the skills reference AI-Q, Nemotron, and cuOpt; AI-Q appears to be the agent-harness context the framework was built for.
- A text-to-SQL benchmark harness (BIRD) lives in a separate repository, `NVIDIA/ontology-sql-eval`. **No benchmark results are published in the main repository**, so comparative accuracy claims are unverified here.
- Documentation inconsistency worth noting: `README.md` describes Auto Ontology as "an open library" under Apache-2.0, while `docs/mcp.md` states "Auto Ontology is NVIDIA-internal today, so this install needs GitHub credentials with access to the repository". The public repository and its license suggest the latter sentence is stale; the `uvx` install instructions still carry the caveat.

## Related Pages

- [[Concepts/semantic-layer-agent-grounding]]
- [[Concepts/answer-readiness-vs-answerability]]
- [[Concepts/grounded-answer-validation]]
- [[Concepts/semantic-contract-for-measures]]
- [[Concepts/agent-tool-surface-curation]]
- [[Research/nvidia-auto-ontology-semantic-grounding]]
- [[Entities/nvidia]]
- [[Raw/nvidia-auto-ontology-2026-11-03]]

## References

- Repository: https://github.com/NVIDIA/auto-ontology
- Benchmark harness: https://github.com/NVIDIA/ontology-sql-eval
