# Estimators

## TL;DR

An **estimator** is a rule or function that uses sample data to estimate an unknown population parameter.

For example, the sample mean

$$
\hat{\mu} = \frac{1}{n}\sum_{i=1}^{n}X_i
$$

is an estimator of the population mean $\mu$.

---

## Estimator vs. Estimate

An **estimator** is the rule used to calculate an estimate.

An **estimate** is the concrete value obtained from a particular sample.

For example:

$$
\hat{\mu} = \frac{1}{n}\sum_{i=1}^{n}X_i
$$

is an estimator, while

$$
\hat{\mu}=5.2
$$

is an estimate obtained from a specific dataset.

---

## Bias

The bias of an estimator $\hat{\theta}$ for a parameter $\theta$ is:

$$
\operatorname{Bias}(\hat{\theta})
=

\mathbb{E}[\hat{\theta}]-\theta
$$

An estimator is **unbiased** if:

$$
\mathbb{E}[\hat{\theta}]=\theta
$$

---

## Variance

An estimator can produce different values for different samples.

Its variance is:

$$
\operatorname{Var}(\hat{\theta})
$$

A low-variance estimator produces estimates that are relatively stable across samples.

---

## Consistency

An estimator is **consistent** if it converges to the true parameter as the sample size increases.

For an estimator $\hat{\theta}_n$:

$$
\hat{\theta}_n
\xrightarrow{P}
\theta
$$

as:

$$
n\rightarrow\infty.
$$

---

## Common Estimators

| Parameter                       | Common estimator                     |
| ------------------------------- | ------------------------------------ |
| Population mean $\mu$           | Sample mean $\bar{X}$                |
| Population variance $\sigma^2$  | Sample variance $S^2$                |
| Population proportion $p$       | Sample proportion $\hat{p}$          |
| Regression coefficients $\beta$ | Estimated coefficients $\hat{\beta}$ |

---

## Maximum Likelihood Estimator

A common way to construct an estimator is **maximum likelihood estimation (MLE)**.

The maximum likelihood estimator is:

$$
\hat{\theta}_{MLE}
=

\arg\max_{\theta} L(\theta)
$$

where $L(\theta)$ is the likelihood of the observed data given $\theta$.

---

## Bias-Variance Trade-Off

Estimators can be compared using their bias and variance.

Under squared error loss:

$$
\operatorname{MSE}(\hat{\theta})
=

\operatorname{Bias}(\hat{\theta})^2
+
\operatorname{Var}(\hat{\theta})
$$

A biased estimator can therefore sometimes be preferable if its lower variance results in a lower overall MSE.

---

## Key Idea

An **estimator** is a statistical procedure for estimating an unknown parameter from sample data.

Important properties include:

* **Bias**
* **Variance**
* **Consistency**
* **Efficiency**
* **Mean squared error (MSE)**
