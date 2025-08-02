---
layout: default
title: Compensators
---

# Lead, Lag, and Lead-Lag Compensators
## Phase Margin
### Definition
phase margin is a measure of stability for a feedback control system. It represents the amount of phase shift, expressed in degrees, that can be added to the open-loop transfer function before the system reaches the point of instability, specifically where the Bode plot crosses the -180° line at the gain crossover frequency.
### Phase Margin Calculation:
$$\text{Phase Margin} = 180^\circ + \angle G(j\omega_{gc})H(j\omega_{gc})$$
$$\text{Phase Margin} = 180^\circ + \angle G(j\omega_{gc})H(j\omega_{gc})$$

$$\omega_{gc}$$ is the **gain crossover frequency** — the frequency at which the **magnitude** of the open-loop transfer function  $$|G(j\omega)H(j\omega)| = 1$$ (i.e., **0 dB**).
$$\angle G(j\omega)H(j\omega)$$ is the **phase** of the open-loop transfer function at that frequency.
## Phase Lead and Lag
A zero (s) adds phase while pole (1/s) subtracts phase.

phase lead compensators add positive phase to the output, so the output leads the input.
phase lag compensators add negative phase to the output, so the output lags behind the input.

### Phase Lead
Example: Differentiator
input: sin(t) output: cos(t)
cosine is leading sine by 90 degrees -> phase lead
A differentiator circuit introduces a positive phase shift of 90 degrees

### Phase Lag
