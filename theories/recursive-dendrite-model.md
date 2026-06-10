## 🌳 Holistic Dendritic Re-arborization Simulator

This repository contains [a Python implementation](https://github.com/curiousquantumelephant777/Holistic-GDNF-Stimulation-ASD-Theory/blob/main/src/Dendrite-Tree-Coherence.py) that models dendritic re-arborization as a recursive function. This simulates how neural structures regenerate and reorganize, as well as prune. For instance, neural overpruning can occur in ASD and following certain environmental factors (e.g., cannabis overuse during adolescence), leading to less dendritic surface area. On the other hand, underpruning can occur in certain states (e.g., Williams Syndrome hyperarborization of Layer IV/V neurons). It is hypothesized that *GDNF* helps regrow neurons (especially following iboga) in this manner, especially dopaminergic and Layer IV/V neurons.
Using a recursive branching algorithm driven by trigonometric transformations, the script visualizes the structural plasticity of a neuron's dendritic tree.

## Mathematical & Algorithmic Foundation

The simulation relies on two core computational principles: Trigonometric Projection and Stochastic Recursion.

### 1. Spatial Projection via Trigonometric Pairs

Each new dendritic segment is calculated relative to its parent node $(x, y)$ using an orientation angle $\theta$ and a segment length $L$. The coordinates for the terminal node $(x_{\text{new}}, y_{\text{new}})$ are projected using the following system:

$$x_{\text{new}} = x + L \cdot \cos(\theta)$$

$$y_{\text{new}} = y + L \cdot \sin(\theta)$$

### 2. Recursive Branching & Morphological Decay

The framework models biological growth through a binary tree structure. At each recursive depth level ($d$), the algorithm simulates physical constraints by introducing an exponential decay to both segment length and line weight:

$$\text{Length}_{d} = \text{Length}_{d-1} \cdot 0.75$$

$$\text{Width}_{d} = d \cdot 0.5$$

### Stochastic Noise & Angular Spread

To mimic the organic, non-uniform navigation of growing axons through the extracellular matrix, a controlled chaotic variable (noise factor, $\eta$) introduces stochasticity into the branching angle:

$$\text{Spread} = 0.5 + (\mathbf{R} \cdot \eta)$$

Where $\mathbf{R} \sim \mathcal{U}(0, 1)$ is a uniformly distributed random float. The two daughter branches are then recursively generated at angles $\theta + \text{Spread}$ and $\theta - \text{Spread}$.

## 3. Simulating Neural States via Recursion Depth
The depth parameter acts as a proxy for the structural complexity and health of the neural network:Low Depth ($d = 5$) — Decoherent / Pruned State: Simulates a degenerate or heavily pruned neural environment. The recursion terminates early, yielding a sparse, stunted topology with low synaptic connectivity.High Depth ($d = 10$) — Hyper-Arborized / "Rebooted" State: Simulates the effects of neurotrophic factors like GDNF. The system undergoes an exponential burst of connectivity ($2^{10}$ or $1,024$ terminal segments), capturing a dense, youthful, and highly plastic "childlike" organizational state.
