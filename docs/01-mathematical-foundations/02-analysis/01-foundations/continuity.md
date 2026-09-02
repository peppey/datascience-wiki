# Continuity

## TL;DR

A function $f$ is **continuous** at a point $x_0$ if:

$$
\boxed{
\lim_{x\to x_0}f(x)=f(x_0)
}
$$

This means that the function has no gap, jump, or undefined value at $x_0$.

---

## Definition

A function is continuous at $x_0$ if all three conditions hold:

1. $f(x_0)$ exists.
2. $\lim_{x\to x_0}f(x)$ exists.
3. The limit equals the function value:

$$
\lim_{x\to x_0}f(x)=f(x_0)
$$

A function is **continuous** if it is continuous at every point of its domain.

---

## Typical Functions

Many common functions are continuous on their domains:

* **Polynomials**, e.g. $f(x)=x^2+3x+1$
* **Exponential functions**, e.g. $f(x)=e^x$
* **Trigonometric functions**, e.g. $\sin(x)$ and $\cos(x)$
* **Rational functions**, as long as the denominator is not zero
* **Roots**, wherever they are defined

For example,

$$
f(x)=\frac{1}{x}
$$

is continuous on

$$
(-\infty,0)\cup(0,\infty)
$$

but is not defined at $x=0$.

---

## Piecewise Functions

For a piecewise-defined function, the transition points need to be checked separately.

For example:

$$
f(x)=
\begin{cases}
x^2 & x<1\
2x-1 & x\geq1
\end{cases}
$$

At $x=1$, continuity requires:

$$
\lim_{x\to1^-}f(x)
=

\lim_{x\to1^+}f(x)

f(1)
$$

Here:

$$
\lim_{x\to1^-}x^2=1
$$

and

$$
\lim_{x\to1^+}(2x-1)=1
$$

while:

$$
f(1)=1.
$$

Therefore, $f$ is continuous at $x=1$.

---

## Key Idea

To check continuity:

$$
\boxed{
\text{Limit exists}
\quad+\quad
\text{Function value exists}
\quad+\quad
\text{Both are equal}
}
$$

For piecewise functions, the **transition points** are particularly important.
