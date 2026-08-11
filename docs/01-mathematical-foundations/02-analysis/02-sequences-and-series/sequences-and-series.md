# Sequences and Series

## TL;DR

A **sequence** is an ordered list of numbers or other mathematical objects:

$$
(a_n)_{n=1}^{\infty}.
$$

A **series** is the sum of the elements of a sequence:

$$
\sum_{n=1}^{\infty}a_n.
$$

Sequences and series are fundamental to **analysis**, especially for limits, convergence, and approximation.

---

## Sequences

A sequence can be viewed as a function:

$$
a:\mathbb{N}\to X.
$$

A sequence $(a_n)$ **converges** to $a$ if:

$$
\lim_{n\to\infty}a_n=a.
$$

Formally, for every $\varepsilon>0$, there exists $N\in\mathbb{N}$ such that:

$$
n\geq N
\Rightarrow
|a_n-a|<\varepsilon.
$$

---

## Important Types

A sequence may be:

* **bounded**
* **monotone**
* **convergent**
* **divergent**
* **Cauchy**

Every convergent sequence in $\mathbb{R}$ is bounded and Cauchy.

---

## Series

A series is written as:

$$
\sum_{n=1}^{\infty}a_n.
$$

It is defined through its **partial sums**:

$$
S_N=\sum_{n=1}^{N}a_n.
$$

The series converges if:

$$
\lim_{N\to\infty}S_N=S
$$

for some finite $S$.

---

## Absolute Convergence

A series is **absolutely convergent** if:

$$
\sum_{n=1}^{\infty}|a_n|<\infty.
$$

Absolute convergence implies convergence:

$$
\sum |a_n|<\infty
\Rightarrow
\sum a_n\text{ converges}.
$$

---

## Common Convergence Tests

Important tests for infinite series include:

* comparison test
* ratio test
* root test
* integral test
* alternating series test

---

## Important Examples

### Geometric Series

$$
\sum_{n=0}^{\infty}r^n
======================

\frac{1}{1-r},
\qquad |r|<1.
$$

### Harmonic Series

$$
\sum_{n=1}^{\infty}\frac1n
$$

diverges.

More generally:

$$
\sum_{n=1}^{\infty}\frac1{n^p}
$$

converges exactly when:

$$
p>1.
$$

---

## Key Idea

Sequences study the behavior of individual terms:

$$
a_n,
$$

while series study the behavior of their cumulative sums:

$$
\sum_{n=1}^{\infty}a_n.
$$

The central concept is **convergence**.
