# Full Dynamic Model of a Truck (Kodiak Interview Prep)

Understanding the full dynamic model of a truck is critical for interviews with autonomous trucking companies like **Kodiak**. Trucks have unique dynamics due to their size, mass distribution, and articulated trailer structure.

---

## 1. Basic Models (Used in Control & Estimation)

### A. Kinematic Bicycle Model

- Simplified model assuming **no slip**, **pure rolling**.
- State: $x, y, \theta, v$
- Control: $a, \delta$ (acceleration and steering angle)

$$
\dot{x} = v \cos\theta, \quad \dot{y} = v \sin\theta, \quad \dot{\theta} = \frac{v}{L} \tan\delta
$$

> Use case: **low-speed control and path planning**

---

### B. Dynamic Single-Track Model (No Trailer)

- Captures lateral slip, yaw dynamics, and tire forces.
- States: $x, y, \theta, v_x, v_y, r$
- Inputs: $F_x$, $\delta$

**Equations of motion:**

- **Longitudinal**:
  $$
  m(\dot{v}_x - v_y r) = F_{x,f} \cos\delta - F_{y,f} \sin\delta + F_{x,r}
  $$
- **Lateral**:
  $$
  m(\dot{v}_y + v_x r) = F_{x,f} \sin\delta + F_{y,f} \cos\delta + F_{y,r}
  $$
- **Yaw**:
  $$
  I_z \dot{r} = a F_{y,f} \cos\delta + a F_{x,f} \sin\delta - b F_{y,r}
  $$

Where:
- $a$, $b$: distances from CG to front/rear axle
- $F_{y,f}$, $F_{y,r}$: lateral tire forces from slip angles
- $F_{x,f}$, $F_{x,r}$: longitudinal tire forces

---

## 2. Truck-Specific Models

### C. Articulated Truck Model (Tractor + Trailer)

> **Essential for Kodiak!** Includes yaw dynamics and articulation between tractor and trailer.

Typical state vector:
$$
\mathbf{x} = [x, y, \psi_t, \psi_{tr}, v_x, v_y, r_t, r_{tr}]
$$

- $\psi_t$: yaw angle of tractor  
- $\psi_{tr}$: yaw angle of trailer  
- $r_t$, $r_{tr}$: yaw rates  
- **Articulation angle**: $\phi = \psi_{tr} - \psi_t$  
- **Articulation rate**: $\dot{\phi} = r_{tr} - r_t$

**Yaw Dynamics** (high-level):

- **Tractor**:
  $$
  I_{z,t} \dot{r}_t = \text{sum of moments on tractor}
  $$
- **Trailer**:
  $$
  I_{z,tr} \dot{r}_{tr} = \text{sum of moments on trailer}
  $$

> Used for high-speed motion, stability control, and trailer swing suppression.

---

## 3. Higher-Fidelity Models (for Simulation & MPC)

- **Pacejka "Magic Formula"** for nonlinear tire force modeling
- **Suspension & compliance** modeling
- **ABS/EBS braking system dynamics**
- **Multi-body** dynamics of each axle and articulation constraint

---

## Summary Table

| Model                        | Captures                  | Use Cases                                 |
|-----------------------------|---------------------------|--------------------------------------------|
| **Kinematic Bicycle**        | No dynamics or slip       | Path planning, low-speed control           |
| **Dynamic Single Track**     | Lateral slip, yaw         | Medium-speed control, stability analysis   |
| **Articulated Truck Model**  | Tractor-trailer coupling  | High-speed maneuvering, safety, control    |
| **Full Multi-Body Model**    | All dynamics              | Simulation, MPC, offline validation        |

---