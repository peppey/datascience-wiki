# Principal Component Analysis (PCA)

## TL;DR

**Principal Component Analysis (PCA)** is a dimensionality reduction technique that transforms data into a new coordinate system where the directions with the most variance are the principal components.

It is often used to reduce high-dimensional data while preserving important information.

---

## Idea

PCA finds new axes (**principal components**) that capture the maximum variance in the data.

The first component explains the most variance, the second the second most, and so on.

Example:
Original features:
x₁, x₂, x₃, x₄

↓

Principal components:

PC1, PC2


The data can be represented using fewer dimensions.

---

## Steps

1. **Center the data**

Subtract the mean of each feature.

2. **Compute covariance matrix**

Measures relationships between features.

3. **Find eigenvectors and eigenvalues**

- Eigenvectors → directions of principal components
- Eigenvalues → amount of explained variance

4. **Project data**

Transform the original data into the new PCA space.

---

## Example

A dataset with two correlated features:

```text
Height
  |
  |        *
  |
  |    *
  |
  | *
  |
  |________________ Weight
```

PCA finds a new axis along the main direction of variation:

```text
    PC1
   /
  /
 *
*
```
---

## Explained Variance

Each principal component explains a percentage of the total variance.

Example:
- C1: 80%
- PC2: 15%
- PC3: 5%

Keeping only PC1 and PC2 preserves 95% of the information

---

## Advantages

- Reduces dimensionality
- Removes correlated features
- Helps visualization
- Can improve model performance

---

## Disadvantages

- Components are harder to interpret
- Assumes linear relationships
- Sensitive to feature scaling

---

## Python Example

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_reduced = pca.fit_transform(X)
```


## Applications

- Data visualization
- Feature compression
- Noise reduction
- Preprocessing for machine learning models



