---
title: "Qwen3.7: The Agent Frontier"
detail: Today we introduce **Qwen3.7-Max**, our latest proprietary model designed for the agent era. Qwen3.7-Max is built to be a versatile agent foundatio...
details: Today we introduce **Qwen3.7-Max**, our latest proprietary model designed for the agent era. Qwen3.7-Max is built to be a versatile agent foundatio...
tags:
  - raw
created: 2026-06-04
updated: 2026-06-04
type: raw
source: "https://qwen.ai/blog?id=qwen3.7"
date: 2026-05-20
author: QwenTeam
---
# Qwen3.7: The Agent Frontier

Today we introduce **Qwen3.7-Max**, our latest proprietary model designed for the agent era. Qwen3.7-Max is built to be a versatile agent foundation — equally capable of writing and debugging code, automating office workflows, and sustaining autonomous execution across hundreds or thousands of steps.

What sets Qwen3.7-Max apart is the breadth and depth of its agent capabilities. It excels as a coding agent, from frontend prototyping to complex multi-file engineering. It serves as a reliable office and productivity assistant through MCP integrations and multi-agent orchestration. It sustains coherent reasoning across extremely long horizons — as demonstrated by a 35-hour, fully autonomous kernel optimization run comprising over 1,000 tool calls. It generalizes across agent scaffolds, performing consistently whether deployed through Claude Code, OpenClaw, Qwen Code, or other frameworks.

- **Qwen3.7-Max** — now available via [Alibaba Cloud Model Studio](https://modelstudio.console.alibabacloud.com):
  - frontier coding agent: from frontend prototyping to complex software engineering
  - office productivity and workflow automation via MCP and multi-agent orchestration
  - sustained autonomous execution across long-horizon tasks
  - cross-scaffold generalization across diverse agent frameworks
- Call via API on [Alibaba Cloud Model Studio](https://modelstudio.console.alibabacloud.com).

## Performance

| | Opus-4.6 Max | K2.6 Thinking | GLM-5.1 Thinking | DS-V4-Pro Max | Qwen3.6-Plus | Qwen3.7-Max |
|---|---|---|---|---|---|---|
| **Coding Agent** | | | | | | |
| Terminal Bench 2.0-Terminus | 65.4 | 66.7 | 63.5 | 67.9 | 61.6 | **69.7** |
| SWE-Verified | 80.8 | 80.2 | -- | 80.6 | 78.8 | 80.4 |
| SWE-Pro | 57.3 | 59.5 | 58.8 | 59.0 | 56.6 | **60.6** |
| SWE-Multilingual | 77.5 | 76.7 | -- | 76.2 | 73.8 | **78.3** |
| NL2repo | 47.6 | 42.8 | 41.0 | 35.5 | 34.4 | 47.2 |
| SciCode | 51.9 | 52.2 | 45.1 | -- | 41.4 | **53.5** |
| QwenWebDev | 1617 | -- | 1564 | 1570 | 1500 | 1568 |
| QwenSVG | 1541 | 1325 | 1605 | 1506 | 1432 | **1608** |
| **General Agent** | | | | | | |
| Qwenclaw | 65.5 | 54.7 | 58.7 | 59.2 | 57.2 | 64.3 |
| CoWorkBench | 68.2 | 58.2 | 66.0 | 66.3 | 64.5 | 67.2 |
| ClawEval | 70.4 | 61.5 | 62.7 | 58.4 | 57.1 | 65.2 |
| Skillsbench | -- | 56.2 | 53.1 | 52.3 | 45.7 | **59.2** |
| BFCL-V4 | 76.7 | 71.3 | 70.9 | 70.6 | 68.9 | 75.0 |
| MCP-Mark | 56.7 | 55.9 | 57.5 | 57.1 | 48.2 | **60.8** |
| MCP-Atlas | 75.8 | 66.6 | 71.8 | 73.6 | 74.1 | **76.4** |
| Vitabench | -- | 39.1 | 45.1 | 51.9 | 42.8 | 47.9 |
| SpreadSheetBench-v1 | 89.3 | 84.5 | 85.2 | 84.9 | 80.2 | 87.0 |
| Kernel Bench L3 | 2.63/98% | 1.41/80% | 2.00/78% | 1.07/54% | 1.03/48% | 1.98/96% |
| HLE w/ tools | 53.0 | 54.0 | 52.3 | 48.2 | 50.2 | **53.5** |
| QwenWorldBench | 56.1 | 50.9 | 50.2 | 52.3 | 47.6 | **57.3** |
| **STEM & Reasoning** | | | | | | |
| GPQA Diamond | 91.3 | 90.5 | 86.2 | 90.1 | 90.4 | **92.4** |
| HLE | 40.0 | 36.4 | 34.7 | 37.7 | 28.8 | **41.4** |
| LiveCodeBench | 88.8 | 89.6 | -- | 93.5 | 87.1 | 91.6 |
| HMMT 2026 Feb | 96.2 | 92.7 | 89.4 | 95.2 | 87.8 | **97.1** |
| IMOAnswerBench | 75.3 | 86.0 | 83.8 | 89.8 | 83.8 | **90.0** |
| CritPT | 12.6 | 8.0 | 4.6 | 12.9 | 2.9 | 11.4 |
| Apex | 34.5 | 24.0 | 11.5 | 38.3 | 8.8 | **44.5** |
| **General Capability** | | | | | | |
| MMLU-Pro | 89.7 | 87.1 | 86.3 | 87.5 | 88.5 | 89.6 |
| MMLU-Redux | 95.2 | 95.3 | 94.3 | 94.8 | 94.5 | 95.0 |
| SuperGPQA | 72.5 | 71.3 | 68.0 | 69.9 | 71.6 | **73.6** |
| IFEval | 91.9 | 94.5 | 94.5 | 91.9 | 94.3 | 94.3 |
| IFBench | 62.5 | 76.0 | 76.0 | 77.0 | 74.2 | **79.1** |
| MRCR-v2 128k | 84.0 | 63.1 | 62.0 | 74.4 | 85.9 | **90.4** |
| **Multilingualism** | | | | | | |
| WMT24++ | 82.7 | 81.6 | 81.8 | 82.2 | 84.3 | **85.8** |
| MAXIFE | 81.3 | 87.7 | 87.7 | 88.9 | 88.2 | **89.2** |
| MMMLU | 90.6 | 87.5 | 87.2 | 87.9 | 89.5 | 90.3 |
| MMLU-ProX | 86.1 | 83.7 | 83.9 | 83.9 | 84.7 | **87.0** |
| NOVA-63 | 59.1 | 56.7 | 54.6 | 52.8 | 57.9 | **59.0** |
| INCLUDE | 87.4 | 84.2 | 84.3 | 86.1 | 85.1 | 86.2 |
| Global PIQA | 91.2 | 89.2 | 89.5 | 90.5 | 89.8 | **91.4** |
| PolyMATH | 80.2 | 82.7 | 67.6 | 72.0 | 77.4 | **86.5** |

### Benchmark Notes

- Terminal-Bench 2.0: Harbor/Terminus-2 harness; 5h timeout, 12 CPU/24 GB RAM; temp=1.0, top_p=0.95, top_k=20, max_tokens=80K, 256K ctx; avg of 5 runs.
- SWE-Bench Series: Internal agent scaffold (bash + file-edit tools); temp=1.0, top_p=0.95, 200K context window.
- NL2Repo: Evaluated via Claude-code. Bash commands accessing specific repos disabled.
- QwenWebDev: Internal front-end code generation benchmark; bilingual (EN/CN), 7 categories; auto-render + multimodal judge.
- SkillsBench: Evaluated via OpenCode on 78 tasks; avg of 5 runs.
- MCP-Mark: GitHub MCP v0.30.3; Playwright responses truncated at 32K tokens.
- Kernel Bench L3: Median per-problem speedup over PyTorch eager / fraction faster than torch.compile, across 50 problems on H100 80GB.
- QwenWorldBench: Internal benchmark for LLMs as world models; 7 domains; open-ended 5-dim rubric judge.
- WMT24++: Harder WMT24 subset; avg scores on 55 langs via XCOMET-XXL.

### Performance Summary

In **coding agents**, Qwen3.7-Max performs strongly on SWE-Pro (60.6), SWE-Multilingual (78.3), SciCode (53.5), and QwenSVG (1608). On Terminal Bench 2.0-Terminus (69.7), it outperforms DS-V4-Pro Max (67.9). On SWE-Verified (80.4), it is on par with Opus-4.6 Max (80.8).

In **general-purpose agents**, improvements are even more pronounced. MCP-Mark (60.8 vs. GLM-5.1's 57.5), MCP-Atlas (76.4 vs. Opus-4.6's 75.8), Skillsbench (59.2 vs. K2.6's 56.2), and Kernel Bench L3 (1.98x median speedup, 96% win rate).

In **reasoning**, leading results on GPQA Diamond (92.4), HLE (41.4), HMMT 2026 Feb (97.1), IMOAnswerBench (90), and Apex (44.5).

In **general capabilities and multilingualism**, stands out on IFBench (79.1), WMT24++ (85.8), MAXIFE (89.2), SuperGPQA (73.6), and QwenWorldBench (57.3).

Notably, these scores are drawn from a wide variety of agent scaffolds. Qwen3.7-Max delivers consistently across Claude Code, OpenClaw, Qwen Code, and custom tool-use frameworks.

## Cowork Productivity Assistant

Qwen3.7-Max serves as an advanced coworker for real-world productivity. Its powerful agent capabilities streamline professional workflows — synthesizing complex information, performing in-depth data analysis and modeling, and generating publication-ready documents and visualizations — to reliably handle high-complexity enterprise workloads.

Features native compatibility with mainstream agent harnesses. For long-horizon tasks, supports autonomous planning and continuous execution across multi-hour sessions. Through thousands of tool calls and dozens of refinement iterations, it steadily improves output quality. Complex projects that typically require one to two weeks of specialized team effort can now be completed end-to-end within hours.

## Agent Scaling

Building on the environment scaling approach introduced in Qwen3.5, Qwen3.7 aggressively expands both the quality and diversity of agentic training environments. Just as language models generalize from diverse pretraining text, agentic capabilities generalize from diverse training environments.

This environment scaling produces a clear and consistent improvement trajectory, with Qwen3.7-Max achieving a top-3 average ranking that approaches Claude-4.6-Opus-Max. Crucially, all benchmarks feature entirely unseen, out-of-domain environments that were never present in training.

Performance gains across any subset of benchmarks are highly consistent and can reliably predict the relative gains on the remaining benchmarks, suggesting that environment scaling drives genuine capability generalization rather than benchmark-specific improvement.

## Cross-Harness Generalization

The Rollout environment infrastructure decouples each training instance into three orthogonal components — **Task**, **Harness**, and **Verifier** — that can be freely recombined. This decoupled design enables combinatorial scaling: the same task is paired with diverse harnesses and verifiers at minimal marginal cost.

More critically, it enables cross-harness and cross-verifier RL training, where the model encounters identical tasks under varying harness configurations, forcing it to learn generalizable problem-solving strategies rather than harness-specific shortcuts. Across QwenClawBench and CoWorkBench, Qwen3.7-Max delivers strong, consistent performance regardless of the harness used at evaluation time.

## Self-Evolving in the Wild

### Kernel Optimization Case Study

Extend Attention is a production-grade, variable-length multi-head attention operator in SGLang. The task: optimize this kernel on T-Head ZW-M890 PPUs — a hardware platform never seen during training. No prior profiling data, no hardware documentation, no example kernels.

Over ~35 hours of continuous autonomous execution, the model performed 432 kernel evaluations across 1,158 tool calls. It wrote, compiled, profiled, and iteratively improved the Extend Attention Kernel entirely on its own.

**Final result: 10.0x geometric mean speedup** over the Triton reference. The optimization trajectory shows sustained, non-trivial progress far beyond the first few hours: the model was still finding meaningful improvements after 30+ hours.

Comparison under identical conditions: GLM 5.1 reached 7.3x; Kimi K2.6 reached 5.0x; DeepSeek V4 Pro reached 3.3x; Qwen3.6-Plus reached 1.1x.

On KernelBench L3, Qwen3.7-Max produces accelerated kernels for 96% of scenarios (vs. 98% for Opus-4.6, 78% for GLM 5.1, 80% for Kimi K2.6, 54% for DeepSeek V4 Pro, 48% for Qwen3.6-Plus).

Key properties demonstrated:
- **Sustained long-horizon reasoning** — coherent optimization strategy across over a thousand tool calls
- **Strong in-context generalization** — competitive kernels for an architecture never encountered, relying on runtime feedback rather than memorized hardware knowledge

## Reward Hacking Monitoring for Long-Horizon Training

Qwen3.7-Max was integrated into RL monitoring for SWE tasks, building a framework for reward hacking self-monitoring and rule self-evolution. During RL experiments exceeding 80 hours, the model autonomously retrieved and replayed training trajectories, executing over 10,000 calls.

The system identified candidate hacking patterns (such as attempts to bypass constraints to access ground-truth answers on GitHub) while performing rule verification, counter-example mining, and iterative optimization.

Result: multiple rounds of rule self-evolution, adding 13 new heuristic rules and accurately flagging 1,618 hacking cases.

## Long-Horizon Planning and Execution in Startup Management

Within the Dynamic Cumulative Survival Games framework, temporal complexity of training tasks was scaled to reinforce long-horizon planning and execution capabilities.

In **YC-Bench** — a benchmark simulating a full year-long startup lifecycle — Qwen3.7-Max achieved total revenue of **2.08M USD**, which is:
- 2x the performance of Qwen3.6-Plus (1.05M USD)
- 5.9x that of Qwen3.5-Plus (352K USD)
- Successfully completed 237 tasks

The model demonstrated strategic evolution across context windows: actively explored potential clients, identified and blacklisted malicious traps, prioritized reliable revenue streams, and autonomously recovered from mid-term crises.

## Build with Qwen3.7

### API Usage

Qwen3.7-Max supports the `preserve_thinking` feature: preserving thinking content from all preceding turns in messages, recommended for agentic tasks.

Available via Alibaba Cloud Model Studio, supporting OpenAI-compatible chat completions and responses APIs, as well as an Anthropic-compatible API interface.

### Coding Assistant Integration

- **Claude Code**: Uses Anthropic API protocol with `ANTHROPIC_MODEL="qwen3.7-max"`
- **OpenClaw**: Connect via Model Studio with OpenAI-compatible config
- **Qwen Code**: Deeply optimized for the Qwen series via `npm install -g @qwen-code/qwen-code@latest`

## Citation

```bibtex
@misc{qwen37,
    title = {{Qwen3.7}: The Agent Frontier},
    url = {https://qwen.ai/blog?id=qwen3.7},
    author = {{Qwen Team}},
    month = {May},
    year = {2026}
}
```
