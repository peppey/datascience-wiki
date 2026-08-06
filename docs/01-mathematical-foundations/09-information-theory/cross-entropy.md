# Cross-Entropy

## TL;DR

**Cross-Entropy** measures the difference between two probability distributions.

In machine learning, it is commonly used as a **loss function for classification models**.

The goal is to minimize the difference between:

- the true distribution of the labels
- the predicted probabilities of the model

---

## Definition

For two probability distributions $p$ and $q$, the cross-entropy is:

$$
H(p,q)=-\sum_x p(x)\log(q(x))
$$

where:

- $p(x)$ is the true probability
- $q(x)$ is the predicted probability

---

## Binary Cross-Entropy

For binary classification:

$$
L=-\left(y\log(\hat{y})+(1-y)\log(1-\hat{y})\right)
$$

where:

- $y$ is the true label ($0$ or $1$)
- $\hat{y}$ is the predicted probability of class $1$

Example:

A model predicts:

$$
\hat{y}=0.9
$$

for a sample with:

$$
y=1
$$

The loss is small because the prediction is close to the true label.

---

## Multiclass Cross-Entropy

For multiple classes:

$$
L=-\sum_{i=1}^{C} y_i\log(\hat{y}_i)
$$

where:

- $C$ is the number of classes
- $y_i$ is the true class indicator
- $\hat{y}_i$ is the predicted probability

Usually, the model output is converted into probabilities using **softmax**.

---

## Intuition

Cross-entropy penalizes confident wrong predictions.

Example:

True class:
Cat

Prediction 1:
Cat: 0.95
Dog: 0.05

Low loss.

Prediction 2:
Cat: 0.05
Dog: 0.95

High loss.

A model is strongly penalized when it assigns a high probability to the wrong class.

---

## Connection to Maximum Likelihood

Minimizing cross-entropy is equivalent to maximizing the likelihood of the observed data.

The model tries to find parameters that make the correct labels as probable as possible.

---

## Cross-Entropy vs Mean Squared Error

| Cross-Entropy | Mean Squared Error |
|---|---|
| Mostly used for classification | Mostly used for regression |
| Works with probabilities | Works with continuous values |
| Strong penalty for confident wrong predictions | Measures squared distance |

For classification problems, cross-entropy usually provides better gradients than mean squared error.

---

## Summary

- Cross-entropy measures the difference between true and predicted probabilities.
- It is the standard loss function for classification.
- It strongly penalizes confident incorrect predictions.
- Minimizing cross-entropy improves probabilistic predictions.
