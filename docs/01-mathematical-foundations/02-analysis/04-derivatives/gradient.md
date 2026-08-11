# Gradient

## TL;DR

The **gradient** describes the direction of **steepest increase** of a scalar-valued function.

For a function

$$
f:\mathbb{R}^n\rightarrow\mathbb{R},
$$

the gradient is

$$
\nabla f(x)
=

\begin{pmatrix}
\frac{\partial f}{\partial x_1}\
\frac{\partial f}{\partial x_2}\
\vdots\
\frac{\partial f}{\partial x_n}
\end{pmatrix}.
$$

It points in the direction in which $f$ increases most rapidly.

## Example

Consider

$$
f(x,y)=x^2+y^2.
$$

Its gradient is

$$
\nabla f(x,y)
=

\begin{pmatrix}
2x\
2y
\end{pmatrix}.
$$

At the point $(1,2)$:

$$
\nabla f(1,2)
=

\begin{pmatrix}
2\
4
\end{pmatrix}.
$$

Thus, the function increases most rapidly in the direction $(2,4)$.

## Gradient Descent

In machine learning, gradients are commonly used to **minimize a loss function**.

If $L(\theta)$ is a loss function, gradient descent updates the parameters according to

$$
\theta_{\text{new}}
=

\theta_{\text{old}}

\eta \nabla L(\theta_{\text{old}}),
$$

where $\eta$ is the **learning rate**.

The negative gradient points in the direction of steepest decrease.

## Gradient and Directional Derivatives

For a unit vector $u$, the directional derivative is

$$
D_u f(x)
=

\nabla f(x)\cdot u.
$$

The maximum directional derivative is achieved when $u$ points in the direction of the gradient.

Therefore, the gradient provides both:

* the direction of steepest increase
* the rate of steepest increase, given by $|\nabla f(x)|$

## In Machine Learning

For a model with parameters

$$
\theta=(\theta_1,\ldots,\theta_n),
$$

the gradient of the loss is

$$
\nabla_\theta L
=

\begin{pmatrix}
\frac{\partial L}{\partial \theta_1}\
\vdots\
\frac{\partial L}{\partial \theta_n}
\end{pmatrix}.
$$

Optimization algorithms such as **gradient descent**, **stochastic gradient descent**, and **Adam** use this information to update model parameters.