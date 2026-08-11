# Continuous Wavelet Transform

## TL;DR

The **Continuous Wavelet Transform (CWT)** represents a signal using wavelets at different **scales** and **positions**.

Unlike the Fourier Transform, which describes which frequencies are present, the CWT also provides information about **when** structures occur in the signal.

---

## Definition

Given a signal $f(t)$ and a mother wavelet $\psi(t)$, the Continuous Wavelet Transform is defined as

$$
W_f(a,b)
=

\frac{1}{\sqrt{|a|}}
\int_{-\infty}^{\infty}
f(t)
\overline{
\psi\left(\frac{t-b}{a}\right)
}
,dt,
$$

where:

* $a$ is the **scale**
* $b$ is the **translation (position)**
* $\psi$ is the **mother wavelet**
* $\overline{\psi}$ denotes the complex conjugate

The result $W_f(a,b)$ describes how strongly the signal resembles the wavelet at scale $a$ and position $b$.

---

## Scale and Translation

The wavelet is shifted and scaled according to

$$
\psi_{a,b}(t)
=

\frac{1}{\sqrt{|a|}}
\psi\left(\frac{t-b}{a}\right).
$$

### Scale

The scale controls the size of the wavelet:

```text
Small scale
     /\    /\
    /  \  /  \
   /    \/    \

Large scale
      /      \
_____/        \_____
```

* Small scale → short-duration, high-frequency structures
* Large scale → long-duration, low-frequency structures

### Translation

The translation $b$ determines **where** the wavelet is located in the signal.

---

## Time-Frequency Localization

The CWT provides a **time-scale representation** of a signal:

```text
             Time
        ─────────────────→
Scale
  │
  │      ●
  │    ●   ●
  │  ●       ●
  │        ●
  ▼
```

This makes the CWT useful for signals whose frequency content changes over time.

Examples include:

* audio signals
* EEG signals
* vibration signals
* seismic signals
* financial time series

---

## CWT vs. Fourier Transform

The Fourier Transform decomposes a signal into sinusoidal frequencies:

$$
f(t)
\rightarrow
\hat{f}(\omega).
$$

The CWT instead uses localized wavelets:

$$
f(t)
\rightarrow
W_f(a,b).
$$

| Fourier Transform               | Continuous Wavelet Transform        |
| ------------------------------- | ----------------------------------- |
| Global frequency representation | Localized time-scale representation |
| Uses sinusoids                  | Uses wavelets                       |
| Poor temporal localization      | Good temporal localization          |
| Fixed resolution                | Multi-scale resolution              |

---

## Wavelet Scalogram

The magnitude of the CWT coefficients can be visualized as a **scalogram**:

$$
|W_f(a,b)|^2.
$$

A scalogram shows how strongly different scales are present at different positions in the signal.

```text
             Time
        ─────────────────→
Scale
  │       ███
  │     ███████
  │       ███      ██
  │  ██           ████
  │ ████             █
  ▼
```

Bright or large values indicate strong similarity between the signal and the wavelet at a particular scale and position.

---

## Choice of Wavelet

Different wavelets are suitable for different types of signals.

Common wavelets include:

* Haar wavelet
* Mexican Hat wavelet
* Morlet wavelet
* Daubechies wavelets

The choice of wavelet affects which signal structures are detected effectively.

---

## Applications

The CWT is commonly used for:

* **Signal analysis**
* **Time-frequency analysis**
* **Feature extraction**
* **Pattern detection**
* **Anomaly detection**
* **Audio analysis**
* **Biomedical signal analysis**

For example, transient events in an audio signal can be detected by identifying strong CWT coefficients at specific times and scales.

---

## Key Idea

The Continuous Wavelet Transform analyzes a signal using **localized wavelets at different scales**:

$$
\boxed{
\text{Signal}
\rightarrow
\text{time-scale representation}
}
$$

Small scales reveal fine, rapidly changing structures, while large scales reveal broader structures.
