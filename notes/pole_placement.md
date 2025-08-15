---
layout: default
title: Pole Placement
---
# Pole Placement
## Linear system
For the controllable linear system, 
$$
\dot{x} = Ax+Bu,
u=-Kx,
\dot{x}=(A-BK)x
$$, 

there's a trade off between convergence rate (eigenvalues or poles) and system jerkiness, ie, more negative real parts would lead to faster convergence to stability but sacrifice system response smoothness. Linear Quadratic Regulator (LQR) can be used to find optimal point.

---

### Poles to the far left of the complex plane:
Pro:
1. Faster Response
2. Increased stability margin

Cons:
1. Control effort becomes large. Actuators may saturate.
2. Sensitivity to Noise and model uncretainty. High gain feedback amplified measurement noise and unmodeled dynamics
3. Numerical instability
4. Reduced Robustness

---

## Linear Quadratic Regulator
### Formulation
Cost function $$J=\int_{0}^{\infty}(x^TQx + u^TRu)dt$$, where Q is positive semidefinite and x and u are dependet on t. There are **two** components of the cost:
1. first term penalizes difference between desired state and actual state, which accelerates convergence.
2. second term penalizes bigger u - for instance, gas may be expensive and the cost cannot be exorbitant.
The term **linear** refers to $$u=-Kx$$, which is a linear controller; **Quadratic** refers to the Cost function; **Regulator** means this stabilizes the system.
### Result
LQR gives u=-Kx specifically the K matrix that yields the best strategy.

## Linear Quadratic Estimator
The Kalman filter is an example of an LQE. More details are in State Estimation page.