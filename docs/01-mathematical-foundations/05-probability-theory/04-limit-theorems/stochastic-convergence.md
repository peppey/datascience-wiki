# Stochastic Convergence

## TL;DR

**Stochastic convergence** describes how a sequence of random variables approaches a limiting random variable.

Unlike ordinary convergence, the variables are random, so several different notions of convergence are possible.

The main types are:

* convergence almost surely
* convergence in probability
* convergence in distribution
* convergence in $L^p$

## Convergence Almost Surely

A sequence $X_1,X_2,\ldots$ converges **almost surely** to $X$ if:

$$
P\left(
\lim_{n\to\infty}X_n=X
\right)=1.
$$

It means that for almost every outcome $\omega$:

$$
X_n(\omega)\to X(\omega).
$$

This is one of the strongest common forms of stochastic convergence.

## Convergence in Probability

$X_n$ converges **in probability** to $X$ if, for every $\varepsilon>0$:

$$
P(|X_n-X|>\varepsilon)
\to0
\qquad\text{as }n\to\infty.
$$

In other words, the probability that $X_n$ differs substantially from $X$ becomes arbitrarily small.

We write:

$$
X_n\xrightarrow{P}X.
$$

## Convergence in Distribution

$X_n$ converges **in distribution** to $X$ if the cumulative distribution functions converge at every continuity point of $F_X$:

$$
F_{X_n}(x)\to F_X(x).
$$

We write:

$$
X_n\xrightarrow{d}X.
$$

Convergence in distribution concerns the **distributions** of the random variables rather than their individual outcomes.

## Convergence in $L^p$

For $p\geq1$, $X_n$ converges to $X$ in $L^p$ if:

$$
\mathbb{E}[|X_n-X|^p]\to0.
$$

We write:

$$
X_n\xrightarrow{L^p}X.
$$

For $p=2$, this is called **mean-square convergence**.

## Relationships

The common implications are:

$$
X_n\xrightarrow{\text{a.s.}}X
\quad\Longrightarrow\quad
X_n\xrightarrow{P}X
\quad\Longrightarrow\quad
X_n\xrightarrow{d}X.
$$

Also, for $p\geq1$:

$$
X_n\xrightarrow{L^p}X
\quad\Longrightarrow\quad
X_n\xrightarrow{P}X.
$$

The converse implications generally do **not** hold.

## Example

Let $X_1,X_2,\ldots$ be independent random variables with:

$$
X_i\sim\operatorname{Bernoulli}(p).
$$

The sample mean is:

$$
\bar X_n
=

\frac{1}{n}\sum_{i=1}^nX_i.
$$

The **Law of Large Numbers** states that:

$$
\bar X_n\xrightarrow{P}p
$$

under the weak law, and under appropriate conditions:

$$
\bar X_n\xrightarrow{\text{a.s.}}p
$$

under the strong law.

Thus, stochastic convergence provides the mathematical language for describing why sample averages approach their population expectation.

## Importance

Stochastic convergence is fundamental to **probability theory and statistics**. It is used to establish the theoretical behavior of estimators, sample averages, and statistical models as the amount of data increases.
