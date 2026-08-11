# Ordinary Differential Equations

## TL;DR

An **ordinary differential equation (ODE)** is an equation involving an unknown function of **one independent variable** and its derivatives.

For example:

$$
\frac{dy}{dx}=f(x,y).
$$

ODEs are used to model how quantities change with respect to a single variable, such as time.

---

## General Form

An ODE can involve derivatives of different orders:

$$
F\left(x,y,y',y'',\ldots,y^{(n)}\right)=0.
$$

The **order** of an ODE is the highest derivative that appears.

For example:

$$
y''+3y'-2y=0
$$

is a **second-order ODE**.

---

## Linear and Nonlinear ODEs

A **linear ODE** has the form:

$$
a_n(x)y^{(n)}
+\cdots+
a_1(x)y'
+a_0(x)y
=

f(x).
$$

The function $y$ and its derivatives only appear to the first power and are not multiplied by each other.

For example:

$$
y''+x y'-y=\sin(x)
$$

is linear.

A nonlinear ODE could be:

$$
y'=y^2+x
$$

because $y$ appears quadratically.

---

## Initial Value Problems

An **initial value problem (IVP)** specifies the value of the solution and possibly its derivatives at a particular point.

For example:

$$
y'=f(x,y),
\qquad
y(x_0)=y_0.
$$

For a second-order ODE:

$$
y''=f(x,y,y'),
$$

two initial conditions are typically required:

$$
y(x_0)=y_0,
\qquad
y'(x_0)=v_0.
$$

---

## Boundary Value Problems

A **boundary value problem (BVP)** specifies conditions at different points.

For example:

$$
y''=f(x,y,y')
$$

with:

$$
y(a)=\alpha,
\qquad
y(b)=\beta.
$$

BVPs commonly arise in physical systems and engineering problems.

---

## Stiff ODEs

A **stiff ODE** is an ODE whose solution contains very different time or length scales, making many explicit numerical methods require extremely small step sizes for stability.

A simple example is:

$$
y'=-\lambda y
$$

with a large $\lambda$.

The analytical solution is:

$$
y(t)=y_0e^{-\lambda t}.
$$

The solution may decay very rapidly, requiring a numerical solver to take small steps even after the solution has become relatively smooth.

Stiffness is therefore primarily a **numerical difficulty**, rather than a special type of differential equation.

For stiff problems, **implicit methods** are often preferred, such as:

* Backward Euler
* BDF methods
* implicit Runge-Kutta methods

---

## Analytical Solutions

Some ODEs can be solved analytically using methods such as:

* separation of variables
* integrating factors
* characteristic equations
* variation of parameters
* Laplace transforms
* power-series methods
* Green's functions

However, many ODEs do not have a simple closed-form solution.

---

## Numerical Solutions

When an analytical solution is unavailable, numerical methods can approximate the solution.

Common methods include:

* Euler's method
* Runge-Kutta methods
* Adams methods
* Backward differentiation formulas

For **stiff ODEs**, implicit methods are often more suitable than explicit methods.

---

## Applications

ODEs are used to model many systems, including:

* physical dynamics
* population growth
* chemical reactions
* electrical circuits
* mechanical systems
* epidemiology
* financial models
* biological processes

---

## Key Idea

An ODE describes how an unknown function changes with respect to **one independent variable**.

Important classifications include:

* linear vs. nonlinear
* first-order vs. higher-order
* initial value vs. boundary value
* stiff vs. non-stiff

The main distinction from **partial differential equations (PDEs)** is that ODEs involve ordinary derivatives with respect to a single independent variable.
