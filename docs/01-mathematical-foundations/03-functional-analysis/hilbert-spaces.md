# Hilbert Space

## TL;DR

A **Hilbert space** is a complete inner product space.

It generalizes Euclidean spaces to potentially **infinite-dimensional** settings and is fundamental in:

* functional analysis
* quantum mechanics
* Fourier analysis
* partial differential equations
* statistics and machine learning

---

## Definition

A Hilbert space is a vector space $H$ equipped with an inner product:

$$
\langle x,y\rangle
$$

such that the induced norm:

$$
|x|=\sqrt{\langle x,x\rangle}
$$

makes $H$ **complete**.

Completeness means that every **Cauchy sequence** in $H$ converges to an element of $H$.

---

## Inner Product

For a real vector space, an inner product satisfies:

$$
\langle x,y\rangle=\langle y,x\rangle,
$$

$$
\langle ax+by,z\rangle
=

a\langle x,z\rangle+b\langle y,z\rangle,
$$

and:

$$
\langle x,x\rangle\geq0
$$

with equality only when:

$$
x=0.
$$

For complex vector spaces, the inner product is conjugate symmetric:

$$
\langle x,y\rangle
=

\overline{\langle y,x\rangle}.
$$

---

## Examples

### Euclidean Space

$$
\mathbb{R}^n
$$

with the standard inner product:

$$
\langle x,y\rangle
=
\sum_{i=1}^n x_i y_i
$$

is a finite-dimensional Hilbert space.

### Sequence Space

The space:

$$
\ell^2
=

\{
(x_n):
\sum_{n=1}^{\infty}|x_n|^2<\infty
\}
$$

is a Hilbert space with:

$$
\langle x,y\rangle
=

\sum_{n=1}^{\infty}x_n\overline{y_n}.
$$

### Function Spaces

The space:

$$
L^2(\Omega)
$$

of square-integrable functions is a Hilbert space with:

$$
\langle f,g\rangle
=

\int_\Omega f(x)\overline{g(x)},dx.
$$

---

## Orthogonality

Two vectors are **orthogonal** if:

$$
\langle x,y\rangle=0.
$$

This generalizes perpendicularity from Euclidean geometry.

The **Pythagorean theorem** holds:

$$
x\perp y
\Rightarrow
|x+y|^2
=

|x|^2+|y|^2.
$$

---

## Orthonormal Bases

A sequence $(e_i)$ is **orthonormal** if:

$$
\langle e_i,e_j\rangle
=

\delta_{ij}.
$$

In a Hilbert space, vectors can be represented using an orthonormal basis:

$$
x
=

\sum_i
\langle x,e_i\rangle e_i.
$$

For an orthonormal basis, **Parseval's identity** gives:

$$
|x|^2
=====

\sum_i|\langle x,e_i\rangle|^2.
$$

---

## Projection

For a closed subspace $M\subseteq H$, every $x\in H$ can be decomposed as:

$$
x=P_Mx+(x-P_Mx),
$$

where:

$$
P_Mx\in M
$$

and:

$$
x-P_Mx\perp M.
$$

The operator $P_M$ is the **orthogonal projection** onto $M$.

This is fundamental to least-squares methods and approximation theory.

---

## Riesz Representation Theorem

Every continuous linear functional:

$$
f:H\to\mathbb{R}
$$

can be represented uniquely as an inner product:

$$
f(x)=\langle x,y\rangle
$$

for some $y\in H$.

Thus:

$$
H^*\cong H.
$$

This is one of the fundamental structural properties of Hilbert spaces.

---

## Hilbert Spaces in Machine Learning

Hilbert spaces provide the mathematical framework for **kernel methods**.

A **Reproducing Kernel Hilbert Space (RKHS)** is a Hilbert space of functions in which evaluation is a continuous linear functional.

This leads to kernel methods such as:

* Support Vector Machines
* kernel regression
* Gaussian processes

---

## Key Idea

A Hilbert space combines:

$$
\boxed{
\text{Vector Space}
+
\text{Inner Product}
+
\text{Completeness}
}
$$

It extends the geometry of Euclidean space to infinite-dimensional spaces while retaining concepts such as **distance, angles, orthogonality, projection, and bases**.
