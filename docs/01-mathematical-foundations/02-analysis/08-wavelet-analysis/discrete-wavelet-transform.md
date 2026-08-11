# Discrete Wavelet Transform

## TL;DR

The **Discrete Wavelet Transform (DWT)** decomposes a signal into components at different **scales and positions**.

Unlike the Continuous Wavelet Transform, the DWT uses a **discrete set of scales and translations**, making it computationally efficient and suitable for signal processing.

---

## Definition

The DWT represents a signal using scaled and shifted versions of a wavelet.

A common dyadic parameterization is

$$
a = 2^j,
\qquad
b = k2^j,
$$

where $j,k\in\mathbb{Z}$.

The corresponding wavelet functions can be written as

$$
\psi_{j,k}(t)
=

\frac{1}{\sqrt{2^j}}
\psi\left(
\frac{t-k2^j}{2^j}
\right).
$$

The wavelet coefficients are obtained using inner products:

$$
d_{j,k}
=

\langle f,\psi_{j,k}\rangle.
$$

These coefficients describe the signal at different scales and positions.

---

## Multiresolution Decomposition

The DWT commonly separates a signal into:

* **Approximation coefficients** — low-frequency information
* **Detail coefficients** — high-frequency information

For a one-dimensional signal:

```text
Signal
  │
  ▼
 ┌───────────────────┐
 │ Low-pass filter   │ ──→ Approximation
 └───────────────────┘
  │
 ┌───────────────────┐
 │ High-pass filter  │ ──→ Detail
 └───────────────────┘
```

The approximation can then be decomposed again:

```text
Signal
  │
  ├── Approximation ──┐
  │                   │
  │                   ▼
  │              ┌─────────┐
  │              │   DWT   │
  │              └─────────┘
  │               │       │
  │               ▼       ▼
  │              A₂       D₂
  │
  └── Detail → D₁
```

This creates a **multi-scale representation**.

---

## Filter Bank

In practice, the DWT is usually implemented using a pair of filters:

* **Low-pass filter** $h$ — extracts approximation information
* **High-pass filter** $g$ — extracts detail information

After filtering, the results are typically **downsampled by a factor of 2**.

```text
                 Signal
                   │
          ┌────────┴────────┐
          ▼                 ▼
     Low-pass h       High-pass g
          │                 │
     Downsample          Downsample
          │                 │
          ▼                 ▼
   Approximation A     Detail D
```

---

## DWT vs. CWT

| Discrete Wavelet Transform             | Continuous Wavelet Transform               |
| -------------------------------------- | ------------------------------------------ |
| Discrete scales and positions          | Continuous scales and positions            |
| Computationally efficient              | More computationally expensive             |
| Often uses filter banks                | Usually computed over many scales          |
| Suitable for compression and denoising | Useful for detailed signal analysis        |
| Produces a compact representation      | Produces a dense time-scale representation |

---

## Wavelet Families

Common wavelet families include:

* **Haar**
* **Daubechies**
* **Symlets**
* **Coiflets**

Different wavelets provide different properties such as smoothness, compact support, and symmetry.

---

## Applications

The DWT is commonly used for:

* **Signal denoising**
* **Data compression**
* **Feature extraction**
* **Image processing**
* **Audio processing**
* **Time-series analysis**
* **Anomaly detection**

For example, noise can often be reduced by thresholding small detail coefficients and reconstructing the signal.

---

## Reconstruction

The original signal can be reconstructed from its wavelet coefficients using the **inverse DWT (IDWT)**.

```text
Wavelet coefficients
        │
        ▼
     IDWT
        │
        ▼
Original signal
```

For suitable wavelet bases, the decomposition can be lossless.

---

## Key Idea

The Discrete Wavelet Transform decomposes a signal into **approximation and detail components at multiple scales**:

$$
\boxed{
\text{Signal}
\rightarrow
\text{Approximation}
+
\text{Details at different scales}
}
$$

It provides a compact multi-resolution representation that is particularly useful for signal processing.
