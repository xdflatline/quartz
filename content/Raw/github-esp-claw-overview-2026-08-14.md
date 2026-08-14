---
title: "ESP-Claw — Espressif Chat Coding AI Agent Framework for IoT"
details: "Verbatim GitHub repository overview for espressif/esp-claw, a C-implemented agent runtime targeting ESP32-series chips that pairs an LLM agent loop with dynamic Lua scripting, MCP, and IM chat frontends. Retrieved 2026-08-14 from the GitHub repository landing page."
tags:
  - raw
  - github-readme
  - agent
  - agentic-system
created: 2026-08-14
updated: 2026-08-14
type: raw
source: "https://github.com/espressif/esp-claw"
---

# ESP-Claw 🦞 AI Agent Framework for IoT Devices

**Repository:** [espressif/esp-claw](https://github.com/espressif/esp-claw)
**Website:** [esp-claw.com](https://esp-claw.com/)
**License:** Apache-2.0
**Date Retrieved:** 2026-08-14

---

## Overview

ESP-Claw is Espressif's **Chat Coding AI agent framework for IoT devices**. It defines device behavior through conversation and completes the full loop of sensing, decision-making, and execution locally on Espressif chips. Inspired by the OpenClaw concept and reimplemented in C, ESP-Claw is lightweight, intelligent, and continuously evolving.

> *"With just an ESP32-series chip that costs only a few dollars, you can experience what makes ESP-Claw so nimble."*

### Tagline
**💬 Chat as Creation · 🚀 Millisecond Response · 🧩 Smart and Extensible · 😋 Grows with You**

## Repository Stats

| Metric | Value |
|--------|-------|
| ⭐ Stars | **2.0k** |
| 👁️ Watchers | **29** |
| 🔱 Forks | **418** |
| 📝 Commits | **753** |
| 👥 Contributors | **43** |
| 🏷️ Latest Release | v0.1.0 (Jun 12, 2026) |

## 🌟 Key Features

Traditional IoT usually stops at connectivity: devices can connect to the network, but they cannot think; they can execute commands, but they cannot make decisions. ESP-Claw brings the Agent Runtime down onto Espressif chips, turning them from passive executors into active decision-making centers.

| Feature | Description |
|---------|-------------|
| **💬 Chat as Creation** | IM chat + dynamic Lua loading; ordinary users can define device behavior without programming |
| **⚙️ Event Driven** | Any event can trigger the Agent Loop; response can be as fast as milliseconds |
| **🧬 Structured Memory** | Organize memories in a structured way; privacy stays off the cloud |
| **📤 MCP Communication** | Supports standard MCP devices; works as both Server and Client |
| **🧰 Ready Out of the Box** | Quick setup with Board Manager; supports one-click flashing |
| **🧩 Component Extensibility** | Every module can be trimmed as needed; you can add your own component integrations |

## 📦 Quick Start

ESP-Claw supports a wide range of development boards based on:
- **ESP32-S3**
- **ESP32-P4**
- **ESP32-C5**
- **ESP32-S31**

Including breadboards, M5Stack CoreS3, and others. Supported boards in [`./application/edge_agent/boards/`](https://github.com/espressif/esp-claw/blob/master/application/edge_agent/boards) can be **flashed online directly** via the browser — no local compilation required.

**Online Flashing:** [esp-claw.com/en/flash/](https://esp-claw.com/en/flash/)
**Local Build Docs:** [esp-claw.com/en/reference-project/build-from-source/](https://esp-claw.com/en/reference-project/build-from-source/)

## Supported Platforms

### LLM Support
ESP-Claw supports both **OpenAI-style** and **Anthropic-style** APIs. It natively supports:

| Provider | Models |
|----------|--------|
| OpenAI | GPT models |
| Alibaba Cloud Bailian | Qwen models |
| Anthropic | Claude models |
| DeepSeek | DeepSeek models |
| Custom | Custom endpoints |

> **💡 Tip:** ESP-Claw's self-programming capability depends on models with strong tool use and instruction-following ability. Recommended models: `gpt-5.4`, `qwen3.6-plus`, `claude4.6-sonnet`, `deepseek-v4-pro` or comparable capability.

### IM (Instant Messaging) Support
- Telegram
- QQ
- Feishu
- WeChat
- Extensible for additional platforms

## Repository Structure

```
.
├── .agents/                    # Agent configuration
├── .github/workflows/          # GitHub CI/CD
├── .gitlab/ci/                 # GitLab CI
├── application/                # Application code
├── components/                 # Reusable components
├── docs/                       # Documentation
├── pages/simulator/            # Web simulator (Lua LVGL)
├── tools/                      # Build/development tools
├── AGENTS.md                   # Agent instructions
├── CLAUDE.md                   # Claude AI instructions
├── CHANGELOG.md                # Version history
├── LICENSE                     # Apache-2.0
├── README.md / README_CN.md    # English/Chinese READMEs
└── .pre-commit-config.yaml
```

## Language Composition

| Language | Percentage |
|----------|------------|
| C | 83.9% |
| Lua | 5.8% |
| TypeScript | 5.7% |
| Python | 1.4% |
| CMake | 1.0% |
| C++ | 0.9% |
| Other | 1.3% |

## Development Plan

ESP-Claw is still under **active development**:
- Open an issue to report problems or request features
- Share ideas via [online survey (in Chinese)](https://fcn5wbhnyubf.feishu.cn/share/base/form/shrcndYcjbGFY1ymttTSyYoGIPh)
- View the [TODO List](https://fcn5wbhnyubf.feishu.cn/wiki/SRlgwWUYei4WmykU8uMcUtzTnFf?table=tblWSgzWcyW7jv7B&view=vewaP9B0KX) and vote for features to influence prioritization

## Acknowledgements

- Inspired by **[OpenClaw](https://github.com/openclaw/openclaw)**
- Agent Loop, IM communication, and related capabilities on ESP32 draw on **[MimiClaw](https://github.com/memovai/mimiclaw)**
