# Central Limit Theorem

## TL;DR

The **Central Limit Theorem (CLT)** states that, under suitable conditions, the distribution of the **sample mean** approaches a normal distribution as the sample size increases.

If

$$
X_1,\ldots,X_n
$$

are independent and identically distributed random variables with mean $\mu$ and finite variance $\sigma^2$, then:

$$
\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}
\rightarrow
\mathcal{N}(0,1)
$$

as $n\rightarrow\infty$.

---

## Sample Mean

The sample mean is:

$$
\bar{X}
=

\frac{1}{n}
\sum_{i=1}^{n}X_i
$$

For sufficiently large $n$, it can be approximated by:

$$
\bar{X}
\approx
\mathcal{N}
\left(
\mu,
\frac{\sigma^2}{n}
\right)
$$

Thus, the standard deviation of the sample mean is:

$$
\frac{\sigma}{\sqrt{n}}
$$

This is called the **standard error**.

---

## Why It Matters

The CLT explains why the normal distribution appears so frequently in statistics.

Even if the original data is not normally distributed, the distribution of the sample mean can become approximately normal for sufficiently large samples.

This enables statistical methods such as:

* confidence intervals
* hypothesis testing
* estimation
* statistical modeling

---

## Example

Suppose individual observations follow a skewed distribution:

$$
X_i \sim F
$$

with:

$$
\mathbb{E}[X_i]=\mu
$$

and:

$$
\operatorname{Var}(X_i)=\sigma^2
$$

Taking increasingly large samples and computing their means produces a distribution that becomes increasingly close to:

$$
\mathcal{N}
\left(
\mu,
\frac{\sigma^2}{n}
\right)
$$

The original distribution does **not** need to be normal.

---

## Important Conditions

The classical CLT assumes, among other conditions:

* observations are independent
* observations are identically distributed
* the mean exists
* the variance is finite

There are also generalized versions of the CLT that relax some of these assumptions.

---

## CLT vs. Law of Large Numbers

The **Law of Large Numbers** states that:

$$
\bar{X}\rightarrow\mu
$$

as $n$ increases.

It describes **where the sample mean converges**.

The **Central Limit Theorem** describes the **distribution of the fluctuations around the mean**:

$$
\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}
\rightarrow
\mathcal{N}(0,1)
$$

---

## Related Concepts

* [Normal Distribution](normal-distribution.md)
* [Law of Large Numbers](law-of-large-numbers.md)
* [Expected Value](expected-value.md)
* [Variance](variance.md)
* [Confidence Intervals](confidence-intervals.md)
* [Sampling Distribution](sampling-distribution.md)
