# Beta Distribution

## TL;DR

The **Beta distribution** is a continuous probability distribution defined on $[0,1]$.

It is commonly used to model **probabilities, proportions, and rates**.

A random variable $X$ follows a Beta distribution if:

$$
X\sim\operatorname{Beta}(\alpha,\beta),
$$

where $\alpha,\beta>0$.

## Probability Density Function

The probability density function is:

$$
f(x;\alpha,\beta)
=

\frac{x^{\alpha-1}(1-x)^{\beta-1}}
{B(\alpha,\beta)},
\qquad 0\leq x\leq1,
$$

where $B(\alpha,\beta)$ is the **Beta function**, which normalizes the density.

## Parameters

The parameters $\alpha$ and $\beta$ determine the shape of the distribution.

Some examples:

* $\operatorname{Beta}(1,1)$: uniform distribution
* $\alpha>\beta$: more mass toward $1$
* $\alpha<\beta$: more mass toward $0$
* $\alpha,\beta>1$: often unimodal
* $\alpha,\beta<1$: more mass near $0$ and $1$

## Mean and Variance

The expected value is:

$$
\mathbb{E}[X]
=
\frac{\alpha}{\alpha+\beta}.
$$

The variance is:

$$
\operatorname{Var}(X)
=

\frac{\alpha\beta}
{(\alpha+\beta)^2(\alpha+\beta+1)}.
$$

## Bayesian Inference

The Beta distribution is particularly important in **Bayesian inference** because it is the **conjugate prior** for Bernoulli and Binomial likelihoods.

For example, suppose:

$$
\theta\sim\operatorname{Beta}(\alpha,\beta)
$$

and we observe $h$ successes and $t$ failures.

The posterior is:

$$
\theta\mid D
\sim
\operatorname{Beta}(\alpha+h,\beta+t).
$$

Thus, the Beta distribution provides a convenient way to represent uncertainty about an unknown probability and update it as data is observed.

## Applications

The Beta distribution is commonly used for:

* Bayesian estimation of probabilities
* Modeling proportions
* Conversion rates
* Success probabilities
* Bayesian A/B testing
* Reliability and rate modeling