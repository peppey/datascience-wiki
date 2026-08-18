# Norms

## TL;DR

A **norm** measures the size or magnitude of a vector or matrix.

For a vector `v`, the norm is denoted:

```
||v||
```

Common vector norms:

- **L1 norm (Manhattan):** `||v||_1 = sum(|v_i|)`
- **L2 norm (Euclidean):** `||v||_2 = sqrt(sum(v_i^2))`
- **L∞ norm (Maximum):** `||v||_∞ = max(|v_i|)`

For a matrix `A`, norms measure its magnitude:

- **Frobenius norm:** `||A||_F = sqrt(sum(a_ij^2))`
- **Spectral norm:** `||A||_2 = σ_max(A)`

Norms satisfy three key properties:
1. `||v|| >= 0` (non-negative)
2. `||cv|| = |c| ||v||` (scaling)
3. `||u + v|| <= ||u|| + ||v||` (triangle inequality)

---

## Definition

A **norm** is a function that assigns a non-negative scalar to every vector (or matrix), representing its size, length, or magnitude.

**Formal Definition:**
A norm `||·||` on a vector space `R^n` is a function satisfying:

1. **Positive definiteness:** `||v|| >= 0` for all `v`, and `||v|| = 0` if and only if `v = 0`
2. **Homogeneity:** `||cv|| = |c| ||v||` for any scalar `c`
3. **Triangle inequality:** `||u + v|| <= ||u|| + ||v||` for any vectors `u, v`

Any function satisfying these properties is a valid norm.

---

## Vector Norms

### L2 Norm (Euclidean Norm)

The **L2 norm** is the most common norm, representing the Euclidean distance from the origin.

```
||v||_2 = sqrt(sum(v_i^2)) = sqrt(v_1^2 + v_2^2 + ... + v_n^2)
```

Alternatively:

```
||v||_2 = sqrt(v^T v)
```

**Example:**

```
v = [3, 4]

||v||_2 = sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5
```

**Properties:**
- Measures straight-line distance
- Most common in machine learning and optimization
- Used in regression, neural networks, and distance computations

---

### L1 Norm (Manhattan Norm)

The **L1 norm** is the sum of absolute values, representing Manhattan (taxicab) distance.

```
||v||_1 = sum(|v_i|) = |v_1| + |v_2| + ... + |v_n|
```

**Example:**

```
v = [3, 4]

||v||_1 = |3| + |4| = 7
```

**Properties:**
- Measures distance along grid axes
- Encourages **sparsity** (many zeros) in optimization
- Used in L1 regularization (LASSO)
- More robust to outliers than L2

---

### L∞ Norm (Maximum Norm)

The **L∞ norm** is the maximum absolute value.

```
||v||_∞ = max(|v_i|)
```

**Example:**

```
v = [3, 4, -2]

||v||_∞ = max(|3|, |4|, |-2|) = 4
```

**Properties:**
- Represents the largest magnitude in the vector
- Used in uniform error bounds
- Useful for bounding maximum deviation

---

### Lp Norm (General p-norm)

The **Lp norm** generalizes all norms for any `p >= 1`:

```
||v||_p = (sum(|v_i|^p))^(1/p)
```

Special cases:
- `p = 1`: L1 norm
- `p = 2`: L2 norm
- `p = ∞`: L∞ norm (limit as `p -> ∞`)

**Example with p = 3:**

```
v = [1, 2]

||v||_3 = (|1|^3 + |2|^3)^(1/3) = (1 + 8)^(1/3) = 9^(1/3) ≈ 2.08
```

**Visualization:**
- L1: Diamond-shaped ball
- L2: Circular ball
- L∞: Square ball

---

## Matrix Norms

### Frobenius Norm

The **Frobenius norm** treats the matrix like a long vector and computes the L2 norm of all elements.

```
||A||_F = sqrt(sum(sum(a_ij^2)))
```

Equivalently:

```
||A||_F = sqrt(trace(A^T A))
```

**Example:**

```
A = [[1, 2],
     [3, 4]]

||A||_F = sqrt(1^2 + 2^2 + 3^2 + 4^2) = sqrt(1 + 4 + 9 + 16) = sqrt(30) ≈ 5.48
```

**Properties:**
- Most common matrix norm
- Easy to compute
- Useful for measuring approximation error
- Related to singular values: `||A||_F = sqrt(sum(σ_i^2))`

---

### Spectral Norm (L2 Matrix Norm)

The **spectral norm** is the largest singular value of the matrix.

```
||A||_2 = σ_max(A)
```

where `σ_max` is the largest singular value from the SVD.

Equivalently, it's the maximum magnification of any unit vector:

```
||A||_2 = max(||Av||_2) where ||v||_2 = 1
```

**Example:**

```
A = [[2, 0],
     [0, 3]]

The singular values are 3 and 2, so:
||A||_2 = 3
```

**Properties:**
- Measures maximum stretching of vectors
- Important for numerical stability
- Harder to compute than Frobenius norm
- Related to eigenvalues for symmetric matrices

---

### Matrix L1 Norm

The **matrix L1 norm** is the maximum absolute column sum.

```
||A||_1 = max_j(sum(|a_ij|))
```

**Example:**

```
A = [[1, 2],
     [3, 4]]

Column sums: |1| + |3| = 4 and |2| + |4| = 6
||A||_1 = max(4, 6) = 6
```

**Properties:**
- Column-oriented perspective
- Natural in certain applications (graph theory)
- Easier to compute than spectral norm

---

### Matrix ∞ Norm

The **matrix ∞ norm** is the maximum absolute row sum.

```
||A||_∞ = max_i(sum(|a_ij|))
```

**Example:**

```
A = [[1, 2],
     [3, 4]]

Row sums: |1| + |2| = 3 and |3| + |4| = 7
||A||_∞ = max(3, 7) = 7
```

**Properties:**
- Row-oriented perspective
- Dual to the L1 norm
- Used in error analysis and perturbation bounds

---

## Geometric Intuition

**Vector Norms:**

Imagine a vector as an arrow in space. Different norms measure the "length" differently:

- **L2 norm:** Straight-line distance (Euclidean)
- **L1 norm:** Grid distance (Manhattan)
- **L∞ norm:** Maximum coordinate distance (Chebyshev)

For the same vector, the norms satisfy:

```
||v||_∞ <= ||v||_2 <= ||v||_1
```

**Matrix Norms:**

A matrix transforms vectors. The matrix norm measures how much the matrix can stretch vectors:

- **Frobenius norm:** Total "energy" of the transformation
- **Spectral norm:** Maximum possible stretching
- **L1 and ∞ norms:** Column and row perspectives

---

## Norm Relationships

For a vector `v` in `R^n`:

```
(1/sqrt(n)) ||v||_2 <= ||v||_∞ <= ||v||_2

(1/n) ||v||_1 <= ||v||_2 <= ||v||_1

||v||_∞ <= ||v||_2 <= sqrt(n) ||v||_∞
```

These relationships show how different norms compare.

For a matrix `A` in `R^(m x n)`:

```
(1/sqrt(m)) ||A||_F <= ||A||_2 <= ||A||_F

||A||_2 <= sqrt(||A||_1 ||A||_∞)
```

---

## Properties of Norms

All norms satisfy the **norm axioms**:

| Property | Formula |
|---|---|
| Non-negativity | `||v|| >= 0`, with equality iff `v = 0` |
| Homogeneity | `||cv|| = |c| ||v||` |
| Triangle inequality | `||u + v|| <= ||u|| + ||v||` |

**Additional properties:**

| Property | Formula |
|---|---|
| Reverse triangle inequality | `|||u|| - ||v||| <= ||u - v||` |
| Matrix-vector multiplication | `||Av|| <= ||A|| ||v||` |
| Matrix product | `||AB|| <= ||A|| ||B||` |
| Equivalence of norms | All norms on `R^n` are equivalent |

---

## Induced Norms

A **matrix norm** is **induced** by a vector norm if:

```
||A|| = max(||Av||) where ||v|| = 1
```

The induced norms are:
- **Spectral norm (L2):** Induced by L2 vector norm
- **Matrix L1:** Induced by L1 vector norm
- **Matrix ∞:** Induced by L∞ vector norm

The **Frobenius norm is NOT induced** by any vector norm.

---

## Applications

### Machine Learning

**Regularization:**
- **L1 regularization:** Encourages sparse solutions (feature selection)
- **L2 regularization:** Encourages small weights (weight decay)

```
min_w (1/2)||Xw - y||_2^2 + λ ||w||_1
```

### Optimization

**Convergence criteria:**
Algorithms stop when:

```
||∇f(x)|| < ε
```

**Trust region methods:**
Restrict step size using:

```
||s|| <= Δ
```

### Numerical Analysis

**Error bounds:**
The condition number uses spectral norm:

```
κ(A) = ||A||_2 ||A^(-1)||_2
```

**Perturbation analysis:**
How noise affects solutions:

```
(||Δx|| / ||x||) <= κ(A) (||ΔA|| / ||A||)
```

### Signal Processing

**Signal magnitude:**
L2 norm represents signal energy.

**Sparsity promotion:**
L1 norm encourages sparse representations (compressed sensing).

### Graph Theory

Matrix norms measure properties of adjacency matrices and network structure.

---

## Summary

| Norm | Formula | Intuition | Common Use |
|---|---|---|---|
| **L1** | `sum(|v_i|)` | Manhattan distance | Sparsity, LASSO |
| **L2** | `sqrt(sum(v_i^2))` | Euclidean distance | Regression, ML |
| **L∞** | `max(|v_i|)` | Maximum distance | Bounds, Chebyshev |
| **Lp** | `(sum(|v_i|^p))^(1/p)` | General p-norm | Theoretical analysis |
| **Frobenius** | `sqrt(sum(a_ij^2))` | Total magnitude | Approximation error |
| **Spectral** | `σ_max(A)` | Max stretching | Stability, condition |
| **Matrix L1** | `max_j(sum(|a_ij|))` | Column sums | Network analysis |
| **Matrix ∞** | `max_i(sum(|a_ij|))` | Row sums | Error bounds |

Norms quantify size and distance, enabling robust algorithms, stability analysis, and optimization across mathematics, engineering, and machine learning.
