# QR Decomposition

## TL;DR

**QR decomposition** factorizes a matrix into:

$A = QR$

where:

- $Q$ is an **orthogonal matrix** (its columns are orthonormal vectors)
- $R$ is an **upper triangular matrix**

QR decomposition is mainly used for:

- solving least squares problems
- linear regression
- numerical optimization
- solving linear systems

---

## Idea

A matrix can be interpreted as a collection of vectors.

QR decomposition transforms these vectors into:

- an orthogonal basis $Q$
- a transformation matrix $R$

The decomposition is:

$A = QR$

where:

- $A$ is the original matrix
- $Q$ contains orthonormal basis vectors
- $R$ describes how the original vectors are represented in this basis

---

## Properties

### Orthogonal Matrix $Q$

The columns of $Q$ are orthonormal, meaning:

$Q^TQ = I$

This means:

- vectors are perpendicular
- vectors have length 1
- no information is lost during the transformation

---

### Upper Triangular Matrix $R$

The matrix $R$ has values only on and above the diagonal.

Example:

| | | |
|-|-|-|
| $r_{11}$ | $r_{12}$ | $r_{13}$ |
| 0 | $r_{22}$ | $r_{23}$ |
| 0 | 0 | $r_{33}$ |

---

## How is QR Decomposition Computed?

There are several algorithms to compute QR decomposition.

### Gram-Schmidt Orthogonalization

The idea:

1. Take the first vector
2. Normalize it
3. Remove its influence from the remaining vectors
4. Repeat for all vectors

This creates orthogonal vectors.

Advantages:

- easy to understand
- mathematically intuitive

Disadvantages:

- can be numerically unstable

---

### Householder Transformations

Householder transformations use reflections to transform a matrix into an upper triangular form.

Advantages:

- numerically stable
- commonly used in numerical libraries

Many scientific computing libraries use variants of this method.

---

## QR Decomposition in Linear Regression

Linear regression solves:

$Xw = y$

The goal is to find weights $w$ that minimize the error:

$||Xw-y||^2$

A common approach is the normal equation:

$w=(X^TX)^{-1}X^Ty$

However, explicitly calculating the inverse is:

- computationally expensive
- numerically unstable

Instead, QR decomposition is used.

First:

$X = QR$

Substitute:

$QRw = y$

Multiply by $Q^T$:

$Rw = Q^Ty$

Now the problem becomes solving an upper triangular system, which is much more stable.

---

## QR vs Normal Equation vs Gradient Descent

| Method | Advantages | Disadvantages |
|---|---|---|
| Normal equation | Direct solution | Numerical instability, matrix inverse |
| QR decomposition | Stable and accurate | More computation |
| Gradient descent | Works for very large datasets | Requires iterations and tuning |

---

## Python Example

Using NumPy:

```python
import numpy as np

A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

Q, R = np.linalg.qr(A)

print(Q)
print(R)
```

The result satisfies:

$A \approx QR$

---

## Summary

- QR decomposition factorizes a matrix $A = QR$

- $Q$ contains orthonormal vectors
- $R$ is an upper triangular matrix
- It is more numerically stable than the normal equation
- It is commonly used behind the scenes when solving linear regression problems