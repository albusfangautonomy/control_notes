---
layout: default
title: Robust Control
---
# Robust Control
## Motivation and Background
A paper by John Doyle proved that there is no guarantee on robustness of LQG scheme. This discovery pushed the industry towards robust control. We need to delve into Laplace domain and determine Robustness of a system. Laplace Transform domain gives us insights into the **performance, sensitivity, and robustness characteristics**.

## Three Equivalent Representations of Linear Systems
1. State space representation
    $$\dot{x}=Ax+Bu \\ y=Cx$$
2. Transfer functions
$$G(s)=C(sI-A)^{-1}B$$
3. Impulse response time domain
$$y(t)=\int_{0}^{t}h(t-\tau)u(\tau)d\tau $$ 
This is a convolution between impulse response and control input
**Note** there are different usages for each of the three representations. 1. If physics can be represented, State space representation can be very useful. Transfer functions can be useful for investigating robustness and performance


---

## Loop Transfer Function
