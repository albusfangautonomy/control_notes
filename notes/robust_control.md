---
layout: default
title: Robust Control
---
# Robust Control
## Motivation and Background
A paper by John Doyle proved that there is no guarantee on robustness of LQG scheme. This discovery pushed the industry towards robust control. We need to delve into Laplace domain and determine Robustness of a system. Laplace Transform domain gives us insights into the performance and robustness.
## Three Equivalent Representations of Linear Systems
1. State space representation
    $$\dot{x}=Ax+Bu \\ y=Cx$$
2. Transfer functions
$$G(s)=C(sI-A)^{-1}B$$
3. Impulse response time domain
$$y(t)=\int_{0}^{t}h(t-\tau)u(\tau)d\tau $$ 
This is a convolution between impulse response and control input
**Note** there are different usages for each of the three representations. 1. If physics can be represented, State space representation can be very useful. Transfer functions can be useful for investigating robustness and performance

## Fourier and Laplace Transforms
## Fourier Series

If $f(t)$ is a periodic function with period $T$, its **Fourier series** representation is:

$$
f(t) = a_0 + \sum_{n=1}^{\infty} \left[ a_n \cos\left(\frac{2\pi n t}{T}\right) + b_n \sin\left(\frac{2\pi n t}{T}\right) \right]
$$

The coefficients are given by:

$$
a_0 = \frac{1}{T} \int_{-T/2}^{T/2} f(t) \, dt
$$

$$
a_n = \frac{2}{T} \int_{-T/2}^{T/2} f(t) \cos\left(\frac{2\pi n t}{T}\right) dt
$$

$$
b_n = \frac{2}{T} \int_{-T/2}^{T/2} f(t) \sin\left(\frac{2\pi n t}{T}\right) dt
$$

You can also write the Fourier series using **complex exponentials**:

$$
f(t) = \sum_{n=-\infty}^{\infty} c_n e^{i 2\pi n t / T}
$$

with coefficients:

$$
c_n = \frac{1}{T} \int_{-T/2}^{T/2} f(t) e^{-i 2\pi n t / T} dt
$$

---

## Fourier Transform

For non-periodic functions, the **Fourier Transform** is used. The **continuous-time Fourier transform (CTFT)** of a function $f(t)$ is:

$$
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i \omega t} dt
$$

The **inverse Fourier transform** is:

$$
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i \omega t} d\omega
$$

Alternatively, in terms of frequency $f$ (Hz) instead of angular frequency $\omega = 2\pi f$:

$$
F(f) = \int_{-\infty}^{\infty} f(t) e^{-i 2\pi f t} dt
$$

$$
f(t) = \int_{-\infty}^{\infty} F(f) e^{i 2\pi f t} df
$$

## Transfer Function


### Frequency Response
![frequency response of a mass-spring damper system](../figures/frequency_response.png)

$$ ratio{\bar{x}}{\bar{u}}$$
**Notes:** 
1. The bode plots are plotted in log scale. A small bump in Gain plot corresponds to huge response at resonate frequency. 
2. At extremely low frequency, this system displays no gain at all hence Gain = 0 for low frequencies. At high frequencies, the sytems doesn't have the capacity to respond in times hence the gain drops asymptotically to zero or $-\infty$ in log scale.
3. 