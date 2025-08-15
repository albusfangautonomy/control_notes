---
layout: default
title: Nichols Chart, Nyquist Plot, Bode Plot, and Root Locus Plot
---

# Nichols Chart, Nyquist Plot, and Bode Plot

![Bode, Nyquist, Nichols plots](../figures/bode_nyquist_nichols.png)

All three plots display 3 Key information about the system: 1. **Gain** 2. **Phase** 3. **Frequency**

## Which to Use? A comparison
**All three display the same information just in different ways**
Bode Plot is useful for Loop shaping
Nyquist Plot and Nichols Plot are useful for general sensitivity and stability analysis.

## Intuition

Bode plot is extremely useful when analyzing open loop frequency reponse  $$G(s)$$ of **minimum phase and stable systems** to predict the beahvior of the closed loop system $$\frac{G(s)}{1+G(s)}$$.
However, Bode plot falls apart when dealing with non-minimum phase or unstable systems. This is where **Nyquist plot** comes in useful. Nyquist plot displays all three in one plot (Gain, Phase, Frequency).
Nichols encodes Bode magnitude and phase plots into one single plot, displaying same information as the Nyquist plot in cartesian coordinates.

## Nyquist Plot
<!-- ![Nyquist Plot example](../figures/nyquist_plot.png)

![Nyquist Plot and Bode plot](../figures/nyquist_bode.png)

![Nyquist Plot Margins](../figures/nyquist_margin.png)  -->
<img src="../figures/nyquist_plot.png" alt="Nyquist Plot example" width="300">
<img src="../figures/nyquist_bode.png" alt="Nyquist Plot and Bode plot" width="500" height="300">
<img src="../figures/nyquist_margin.png" alt="Nyquist Plot Margins" width="300">


### Nyquist Plot Stability analysis (benefits)
1. for minimum phase and stable open loop systems, don't corss the cricitical point (-1,0)
2. Gain margin and Phase Margin can be read from Nyquist Plot
3. We can still use Nyquist Stability Criterion and Nyquist plot even for unstable open loop systems
4. Easier to see combinations of gain and phase (**disk margin**)
5. Information displayed in polar coordinates.
### Nyquist Plot Critical Point
Avoid (-1,0) on Nyquist plot. Closed loop system oscillates at that point.

## Nichols Plot 
<img src="../figures/nichols_plot.png" alt="Nichols Plot example" width="300">
Frequency is not explicitly shown just as Nyquist plot

## Applications

### System Identification with Bode Plot

Given a **blackbox** LTI system, feeding in signals of various frequency (**Sine sweep**) and observing the output can generate the bode plot of the transfer function.

### System Design and Analysis with Bode plot
Fundamental Principle: Open loop system can provide insightful information about the close loop system.
Let open loop system = G(s) = L(s) = P(s) * K(s), closed loop system =  $$\frac{G(s)}{1+G(s)}$$

**Applications of Bode plot**
1. If $$G(s)$$, an open loop system transfer function has any 0 dB and -180 degrees phase frequencies (G(s)=-1+0j), then closed loop $$\frac{G(s)}{1+G(s)}$$ will oscillate. Bode plot can be used to check.
2. If open loop system is miminum phase and stable, (both zeroes poles are on the LHP), then we can determine closed loop easily through bode plot

**Key Observation**
Bode-plot restatements of Nyquist Criterion (margins)

Let $$\omega_{gc}$$ 
be a gain-crossover frequency where 
$$ |G(j\omega_{gc})|=1 $$
, and let $$ \omega_{pc} $$ be a phase-crossover frequency where 
$$\angle G(j\omega_{pc})=-180^\circ$$.

- **Phase margin condition (at gain crossover):**
  $$
  |G(j\omega_{gc})|=1 \quad \Rightarrow \quad \angle G(j\omega_{gc}) > -180^\circ
  $$
  (positive phase margin). This ensures the Nyquist plot does **not** cross the real axis at or left of $$-1$$.

- **Gain margin condition (at phase crossover):**
  $$
  \angle G(j\omega_{pc})=-180^\circ \quad \Rightarrow \quad |G(j\omega_{pc})| < 1
  $$
  (positive gain margin). This keeps the Nyquist locus inside the unit circle when it is at $$-180^\circ$$, avoiding the point $$-1$$.

If **both** conditions hold for all relevant crossovers and $$P=0$$, the loop has positive stability margins and the closed loop is stable.