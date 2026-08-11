# Curves

## TL;DR

In **differential geometry**, a curve is a smooth map from an interval into a geometric space:

$$
\gamma:I\to\mathbb{R}^n.
$$

Curves provide the basic objects for studying **velocity, acceleration, arc length, curvature, and torsion**.

---

## Parametric Curve

A curve is represented by a parameter $t$:

$$
\gamma(t)
=

\begin{pmatrix}
x_1(t)\
\vdots\
x_n(t)
\end{pmatrix}.
$$

For example, a circle can be parameterized as:

$$
\gamma(t)
=

\begin{pmatrix}
\cos t\
\sin t
\end{pmatrix},
\qquad
t\in[0,2\pi].
$$

Different parameterizations can describe the same geometric curve.

---

## Regular Curves

A curve is **regular** if:

$$
\gamma'(t)\neq0
$$

for every $t$ in its domain.

The derivative:

$$
\gamma'(t)
$$

is the **tangent vector** to the curve.

The corresponding unit tangent vector is:

$$
T(t)
=

\frac{\gamma'(t)}
{|\gamma'(t)|}.
$$

---

## Velocity and Acceleration

For a parameterized curve:

$$
\gamma(t),
$$

the first derivative is the **velocity**:

$$
v(t)=\gamma'(t),
$$

and the second derivative is the **acceleration**:

$$
a(t)=\gamma''(t).
$$

The speed is:

$$
|\gamma'(t)|.
$$

---

## Arc Length

The length of a curve between $a$ and $b$ is:

$$
L
=

\int_a^b
|\gamma'(t)|,dt.
$$

A parameterization is called **unit-speed** or **arc-length parameterized** if:

$$
|\gamma'(t)|=1.
$$

Then the parameter directly measures distance along the curve.

---

## Curvature

The **curvature** measures how rapidly a curve changes its direction.

For a unit-speed curve:

$$
\boxed{
\kappa(s)=|T'(s)|
}
$$

For a general regular curve:

$$
\kappa(t)
=

\frac{
|\gamma'(t)\times\gamma''(t)|
}{
|\gamma'(t)|^3
}
$$

in $\mathbb{R}^3$.

A straight line has:

$$
\kappa=0.
$$

A circle with radius $r$ has constant curvature:

$$
\kappa=\frac1r.
$$

---

## Frenet Frame

For a sufficiently smooth curve in $\mathbb{R}^3$, the **Frenet frame** consists of:

* tangent vector $T$
* normal vector $N$
* binormal vector $B$

defined by:

$$
T=\frac{\gamma'}{|\gamma'|},
$$

$$
N=\frac{T'}{|T'|},
$$

and:

$$
B=T\times N.
$$

These vectors describe the local geometry of the curve.

---

## Torsion

The **torsion** measures how much a curve twists out of its osculating plane.

For a regular curve in $\mathbb{R}^3$:

$$
\tau
====

\frac{
(\gamma'\times\gamma'')\cdot\gamma'''
}{
|\gamma'\times\gamma''|^2
}.
$$

A planar curve has:

$$
\tau=0.
$$

---

## Curves on Manifolds

Curves can also be defined on a manifold $M$:

$$
\gamma:I\to M.
$$

Their derivatives are tangent vectors:

$$
\gamma'(t)\in T_{\gamma(t)}M.
$$

This provides the connection between curves and **tangent spaces** in differential geometry.

---

## Key Idea

A curve is a smooth map:

$$
\boxed{
\gamma:I\to M
}
$$

and its derivatives describe increasingly detailed local geometry:

$$
\boxed{
\text{Tangent}
\rightarrow
\text{Curvature}
\rightarrow
\text{Torsion}
}
$$
