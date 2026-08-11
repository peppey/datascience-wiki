# Normal Distribution

## TL;DR

The **normal distribution**, also called the **Gaussian distribution**, is a continuous probability distribution characterized by its mean $\mu$ and standard deviation $\sigma$.

It is written as:

$$
X \sim \mathcal{N}(\mu,\sigma^2)
$$

Its probability density function is:

$$
f(x)
=

\frac{1}{\sigma\sqrt{2\pi}}
\exp\left(
-\frac{(x-\mu)^2}{2\sigma^2}
\right)
$$

The normal distribution is symmetric around $\mu$.

---

## Parameters

The distribution has two parameters:

* $\mu$ — **mean**, determining the center
* $\sigma$ — **standard deviation**, determining the spread

The variance is:

$$
\operatorname{Var}(X)=\sigma^2
$$

and the expected value is:

$$
\mathbb{E}[X]=\mu
$$

---

## Standard Normal Distribution

The **standard normal distribution** has:

$$
\mu=0,\qquad \sigma=1
$$

and is denoted by:

$$
Z\sim\mathcal{N}(0,1)
$$

Any normally distributed variable can be standardized using:

$$
Z=\frac{X-\mu}{\sigma}
$$

---

## Properties

For a normal distribution:

* mean = median = mode
* it is symmetric around $\mu$
* approximately 68% of values lie within $1\sigma$
* approximately 95% lie within $2\sigma$
* approximately 99.7% lie within $3\sigma$

This is known as the **68–95–99.7 rule**.

---

## Central Limit Theorem

The normal distribution is closely related to the **Central Limit Theorem**.

Under suitable conditions, the sum or mean of many independent random variables approaches a normal distribution, even when the original variables are not normally distributed.

This is one reason why the normal distribution appears frequently in statistics.

---

## Applications

The normal distribution is commonly used for:

* modeling measurement errors
* statistical inference
* confidence intervals
* hypothesis testing
* regression
* Gaussian mixture models
* modeling noise
* approximating sampling distributions