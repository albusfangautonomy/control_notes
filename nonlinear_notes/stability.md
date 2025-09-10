---
layout: default
title: Lyapunov Stability
---

# Lyapunov Stability

## Intuitive Summary of Stability in the Sense of Lyapunov (isL)

1. Stable isL

## Setup
Consider an **autonomous** system
$$
\dot x = f(x),\quad x\in\mathbb{R}^n,
$$
and a scalar candidate $$V:\mathbb{R}^n\to\mathbb{R}$$ (no explicit time dependence).

---

## Chain rule along trajectories
Let $$x(t)$$ be a trajectory of $$\dot x=f(x)$$. Since $$V=V(x)$$ has no explicit $$t$$,
$$
\frac{d}{dt}V\big(x(t)\big)
= \nabla V(x)^\top \dot x
= \nabla V(x)^\top f(x).
$$

---

## Lie derivative
The **Lie derivative** of $$V$$ along $$f$$ is the directional derivative
$$
\mathcal{L}_f V(x) \; =  \nabla V(x)^\top f(x).
$$
Hence, along solutions,
$$
\boxed{\ \dot V(x) \equiv \frac{d}{dt}V(x(t)) = \mathcal{L}_f V(x)\ }.
$$

---

## Lyapunov stability (equilibrium at the origin)
Assume $$x^\star=0$$ is an equilibrium: $$f(0)=0$$. Let $$\alpha_i$$ be class-$$\mathcal{K}_\infty$$ functions.

### Stability (Lyapunov)
If there exists $$V:\mathbb{R}^n\to\mathbb{R}_{\ge 0}$$ and $$\alpha_1,\alpha_2\in\mathcal{K}_\infty$$ such that, in a neighborhood of $$0$$,
$$
\alpha_1(\|x\|)\le V(x)\le \alpha_2(\|x\|),\quad
\dot V(x)=\mathcal{L}_f V(x)\le 0,
$$
then $$x=0$$ is **stable**.

### Asymptotic stability
If, in addition, there exists $$\alpha_3\in\mathcal{K}_\infty$$ with
$$
\dot V(x)=\mathcal{L}_f V(x)\le -\,\alpha_3(\|x\|)\quad(\text{for }x\neq 0),
$$
then $$x=0$$ is **asymptotically stable**.

### Exponential stability (sufficient condition)
If there exist $$c>0$$ and $$\alpha_1,\alpha_2\in\mathcal{K}_\infty$$ such that
$$
\alpha_1(\|x\|)\le V(x)\le \alpha_2(\|x\|),\quad
\dot V(x)\le -\,c\,V(x),
$$
then $$x=0$$ is **(locally) exponentially stable**.

### Global versions
If the above properties hold for all $$x\in\mathbb{R}^n$$ and $$V$$ is **radially unbounded**
($$V(x)\to\infty$$ as $$\|x\|\to\infty$$),
then the corresponding stability property is **global**.

### LaSalle’s invariance principle (autonomous)
If $$V$$ is positive definite and $$\dot V(x)=\mathcal{L}_f V(x)\le 0$$,
then every trajectory approaches the largest invariant set contained in
$$
\mathcal{S} \;=\; \{\,x:\ \mathcal{L}_f V(x)=0\,\}.
$$
If the only invariant set in $$\mathcal{S}$$ is $$\{0\}$$, then the origin is **asymptotically stable**.

---

## Quick checklist
- $$V(0)=0$$, $$V(x)>0$$ for $$x\neq 0$$ (positive definite); preferably radially unbounded.
- Compute $$\dot V=\mathcal{L}_f V=\nabla V^\top f$$.
- Aim for $$\dot V\le 0$$ (stability), $$\dot V<0$$ or LaSalle conditions (asymptotic), or $$\dot V\le -cV$$ (exponential).
