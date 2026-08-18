# Scalar and Cross Product

## TL;DR

The **scalar product** and **cross product** are two ways of multiplying vectors.

* **Scalar product (dot product)** → produces a **scalar**
* **Cross product** → produces a **vector** in $\mathbb{R}^3$

$$
\boxed{
\text{Vector}\cdot\text{Vector}
\rightarrow
\text{Scalar}
}
$$

$$
\boxed{
\text{Vector}\times\text{Vector}
\rightarrow
\text{Vector}
}
$$

---

## Scalar Product

For two vectors $a,b\in\mathbb{R}^n$:

$$
\boxed{
a\cdot b
=
\sum_{i=1}^{n}a_i b_i
}
$$

For example:

$$
\begin{pmatrix}
1\
2
\end{pmatrix}
\cdot
\begin{pmatrix}
3\
4
\end{pmatrix}
=
1\cdot3+2\cdot4
=11
$$

Geometrically:

$$
a\cdot b
=

|a||b|\cos(\theta)
$$

where $\theta$ is the angle between the vectors.

Therefore:

$$
a\cdot b=0
\iff
a\perp b
$$

The scalar product is commonly used for **angles, projections, vector lengths, orthogonality, and cosine similarity**.

---

## Cross Product

The **cross product** is defined for vectors in $\mathbb{R}^3$.

For

$$
a=
\begin{pmatrix}
a_1\
a_2\
a_3
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
b_1\
b_2\
b_3
\end{pmatrix}
$$

the cross product is:

$$
\boxed{
a\times b
=

\begin{pmatrix}
a_2b_3-a_3b_2\
a_3b_1-a_1b_3\
a_1b_2-a_2b_1
\end{pmatrix}
}
$$

The result is a vector that is **perpendicular to both** $a$ and $b$.

Its magnitude is:

$$
\boxed{
|a\times b|
=

|a||b|\sin(\theta)
}
$$

This magnitude corresponds to the **area of the parallelogram** spanned by the two vectors.

---

## Direction of the Cross Product

The direction of $a\times b$ is determined by the **right-hand rule**.

Importantly, the cross product is **anti-commutative**:

$$
\boxed{
a\times b=-(b\times a)
}
$$

In contrast, the scalar product is commutative:

$$
a\cdot b=b\cdot a
$$

---

## Scalar vs. Cross Product

| Property                | Scalar Product         | Cross Product        |
| ----------------------- | ---------------------- | -------------------- |
| Notation                | $a\cdot b$             | $a\times b$          |
| Input                   | Vectors                | Vectors              |
| Output                  | Scalar                 | Vector               |
| Dimensions              | $\mathbb{R}^n$         | $\mathbb{R}^3$       |
| Depends on              | $\cos(\theta)$         | $\sin(\theta)$       |
| Result is perpendicular | No                     | Yes                  |
| Zero when               | Vectors are orthogonal | Vectors are parallel |

---

## Key Idea

The two products capture different geometric relationships:

$$
\boxed{
a\cdot b
=

|a||b|\cos(\theta)
}
$$

measures how much two vectors point in the **same direction**, while

$$
\boxed{
|a\times b|
=

|a||b|\sin(\theta)
}
$$

measures the **area spanned by them**.

Together, they provide fundamental tools for geometry, physics, and linear algebra.
