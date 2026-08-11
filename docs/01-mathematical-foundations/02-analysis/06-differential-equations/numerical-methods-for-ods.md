# Numerical Methods for ODEs

## TL;DR

**Numerical methods for ordinary differential equations (ODEs)** approximate solutions when an ODE cannot be solved analytically.

For an initial value problem:

$$
\frac{dy}{dt}=f(t,y),
\qquad
y(t_0)=y_0,
$$

numerical methods compute approximate values of $y(t)$ at discrete points.

---

## Discretization

Choose a step size $h$ and define:

$$
t_n=t_0+nh.
$$

The continuous solution $y(t)$ is approximated by values:

$$
y_0,y_1,y_2,\ldots
$$

where:

$$
y_n\approx y(t_n).
$$

---

## Euler's Method

The simplest method is **Euler's method**:

$$
y_{n+1}
=======

y_n+h f(t_n,y_n).
$$

It uses the derivative at the current point to estimate the next point.

Euler's method is simple but generally has relatively low accuracy.

---

## Runge-Kutta Methods

**Runge-Kutta methods** use several evaluations of the derivative within each step.

The most common example is **RK4**:

$$
k_1=f(t_n,y_n)
$$

$$
k_2=f\left(t_n+\frac h2,y_n+\frac h2k_1\right)
$$

$$
k_3=f\left(t_n+\frac h2,y_n+\frac h2k_2\right)
$$

$$
k_4=f(t_n+h,y_n+hk_3)
$$

and:

$$
y_{n+1}
=

y_n+
\frac h6(k_1+2k_2+2k_3+k_4).
$$

RK4 is widely used because it provides good accuracy without requiring excessively small step sizes.

---

## Multistep Methods

**Multistep methods** use information from previous time steps.

Examples include:

* Adams-Bashforth methods
* Adams-Moulton methods
* Backward differentiation formulas (BDF)

They can be more efficient than single-step methods but require previously computed solution values.

---

## Explicit vs. Implicit Methods

### Explicit

An explicit method calculates the next value directly:

$$
y_{n+1}=F(t_n,y_n).
$$

Euler's method and classical RK4 are explicit.

### Implicit

An implicit method involves the unknown future value:

$$
y_{n+1}
=

y_n+h f(t_{n+1},y_{n+1}).
$$

This usually requires solving an equation at every step.

Implicit methods are particularly useful for **stiff ODEs**.

---

## Accuracy

Numerical methods introduce approximation errors.

The **local truncation error** measures the error introduced in one numerical step.

The **global error** measures the accumulated error over the entire integration interval.

For Euler's method:

$$
\text{Global Error}=O(h).
$$

For classical RK4:

$$
\text{Global Error}=O(h^4).
$$

---

## Stability

A numerical method should not introduce artificial instability into a stable differential equation.

This is especially important for **stiff ODEs**, where explicit methods may require extremely small step sizes.

Implicit methods such as BDF methods are often preferred for stiff problems.

---

## Common Methods

| Method          | Type     | Global order | Typical use                    |
| --------------- | -------- | -----------: | ------------------------------ |
| Euler           | Explicit |          $1$ | Simple problems                |
| Heun            | Explicit |          $2$ | Improved Euler                 |
| RK4             | Explicit |          $4$ | General-purpose problems       |
| Adams-Bashforth | Explicit |       Varies | Multistep integration          |
| Adams-Moulton   | Implicit |       Varies | Accurate multistep integration |
| BDF             | Implicit |       Varies | Stiff problems                 |

---

## Key Idea

Numerical ODE methods replace a continuous differential equation with a sequence of discrete approximations.

The main concerns are:

* **Accuracy**
* **Stability**
* **Efficiency**
* **Step-size selection**

The choice of method depends strongly on the properties of the ODE, especially whether it is **stiff**.
