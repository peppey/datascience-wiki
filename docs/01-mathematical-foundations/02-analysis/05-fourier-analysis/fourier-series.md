# Fourier Series

## TL;DR

A **Fourier series** represents a periodic function as a sum of sine and cosine functions.

For a periodic function $f(x)$, its Fourier series can be written as

$$
f(x)
=

\frac{a_0}{2}
+
\sum_{n=1}^{\infty}
\left(
a_n\cos(nx)
+
b_n\sin(nx)
\right).
$$

It allows complex periodic signals to be represented using simple oscillations.

## Fourier Coefficients

The coefficients are determined by the function:

$$
a_0
=

\frac{2}{\pi}
\int_{-\pi}^{\pi}
f(x),dx
$$

and

$$
a_n
=

\frac{1}{\pi}
\int_{-\pi}^{\pi}
f(x)\cos(nx),dx,
$$

$$
b_n
=

\frac{1}{\pi}
\int_{-\pi}^{\pi}
f(x)\sin(nx),dx.
$$

Different conventions use different interval lengths and scaling factors.

## Example

A square wave can be represented using only sine functions:

$$
f(x)
=

\frac{4}{\pi}
\left(
\sin(x)
+
\frac{1}{3}\sin(3x)
+
\frac{1}{5}\sin(5x)
+\cdots
\right).
$$

Adding more terms produces a better approximation of the square wave.

## Interpretation

Each term represents a different **frequency**:

* $\sin(x)$ and $\cos(x)$ represent the fundamental frequency.
* $\sin(2x)$ and $\cos(2x)$ represent twice the frequency.
* $\sin(3x)$ and $\cos(3x)$ represent three times the frequency.
* and so on.

The coefficients determine how strongly each frequency contributes to the original signal.

## Fourier Series vs. Fourier Transform

A **Fourier series** is mainly used for **periodic signals**.

The **Fourier transform** generalizes this idea to non-periodic signals and represents them using a continuous range of frequencies.

## Applications

Fourier series are used in many areas, including:

* signal processing
* audio processing
* image processing
* differential equations
* physics
* electrical engineering
* time-series analysis
