---
title: "NVIDIA Auto Ontology — repository README and agent documentation"
details: "Verbatim capture of the NVIDIA Auto Ontology repository documentation: the project README, the MCP server guide, the three shipped agent skills (setup, management, query), and the AGENTS.md entry point. Covers the semantic-layer architecture, readiness and answerability checks, source-grounded modeling contracts, and answer-validation workflow."
tags:
  - raw
  - llm
  - agent
  - mcp
  - schema
  - knowledge-management
  - github-readme
created: 2026-11-03
updated: 2026-11-03
type: raw
source: "https://github.com/NVIDIA/auto-ontology"
author: "NVIDIA"
published: 2026-11-03
---

# NVIDIA Auto Ontology — repository documentation

**Source:** [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) (Apache-2.0)
**Date Retrieved:** 2026-11-03
**Type:** GitHub repository documentation bundle
**Scope:** README, `docs/mcp.md`, the three `skills/nvidia-ontology-*` skills, and `AGENTS.md`. SPDX comment headers stripped; heading levels demoted one step inside each embedded document. Nothing else edited.

---

## Source: README.md (repository root)

## Auto Ontology

Agents can retrieve documents and query databases, but reliability gates agentic analytics: a revenue metric answered faster is worth nothing if the number is wrong. Agents need a context layer that tells them where data lives, what it means, whether to use it, how to use it, where it came from, and what is similar. NVIDIA Auto Ontology is an open library that builds that layer from enterprise metadata, reconciles definitions across systems, and exposes it to any agent harness through MCP, CLI, and API. It complements the semantic models customers already own.

It enables developers to:

- Discover: generate enterprise ontologies from metadata; connect existing ontologies and semantic models; build AI-ready knowledge graphs.
- Ground: give agents trusted business meaning for metrics, entities, and relationships; reconcile inconsistent definitions across systems.
- Validate: check generated queries against certified definitions and lineage; return provenance with every answer.
- Expose: serve context to any agent harness through MCP, CLI, and API.
Learn: fold certified corrections and usage back into the ontology, so shared context improves with every question.

### Benchmarks

To run a text-to-SQL benchmark such as BIRD, refer to the
[ontology SQL evaluation repository](https://github.com/NVIDIA/ontology-sql-eval/).

> **Licensing & contributions.** Auto Ontology is distributed under the
> [Apache License 2.0](./LICENSE). Third-party open-source components
> bundled, linked, or otherwise used by this project are listed in
> [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md). **This project
> is currently not accepting external contributions.**

<p>
<img src="./docs/assets/arch.png" alt="Auto Ontology Architecture" width="800">
</p>

### Key Features

- **Natural-language querying** of structured data — questions are translated to
  SQL and executed against connected databases, powered by NVIDIA NIM.
- **Semantic catalog / ontology layer** over relational sources, stored in
  Postgres alongside the catalog it describes.
- **Authentication & RBAC** —using [Better Auth](https://github.com/better-auth/better-auth).
- **Web UI** for chat, analysis, data catalog, analytics, and settings.
- **Flexible deployment** — Helm chart for Kubernetes or Docker Compose for a
  local stack.

### Software Components

| Component           | Technology                                                             | Role                                       | Default port |
| ------------------- | ---------------------------------------------------------------------- | ------------------------------------------ | ------------ |
| Frontend            | Next.js 16 (React 19, TypeScript, Tailwind CSS 4), Better Auth, Prisma | Web UI, authentication, API gateway        | 3000         |
| Backend             | FastAPI (Python 3.12+), LangChain                                      | Chat / NL-to-SQL, catalog, datasource APIs | 3001         |
| Ingestion worker    | FastAPI (Python 3.12+)                                                 | Ingests tabular data and writes embeddings | 3002         |
| Postgres + pgvector | Relational Database                                                    | App metadata, the catalog and ontology, vector store | 5432 |
| HashiCorp Vault     | Optional                                                               | Secure storage of connection credentials   | —            |

#### NVIDIA NIM

Auto Ontology uses NVIDIA NIM endpoints for inference — either the hosted
[NVIDIA API catalog](https://build.nvidia.com) (`integrate.api.nvidia.com`) or
self-hosted NIMs. The defaults in `.env.example` are:

- **LLM:** `nvidia/nemotron-3-nano-30b-a3b`
- **Embeddings:** `nvidia/nemotron-3-embed-1b`
- **Reranking:** `nvidia/llama-nemotron-rerank-vl-1b-v2`

The endpoints and models are configured via the `DEFAULT_MODELS_ENDPOINT`, `DEFAULT_MODELS_MODEL`,
`EMBED_ENDPOINT`, and `EMBED_MODEL` environment variables and require a
`DEFAULT_MODELS_API_KEY`.

##### Model triplets

Each model role is configured by a **triplet** of environment variables —
`<PREFIX>_ENDPOINT` (URL), `<PREFIX>_API_KEY`, and `<PREFIX>_MODEL`:

| Prefix           | Role                                                        |
| ---------------- | ----------------------------------------------------------- |
| `DEFAULT_MODELS` | Shared default; every field below falls back to it.         |
| `REASONING`      | Main chat / NL-to-SQL model.                                |
| `NON_REASONING`  | Lighter model used for entity extraction.                   |
| `EMBED`          | Text-embedding model (must match between ingest and query). |
| `RERANK`         | Reranker used by the retrieval flow.                        |

You can set a full triplet, only some of its fields, or none at all — any field
left unset falls back to the matching `DEFAULT_MODELS_<FIELD>`. So the simplest
setup is to fill in `DEFAULT_MODELS_*` and override per-triplet fields only where
they differ (e.g. `EMBED_MODEL`, `NON_REASONING_MODEL`). `*_API_KEY` also falls
back to the legacy `NVIDIA_API_KEY` for backward compatibility.

### Deployment

#### Prerequisites

- **Docker** with **Docker Compose v2** (e.g. Docker Desktop on macOS/Windows,
  Docker Engine on Linux) for the local stack. For Kubernetes deployments see
  [`DEPLOYMENT.md`](./DEPLOYMENT.md).
- An **NVIDIA API key** (`nvapi-...`) for NVIDIA NIM (chat and ingestion) from
  the NVIDIA API catalog at <https://build.nvidia.com>.
- Connection details for the source database(s) you want to query
  (Databricks, Postgres, Snowflake, or DuckDB).

#### Installation

**Kubernetes**

To deploy Auto Ontology on a Kubernetes cluster, see [`DEPLOYMENT.md`](./DEPLOYMENT.md).

**Local (Docker Compose)**

1. Clone the repository:

   ```bash
   git clone <repo-url> auto_ontology && cd auto_ontology
   ```

2. Create your environment file (.env) from the template and fill in the values
   (Postgres credentials, `DEFAULT_MODELS_API_KEY`, `CONNECTION_STRINGS`, etc.).
   See [`.env.example`](./.env.example) for the full list of variables:

   ```bash
   cp .env.example .env
   # edit .env
   ```

   Note:
   - `AUTH_SECRET` and `APP_URL` are **required** — without them every page
     fails with a Better Auth "default secret" error.
   - `POSTGRES_PORT` only changes the **host-side** port mapping (set it if
     5432 is already taken on your machine); containers always reach Postgres
     on the internal network port.

3. Build the images and start the stack:

   ```bash
   docker compose up -d --build
   ```

   This builds the backend (`auto_ontology`) and frontend (`auto-ontology-frontend`) images, brings
   up Postgres and pgAdmin, runs the one-shot `frontend-migrate` job to
   sync the database schema, and starts the app (backend, ingestion service,
   and frontend).

4. Open the UI at <http://localhost:3000> (the backend API is on `:3001`,
   pgAdmin on `:5050`).

   > **Troubleshooting:** if the UI loads without the left navigation panel
   > (or otherwise looks broken after a restart), your browser is holding a
   > stale session cookie — this happens when `AUTH_SECRET` changes or the
   > database is reset. Clear the site data for `localhost:3000` (or delete
   > the `better-auth.session_token` cookie) and sign in again.

### Connections Management

Auto Ontology resolves the source databases it connects to from two sources:

1. **Added through the UI** — connections created from within the app. With this
   option the connection credentials are **stored in plaintext in Postgres unless
   Vault is configured**:
   - **Without Vault:** the full connection object (including the password) is
     JSON-serialized and stored, unencrypted, on the catalog's database row.
   - **With Vault:** the credentials are written to Vault, keyed by the database
     name, and the catalog row stores no credentials (the database name is the
     lookup key — there is no separate reference field).

   Vault is enabled only when all of `VAULT_ADDR`, `VAULT_NAMESPACE`,
   `VAULT_ROLE_ID`, and `VAULT_SECRET_ID` are set (`VAULT_AUTH_MOUNT` and
   `VAULT_KV_MOUNT` are optional overrides). It is off by default; a partial
   configuration is ignored with a warning and falls back to plaintext storage.

2. **`CONNECTION_STRINGS` environment variable** — a comma-separated list of
   connection strings supplied at deploy time (e.g. the Helm
   `--set connectionStrings=<CONNECTION-STRINGS>` flag). This is a fallback: it
   is used only when there are no UI-added connections.

### Authentication

Auto Ontology Supports SSO for authentication.
The Redirect URI should be configured in the IdP as: APP_URL/api/auth/sso/callback

#### API tokens (scripting)

A browser signs in and gets a session cookie, which a script cannot obtain. For
scripts, notebooks, and scheduled jobs, mint an **API token** instead:

1. Open the user menu (top right) → **API Tokens** → **New token**.
2. Name it, optionally pick an expiry (default: never), and **copy the token**.
   Auto Ontology stores only a SHA-256 hash of it, so it is shown exactly once. Losing it
   means minting a new one.

Send it as `x-api-key` on any `/api/...` call — `Authorization: Bearer <token>`
works too:

```sh
curl -H "x-api-key: $AUTO_ONTOLOGY_API_TOKEN" https://auto_ontology.example.com/api/terms
```

```python
import os
import requests

session = requests.Session()
session.headers["x-api-key"] = os.environ["AUTO_ONTOLOGY_API_TOKEN"]

terms = session.get("https://auto_ontology.example.com/api/terms").json()

answer = session.post(
    "https://auto_ontology.example.com/api/chat/completions",
    json={"question": "How many orders shipped last week?"},
).json()
```

Things worth knowing:

- **A token acts as its owner.** It carries no permissions of its own — every
  call is authorized against the owner's role, exactly as it would be in the
  browser. A viewer's token cannot do admin things.
- **The whole API surface accepts it.** Authentication is resolved in one place
  (`frontend/auth/resolve-user.ts`) for every route, so any endpoint in
  [`docs/openapi/auto-ontology-api.json`](./docs/openapi/auto-ontology-api.json) that is not
  `withPublic` works with a token.
- **Revocation is immediate.** Delete the token in the UI, or delete/ban the
  owning user, and the next request with it gets a 401.
- **Tokens cannot manage tokens.** Creating and revoking requires a signed-in
  session, so a leaked token cannot issue itself successors.
  
### Agent API conversations

Public clients call the authenticated Next.js gateway at
`POST /api/chat/completions`. The response is an SSE stream containing `step`,
`result`, or `error` events, followed by `[DONE]`.

`conversation_id` is optional:

- Omit it for a stateless, one-shot request.
- Supply a client-generated UUID to create or continue a conversation.
- Reuse the same UUID for every turn in the thread. Wait for `[DONE]` before
  sending the next turn; overlapping requests for one conversation return
  `409 Conversation in progress`.

```json
{
  "question": "What about last month?",
  "conversation_id": "d61d8aa3-d496-4fa7-97ce-4f831c162e7f"
}
```

For conversational requests, FastAPI loads up to the five most recent completed
turns (bounded to 12,000 characters) and rewrites contextual input such as
“What about August?” into a standalone question before running the existing
text-to-SQL graph. Independent questions are passed through unchanged. Internal
agent thoughts, chart payloads, errors, and raw SQL result sets are not reused as
context.

Conversation history is scoped to the authenticated Auto Ontology user. Browser and
service callers should use the Next.js gateway, which resolves the user and
forwards the internal `x-auto-ontology-user-id` header to FastAPI. The FastAPI port is a
trusted internal service boundary: it must not be exposed publicly because that
header is not independently verified by FastAPI. A direct FastAPI request
without `conversation_id` remains stateless; a direct request with
`conversation_id` requires the trusted identity header.

The web UI manages the UUID automatically. An API-created conversation can be
opened in the UI at `/chat?focus=<conversation_id>` when it belongs to the
signed-in user.

### Agent skills

Coding agents: start at [`AGENTS.md`](./AGENTS.md). Skills live in
[`skills/`](./skills/) (`nvidia-ontology-setup`, `nvidia-ontology-management`, `nvidia-ontology-query`).
Maintainers keep using [`CLAUDE.md`](./CLAUDE.md).

### MCP server

Agent harnesses such as Cursor and Claude Desktop can query your data through
Auto Ontology's [MCP](https://modelcontextprotocol.io) server. See
[`mcp/`](./mcp/) to run it and [`docs/mcp.md`](./docs/mcp.md) for the details.

### License

Auto Ontology is licensed under the [Apache License, Version 2.0](./LICENSE).
SPDX identifier: `Apache-2.0`.

Each NVIDIA-authored source file in this repository carries an SPDX header
of the form:

```text
SPDX-FileCopyrightText: Copyright (c) 2024-2026, NVIDIA CORPORATION & AFFILIATES.
All rights reserved.
SPDX-License-Identifier: Apache-2.0
```

Third-party open-source components used by Auto Ontology are enumerated, with their
upstream licenses and project URLs, in
[`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md). Components added by the
container images are listed separately in
[`CONTAINER_THIRD_PARTY_NOTICES.md`](./CONTAINER_THIRD_PARTY_NOTICES.md).

### Notice and Disclaimer

NOTICE AND DISCLAIMER: This software automatically retrieves, accesses or
interacts with external materials. Those retrieved materials are not
distributed with this software and are governed solely by separate terms,
conditions and licenses. You are solely responsible for finding, reviewing and
complying with all applicable terms, conditions, and licenses, and for
verifying the security, integrity and suitability of any retrieved materials
for your specific use case. This software is provided "AS IS", without warranty
of any kind. The author makes no representations or warranties regarding any
retrieved materials, and assumes no liability for any losses, damages,
liabilities or legal consequences from your use or inability to use this
software or any retrieved materials. Use this software and the retrieved
materials at your own risk.

External materials Auto Ontology interacts with at run time:

| Material | When | Terms |
| --- | --- | --- |
| NVIDIA-hosted model APIs ([build.nvidia.com](https://build.nvidia.com), `integrate.api.nvidia.com`) for LLM, embedding, and reranking | Chat, ingestion, and semantic compilation, with the default model configuration | Terms of the NVIDIA API catalog and of each model |
| Any other OpenAI-compatible model endpoint you configure (`*_ENDPOINT` / `*_MODEL`) | Same | Terms of that provider and model |
| KumoRFM predictive-query service | Only when `KUMO_RFM_API_KEY` is set | Kumo's terms |
| Your source databases | Ingestion, profiling, and query execution | Your agreements for those systems |

### Contributing

**This project is currently not accepting contributions.** Issues, pull
requests, and patches submitted from outside the Auto Ontology maintainer team will
not be reviewed or merged. Security-relevant reports should follow the
process described in [`SECURITY.md`](./SECURITY.md). Maintainer workflow is in
[`CONTRIBUTING.md`](./CONTRIBUTING.md).

---

## Source: docs/mcp.md — MCP server

## Auto Ontology MCP server

Lets any MCP-capable agent — Cursor, Claude Desktop, an internal agent — ask
questions about your data in natural language, and inspect the semantic layer
behind the answers. Anything that speaks [Model Context
Protocol](https://modelcontextprotocol.io) can use it.

### How it works

The server is an HTTP client of the public Auto Ontology API. It holds no database
credentials, no model configuration, and no credentials of its own:

```
agent harness  ──MCP──▶  auto-ontology-mcp  ──HTTPS──▶  Next.js (public API)
                                                   │
                                                   ▼
                                        FastAPI, Postgres
```

Authentication and permission checks already live in that Next.js layer, so the
server inherits them rather than reimplementing them. Two things follow: it can
run anywhere that can reach your deployment, and **a session can do exactly what
the person behind it can do** — a viewer gets a viewer's answers.

### Running it

Run one server; people log in through it. The URL of your Auto Ontology deployment is the
only thing it needs to be told:

```sh
AUTO_ONTOLOGY_API_URL=https://auto_ontology.example.com auto-ontology-mcp
```

Install with `uvx`, which fetches and builds straight from the repository, so
there is nothing to clone:

```sh
uvx --from "git+https://github.com/NVIDIA/auto-ontology.git#subdirectory=mcp" auto-ontology-mcp
```

> [!NOTE]
> Auto Ontology is NVIDIA-internal today, so this install needs GitHub credentials with
> access to the repository (`gh auth login`, or any cached git credential
> helper). It shortens to a plain `uvx auto-ontology-mcp` once the package is published to
> PyPI; until then `uvx auto-ontology-mcp` alone will not resolve.

### Connecting a client

Point the client at the URL. There are no credentials in the config:

```json
{
  "mcpServers": {
    "auto-ontology": {
      "url": "https://auto-ontology-mcp.example/mcp"
    }
  }
}
```

Note the `/mcp` suffix: that is the endpoint, not the server's root. Restart the
client after editing its config, since most read MCP configuration only at
startup.

The client sees that the server wants authorization and offers to sign in —
Cursor lists it as needing login. The user gets Auto Ontology's ordinary login page, with
whatever SSO that deployment uses, and the client ends up holding a token it
manages itself. Nothing is minted or pasted by hand, and every call runs as the
person who signed in.

Then ask something like *"what does Auto Ontology mean by an active customer, and how many
were there last quarter?"*

### Sign-in

Auto Ontology is the authorization server. This server holds no client id, no client
secret, and no redirect URI, so there is nothing to configure per deployment and
nothing to register with an identity provider — clients register themselves with
Auto Ontology automatically.

Registrations and grants live in Auto Ontology's database, so replicas share them and a
restart signs nobody out. Permissions come from the account on every call rather
than from the token, so changing a role, banning a user, or deleting a grant
takes effect immediately.

The tokens are opaque, so the server asks Auto Ontology's OAuth UserInfo endpoint to check
each one. That bearer-authenticated endpoint needs no client secret and checks
expiry, revocation, client, and browser-session state on every call. The grant
must include the `openid` scope (Better Auth's UserInfo requirement); Auto Ontology
advertises it on the authorization server so clients that copy
`scopes_supported` include it. If Auto Ontology cannot be reached the call fails as an
error rather than as "sign in again", so an outage does not send everyone into a
login that cannot succeed either.

There is no way to configure a token for the server itself. One would make every
caller act as its owner — their permissions, their conversation history — and
nothing in the protocol would reveal it.

### Pointing at a Auto Ontology on your own machine

Only `AUTO_ONTOLOGY_API_URL` changes. For the Docker stack the web app is on `:3000`:

```sh
AUTO_ONTOLOGY_API_URL=http://localhost:3000 auto-ontology-mcp
```

Sign-in needs a Auto Ontology new enough to be an authorization server, which an
already-built image may not be. Checking first is worth it, because otherwise the
failure surfaces as a client that cannot log in:

```sh
curl -s -o /dev/null -w '%{http_code}\n' $AUTO_ONTOLOGY_API_URL/.well-known/oauth-authorization-server
```

A `200` is what you want. Anything else means running the frontend from your
checkout instead — `pnpm dev`, with `AUTO_ONTOLOGY_API_URL` pointing at its port.

### Tools

Everything here reads. Nothing modifies the glossary, the catalog, or the
underlying databases.

| Tool | What it is for |
| --- | --- |
| `ask_question` | **The primary tool.** Ask a question in plain language; get the answer, the SQL Auto Ontology ran, and the rows. |
| `check_answerable` | Grade whether the semantic layer covers a question. Cheap pre-flight before `ask_question`. |
| `check_readiness` | Whether this deployment can answer anything at all. |
| `search_terms` | Search the business glossary. |
| `get_term` | One term: description, synonyms, related terms. |
| `get_term_columns` | The physical columns a term maps to. |
| `get_term_sql_attributes` | The SQL attributes defined under a term. |
| `get_sql_attribute` | One SQL attribute: its expression and purpose. |
| `describe_table` | A table's columns, related terms, and SQL attributes together. |

There is deliberately no tool for browsing databases, schemas, or raw columns.
Consumers are meant to reach the data through the semantic layer, and a catalog
browser invites an agent to reason about raw tables instead. `describe_table`
covers the legitimate case, since what it returns is the terms and SQL attributes
a table participates in.

The server also advertises **instructions** at handshake describing how the tools
sequence, which spares the model from inferring it — left to itself it tends to
reach straight for `ask_question`.

#### About `ask_question`

It is a call to `POST /api/chat/completions`, the same endpoint the web UI uses,
which runs the full text-to-SQL agent: many sequential model calls, typically
tens of seconds. It returns the answer, the SQL, and the rows as separate fields
rather than the markdown the UI receives, so an agent can use the SQL without
parsing prose. Results are capped at 100 rows, with `row_count` and `truncated`
reporting what was withheld. It emits MCP progress notifications as the agent
works, mirroring the reasoning trace the web UI shows.

#### About `check_readiness`

Answering a question needs two independent things: a compiled semantic layer to
resolve the question against, and a live database connection to run the SQL on.
Having one without the other is this deployment's most misleading state, because
everything looks healthy — the glossary reads, terms resolve — and every question
still fails, expensively and vaguely, after minutes of model calls.
`check_readiness` tells that apart up front, and reports every blocker at once.

Note that `databases` can be non-empty while `can_execute_sql` is false: the
catalog outlives the connection it was ingested from, so a named database is not
evidence that anything can be queried. Reading connections is also admin-only by
default, so a viewer gets a 403 there while chat and the catalog read fine — that
is neither a broken deployment nor a bad credential, so the fact is reported
under `unverified` and the verdict stands on what could be checked.

### Configuration

| Variable | Default | Meaning |
| --- | --- | --- |
| `AUTO_ONTOLOGY_API_URL` | `http://localhost:3000` | Base URL of the Auto Ontology web app. |
| `AUTO_ONTOLOGY_MCP_PUBLIC_URL` | `http://localhost:3003` | Public MCP origin, without `/mcp`. The frontend must receive the same value so issued tokens have the resource URL clients use. |

Rarely needed: `AUTO_ONTOLOGY_MCP_HOST` and `AUTO_ONTOLOGY_MCP_PORT` (bind address and port, default
`0.0.0.0:3003`), `AUTO_ONTOLOGY_MCP_TIMEOUT_S` and `AUTO_ONTOLOGY_MCP_CHAT_TIMEOUT_S` (request
timeouts, `30` and `900`), and `AUTO_ONTOLOGY_OPENAPI_SPEC` (override the spec tools are
generated from).

### Extending the tool surface

The tool set is an explicit allow-list in
[`mcp/auto_ontology_mcp/tools.py`](../mcp/auto_ontology_mcp/tools.py). The spec publishes 87
operations, and exposing all of them would degrade tool selection badly. To
publish another, add a `ToolSpec` naming its method, path, an agent-facing name,
and a description that says *when to reach for it*. Startup fails loudly if a
curated entry no longer exists in the spec, so a rename upstream cannot silently
drop a tool.

Parameters and descriptions come from
[`auto-ontology-api.json`](./openapi/auto-ontology-api.json), which is committed twice: canonically
under `docs/openapi/`, and again inside the package, because the server reads it
at startup and must work from an install where no `docs/` directory exists.
`pnpm openapi` writes both and CI diffs both, so never edit the packaged copy by
hand.

### Troubleshooting

**A client cannot discover how to sign in** — check that
`$AUTO_ONTOLOGY_API_URL/.well-known/oauth-authorization-server` returns JSON. A redirect to
the login page instead means the deployment predates that route.

**"Protected resource ... does not match expected ..."** — the server advertises
the address it was bound to, and the client is reaching it under a different
spelling of the same host, almost always `127.0.0.1` against `localhost`. Set
`AUTO_ONTOLOGY_MCP_PUBLIC_URL` to the URL the client uses, or leave `AUTO_ONTOLOGY_MCP_HOST` unset.

**"This request carried no signed-in session"** — the grant behind the call
expired or was revoked in Auto Ontology. Sign in again from the client.

**`ask_question` returned an empty answer, with no SQL and no error** — the run
completed but retrieval found nothing to build a query from. Call
`check_readiness` first: most often no database connection is configured, so no
question can succeed however it is phrased. If the deployment is ready, the
question's vocabulary is the problem — `search_terms` for the nouns in it.

**"Auto Ontology cannot answer right now"** — usually the semantic layer was never
compiled; confirm with `check_readiness`. It also appears when a
`conversation_id` already has a turn in flight.

**Client shows no tools** — check the client's MCP logs. The server logs to
stderr.

---

## Source: skills/nvidia-ontology-query/SKILL.md

---
name: nvidia-ontology-query
description: >-
  Query Auto Ontology and validate generated SQL, rows, and
  answers. Use for MCP or REST access, readiness, authentication, conversations,
  and grounded questions.
license: Apache-2.0
metadata:
  version: "0.2.1"
  author: "NVIDIA <opensource@nvidia.com>"
  tags:
    - nvidia-ontology
    - mcp
    - api
    - agents
    - aiq
---



## Auto Ontology grounded queries

### Purpose

Query the current Auto Ontology implementation from an agent without prescribing a
harness, SDK, or LangGraph template. Typed workflow artifacts, statuses, gates,
and handoffs are in [runtime-contract.yaml](assets/runtime-contract.yaml).

### Prerequisites

Use a running Auto Ontology deployment and an authenticated MCP or REST client. If Auto Ontology is
not running, use `nvidia-ontology-setup` first.

### Limitations

This skill reads and validates answers. It does not expose FastAPI directly,
write semantic definitions, publish governed results, or provide a raw-schema
browser. Hand mutations and publication to `nvidia-ontology-management`.

### Instructions

1. Call readiness before asking a question.
2. Discover terms and confirm answerability through the semantic layer.
3. Ask through MCP, or use the authenticated Next.js REST gateway as fallback.
4. Validate material intent, SQL, rows, truncation, and prose before presenting
   a claim-bearing answer.

### Prefer MCP for reads

When the harness speaks MCP, use it. The **handshake tool list** is the live
source of truth (`mcp/auto_ontology_mcp/tools.py`). Do not copy a tool table into the
session; if the handshake and this skill disagree, trust the handshake.

Sequence (the server also advertises this so models do not jump straight to
`ask_question`):

1. `check_readiness` — compiled semantic layer **and** a live DB connection.
2. `search_terms` — what the nouns mean here.
3. `check_answerable` — cheap coverage check.
4. `ask_question` — full text-to-SQL; tens of seconds; answer + SQL + rows
   (capped at 100 rows, with `row_count` / `truncated`).
5. For a claim-bearing answer, validate material intent, generated SQL, returned
   rows, truncation, and prose using
   [query-validation.md](references/query-validation.md).

Everything on MCP **reads**. There is no MCP tool for raw databases, schemas,
or columns on purpose. `describe_table` is the legitimate table view: terms
and SQL attributes the table participates in.

Connect: `AUTO_ONTOLOGY_API_URL` is the **web app**. Run `auto-ontology-mcp`, point the client at
`…/mcp`, user signs in. No token on the MCP server. Details:
repository `mcp/README.md` and `docs/mcp.md`.

### REST fallback and write handoff

When MCP is unavailable, public clients call the authenticated **Next.js
gateway**, not FastAPI
`:3001`. FastAPI trusts `x-auto-ontology-user-id` and must not be exposed. A direct
FastAPI request without `conversation_id` is stateless; with
`conversation_id` it requires that internal header.

Auth (any of these; resolved in one place):

- Browser session cookie
- API token: `x-api-key: $AUTO_ONTOLOGY_API_TOKEN` (`Authorization: Bearer` works for
  `auto_ontology_…` tokens too). Token acts as its owner.
- OAuth bearer issued by Auto Ontology (MCP sign-in)
- SSO id token (`Authorization: Bearer <jwt>`), e.g. AI-Q — see
  [stack.md](references/stack.md)

Shapes: `docs/openapi/auto-ontology-api.json`. Do not scrape all ~87 operations. A write
request hands off to `nvidia-ontology-management`; this skill does not turn a read-only
question into a mutation.

#### Chat

`POST /api/chat/completions` — SSE `step` / `result` / `error` / `charts`,
then `[DONE]`. Permission `chat:use`; a request with `conversation_id` also
needs `conversation:write`, or it gets 403.

- Omit `conversation_id` for a one-shot (no history, no chart step).
- Supply a client-generated UUID to create or continue a thread (needs
  `chat:use` and `conversation:write`).
- Wait for `[DONE]` before the next turn; overlapping requests return
  **`409 Conversation in progress`**.
- A 404 on a conversation id means it belongs to another user.

Python (from the Auto Ontology README; no extra SDK):

```python
import os
import requests

session = requests.Session()
session.headers["x-api-key"] = os.environ["AUTO_ONTOLOGY_API_TOKEN"]

terms = session.get("https://ontology.example.com/api/terms").json()

answer = session.post(
    "https://ontology.example.com/api/chat/completions",
    json={"question": "How many orders shipped last week?"},
)
## response is SSE, not a single JSON object
```

Open an API-created thread in the UI at `/chat?focus=<conversation_id>` when
it belongs to the signed-in user.

#### Discovery (semantic layer, not a catalog browser)

MCP first. REST fallback:

- `GET /api/terms` (`query`, `skip`, `limit`)
- `GET /api/terms/{term_id}`
- `GET /api/exploration/tables/{table_id}/details`
- `GET /api/exploration/graph`

Writes and compile reset: `nvidia-ontology-management`.

### Validate claim-bearing answers

Do not treat successful execution as sufficient evidence. Before presenting a
decision-facing result, apply
[query-validation.md](references/query-validation.md) to check population,
measure, unit, grain, joins, lineage, status, validity, rows, truncation, and
answer prose. If a material constraint cannot be verified, return the gap rather
than a stronger claim.

### Empty or failed answers

`ask_question` / chat returned nothing useful → `check_readiness` (or
`GET /api/semantic-compilation/status`) before rewriting the question. A
named database is not proof SQL can execute. See `nvidia-ontology-setup`
troubleshooting.

### Examples

- For a grounded count, run `check_readiness`, `search_terms`,
  `check_answerable`, and then `ask_question`.
- If a response is truncated or violates measure grain, refuse the complete
  claim and follow [query-validation.md](references/query-validation.md).

### Troubleshooting

For empty or failed answers, check readiness and compilation status before
rephrasing. For REST errors, verify the public web origin, authentication, and
conversation ownership before retrying.

### See also

- [stack.md](references/stack.md) — AI-Q, Nemotron, cuOpt (what exists vs
  what partners wire)
- [query-validation.md](references/query-validation.md) — material intent, SQL,
  rows, and answer checks
- `nvidia-ontology-management` — model, modify, and publish through the layer
- `nvidia-ontology-setup` — bring-up and MCP OAuth discovery

---

## Source: skills/nvidia-ontology-management/SKILL.md

---
name: nvidia-ontology-management
description: >-
  Model and publish semantic definitions in Auto Ontology. Use for terms, relationships,
  measures, imports, and governed results—not deployment or querying.
license: Apache-2.0
metadata:
  version: "0.2.1"
  author: "NVIDIA <opensource@nvidia.com>"
  tags:
    - nvidia-ontology
    - ontology
    - glossary
    - sql-attributes
    - catalog
---



## Auto Ontology management and modeling

### Purpose

Inspect and change Auto Ontology's semantic layer without confusing a successful API call
with correct business meaning or durable publication. The machine-readable
inputs, outputs, statuses, gates, and handoffs are in
[runtime-contract.yaml](assets/runtime-contract.yaml).

Choose the focused workflow before acting:

- routine inspection or metadata edits: continue below and use
  [write-api.md](references/write-api.md);
- concepts, relationships, measures, units, grain, or policies: use
  [modeling.md](references/modeling.md);
- model promotion or reusable analytical results: use
  [publication.md](references/publication.md).

MCP tools only **read**. Create, patch, import, and compile-reset go through
the Next.js `/api/...` gateway. Governed result rows require an approved source
writer; Auto Ontology has no generic result-row writeback endpoint. Request bodies and
field types live in `docs/openapi/auto-ontology-api.json`; this skill names operations and
permissions only.

### Prerequisites

Use a running, authenticated Auto Ontology deployment. Use `nvidia-ontology-setup` when
the deployment or semantic layer is not ready.

### Limitations

MCP is read-only, Auto Ontology has no generic result-row writeback endpoint, and current
model import and certification APIs do not prove atomic promotion. Follow the
publication gates below and fail closed when exact readback is unavailable.

### Auth

Scripts use an API token (`x-api-key` or `Authorization: Bearer`). Mint it in
the UI (user menu → API Tokens). A token **acts as its owner** — a viewer's
token cannot do admin things. Creating and revoking tokens requires a signed-in
session; a token cannot mint another token.

Writes below need `catalog:edit` unless noted. `403` means the owner's role
lacks that permission, not that the path is wrong.

### Instructions

1. **Discover current meaning** via MCP (`search_terms`, `get_term`,
   `get_term_columns`, `get_term_sql_attributes`, `describe_table`) or REST
   if MCP is absent (`GET /api/terms`, `GET /api/terms/{term_id}`,
   `GET /api/exploration/tables/{table_id}/details`).
2. **Resolve the semantic contract** when meaning changes. Record source
   binding, identity, population, relationship cardinality, measure expression,
   unit, grain, denominator, time, validity, and counterexamples; see
   [modeling.md](references/modeling.md).
3. **State the proposed change** to the user (term rename, new SQL attribute,
   import, and so on). Do not silently rewrite the glossary.
4. **Validate SQL** before create/update: `POST /api/sql-attributes/validate`.
   A parse failure is **HTTP 422**, not `valid: false`.
5. **Apply** the smallest write that matches the request (see
   [write-api.md](references/write-api.md)).
6. **Compilation is not a hidden side effect.** Check
   `GET /api/semantic-compilation/status`. Do **not** call
   `POST /api/semantic-compilation/reset` as cleanup — it is an asynchronous,
   destructive rebuild of every database's compiled layer, returns 202, and
   requires `semanticCompilation:manage`.
7. **Verify the persisted change**, not merely request success. Model imports
   require a scoped backup and exact re-export comparison; see
   [publication.md](references/publication.md). Then use MCP
   `check_answerable` / `ask_question` (or REST
   `POST /api/question-entity-coverage` and `POST /api/chat/completions`) for
   positive and negative behavior checks.

### Semantic relationships and "what does this dataset mean"

Stay on the semantic layer. Do not browse raw schemas to answer meaning.

- Term → columns: MCP `get_term_columns` or
  `GET /api/terms/{term_id}/column-attributes`
- Term → derived SQL: MCP `get_term_sql_attributes`
- Table → terms and SQL attributes: MCP `describe_table` or
  `GET /api/exploration/tables/{table_id}/details`
- Semantic hop chain between two terms:
  `GET /api/exploration/terms/{term_id}/path/{other_term_id}`
- Semantic graphs: `GET /api/exploration/graph`,
  `GET /api/exploration/semantic-graph`

These are semantic relationship paths, not generation provenance, source
revision, certification history, or version lineage.

### Bulk import / export

- `POST /api/model/export` — YAML of catalog + semantic layer.
  Permission `modelInterchange:export`. Body may set catalog database **IDs**
  in `databases` (empty = all) and `format` (`auto_ontology` or `ossie`).
- `POST /api/model/import` — multipart YAML; native Auto Ontology
  (`data_layer` / `semantic_layer`) or Apache Ossie (`version`, `name`,
  `datasets` at the root).
  Query `replace` (default true) and `embed` (default true). Permission
  `modelInterchange:import`. Can replace existing data — confirm with the
  user before `replace=true`, apply first in isolation, and use the exact
  readback workflow in [publication.md](references/publication.md).

### Examples

- To define a run-grain measure, follow the evidence and counterexample workflow
  in [modeling.md](references/modeling.md).
- To revise and promote a model, back up the exact scope and follow the staged
  readback workflow in [publication.md](references/publication.md).

### Troubleshooting

For write failures, verify the authenticated owner's permission, distinguish
HTTP 422 parse failures from validation results, and inspect compilation status
before changing the model or resetting compilation.

### See also

- [write-api.md](references/write-api.md)
- [modeling.md](references/modeling.md)
- [publication.md](references/publication.md)
- `nvidia-ontology-query` — how to call Auto Ontology and validate query results
- `nvidia-ontology-setup` — deployment not ready
- `mcp/auto_ontology_mcp/tools.py` — live read-tool allow-list

---

## Source: skills/nvidia-ontology-setup/SKILL.md

---
name: nvidia-ontology-setup
description: >-
  Set up or troubleshoot the Auto Ontology runtime. Use for Helm (the official
  install), Docker Compose, developer setup, and MCP connection to an existing
  deployment.
license: Apache-2.0
metadata:
  version: "0.3.1"
  author: "NVIDIA <opensource@nvidia.com>"
  tags:
    - nvidia-ontology
    - install
    - docker
    - helm
    - mcp
    - troubleshooting
---



## Auto Ontology setup

### Purpose

Bring up the current Auto Ontology implementation, troubleshoot it, or connect an agent
to an instance that is already running. Do not invent a second installer:
the official installation is the Helm chart in repository-root `DEPLOYMENT.md`;
Docker Compose runs the same stack on one machine. `dev_tools/setup_env.sh` is a
developer tool, not an installer. Typed setup, connection, ingestion,
compilation, and readiness artifacts are in
[runtime-contract.yaml](assets/runtime-contract.yaml).

On failure, read [troubleshooting.md](references/troubleshooting.md) instead of
searching the web.

### Instructions

#### Required questions

Ask these if not already clear. Do not guess a default and emit a command.

1. **Target** — Helm on Kubernetes (the official install, and the default
   recommendation), Docker Compose on one machine, a developer workflow
   (`--dev` / `--ds`, only when changing Auto Ontology itself), or "Auto
   Ontology is already up, I only need MCP"?
2. **NVIDIA NIM key** — is `DEFAULT_MODELS_API_KEY` (Helm:
   `defaultModelsApiKey`) available? Chat and ingest need it.
3. **Admin account** — the email and password for the bootstrap admin.
   Self-service sign-up is disabled, so this is the only way to sign in.
4. **Source database** — a connection string (`CONNECTION_STRINGS` /
   `connectionStrings`), or will connections be added in the UI?
5. **Helm only** — which chart version, and the URL users will browse to
   (`appUrl`).
6. **Compose only** — is host `5432` free? `POSTGRES_PORT` only remaps the
   host side; containers still use 5432 internally.

Never ask the user to paste secrets into the conversation, and never put them
in command arguments. Have the user write them into a values file or `.env`.

### Install with Helm (official)

Releases are published to the public NGC `nvidia` org (chart and images). Follow
`DEPLOYMENT.md` with the version the user named:

The user creates a values file in an editor (not on the command line, so
values stay out of shell history and process arguments), readable only by
them, and out of git:

```yaml
## auto-ontology-values.yaml
defaultModelsApiKey: <API-KEY>
postgresPassword: <POSTGRES-PASSWORD>
adminEmail: <ADMIN-EMAIL>
adminPassword: <ADMIN-PASSWORD>
connectionStrings: <CONNECTION-STRINGS>   # optional; or add connections in the UI
```

```bash
helm fetch https://helm.ngc.nvidia.com/nvidia/charts/auto-ontology-<VERSION>.tgz
helm install auto-ontology auto-ontology-<VERSION>.tgz -f auto-ontology-values.yaml
kubectl port-forward svc/frontend 3000:3000
```

- `adminEmail` and `adminPassword` are required; the install fails without them.
- `appUrl` must be the exact origin users browse to. The default
  (`http://localhost:3000`) only fits the port-forward above; set it for a
  NodePort, ingress, or HTTPS origin.
- `authSecret` is generated on first install and kept across upgrades; set it
  only to share one value across environments.
- If the chart fetch returns 404, that version is not published yet. Ask the
  user; do not fall back to the internal staging registry.

This skill does not cover Astra GitOps.

### Local: Docker Compose

For running the whole stack on one machine. In the repository root, the user
copies `.env.example` to `.env` and fills in `AUTH_SECRET`, `APP_URL`,
`AUTO_ONTOLOGY_ADMIN_EMAIL`, and `AUTO_ONTOLOGY_ADMIN_PASSWORD` (all required).
Then:

```bash
docker compose up -d --build
```

`AUTH_SECRET` and `APP_URL` are required. Without them every page fails with a
Better Auth "default secret" error. Fill `DEFAULT_MODELS_API_KEY` and a
`CONNECTION_STRINGS` value (or plan to add connections in the UI). The full
variable list is `.env.example`.

This builds `auto-ontology` and `auto-ontology-frontend`, starts Postgres,
pgAdmin, and the ingestion service, runs two one-shot migrate jobs, and starts
the app:

- `auto-ontology-migrate` applies Alembic migrations to the backend's `public`
  schema (catalog and semantic tier). The backend waits for it.
- `frontend-migrate` syncs the Prisma `frontend` schema: users, sessions, API
  keys, and the OAuth tables MCP sign-in uses. The frontend waits for it.

If sign-in or MCP login fails, check both with `docker compose ps -a` and
`docker compose logs frontend-migrate`. Read the `frontend-migrate` log even
when it exited 0: it has finished without an error before while leaving MCP
login broken.

| Service | URL |
| --- | --- |
| UI | http://localhost:3000 |
| FastAPI (internal) | http://localhost:3001 |
| Ingestion | http://localhost:3002 |
| pgAdmin | http://localhost:5050 |
| Postgres | localhost:`$POSTGRES_PORT` (from `.env`, default 5432) |

### Developer workflows (`--dev`, `--ds`)

Only for people changing Auto Ontology itself; these are not installations.
`dev_tools/setup_env.sh` starts part of the stack in Docker and leaves the rest
to run from the checkout. Both need the `.env` above plus:

```bash
cd frontend && pnpm install   # Next.js
## from repo root:
uv sync
```

`--dev` runs infra only (Postgres, pgAdmin, ingestion); you run Next.js and FastAPI:

```bash
./dev_tools/setup_env.sh --dev
cd frontend && pnpm dev
## repo root:
uv run uvicorn auto_ontology.server.__main__:create_app --factory --reload --host 127.0.0.1 --port 3001
```

The app factory is `create_app()` in `auto_ontology/server/__main__.py`. There is no
`auto_ontology/server/main.py`. `uv run python -m auto_ontology.server` is the same app without
reload (what the container runs).

`--ds` runs the frontend in Docker and FastAPI on the host:

```bash
./dev_tools/setup_env.sh --ds
uv run python -m auto_ontology.server
```

The frontend image bakes `PYTHON_API_URL=http://host.docker.internal:3001`, so
the API must accept connections from the container, not just loopback.
`python -m auto_ontology.server` binds `0.0.0.0:3001` (what `setup_env.sh --ds`
prints); a `--host 127.0.0.1` uvicorn is unreachable from the container on
Linux. Because FastAPI trusts `x-auto-ontology-user-id`, keep port 3001
firewalled from other machines. On native Linux Docker you may need
`--add-host=host.docker.internal:host-gateway`.

### Limitations

This skill uses the repository's existing Helm chart and Compose file and does
not cover Astra GitOps, change semantic definitions, or treat partial Vault
configuration as secret storage. Ask before destructive volume deletion.

### Auto Ontology is already up — MCP only

Do not reinstall. Point `AUTO_ONTOLOGY_API_URL` at the **web app** (Compose UI is
`:3000`, not FastAPI `:3001`):

```bash
AUTO_ONTOLOGY_API_URL=http://localhost:3000 uvx --from "git+https://github.com/NVIDIA/auto-ontology.git#subdirectory=mcp" auto-ontology-mcp
```

Until the package is on PyPI this needs GitHub credentials that can read
`NVIDIA/auto-ontology`. Client config uses the MCP server URL with a `/mcp` suffix.
People sign in through Auto Ontology; do not put a token on the MCP server.

Confirm the deployment is new enough to be an authorization server:

```bash
curl -s -o /dev/null -w '%{http_code}\n' "$AUTO_ONTOLOGY_API_URL/.well-known/oauth-authorization-server"
```

`200` is required. Anything else: run the frontend from the checkout
(`pnpm dev`) and point `AUTO_ONTOLOGY_API_URL` at that port.

### Examples

- Kubernetes: install the published Helm chart from `DEPLOYMENT.md` with the
  admin account and `appUrl` set.
- One machine: `docker compose up -d --build` after filling `.env`.
- Existing deployment: do not reinstall; configure `AUTO_ONTOLOGY_API_URL` and verify
  OAuth discovery before connecting the MCP client.

### Connect a source

Connections come from one of two places, and only one is used:

- **UI-managed** (Settings → Connections, or the API below). When any exist,
  `CONNECTION_STRINGS` is ignored.
- **`CONNECTION_STRINGS`** in `.env` is a fallback used only when there are no
  UI-managed connections. `GET /api/connections/source` reports whether it is
  set; it cannot carry schema or table filters.

To add a UI-managed connection (permission `connection:manage`):

1. `POST /api/connections/test` validates credentials and returns the schemas
   for the allowlist. A 422 carries the driver's error; fix it before creating.
2. `POST /api/connections` stores the connection. The 201 only means it was
   saved: ingestion is triggered best-effort and may fail or still be running.
3. Verify it landed: `GET /api/datasources/dbs` (`catalog:read`) lists the
   database with the expected tables, `GET /api/semantic-compilation/status`
   reports progress, and MCP `check_readiness` reports no blockers.

Scope is set per connection: a schema allowlist, plus `table_allow_regex` /
`table_deny_regex` applied at catalog extraction (deny wins; unqualified,
case-sensitive names). Env connections have neither. The full table-level scope
guarantee is still open in
[#255](https://github.com/NVIDIA/auto-ontology/issues/255), so if particular tables must never be
catalogued, sampled, or embedded, say that this is not yet enforceable
end-to-end rather than implying it is.

### Verify

1. UI loads at http://localhost:3000 (or the deployed `APP_URL` / Helm `appUrl`) and shows
   the left navigation. Missing nav → stale cookie; see
   [troubleshooting.md](references/troubleshooting.md).
2. `GET /api/semantic-compilation/status` on the **web** origin authenticates
   (cookie, `x-api-key`, or SSO bearer) and returns JSON. `calculated: false`
   means the glossary is empty — ingest / compile, do not keep retrying chat.
3. MCP: OAuth discovery returns 200 (above). Then `check_readiness` once a
   client is connected.

### Stop

```bash
helm uninstall auto-ontology  # Helm; also deletes the postgres-data PVC and its data
docker compose down           # Compose; keep volumes
docker compose down -v        # Compose; wipe Postgres / pgAdmin data
```

Both `helm uninstall` and `docker compose down -v` destroy data; ask first.

### Troubleshooting

Use [troubleshooting.md](references/troubleshooting.md) for stale sessions,
model-key failures, embedding mismatches, port conflicts, and partial Vault
configuration. Redact secrets before sharing command output as evidence.

### See also

- [troubleshooting.md](references/troubleshooting.md)
- [runtime-contract.yaml](assets/runtime-contract.yaml)
- `nvidia-ontology-query` — call Auto Ontology once it is running
- `nvidia-ontology-management` — edit the semantic layer
- `CLAUDE.md` — maintain Auto Ontology itself

---

## Source: AGENTS.md — agent entry point

## AGENTS.md — Auto Ontology agent entry point

Skills that teach an agent how to **set up** the current Auto Ontology implementation and
**use** its ontology layer. They live in **`skills/`** (repo root), one directory
per skill, under the durable `nvidia-ontology*` namespace.

This file is for developers bringing Auto Ontology up and partners embedding it in an
agent harness. Auto Ontology **maintainers** (build, test, schema, frontend conventions)
stay on [`CLAUDE.md`](./CLAUDE.md). Do not fold those conventions into these
skills.

### Which skill to read

- [`skills/nvidia-ontology-setup/`](./skills/nvidia-ontology-setup/) — Helm (the official
  install), local Compose, developer `--dev` / `--ds`, MCP against an
  already-running instance, and troubleshooting. Start here when Auto Ontology is not up yet or something failed
  during bring-up.
- [`skills/nvidia-ontology-management/`](./skills/nvidia-ontology-management/) — inspect, model,
  **modify**, and safely publish through glossary terms, SQL attributes,
  semantic relationships, model YAML import/export, and governed result
  definitions. MCP cannot write; this skill covers the approved write paths.
- [`skills/nvidia-ontology-query/`](./skills/nvidia-ontology-query/) — how an
  agent calls Auto Ontology (MCP first, REST fallback), discovers meaning through the
  semantic layer, and validates SQL, rows, and answers. Start here when Auto Ontology is
  already deployed.

### Workflow ownership and handoffs

| User action | Owning skill |
| --- | --- |
| Install, configure, connect, ingest, compile, prove readiness | `nvidia-ontology-setup` |
| Inspect meaning and semantic relationships | `nvidia-ontology-management` |
| Design concepts, mappings, relationships, measures, units, grain, and policies | `nvidia-ontology-management` → `references/modeling.md` |
| Apply, verify, certify honestly, publish, and roll back | `nvidia-ontology-management` → `references/publication.md` |
| Ask descriptive or diagnostic questions and validate SQL, rows, and prose | `nvidia-ontology-query` → `references/query-validation.md` |

The composed lifecycle is install/connect/readiness → inspect/model → staged
apply/readback → query validation → governed publication → fresh query readback.
A step that lacks product support must return an explicit gap or receipt rather
than inventing an operation. Authentication, permissions, provenance, and error
handling remain shared concerns rather than separate overlapping skills.

### Sources of truth (do not duplicate)

Skills encode **workflow, order, and pitfalls**. They must not become a second
API catalog or a second installer.

| Job | Owner | Skills do |
| --- | --- | --- |
| Install commands | `DEPLOYMENT.md` (Helm, official), `docker-compose.yml`; `dev_tools/setup_env.sh` for developer workflows | Invoke them; do not write a new installer |
| Live read tools | `mcp/auto_ontology_mcp/tools.py` (handshake tool list) | Prefer MCP; sequence reads; never copy the tool table |
| REST shapes and permissions | `docs/openapi/auto-ontology-api.json` | Name the operation and permission; link; do not paste schemas |

MCP is read-only by design. Writes go through the Next.js `/api/...` surface.
The live MCP tool list at handshake is the source of truth if it disagrees
with anything in a skill.

### Catalog mirror

These directories sync to
[github.com/nvidia/skills](https://github.com/nvidia/skills) (`npx skills add nvidia/skills`)
and build.nvidia.com/skills. That pipeline requires, per skill:

- `SKILL.md`, `skill-card.md`, `evals/evals.json` (maintained here)
- `BENCHMARK.md` and `skill.oms.sig` — generated by NVSkills CI. A maintainer
  comments `/nvskills-ci` on any pull request that changes `skills/`; the
  `nv-skills-ci[bot]` pushes an "Attach NVSkills validation signatures" commit
  that must stay in the PR. Never hand-edit or fabricate these files, and rerun
  NVSkills CI after any later change to a skill in the same PR.
- the `components.d/auto-ontology.yml` entry in **nvidia/skills** registering:

```yaml
name: Auto Ontology
repo: NVIDIA/auto-ontology
description: Set up Auto Ontology, model and publish its semantic layer, and run validated text-to-SQL queries through it.
skills:
  - path: skills/nvidia-ontology-setup/
    catalog_dir: nvidia-ontology-setup
  - path: skills/nvidia-ontology-management/
    catalog_dir: nvidia-ontology-management
  - path: skills/nvidia-ontology-query/
    catalog_dir: nvidia-ontology-query
```

Skills must stay free of staging hostnames, cluster names, Vault paths, and
credentials — the catalog is public even when Auto Ontology itself is
access-restricted.

---

