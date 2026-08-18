# Eigenvectors and Eigenvalues

## TL;DR

**Eigenvectors** are vectors that do not change their direction when a linear transformation is applied. 

The corresponding scaling factor is called the **eigenvalue**.

They are important for:
- PCA (Principal Component Analysis)
- dimensionality reduction
- matrix decompositions
- dynamical systems

---

## Definition

For a matrix $A$, an eigenvector $v$ satisfies:

$$
Av = \lambda v
$$

where:

- $A$ is a square matrix
- $v$ is an eigenvector
- $\lambda$ is the eigenvalue

This means that applying $A$ to $v$ only scales the vector but does not change its direction.

---

## Intuition

Most vectors change both **length and direction** after a transformation.

Eigenvectors are special: The direction stays the same, only the length changes.

---

## Finding Eigenvalues

Eigenvalues can be found by solving:

$$
det(A - \lambda I) = 0
$$

This equation is called the **characteristic equation**.

Once an eigenvalue is known, the corresponding eigenvector can be found by solving:

$$
(A - \lambda I)v = 0
$$

---

## Example

Given:

$$
A =
\begin{bmatrix}
2 & 0 \\
0 & 3
\end{bmatrix}
$$

The vectors:

$$
v_1 =
\begin{bmatrix}
1\\
0
\end{bmatrix}
$$

and

$$
v_2 =
\begin{bmatrix}
0\\
1
\end{bmatrix}
$$

are eigenvectors.

They are scaled by:

$$
\lambda_1 = 2
$$

and

$$
\lambda_2 = 3
$$

---

## Summary

| Concept | Meaning |
|---|---|
| Eigenvector | Direction unchanged by a transformation |
| Eigenvalue | Scaling factor of an eigenvector |
| Equation | $Av=\lambda v$ |
| PCA | Uses eigenvectors of covariance matrices |
