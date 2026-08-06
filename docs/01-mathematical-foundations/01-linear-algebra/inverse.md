# Matrix Inverse

## TL;DR

The **inverse of a matrix** reverses the effect of a linear transformation.

For a square matrix $A$, the inverse is written as:

$$
A^{-1}
$$

and satisfies:

$$
AA^{-1}=A^{-1}A=I
$$

where $I$ is the identity matrix.

A matrix has an inverse **only if**:

$$
\det(A)\neq0
$$

---

## Definition

The inverse matrix transforms the output of a linear transformation back to the original input.

If:

$$
Ax=b
$$

then multiplying both sides by the inverse gives:

$$
A^{-1}Ax=A^{-1}b
$$

Because:

$$
A^{-1}A=I
$$

we get:

$$
x=A^{-1}b
$$

---

## Example

Consider the matrix:

$$
A=
\begin{bmatrix}
2 & 0\\
0 & 3
\end{bmatrix}
$$

The inverse is:

$$
A^{-1}=
\begin{bmatrix}
\frac{1}{2} & 0\\
0 & \frac{1}{3}
\end{bmatrix}
$$

Multiplying them:

$$
AA^{-1}
=
\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix}
=I
$$

The transformation is reversed.

---

## Geometric Intuition

A matrix represents a transformation of space.

The inverse performs the opposite transformation:

- scaling by 2 → scaling by $\frac{1}{2}$
- rotation clockwise → rotation counterclockwise
- stretching → shrinking

Applying a matrix and then its inverse returns the original vector.

---

## Connection to Determinants

A matrix is invertible if and only if:

$$
\det(A)\neq0
$$

If:

$$
\det(A)=0
$$

the transformation loses information.

For example, a 2D space could be compressed into a line. Since information is lost, the original input cannot be recovered.

---

## Computing the Inverse

For small matrices, the inverse can be computed using formulas.

For larger matrices, numerical methods are preferred, such as:

- Gaussian elimination
- LU decomposition
- QR decomposition
- Singular Value Decomposition (SVD)

In practice, the inverse is often **not explicitly computed**. Instead, systems like:

$$
Ax=b
$$

are solved directly using decomposition methods.

---

## Summary

| Property | Matrix Inverse |
|---|---|
| Notation | $A^{-1}$ |
| Exists when | $\det(A)\neq0$ |
| Reverses transformation | Yes |
| Singular matrix | No inverse |
| Common applications | Solving linear systems, transformations, optimization |

The inverse matrix allows us to undo a linear transformation and recover the original input.