---
layout: default
title: Drone Control Interview Prep
---

## Q1: The drone starts oscillating in pitch right after you increase the control gain on PID. What do you check? How do you restore stability?

### 1. Triage:
Almost always caused by **excessively high** gains.
1. Actuator limits: If you’re near saturation or hitting rate limits, that can create oscillations or limit cycles.
2. Sign/Wiring check: Ensure control sign hasn't flipped (positive feedback will cause instant oscillation).
3. Sensor sanity: Verify steering angle measurement is valid and not noisy.
4. Latency: Check comms or control loop timing - extra **delay** can destabilize a loop even at the same gain.

### 2. Diagnosis - Why gain change caused oscillation
1. Increasing Kp shifts the gain crossover frequency higher, which usually reduces phase margin.
2. Reduced phase margin → system is closer to the -180° phase point when magnitude crosses 0 dB → oscillation.

### 3. Action plan — How to restore stability
1. Quick fix: Lower Kp back down until oscillation stops, then re-tune more conservatively.
2. Improve phase margin: Add phase lead at high frequencies to recover margin at the new crossover. Increase loop bandwidth gradually while monitoring margins.
3. Filter noise: If derivative gain adds noise, use a small low-pass filter on the measurement.










