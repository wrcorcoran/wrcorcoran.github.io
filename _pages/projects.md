---
layout: page
permalink: /projects/
title: projects
nav: true
nav_order: 2
---

## table of contents

**personal**
- [LLM & LLM Serving](#llm-scratch) (Active)
- [Foundation Model for Prediction Markets](#foundation-model) (Active)
- [Linear Encoding of Code Quality in Large Language Models](#code-quality) (Apr–Jun 2026)
- [Distributed Data Centers](#distributed-data-centers) (Jan–Mar 2026)
- [Prediction Market Arbitrage System](#prediction-market) (Dec 2025–Jan 2026)
- [CXXGraph (open-source)](#cxxgraph) (Jul–Sep 2024)
- [FillerAI](#fillerai) (Sep–Dec 2023)
- [Verde](#verde) (Dec 2022–Mar 2023)

**academic**
- [Steering Graph Properties in Large Language Models](#steering-graphs) (2026)
- [AMeLIA: 2-Phase Adversarial Attack on GNNs](#amelia) (2024–2026)
- [Improving Bounds for Randomly Sampling Graph Colorings](#coloring) (2024–2025)
- [GraphEval36K: Benchmarking and Improving LLMs on Graph Datasets](#grapheval) (2024)
- [Targeted Edge Perturbations on GNNs](#perturbations) (2023–2024)

---

## personal

#### LLM & LLM Serving {#llm-scratch}
*Active*

During my last quarter at UCSB, I learned a lot about LLM Inference techniques. I decided that the best way to understand how LLMs work and are served is to implement one from scratch. I'm actively traveling, so development is slow, but I'm reading papers and writing code when I can. All code is written by hand (except for some scaffolding). Learning and planning is done in collaboration with Claude. 

**Links:** [GitHub](https://github.com/wrcorcoran/Mini-LLM)

{% assign _related = site.writing | where_exp: "item", "item.project contains 'llm-scratch'" | sort: "date" | reverse %}{% if _related.size > 0 %}
**Related writing:** {% for _p in _related %}[{{ _p.title }}]({{ _p.url }}){% unless forloop.last %} &middot; {% endunless %}{% endfor %}
{% endif %}

---

#### Foundation Model for Prediction Markets {#foundation-model}
*Active*

Working on a foundation model for prediction markets. Cannot share much outside of my writings... for obvious reasons.

I do not gamble! However, I have had a lifelong interest in financial markets and derivatives. Hence, I've grown to have an interest in prediction markets and their use as a financial tool. Though, most often, they are used as a gambling device.

{% assign _related = site.writing | where_exp: "item", "item.project contains 'foundation-model'" | sort: "date" | reverse %}{% if _related.size > 0 %}
**Related writing:** {% for _p in _related %}[{{ _p.title }}]({{ _p.url }}){% unless forloop.last %} &middot; {% endunless %}{% endfor %}
{% endif %}

---

#### Linear Encoding of Code Quality in Large Language Models {#code-quality}
*Apr–Jun 2026 — Course Project for CS 291A, UCSB*

We investigate whether code quality metrics are linearly encoded in the activation space of LLMs. Using Contrastive Activation Addition (CAA) and linear probes, we analyze three open-weight models across seven code quality metrics. Linear probes achieve R² ≥ 0.68 for four of the seven metrics, showing strong linear encodings across all three models. Steering vector analysis reveals that the Halstead metrics and Cyclomatic Complexity form a cluster, while Comment Ratio remains largely orthogonal. Steering Comment Ratio and Maintainability Index produces monotonic, controllable changes across most models and steering strengths, with minimal degradation in Pass@1 at moderate α — suggesting that LLMs implicitly learn linear representations of code quality and that steering vectors are a viable training-free mechanism for inference-time control.

**Links:** [Paper](../assets/pdf/wcorcoran-cs291a-code-quality-llm.pdf)

---

#### Distributed Data Centers {#distributed-data-centers}
*Jan–Mar 2026 — Python, RAFT, Two-Phase Commit (2PC)*

- Modeled 3 data centers each with 3 servers, responsible for handling financial transactions with strict consistency
and atomicity guarantees.
- Implemented an amalgamation of RAFT consensus and Two-Phase Commit (2PC) for fault-tolerant, atomic
distributed transactions.

**Links:** None... class project, thus, private.

---

#### Prediction Market Arbitrage System {#prediction-market}
*Dec 2025–Jan 2026 — Python, asyncio, WebSockets*

- Built a live cross-market arbitrage detection and automated trading system spanning Kalshi and Polymarket
prediction markets.
- Designed core infrastructure: WebSocket-based real-time market data ingestion, event-driven async strategy
orchestrator that dispatches trading strategies on incoming signals, and multi-platform order execution via Kalshi
and Polymarket APIs.
- Implemented robust failed-fill handling and concurrency management; system was previously deployed live.

**Links:** None... private for obvious reasons!

---
#### CXXGraph (open-source) {#cxxgraph}
*Jul–Sep 2024 — C++, Google Test, CMake*

- Implemented graph algorithms (adjacency and transition matrix powers) for popular header-only C++ library.

**Links:** [GitHub](https://github.com/wrcorcoran/CXXGraph) &middot; [Presentation](../assets/pdf/cxx-graph-presentation.pdf)

---
#### FillerAI {#fillerai}
*Sep–Dec 2023 — TypeScript, Next.js, GitHub Actions*

- Produced an AI player for a strategy game using Minimax with Alpha-Beta pruning algorithms to make quality moves.
- Formulated specific mathematically rigorous evaluation function to quantify board states for AI player.

**Links:** [Play!](https://wrcorcoran.github.io/FillerAI/) &middot; [GitHub](https://github.com/wrcorcoran/FillerAI)

---
#### Verde {#verde}
*Dec 2022–Mar 2023 — TypeScript, Firebase, React Native, Expo*

- Crafted a social media app, Verde, with daily environmentally-focused challenges along with photos and user
interaction.
- Contributed with a team of 3 others in an Agile development process using React Native, Expo, and Firebase.
- Awarded 1st place in UCSB’s Google Developers’ 2023 Solution Challenge.

**Links:** [GitHub](https://github.com/AjayLiu/verde)

---
## academic

#### Steering Graph Properties in Large Languages Models {#steering-graphs}
*2026 — Graduate Project with Professor Ambuj Singh*

this is the project i'm most passionate about, but cannot share much as it's currently under double-blind review. served as my "project" necessary for MS graduation.

in submission at NeurIPS '26. fine-tuned Llama on graph properties. looked at linear probes and steering vectors. 

similar to [code quality](#code-quality).

---
#### AMeLIA: 2-Phase Adversarial Attack on GNNs {#amelia}
*2024–2026 — with Professor Ambuj Singh*

likely in submission at ICLR '27. as i've graduated, i've stepped away from this project. we developed an adversarial attack framework capable of staying undetected for the first 50% of an adversarial attack while achieving the same degradation as full attacks. 

---

#### Improving Bounds for Randomly Sampling Graph Colorings {#coloring}
*2024–2025 — Undergraduate Senior Thesis with Professor Eric Vigoda*

Looked at the classic *Sampling for $k$-colorings problem*. Developed various variable length and layer coupling approaches with Markov chain Monte Carlo. Lots of linear and quadratic programming!

**Links:** [Poster (formatting is broken)](../assets/pdf/undergraduate-project.pdf)

---

#### GraphEval36K: Benchmarking and Improving Large Language Models on Graph Datasets {#grapheval}
*2024 — with Professor Ambuj Singh*

Large language models (LLMs) have achieved remarkable success in natural language processing (NLP), demonstrating significant capabilities in processing and understanding text data. However, recent studies have identified limitations in LLMs’ ability to manipulate, program, and reason about structured data, especially graphs. We introduce GraphEval36K, the first comprehensive graph dataset, comprising 40 graph coding problems and 36,900 test cases to evaluate the ability of LLMs on graph problem-solving. Our dataset is categorized into eight primary and four sub-categories to ensure a thorough evaluation across different types of graphs. We benchmark eight LLMs, finding that private models outperform open-source ones, though the gap is narrowing. We also analyze the performance of LLMs across directed vs undirected graphs, different kinds of graph concepts, and network models. Furthermore, to improve the usability of our evaluation framework, we propose Structured Symbolic Decomposition (SSD), an instruction-based method designed to enhance LLM performance on complex graph tasks. Results show that SSD improves the average passing rate of GPT-4, GPT-4o, Gemini-Pro and Claude-3-Sonnet by 8.38%, 6.78%, 29.28% and 25.28%, respectively.

**Links:** [Paper](https://aclanthology.org/2025.findings-naacl.452.pdf)

---

#### Targeted Edge Perturbations on GNNs: Exploring Greedy, Heuristic, and Gradient-Driven Approaches {#perturbations}
*2023–2024 — ERSP, with Professor Ambuj Singh*

We study the Minimum Edge Set Perturbation problem — maximizing edges added to a graph without changing GNN classification accuracy — and introduce the Greedy-Primed Metattack, which achieves comparable accuracy reduction to vanilla Metattack while remaining covert for over 50% of the specified budget.

**Links:** [Research Log](https://github.com/wrcorcoran/2324_TeamSingh_ERSP) &middot; [Code](https://github.com/wrcorcoran/minimum-edge-set-perturbation) &middot; [Poster](../assets/pdf/ERSP_Presentation.pdf) &middot; [Proposal](../assets/pdf/SinghProjectProposal-Final-Final.pdf)
