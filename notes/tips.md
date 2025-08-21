---
layout: default
title: Tips
---

# Stability Tips
1. The Gain and Phase Margins are **defined with respect to open-loop transfer function**, but the margins are not intrinsic properties of the open-loop system alone, and are only meaningful for the corresponding closed-loop system.

2. Margins are local properties measured at specific crossover points. It is very possible for a higher-order system to have multiple crossover frequencies and therefore multiple Stability Margins. **Conservative Rule** the smallest (worst-case) margin dictates stability.

---


# Bode, Nyquist, Nichols, Root Locus Tips

1. Nyquist plot is primarily for analysing open-loop system graph to determine closed loop stability - hence the -1 point

2. The root locus method, the poles and zeroes you start with are those of the open-loop transfer function.

    - The root locus then shows how the closed-loop poles move in the s-plane as the gain K varies
    - The plotted pole/zero markers themselves are always the open-loop ones.

3. When designing a controller, Bode plot you work with is almost always for the open-loop transfer function $$G(s)H(s)$$


## Bode plot tips

1. Peaks in Bode plots impact closed-loop stability

    - Phase Margin reduction: At the peak, the phase often drops sharply, since the system oscillates more and delays response. If the peak is near the gain crossover frequency, this can push the phase margin down, making the closed-loop system more oscillatory or unstable.

    - Lower gain margin: If the peak height is close to or above 0 dB, it takes less additional loop gain to cross into instability.

    - Poor disturbance rejection: Peaks mean the system will amplify disturbances at those frequencies in closed-loop.

    - High overshoot / ringing: 

## Nyquist Plot tips

1. Nyquist plots are plotted in **polar coordinates**, in contrast to Bode and Nichols

## Root Locus Tips

---

# Controllability and Observability Tips

1. Unstable systems are not always uncontrollable. If unstable modes are controllable, then the system is **stabilizable**.

2. Degrees of controllability can be determined from the Controllability Gramian or the SVD of the controllability matrix.

3. Controllability = Reachability.

4. Degrees of Observability can be determined from the Observability Gramian or the SVD of the observability matrix.

---

# Transfer Function and Frequency Analysis tips

0. For an LTI system, the transfer function G(s) is the Laplace transform of the impulse response
    - It can be derived either by equations or Testing with impulse response


1. The **peaks** at resonance on bode plots are caused by the presence of **lightly damped poles**. A higher order bode plot can have multiple peaks since the system may have multiple **lightly damped poles**.

2. The presence of **RHP zeroes** make the system **non-minimum phase** by introducing a non-causal phase lag, which means the transient response w goes in the wrong direction first.
    - **Each RHP zero cause the system to switch directions**.

3. Bode plot shows the **steady state response only** (evaluating at $$s=j\omega$$). Transient response can only be investigated in **time-domain** since it is a time baseed phenomenon.

4. Avoid 
$$|L(s)| = 0 dB, \angle L(s) = -180^\circ, \text{ where } |L(s)| \text{ is the open-loop transfer function}$$. This is the boundary of stability. At this point gain = -1 (magnitude = 1, phase = $$-180^\circ$$), which causes denominator of closed loop transfer function to be 0.

5. Non-miminum phase can be primarily caused by three phenomena: 1. Time delay $$e^{-sT}$$ 2. RHP zeroes 3. Non-causal/Inverse-unstable Dynamics (Non-causal systems depend on input in the future). 
    - **Only RHP zeroes can cause step response of the system to go in the wrong direction first**. Time delay only causes the step response to shift to the right.

6. Easiest way to deal with RHP zeroes is to lower controller gain (shift magnitude plot down, thereby shifting x axis intercept to the left) to maintain stability and increase phase margin. Allocating a pole to cancel out RHP zero at the plant is risky since the output of the controller can be unbounded even if output of the plant (ie entire system) is stable.

7. **Dominant Poles** are typically those with the **smallest damping** since the impulse response of poles with larger real parts quickly disappears.

---

## LQG and Extended Kalman Tips

1. An LQG controller does not have any guarantee on robustness.

2. LQR and LQR solves an Algebraic Riccati Equation to calculate an analytical solution to the problem given Q and R.

3. If the system is observable, LQE can deduce all states from a few measurable states. Degrees of observability would be helpful when desining an observer. 

--- 

## Sensitivity and Complementary Sensitivity Tips

1. Sensitivity plots also have peaks at resonance frequencies. These peaks occur where the **Open Loop Transfer Function** $$L(s)$$ is close to -1 in the complex plane. This often happens near the gain crossover frequency and when there is low damping (phase lag close to $$-180^\circ$$).

2. Gain Crossover frequency is defined as the frequency 
$$\omega_{gc}$$ at which $$|L(j\omega)|=1$$

3. Time delay and Non-minimum phase place a **fundamental limit** on how small
$$ max(|S|)$$ can be! This is a hard rule that needs to be satisfied. One can shift $$\omega_{gc}$$ to the left, which means the system can only track low frequency references and reject lower frequency disturbances. 

Peaks in Sensitivity Plots are directly correlated with Gain and Phase Margins. The smaller the margins, the bigger the peak.

## Loop shaping Tips

1. Loop shaping is a technique that tries to shape the **Open Loop Transfer Function** $$L(s)$$, according to the desired shape - an **integrator**. The Transfer Function on the bode plot can be shifted left or right by multiplying $$L(s)$$ with $$\omega_{s}$$ to change the gain at low and high frequencies.