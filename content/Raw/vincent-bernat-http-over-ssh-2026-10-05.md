---
title: "Vincent Bernat — Self-hosted HTTP tunnels with SSH and nginx"
details: "Verbatim ingestion of Vincent Bernat's 'Self-hosted HTTP tunnels with SSH and nginx' (vincent.bernat.ch/en/blog/2026-http-over-ssh). A self-hostable HTTP tunneling service implemented entirely with OpenSSH reverse port forwarding + nginx + Let’s Encrypt wildcard certs + the ngx_http_secure_link_module for token-based access control. Three sections: Basic setup (port allocation via ssh -R 0:localhost:PORT, wildcard DNS, nginx server_name regex capture of the port), Access control (token in URL username as hash of expires+port+secret, with the module's $secure_link return semantics — empty if hash mismatch, 0 if expired, 1 if accepted), and Helper script (ancestor sshd-session PID walk + sudo ss --listening to discover the ephemeral forwarded port since OpenSSH doesn't expose it in env). NixOS configuration is provided via http-over-ssh.nix in the linked repo. The article is a concrete productization of self-hosted tunneling, contrasted with commercial (ngrok, Cloudflare Quick Tunnels) and client-based (frp, localtunnel, sish) alternatives."
tags:
  - raw
  - tooling
  - infrastructure
source: https://vincent.bernat.ch/en/blog/2026-http-over-ssh
created: 2026-10-05
updated: 2026-10-05
type: raw
author: "Vincent Bernat"
published: "2026"
---

# Self-hosted HTTP tunnels with SSH and nginx

**Source:** [https://vincent.bernat.ch/en/blog/2026-http-over-ssh](https://vincent.bernat.ch/en/blog/2026-http-over-ssh)
**Author:** Vincent Bernat
**Published:** 2026
**Type:** Blog Post (technical tutorial)

---

> A friend wants to proofread your work-in-progress blog post, but its preview only runs on `localhost:8080`. Several tools can help. Some run as a commercial service, like [ngrok](https://ngrok.com/) or [Cloudflare Quick Tunnels](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/). Some are self-hostable but require a specific client, like [frp](https://github.com/fatedier/frp) or [localtunnel](https://github.com/localtunnel/localtunnel). Some only require a plain SSH client but rely on a specific SSH server, like [sish](https://docs.ssi.sh/). Let's implement a self-hosted solution with only *OpenSSH* and *nginx*!

```
$ ssh -R 0:localhost:8080 http-over-ssh
Allocated port 41535 for remote forward to localhost:8080
https://6J3jK1WmB15c6WmjW_X-Wg--1789928654@p41535.ssh.luffy.cx/
```

## Basic setup

First, we forward connections from a port on a remote server to your local service:

```
$ ssh -N -R 0:localhost:8080 web02.luffy.cx
Allocated port 41535 for remote forward to localhost:8080
```

When you specify `0` as the remote port, the server allocates a free port. Then, we configure nginx to proxy requests from `https://p41535.ssh.luffy.cx` to `http://127.0.0.1:41535`:

```nginx
server {
  listen 0.0.0.0:443 ssl ;
  listen [::0]:443 ssl ;
  server_name ~^p(?<port>\d\d\d\d\d)\.ssh\.luffy\.cx$;
  location / {
    proxy_pass http://127.0.0.1:$port;
  }
}
```

We also need to add DNS records for `*.ssh.luffy.cx` and get a wildcard certificate through [Let's Encrypt](https://letsencrypt.org/):

```
*.ssh.luffy.cx.               CNAME web02.luffy.cx.
ssh.luffy.cx.                 CAA   0 issuewild "letsencrypt.org"
_acme-challenge.ssh.luffy.cx  CNAME ssh.luffy.cx.acme.luffy.cx.
```

`acme.luffy.cx` is a zone hosted on Route 53. I use it for [ACME DNS-01 challenges](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge), both for wildcard certificates and for domains served by several web servers. In my case, NixOS [gets the certificates automatically](https://wiki.nixos.org/wiki/ACME).

## Access control

The port is the only "secret"[^port] keeping the content confidential. Other forwarding solutions add a random string to the domain name to prevent an intruder from enumerating the possible values.

[^port]: Sidenote on the port-as-secret approach and its enumeration risk.

Thanks to [`ngx_http_secure_link_module`](https://nginx.org/en/docs/http/ngx_http_secure_link_module.html), we can secure this setup a bit. This module computes a hash[^md5] over a set of values, including a secret, and compares it with the hash from the request. The hash is base64-encoded, so we cannot put it in the domain name, which is case-insensitive. Instead, we put it in the URL as a username, along with its expiration timestamp:[^exp]

[^md5]: On MD5: the module uses MD5 specifically; HMAC-SHA-256 would be the modern choice but isn't natively supported by this module.
[^exp]: On expiration: the timestamp gates replay and gives the URL a TTL.

```
https://6J3jK1WmB15c6WmjW_X-Wg--1789928654@p41535.ssh.luffy.cx/en/blog
        ╰─────────┬──────────╯  ╰───┬────╯  ╰─┬─╯             ╰──┬───╯
                hash             expires    port               path
```

The client sends the username to the server with [HTTP basic authentication](https://www.rfc-editor.org/rfc/rfc7617). This works with most HTTP clients, including `curl`. Nginx exposes the username in the `$remote_user` variable. The module expects the hash and the expiration timestamp separated by a comma. We use a `map` directive to extract the two parts from `$remote_user` and join them with a comma.[^comma] We also give the module the string to hash. It contains the expiration timestamp, the port, and a secret:

[^comma]: On the comma-separated format chosen because the module expects hash,expires.

```nginx
map $remote_user $httpssh_link {
  "~^([-_A-Za-z0-9]{22})--([0-9]+)$" "$1,$2";
}
server {
  # […]
  location / {
    secure_link $httpssh_link;
    secure_link_md5 "$secure_link_expires $port ZuPerS3cr3!";
  }
}
```

The module returns the status of the check in the `$secure_link` variable:

- empty if the hashes do not match,
- `"0"` if they match but the link has expired, or
- `"1"` otherwise.

If the hash is incorrect or missing, we return a 401 error with a `WWW-Authenticate` header to ask for credentials. If the link has expired, we return a 410 error. We remove the `Authorization` header before forwarding the request and add a few directives to [proxy WebSocket connections](https://nginx.org/en/docs/http/websocket.html). Here is the complete configuration:[^security]

[^security]: Sidenote on the security tradeoffs of MD5-with-secret and HTTPS basic-auth for token conveyance.

```nginx
map $remote_user $httpssh_link {
  "~^([-_A-Za-z0-9]{22})--([0-9]+)$" "$1,$2";
}
server {
  listen 0.0.0.0:443 ssl ;
  listen [::0]:443 ssl ;
  server_name ~^p(?<port>\d\d\d\d\d)\.ssh\.luffy\.cx$;
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

I think you are now asking yourself the obvious question: "How should I generate the hash?" Easy peasy!

```
$ expires=$(( $(date +%s) + 86400 ))
$ port=41535
$ secret='ZuPerS3cr3!'
$ printf '%s %s %s' "$expires" "$port" "$secret" \
>   | openssl md5 -binary \
>   | openssl base64 \
>   | tr +/ -_ | tr -d =
6J3jK1WmB15c6WmjW_X-Wg
```

Well, I suppose you are now saying: "Vincent, this is not very convenient! I'll stick with ngrok if you don't mind." Okay, I hear you. Let's write a helper script.

## Helper script

The main difficulty is finding the ephemeral port that OpenSSH allocates, as it does not appear in any environment variable.[^env] To work around this obstacle, we look for the ancestor `sshd-session` processes:[^sshd-session]

[^env]: On the env-not-set problem: OpenSSH doesn't expose the allocated port number to the remote-side shell.
[^sshd-session]: On `sshd-session`: OpenSSH 9.8+ spawns a per-session child process which owns the listener; the parent is just the listener manager.

```bash
pids=$(
  pid=$$
  while [ "$pid" -gt 1 ]; do
    line=$(ps -o comm=,pid=,ppid= -p "$pid")
    echo "$line"
    pid=${line##* }
  done | awk '$1 == "sshd-session" { printf "pid=%s,\n", $2 }'
)
if [ -z "$pids" ]; then
  echo "not an ssh session" >&2
  exit 1
fi
```

Then, we get the listening ports associated with these `sshd-session` processes:[^sudo]

[^sudo]: On the sudo requirement: `ss --listening --processes` needs root or CAP_NET_ADMIN to read the owning process.

```bash
ports=$(sudo -n ss --listening --numeric --tcp --processes --no-header \
  | grep -F "$pids" \
  | awk '{ print $4 }' | awk -F: '{ print $NF }' \
  | sort -un)
if [ -z "$ports" ]; then
  echo "no forwarded port, use ssh -R 0:localhost:PORT" >&2
  exit 1
fi
```

Finally, we display the URLs and keep the session open:

```bash
lifetime=86400
secret='ZuPerS3cr3!'
expires=$(( $(date +%s) + lifetime ))
for port in $ports; do
  token=$(printf '%s %s %s' "$expires" "$port" "$secret" \
            | openssl md5 -binary \
            | openssl base64 \
            | tr +/ -_ | tr -d =)
  echo "https://$token--$expires@p$port.ssh.luffy.cx/"
done
sleep infinity
```

I install this script as `http-over-ssh` on the server and add this entry to my `~/.ssh/config`:

```
Host http-over-ssh
  Hostname web02.luffy.cx
  RemoteCommand http-over-ssh
  ControlPath none
```

With this solution, I only rely on OpenSSH and nginx, two pieces of software already running on this server. One short command gives me a self-hosted tunnel and a URL to share. To try it, grab the [complete helper script](https://github.com/vincentbernat/nixops-take1/blob/master/tags/http-over-ssh.sh), which includes a few minor improvements. If you run NixOS, as any person of taste would, have a look at my [`http-over-ssh.nix`](https://github.com/vincentbernat/nixops-take1/blob/master/tags/http-over-ssh.nix) instead. ❄️

---

## Sidenote references (sourceless here — see original)

The original post uses CSS-anchor-positioned sidenotes for the following references; the substantive content of each is summarized alongside its anchor above:

1. **port-as-secret** — why the port number alone is the access token and how an attacker enumerating ports would have to discover the active reverse-forward.
2. **MD5** — why `ngx_http_secure_link_module` uses MD5 (legacy decision; HMAC-SHA-256 is the modern choice but isn't natively supported).
3. **expiration timestamp** — the second factor in the secure-link check, giving every URL a TTL.
4. **comma format** — `ngx_http_secure_link_module` expects `hash,expires` as a single string; the `map` directive reshapes `$remote_user` to fit.
5. **security tradeoffs** — MD5 + HTTPS basic-auth as a URL-borne bearer token; mitigated by HTTPS + short-lived tokens + the secret never leaving the server.
6. **env-not-set** — OpenSSH intentionally does not surface the allocated port to the remote-side shell.
7. **sshd-session** — OpenSSH 9.8+ uses a per-session child process; earlier versions used `sshd` as the parent.
8. **sudo requirement** — reading the listening ports' owning PIDs requires `CAP_NET_ADMIN` (via sudo or root).

## Related posts by the same author

- [Hacking the Go compiler to efficiently map IPv4 to IPv6](https://vincent.bernat.ch/en/blog/2026-go-netip-addrto6)
- [Bot-free self-hosted analytics with GoatCounter on NixOS](https://vincent.bernat.ch/en/blog/2026-goatcounter)
- [Sidenotes with CSS anchor positioning](https://vincent.bernat.ch/en/blog/2026-css-sidenotes)
- [Keepalived and unicast over multiple interfaces](https://vincent.bernat.ch/en/blog/2020-keepalived-unicast-vxlan)

## What this page adds to the wiki

The article is a concrete productization of self-hosted HTTP tunneling using only OpenSSH + nginx + Let's Encrypt + the `ngx_http_secure_link_module`. The genuinely reusable wiki-worthy idea is the **port-in-domain / hash-in-username** access-control pattern, which solves the bearer-in-URL problem cleanly: the hash lives in a case-preserving position (URL user field), the port lives in a case-insensitive position (subdomain), and the link is short-lived via the embedded timestamp.

This is closely related to:
- [[Concepts/live-asset-graph-blast-radius]] — both articles ask "how do I expose the minimum surface for a public service."
- [[Concepts/deterministic-hook-guardrails]] — the `secure_link` ternary in this article (empty / "0" / "1") is the same shape as a three-state hook return.

A future Concept write-up of the port-in-domain pattern would belong at `Concepts/ephemeral-port-in-subdomain-tunnel.md`.