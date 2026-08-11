# Sine

## TL;DR

The **sine function** $\sin(x)$ is a fundamental trigonometric function that relates an angle to the ratio of the opposite side to the hypotenuse in a right triangle.

It is also naturally defined using the **unit circle**.

---

## Definition

For a right triangle:

$$
\sin(\theta)
=

\frac{\text{opposite}}{\text{hypotenuse}}.
$$

Using the unit circle, $\sin(x)$ is the **$y$-coordinate** of the point corresponding to angle $x$.

---

## Properties

The sine function has:

* **Domain:** $\mathbb{R}$
* **Range:** $[-1,1]$
* **Period:** $2\pi$
* **Zeros:** $x=k\pi$, $k\in\mathbb{Z}$
* **Maximum:** $1$
* **Minimum:** $-1$

It satisfies:

$$
\sin(x+2\pi)=\sin(x).
$$

---

## Important Values

$$
\sin(0)=0
$$

$$
\sin\left(\frac{\pi}{6}\right)=\frac12
$$

$$
\sin\left(\frac{\pi}{4}\right)=\frac{\sqrt2}{2}
$$

$$
\sin\left(\frac{\pi}{2}\right)=1
$$

$$
\sin(\pi)=0
$$

---

## Derivative

The derivative of sine is cosine:

$$
\frac{d}{dx}\sin(x)=\cos(x).
$$

The second derivative is:

$$
\frac{d^2}{dx^2}\sin(x)=-\sin(x).
$$

This relationship is important in differential equations and mathematical physics.

---

## Taylor Series

The sine function can be represented by its Maclaurin series:

$$
\sin(x)
=

x-\frac{x^3}{3!}
+\frac{x^5}{5!}
-\frac{x^7}{7!}
+\cdots
$$

This provides a polynomial approximation of $\sin(x)$ near $x=0$.

---

## Applications

Sine is used extensively in:

* Geometry
* Physics
* Signal processing
* Fourier analysis
* Waves and oscillations
* Differential equations
* Machine learning
