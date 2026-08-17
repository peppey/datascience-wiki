# Pseudoinverse

## TL;DR

The **pseudoinverse**, also called the **Moore-Penrose pseudoinverse**, extends the concept of a matrix inverse to matrices that are not square or not invertible.

It is denoted by:

$$
A^+
$$

For an invertible square matrix:

$$
A^+=A^{-1}
$$

The pseudoinverse is particularly useful for solving **linear systems** and **least-squares problems**.

---

## Motivation

A normal inverse only exists for a square, invertible matrix.

For example, consider:

$$
Ax=b
$$

If $A$ is not square, or if $A$ is singular, $A^{-1}$ does not exist.

The pseudoinverse provides a generalized solution:

$$
\boxed{
x=A^+b
}
$$

---

## Least-Squares Solution

Consider an overdetermined system:

$$
Ax=b
$$

where there are more equations than unknowns.

Usually, there is no exact solution. Instead, we search for $x$ that minimizes the squared error:

$$
\boxed{
\min_x|Ax-b|^2
}
$$

The pseudoinverse gives the least-squares solution:

$$
\boxed{
x=A^+b
}
$$

This is widely used in **linear regression**.

---

## Computing the Pseudoinverse

For a matrix with **full column rank**, the pseudoinverse can be computed as:

$$
\boxed{
A^+=(A^TA)^{-1}A^T
}
$$

For a matrix with **full row rank**:

$$
\boxed{
A^+=A^T(AA^T)^{-1}
}
$$

These formulas are useful theoretically, but are not always numerically stable.

---

## Singular Value Decomposition

A general and numerically robust way to compute the pseudoinverse is using the **Singular Value Decomposition (SVD)**.

If:

$$
A=U\Sigma V^T
$$

then:

$$
\boxed{
A^+=V\Sigma^+U^T
}
$$

where $\Sigma^+$ is obtained by:

1. Taking the reciprocal of every non-zero singular value.
2. Transposing the resulting matrix.
3. Keeping zero singular values as zero.

---

## Example

Consider:

$$
A=
\begin{bmatrix}
1 & 0\
0 & 2\
1 & 1
\end{bmatrix}
$$

This is a $3\times2$ matrix, so a regular inverse does not exist.

If $A$ has full column rank, its pseudoinverse is:

$$
A^+=(A^TA)^{-1}A^T
$$

It can then be used to find the least-squares solution of:

$$
Ax=b
$$

by computing:

$$
x=A^+b
$$

---

## Properties

The Moore-Penrose pseudoinverse satisfies the four **Penrose conditions**:

$$
AA^+A=A
$$

$$
A^+AA^+=A^+
$$

$$
(AA^+)^T=AA^+
$$

$$
(A^+A)^T=A^+A
$$

These conditions uniquely define the Moore-Penrose pseudoinverse.

---

## Applications

The pseudoinverse is commonly used for:

* **Linear regression**
* **Least-squares problems**
* Solving underdetermined or overdetermined systems
* Numerical linear algebra
* Signal processing
* Machine learning

---

## Key Idea

$$
\boxed{
\text{Inverse}
\rightarrow
\text{Square and invertible matrices}
}
$$

$$
\boxed{
\text{Pseudoinverse}
\rightarrow
\text{General matrices}
}
$$

The pseudoinverse generalizes matrix inversion and provides a principled way to solve linear systems when an ordinary inverse does not exist.
