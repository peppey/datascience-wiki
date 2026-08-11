# Bootstrap

## TL;DR

The **bootstrap** is a resampling method used to estimate the uncertainty or sampling distribution of a statistic without requiring a known analytical distribution.

It is commonly used for:

* confidence intervals
* standard errors
* bias estimation
* hypothesis testing
* model evaluation

---

## Basic Idea

Suppose we have observations:

$$
X={x_1,\ldots,x_n}.
$$

The **empirical distribution** assigns probability:

$$
\frac{1}{n}
$$

to each observation.

A bootstrap sample is created by sampling $n$ observations **with replacement** from the original data:

$$
X^*={x_1^*,\ldots,x_n^*}.
$$

The statistic of interest is then computed on the bootstrap sample:

$$
\hat{\theta}^*=T(X^*).
$$

This process is repeated many times.

---

## Bootstrap Distribution

After generating $B$ bootstrap samples:

$$
X_1^*,\ldots,X_B^*,
$$

we obtain bootstrap estimates:

$$
\hat{\theta}_1^*,\ldots,\hat{\theta}_B^*.
$$

Their empirical distribution approximates the sampling distribution of the statistic.

---

## Standard Error

The bootstrap standard error can be estimated as:

$$
\operatorname{SE}_{boot}
=

\sqrt{
\frac{1}{B-1}
\sum_{b=1}^{B}
\left(
\hat{\theta}_b^*-\bar{\theta}^*
\right)^2
}.
$$

where:

$$
\bar{\theta}^*
=

\frac{1}{B}
\sum_{b=1}^{B}\hat{\theta}_b^*.
$$

---

## Bootstrap Confidence Intervals

A simple approach is the **percentile bootstrap**.

For a confidence level of $1-\alpha$, the interval is obtained from the corresponding quantiles of the bootstrap distribution:

$$
\left[
q_{\alpha/2},
q_{1-\alpha/2}
\right].
$$

For example, a 95% confidence interval uses the 2.5th and 97.5th percentiles.

Other approaches include:

* basic bootstrap interval
* bias-corrected and accelerated (BCa) interval
* bootstrap-$t$ interval

---

## Example

Suppose we want to estimate the uncertainty of the sample mean.

Original data:

$$
x_1,\ldots,x_n.
$$

Repeatedly sample $n$ observations with replacement and calculate:

$$
\bar{x}^*
=

\frac{1}{n}
\sum_{i=1}^n x_i^*.
$$

The resulting distribution of $\bar{x}^*$ approximates the sampling distribution of the sample mean.

---

## Parametric vs. Nonparametric Bootstrap

The **nonparametric bootstrap** samples directly from the empirical distribution of the observed data.

The **parametric bootstrap** instead assumes a parametric model:

$$
X\sim P_\theta
$$

and generates bootstrap samples from the fitted model:

$$
X^*\sim P_{\hat{\theta}}.
$$

---

## Limitations

Bootstrap methods may perform poorly when:

* the sample size is very small
* observations are strongly dependent
* the statistic has unusual sampling behavior
* the empirical distribution poorly represents the population

For dependent data, specialized methods such as the **block bootstrap** can be used.

---

## Key Idea

The bootstrap replaces an unknown sampling distribution with a distribution obtained through repeated resampling:

$$
\boxed{
\text{Observed Data}
\rightarrow
\text{Resample With Replacement}
\rightarrow
\text{Statistic}
\rightarrow
\text{Bootstrap Distribution}
}
$$

It is one of the most general tools for estimating uncertainty from data.
