---
layout: default
title: Open loop vs closed loop control
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
