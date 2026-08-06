# Basis

## TL;DR

A **basis** is a set of vectors that can represent every vector in a vector space uniquely.

A basis must satisfy two properties:

- **Linear independence**: No vector can be written as a combination of the others.
- **Spanning**: Every vector in the space can be created from the basis vectors.

---

## Definition

A basis of a vector space \(V\) is a set of vectors:
B = {v₁, v₂, ..., vₙ}

such that every vector:
x ∈ V

can be written as:
x = a₁v₁ + a₂v₂ + ... + aₙvₙ

where the coefficients `a₁, ..., aₙ` are unique.

---

## Example

The standard basis of **R²** is:
e₁ = (1, 0)
e₂ = (0, 1)

Every vector:
x = (3, 5)

can be represented as:
x = 3e₁ + 5e₂

---

## Dimension

The number of vectors in a basis defines the **dimension** of the vector space.

Example:
R² → 2 basis vectors
R³ → 3 basis vectors

---

## Change of Basis

A vector can be represented using different bases.

Changing the basis changes the coordinates, but not the underlying vector.

---

## Applications

Bases are used in:

- Linear algebra
- Machine learning feature spaces
- Eigenvector decompositions
- Dimensionality reduction (e.g. PCA)
- Coordinate transformations
