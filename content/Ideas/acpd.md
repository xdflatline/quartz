---
title: ACPd
---

ACPd is a daemon that connects to agents via the Agent Client Protocol (ACP) and serves as a standard interface for agent remote control through various transports.

## Architecture

Here is a block diagram illustrating how ACPd sits between various clients and target AI agents, managing connections, sessions, and dispatching commands over the standardized Agent Client Protocol (ACP):

```mermaid
graph TD
    %% Clients
    Client1[IDE Extension / VS Code] --> |WebSocket / gRPC| ACPd
    Client2[CLI Controller] --> |Local IPC / Unix Socket| ACPd
    Client3[Remote Gateway] --> |Secure HTTPS / TCP| ACPd

    subgraph ACPd [ACPd Daemon]
        direction TB
        Handlers[Connection Handlers] --> SessionManager[Session & Auth Manager]
        SessionManager --> Router[Command Router / Dispatcher]
    end

    %% AI Agents
    Router --> |ACP over stdio / Pipe| Agent1[Hermes Agent]
    Router --> |ACP over WebSocket| Agent2[Claude Code]
    Router --> |ACP over TCP| Agent3[Custom Coding Agent]

    classDef client fill:#3498db,stroke:#2980b9,color:#fff;
    classDef daemon fill:#2ecc71,stroke:#27ae60,color:#fff;
    classDef agent fill:#f1c40f,stroke:#f39c12,color:#333;

    class Client1,Client2,Client3 client;
    class Handlers,SessionManager,Router daemon;
    class Agent1,Agent2,Agent3 agent;
```

**Relevant Information/Docs:**
* https://agentclientprotocol.com
