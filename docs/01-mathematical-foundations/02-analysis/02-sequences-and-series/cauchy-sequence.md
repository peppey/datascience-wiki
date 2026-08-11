# Cauchy Sequences

## TL;DR

A **Cauchy sequence** is a sequence whose elements become arbitrarily close to each other as the sequence progresses.

It does not require knowing the limit in advance.

---

## Definition

A sequence $(x_n)$ in a metric space $(X,d)$ is **Cauchy** if:

$$
\forall \varepsilon > 0,\ \exists N \in \mathbb{N}
$$

such that for all $m,n > N$:

$$
d(x_m,x_n)<\varepsilon.
$$

In other words, after some point, **all elements of the sequence are arbitrarily close to each other**.

---

## Example

Consider:

$$
x_n = \frac{1}{n}.
$$

For sufficiently large $m$ and $n$,

$$
\left|\frac{1}{m}-\frac{1}{n}\right|
$$

becomes arbitrarily small.

Therefore, $(1/n)$ is a Cauchy sequence.

It converges to:

$$
\lim_{n\to\infty}\frac{1}{n}=0.
$$

---

## Cauchy vs. Convergent

Every **convergent sequence is Cauchy**.

However, the converse is only true in a **complete space**.

$$
\text{Convergent}
\Rightarrow
\text{Cauchy}
$$

In a complete space:

$$
\text{Cauchy}
\Rightarrow
\text{Convergent}.
$$

---

## Completeness

A metric space is **complete** if every Cauchy sequence converges to a point within the space.

For example, $\mathbb{R}$ is complete.

The rational numbers $\mathbb{Q}$ are not complete because there are Cauchy sequences of rational numbers that converge to irrational numbers.

For example, a sequence of rational approximations to $\sqrt{2}$ is Cauchy in $\mathbb{Q}$ but does not converge to an element of $\mathbb{Q}$.

---

## Importance

Cauchy sequences provide a way to define convergence **without explicitly knowing the limit**.

They are fundamental in:

* Real analysis
* Metric spaces
* Functional analysis
* Banach spaces
* Numerical analysis
* Approximation theory