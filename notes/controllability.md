---
layout: default
title: Controllability
---
# Equivalence
1. System is controllable
2. Arbitrary Eigenvalue (Pole) placement is allowed
    - $$u = -Kx => \dot{x} = (A-BK)x$$ 
3. Reachability (full in R^{n})
    - Theorectically one can drive from Massachusetts to California in a second
    - This can be proven by Cayley-Hamilton theorem


## Cayley-Hamilton Theorem
The characteristic polynomial of matrix $A$ is defined as:
$$
p_A(\lambda) = \det(\lambda I_n - A)
$$
Since this is a degree-$n$ monic polynomial, it can be written as:
$$
p_A(\lambda) = \lambda^n + c_{n-1} \lambda^{n-1} + \cdots + c_1 \lambda + c_0
$$
By replacing the scalar variable $\lambda$ with the matrix $A$, we define the matrix polynomial:
$$
p_A(A) = A^n + c_{n-1} A^{n-1} + \cdots + c_1 A + c_0 I_n
$$
# Controllability
## Stabilizability

Controllability for a large dimension space maybe too extreme and sometimes unrealistic. For this purpose, Stabilizability is defined as
**Stabilizability**
A system is stabilizable if and only if all unstable (or lightly damped) eigenvectors of A are in controlable subspace. (Anything unstable can be damped)

Actuator B should be designed so that the unstable dynamic direcitons correspond to the big singular vector of the controlability matrix.

## Controllability of Linear system
$$\dot{x}=Ax+Bu$$
$$y=Cx$$
This system is controllable if and only if the controllability matrix $$C=[B\ AB\ A^2B\ ...\ A^{n-1}B]$$ is of full column rank

**Note** This is a binary check. To see how controllable this system is, investigate the SVD of C.

## Degrees of Controllability
The Singular Value Decomposition (SVD) of the controllability matrix provides deep insight into the degree and direction of controllability of a linear system:
1. Controllability Rank
    If 𝐶 has full rank (i.e. rank = number of states 𝑛), the system is completely controllable.

    The number of nonzero singular values = the rank of 𝐶.

2. Strength of Controllability (Conditioning)
    The magnitude of the singular values tells you how "strongly" controllable the system is in different directions:

    Large singular values → easy to move the system in that direction.

    Tiny singular values → very difficult to control (require large input energy).

    Zero singular values → system not controllable in that direction.

3. Controllable Directions
    The right singular vectors V from $$𝐶 = 𝑈Σ𝑉^𝑇$$ span the input space.

    The left singular vectors 𝑈 represent orthogonal directions in the state space.

    Directions associated with large singular values in 𝑈 are the most controllable.
## Controllability Gramian
**The eigenvectors of the Gramian ($W_t$) that correspond to the biggest eigenvalues are the most controllable directions in state space. This is the same as the first column vector of the U matrix of the SVD of controllability matrix**
$$W_{t} \approx CC^T$$
The determinant of the Gramian indicates the volume of the ellipsoid and the **signal to noise ratio**
## PBH Test
(A,B) is controllable if and only if
$$
rank[(A-\lambda I)\ B] = n \forall \lambda \in \mathbb{C}
$$
1. $rank(A-\lambda I)=n$ except for eigenvalues $\lambda$
2. B needs to have some component in each eigenvector directions
3. (Advanced) a random vector B would make (A,B) controllably with high probability
## Reachability
In control theory, **reachability** describes whether it is possible to move a system from an initial state to a desired final state using admissible control inputs over a finite time interval.

For a continuous-time linear time-invariant (LTI) system described by:

$$
\dot{x}(t) = A x(t) + B u(t)
$$

where:
- $x(t) \in \mathbb{R}^n$ is the state vector,
- $u(t) \in \mathbb{R}^m$ is the control input,
- $A \in \mathbb{R}^{n \times n}$ is the system matrix,
- $B \in \mathbb{R}^{n \times m}$ is the input matrix,

the system is **reachable** if, for any initial state $x(0)$ and any final state $x_f$, there exists an input $u(t)$ that drives the system from $x(0)$ to $x_f$ in finite time.

### Reachability Matrix

The reachability of the system can be tested using the **reachability matrix**:

$$
\mathcal{R} = \begin{bmatrix} B & AB & A^2B & \cdots & A^{n-1}B \end{bmatrix}
$$

If $\mathcal{R}$ has **full rank** (i.e., $\text{rank}(\mathcal{R}) = n$), then the system is reachable
### 🎯 Reachability Set

The **reachability set** (or reachable set) at time $t_f$ is the set of all states that the system can reach from an initial state $x(0)$ under some admissible input $u(t)$ over the time interval $[0, t_f]$.

Formally, for a continuous-time LTI system:

$$
\dot{x}(t) = A x(t) + B u(t), \quad x(0) = 0
$$

the **reachability set** at time $t_f$ is defined as:

$$
\mathcal{R}(t_f) = \left\{ x(t_f) \in \mathbb{R}^n \;\middle|\; x(t_f) = \int_0^{t_f} e^{A(t_f - \tau)} B u(\tau) \, d\tau,\; u(\cdot) \in \mathcal{L}^2[0, t_f] \right\}
$$

This set contains all possible states the system can reach at time $t_f$ from the origin with square-integrable inputs $u(t)$.

If $\mathcal{R}(t_f)$ spans $\mathbb{R}^n$ for some finite $t_f$, the system is reachable.

For discrete-time systems:

$$
x[k+1] = A x[k] + B u[k], \quad x[0] = 0
$$

the reachability set after $N$ steps is:

$$
\mathcal{R}_d(N) = \left\{ x[N] = \sum_{i=0}^{N-1} A^i B u[N-1-i] \;\middle|\; u[i] \in \mathbb{R}^m \right\}
$$

The union of all such sets over all $t_f$ (or $N$ in discrete time) is the **total reachable set** from the origin.

