---
title: Qwen

details: Qwen (通义千问, Tongyi Qianwen) is a family of large language models developed by Alibaba's Tongyi Lab. The series spans multiple model sizes and speci...
tags:
  - entities
created: 2026-05-20
updated: 2026-06-04
type: entitie
confidence: high
---
## Overview

Qwen (通义千问, Tongyi Qianwen) is a family of large language models developed by Alibaba's Tongyi Lab. The series spans multiple model sizes and specialized variants, competing with GPT, Claude, and Gemini in both proprietary and open-weight segments. Available via [Alibaba Cloud Model Studio](https://modelstudio.console.alibabacloud.com).

## Model History

### Qwen3.7-Max (2026-05)

Latest flagship model, positioned as "The Agent Frontier" — designed for the agent era.

**Key capabilities:**
- Frontier coding agent: from frontend prototyping to complex multi-file software engineering
- Office productivity and workflow automation via MCP and multi-agent orchestration
- Sustained autonomous execution across long-horizon tasks (35-hour autonomous kernel optimization with 1,158 tool calls)
- Cross-scaffold generalization across diverse agent frameworks (Claude Code, OpenClaw, Qwen Code, custom scaffolds)

**Notable benchmarks:**
- Terminal Bench 2.0-Terminus: 69.7 (vs. Opus-4.6 Max 65.4, DS-V4-Pro Max 67.9)
- SWE-Pro: 60.6 (leading)
- GPQA Diamond: 92.4 (vs. Opus-4.6 91.3)
- HMMT 2026 Feb: 97.1 (vs. Opus-4.6 96.2)
- MCP-Mark: 60.8 (leading)
- Kernel Bench L3: 1.98x median speedup, 96% win rate

**Architecture highlights:**
- `preserve_thinking` feature for agentic tasks (preserves reasoning across turns)
- 1M token context window
- 65K max output tokens
- Supports both OpenAI-compatible and Anthropic-compatible API protocols

### Model Lineup

- Qwen series spans multiple sizes: 0.5B, 7B, 14B, 32B, 72B parameters
- Specialized variants: Qwen-Coder, Qwen-Math, Qwen-VL (vision-language)
- QwQ: deep thinking/reasoning variant
- Qwen-Omni: multimodal model

## Agent Architecture

### Environment Scaling

Building on Qwen3.5's approach, Qwen3.7 aggressively expands quality and diversity of agentic training environments. Agentic capabilities generalize from diverse training environments, analogous to how LLMs generalize from diverse pretraining text. Performance gains across benchmark subsets are highly consistent, suggesting genuine capability generalization rather than benchmark-specific improvement.

### Cross-Harness Generalization

Rollout infrastructure decouples training into three orthogonal components:
- **Task** — the problem to solve
- **Harness** — the agent scaffold (tool interface, execution environment)
- **Verifier** — correctness checking

This enables cross-harness RL training where the model learns generalizable problem-solving strategies rather than harness-specific shortcuts.

### Long-Horizon Autonomous Execution

Demonstrated capabilities:
- **Kernel optimization**: 35-hour autonomous run, 432 evaluations across 1,158 tool calls, achieving 10.0x speedup on unseen hardware (T-Head ZW-M890 PPUs)
- **Reward hacking monitoring**: 80+ hour RL monitoring, 10,000+ calls, 13 new heuristic rules, 1,618 hacking cases flagged
- **Startup simulation (YC-Bench)**: 2.08M USD revenue across 237 tasks in year-long lifecycle simulation

## Platform Capabilities

Qwen Studio offers:
- Chatbot interface with thinking/reasoning modes
- Image and video understanding
- Image generation
- Document processing
- Web search and MCP tool integrations
- Code agent capabilities (Qwen Code CLI)
- Multi-agent orchestration
- Robotics agent harness (Qwen-RobotClaw) and navigation model (Qwen-RobotNav)

## API Integration

Available via standard protocols:
- OpenAI-compatible chat completions API (DashScope endpoint)
- Anthropic-compatible API
- Direct integration with Claude Code, OpenClaw, and Qwen Code

## Position in AI Landscape

- Major Chinese model provider competing with Baidu, Tencent, and international models
- Strong presence in both open-weight and proprietary segments
- Available on HuggingFace, GitHub, and via local deployment (Ollama, LMStudio)
- Competes with [[anthropic|Anthropic]]'s Claude, [[openai|OpenAI]]'s GPT series, and Google's Gemini

## Related

- [[qwen-agent-capabilities|qwen-agent-capabilities]]
- [[ai-agents|ai-agents]]
- [[llm-architecture|llm-architecture]]
- [[tool-calling-llm|tool-calling-llm]]
- [[agent-self-improvement|agent-self-improvement]]