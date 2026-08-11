# Consistency

## TL;DR

In statistics, an estimator is **consistent** if it approaches the true parameter value as the sample size increases.

For an estimator $\hat{\theta}_n$ of a parameter $\theta$:

$$
\hat{\theta}_n \xrightarrow{P} \theta
\qquad\text{as } n\to\infty.
$$

Consistency means that, with enough data, the estimator becomes arbitrarily close to the true value.

---

## Formal Definition

An estimator $\hat{\theta}_n$ is **consistent** for $\theta$ if, for every $\varepsilon>0$:

$$
P\left(
|\hat{\theta}_n-\theta|>\varepsilon
\right)
\to 0
\qquad\text{as } n\to\infty.
$$

This is **consistency in probability**.

---

## Example: Sample Mean

Suppose:

$$
X_1,X_2,\ldots,X_n
$$

are independent and identically distributed random variables with finite expectation:

$$
\mathbb{E}[X_i]=\mu.
$$

The sample mean is:

$$
\bar{X}_n
=

\frac{1}{n}
\sum_{i=1}^{n}X_i.
$$

By the **Law of Large Numbers**:

$$
\bar{X}_n\xrightarrow{P}\mu.
$$

Therefore, $\bar{X}_n$ is a consistent estimator of $\mu$.

---

## Consistency vs. Unbiasedness

**Unbiasedness** and **consistency** are different properties.

An estimator can be biased but consistent.

For example, consider:

$$
\hat{\mu}_n
=

\frac{1}{n+1}
\sum_{i=1}^{n}X_i.
$$

Its expectation is:

$$
\mathbb{E}[\hat{\mu}_n]
=

\frac{n}{n+1}\mu,
$$

so it is biased for finite $n$.

However:

$$
\frac{n}{n+1}\mu\to\mu,
$$

and therefore $\hat{\mu}_n$ is still consistent.

---

## Strong Consistency

A stronger form is **almost sure consistency**:

$$
\hat{\theta}_n
\xrightarrow{\text{a.s.}}
\theta.
$$

This means:

$$
P\left(
\lim_{n\to\infty}\hat{\theta}_n=\theta
\right)=1.
$$

Almost sure convergence implies convergence in probability:

$$
\hat{\theta}_n\xrightarrow{\text{a.s.}}\theta
\quad\Longrightarrow\quad
\hat{\theta}_n\xrightarrow{P}\theta.
$$

---

## Key Idea

**Consistency means that an estimator gets closer to the true parameter as more data become available.**

It is one of the fundamental properties used to evaluate statistical estimators.
