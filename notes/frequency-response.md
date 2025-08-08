---
layout: default
title: Frequency Response and Fourier Transform
---
# Frequency Response and Fourier Transform
## Fourier and Laplace Transforms
### Laplace Transform
$$
\mathcal{L}\{f(t)\} = F(s) = \int_0^{\infty} e^{-st} f(t) \, dt
$$

Laplace Tranform is a generialized form of Fourier Transform. Specifically, Fourier Transform evaluates Laplace Transform at $$i\omega$$, with no real parts, ie. Fourier Transform only evaluates purely imaginary arguments for Laplace Transform.
**Inpoulse response** h(t) given $$u = \delta(t)$$ is $$L^{-1}{G(s), where Y(s) = G(s)X(s)}$$ ie the inverse Laplace Transform of the Transfer function (G(s))
### Fourier Series

If $$f(t)$$ is a periodic function with period $T$, its **Fourier series** representation is:

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

### Fourier Transform

For non-periodic functions, the **Fourier Transform** is used. The **continuous-time Fourier transform (CTFT)** of a function $f(t)$ is:

$$
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i \omega t} dt
$$

The **inverse Fourier transform** is:

$$
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i \omega t} d\omega
$$

Alternatively, in terms of frequency $$f$$ (Hz) instead of angular frequency $\omega = 2\pi f$:

$$
F(f) = \int_{-\infty}^{\infty} f(t) e^{-i 2\pi f t} dt
$$

$$
f(t) = \int_{-\infty}^{\infty} F(f) e^{i 2\pi f t} df
$$

**Intuition** Fourier Transform converts a time-domain $$\bar{x}(t)$$ to frequency domain $$X(f)$$. This investigates how much of this specific frequency exists in the signal.
Fourier Transform returns a complex number.
1. The magnitude of this number denotes how strong that frequency is in the signal
2. The angle of the complex number signifies the phase offset of that frequency - i.e., where that sine wave starts relative to time zero.


## Bode and Nyquist Plots

### Frequency Response
![frequency response of a mass-spring damper system](../figures/frequency_response.png)

$$ ratio{\bar{x}}{\bar{u}}$$
**Notes:** 
1. The bode plots are plotted in log scale. A small bump in Gain plot corresponds to huge response at resonate frequency. 
2. At extremely low frequency, this system displays no gain at all hence Gain = 0 for low frequencies. At high frequencies, the sytems doesn't have the capacity to respond in times hence the gain drops asymptotically to zero or $-\infty$ in log scale.
Coming soon...
