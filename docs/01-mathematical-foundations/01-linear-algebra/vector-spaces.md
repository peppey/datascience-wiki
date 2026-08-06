# Vector Spaces

## TL;DR

A **vector space** is a mathematical structure where vectors can be added together and multiplied by scalars while following certain rules.

Vector spaces are the foundation of **linear algebra**, used in machine learning, physics, and computer science.

---

## Definition

A vector space consists of:

- a set of **vectors** `V`
- a set of **scalars** (usually real numbers `R`)

with two operations:

1. **Vector addition**
u + v = w

2. **Scalar multiplication**
a · v = w

where `a` is a scalar.

---

## Examples

### 1. Euclidean Space

The most common example is:
R² = {(x, y)}

A vector can be written as:
v = (2, 3)

Vectors represent points or directions in space.

---

### 2. Machine Learning Features

A data point can be represented as a vector:
x = (age, height, weight)

Example:
x = (25, 180, 75)

Each feature is a dimension of the vector space.

---

## Important Properties

A vector space must satisfy rules such as:

### Addition
u + v = v + u

(order does not matter)

### Zero Vector

There exists a vector:
0

such that:
v + 0 = v

### Scalar Multiplication
a(bv) = (ab)v

---

## Basis of a Vector Space

A **basis** is a set of vectors that can create every vector in the space.

Example in `R²`:
e1 = (1,0)
e2 = (0,1)


Every vector can be written as:
v = a e1 + b e2

The number of basis vectors is the **dimension** of the vector space.

---

## Vector Spaces in Machine Learning

Machine learning often represents data as vectors:
image → pixel vector
text → embedding vector

customer → feature vector


Operations such as distances, projections, and transformations are performed inside vector spaces.

---

## Key Idea

A vector space is a framework where vectors can be combined and transformed while preserving mathematical structure.
