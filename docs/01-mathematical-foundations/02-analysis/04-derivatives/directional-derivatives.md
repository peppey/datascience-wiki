# Directional Derivatives

## TL;DR

The **directional derivative** measures how fast a function changes in a specific direction.

For a differentiable function

$$
f:\mathbb{R}^n\rightarrow\mathbb{R},
$$

at a point $x$ and in a unit direction $u$, the directional derivative is

$$
D_u f(x)=\nabla f(x)\cdot u.
$$

It generalizes the ordinary derivative to arbitrary directions.

## Definition

Let

$$
u\in\mathbb{R}^n
$$

be a unit vector, meaning

$$
|u|=1.
$$

The directional derivative of $f$ at $x$ in the direction $u$ is

$$
D_u f(x)
=

\lim_{h\rightarrow 0}
\frac{f(x+hu)-f(x)}{h}.
$$

It describes the instantaneous rate of change of $f$ when moving from $x$ in direction $u$.

## Example

Consider

$$
f(x,y)=x^2+y^2
$$

at the point

$$
p=(1,2).
$$

The gradient is

$$
\nabla f(1,2)
=

\begin{pmatrix}
2\
4
\end{pmatrix}.
$$

Suppose we want the directional derivative in the direction

$$
u=
\frac{1}{\sqrt{2}}
\begin{pmatrix}
1\
1
\end{pmatrix}.
$$

Then

$$
D_u f(1,2)
=

\nabla f(1,2)\cdot u
$$

and therefore

$$
D_u f(1,2)
=
 
 \frac{2+4}{\sqrt{2}}

3\sqrt{2}.
$$

## Relation to the Gradient

The gradient determines the directional derivative:

$$
D_u f(x)=\nabla f(x)\cdot u.
$$

The directional derivative is largest when $u$ points in the direction of the gradient.

Thus:

* $\nabla f(x)$ points in the direction of steepest increase.
* $-\nabla f(x)$ points in the direction of steepest decrease.
* $|\nabla f(x)|$ is the maximum directional derivative.

## Connection to Partial Derivatives

Partial derivatives are special cases of directional derivatives.

For example, the partial derivative with respect to $x_i$ corresponds to the direction of the $i$-th coordinate axis:

$$
\frac{\partial f}{\partial x_i}
=

D_{e_i}f,
$$

where $e_i$ is the $i$-th standard basis vector.

Therefore, directional derivatives generalize partial derivatives to arbitrary directions.

## In Machine Learning

Directional derivatives describe how a loss function changes when model parameters are changed in a particular direction.

For a loss function $L(\theta)$ and parameter direction $u$:

$$
D_u L(\theta)
=

\nabla L(\theta)\cdot u.
$$

This is useful for understanding optimization and gradient-based learning.