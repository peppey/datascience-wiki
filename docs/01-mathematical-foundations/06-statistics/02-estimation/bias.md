# Bias

## TL;DR

**Bias** describes a systematic tendency for an estimator or model to deviate from the true value.

In machine learning, bias is often associated with **underfitting**: a model with high bias is too simple to capture important patterns in the data.

---

## Statistical Bias

For an estimator $\hat{\theta}$ of a parameter $\theta$, the bias is:

$$
\operatorname{Bias}(\hat{\theta})
=

\mathbb{E}[\hat{\theta}] - \theta
$$

An estimator is **unbiased** if:

$$
\mathbb{E}[\hat{\theta}] = \theta
$$

---

## Bias in Machine Learning

In the **bias-variance trade-off**, bias measures the error caused by simplifying assumptions made by the model.

A model with **high bias** typically:

* is too simple
* misses important patterns
* underfits the training data
* performs poorly on both training and test data

A model with **low bias** is more flexible and can represent more complex relationships.

---

## Example

Suppose the true relationship between $x$ and $y$ is nonlinear, but we use a linear model:

$$
\hat{y}=ax+b
$$

The linear model may systematically fail to represent the true relationship.

This results in **high bias**.

Using a more flexible model can reduce the bias, but may increase variance.

---

## Bias-Variance Trade-Off

Prediction error can be decomposed into several components:

$$
\text{Expected Error}
=

\text{Bias}^2
+
\text{Variance}
+
\text{Irreducible Error}
$$

The goal is not necessarily to minimize bias alone, but to find a good balance between **bias and variance**.

---

## Key Idea

**High bias → model too simple → underfitting**

**Low bias → model more flexible → potentially higher variance**

Bias is therefore an important concept for understanding **model complexity and generalization**.
