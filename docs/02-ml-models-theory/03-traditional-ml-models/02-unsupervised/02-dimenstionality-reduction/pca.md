# Principal Component Analysis (PCA)

## TL;DR

**Principal Component Analysis (PCA)** is an unsupervised dimensionality reduction method.

It transforms correlated features into a smaller set of **uncorrelated principal components** that preserve as much variance in the data as possible.

---

## Idea

Given a dataset with many features, PCA finds new directions in the feature space along which the data varies the most.

The first principal component captures the largest possible variance.

The second captures the largest remaining variance while being orthogonal to the first, and so on.

---

## Transformation

Let the centered data matrix be:

$$
X \in \mathbb{R}^{n \times d}
$$

PCA finds a set of orthogonal directions:

$$
w_1, w_2, ..., w_d
$$

The principal components are obtained by projecting the data onto these directions:

$$
Z = XW
$$

where:

* $X$ = centered data
* $W$ = matrix of principal component directions
* $Z$ = transformed data

Usually, only the first $k$ components are kept:

$$
Z_k = XW_k
$$

with:

$$
k < d
$$

---

## How PCA Finds the Components

PCA can be computed using the **eigendecomposition** of the covariance matrix:

$$
\Sigma = \frac{1}{n-1}X^TX
$$

The eigenvectors of $\Sigma$ are the principal directions.

The corresponding eigenvalues describe how much variance is explained by each component.

Alternatively, PCA can be computed directly using **Singular Value Decomposition (SVD)**:

$$
X = U\Sigma V^T
$$

The rows of $V^T$ correspond to the principal directions.

---

## Choosing the Number of Components

The number of components $k$ is often chosen based on the **explained variance**.

The explained variance ratio of component $i$ is:

$$
\frac{\lambda_i}{\sum_j \lambda_j}
$$

where $\lambda_i$ is the eigenvalue of component $i$.

For example, one might choose enough components to explain **95% of the total variance**.

---

## Example

Suppose a dataset contains:

* height
* weight
* arm length
* leg length
* shoe size

Many of these features are correlated.

PCA might transform them into a smaller number of components such as:

* **PC1:** overall body size
* **PC2:** relative body proportions

Instead of using all five original features, a model could use only the first two principal components.

---

## Important: Scaling

PCA is sensitive to the scale of the features.

For example:

* age: values between $0$ and $100$
* income: values between $0$ and $100000$

Income would dominate the variance.

Therefore, PCA is often applied after **standardization**:

$$
x' = \frac{x-\mu}{\sigma}
$$

---

## Applications

Common applications include:

* dimensionality reduction
* data visualization
* noise reduction
* feature compression
* preprocessing for machine learning
* exploratory data analysis

PCA is particularly useful for visualizing high-dimensional data in 2D or 3D.

---

## Limitations

PCA:

* is a **linear** dimensionality reduction method
* is sensitive to feature scaling
* can be sensitive to outliers
* produces components that may be difficult to interpret
* does not use target labels

For nonlinear structures, methods such as **Kernel PCA**, **t-SNE**, or **UMAP** can be considered.

---

## Key Takeaway

PCA transforms a high-dimensional dataset into a smaller set of orthogonal components that capture the largest amount of variance.

The basic workflow is:

$$
\boxed{
\text{Center/Scale}
\rightarrow
\text{Compute PCA}
\rightarrow
\text{Select Components}
\rightarrow
\text{Project Data}
}
$$
