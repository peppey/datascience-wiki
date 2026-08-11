# Partial Derivatives

## TL;DR

A **partial derivative** measures how a function changes with respect to one variable while keeping all other variables constant.

For a function

$$
f(x_1,\ldots,x_n),
$$

the partial derivative with respect to $x_i$ is written as

$$
\frac{\partial f}{\partial x_i}.
$$

## Definition

For a function of two variables

$$
f(x,y),
$$

the partial derivative with respect to $x$ is

$$
\frac{\partial f}{\partial x}
=

\lim_{h\rightarrow 0}
\frac{f(x+h,y)-f(x,y)}{h}.
$$

The variable $y$ is treated as constant.

Similarly,

$$
\frac{\partial f}{\partial y}
=

\lim_{h\rightarrow 0}
\frac{f(x,y+h)-f(x,y)}{h}.
$$

## Example

Consider

$$
f(x,y)=x^2y+3y.
$$

The partial derivative with respect to $x$ is

$$
\frac{\partial f}{\partial x}=2xy.
$$

Here, $y$ is treated as a constant.

The partial derivative with respect to $y$ is

$$
\frac{\partial f}{\partial y}=x^2+3.
$$

Here, $x$ is treated as a constant.

## Partial Derivatives and the Gradient

The partial derivatives can be combined into the **gradient**:

$$
\nabla f(x)
=

\begin{pmatrix}
\frac{\partial f}{\partial x_1}\
\vdots\
\frac{\partial f}{\partial x_n}
\end{pmatrix}.
$$

For

$$
f(x,y),
$$

this becomes

$$
\nabla f(x,y)
=

\begin{pmatrix}
\frac{\partial f}{\partial x}\
\frac{\partial f}{\partial y}
\end{pmatrix}.
$$

The gradient describes the direction of steepest increase.

## Higher-Order Partial Derivatives

Partial derivatives can be taken multiple times.

For example,

$$
\frac{\partial^2 f}{\partial x^2}
$$

is the second partial derivative with respect to $x$.

Mixed partial derivatives are written as

$$
\frac{\partial^2 f}{\partial x\partial y}.
$$

Under suitable smoothness conditions, mixed partial derivatives are equal:

$$
\frac{\partial^2 f}{\partial x\partial y}
=

\frac{\partial^2 f}{\partial y\partial x}.
$$

## In Machine Learning

Partial derivatives are fundamental for optimization.

For a loss function

$$
L(\theta_1,\ldots,\theta_n),
$$

the partial derivative

$$
\frac{\partial L}{\partial \theta_i}
$$

describes how the loss changes when only the parameter $\theta_i$ is changed.

Together, these derivatives form the gradient used by algorithms such as **gradient descent**.