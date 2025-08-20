---
layout: default
title: Open loop vs closed loop control
---

# Categorizing controllers

## Classical (Transfer Function-Based) Controllers
1. PID - most common in industry, time/frequency-domain based.
    - Use when: 
        1. Plant dynamics are reasonable well-behaved (not too nonlinear not too fast) 
        2. No full state-space model (just input-output data)
        3. Need something simple, reliable, and easy to tune

2. Lead-Lag Compensators – designed using Bode/Nyquist plots.
    - Use when:
        1. You want to shape frequency response to improve stability margins or transient response
        2. You're working in frequency domain (Bode Nyuquist)

3. Notch filters -suppress certain frequencies.
   

## State-Space Controllers
1. LQR and LQI
     - Use when:
        1. You have a full state-space model (A, B matices)
        2. Need optimal trade-off between control effort and performance
        3. The system is **MIMO**

2. LQG - LQR + Kalman for output feedback
    - Use when:
        1. Same as LQR but not all states are measurable
        2. Need optimal performance with noisy *sensors*

3. Pole Placement - place closed-loop poles via state feedback
    - Use when:
        1. You want specific transient dynamics (settling time, damping, overshoot).
        2. Model is known in state-space form

4. MPC
    - Use when:
        1. Need to handle constraints (actuator limits, safety boundaries)
        2. Computational resources are available

## Adaptive & Nonlinear Controllers
1. Model Reference Adaptive Control (MRAC) – adapts gains in real time.
    - Use when: Plant dynamics **change over time** or are partially unknown
    
2. Sliding Mode Control - robust to disturbances, discontinuous control law
    - Use when: You need robustness against large uncertainties/disturbances

3. Feedback Linearization – cancels nonlinearities with nonlinear control law.
    - Use when: System is strongly nonlinear but exact model is known.

4. Backstepping - recursive Lyapunov-based design
    - Use when: dynamics are too complex or unkown for modeling

## Data-Driven Modern AI controllers
1. RL controllers -learn optimal policies from data
2. Neural network controllers

---

# Open Loop vs Closed Loop Control
Why feedback control?
1. Uncertainty (inherent in the system) in open loop system dynamics. Preplanned control inputs may fall flat against uncertainties.
2. Instability of the open loop system cann never be dealt with by open loop control. Feedback control allows us to directly change the dynamics of the system, inlcuding the eigenvalues of the system.
3. Disturbances (external forces) can be rejected by feedback.
4. Energy and efficiency.

---

## Fixing Instability with Pole Placement
$$
\dot{x}=Ax + Bu$$, $$y=Cx$$, let $$u=-Kx$$, $$\dot{x}=Ax-BKx=(A-BK)x
$$
<br>
We are able to change the actual dynamics of the system to stabilize it by selecting appropriate $$B*K$$.

---
## An Ideal Controller
1. design for stability
2. compensate for uncertainty
3. reject diturbance
4. attenduate noise

## Why is Open Loop Transfer Functions Important

1. **Closed-loop stability depends on open-loop behavior**
    - The closed-loop characteristic equation is:
    $$
    1+L(s)=0
    $$
    where $$L(s)$$ is the open-loop transfer function.

    - All the closed-loop poles (which determine stability) come from this equation.

    - If $$L(s)$$ has certain properties (like unstable poles or bad phase margins), the closed loop can become unstable.

2. Open Loop Transfer Functions reveal robustness by Sensitivity and Complementary Sensitivity
    - The closer the Open Loop Transfer Function L gets to -I, the bigger Sensitivity gets, and the less stable the system gets
