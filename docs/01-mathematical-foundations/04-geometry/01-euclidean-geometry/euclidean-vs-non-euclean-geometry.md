# Euclidean vs. Non-Euclidean Geometry

## TL;DR

**Euclidean geometry** studies spaces that follow the familiar geometry of flat space, while **non-Euclidean geometry** studies spaces where Euclid's parallel postulate does not hold.

---

## Euclidean Geometry

In Euclidean geometry, space is **flat**.

For example, in a Euclidean plane:

* Parallel lines never intersect.
* The angles of a triangle sum to $180^\circ$.
* The shortest path between two points is a straight line.
* The Pythagorean theorem applies:

$$
a^2+b^2=c^2
$$

Euclidean spaces include:

$$
\mathbb{R},\quad \mathbb{R}^2,\quad \mathbb{R}^3
$$

with the usual Euclidean distance:

$$
d(x,y)=\sqrt{\sum_i (x_i-y_i)^2}.
$$

---

## Non-Euclidean Geometry

Non-Euclidean geometries describe spaces that are **curved** rather than flat.

Two important examples are:

### Spherical Geometry

On a sphere, there are no parallel lines in the Euclidean sense.

The angles of a triangle can sum to **more than** $180^\circ$.

For example, triangles formed by great circles on Earth have this property.

### Hyperbolic Geometry

In hyperbolic geometry, there can be **multiple parallel lines** through a point outside a given line.

The angles of a triangle sum to **less than** $180^\circ$.

---

## Comparison

| Property           | Euclidean   | Spherical         | Hyperbolic        |
| ------------------ | ----------- | ----------------- | ----------------- |
| Curvature          | $0$         | Positive          | Negative          |
| Parallel lines     | One         | None              | Multiple          |
| Triangle angle sum | $180^\circ$ | $>180^\circ$      | $<180^\circ$      |
| Space              | Flat        | Positively curved | Negatively curved |

---

## Why It Matters in Data Science

Many machine learning methods assume that data lies in a **Euclidean space**.

However, some data has an inherently non-Euclidean structure.

Examples include:

* **Graphs** and networks
* Hierarchical data
* Manifolds
* Geographical data on the Earth's surface

This motivates methods such as **graph neural networks**, **manifold learning**, and **hyperbolic embeddings**.
