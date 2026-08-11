# Separation of Variables

## TL;DR

**Separation of variables** is a method for solving certain first-order ODEs by rearranging the equation so that all terms involving the dependent variable are on one side and all terms involving the independent variable are on the other.

It applies to ODEs of the form:

$$
\frac{dy}{dx}=f(x)g(y).
$$

---

## Method

Starting with:

$$
\frac{dy}{dx}=f(x)g(y),
$$

rearrange:

$$
\frac{1}{g(y)},dy=f(x),dx.
$$

Then integrate both sides:

$$
\int\frac{1}{g(y)},dy
=

\int f(x),dx.
$$

The resulting equation implicitly or explicitly defines the solution $y(x)$.

---

## Example

Consider:

$$
\frac{dy}{dx}=xy.
$$

Separate the variables:

$$
\frac{1}{y},dy=x,dx.
$$

Integrate:

$$
\int\frac{1}{y},dy
==================

\int x,dx.
$$

Therefore:

$$
\ln|y|
======

\frac{x^2}{2}+C.
$$

Exponentiating gives:

$$
y=Ce^{x^2/2}.
$$

---

## Initial Conditions

An initial condition can be used to determine the constant $C$.

For example:

$$
y(0)=2.
$$

Using:

$$
y=Ce^{x^2/2},
$$

we obtain:

$$
2=C.
$$

Therefore:

$$
\boxed{y(x)=2e^{x^2/2}}.
$$

---

## Equilibrium Solutions

When:

$$
g(y)=0,
$$

constant solutions may exist.

For example:

$$
\frac{dy}{dx}=y(1-y).
$$

The values

$$
y=0
$$

and

$$
y=1
$$

are equilibrium solutions.

When separating variables, dividing by $g(y)$ can remove these solutions, so they should be checked separately.

---

## When It Applies

Separation of variables works when the ODE can be written as:

$$
y'=f(x)g(y).
$$

It is particularly useful for:

* exponential growth and decay
* logistic growth
* population models
* simple physical models
* some nonlinear first-order ODEs

Not every first-order ODE can be separated.

---

## Key Idea

The method transforms a differential equation into two integrals:

$$
\boxed{
\frac{dy}{dx}=f(x)g(y)
\quad\Longrightarrow\quad
\int\frac{1}{g(y)},dy
=

\int f(x),dx
}
$$

The main idea is to **separate the variables before integrating**.
