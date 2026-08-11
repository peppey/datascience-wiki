# Confidence Intervals

## TL;DR

A **confidence interval (CI)** is a range of values used to estimate an unknown population parameter from a sample.

For example, instead of reporting only a sample mean

$$
\bar{x} = 10.2,
$$

we might report

$$
95 \% \text{ CI} = [9.8, 10.6].
$$

The interval describes the uncertainty associated with the estimate.

---

## Definition

Let $\theta$ be an unknown population parameter.

A confidence interval is an interval

$$
[L(X), U(X)]
$$

constructed from sample data $X$ such that

$$
P\left(
L(X) \leq \theta \leq U(X)
\right)
=======

1-\alpha.
$$

Here:

* $\theta$ is the unknown parameter
* $L(X)$ is the lower bound
* $U(X)$ is the upper bound
* $1-\alpha$ is the **confidence level**
* $\alpha$ is the significance level

Common confidence levels are:

* $90\%$
* $95\%$
* $99\%$

---

## Example: Mean

Suppose we estimate a population mean using a sample mean $\bar{x}$.

If the population standard deviation $\sigma$ is known, a confidence interval can be constructed as

$$
\bar{x}
\pm
z_{\alpha/2}
\frac{\sigma}{\sqrt{n}},
$$

where:

* $n$ is the sample size
* $\sigma$ is the population standard deviation
* $z_{\alpha/2}$ is a standard normal quantile

For a $95\%$ confidence interval:

$$
z_{\alpha/2} \approx 1.96.
$$

Thus,

$$
\boxed{
\bar{x}
\pm
1.96\frac{\sigma}{\sqrt{n}}
}
$$

---

## Unknown Standard Deviation

If $\sigma$ is unknown, the sample standard deviation $s$ can be used.

The corresponding interval is often

$$
\bar{x}
\pm
t_{\alpha/2,n-1}
\frac{s}{\sqrt{n}},
$$

where $t_{\alpha/2,n-1}$ is a quantile of the **Student's $t$-distribution**.

---

## Interpretation

A common interpretation of a $95\%$ confidence interval is:

> If we repeatedly took samples and constructed confidence intervals using the same procedure, approximately $95\%$ of those intervals would contain the true parameter.

Importantly, this does **not** mean that there is a 95% probability that the fixed parameter lies inside a particular computed interval.

---

## Confidence Level

Higher confidence generally produces a wider interval:

```text
90%:       [────────────]
95%:      [──────────────]
99%:    [──────────────────]
```

For a fixed sample size:

$$
\text{higher confidence}
\Rightarrow
\text{wider interval}.
$$

---

## Sample Size

For many common confidence intervals, increasing the sample size reduces the uncertainty.

For the mean:

$$
\text{standard error}
=

\frac{\sigma}{\sqrt{n}}.
$$

Therefore,

$$
n \uparrow
\quad\Rightarrow\quad
\text{interval width} \downarrow.
$$

---

## Confidence Interval vs. Prediction Interval

A **confidence interval** estimates a population parameter, such as a mean.

A **prediction interval** estimates the range in which a future individual observation is expected to fall.

| Confidence Interval                       | Prediction Interval             |
| ----------------------------------------- | ------------------------------- |
| Estimates a parameter                     | Predicts a future observation   |
| Usually narrower                          | Usually wider                   |
| Describes uncertainty about the parameter | Includes individual variability |

---

## Applications

Confidence intervals are commonly used for:

* Population means
* Population proportions
* Regression coefficients
* Treatment effects
* Model performance metrics
* Differences between groups

They provide more information about uncertainty than a point estimate alone.

---

## Key Idea

A confidence interval combines a **point estimate** with an estimate of its **uncertainty**:

$$
\boxed{
\text{estimate}
\pm
\text{margin of error}
}
$$

The confidence level determines how much uncertainty the interval is designed to cover.
