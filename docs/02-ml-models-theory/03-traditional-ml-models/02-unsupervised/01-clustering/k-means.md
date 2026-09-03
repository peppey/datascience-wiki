# K-Means

## TL;DR

**K-Means** is an unsupervised learning algorithm for **clustering** data into $k$ groups.

It assigns each data point to the nearest **cluster centroid** and iteratively updates the centroids.

---

## Idea

Given a dataset:

$$
X = {x_1, x_2, ..., x_n}
$$

K-Means tries to divide the data into $k$ clusters.

Each cluster has a **centroid** representing the center of the cluster.

The algorithm alternates between:

1. assigning points to the nearest centroid
2. recomputing the centroids

---

## Algorithm

The algorithm starts with $k$ initial centroids.

### Assignment

Each point is assigned to its closest centroid:

$$
c_i = \arg\min_j |x_i-\mu_j|^2
$$

where:

* $x_i$ = data point
* $\mu_j$ = centroid of cluster $j$
* $c_i$ = assigned cluster

### Update

The centroid of each cluster is recalculated as the mean of its assigned points:

$$
\mu_j =
\frac{1}{|C_j|}
\sum_{x_i \in C_j} x_i
$$

These two steps are repeated until the assignments no longer change significantly.

---

## Objective

K-Means minimizes the **within-cluster sum of squares (WCSS)**:

$$
\min
\sum_{j=1}^{k}
\sum_{x_i \in C_j}
|x_i-\mu_j|^2
$$

The objective is therefore to create clusters whose points are as close as possible to their centroid.

---

## Choosing $k$

The number of clusters $k$ must be specified beforehand.

Common approaches include:

### Elbow Method

Run K-Means for different values of $k$ and plot the WCSS.

The optimal $k$ is often chosen near the point where adding more clusters provides diminishing improvements.

### Silhouette Score

The **silhouette score** measures how well points fit their own cluster compared to other clusters.

Higher values generally indicate better-separated clusters.

---

## Example

Suppose customer data contains:

* annual income
* number of purchases

K-Means might identify groups such as:

* low-income, low-purchase customers
* high-income, low-purchase customers
* high-income, high-purchase customers

The algorithm discovers these groups without requiring predefined labels.

---

## Scaling

K-Means is sensitive to feature scales because it usually uses **Euclidean distance**.

For example, if one feature ranges from $0$ to $1$ and another from $0$ to $100000$, the second feature can dominate the clustering.

Therefore, standardization is often useful:

$$
x' = \frac{x-\mu}{\sigma}
$$

---

## Initialization

K-Means can converge to different solutions depending on the initial centroids.

A common strategy is **K-Means++**, which chooses initial centroids more carefully to improve the starting configuration.

In practice, K-Means is often run multiple times with different initializations.

---

## Limitations

K-Means works best when clusters are:

* relatively compact
* roughly spherical
* similar in scale

It can perform poorly when clusters have:

* very different densities
* irregular shapes
* strong outliers
* very different sizes

It also requires the number of clusters $k$ to be chosen in advance.

---

## Key Takeaway

K-Means groups data by repeatedly assigning points to their nearest centroid and updating the centroids.

The basic workflow is:

$$
\boxed{
\text{Initialize Centroids}
\rightarrow
\text{Assign Points}
\rightarrow
\text{Update Centroids}
\rightarrow
\text{Repeat}
}
$$
