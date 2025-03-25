---
layout: page
permalink: /research/
title: research
nav: true
nav_order: 3
---
<details open="open">
  <summary>Projects</summary>
  <ol>
    <li>
      <a href="#coloring">Improving Bounds for Randomly Sampling Graph Colorings</a>
    </li>
    <li>
      <a href="#perturbations">Targeted Edge Perturbations on GNNs: Exploring Greedy, Heuristic, and Gradient-Driven Approaches</a>
    </li>
    <li>
      <a href="#grapheval">GraphEval2000: Benchmarking and Improving Large Language Models on Graph Datasets</a>
    </li>
  </ol>
</details>
<details open="open">
  <summary>Links</summary>
    <ol>
        <li>
            <a href="https://scholar.google.com/citations?user=ZmVqkdsAAAAJ&hl=en">Google Scholar</a>
        </li>
    </ol>
</details>

<!-- COLORINGS -->
## Improving Bounds for Randomly Sampling Graph Colorings
Undergraduate Senior Thesis (in progress).

<!-- PERTURBATIONS -->
## Targeted Edge Perturbations on GNNs: Exploring Greedy, Heuristic, and Gradient-Driven Approaches {#perturbations}
<!-- This year, I will be researching in the [Dynamic Networks: Analysis and Modeling Lab (Dynamo)](https://dynamo.cs.ucsb.edu/) under guidance from Dr. Ambuj Singh. 
Fortunately, this is through [UCSB's Early Research Scholars Program (ERSP)](https://ersp.cs.ucsb.edu/home).

### GitHub
See the repository [here](https://github.com/wrcorcoran/querying-graphs)!

### Project
Here is a broad description of this year's [research project](https://ersp.cs.ucsb.edu/2023-2024-projects/group-6-2023-2024):
- Graph neural networks transform the nodes of a graph into a high dimensional latent space.
- This project will contrast the distances between nodes of a graph in the input space (graph structure) to their embedding in the latent space.
- Queries of interest will be finding node/subgraph outliers, and comparing representations produced by different deep learning methods.
- Project can be extended to consider different ways of reducing distortions in embeddings and measuring the local dimensionality of the embedding space.

**Professor**: [Dr. Ambuj Singh](https://sites.cs.ucsb.edu/~ambuj/)

**Graduate Mentor**: [Danish Ebadulla](https://scholar.google.com/citations?user=LNzVTfcAAAAJ&hl=en)

**Other Teammates**: Wyatt Hamabe, Niyati Mummidivarapu

--- -->
### Spring
Here is an abstract for the final project:
> Graph neural networks (GNNs) have grown in application and research over the past decade in tandem with an investigation into adversarial attacks targeting GNNs. Most adversarial attacks proposed thus far fail to be realistic in practice, as they prioritize budget-based impact compared to inconspicuousness. Guided by consideration of the Minimum Edge Set Perturbation problem, we propose a set of edge perturbation methods that guarantee no change in accuracy while achieving a budgeted perturbation relative to the initial topological structure of the input graph. Alongside these methods, we present the Greedy-Primed Metattack, which achieves a similar reduction in accuracy as the vanilla Metattack while staying covert for more than 50% of the specified budget. The Greedy-Primed Metattack sparks inquiry into optimal heuristics for maximally furtive adversarial attacks while fueling further analysis of architectural robustness.

&nbsp;
Here is the final poster:
<object data="../assets/pdf/ERSP_Presentation.pdf" width="100%" height="650" type="application/pdf"></object>

---
### Winter

Please see the [research log](https://github.com/wrcorcoran/2324_TeamSingh_ERSP) for updates.

We have pivoted to the [*minimum edge set perturbation problem*](https://github.com/wrcorcoran/minimum-edge-set-perturbation). Here is the guiding question:

What is the maximum number of edges that can be added to a graph without changing the accuracy of a graph neural network classification? Are there certain metrics (homophily, degree, nearest neighbors), that provide an algorithmic way to add these edges? How does this compare to standard adversarial attacks?

---
### Fall

#### Research Proposal:
<object data="../assets/pdf/SinghProjectProposal-Final-Final.pdf" width="100%" height="1000" type='application/pdf'></object>

&nbsp;

#### Research Proposal Presentation:
<object data="../assets/pdf/FINALSLIDES_TEAMSINGH.pdf" width="100%" height="1000" type='application/pdf'></object>

---
<!-- GRAPHEVAL -->
## GraphEval36K: Benchmarking Coding and Reasoning Capabilities of Large Language Models on Graph Datasets
The following project was also completed in Professor Singh's [DYNAMO](https://dynamo.cs.ucsb.edu/) Lab.
### Abstract
>Large language models (LLMs) have achieved remarkable success in natural language processing (NLP), demonstrating significant capabilities in processing and understanding text data. However, recent studies have identified limitations in LLMs’ ability to manipulate, program, and reason about structured data, especially graphs. We introduce GraphEval36K1, the first comprehensive graph dataset, comprising 40 graph coding problems and 36,900 test cases to evaluate the ability of LLMs on graph problemsolving. Our dataset is categorized into eight primary and four sub-categories to ensure a thorough evaluation across different types of graphs. We benchmark ten LLMs, finding that private models outperform open-source ones, though the gap is narrowing. We also analyze the performance of LLMs across directed vs undirected graphs, different kinds of graph concepts, and network models. Furthermore, to improve the usability of our evaluation framework, we propose Structured Symbolic Decomposition (SSD), an instruction-based method designed to enhance LLM performance on complex graph tasks. Results show that SSD improves the average passing rate of GPT-4, GPT4o, Gemini-Pro and Claude-3-Sonnet by 8.38%, 6.78%, 29.28% and 25.28%, respectively.

### Paper
Here is a link to the paper: [click here](https://openreview.net/pdf?id=OhsAyUSK60).