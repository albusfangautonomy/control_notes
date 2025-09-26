---
layout: default
title: Pole Placement and Optimal Control
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

# Linear Quadratic Regulator
## Formulation
Cost function $$J=\int_{0}^{\infty}(x^TQx + u^TRu)dt$$, where Q is positive semidefinite and x and u are dependet on t. There are **two** components of the cost:
1. first term penalizes difference between desired state and actual state, which accelerates convergence.
2. second term penalizes bigger u - for instance, gas may be expensive and the cost cannot be exorbitant.
The term **linear** refers to $$u=-Kx$$, which is a linear controller; **Quadratic** refers to the Cost function; **Regulator** means this stabilizes the system.

## Local stabilization of nonlinear systems (General Result)
Given the nonlinear auitonomous system $$\dot{\mathbf{x}} = f(\mathbf{x}, \mathbf{u})$$ and a stabilizable operating point, 
$$(\mathbf{x}_0, \mathbf{u}_0)$$ 
with 
$$f(\mathbf{x}_0,\mathbf{u}_0) = 0.$$

We can define a relative coordinate system 
$$\bar{\mathbf{x}} = \mathbf{x} - \mathbf{x}_0, \quad \bar{\mathbf{u}} = \mathbf{u} - \mathbf{u}_0.$$

Observe that 
$$\dot{\bar{\mathbf{x}}} = \dot{\mathbf{x}} = f(\mathbf{x}, \mathbf{u})$$ 
which we can approximate with a first-order Taylor series to

$$
\dot{\bar{\mathbf{x}}} \approx 
f(\mathbf{x}_0,\mathbf{u}_0) + 
\frac{\partial f(\mathbf{x}_0,\mathbf{u}_0)}{\partial \mathbf{x}}(\mathbf{x} - \mathbf{x}_0) + 
\frac{\partial f(\mathbf{x}_0,\mathbf{u}_0)}{\partial \mathbf{u}}(\mathbf{u} - \mathbf{u}_0) 
= A \bar{\mathbf{x}} + B \bar{\mathbf{u}}
$$

where $$A$$ and $$B$$ are the Jacobian matrices.

The resulting controller takes the form 
$$\bar{\mathbf{u}}^* = -K \bar{\mathbf{x}}$$

or

$$
\boxed{\mathbf{u}^* = \mathbf{u}_0 - K(\mathbf{x} - \mathbf{x}_0) = \mathbf{u}_0 - K*{\mathbf{e_state}}}
$$

---

# LQR example
## Cartpole
### Generlized coordinates
$$x$$ and $$theta$$, both scalars. $$\mathbf{q} = [x, \theta]^T$$. $$\dot{\mathbf{q}} = [\dot{x}, \dot{\theta}]^T$$

$$\mathbf{x} = [q, \dot{q}]^T$$, $$\mathbf{x_0} = [0, \pi, 0, 0 ]^T$$



## Linear Quadratic Estimator
The Kalman filter is an example of an LQE. More details are in State Estimation page.



---

## Bryson’s Rule for Initial $$ Q $$ and $$ R $$ in LQR

Bryson’s Rule is a practical heuristic for choosing initial values for the weighting matrices $$ Q $$ and $$ R $$ in LQR when you don’t yet have a fine-tuned cost function.

---

### **Rule**
The idea is to scale each state and input so that their **maximum acceptable excursion** corresponds to a cost of 1 in the LQR objective:

$$
Q_{ii} = \frac{1}{x_{i,\text{max}}^2}
$$
$$
R_{jj} = \frac{1}{u_{j,\text{max}}^2}
$$

Where:
- $$ x_{i,\text{max}} $$ = maximum tolerable value of state $$ i $$ (in magnitude)  
- $$ u_{j,\text{max}} $$ = maximum tolerable value of control input $$ j $$ (in magnitude)  

---

### **Procedure**
1. **Decide performance limits**
   - For each state $$ x_i $$, choose the largest magnitude you’re willing to allow.
   - For each control $$ u_j $$, choose the largest magnitude you can apply (actuator limit or desired bound).

2. **Build $$ Q $$**
   - Place $$ Q_{ii} = 1 / x_{i,\max}^2 $$ on the diagonal.  
   - If you want to weight some states more heavily, increase their $$ Q_{ii} $$.

3. **Build $$ R $$**
   - Place $$ R_{jj} = 1 / u_{j,\max}^2 $$ on the diagonal.  
   - Increasing $$ R_{jj} $$ penalizes control usage more.

4. **Run LQR**
   - Solve the algebraic Riccati equation for $$ K $$.
   - If the closed-loop behavior is too aggressive → increase $$ R $$.  
     If it’s too sluggish → decrease $$ R $$ or increase $$ Q $$.

---

### **Example**
Say you have a 2-state system: position $$ p $$ and velocity $$ v $$, and 1 control $$ u $$.  
- Max tolerable $$ p $$: 0.2 m  
- Max tolerable $$ v $$: 0.5 m/s  
- Max control $$ u $$: 2 N  

$$
Q = \begin{bmatrix}
1/(0.2)^2 & 0 \\
0 & 1/(0.5)^2
\end{bmatrix}
= \begin{bmatrix}
25 & 0 \\
0 & 4
\end{bmatrix}
$$

$$
R = [ 1/(2)^2 ] = [ 0.25 ]
$$

## Finite Horizon LQR
1. 