---
layout: default
title: Stability Analysis
---
# Stability Analysis

## Stability Margins - Gain and Phase Margins
In simple terms, Gain and Phase margins are the safe net and the extra that protects us from instability.
less margin = less stable

**Note:**
*Gain* crossover frequency is used to caluclate *Phase* Margin.

*Phase* crossover frequency is used to caculate *Gain* Margin.

The Gain and PhaseMargins are **defined with respect to open-loop transfer function**, but the margins are not intrinsic properties of the open-loop system alone, and are only meaningful for the corresponding closed-loop system.

---

### Gain Margin

The gain margin (GM) is defined at the phase crossover frequency 
$$ \omega_{pc}  \text{ where } \angle L(j\omega_{pc}) = -180^\circ $$:

$$
GM = \frac{1}{|L(j\omega_{pc})|}
$$

In decibels (dB):

$$
GM_{\text{dB}} = -20 \log_{10} |L(j\omega_{pc})|
$$


If there are multiple **Phase crossover frequencies $$\omega_{pc} $$**, use the most conservative Gain Margin.


### Phase Margin

The phase margin (PM) is defined at the gain crossover frequency 
$$ \omega_{gc} $$ where $$ |L(j\omega_{gc})| = 1 $$:

$$
PM = 180^\circ + \angle L(j\omega_{gc})
$$



### Margins and Sensitivity

Peaks in Sensitivity Plots are directly correlated with Gain and Phase Margins. The smaller the margins, the bigger the peak.

---

## Closed Loop Stability

In a non-unity feedback system whose feedback transfer function is $$H(s)$$, the closed loop transfer function is $$\frac{G(s)}{1+GH}$$. We can study the stability of the closed loop transfer function by identifying the **zeros** of $$1+GH$$.

**Adding 1 to the Nyquist plot of the open loop transfer function shift the plot to the right by 1**


---

## Nyquist Criterion — Bode/Nyquist Terms (Unity Feedback)

**Setup.** Let the open-loop transfer be $$G(s)$$ for a unity-feedback loop with closed-loop characteristic $$1+G(s)=0$$. Let:
- $$P$$ = number of open-loop poles of $$G(s)$$ in the right-half plane (RHP),
- $$N$$ = number of *clockwise* encirclements of the Nyquist critical point $$-1+0j$$ by the Nyquist plot of $$G(j\omega)$$ (standard Nyquist contour),
- $$Z$$ = number of closed-loop poles in the RHP.

**General Nyquist criterion.**
$$
Z = N + P.
$$
The closed loop is **stable** iff $$Z=0$$. Equivalently, the Nyquist plot must encircle $$-1$$ **clockwise** exactly $$N=-P$$ times.

**Common special case (open-loop stable, i.e., $$P=0$$).**
If $$G(s)$$ has no RHP poles and no poles on the $$j\omega$$-axis (aside from allowable integrators handled with the modified contour), then:
- Closed loop is stable **iff** the Nyquist plot of $$G(j\omega)$$ **does not encircle** $$-1+0j$$ (i.e., $$N=0 \Rightarrow Z=0$$).

---

### Bode-plot restatements (margins)

Let $$\omega_{gc}$$ be a gain-crossover frequency 
where $$|G(j\omega_{gc})|=1$$, 
and let $$\omega_{pc}$$ be a phase-crossover frequency
 where $$\angle G(j\omega_{pc})=-180^\circ$$.

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

---

### Notes/Caveats

- If $$P>0$$ (open-loop unstable), you **must** have exactly $$N=-P$$ clockwise encirclements of $$-1$$. Simple “margin checks” at crossovers are insufficient without accounting for $$P$$.
- Poles on the imaginary axis (e.g., pure integrators) require the standard indentation in the Nyquist contour; apply the modified criterion accordingly.
- The above statements presume unity feedback; for non-unity feedback, apply the criterion to the appropriate open-loop function that multiplies the feedback path.


