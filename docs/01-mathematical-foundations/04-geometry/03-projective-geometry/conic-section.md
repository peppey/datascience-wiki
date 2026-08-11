# Conic Sections

## TL;DR

A **conic section** is a curve obtained by intersecting a plane with a cone.

In **projective geometry**, all non-degenerate conics are fundamentally the same: they can be transformed into one another by projective transformations.

A conic can be represented by a homogeneous quadratic equation

$$
ax^2+bxy+cy^2+dxz+eyz+fz^2=0.
$$

## Conics in Projective Geometry

Projective geometry uses **homogeneous coordinates**. A point is represented as

$$
[x:y:z],
$$

where multiplying all coordinates by the same non-zero scalar does not change the point.

A conic is therefore represented by a homogeneous quadratic equation in $x$, $y$, and $z$.

It can also be written as

$$
x^T Qx=0,
$$

where $Q$ is a symmetric $3\times3$ matrix.

## Examples

The three classical non-degenerate conics are:

* **Ellipse**
* **Parabola**
* **Hyperbola**

In Euclidean geometry, these curves are distinct.

In projective geometry, however, they are different coordinate representations of the same type of geometric object.

For example, a circle can be written as

$$
x^2+y^2-z^2=0.
$$

A parabola can be written as

$$
xz-y^2=0.
$$

These can be transformed into each other using suitable projective transformations.

## Points at Infinity

One important difference between Euclidean and projective geometry is the treatment of **parallel lines**.

In projective geometry, parallel lines intersect at a **point at infinity**.

This means that a conic can be studied together with its points at infinity, which explains some of the differences between ellipses, parabolas, and hyperbolas in Euclidean geometry.

For example:

* an ellipse has no real points at infinity
* a parabola has one real point at infinity
* a hyperbola has two real points at infinity

## Degenerate Conics

A quadratic equation can also describe a **degenerate conic**, such as two intersecting lines.

For example,

$$
xy=0
$$

represents the union of the two lines

$$
x=0
$$

and

$$
y=0.
$$

Degenerate conics are important when studying projective transformations and intersections.

## Applications

Conics play an important role in:

* projective geometry
* computer vision
* camera calibration
* geometric transformations
* algebraic geometry
* computer graphics