# Banach Spaces

## TL;DR

A **Banach space** is a **complete normed vector space**.

That means it is a vector space equipped with a norm, where every Cauchy sequence converges to a point **inside the space**.

---

## Definition

A normed vector space $(X,|\cdot|)$ is a Banach space if it is **complete**.

Completeness means that every Cauchy sequence $(x_n)$ satisfies:

$$
|x_n-x_m| \to 0
\quad\text{as } n,m\to\infty
$$

and converges to some $x\in X$:

$$
x_n\to x.
$$

---

## Norm

A **norm** measures the size or length of a vector.

A norm $|\cdot|$ satisfies:

$$
|x|\geq 0
$$

$$
|x|=0 \iff x=0
$$

$$
|\alpha x|=|\alpha||x|
$$

and the triangle inequality:

$$
|x+y|\leq|x|+|y|.
$$

---

## Examples

### Euclidean Space

Every finite-dimensional Euclidean space

$$
\mathbb{R}^n
$$

with the Euclidean norm

$$
|x|_2=\sqrt{\sum_i x_i^2}
$$

is a Banach space.

### Function Spaces

Many spaces of functions are Banach spaces when equipped with an appropriate norm.

For example, continuous functions on a compact domain can form a Banach space under the supremum norm:

$$
|f|_\infty=\sup_x |f(x)|.
$$

---

## Banach vs. Hilbert Spaces

Every **Hilbert space** is a Banach space, because an inner product induces a norm:

$$
|x|=\sqrt{\langle x,x\rangle}.
$$

However, not every Banach space is a Hilbert space.

The key distinction is:

* **Banach space:** complete normed vector space
* **Hilbert space:** complete inner-product space

Thus:

$$
\text{Hilbert spaces} \subseteq \text{Banach spaces}.
$$

---

## Why They Matter

Banach spaces provide a mathematical framework for analyzing:

* Functional analysis
* Differential equations
* Optimization
* Approximation theory
* Infinite-dimensional problems
* Machine learning theory

They are particularly useful when working with **infinite-dimensional vector spaces**, such as spaces of functions.
