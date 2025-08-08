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

Coming soon...
