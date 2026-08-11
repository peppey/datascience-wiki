# Covariance

## TL;DR

**Covariance** measures how two random variables vary together.

For random variables $X$ and $Y$:

$$
\operatorname{Cov}(X,Y)
=

\mathbb{E}\left[(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])\right]
$$

Equivalently:

$$
\operatorname{Cov}(X,Y)
=

\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]
$$

* $\operatorname{Cov}(X,Y)>0$: $X$ and $Y$ tend to increase together.
* $\operatorname{Cov}(X,Y)<0$: when one increases, the other tends to decrease.
* $\operatorname{Cov}(X,Y)=0$: no linear co-variation.

## Sample Covariance

For observations $(x_1,y_1),\ldots,(x_n,y_n)$:

$$
s_{XY}
=

\frac{1}{n-1}
\sum_{i=1}^{n}
(x_i-\bar{x})(y_i-\bar{y})
$$

where $\bar{x}$ and $\bar{y}$ are the sample means.

## Covariance Matrix

For a random vector

$$
X =
\begin{pmatrix}
X_1\
\vdots\
X_n
\end{pmatrix},
$$

the covariance matrix is

$$
\Sigma_{ij}
=

\operatorname{Cov}(X_i,X_j).
$$

Thus,

$$
\Sigma =
\begin{pmatrix}
\operatorname{Var}(X_1) & \operatorname{Cov}(X_1,X_2) & \cdots\
\operatorname{Cov}(X_2,X_1) & \operatorname{Var}(X_2) & \cdots\
\vdots & \vdots & \ddots
\end{pmatrix}.
$$

The diagonal contains the **variances**, while the off-diagonal entries contain the **covariances**.

## Properties

Covariance is symmetric:

$$
\operatorname{Cov}(X,Y)=\operatorname{Cov}(Y,X).
$$

For constants $a,b,c,d$:

$$
\operatorname{Cov}(aX+b,cY+d)
=

ac,\operatorname{Cov}(X,Y).
$$

The variance is the covariance of a variable with itself:

$$
\operatorname{Var}(X)=\operatorname{Cov}(X,X).
$$

If $X$ and $Y$ are independent, then:

$$
\operatorname{Cov}(X,Y)=0.
$$

However, zero covariance does **not** generally imply independence.

## Relation to Correlation

Covariance depends on the scale of the variables. **Correlation** normalizes covariance:

$$
\rho_{X,Y}
=

\frac{\operatorname{Cov}(X,Y)}
{\sigma_X\sigma_Y}.
$$

Therefore, correlation is dimensionless and always lies between $-1$ and $1$.
