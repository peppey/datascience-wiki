
# Support Vector Machines (SVMs)

SVMs search for a decision boundary with the maximum distance to the data points.

The decision boundary:

$$
w^Tx+b=0
$$

---

The points closest to the boundary are called:

**Support Vectors**

They determine the position of the decision boundary.

---

## Why Do Kernel SVMs Work?

An SVM only requires inner products between data points.

The optimization uses terms such as:

$$
x_i^Tx_j
$$

With Kernel Methods, these are replaced by:

$$
K(x_i,x_j)
$$

This allows the SVM to operate in the feature space.

---

Workflow:

Data
↓

Kernel computes similarities

↓

SVM finds optimal decision boundary in feature space

↓

Nonlinear boundary in the original space

---


## Relationship with Regularization

SVMs also use a form of regularization.

The optimization:

$$
\min
\frac{1}{2}||w||^2
+
C
\sum_i \xi_i
$$

Where:

- $||w||^2$ controls model complexity
- $C$ determines the influence of errors

---

Large $C$:

- fewer errors allowed
- more complex model

Small $C$:

- stronger regularization
- simpler model

