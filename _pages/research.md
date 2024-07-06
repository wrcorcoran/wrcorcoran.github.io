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

<!-- PERTURBATIONS -->
## Targeted Edge Perturbations on GNNs: Exploring Greedy, Heuristic, and Gradient-Driven Approaches {#perturbations}
This year, I will be researching in the [Dynamic Networks: Analysis and Modeling Lab (Dynamo)](https://dynamo.cs.ucsb.edu/) under guidance from Dr. Ambuj Singh. 
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

---
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
## GraphEval2000: Benchmarking and Improving Large Language Models on Graph Datasets {#grapheval}
The following project was also completed in Professor Singh's [DYNAMO](https://dynamo.cs.ucsb.edu/) Lab.
### Abstract
>Large language models (LLMs) have achieved remarkable success in natural language processing (NLP), demonstrating significant capabilities in processing and understanding text data. However, recent studies have identified limitations in LLMs' ability to reason about graph-structured data. To address this gap, we introduce GraphEval2000, the first comprehensive graph dataset, comprising 40 graph data structure problems along with 2000 test cases. Additionally, we introduce an evaluation framework based on GraphEval2000, designed to assess the graph reasoning abilities of LLMs through coding challenges. Our dataset categorizes test cases into four primary and four sub-categories, ensuring a comprehensive evaluation. We evaluate eight popular LLMs on GraphEval2000, revealing that LLMs exhibit a better understanding of directed graphs compared to undirected ones. While private LLMs consistently outperform open-source models, the performance gap is narrowing. Furthermore, to improve the usability of our evaluation framework, we propose Structured Symbolic Decomposition (SSD), an instruction-based method designed to enhance LLM performance on GraphEval2000. Results show that SSD improves the performance of GPT-3.5, GPT-4, and GPT-4o on complex graph problems, with an increase of 11.11%, 33.37%, and 33.37%, respectively.

### Paper
Here is a link to the paper: [click here](https://arxiv.org/abs/2406.16176).