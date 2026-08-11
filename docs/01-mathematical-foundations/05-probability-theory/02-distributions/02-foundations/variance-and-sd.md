# Variance and Standard Deviation

## TL;DR

**Variance** and **standard deviation** measure how spread out values are around their mean.

Variance is the average squared deviation from the mean:

$$
\operatorname{Var}(X)
=

\mathbb{E}\left[(X-\mathbb{E}[X])^2\right]
$$

Standard deviation is the square root of the variance:

$$
\sigma_X
=

\sqrt{\operatorname{Var}(X)}
$$

## Variance

For a random variable $X$ with mean $\mu$:

$$
\operatorname{Var}(X)
=

\mathbb{E}\left[(X-\mu)^2\right]
$$

An equivalent form is:

$$
\operatorname{Var}(X)
=
\mathbb{E}[X^2]-\mathbb{E}[X]^2
$$

Variance is always non-negative:

$$
\operatorname{Var}(X)\geq 0
$$

A variance of zero means that $X$ is constant almost surely.

### Sample Variance

For observations $x_1,\ldots,x_n$ with sample mean $\bar{x}$:

$$
s^2
=

\frac{1}{n-1}
\sum_{i=1}^{n}(x_i-\bar{x})^2
$$

The denominator $n-1$ provides an unbiased estimator of the population variance.

## Standard Deviation

The standard deviation is the square root of the variance:

$$
\sigma
=

\sqrt{\operatorname{Var}(X)}
$$

For a sample:

$$
s
=

\sqrt{
\frac{1}{n-1}
\sum_{i=1}^{n}(x_i-\bar{x})^2
}
$$

Unlike variance, standard deviation has the **same units as the original variable**.

For example, if $X$ is measured in meters:

* variance is measured in $\mathrm{m}^2$
* standard deviation is measured in $\mathrm{m}$

## Interpretation

A small standard deviation means that values are concentrated close to the mean.

A large standard deviation means that values are more widely spread around the mean.

For a normally distributed variable, approximately:

$$
68%
$$

of observations lie within one standard deviation of the mean,

$$
95%
$$

within two standard deviations, and

$$
99.7%
$$

within three standard deviations.

## Relation to Covariance

Variance is a special case of covariance:

$$
\operatorname{Var}(X)
=

\operatorname{Cov}(X,X)
$$

For two random variables $X$ and $Y$:

$$
\operatorname{Cov}(X,Y)
=

\mathbb{E}[(X-\mu_X)(Y-\mu_Y)].
$$
