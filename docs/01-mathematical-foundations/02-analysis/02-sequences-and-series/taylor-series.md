# Taylor Series

## TL;DR

A **Taylor series** represents a function as an infinite sum of terms based on its derivatives at a point.

Around $x=a$:

$$
f(x)
=

\sum_{n=0}^{\infty}
\frac{f^{(n)}(a)}{n!}(x-a)^n.
$$

It can be used to **approximate complicated functions with polynomials**.

---

## Definition

The Taylor series of a function $f(x)$ around $x=a$ is:

$$
f(x)
=

f(a)
+f'(a)(x-a)
+\frac{f''(a)}{2!}(x-a)^2
+\frac{f'''(a)}{3!}(x-a)^3
+\cdots
$$

The coefficients are determined by the derivatives of $f$ at $a$.

---

## Maclaurin Series

A **Maclaurin series** is a Taylor series centered at $a=0$:

$$
f(x)
====

\sum_{n=0}^{\infty}
\frac{f^{(n)}(0)}{n!}x^n.
$$

For example, the exponential function has the series:

$$
e^x
===

1+x+\frac{x^2}{2!}
+\frac{x^3}{3!}
+\cdots
$$

The sine function has:

$$
\sin(x)
=======

x-\frac{x^3}{3!}
+\frac{x^5}{5!}
-\cdots
$$

---

## Polynomial Approximation

A Taylor series can be truncated after a finite number of terms.

For example:

$$
e^x \approx 1+x+\frac{x^2}{2}.
$$

This gives a **Taylor polynomial** that approximates $e^x$ near $x=0$.

Generally:

$$
T_n(x)
======

\sum_{k=0}^{n}
\frac{f^{(k)}(a)}{k!}(x-a)^k.
$$

The approximation usually becomes better near the expansion point as more terms are added.

---

## Remainder

The difference between the function and its Taylor polynomial is called the **remainder**:

$$
R_n(x)=f(x)-T_n(x).
$$

Under suitable conditions, the remainder becomes small as $n$ increases.

---

## Applications

Taylor series are used for:

* Numerical approximation
* Calculus
* Differential equations
* Numerical methods
* Physics and engineering
* Approximating functions in machine learning

They are especially useful when evaluating the original function is difficult but polynomial operations are easy.
