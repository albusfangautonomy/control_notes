---
layout: default
title: PID Control
---

# PID Control

## Which controller to use?
$$
\begin{array}{c|c|c|c}
Example & System Order & Controller & Reasoning\\
\hline
\text{Controlling mass position using force} & 2 & \text{PD or PID} & \text{Typically needs damping like mass-spring damper, otherwise will oscillate} \\
\text{Controlling V across C using current} & 1 & \text{P or PI} & \text{not much danger of over-shoot or oscillation}  \\
\text{Controlling I across R using voltage} & 0 & \text{P or PI} & \text{not much danger, direct mapping}
\end{array}
$$

**Note** System order denotes how many 'integration' away is your control input from output. For instance controlling position with force would be a second order system.
## PI vs PD vs PID
The derivative controller is highly sensitive to noise and may throw system into instability.

### PI controller
PI controller reduces both rise time and the steady state errors of the system. Integral term introduces phase lag, which may slow down response time.

### PD controller
A PD controller reduces transients like rise time, overshoot, and oscillations in the output. D controller cannot exist on its own since itself doesn't stabilize the system, but amplifies noise.

---

## Strategies for Tuning a PID Controller

### Manual PID Tuning Strategy

1. **Start with:**

$$
K_P > 0, \quad K_I = 0, \quad K_D = 0
$$

2. **Increase $$ K_P $$** until:
   - The system starts responding to setpoint changes.
   - It begins to **oscillate consistently without settling**.

   This means it's reached the **edge of stability**.

3. **Back off $$ K_P $$** by ~10–20% to get a stable (but responsive) system.

4. **Increase $$ K_D $$** to:
   - Dampen the oscillations.
   - Improve settling time and reduce overshoot.

5. **Increase $$ K_I $$** slowly to:
   - Eliminate steady-state error (e.g. small drift from setpoint).
   - Watch for **overshoot or oscillation** due to **integral windup**.

---

## 🧪 Ziegler–Nichols Method (Ultimate Gain Method)

This is a classical tuning rule. It gives you a starting point for 
$$
K_P,\ K_I,\ \text{and}\ K_D
$$
based on when the system first starts oscillating.

### 🔧 Steps:

1. **Set:**
$$
K_I = 0,\quad K_D = 0
$$

2. **Increase $$ K_P $$** until the system output shows **sustained oscillations** (constant amplitude).

   - That value of $$ K_P $$ is called the **ultimate gain**, denoted:
$$
K_u
$$

3. **Measure the oscillation period** — the time between peaks — and call it:
$$
T_u
$$

---

### 📐 Use these tables to compute gains:

| Controller | $$ K_P $$         | $$ K_I $$                  | $$ K_D $$             |
|------------|-------------------|----------------------------|-----------------------|
| **P**      | $$ 0.5K_u $$      | –                          | –                     |
| **PI**     | $$ 0.45K_u $$     | $$ 1.2K_u / T_u $$         | –                     |
| **PID**    | $$ 0.6K_u $$      | $$ 2K_u / T_u $$           | $$ K_u T_u / 8 $$     |

---

| Control Type           | $$K_p$$        | $$T_i$$            | $$T_d$$            | $$K_i$$                 | $$K_d$$                 |
|------------------------|----------------|---------------------|---------------------|--------------------------|--------------------------|
| **P**                  | $$0.5K_u$$     | –                   | –                   | –                        | –                        |
| **PI**                 | $$0.45K_u$$    | $$0.8\overline{3}T_u$$ | –                   | $$0.54K_u / T_u$$        | –                        |
| **PD**                 | $$0.8K_u$$     | –                   | $$0.125T_u$$        | –                        | $$0.10K_u T_u$$          |
| **Classic PID**        | $$0.6K_u$$     | $$0.5T_u$$          | $$0.125T_u$$        | $$1.2K_u / T_u$$         | $$0.075K_u T_u$$         |
| **Pessen Integral Rule** | $$0.7K_u$$   | $$0.4T_u$$          | $$0.15T_u$$         | $$1.75K_u / T_u$$        | $$0.105K_u T_u$$         |
| **Some Overshoot**     | $$0.3\overline{3}K_u$$ | $$0.50T_u$$ | $$0.3\overline{3}T_u$$ | $$0.6\overline{6}K_u / T_u$$ | $$0.1\overline{1}K_u T_u$$ |
| **No Overshoot**       | $$0.20K_u$$    | $$0.50T_u$$         | $$0.3\overline{3}T_u$$ | $$0.40K_u / T_u$$        | $$0.06\overline{6}K_u T_u$$ |

---

---

### ⚠️ Notes for Drone Applications

- Ziegler–Nichols gives **aggressive** tuning, often with **overshoot**.
- For drones, it's safer to:
  - Start with **rate control loops** (angular velocity).
  - Then move to **attitude control** (roll, pitch, yaw).


Coming soon...
