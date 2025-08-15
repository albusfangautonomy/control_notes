---
layout: default
title: Stability Analysis
---

# Stability Analysis

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

Let $$\omega_{gc}$$ be a gain-crossover frequency where $$|G(j\omega_{gc})|=1$$, and let $$\omega_{pc}$$ be a phase-crossover frequency where $$\angle G(j\omega_{pc})=-180^\circ$$.

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


