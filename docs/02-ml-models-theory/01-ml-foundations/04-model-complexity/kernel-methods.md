# Kernel Methods & Reproducing Kernel Hilbert Space (RKHS)

## TL;DR (30 seconds)

**Kernel Methods** allow models to learn complex nonlinear relationships without explicitly transforming data into a high-dimensional feature space.

The core idea:

> Compute similarities between data points instead of explicitly calculating the features.

A kernel describes:

$$
K(x,x')
=
\langle \phi(x),\phi(x')\rangle
$$

Where:

- $\phi(x)$ = transformation into a feature space
- $K(x,x')$ = similarity between two data points

---

**Practical importance:**

Kernel Methods explain:

- Why SVMs can learn nonlinear decision boundaries
- How complex feature spaces are created
- Why high-dimensional transformations do not need to be computed explicitly

---

## Motivation & Intuition

Many machine learning models search for a decision boundary that separates data.

Example:

### Linearly separable data
○ ○ ○

───

● ● ●


A straight line is sufficient.

---

### Nonlinearly separable data

Example:

○ ○ ● ○

○ ● ● ○

● ○ ○ ●

A simple straight line does not work.

---

The idea:

Transform the data from the original space to the feature space:

$
x 
$

↓

$
\phi(x)
$

A feature space is a space in which data is represented by features. In this space, a linear separation may become possible.

---

Example: A point

$$
x=(x_1,x_2)
$$

can be transformed into the feature space:

$$
\phi(x)
=
(x_1,x_2,x_1^2,x_2^2,x_1x_2)
$$

such that in the feature space, the data is linearly separable.

---

### Problem of Explicit Transformation

This transformation can become very expensive. A model with large input can create a feature space with millions or even infinitely many dimensions.

However, we still want to perform computations in this space.

The solution: **The Kernel Trick**

---

## The Kernel Trick

The Kernel Trick replaces the inner product in the feature space:

Instead of:

$$
\langle\phi(x),\phi(x')\rangle
$$

we directly compute:

$$
K(x,x')
$$

---

The transformation is therefore never explicitly calculated.

Original:

$$
x
\rightarrow
\phi(x)
\rightarrow
\langle\phi(x),\phi(x')\rangle
$$

With Kernel:

$$
x,x'
\rightarrow
K(x,x')
$$

## Common Kernels

### Linear Kernel

$$
K(x,x')
=
x^Tx'
$$

Corresponds to:

No transformation.

Useful for:

- many features
- linear problems

---

### Polynomial Kernel

$$
K(x,x')
=
(x^Tx'+c)^d
$$

Creates more complex polynomial decision boundaries.

---

### Radial Basis Function Kernel (RBF)

The most common nonlinear kernel:

$$
K(x,x')
=
e^{-\gamma ||x-x'||^2}
$$

Intuition:

Similar points receive high values.

Dissimilar points receive low values.

---

## Intuition

The kernel contains information about:

- how functions are compared
- which functions are possible in the model
- the complexity of the learning space

---

## Relationship Between Kernel and Model Complexity

The kernel determines the feature space.

A more complex kernel:

- enables more complex models
- can learn finer patterns
- increases the risk of overfitting


---

## Kernel Methods and Generalization

Kernel Methods work well because they:

1. Choose a suitable feature space
2. Control model complexity
3. Use regularization

Generalization depends on:

- choice of kernel
- kernel parameters
- amount of data


### Feature Engineering vs. Kernel Methods

Kernel Methods partially perform feature creation.

Instead of manually creating features, the kernel defines an implicit feature space.


---

### Limitations of Kernel Methods

For very large datasetss, the kernel matrix grows quadratically:

$$
O(n^2)
$$

Therefore, neural networks are often preferred for very large datasets.

## Related Topics

- Support Vector Machines
- Empirical Risk Minimization (ERM)
- Structural Risk Minimization
- Regularization
- VC-Dimension & Rademacher Complexity
