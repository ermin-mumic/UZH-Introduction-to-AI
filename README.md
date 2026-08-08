[← Back to Profile](https://github.com/ermin-mumic)
# Introduction to Artificial Intelligence

A foundational course on the core ideas of AI, spanning intelligent agents, search and problem solving, probabilistic reasoning under uncertainty, natural language processing, supervised learning, and deep learning.

## Course Overview

This repository contains the weekly programming exercises from the Introduction to AI course at the University of Zurich (Spring Semester 2026). Artificial Intelligence is not just a buzzword: it is a research area whose origins trace back to the early decades of computing. After an overview of mathematical prerequisites and key concepts, the course covers problem solving, reasoning and planning, and reasoning under uncertainty, before turning to the basics of natural language processing, supervised learning, and deep learning.

**Grade: 6.0/6.0 | ECTS: 6**

## Topics Covered

- **Intelligent Agents**: PEAS descriptions, environment properties, and the agent taxonomy (reflex, model-based, learning agents)
- **Reinforcement Learning**: Q-learning, epsilon-greedy exploration, and hyperparameter sensitivity
- **Search**: Uninformed search (BFS, DFS, UCS) and heuristic search (Greedy, A\*, Weighted A\*)
- **Heuristic Properties**: Admissibility, consistency, goal-awareness, and safety
- **Bayesian Inference**: Maximum likelihood estimation, latent variable models, and conjugate priors
- **Expectation-Maximization**: Mixture models, responsibilities, and variational EM
- **Probabilistic Reasoning over Time**: Hidden Markov Models with filtering, prediction, and smoothing
- **Decision Theory**: Decision networks, maximum expected utility, and value of perfect information
- **Natural Language Processing**: N-gram language models, word embeddings, and self-attention
- **Supervised Learning**: Linear regression, train/test splits, underfitting and overfitting
- **Deep Learning**: Multilayer perceptrons, backpropagation, learning rates, dropout, and CNNs

## Repository Structure

```text

.
├── W2 - Introduction to Agents/
│   ├── IntroAI_week2_agents_exc.ipynb
│   └── agent_programs_task2.py
├── W3 - Solving Problems with Searching/
│   └── Exc03_search_task.ipynb
├── W6 - Bayesian Inference, Gaussian Mixture Models & EM/
│   └── benchmark_mixture_lab.ipynb
├── W7 - Probabilistic Reasoning over time/
│   ├── HMM_illustration.ipynb
│   └── decision_network_voi.ipynb
├── W9 - Language Models/
│   └── week_8_NLP_exercise.ipynb
├── W10 - Supervised Learning/
│   └── UZH_Intro_to_AI_supervised_learning.ipynb
├── W12 - Deep Learning/
│   └── deep_learning_exercise.ipynb
└── README.md

```

## Key Exercises

### Building Intelligent Agents (Week 2)

Three agent architectures implemented and compared head-to-head in a stochastic 4×4 GridWorld:

**Environment:**

- Start, goal (+10), trap (−5), and a tempting but suboptimal bait (+3)
- Step cost of −0.1 to encourage efficiency, walls blocking direct routes
- 15% slip probability: the agent moves in a random direction instead of the intended one

**Agents Implemented:**

1. **Simple Reflex Agent** — fixed condition-action rules, no internal state; gets stuck
2. **Model-Based Reflex Agent** — maintains an internal model of visited cells and detected walls
3. **Q-Learning Agent** — epsilon-greedy action selection with temporal-difference updates that improve through experience

**Experiments:**

- Effect of the exploration rate ε on learning curves
- Effect of the learning rate α on convergence speed and stability
- Visualization of the learned policy as arrows over the grid
- Final reward-curve comparison across all three agents

A separate `agent_programs_task2.py` implements a utility-based vacuum agent that chooses between *Suck* and *Move* by expected utility given the dirt probability of its location.

### Search Algorithm Comparison (Week 3)

A single generic priority-queue search driver instantiated as five algorithms on the same 10×8 grid, where only the priority function changes:

**Map Geometry (deliberately adversarial):**

- A dead-end "cup" trap between start and goal that lures greedy strategies
- A short top route through water (cost 5 per cell) and a longer, cheaper bottom route
- True optimal path cost: 15

**Results:**

| Algorithm | Nodes Expanded | Path Cost | Optimal? |
|---|---|---|---|
| BFS | 53 | 45 | No |
| DFS | 33 | 21 | No |
| UCS | 54 | 15 | Yes |
| Greedy | 28 | 45 | No |
| A\* | 35 | 15 | Yes |

**Key Findings:**

- BFS ignores terrain cost entirely and expands nearly the whole map
- Greedy is cheapest to run but routes straight through expensive water
- UCS is optimal but explores almost as much as BFS
- A\* achieves the optimal cost with nearly as few expansions as Greedy
- Weighted A\* ($f(n) = g(n) + w \cdot h(n)$) trades optimality for speed as $w$ grows, since inflating the heuristic breaks admissibility

### Bernoulli Mixtures: MLE → EM → Variational EM (Week 6)

Discovering latent question types from LLM benchmark results, framed as a Bernoulli mixture model over a binary matrix $\mathbf{X}$ (questions × models), where $x_{qm} = 1$ if model $m$ answered question $q$ correctly:

**Three Estimation Methods:**

1. **MLE** — types known, parameters obtained by counting and normalizing
2. **EM** — types latent; E-step computes responsibilities, M-step performs weighted counting
3. **Variational EM** — Beta and Dirichlet priors give posterior distributions over parameters instead of point estimates

**Implemented from Scratch:**

- E-step and M-step for the Bernoulli mixture, with log-sum-exp for numerical stability
- Marginal log-likelihood tracking to verify monotone convergence
- Cluster matching via permutation search to align discovered types with ground truth
- Variational E-step using expected log-parameters and pseudo-count updates

**Findings:**

- EM recovers the latent question types and per-type model accuracies from response patterns alone, with no labels
- Variational EM quantifies uncertainty: types with fewer assigned questions get visibly wider Beta posteriors
- Prior strength controls the regularization/shrinkage trade-off
- Applied to real MMLU-Pro evaluation data, the discovered clusters align with meaningful subject categories
- All updates are closed-form — no gradient descent anywhere, thanks to conjugacy

### Probabilistic Reasoning over Time (Week 7)

Two interactive notebooks on the classic umbrella/weather domain:

**Hidden Markov Models:**

- **Filtering** — forward algorithm for $P(X_t \mid e_{1:t})$
- **Prediction** — projecting the belief forward without new evidence, converging to the stationary distribution
- **Smoothing** — forward-backward algorithm for $P(X_k \mid e_{1:t})$ with $k < t$
- Every model parameter (prior, transition probabilities, sensor model) is exposed as an `ipywidgets` slider, so belief curves update live

**Decision Networks and Value of Information:**

- Maximum expected utility of *leave* vs. *take umbrella* under uncertainty
- MEU conditioned on a good or bad forecast
- Value of perfect information (VPI): how much the forecast is worth, and the conditions under which information changes the optimal action at all

### From Counting Words to Attention (Week 9)

A three-part progression tracing the path from n-gram models to transformers:

1. **Bigram Language Model** — building the count matrix, normalizing rows into $P(w_{t+1} \mid w_t)$, and sampling text; local coherence, global nonsense
2. **Word Embeddings** — cosine similarity implemented by hand, the `king − man + woman ≈ queen` analogy, and 2D projections of embedding space using pretrained gensim vectors
3. **Self-Attention from Scratch** — computing $Q$, $K$, $V$ from inputs, scaled dot-product scores, row-wise softmax, and the weighted sum of values, plus causal masking as a bonus

Each stage motivates the next: bigrams see one word of context, static embeddings ignore context entirely, and attention lets every token dynamically attend to every other.

### Supervised Learning (Week 10)

Linear regression built up from intuition to the bias-variance trade-off:

- Fitting a line by hand with interactive sliders for $w_0$ and $w_1$, minimizing mean squared loss
- Comparing hand-tuned parameters against the closed-form least-squares solution
- Train/test split (20/10 houses) to expose the gap between training and generalization error
- A nonlinear fertilizer-yield dataset where a straight line underfits
- Polynomial models of increasing complexity (degree 1, 3, 15) showing overfitting: training loss falls while test loss climbs

### Deep Learning (Week 12)

Training neural networks on FashionMNIST with PyTorch:

- **MLP from scratch** — configurable hidden layers, ReLU activations, optional dropout, trained with SGD and cross-entropy loss
- **Learning-rate experiment** — comparing lr ∈ {0.001, 0.1, 1.0} to see the three regimes: too slow, well-tuned, and divergent
- **Overfitting demonstration** — a deliberately tiny 500-sample subset makes the train/test loss gap unmistakable
- **Dropout as regularization** — the same architecture with dropout 0.5 visibly shrinks the generalization gap
- **CNN vs. MLP (bonus)** — a two-conv-layer CNN outperforms the MLP with roughly 5× fewer parameters; same backprop, same optimizer, different inductive bias

## Format

The exercises are implemented as:

- **Jupyter Notebooks**: One notebook per topic, combining derivations in LaTeX markdown with executable implementations
- **Interactive Widgets**: `ipywidgets` sliders for exploring parameter sensitivity in HMM, decision network, and regression exercises
- **Reproducible Results**: Fixed random seeds throughout so plots and metrics reproduce exactly
- **Standalone Script** (`agent_programs_task2.py`): Utility-based agent implementation outside of a notebook

## Technical Stack

- **Language**: Python 3
- **Scientific Computing**: NumPy, SciPy, pandas
- **Machine Learning**: scikit-learn, PyTorch, torchvision
- **NLP**: gensim (pretrained word embeddings)
- **Visualization**: matplotlib, ipywidgets
- **Environment**: Jupyter / Google Colab

## Key Learning Outcomes

- Map the agent taxonomy from theory onto working implementations and see where each architecture breaks down
- Implement and compare uninformed and heuristic search, and reason about admissibility and consistency
- Derive and implement EM from first principles, then extend it to a variational treatment with priors
- Perform exact inference in temporal models via filtering, prediction, and smoothing
- Quantify the value of information before deciding whether to acquire it
- Build the core components of modern NLP — n-grams, embeddings, attention — from scratch in NumPy
- Diagnose underfitting and overfitting from training and test curves rather than intuition
- Train neural networks in PyTorch and understand how learning rate, regularization, and architecture affect the outcome

## Highlights

The exercise set demonstrates:

- **From Scratch First**: Core algorithms (Q-learning, A\*, EM, self-attention, backprop-driven training loops) implemented directly rather than called from a library
- **Controlled Comparison**: Every topic pits alternatives against each other on identical inputs — three agents in one GridWorld, five search algorithms on one map, MLE vs. EM vs. variational EM, MLP vs. CNN
- **Adversarial Test Cases**: Environments designed so naive methods visibly fail (the search "cup" trap, the bait state, the 500-sample overfitting subset)
- **Interactivity**: Slider-driven notebooks turn parameter sensitivity into something you can watch rather than read about
- **Real Data**: The mixture-model lab moves from synthetic data to the actual MMLU-Pro benchmark results

## Running the Code

To reproduce the results:

1. Install dependencies: `pip install numpy scipy pandas matplotlib scikit-learn torch torchvision gensim ipywidgets`
2. Open any notebook in Jupyter or upload it to Google Colab
3. Run all cells top to bottom — datasets (FashionMNIST, MMLU-Pro, word embeddings) download automatically on first run
4. Adjust the interactive sliders and `# TRY IT` cells to explore parameter sensitivity

---

_Course instructor: Alberto Bacchelli and team_
