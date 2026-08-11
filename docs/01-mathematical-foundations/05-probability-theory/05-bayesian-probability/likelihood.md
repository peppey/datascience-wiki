# Likelihood

## TL;DR

**Likelihood** measures how well different parameter values explain observed data.

Given observed data $x$ and a statistical model with parameters $\theta$, the likelihood is:

$$
L(\theta\mid x)
=

P(x\mid\theta)
$$

The goal is often to find the parameter values that make the observed data most likely.

---

## Probability vs. Likelihood

Probability and likelihood use the same mathematical expression but have different interpretations.

**Probability:**

> Given the parameters, how likely is the data?

$$
P(x\mid\theta)
$$

**Likelihood:**

> Given the observed data, which parameters are most plausible?

$$
L(\theta\mid x)
$$

The data $x$ is treated as **fixed**, while $\theta$ varies.

---

## Example

Suppose we observe several coin flips and want to estimate the probability $\theta$ of heads.

For the observations:

```text
H H T H T H
```

the likelihood is:

$$
L(\theta)
=

\theta^4(1-\theta)^2
$$

Different values of $\theta$ result in different likelihoods.

The value of $\theta$ that maximizes the likelihood is the **maximum likelihood estimate**.

---

## Likelihood Function

For independent observations $x_1,\dots,x_n$:

$$
L(\theta\mid x_1,\dots,x_n)
=

\prod_{i=1}^{n}
P(x_i\mid\theta)
$$

For continuous data, the probability density is used instead:

$$
L(\theta\mid x)
=

\prod_{i=1}^{n}
f(x_i\mid\theta)
$$

---

## Log-Likelihood

Because likelihoods often involve products of many small numbers, it is common to work with the **log-likelihood**:

$$
\ell(\theta)
=

\log L(\theta\mid x)
$$

For independent observations:

$$
\ell(\theta)
=

\sum_{i=1}^{n}
\log f(x_i\mid\theta)
$$

Since the logarithm is monotonically increasing:

$$
\arg\max_\theta L(\theta)
=

\arg\max_\theta \ell(\theta)
$$

Therefore, maximizing the likelihood and maximizing the log-likelihood give the same parameter estimate.

---

## Maximum Likelihood Estimation

**Maximum Likelihood Estimation (MLE)** chooses the parameters that maximize the likelihood:

$$
\hat{\theta}
=

\arg\max_\theta L(\theta\mid x)
$$

Equivalently:

$$
\hat{\theta}
=

\arg\max_\theta \ell(\theta)
$$

MLE is one of the most important methods for **parameter estimation**.

---

## Likelihood in Machine Learning

Likelihood plays an important role in many machine learning methods.

Examples include:

* Logistic regression
* Linear regression
* Gaussian Mixture Models
* Hidden Markov Models
* Neural networks with probabilistic outputs

For example, training a probabilistic model can often be formulated as **maximizing the likelihood of the training data**.

---

## Likelihood and Loss Functions

Maximizing likelihood can be converted into minimizing a loss.

Because:

$$
\ell(\theta)=\log L(\theta)
$$

maximizing log-likelihood is equivalent to minimizing **negative log-likelihood**:

$$
\mathcal{L}(\theta)
=

-\ell(\theta)
$$

This connects statistical estimation directly to machine learning optimization.

---

## Likelihood vs. Probability

| Concept     | What varies? | Question                                |
| ----------- | ------------ | --------------------------------------- |
| Probability | Data         | How likely is the data given the model? |
| Likelihood  | Parameters   | Which parameters best explain the data? |

The distinction is mainly about **what is treated as fixed and what is varied**.