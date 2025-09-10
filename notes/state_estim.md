---
layout: default
title: State Estimation
---

# State Estimation
## Measurement Model
$$\dot{x}=Ax+Bu, y=Cx, x\in\mathbb{R^n}, y \in\mathbb{R^p}$$
## Observability
In simple terms, **observability** is if any state in x can be reproduced and deduced from measurements y(t)
## Observability Matrix
$$
\mathbb{O} = \begin{bmatrix}
C \\
CA \\
CA^2 \\
\vdots \\
CA^{n-1}
\end{bmatrix}
$$
This is a tall matrix and therefore its rank is the column rank.
**Note** that the C matrices are measurement matrices, not controllability matrices.
1. The system is observable if rank(O)=n.
2. The full state x can be estimated from y.
3. **Degrees of Observability** can be calculated from the **Observability Gramian** and the **SVD**

---

## Kalman Filter (Linear Quadratic Estimator)

### Key Assumption
Optimality of Kalman filtering assumes that errors have a normal (Gaussian) distribution. Regardless of Gaussianity, however, if the process and measurement covariances are known, then the Kalman filter is the best possible linear estimator in the minimum mean-square-error sense, although there may be better nonlinear estimators.


### System Dynamics and Measurement Model
$$
\mathbf{x}_{k} = \mathbf{F}_{k} \mathbf{x}_{k-1} + \mathbf{B}_{k} \mathbf{u}_{k} + \mathbf{w}_{k}
$$

where:

- $$\mathbf{F}_{k}$$ is the state transition model applied to the previous state $$\mathbf{x}_{k-1}$$.
- $$\mathbf{B}_{k}$$ is the control-input model applied to the control vector $$\mathbf{u}_{k}$$.
- $$\mathbf{w}_{k}$$ is the process noise, assumed to be drawn from a zero-mean multivariate normal distribution:
$$
\mathbf{w}_{k} \sim \mathcal{N}(0, \mathbf{Q}_{k})
$$
where $$\mathbf{Q}_{k}$$ is the process noise covariance.


### Predict

Predicted (a priori) state estimate:  
$$
\hat{\mathbf{x}}_{k|k-1} = \mathbf{F}_k \hat{\mathbf{x}}_{k-1|k-1} + \mathbf{B}_k \mathbf{u}_k
$$

Predicted (a priori) estimate covariance: \\
$$
\mathbf{P}_{k|k-1} = \mathbf{F}_k \mathbf{P}_{k-1|k-1} \mathbf{F}_k^{\mathsf{T}} + \mathbf{Q}_k
$$

---

### Update

Innovation or measurement pre-fit residual:   
$$
\tilde{\mathbf{y}}_k = \mathbf{z}_k - \mathbf{H}_k \hat{\mathbf{x}}_{k|k-1}
$$

Innovation (or pre-fit residual) covariance:  
$$
\mathbf{S}_k = \mathbf{H}_k \mathbf{P}_{k|k-1} \mathbf{H}_k^{\mathsf{T}} + \mathbf{R}_k
$$

Optimal Kalman gain:   
$$
\mathbf{K}_k = \mathbf{P}_{k|k-1} \mathbf{H}_k^{\mathsf{T}} \mathbf{S}_k^{-1}
$$

Updated (a posteriori) state estimate:  
$$
\hat{\mathbf{x}}_{k|k} = \hat{\mathbf{x}}_{k|k-1} + \mathbf{K}_k \tilde{\mathbf{y}}_k
$$

Updated (a posteriori) estimate covariance:  
$$
\mathbf{P}_{k|k} = \left( \mathbf{I} - \mathbf{K}_k \mathbf{H}_k \right) \mathbf{P}_{k|k-1}
$$

Measurement post-fit residual:  
$$
\tilde{\mathbf{y}}_{k|k} = \mathbf{z}_k - \mathbf{H}_k \hat{\mathbf{x}}_{k|k}
$$

---

### Notes
1. **Both Kalman Filter and LQR solve an algebraic Riccati Equation, yielding a closed-form solution**
2. The algebraic Riccati Equation for Kalman filter is very similar to that of LQR.
3. Kalman filter gain ($$K_{k}$$) is derived by minimizing the estimate coveriance matrix $$P_{k}$$

![A picture of estimator dynamical model](../figures/estimator.png)

Kalman is a **Full State Estimator** that measures full state $x(t)$ given the knowledge of the measurement $$y(t)$$ and control input $$u(t)$$. The eigenvalues of the Kalman filter signifies how fast estimates converge to the true state. Pole placement can be performed on Kalman to find the optimal eigenvalues. More aggressive poles means Kalman will be more susceptible to external noise.

### Kalman Cost Function
$$J= \mathbb{E}[(x-\hat{x})^T(x-\hat{x})]$$

### Measurement Noise
$$ \epsilon = x - \hat{x} \\ \dot{\epsilon}=(A-KC) \epsilon + w_{d} - Kw_{n}$$, where K is the Kalman gain and C is the measurement matrix, $$w_{d}$$ is the process noise from system dynamics and $$w_{n}$$ is the sensor noise

### Two Major noises
1. Model Noise $$w_{d}$$
2. Measurement Noise $$w_{n}$$
if one is high, trust the other more.
