# KKT Conditions

## TL;DR

The **Karush-Kuhn-Tucker (KKT) conditions** are first-order conditions for constrained optimization.

For many **convex optimization problems**, they characterize optimal solutions and generalize the method of Lagrange multipliers to inequality constraints.

---

## Constrained Optimization

Consider:

$$
\begin{aligned}
\min_x \quad & f(x)\
\text{subject to}\quad
& g_i(x)\leq0,\quad i=1,\ldots,m\
& h_j(x)=0,\quad j=1,\ldots,p.
\end{aligned}
$$

The Lagrangian is:

$$
L(x,\lambda,\nu)
=

f(x)
+
\sum_{i=1}^m\lambda_i g_i(x)
+
\sum_{j=1}^p\nu_jh_j(x).
$$

---

## KKT Conditions

A candidate optimum $(x^\star,\lambda^\star,\nu^\star)$ satisfies four conditions.

### 1. Primal Feasibility

The solution must satisfy the original constraints:

$$
g_i(x^\star)\leq0
$$

and:

$$
h_j(x^\star)=0.
$$

### 2. Dual Feasibility

The multipliers of inequality constraints must be non-negative:

$$
\lambda_i^\star\geq0.
$$

Multipliers for equality constraints are unrestricted.

### 3. Stationarity

The gradient of the Lagrangian with respect to $x$ must vanish:

$$
\nabla_x L(x^\star,\lambda^\star,\nu^\star)=0.
$$

Equivalently:

$$
\nabla f(x^\star)
+
\sum_i\lambda_i^\star\nabla g_i(x^\star)
+
\sum_j\nu_j^\star\nabla h_j(x^\star)
=0.
$$

### 4. Complementary Slackness

For every inequality constraint:

$$
\boxed{
\lambda_i^\star g_i(x^\star)=0
}
$$

This means that either:

$$
\lambda_i^\star=0
$$

or:

$$
g_i(x^\star)=0.
$$

An inactive constraint therefore has zero multiplier.

---

## Example

Consider:

$$
\min_x\ x^2
$$

subject to:

$$
x\geq1.
$$

Write the constraint as:

$$
g(x)=1-x\leq0.
$$

The Lagrangian is:

$$
L(x,\lambda)=x^2+\lambda(1-x).
$$

Stationarity gives:

$$
2x-\lambda=0.
$$

At the optimum:

$$
x^\star=1,
\qquad
\lambda^\star=2.
$$

All KKT conditions are satisfied.

---

## Necessary vs. Sufficient

For general nonlinear optimization, KKT conditions are typically **necessary** only under suitable constraint qualifications.

For convex problems, if:

* $f$ is convex
* $g_i$ are convex
* $h_j$ are affine
* a suitable constraint qualification such as **Slater's condition** holds

then KKT conditions are also **sufficient** for global optimality.

Thus:

$$
\boxed{
\text{KKT}
\Rightarrow
\text{Global Optimum}
}
$$

under these conditions.

---

## Constraint Qualifications

Constraint qualifications ensure that the KKT conditions apply properly.

A particularly important one for convex optimization is **Slater's condition**:

There exists some $x$ such that:

$$
g_i(x)<0
$$

for all inequality constraints and:

$$
h_j(x)=0.
$$

Under Slater's condition, strong duality and KKT optimality conditions hold for many convex optimization problems.

---

## Relation to Lagrange Multipliers

For equality-constrained problems:

$$
h_j(x)=0,
$$

the KKT conditions reduce to the classical **method of Lagrange multipliers**.

KKT extends this framework by introducing non-negative multipliers for inequality constraints.

---

## Key Idea

The KKT conditions combine:

$$
\boxed{
\text{Primal Feasibility}
+
\text{Dual Feasibility}
+
\text{Stationarity}
+
\text{Complementary Slackness}
}
$$

and provide a powerful characterization of constrained optima, particularly in **convex optimization**.
