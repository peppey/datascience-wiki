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
2 & 0\
0 & 3
\end{bmatrix}
$$

The inverse is:

$$
A^{-1}=
\begin{bmatrix}
\frac{1}{2} & 0\
0 & \frac{1}{3}
\end{bmatrix}
$$

Multiplying them:

$$
AA^{-1}
=======

\begin{bmatrix}
1 & 0\
0 & 1
\end{bmatrix}
=I
$$

The transformation is reversed.

---

## Geometric Intuition

A matrix represents a transformation of space.

The inverse performs the opposite transformation:

* scaling by $2$ → scaling by $\frac{1}{2}$
* rotation clockwise → rotation counterclockwise
* stretching → shrinking

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

For **small matrices**, the inverse can be computed directly using formulas.

### $2\times2$ Matrix

For

$$
A=
\begin{bmatrix}
a & b\\
c & d
\end{bmatrix}
$$


the determinant is:

$$
\det(A)=ad-bc
$$

If $ad-bc\neq0$, the inverse is:

$$
\boxed{
A^{-1}
=

\frac{1}{ad-bc}
\begin{bmatrix}
d & -b\\
-c & a
\end{bmatrix}

}
$$

For example:

$$
A=
\begin{bmatrix}
2 & 1\
1 & 1
\end{bmatrix}
$$

has determinant:

$$
\det(A)=2\cdot1-1\cdot1=1
$$

Therefore:

$$
A^{-1}
=

\begin{bmatrix}
1 & -1\
-1 & 2
\end{bmatrix}
$$

### $3\times3$ Matrix

For a $3\times3$ matrix, the inverse can be computed using the **adjugate matrix**:

$$
\boxed{
A^{-1}
=

\frac{1}{\det(A)}\operatorname{adj}(A)
}
$$

The adjugate is obtained from the matrix of **cofactors**, followed by transposition.

For larger matrices, calculating the inverse explicitly by this formula becomes cumbersome.

---

## Computing the Adjugate

For a matrix $A$, the minor $M_{ij}$ is the determinant of the matrix obtained by deleting row $i$ and column $j$.
The cofactor is:
$$
C_{ij}=(-1)^{i+j}M_{ij}
$$
The cofactor matrix is:
$$
C=
\begin{bmatrix}
C_{11} & C_{12} & \cdots\\
C_{21} & C_{22} & \cdots\\
\vdots & \vdots & \ddots
\end{bmatrix}

$$The adjugate is the transpose of the cofactor matrix:
$$
\boxed{
\operatorname{adj}(A)=C^T
}
$$
For a $3\times3$ matrix:
$$
A=
\begin{bmatrix}
a & b & c\\
d & e & f\\
g & h & i
\end{bmatrix}
$$
the cofactor matrix is:
$$
C=
\begin{bmatrix}
ei-fh & -(di-fg) & dh-eg\\
-(bi-ch) & ai-cg & -(ah-bg)\\
bf-ce & -(af-cd) & ae-bd
\end{bmatrix}
$$
Therefore:
$$
\operatorname{adj}(A)=C^T
$$
and finally:

$$
\frac{1}{\det(A)}
\operatorname{adj}(A)
$$
This method is useful for understanding the formula, but is usually inefficient for large matrices.



---

## Practical Computation

For larger matrices, numerical methods are preferred, such as:

* **Gaussian elimination**
* **LU decomposition**
* **QR decomposition**
* **Singular Value Decomposition (SVD)**

In practice, the inverse is often **not explicitly computed**. Instead, systems such as

$$
Ax=b
$$

are solved directly using decomposition methods.

---

## Summary

| Property                | Matrix Inverse                                         |
| ----------------------- | ------------------------------------------------------ |
| Notation                | $A^{-1}$                                               |
| Exists when             | $\det(A)\neq0$                                         |
| Reverses transformation | Yes                                                    |
| Singular matrix         | No inverse                                             |
| Common applications     | Solving linear systems, transformations, optimization  |

The inverse matrix allows us to undo a linear transformation and recover the original input.
