---
layout: page
title: Dynamic Programming
---

# Definitions.
1. Discrete states $$s_i \in S$$
2. Discrete action $$a_i \in A$$
3. Discrete time dynamics $$s[n+1]=f(s[n], a[n])$$
4. One-Step Cost $$l(s,a)$$ edge weight on the graph.
5. Total cost along trajectory $$\sum_{n=0}^{N} l(s[n], a[n])$$ (Additive cost)

Thanks to the Additive Cost, we can start from the goal and recursively solve for best action.

## One Step Cost J for Pendulum
1. minimum time (Bang-Bang control) 
$$
l(s,a) =
\begin{cases}
1, & \text{if } s \neq s_{\text{goal}} \\
0, & \text{if } s = s_{\text{goal}}
\end{cases}
$$

2. Quadratic Costs
$$ l(x,u) = x^T x + u^T u$$


# Cost-to-go (Value Function)
Optimal Cost-to-go:

$$
J^*(s) \;=\; \min_{a} \Big[ \, c(s,a) \;+\; \gamma \, \mathbb{E}_{s' \sim P(\cdot|s,a)} \big[ J^*(s') \big] \, \Big]
$$

$$
J^*(s_i) \;=\; \min_{\{a[0], \dots, a[N-1]\}} 
\;\; \sum_{n=0}^{N-1} l\!\big(s[n], a[n]\big)
\quad \text{s.t.} \quad  \\

s[0] = s_i, \;\;\\

s[n+1] = f\!\big(s[n], a[n]\big) \\
$$

## Bellman Equation - Solving Value Function Recursively 

$$
\forall i \quad J^*(s_i) \;\gets\; \min_{a \in \mathcal{A}} 
\Big[ \, \ell(s_i, a) \;+\; J^*\!\big(f(s_i, a)\big) \,\Big]
$$

