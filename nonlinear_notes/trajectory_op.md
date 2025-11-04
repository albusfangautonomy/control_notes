---
layout: page
title: Trajectory Optimization
---

# Trajectory Optimization Formulation
Given a state space model, $$\dot{\mathbf{x}} = f(\mathbf{x},\mathbf{u})$$, an initial condition $$\mathbf{x_0}$$, and an input trajectory $$\mathbf{u}(t)$$, defined over a finite interval, $$ t\in[t_0, t_f] $$, we can simulate the dynamics forward to obtain $$\mathbf{x}(t)$$ over the same interval. We will define the long term (finite-horizon) cost of executing that trajectory using the standard additive cost optimal control objective.

$$
J_{\mathbf{u}(\cdot)}(\mathbf{x}_0) = \ell_f(\mathbf{x}(t_f)) + \int_{t_0}^{t_f} \ell(\mathbf{x}(t), \mathbf{u}(t)) dt
$$


$$\ell$$ is a terminal cost, evaluated at the end of the trajectory, which we did not have in the infinite time horizon formulations.

The trajectory optimization problem can be formulated as

$$
\min_{\mathbf{u}(\cdot)} \quad \ell_f (\mathbf{x}(t_f)) + \int_{t_0}^{t_f} \ell(\mathbf{x}(t), \mathbf{u}(t)) dt
$$

$$
\text{subjected to } \quad \dot{\mathbf{x}(t)} = f(\mathbf{x}(t), \mathbf{u}(t)), \forall t \in [t_0, t_f] 
$$

$$
\mathbf{x}(t_0) = \mathbf{x}_0
$$

These are the most common constraints 1. need to satisfy the **system dynamics** 2. Trajectory needs to be optimized for a **given initial state**. Other constraints can include control input limits (e.g. $$\mathbf{u}_{min} \leq \mathbf{u} \leq \mathbf{u}_{max}$$)

As written, the optimization above is an optimization over continuous trajectories. In order to formulate this as a numerical optimization, we must parameterize it with a finite set of numbers. Perhaps not surprisingly, there are many different ways to write down this parameterization, with a variety of different properties in terms of speed, robustness, and accuracy of the results.


# Convex Formulations for Linear Systems

## Direct Transcription
Core idea: use both $$u[\cdot]$$ and $$x[\cdot]$$ as decision variables for the optimizer.


## Direct Shooting