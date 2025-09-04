---
layout: page
title: Passivity and Passive Control
---

# Passive System

In simple terms, a system is passive if increasing y (output) requires on average increasing u (input).

A passive system cannot produce energy on its own and can only disspate energy store in it initially.

## Passivity Theorem

Two passive systems in negative feedback produce a stable closed-loop system. Therefore, if your system is passive and you can design a passive controller, the stability of the system is guaranteed. This theorem is powerful for models with **high model uncertainties**.

An LQG system typically has positive feedback, so we need to make sure the negative of the system is passive.

### Passivity for Linear Systems
In frequency domain (positive real condition).

$$
G(j \omega) + G^H(j \omega) > 0, \forall \omega \in R
$$
where $$G^H$$ is the hermitian transpose.

For LTI SISO systems, this is saying $$Real(G(j \omega)) > 0$$ at all times. In Nyquist plot sense, the **Nyquist plot of $$G(j \omega)$$ lies on the right half plane entirely**.

## Matlab Example
[Matlab Passivity Example](https://www.mathworks.com/help/control/ug/vibration-control-in-flexible-beam.html)