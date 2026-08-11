# Duality

## TL;DR

**Duality** is a fundamental principle in optimization: a difficult optimization problem, called the **primal problem**, can often be transformed into another problem, called the **dual problem**.

For a minimization problem, the dual typically provides a **lower bound** on the primal optimum.

Duality is central to:

* convex optimization
* linear programming
* constrained optimization
* Lagrangian methods
* support vector machines

---

## Primal Problem

Consider a constrained optimization problem:

$$
\begin{aligned}
\min_x \quad & f(x)\
\text{subject to}\quad
& g_i(x)\leq0,\quad i=1,\ldots,m\
& h_j(x)=0,\quad j=1,\ldots,p.
\end{aligned}
$$

This is the **primal problem**.

---

## Lagrangian

Introduce Lagrange multipliers:

$$
\lambda_i\geq0
$$

for inequality constraints and unrestricted multipliers $\nu_j$ for equality constraints.

The **Lagrangian** is:

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

## Dual Function

The **dual function** is obtained by minimizing the Lagrangian over the primal variables:

$$
q(\lambda,\nu)
=

\inf_x L(x,\lambda,\nu).
$$

The dual problem is therefore:

$$
\boxed{
\max_{\lambda\geq0,\nu}
q(\lambda,\nu)
}
$$

---

## Weak Duality

For every feasible primal and dual solution:

$$
d^\star\leq p^\star,
$$

where:

* $p^\star$ is the primal optimum
* $d^\star$ is the dual optimum

The difference:

$$
p^\star-d^\star
$$

is called the **duality gap**.

---

## Strong Duality

**Strong duality** holds when:

$$
p^\star=d^\star.
$$

For convex optimization, strong duality often holds under suitable constraint qualifications, such as **Slater's condition**.

Strong duality is particularly important because it allows the primal problem to be solved indirectly through its dual.

---

## KKT Conditions

The **Karush-Kuhn-Tucker (KKT) conditions** characterize optimal solutions for many constrained optimization problems.

They consist of:

### Primal Feasibility

$$
g_i(x^\star)\leq0,
\qquad
h_j(x^\star)=0.
$$

### Dual Feasibility

$$
\lambda_i^\star\geq0.
$$

### Stationarity

$$
\nabla_xL(x^\star,\lambda^\star,\nu^\star)=0.
$$

### Complementary Slackness

$$
\lambda_i^\star g_i(x^\star)=0.
$$

For convex problems under suitable conditions, the KKT conditions are both necessary and sufficient for optimality.

---

## Linear Programming Duality

A linear program in standard form:

$$
\min_x c^\top x
$$

subject to:

$$
Ax\geq b,
\qquad
x\geq0
$$

has a corresponding dual:

$$
\max_y b^\top y
$$

subject to:

$$
A^\top y\leq c,
\qquad
y\geq0.
$$

Linear programming exhibits strong duality under standard feasibility and boundedness assumptions.

---

## Geometric Interpretation

The primal and dual problems provide two perspectives on the same optimization problem.

For minimization:

$$
\boxed{
\text{Dual optimum}
\leq
\text{Primal optimum}
}
$$

and under strong duality:

$$
\boxed{
\text{Dual optimum}
=

\text{Primal optimum}
}
$$

The dual can therefore provide certificates of optimality and useful bounds.

---

## Why Duality Matters

Duality is more than a mathematical reformulation. It can:

* provide lower or upper bounds
* simplify optimization problems
* reveal hidden structure
* provide optimality certificates
* lead to efficient algorithms
* expose relationships between constraints and objective functions

In machine learning, the dual formulation is especially important for methods such as **SVMs**.

---

## Key Idea

Duality transforms:

$$
\boxed{
\text{Primal Optimization Problem}
\longleftrightarrow
\text{Dual Optimization Problem}
}
$$

The central result is the relationship:

$$
\boxed{
d^\star\leq p^\star
}
$$

with equality under **strong duality**.
