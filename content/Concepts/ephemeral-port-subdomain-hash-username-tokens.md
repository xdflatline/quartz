---
title: "Ephemeral Port in Subdomain, Hash in Username URL Tokens"
details: "An access-control pattern for self-hosted HTTP tunneling where a service is reached via a URL whose *subdomain encodes an ephemeral allocated port* and whose *username (HTTP basic-auth) carries a hash + expiry token*. The token is HMAC-of (expires, port, secret), base64url'd to survive the case-insensitive domain and the URL-safe username position. The nginx `secure_link` directive returns empty (hash mismatch), \"0\" (expired), or \"1\" (accepted), and the location block dispatches to the matching per-port upstream. The pattern avoids a commercial-tunneling service (ngrok, Cloudflare Quick Tunnels) and a separate tunnel daemon (frp, localtunnel, sish) by relying only on OpenSSH reverse port forwarding (`ssh -R 0:localhost:PORT`) plus nginx's regex server_name capture plus the ngx_http_secure_link_module. Demonstrated by Vincent Bernat's `http-over-ssh` setup."
tags:
  - concept
  - architecture-pattern
  - cybersecurity
  - tooling
created: 2026-10-05
updated: 2026-10-05
type: concept
source: "[[Raw/vincent-bernat-http-over-ssh-2026-10-05]]"
---

# Ephemeral Port in Subdomain, Hash in Username URL Tokens

**Source:** [[Raw/vincent-bernat-http-over-ssh-2026-10-05]] (Vincent Bernat, 2026)
**Category:** Architecture Pattern
**Status:** Production-validated (running on luffy.cx; published as NixOS configuration in the linked repo)

## Overview

A self-hosted HTTP tunneling service can be built with nothing but OpenSSH + nginx + Let's Encrypt + the `ngx_http_secure_link_module`. The pattern encodes access-control information directly into the URL:

```
https://<hash>------<expires>@p<port>.ssh.example.com/path

  https://  - scheme
  -            fixed-prefix optional auth
  hash         - hash     (in URL user field; case-preserving; 22 chars base64url)
  expires      - expires  (unix timestamp)
  port         - port     (in subdomain; case-insensitive)
  path         - path
```

The token has three parts that together prove you are authorized to hit that port:

1. **Hash** — base64url(HMAC-like-MAC(expires, port, secret)) truncated to 22 chars; the secret never leaves the server.
2. **Expires** — unix timestamp; gates the URL's TTL.
3. **Port** — the ephemeral OpenSSH-allocated remote port (5 digits).

Any one without the others is useless. The secret on the server is what binds the token to the port, so an attacker who learns the port still needs the secret-derived hash.

## How the request flows

```
client                                 server (nginx / luffy.cx)
  |                                           |
  |── GET https://<token>------<exp>@p<port>.ssh.example.com/path ──▶
  |                                           │
  |                                $remote_user = "<hash>--<expires>"
  |                                $host        = "p<port>.ssh.example.com"
  |                                map $remote_user $httpssh_link → "<hash>,<expires>"
  |                                secure_link $httpssh_link
  |                                secure_link_md5 "$secure_link_expires $port ZuPerS3cr3!"
  |                                           │
  |                                $secure_link = "1" → proxy_pass http://127.0.0.1:$port
  |                                $secure_link = "0" → return 410 (Gone)
  |                                $secure_link = "" → return 401 + WWW-Authenticate
  |                                           │
  |◀──────────── HTTP 200 (forwarded to localhost) ──────
```

## Why this layout

Three constraints dictate the layout:

1. **The hash cannot live in the subdomain** — DNS is case-insensitive; base64 hashes are case-sensitive; putting the hash there loses entropy.
2. **The hash must survive the username position** — URL basic-auth usernames are case-sensitive; base64url (replace `+`/`/` with `-`/`_`, strip `=`) survives intact.
3. **The port must be visible at L7** — nginx's `server_name` capture (`~^p(?<port>\d\d\d\d\d)\.`) routes to the matching per-port upstream without state.

This produces a URL that's both **bearer-token-like** (URL contains all auth) and **stateless for the server** (no session store; the secret does the work).

## How to allocate the port

OpenSSH reverse port forwarding with `ssh -R 0:localhost:PORT` makes the server pick a free port. The trick is that **OpenSSH doesn't surface the allocated port to the remote-side shell via env vars**. To discover it, walk up to the ancestor `sshd-session` process and read its listening ports via `ss`:

```bash
# Walk up the process tree to find sshd-session ancestors
pids=$(
  pid=$$
  while [ "$pid" -gt 1 ]; do
    line=$(ps -o comm=,pid=,ppid= -p "$pid")
    echo "$line"
    pid=${line##* }
  done | awk '$1 == "sshd-session" { printf "pid=%s,\n", $2 }'
)

# Read the listening sockets from those PIDs
ports=$(sudo -n ss --listening --numeric --tcp --processes --no-header \
  | grep -F "$pids" \
  | awk '{ print $4 }' | awk -F: '{ print $NF }' \
  | sort -un)
```

The `sudo` requirement is real: `ss --listening --processes` needs `CAP_NET_ADMIN` to read the listener's PID back.

## How to generate the token (server-side, given a port)

```bash
lifetime=86400
secret='ZuPerS3cr3!'
expires=$(( $(date +%s) + lifetime ))
for port in $ports; do
  token=$(printf '%s %s %s' "$expires" "$port" "$secret" \
            | openssl md5 -binary \
            | openssl base64 \
            | tr +/ -_ | tr -d =)
  echo "https://$token--$expires@p$port.ssh.example.com/"
done
```

The MD5 + secret pattern matches what `ngx_http_secure_link_module` expects via `secure_link_md5`. The hash function is the module's choice (MD5); an attacker with the URL has expires + port but no way to forge the hash without the secret.

## The full nginx config

```nginx
map $remote_user $httpssh_link {
  "~^([-_A-Za-z0-9]{22})--([0-9]+)$" "$1,$2";
}
server {
  listen 0.0.0.0:443 ssl ;
  listen [::0]:443 ssl ;
  server_name ~^p(?<port>\d\d\d\d\d)\.ssh\.example\.com$;
  location / {
    secure_link $httpssh_link;
    secure_link_md5 "$secure_link_expires $port ZuPerS3cr3!";
    if ($secure_link = "") {
      add_header WWW-Authenticate 'Basic realm="tunnel"' always;
      return 401;
    }
    if ($secure_link = "0") {
      return 410;
    }
    proxy_pass http://127.0.0.1:$port;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Authorization "";
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_buffering off;
    proxy_read_timeout 30m;
  }
}
```

Three things to notice:

1. **Strip the `Authorization` upstream** — the upstream service shouldn't see the bearer token; treat the hash as scoped to the proxy.
2. **`$secure_link_md5` interpolates `$secure_link_expires`** — that's a built-in variable the module populates from the parsed expires token.
3. **Three-state dispatch** — empty/`0`/`1` collapse cleanly into 401/410/200 with no extra logic.

## Why this is good enough

The hash is short-lived (24h default), scoped to one port (can't be replayed across ports), and the secret stays on the server. The downsides are real but bounded:

- **MD5** is the module's choice; a stronger MAC would be better but isn't natively supported by `ngx_http_secure_link_module`.
- **HTTPS basic-auth** is used as a transport for the URL-borne token; works with `curl`, browsers, and most clients without modification.
- **Enumeration of ports** is mitigated by short-lived tokens + the secret; a port-scanner without the token can't replay.

This is materially better than commercial-tunneling defaults for self-hosting:
- No third-party in the data path;
- No client binary on the developer's machine beyond OpenSSH (already there);
- No separate tunnel service (frp, sish) to maintain.

## Tradeoffs vs commercial alternatives

| Dimension | This pattern | ngrok / Cloudflare Quick Tunnels | frp / localtunnel / sish |
|-----------|--------------|----------------------------------|--------------------------|
| Self-hostable | Yes | No | Yes |
| Client binary on dev box | Just `ssh` | Their client | Their daemon |
| Custom domain | Yes (wildcard cert) | Paid plan only | Top-level config |
| Token mechanism | URL-borne HMAC + TTL | Service token | Free for any port |
| Setup cost | Wildcard DNS + DNS-01 ACME | Zero | One config file |

## Connection to other patterns

- [[Concepts/deterministic-hook-guardrails]] — the same three-state return (`""` / `"0"` / `"1"`) is the shape a hook returns when it can hard-stop, soft-fail, or allow.
- [[Concepts/live-asset-graph-blast-radius]] — both articles ask "how do I expose the minimum surface for a public service?"
- [[Concepts/structured-telos-file-for-durable-intent]] — orthogonal: this pattern is a runtime mechanism; TELOS is a state mechanism.

## Key Insights

1. **Case-preserving vs case-insensitive matters.** Hash in username (case-sensitive); port in subdomain (case-insensitive). Mis-assigning loses entropy.
2. **The secret never leaves the server.** The URL only carries `hash(secret)`, never `secret`. A leaked token is bounded by its TTL.
3. **`ngx_http_secure_link_module`'s three-state return is the dispatch.** Empty / "0" / "1" maps cleanly to 401 / 410 / 200 with no extra code.
4. **The hardest engineering is finding the port.** OpenSSH intentionally doesn't expose it; the ancestor `sshd-session` walk + `ss --processes` is the workaround.

## Related Concepts

- [[Concepts/deterministic-hook-guardrails]] — same three-state return shape
- [[Concepts/live-asset-graph-blast-radius]] — minimum-surface-for-public-service question
- [[Entities/lifeos]] — different solution space (full harness); this pattern is a single-purpose tunnel

## References

- Raw: [[Raw/vincent-bernat-http-over-ssh-2026-10-05]]
- Origin: [Self-hosted HTTP tunnels with SSH and nginx](https://vincent.bernat.ch/en/blog/2026-http-over-ssh) by Vincent Bernat
- Helper script: https://github.com/vincentbernat/nixops-take1/blob/master/tags/http-over-ssh.sh
- NixOS config: https://github.com/vincentbernat/nixops-take1/blob/master/tags/http-over-ssh.nix
- nginx module docs: https://nginx.org/en/docs/http/ngx_http_secure_link_module.html
- Tunnels surveyed: https://github.com/anderspitman/awesome-tunneling