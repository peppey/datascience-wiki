# Integral

## TL;DR

An **integral** generalizes the idea of summing infinitely many infinitesimal quantities.

There are two fundamental types:

* **indefinite integrals**, which describe antiderivatives
* **definite integrals**, which describe accumulated quantities such as area

Integration is the inverse operation of differentiation in an important sense.

---

## Indefinite Integral

The indefinite integral of $f(x)$ is the set of all antiderivatives:

$$
\int f(x),dx=F(x)+C,
$$

where:

$$
F'(x)=f(x).
$$

For example:

$$
\int x^2,dx
=

\frac{x^3}{3}+C.
$$

---

## Definite Integral

A definite integral is written as:

$$
\int_a^b f(x),dx.
$$

It represents the **signed accumulated area** between $a$ and $b$.

For a non-negative function:

$$
\int_a^b f(x),dx
$$

corresponds to the area between the graph and the $x$-axis.

---

## Fundamental Theorem of Calculus

The **Fundamental Theorem of Calculus** connects differentiation and integration.

If $F'(x)=f(x)$, then:

$$
\int_a^b f(x),dx
=

F(b)-F(a).
$$

Conversely, defining:

$$
F(x)=\int_a^x f(t),dt
$$

gives:

$$
F'(x)=f(x)
$$

under suitable conditions.

---

## Techniques of Integration

Important analytical techniques include:

* substitution
* integration by parts
* partial fractions
* trigonometric substitution
* trigonometric identities
* improper integration

Some functions do not have elementary antiderivatives.

---

## Improper Integrals

An integral is **improper** if the interval is infinite or the integrand becomes unbounded.

For example:

$$
\int_1^\infty \frac{1}{x^2},dx
=

\lim_{b\to\infty}
\int_1^b\frac{1}{x^2},dx.
$$

The integral **converges** if this limit exists and is finite.

---

## Numerical Integration

When an integral cannot be evaluated analytically, it can be approximated numerically.

Common methods include:

* Riemann sums
* trapezoidal rule
* Simpson's rule
* Gaussian quadrature
* Monte Carlo integration

---

## Multivariable Integration

Integration extends to multiple dimensions:

$$
\int!!\int_D f(x,y),dA.
$$

Higher-dimensional integrals are used for:

* volumes
* mass distributions
* probability densities
* expectations
* physical fields

Important generalizations include **line integrals** and **surface integrals**.

---

## Key Idea

Integration connects **local change** with **global accumulation**:

$$
\boxed{
\text{Derivative}
\longleftrightarrow
\text{Integral}
}
$$

The Fundamental Theorem of Calculus makes this connection precise.
