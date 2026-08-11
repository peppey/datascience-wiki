# Lagrangian

## TL;DR

The **Lagrangian** is a function that incorporates constraints into an optimization problem by introducing **Lagrange multipliers**.

For constrained optimization:

$$
\begin{aligned}
\min_x \quad & f(x)\
\text{subject to}\quad
& g_i(x)\leq0\
& h_j(x)=0,
\end{aligned}
$$

the Lagrangian is:

$$
\boxed{
L(x,\lambda,\nu)
=

f(x)
+
\sum_i\lambda_i g_i(x)
+
\sum_j\nu_j h_j(x)
}
$$

It is the foundation of **Lagrange multipliers, KKT conditions, and Lagrangian duality**.

---

## Equality Constraints

Consider:

$$
\min_x f(x)
$$

subject to:

$$
h(x)=0.
$$

Introduce a multiplier $\nu$ and define:

$$
L(x,\nu)
=

f(x)+\nu h(x).
$$

At a constrained optimum, under suitable regularity conditions:

$$
\nabla_x L(x^\star,\nu^\star)=0.
$$

Thus:

$$
\nabla f(x^\star)
+
\nu^\star\nabla h(x^\star)
=

0.

$$

The constraint is also satisfied:

$$
h(x^\star)=0.
$$

---

## Inequality Constraints

For constraints:

$$
g_i(x)\leq0,
$$

the Lagrangian uses non-negative multipliers:

$$
\lambda_i\geq0.
$$

Thus:

$$
L(x,\lambda)
=

f(x)
+
\sum_i\lambda_i g_i(x).
$$

The non-negativity of the multipliers is essential for the connection to constrained optimization and duality.

---

## Interpretation

The Lagrangian combines:

$$
\boxed{
\text{Objective}
+
\text{Weighted Constraints}
}
$$

The multipliers indicate how strongly the constraints influence the optimization problem.

In many applications, a multiplier can be interpreted as a **shadow price**: how much the optimal objective would change when relaxing a constraint.

---

## Lagrangian Stationarity

For equality-constrained optimization, a candidate optimum satisfies:

$$
\nabla_x L(x^\star,\nu^\star)=0.
$$

Geometrically, this means that at the optimum, the gradient of the objective lies in the span of the gradients of the active constraints.

For one constraint:

$$
\nabla f(x^\star)
=

-\nu^\star\nabla h(x^\star).
$$

---

## Lagrangian Duality

The Lagrangian also provides a systematic way to construct the **dual problem**.

Define the dual function:

$$
q(\lambda,\nu)
=

\inf_x L(x,\lambda,\nu).
$$

The dual problem is:

$$
\boxed{
\max_{\lambda\geq0,\nu}q(\lambda,\nu)
}
$$

This gives the connection:

$$
\text{Lagrangian}
\rightarrow
\text{Dual Function}
\rightarrow
\text{Dual Problem}.
$$

---

## Relation to KKT Conditions

The KKT conditions are expressed directly using the Lagrangian.

The stationarity condition is:

$$
\nabla_xL(x^\star,\lambda^\star,\nu^\star)=0.
$$

Together with:

* primal feasibility
* dual feasibility
* complementary slackness

these form the KKT conditions.

Therefore:

$$
\boxed{
\text{Lagrangian}
\rightarrow
\text{KKT Conditions}
}
$$

---

## Example

Consider:

$$
\min_x x^2
$$

subject to:

$$
x\geq1.
$$

Rewrite the constraint as:

$$
1-x\leq0.
$$

The Lagrangian is:

$$
L(x,\lambda)
=

x^2+\lambda(1-x),
\qquad
\lambda\geq0.
$$

Stationarity gives:

$$
\frac{\partial L}{\partial x}
=

2x-\lambda

0.

$$

Together with the constraint and complementary slackness, this yields:

$$
x^\star=1,
\qquad
\lambda^\star=2.
$$

---

## Key Idea

The Lagrangian transforms a constrained optimization problem into a function containing both the objective and its constraints:

$$
\boxed{
L
=

\text{Objective}
+
\text{Constraint Terms}
}
$$

It provides the common foundation for:

$$
\boxed{
\text{Lagrange Multipliers}
\rightarrow
\text{KKT Conditions}
\rightarrow
\text{Lagrangian Duality}
}
$$
