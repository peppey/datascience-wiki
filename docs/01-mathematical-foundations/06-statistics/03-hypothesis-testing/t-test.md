# t-Test

## TL;DR

A **t-test** is a statistical hypothesis test used to determine whether a mean differs significantly from a reference value or whether the means of two groups differ.

It is commonly used when the population variance is unknown and the sample size is relatively small.

---

## One-Sample t-Test

A **one-sample t-test** tests whether the mean of a sample differs from a hypothesized population mean $\mu_0$.

The test statistic is:

$$
t=
\frac{\bar{x}-\mu_0}
{s/\sqrt{n}}
$$

where:

* $\bar{x}$ is the sample mean
* $\mu_0$ is the hypothesized mean
* $s$ is the sample standard deviation
* $n$ is the sample size

Under the null hypothesis, the statistic follows a **t-distribution** with:

$$
df=n-1
$$

degrees of freedom.

---

## Two-Sample t-Test

A **two-sample t-test** compares the means of two independent groups.

For groups with means $\bar{x}_1,\bar{x}_2$:

$$
H_0:\mu_1=\mu_2
$$

The test can be performed assuming either:

* equal variances (**Student's t-test**)
* unequal variances (**Welch's t-test**)

Welch's t-test is generally preferred when the equality of variances cannot be assumed.

---

## Paired t-Test

A **paired t-test** is used when observations naturally occur in pairs, such as measurements taken:

* before and after a treatment
* from the same individuals
* under two experimental conditions

The test is performed on the differences:

$$
d_i=x_i-y_i
$$

and tests whether the mean difference is zero:

$$
H_0:\mu_d=0
$$

---

## Hypothesis Testing

A typical t-test uses:

$$
H_0:\text{no difference}
$$

against an alternative hypothesis such as:

$$
H_1:\text{there is a difference}.
$$

The resulting **p-value** indicates how compatible the observed data are with the null hypothesis.

A common significance level is:

$$
\alpha=0.05.
$$

If:

$$
p<\alpha,
$$

the null hypothesis is rejected.

---

## Assumptions

Depending on the type of t-test, common assumptions include:

* observations are independent
* the data are approximately normally distributed
* the outcome is measured on a continuous scale
* for the standard two-sample t-test, the groups have equal variances

Welch's t-test does **not** require equal variances.

---

## t-Distribution

The t-test uses the **Student's t-distribution** rather than the standard normal distribution because the population variance is estimated from the sample.

The t-distribution has heavier tails than the normal distribution, especially for small sample sizes.

As the degrees of freedom increase:

$$
t_{df}\rightarrow N(0,1).
$$

---

## Key Idea

A t-test asks whether an observed difference in means is large relative to the uncertainty in the estimated means.

It is one of the most common methods for comparing means in statistical hypothesis testing.
