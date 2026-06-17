---
title: Copyfail Pod To Host Kubernetes Vuln 2026 05 21
detail: From Pod to Host. - Xint
details: From Pod to Host. - Xint
tags:
  - raw
created: 2026-05-21
updated: 2026-05-21
type: raw
---
Copy Fail:
From Pod to Host. - Xint

Copy Fail:
From Pod to Host. - Xint

|

Blog

Subscribe

Search posts...

 Vulnerability Research

AI for Security

Open Source Projects

Copy Fail:
From Pod to Host.

A walkthrough of Copy Fail (CVE-2026-31431) as a container escape primitive: from a 4-byte page cache write to host root on Kubernetes.

Juno Im

May 19, 2026

Contents

Why the Page Cache Crosses Container Boundaries

Scenario 1: Cross-Container Poisoning

1-1: Compromised pod sharing a base layer

1-2: Pod creation rights

Scenario 2: Container Escape

Detection and Mitigation

Community PoCs

Two weeks ago, we disclosed 

Copy Fail

, a new and exceptionally dangerous Linux local-privilege escalation vulnerability.&nbsp;

Copy Fail exploits a kernel memory corruption flaw without injecting code into a running kernel, which makes it small and unusually portable. Copy Fail gives attackers a repeatable, controlled 4-byte write into the Linux page cache backing any readable file; in other words, it allows attackers to rewrite the cached contents of files on a Linux filesystem.&nbsp;

To help operators determine their susceptibility to Copy Fail, we published a proof-of-concept exploit and a model attack path. Our model attack targets the 

su

 binary present on most Linux systems. Because 

su

 is setuid root, an attacker who can rewrite it and then execute it can escalate to root. Instead of having it ask for and check a root password, the rewritten 

su

 skips the paperwork and drops the caller straight into a root shell.

Our proof-of-concept led some to believe that rewriting setuid binaries like 

su

 was the extent of the attack. Not so! The capability that Copy Fail and related page cache writing exploits extend to attackers is powerful and versatile. As an example, let’s walk through how to use it to break out of a namespaced container.

To understand this new exploit pattern, you have to understand a little bit about what’s happening under the hood in Copy Fail.&nbsp;

Copy Fail works by confusing the kernel code that handles IPSec ESP Extended Sequence Numbers (

authencesn

). This code is exposed to unprivileged users via 

AF_ALG

 sockets, which are userland’s interface to Linux’s kernel cryptography subsystem.&nbsp;

Specifically, Copy Fail sets the 

authencesn

 code up to think it’s looking at disposable scratch memory when it’s really handling a mutable reference to the page cache. It tells the kernel’s cryptography code to decrypt a ciphertext blob, using bytes supplied by a zero-length copy from a pipe using 

splice(2)

.&nbsp;

Because the wire format for IPSec ESNs isn’t the implicit format the crypto code operates on, the 

authencesn

 code shuffles sequence numbers around. But the code isn’t handling a disposable buffer from a packet; Copy Fail has tricked it into operating on a reference to a cached file.&nbsp;

Cross-container kernel attacks usually corrupt kernel memory: race windows, UAFs, version-bound payloads. These primitives are powerful, as t

...
