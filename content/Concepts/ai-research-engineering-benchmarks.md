---
title: "AI Research and Engineering Benchmarks (PaperBench, RE-Bench, MLE-bench, KernelBench, CORE-Bench, ScienceAgentBench)"

details: "Weng's appendix enumerates six benchmarks used in harness-evolution research. PaperBench: replicate 20 ICML 2024 papers, 8,316 rubrics. CORE-Bench: 270 tasks for computational reproducibility across 90 papers. ScienceAgentBench: 102 tasks from 44 papers in math/chem/bio/geo. RE-Bench: 7 ML research-engineering environments, 71 8-hour human attempts; humans exceed agents at 8h and 32h, agents beat humans at 2h. MLE-bench: 75 Kaggle ML competitions; o1-preview + AIDE reached bronze-medal level in 16.9%. KernelBench: 250 PyTorch tasks for kernel correctness and speed, metric fast_p = % correct AND faster than baseline."
tags:
  - concepts
  - benchmark
  - evaluation
created: 2026-08-07
updated: 2026-08-07
type: concept
source: https://lilianweng.github.io/posts/2026-07-04-harness/
---

# AI Research and Engineering Benchmarks

**Source:** [[Raw/lilianweng-harness-engineering-2026-07-04]]
**Category:** Technical Reference
**Status:** Industry standard suite (as of mid-2026)

---

## Overview

Weng's appendix enumerates six benchmarks that are routinely used to evaluate coding agents and AI research automation systems. Each is a useful signal for a **different capability** — paper reproduction, ML research engineering, Kaggle-style competitions, GPU kernel generation, computational reproducibility, and data-driven scientific discovery. The set collectively forms a minimal suite for any harness-evolution experiment.

## Core Content

### Benchmark Reference

| Benchmark | Year | Tasks | Capability measured | Signal |
|-----------|------|-------|----------------------|--------|
| **PaperBench** | 2025 | 20 ICML 2024 Spotlight+Oral papers, 8,316 rubrics | Full paper reproduction from scratch | Long-horizon research execution |
| **CORE-Bench** | 2024 | 270 tasks, 90 papers (CS, social sci, medicine) | Computational reproducibility of published research | Strict verification, multiple difficulty levels |
| **ScienceAgentBench** | 2025 | 102 tasks, 44 peer-reviewed papers (math, chem, bio, geo) | Data-driven scientific discovery | Domain breadth, real published-task grounding |
| **RE-Bench** | 2025 | 7 ML research-engineering environments, 71 8h human attempts | Frontier ML R&D vs human experts | 2h vs 8h vs 32h scaling, return on longer budgets |
| **MLE-bench** | 2024 | 75 ML Kaggle competitions | ML engineering at scale | Public leaderboard as human baseline, contamination analysis |
| **KernelBench** | 2025 | 250 PyTorch tasks | GPU kernel correctness and speed | fast_p = % correct AND faster than baseline |

### When to Use Each

#### PaperBench (ICML 2025)

Replicating 20 ICML 2024 Spotlight+Oral papers from scratch, including understanding contributions, developing a codebase, and successfully executing experiments. 8,316 rubrics co-developed with paper authors. Best model at the time (`Claude 3.5 Sonnet`, ~21%) **does not outperform ML PhDs**. Includes PaperBench, PaperBench Code-Dev (lighter), and JudgeEval.

**Use for:** end-to-end research reproduction; the hardest known coding-agent benchmark.

#### CORE-Bench (TMLR 2024)

270 tasks based on 90 scientific papers across computer science, social science, and medicine. Tasks involve reproducing results from provided code and data. Multiple difficulty levels; language-only and vision-language tasks. Best reported agent at the time (`GPT-4o` and `GPT-4o-mini`) achieved only 21% accuracy on the hardest task.

**Use for:** evaluating reproducibility specifically; multi-domain signal.

#### ScienceAgentBench (ICLR 2025)

102 tasks from 44 peer-reviewed publications in four disciplines (math, chemistry, biology, geography). Covers data processing, model development, data analysis, and information visualization.

**Use for:** domain breadth; tasks grounded in real published research.

#### RE-Bench (ICML 2025)

7 challenging, open-ended ML research-engineering environments. Each environment = (scoring function, starting solution, reference solution); each can be run with 8 or fewer H100 GPUs. Examples: optimize a kernel, run a scaling-law experiment, fix an embedding, fine-tune GPT-2 for QA, etc. Includes data from 71 eight-hour attempts by 61 distinct human experts.

- Human experts achieved non-zero score in 82% of 8-hour attempts; 24% matched or exceeded strong reference solutions
- Best AI agents scored 4× higher than humans at a 2-hour budget, but humans had better returns to longer budgets and **exceeded agents at 8-hour and 32-hour settings**

**Use for:** head-to-head vs human experts; budget-scaling analysis.

#### MLE-bench (2024)

75 ML-engineering competitions curated from Kaggle. Tests training models, preparing datasets, running experiments, and submitting predictions to grading scripts. Uses Kaggle public leaderboards as human baselines. Best setup: `o1-preview` with AIDE scaffolding reached ≥ Kaggle bronze-medal level in 16.9% of competitions. Includes resource-scaling and contamination analyses.

**Use for:** standardized engineering-ability measurement; public-leaderboard comparison.

#### KernelBench (2025)

250 PyTorch tasks to evaluate whether LLMs can write fast and correct kernels. Metric `fast_p` = percentage of generated kernels that are correct and faster than baseline.

**Use for:** low-level performance optimization; the KernelBench signal correlates with downstream RL/serving efficiency.

### The RE-Bench Result Is the Most Important

The most actionable finding across this benchmark suite is the RE-Bench scaling result: **agents beat humans at 2-hour budgets; humans beat agents at 8-hour and 32-hour budgets**. This is direct evidence for bottleneck #6 in [[Concepts/open-rsi-bottlenecks]] — short-term rewards (a 2-hour eval) overstate agent capability, and the long-term factors humans contribute (maintainability, judgment, debugging discipline) only show up at longer budgets.

## Key Insights

1. **No single benchmark is sufficient.** Each measures a different capability. Use at least 2-3 from this set when comparing harnesses.
2. **The hardest signal is paper reproduction.** PaperBench at ~21% (Claude 3.5 Sonnet) is the headline number for "how far are we from automated research?"
3. **Budget-scaling is the key insight from RE-Bench.** Short-budget wins for agents hide long-budget wins for humans. A harness that scores well at 2h may not generalize to 8h+.
4. **fast_p captures correctness AND performance.** A "correct but slow" kernel doesn't pass. The dual metric catches overfitting to test cases.

## Related Concepts

- [[Concepts/open-rsi-bottlenecks]] — the broader challenges these benchmarks measure against
- [[Concepts/harness-as-runtime-os-analog]] — the OS analogy: a benchmark is the syscall contract
- [[Concepts/agentic-harness-engineering-ahe]] — AHE's Terminal-Bench-2 and SWE-bench-Verified transfer result
- [[Concepts/meta-harness-outer-loop]] — TerminalBench-2 is the canonical Meta-Harness benchmark

## References

- Raw Article: [[Raw/lilianweng-harness-engineering-2026-07-04]]
- Original: <https://lilianweng.github.io/posts/2026-07-04-harness/>
- Related Entities: [[Entities/paperbench]], [[Entities/core-bench]], [[Entities/scienceagentbench]], [[Entities/re-bench]], [[Entities/mle-bench]], [[Entities/kernelbench]]
