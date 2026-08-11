# Partial Differential Equations

## TL;DR

A **partial differential equation (PDE)** is an equation involving an unknown function of **multiple independent variables** and its partial derivatives.

For example:

$$
\frac{\partial u}{\partial t}
=

D\frac{\partial^2 u}{\partial x^2}.
$$

PDEs are commonly used to describe systems that vary across **space and time**.

---

## General Form

A PDE can involve partial derivatives of different orders:

$$
F\left(
x_1,\ldots,x_n,
u,
\frac{\partial u}{\partial x_i},
\frac{\partial^2u}{\partial x_i\partial x_j},
\ldots
\right)=0.
$$

The **order** of a PDE is the highest order of any partial derivative that appears.

For example:

$$
\frac{\partial^2u}{\partial x^2}
+
\frac{\partial^2u}{\partial y^2}
=0
$$

is a **second-order PDE**.

---

## Linear and Nonlinear PDEs

A **linear PDE** has the form:

$$
L[u]=f,
$$

where $L$ is a linear differential operator.

For example:

$$
\frac{\partial u}{\partial t}
=

D\frac{\partial^2u}{\partial x^2}
$$

is linear.

A nonlinear PDE could be:

$$
\frac{\partial u}{\partial t}
+
u\frac{\partial u}{\partial x}
=0.
$$

Here, the unknown function $u$ is multiplied by one of its derivatives.

---

## Initial and Boundary Conditions

PDEs often require both **initial conditions** and **boundary conditions**.

For example, a time-dependent PDE might have:

$$
u(x,0)=u_0(x)
$$

as an initial condition.

Boundary conditions could specify values at the boundaries:

$$
u(0,t)=0,
\qquad
u(L,t)=0.
$$

The combination of a PDE with its initial and/or boundary conditions defines a well-posed problem.

---

## Classification of Second-Order PDEs

A second-order PDE can often be classified as:

* **Elliptic**
* **Parabolic**
* **Hyperbolic**

These classes have different mathematical and physical properties.

### Elliptic

Example: **Laplace's equation**

$$
\nabla^2u=0.
$$

Often associated with equilibrium or steady-state problems.

### Parabolic

Example: **Heat equation**

$$
\frac{\partial u}{\partial t}
=

D\nabla^2u.
$$

Often describes diffusion and smoothing processes.

### Hyperbolic

Example: **Wave equation**

$$
\frac{\partial^2u}{\partial t^2}
=

c^2\nabla^2u.
$$

Often describes wave propagation.

---

## Analytical Methods

Some PDEs can be solved analytically using methods such as:

* separation of variables
* Fourier series
* Fourier transforms
* Laplace transforms
* Green's functions
* method of characteristics

Analytical solutions are generally only available for special classes of PDEs and boundary conditions.

---

## Numerical Methods

Many practically relevant PDEs require numerical methods.

Common approaches include:

* finite difference methods
* finite element methods
* finite volume methods
* spectral methods

These methods discretize the spatial and/or temporal variables and transform the PDE into a system that can be solved computationally.

---

## Applications

PDEs are used to model:

* heat and diffusion
* waves and acoustics
* fluid dynamics
* electromagnetism
* elasticity
* quantum mechanics
* financial models
* reaction-diffusion systems

---

## ODEs vs. PDEs

|                       | ODE                              | PDE                                 |
| --------------------- | -------------------------------- | ----------------------------------- |
| Independent variables | One                              | Multiple                            |
| Derivatives           | Ordinary                         | Partial                             |
| Example               | $y'=f(x,y)$                      | $u_t=D u_{xx}$                      |
| Typical domains       | Time or one-dimensional variable | Space, time, or multiple dimensions |

An ODE can sometimes result from a PDE after reducing the number of independent variables, for example through symmetry assumptions.

---

## Key Idea

A PDE describes how an unknown function changes with respect to **multiple independent variables**.

Important classifications include:

* linear vs. nonlinear
* first-order vs. higher-order
* elliptic vs. parabolic vs. hyperbolic
* initial value vs. boundary value problems

PDEs form a central part of **mathematical modeling, physics, engineering, and applied mathematics**.
