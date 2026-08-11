# Interior-Point Method

## TL;DR

**Interior-point methods** are optimization algorithms that solve constrained optimization problems by moving through the **interior of the feasible region** rather than along its boundary.

They are particularly important for:

* linear programming
* convex optimization
* large-scale constrained optimization

---

## Basic Idea

Consider:

$$
\begin{aligned}
\min_x\quad &f(x)\
\text{subject to}\quad
&g_i(x)\leq0.
\end{aligned}
$$

Instead of directly enforcing the inequality constraints, an interior-point method keeps the iterates strictly feasible:

$$
g_i(x)<0.
$$

The algorithm approaches the optimal boundary from within the feasible region.

---

## Barrier Method

A common approach replaces the constrained problem with an unconstrained or equality-constrained problem using a **barrier function**.

For constraints:

$$
g_i(x)<0,
$$

a logarithmic barrier is:

$$
-\mu\sum_i\log(-g_i(x)),
$$

where:

$$
\mu>0
$$

controls the barrier strength.

The resulting objective is:

$$
\boxed{
\min_x
\left[
f(x)
-

\mu\sum_i\log(-g_i(x))
\right]
}
$$

As:

$$
\mu\rightarrow0,
$$

the solution approaches the constrained optimum.

---

## Logarithmic Barrier

For a simple constraint:

$$
x>0,
$$

the barrier is:

$$
-\mu\log(x).
$$

As $x$ approaches zero:

$$
-\mu\log(x)\rightarrow\infty.
$$

The barrier therefore prevents the optimization process from crossing the constraint boundary.

---

## Central Path

As the barrier parameter $\mu$ varies, the minimizers of the barrier problems form a curve called the **central path**.

Conceptually:

$$
\mu\text{ large}
\rightarrow
\text{central region}
\rightarrow
\mu\rightarrow0
\rightarrow
\text{optimal solution}.
$$

Interior-point algorithms approximately follow this path.

---

## Relation to KKT Conditions

Modern primal-dual interior-point methods are closely connected to the KKT conditions.

Instead of enforcing complementary slackness exactly:

$$
\lambda_i g_i(x)=0,
$$

they use a perturbed condition:

$$
\boxed{
\lambda_i g_i(x)=-\mu
}
$$

for constraints written as:

$$
g_i(x)\leq0.
$$

As:

$$
\mu\rightarrow0,
$$

the perturbed KKT conditions approach the original KKT conditions.

---

## Primal-Dual Methods

A **primal-dual interior-point method** simultaneously updates:

* primal variables $x$
* dual variables $\lambda$
* equality multipliers $\nu$

by approximately solving the perturbed KKT system.

This is the basis of many efficient algorithms for large-scale convex optimization.

---

## Linear Programming

For a linear program:

$$
\min_x c^\top x
$$

subject to:

$$
Ax=b,
\qquad
x\geq0,
$$

interior-point methods can solve the problem by following the central path toward the optimal solution.

They provide an alternative to **simplex methods**.

---

## Interior-Point vs. Simplex

Conceptually:

**Simplex methods**

$$
\text{move along vertices/edges}
\rightarrow
\text{optimal vertex}
$$

**Interior-point methods**

$$
\text{move through interior}
\rightarrow
\text{approach optimal boundary}
$$

Both are important approaches to linear and convex optimization.

---

## Advantages

Interior-point methods are particularly attractive for:

* large optimization problems
* sparse problems
* convex optimization
* problems with many constraints

They often have strong polynomial-time complexity guarantees for convex problems.

---

## Key Idea

Interior-point methods avoid the constraint boundary during intermediate iterations and approach the optimum through the interior:

$$
\boxed{
\text{Interior of Feasible Region}
\rightarrow
\text{Central Path}
\rightarrow
\text{Optimal Boundary}
}
$$

Their modern formulation is closely connected to the **Lagrangian, duality, and KKT conditions**.
