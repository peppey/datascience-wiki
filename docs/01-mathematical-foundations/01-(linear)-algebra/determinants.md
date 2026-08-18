# Determinants

## TL;DR

The **determinant** is a scalar value that describes important properties of a square matrix:

- whether a matrix is invertible
- how a transformation changes volume
- whether vectors are linearly independent

---

## Definition

For a square matrix $A$, the determinant is written as:

$$
\det(A)
$$

The determinant maps a matrix to a single number.

Example for a $2 \times 2$ matrix:

$$
A =
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

The determinant is:

$$
\det(A)=ad-bc
$$

---

## Geometric Intuition

A matrix represents a linear transformation.

The determinant describes how this transformation changes volume:

- $|\det(A)| > 1$ → volume is expanded
- $0 < |\det(A)| < 1$ → volume is reduced
- $\det(A)=0$ → volume collapses

Example:

```text
Before transformation:

+------+
|      |
|      |
|      |
+------+

After transformation:

+------------+
|            |
|            |
+------------+
```

The determinant measures the scaling factor of the area (2D) or volume (3D).

# Determinant and Invertibility

## TL;DR

The **determinant** is a scalar value that describes important properties of a square matrix:

- whether a matrix is invertible
- how a transformation changes volume
- whether vectors remain linearly independent

A matrix is invertible **if and only if** its determinant is not zero.

---

## Definition

For a square matrix $A$, the determinant is written as:

$$
\det(A)
$$

It maps a matrix to a single number.

Example:

$$
A =
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

has determinant:

$$
\det(A)=ad-bc
$$

---

## Determinant and Invertibility

A matrix has an inverse if:

$$
A^{-1}
$$

exists such that:

$$
AA^{-1}=I
$$

A matrix is invertible exactly when:

$$
\det(A)\neq 0
$$

If:

$$
\det(A)=0
$$

the matrix is **singular** and no inverse exists.

---

## Geometric Intuition

A matrix represents a linear transformation.

The determinant describes how this transformation changes volume.

For example:

- $\det(A)=2$ → volume doubles
- $\det(A)=0.5$ → volume is reduced by half
- $\det(A)=0$ → the space collapses into a lower dimension

If a transformation collapses dimensions, information is lost and the inverse cannot exist.

---

## Connection to Linear Independence

The columns of a matrix represent vectors.

If the columns are linearly independent:

$$
\det(A)\neq 0
$$

the vectors span the whole space.

If they are dependent:

$$
\det(A)=0
$$

the vectors lie in a lower-dimensional space.

Example:

Two vectors that point in the same direction cannot span a 2D plane.

Therefore, the matrix cannot be inverted.

---

## Example

Consider:

$$
A=
\begin{bmatrix}
1 & 2\\
3 & 6
\end{bmatrix}
$$

The determinant is:

$$
\det(A)=1\cdot6-2\cdot3
$$

$$
=6-6=0
$$

The matrix is not invertible because the second column is just:

$$
2 \cdot
\begin{bmatrix}
1\\
3
\end{bmatrix}
$$

The columns are linearly dependent.

---

## Summary

| Property | Determinant |
|---|---|
| Invertible matrix | $\det(A)\neq0$ |
| Singular matrix | $\det(A)=0$ |
| Volume preserved | $\operatorname{abs}(\det(A))=1$ |
| Volume scaling | $\operatorname{abs}(\det(A))$ |
| Linear independence | $\det(A)\neq0$ |

The determinant tells us whether a linear transformation keeps all information or loses dimensions.