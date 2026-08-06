# Euclidean Space

## TL;DR

A **Euclidean space** is a vector space where points have coordinates and distances can be measured using the standard geometry we know from everyday life.

The most common examples are:
- R² → 2-dimensional space
- R³ → 3-dimensional space

---

## Definition

An `n`-dimensional Euclidean space is written as:
Rⁿ

A point or vector is represented by:
x = (x₁, x₂, ..., xₙ)

Example:
x = (2, 5, 3)

represents a point in three-dimensional space.

---

## Distance

The distance between two points is calculated using the Euclidean distance:

d(x,y) = sqrt((x₁-y₁)² + (x₂-y₂)² + ... + (xₙ-yₙ)²)

Example in 2D:
- x = (1,2)
- y = (4,6)


Distance:

d = sqrt((4-1)² + (6-2)²)

---

## Euclidean Norm

The length of a vector is called the **Euclidean norm**:

||x|| = sqrt(x₁² + x₂² + ... + xₙ²)

Example:
- x = (3,4)
- ||x|| = 5


This is the same idea as the Pythagorean theorem.

---

## Inner Product

Euclidean spaces use the standard dot product:

x · y = x₁y₁ + x₂y₂ + ... + xₙyₙ

The dot product allows us to measure:

- angles between vectors
- similarity
- projections

---

## Euclidean Space in Machine Learning

Many ML algorithms represent data as points in Euclidean space.

Example:
customer = (age, income, purchases)

Each feature corresponds to one dimension.

Distances in this space are used for:

- k-nearest neighbors (KNN)
- clustering
- anomaly detection
- dimensionality reduction

---

## Euclidean Space vs Vector Space

A vector space describes the operations on vectors:
addition + scalar multiplication

A Euclidean space adds geometric concepts:
distance + angles + lengths

Therefore:
Euclidean space = vector space + inner product

---

## Key Idea

Euclidean spaces provide the mathematical foundation for geometry in multiple dimensions and are the standard way to represent numerical data in machine learning.
