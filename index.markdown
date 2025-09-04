---
layout: default
title: Control Notes
---

# 🧠 Control Notes

Welcome to my personal collection of control systems notes. This site compiles essential topics, explanations, and formulas for quick reference and deeper learning.

## 📚 Core Topics

### Linear Control

- [Useful Tips](./notes/tips.html) \\
  Important Intuitions for designing control systems.

- [Overview](./notes/overview.html)\\
  A comparison between Open Loop control and Closed Loop control, and categorizing controllers.

- [Design Workflow](./notes/workflow.html) \\
  Typical design requirements and design actions.

- [Plot Reviews](./notes/important_plots.html)\\
  Review Nichols Chart, Nyquist Plot, Bode Plot, and Root Locus Plot.

- [Performance Specifications](./notes/performance_specs.html)  \\
  Rise time, settling time, overshoot, **Steady-State Error** (error constants, system type, examples).

- [System ID](./notes/system_id.html) \\
  Linear, Nonlinear, Online and recursive system identification.

- [Stability Analysis](./notes/stability.html)  \\
  Routh-Hurwitz, Nyquist, Lyapunov methods and practical insights.

- [Sensor Fusion](./notes/senser_fusion.html) \\
  Common Sensor Fusion algorithms.

- [PID Control](./notes/pid.html)  \\
  Overview of Proportional-Integral-Derivative control, tuning methods, use cases.

- [Lead, Lag, and Lead-Lag Compensators](./notes/compensators)  \\
  Frequency domain intuition, Bode plot effects, stability and performance improvement.

- [Root Locus Analysis](./notes/root-locus.html)  
  Pole-zero placement and visualizing the impact of controller design.

- [Optimal Pole Placement in Linear Systems](./notes/pole_placement) \\
  Introduces LQR and pole placement.

- [State Observers](./notes/state_estim.html)   
  Linear quadratic Estimator and Observability.

- [Controllability and Reachability](./notes/controllability.html)   \\
  Illustrates the equivalence between controllability and reachability.

- [Frequency Analysis and Fourier Transform](./notes/frequency-response.html)  
  How to interpret system behavior in the frequency domain, including Fourier Transform and Bode Plots. Non-minimum phase

- [Sensitivity, Robustness, and Robust Control](./notes/robust_control.html)  
  Sensitive, complimentary Sensitivity, and robust control techniques.

- [Discrete-Time Control](./notes/discrete-control.html) \\
  Z-transform, digital implementation of controllers, sampling effects.

- [Model Predictive Control (MPC)](./notes/mpc.html)  \\
  Optimization-based control for constrained systems (intro-level overview).

- [Filters & Signal Conditioning](./notes/filters.html)  \\
  Notch filters for resonances, derivative filtering, reference prefilters, and anti-aliasing.

- [SVD](./notes/svd.html) \\
  A basic review of SVD.

- [Control Theory Techniques](../notes/techniques.html) \\
  Commonly used techniques in controller desing. Pade Approximation, SVD.

- [Data Driven Control](./notes/data_driven_control.html) \\
  Advanced control topics for Machine Learning based control.

### Nonlinear Control

- [Lyapunov Stability Principle](./nonlinear_notes/stability.html) \\
  Lyapunov Stability and LaSelle's Principle.

- [Passivity Theorem](./nonlinear_notes/passivity.html) \\
  Passivity-based controller design.

- [Sliding Mode Control](./nonlinear_notes/sliding_mode.html) \\
  Sliding Mode Control derivation and design.

## Domain Specific Control

- [Quadcoptor Control](./domain_specific_control/drone.html)

- [Autonomous Cars](./domain_specific_control/car.html)


## Interview Prep

- [Kodiak Autonomous Trucking](./interview_prep/kodiak.html)

- [Drone Control](./interview_prep/drone_control.html)

## Data Driven Control

- [Reinforcement Learning]()


## 🛠️ Tools and Techniques

- [Control System Design Workflow](./notes/workflow.html)  
  From modeling to simulation to real-world tuning.

- [Control Using Simulink & Python](./notes/tools.html)  
  Practical guides using Simulink, Python (`control`, `matplotlib`, etc.).

---

*Made using [Jekyll](https://jekyllrb.com/)*
