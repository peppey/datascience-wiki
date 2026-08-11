# Laplacian

## TL;DR

The **Laplacian** is a second-order differential operator that measures how a scalar function differs from its local surroundings.

For a function $f:\mathbb{R}^n\to\mathbb{R}$:

$$
\Delta f
=

\nabla^2 f

\sum_{i=1}^{n}
\frac{\partial^2 f}{\partial x_i^2}.
$$

It is fundamental in **vector calculus, PDEs, physics, and machine learning**.

---

## Definition

For a function:

$$
f(x_1,\ldots,x_n),
$$

the Laplacian is:

$$
\boxed{
\Delta f
=

\sum_{i=1}^{n}
\frac{\partial^2 f}{\partial x_i^2}
}
$$

In three-dimensional Cartesian coordinates:

$$
\Delta f
=

\frac{\partial^2f}{\partial x^2}
+
\frac{\partial^2f}{\partial y^2}
+
\frac{\partial^2f}{\partial z^2}.
$$

---

## Gradient

For a scalar function $f:\mathbb{R}^n\to\mathbb{R}$, the **gradient** is the vector of first partial derivatives:

$$
\nabla f
=

\begin{pmatrix}
\frac{\partial f}{\partial x_1}\
\vdots\
\frac{\partial f}{\partial x_n}
\end{pmatrix}.
$$

It points in the direction of the **steepest increase** of $f$.

---

## Divergence

The **divergence** measures the net tendency of a vector field to flow outward from a point.

For a vector field:

$$
\mathbf{F}
=

(F_1,\ldots,F_n),
$$

the divergence is:

$$
\boxed{
\nabla\cdot\mathbf{F}
=

\sum_{i=1}^{n}
\frac{\partial F_i}{\partial x_i}
}
$$

For example, in three dimensions:

$$
\nabla\cdot\mathbf{F}
=

\frac{\partial F_x}{\partial x}
+
\frac{\partial F_y}{\partial y}
+
\frac{\partial F_z}{\partial z}.
$$

A positive divergence indicates a local **source**, while a negative divergence indicates a local **sink**.

---

## Relation to the Gradient

The Laplacian is the **divergence of the gradient**:

$$
\boxed{
\Delta f
========

\nabla\cdot(\nabla f)
}
$$

Since the gradient contains first derivatives and the divergence differentiates them again, the Laplacian contains second derivatives.

---

## Example

For:

$$
f(x,y)=x^2+y^2,
$$

the gradient is:

$$
\nabla f
=

\begin{pmatrix}
2x\
2y
\end{pmatrix}.
$$

Taking the divergence:

$$
\nabla\cdot(\nabla f)
=

\frac{\partial(2x)}{\partial x}
+
\frac{\partial(2y)}{\partial y}
=
2+2=4.
$$

Therefore:

$$
\Delta f=4.
$$

---

## Harmonic Functions

A function is **harmonic** if:

$$
\Delta f=0.
$$

Such functions satisfy **Laplace's equation**:

$$
\boxed{\Delta f=0}.
$$

Harmonic functions occur frequently in potential theory and steady-state physical systems.

---

## Laplace and Poisson Equations

The **Poisson equation** has the form:

$$
\Delta f=g.
$$

Laplace's equation is the special case:

$$
g=0.
$$

These are fundamental elliptic PDEs.

---

## Physical Interpretation

The Laplacian often describes how a quantity diffuses or spreads.

For example, the heat equation can be written as:

$$
\frac{\partial u}{\partial t}
=

\alpha\Delta u.
$$

Regions where:

$$
\Delta u>0
$$

tend to increase under diffusion, while regions where:

$$
\Delta u<0
$$

tend to decrease.

---

## Other Coordinate Systems

The expression for the Laplacian depends on the coordinate system.

For example, in two-dimensional polar coordinates:

$$
\Delta f
=

\frac{\partial^2f}{\partial r^2}
+
\frac{1}{r}\frac{\partial f}{\partial r}
+
\frac{1}{r^2}
\frac{\partial^2 f}{\partial\theta^2}.
$$

---

## Discrete Laplacian

For numerical computations, the Laplacian can be approximated using finite differences.

In one dimension:

$$
f''(x)
\approx
\frac{
f(x+h)-2f(x)+f(x-h)
}{h^2}.
$$

This leads to the **discrete Laplacian**, which is widely used in numerical PDEs, image processing, and graph-based methods.

---

## Key Idea

The Laplacian combines the second partial derivatives of a function:

$$
\boxed{
\Delta f
=

\nabla\cdot(\nabla f)
}
$$

The gradient produces a vector field from a scalar function, and the divergence measures the local outflow of that vector field.
