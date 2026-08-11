# Numerical Stability

## TL;DR

**Numerical stability** describes how sensitive a numerical algorithm is to small errors introduced during computation.

These errors can come from:

* floating-point arithmetic
* rounding
* truncation
* measurement errors
* approximation errors

A stable algorithm limits the amplification of these errors.

---

## Floating-Point Errors

Computers represent real numbers with finite precision. Therefore, operations such as:

$$
a+b
$$

may introduce small rounding errors.

Repeated operations can accumulate or amplify these errors.

A particularly problematic example is **catastrophic cancellation**, where two nearly equal numbers are subtracted:

$$
a-b
\qquad
a\approx b.
$$

The result may have significantly fewer accurate digits than the original values.

---

## Conditioning vs. Stability

These concepts describe different sources of numerical difficulty.

### Conditioning

**Conditioning** describes the sensitivity of the **mathematical problem** to perturbations in its input.

### Stability

**Stability** describes how an **algorithm** behaves in the presence of numerical errors.

A problem can therefore be:

* well-conditioned and solved stably
* well-conditioned but solved unstably
* ill-conditioned even when solved by a stable algorithm

---

## Condition Number

For a problem involving a function $f$, a relative condition number can be expressed approximately as:

$$
\kappa
\approx
\left|
\frac{x}{f(x)}f'(x)
\right|.
$$

A large condition number indicates that small input errors can produce large output errors.

For a matrix $A$, the condition number with respect to a norm is:

$$
\kappa(A)
=

|A||A^{-1}|.
$$

If $\kappa(A)$ is large, solving systems involving $A$ can be sensitive to perturbations.

---

## Stable Algorithms

An algorithm is considered **numerically stable** if errors introduced during computation do not grow excessively relative to the problem's inherent sensitivity.

For example, solving:

$$
Ax=b
$$

using an appropriate factorization such as **LU decomposition with pivoting** is generally much more stable than explicitly computing:

$$
x=A^{-1}b.
$$

In numerical linear algebra, avoiding unnecessary matrix inversion is therefore an important practical principle.

---

## Backward Stability

An algorithm is **backward stable** if its computed result can be interpreted as the exact solution to a slightly perturbed input problem.

Instead of requiring:

$$
\hat{x}=x,
$$

we ask whether $\hat{x}$ is the exact solution of:

$$
(A+\Delta A)\hat{x}=b+\Delta b
$$

where $\Delta A$ and $\Delta b$ are small.

Backward stability is one of the central concepts in numerical linear algebra.

---

## Forward Error

The **forward error** measures the difference between the computed result $\hat{x}$ and the exact result $x$.

For example:

$$
|\hat{x}-x|.
$$

Relative forward error is:

$$
\frac{|\hat{x}-x|}{|x|}.
$$

Backward error instead measures how much the original problem would need to be perturbed to make the computed solution exact.

---

## Sources of Numerical Error

Common numerical errors include:

### Roundoff Error

Caused by finite floating-point precision.

### Truncation Error

Caused by replacing an exact mathematical operation with an approximation.

For example:

$$
e^x
\approx
\sum_{k=0}^{n}\frac{x^k}{k!}.
$$

### Cancellation

Subtracting nearly equal quantities can cause a severe loss of significant digits.

### Error Propagation

Errors from earlier computations can propagate through subsequent operations.

---

## Improving Numerical Stability

Common techniques include:

* choosing stable algorithms
* scaling and normalization
* avoiding unnecessary subtraction of nearly equal quantities
* using pivoting in matrix factorizations
* avoiding explicit matrix inversion
* using appropriate numerical precision
* reformulating mathematically equivalent expressions

---

## Key Idea

Numerical stability is about controlling computational errors:

$$
\boxed{
\text{Problem Conditioning}
+
\text{Algorithmic Stability}
+
\text{Floating-Point Errors}
\rightarrow
\text{Numerical Accuracy}
}
$$

A good numerical method should not unnecessarily amplify the errors already present in the computation.
