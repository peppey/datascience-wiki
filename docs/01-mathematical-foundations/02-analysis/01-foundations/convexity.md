# Convexity

## TL;DR

A set or function is **convex** if, intuitively, the straight line between any two points stays inside the set or lies above the function.

For a function $f$, convexity means:

$$
f(\lambda x+(1-\lambda)y)
\leq
\lambda f(x)+(1-\lambda)f(y)
$$

for all $x,y$ and $\lambda\in[0,1]$.

Convexity is important in **optimization** because convex problems have particularly useful properties, such as the absence of local minima that are not global minima.

---

## Definition

A function $f$ is **convex** if for any two points $x$ and $y$ and any

$$
\lambda\in[0,1],
$$

we have:

$$
f(\lambda x+(1-\lambda)y)
\leq
\lambda f(x)+(1-\lambda)f(y)
$$

The point

$$
\lambda x+(1-\lambda)y
$$

lies between $x$ and $y$.

Geometrically, a convex function lies **below the straight line connecting two points on its graph**.

---

## Example

Consider:

$$
f(x)=x^2
$$

This function is convex.

For example, between $x=0$ and $x=2$:

$$
f(0)=0
$$

and

$$
f(2)=4.
$$

The line connecting these points lies above the function:

$$
f(x)\leq 2x
$$

for $x\in[0,2]$.

Therefore, $f(x)=x^2$ is convex.

---

## Geometric Intuition

For a convex function:

* the line between two points lies **above** the function
* there are no isolated "valleys" separated by higher regions
* a local minimum is also a global minimum

For a non-convex function, the graph can contain multiple valleys and local minima.

---

## Convex Sets

Convexity also applies to **sets**.

A set $C$ is convex if:

$$
x,y\in C
\quad\Rightarrow\quad
\lambda x+(1-\lambda)y\in C
$$

for every $\lambda\in[0,1]$.

In other words, the straight line between any two points in the set remains inside the set.

Examples of convex sets include:

* intervals
* circles and disks
* rectangles
* half-spaces

---

## Connection to Optimization

Convexity is especially important in optimization.

Consider:

$$
\min_x f(x)
$$

If $f$ is convex, every local minimum is also a **global minimum**.

This makes optimization much easier:

$$
\text{local minimum}
\quad\Rightarrow\quad
\text{global minimum}
$$

This property is one reason why convex optimization is much more tractable than general non-convex optimization.

---

## Checking Convexity

For a twice-differentiable function, convexity can often be checked using the **Hessian matrix**.

A function is convex if:

$$
\nabla^2 f(x)\succeq0
$$

for all $x$.

This means that the Hessian is **positive semidefinite**.

In one dimension, this simplifies to:

$$
f''(x)\geq0.
$$

For example:

$$
f(x)=x^2
$$

has:

$$
f''(x)=2>0,
$$

so it is convex.

---

## Machine Learning

Convexity appears frequently in machine learning.

Examples include:

* linear regression with squared loss
* logistic regression
* Support Vector Machines
* convex regularization such as L1 and L2 regularization

For convex optimization problems, optimization algorithms can often find the global optimum reliably.

In contrast, many neural networks involve **non-convex optimization**, which can contain many local minima and saddle points.

---

## Summary

| Property                            | Convexity                                   |
| ----------------------------------- | ------------------------------------------- |
| Function lies below connecting line | Yes                                         |
| Local minimum is global             | Yes                                         |
| Important for optimization          | Yes                                         |
| 1D condition                        | $f''(x)\geq0$                               |
| Multivariate condition              | $\nabla^2f(x)\succeq0$                      |
| Common in ML                        | Logistic regression, SVM, linear regression |

Convexity describes a useful geometric structure of functions and sets. It is fundamental to **optimization and machine learning** because convex problems are generally much easier to solve and analyze than non-convex ones.
