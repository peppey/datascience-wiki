# Change of Basis

## TL;DR

A **change of basis** expresses the same vector or linear transformation using a different basis.

The geometric object stays the same; only its **coordinates** change.

---

## Basis

A basis of a vector space is a set of linearly independent vectors that spans the entire space.

For example, the standard basis of $\mathbb{R}^2$ is

$$
E =
\left\{
\begin{pmatrix}
1\\
0
\end{pmatrix},
\begin{pmatrix}
0\\
1
\end{pmatrix}
\right\}.
$$
Another basis could be

$$
B =
\left\{
\begin{pmatrix}
1\\
1
\end{pmatrix},
\begin{pmatrix}
1\\
-1
\end{pmatrix}
\right\}.
$$
---

## Coordinate Representation

A vector has different coordinate representations depending on the chosen basis.

For example, a vector $v$ can be written as

$$
v = x_1 b_1 + x_2 b_2
$$

with coordinates

$$
[v]_B =
\begin{pmatrix}
x_1\
x_2
\end{pmatrix}.
$$

The vector itself does not change when the basis changes.

---

## Change-of-Basis Matrix

Suppose $B = (b_1,\ldots,b_n)$ is a new basis and $E$ is the standard basis.

Construct the matrix

$$
P_{E\leftarrow B}
=
\begin{pmatrix}
| & & |\\
b_1 & \cdots & b_n\\
| & & |
\end{pmatrix}.
$$

It converts coordinates from basis $B$ to basis $E$:

$$
[v]_E
=

P_{E\leftarrow B}[v]_B.
$$

The inverse conversion is

$$
[v]_B
=

P_{E\leftarrow B}^{-1}[v]_E.
$$

---

## General Change of Basis

For two arbitrary bases $B$ and $C$, the change-of-basis matrix is

$$
P_{C\leftarrow B}
=

P_{E\leftarrow C}^{-1}P_{E\leftarrow B}.
$$

Therefore,

$$
[v]_C
=

P_{C\leftarrow B}[v]_B.
$$
