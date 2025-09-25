---
layout: page
title: Euler-Lagrange Equations
---

## Partial Derivative Review

**Example 1**  
Let  
$
F(x, y, y') = 2x + xyy' + (y')^2 + y
$  

Then:  

$$
\frac{\partial F}{\partial y'} = xy + 2y'
$$  

$$
\frac{d}{dx} \left( \frac{\partial F}{\partial y'} \right) = y + xy' + 2y''
$$  

$$
\frac{\partial F}{\partial y} = xy' + 1
$$  

$$
\frac{\partial F}{\partial x} = 2 + yy'
$$  

$$
\frac{dF}{dx} = 2 + yy' + x(y')^2 + xy y'' + 2y'y'' + y'
$$  

and the Euler–Lagrange equation is:  

$$
y + xy' + 2y'' \;=\; xy' + 1 \quad
$$


**Warning 1**  

You might be wondering what
$$
\frac{\partial F}{\partial y'}
$$
is supposed to mean: how can we differentiate with respect to a derivative?  

Think of it like this: **F** is given to you as a function of three variables, say $$F(u, v, w)$$, and when we evaluate the functional $$I$$, we plug in $$x, y(x), y'(x)$$ for $$u, v, w$$ and then integrate. The derivative 
$$
\frac{\partial F}{\partial y'}
$$
is just the partial derivative of $$F$$ with respect to its third variable $$w$$. In other words, to find  
$$
\frac{\partial F}{\partial y'}
$$
just pretend $$y'$$ is a variable.  



Equally, there's an important difference between
$$
\frac{dF}{dx}
\quad \text{and} \quad
\frac{\partial F}{\partial x}.
$$

The former is the derivative of $$F$$ with respect to $$x$$, **taking into account** the fact that $$y = y(x)$$ and $$y' = y'(x)$$ are functions of $$x$$ too.  

The latter is the partial derivative of $$F$$ with respect to its first variable, so it's found by differentiating $$F$$ with respect to $$x$$ and pretending that $$y$$ and $$y'$$ are just variables and do not depend on $$x$$. Hopefully the example makes this clear.

# Euler-Lagrange Theorems

## Theorem 1
Let $$ C^k[a, b] $$ denote the set of continuous functions defined on the interval  
$$ a \leq x \leq b $$ which have their first $$ k $$-derivatives also continuous on $$ a \leq x \leq b $$.

If $$ I(y) $$ is an extremum of the functional  

$$
I(y) = \int_a^b F(x, y, y') \, dx
$$  

defined on all functions $$ y \in C^2[a, b] $$ such that $$ y(a) = A $$, $$ y(b) = B $$,  
then $$ Y(x) $$ satisfies the second-order ordinary differential equation  

$$
\frac{d}{dx} \left( \frac{\partial F}{\partial y'} \right) - \frac{\partial F}{\partial y} = 0. \tag{1}
$$  


## Definitions  
Equation (1) is the **Euler–Lagrange equation**, or sometimes just **Euler's equation**.

A solution of the Euler-Lagrange equation is called an extremal of the functional.2


---

## Explanation
### 1. What exactly is $$I(y)$$?
$$I(y)$$ is a **functional**.  
- A **function** takes numbers → numbers (e.g., $$f(x)=x^2$$).  
- A **functional** takes a *whole function* → a number.  

Here:  

$$
I(y) = \int_a^b F(x, y(x), y'(x)) \, dx
$$  

- You give it a *candidate function* $$y(x)$$.  
- It spits out a scalar (the value of the integral).  
- You then ask: which function $$y(x)$$ makes $$I(y)$$ extremal (minimized or maximized)?  

This is the variational problem.  




---

### 2. Why is this important? (Physics / First Principles)
In **modeling physical systems**, nature often picks the trajectory $$y(x)$$ that extremizes such a functional.  

- **Classical mechanics (Lagrangian mechanics):**  
  The functional is the **action integral**:  
  $$
  I[q] = \int_{t_0}^{t_1} L(q(t), \dot{q}(t), t) \, dt
  $$
  where $$q$$ is the generalized coordinate, and $$L = T - V$$ (kinetic – potential energy).  
  The extremum of this functional gives the **Euler–Lagrange equations**, i.e. Newton’s laws in disguised form.  

- **Optimal control:**  
  You choose $$F$$ to encode cost (fuel usage, error, energy, etc.), then extremizing $$I(y)$$ gives the optimal trajectory.  

- **Other examples:**  
  - Minimal surfaces (soap films): minimize area functional.  
  - Geodesics: shortest path between two points minimizes length functional.  

---

### 3. The link to **first principles modeling**
First principles = start with physics laws (energy, Newton’s 2nd law, conservation, etc.), not black-box data.  

- The **choice of $$F(x,y,y')$$** comes from those first principles.  
  - In mechanics, $$F$$ is the Lagrangian.  
  - In thermodynamics, $$F$$ might encode entropy/energy.  
  - In control, $$F$$ encodes cost or performance.  

- The fact that the true system trajectory satisfies the Euler–Lagrange equation is exactly what lets us *derive governing ODEs from physical principles*.  

So $$I(y)$$ is the mathematical wrapper, and “minimizing/extremizing it” is how first principles get translated into **differential equations describing system dynamics**.  

---

### In short
- $$I(y)$$ = a functional (integral of $$F$$) → extremized to find best/true trajectory.  
- First principles tell you the right $$F$$.  
- Solving Euler–Lagrange from $$I(y)$$ recovers the governing system equations.  

---

## Euler–Lagrange Equation for Manipulators

For a manipulator with generalized coordinates 
$$
q = [q_1, q_2, \dots, q_n]^T,
$$
and Lagrangian 
$$
L(q,\dot q) = T(q,\dot q) - V(q),
$$
the Euler–Lagrange equation is applied **separately to each generalized coordinate $$q_i$$:**

$$
\frac{d}{dt}\!\left(\frac{\partial L}{\partial \dot q_i}\right) - \frac{\partial L}{\partial q_i} = \tau_i + Q^{\text{nc}}_i,
\qquad i = 1,2,\dots,n.
$$

- $$ \tau_i $$: input torque/force applied at joint $$i$$  
- $$ Q^{\text{nc}}_i $$: non-conservative forces (e.g., friction) acting on coordinate $$i$$  

## Breaking Down Each Term

- $$\frac{\partial L}{\partial \dot{q}_i}$$: generalized momentum (linear/angular).
- $$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}_i}\right)$$: time derivative of momentum.
- $$\frac{\partial L}{\partial q_i}$$: generalized force from potential energy/geometry.
- $$Q_i$$: external generalized force (friction, actuation, etc.).

### Useful Formulae
1. Mass Matrix
$$
M_{ij}(q) = \frac{\partial^2 L}{\partial \dot{q}_i \, \partial \dot{q}_j}
$$

In python casadi,
```
M(q) = H = ca.jacobian(dLdqdot, dq)   # 2x2
```
where H is the **Hessian of the kinetic energy** wrt velocities.

2. Coriolis/Centrifugal (Christoffel form)
$$
C_{ijk}(q) = \tfrac{1}{2}\left(
\frac{\partial M_{ij}}{\partial q_k} +
\frac{\partial M_{ik}}{\partial q_j} -
\frac{\partial M_{jk}}{\partial q_i}
\right)
$$
and then
$$
(C(q,\dot{q})\dot{q})_i = \sum_{j,k} C_{ijk}(q) \, \dot{q}_j \, \dot{q}_k
$$

3. Gravity Vector
$$
G_i(q) = \frac{\partial V(q)}{\partial q_i}
$$
