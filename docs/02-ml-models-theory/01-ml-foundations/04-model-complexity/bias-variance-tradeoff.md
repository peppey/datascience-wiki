# Bias-Variance Trade-Off

## TL;DR

The **bias-variance trade-off** describes the balance between two sources of prediction error:

* **Bias**: error caused by overly simple assumptions
* **Variance**: error caused by excessive sensitivity to the training data

Increasing model complexity usually **reduces bias but increases variance**.

---

## Bias

**Bias** measures how much a model systematically differs from the true relationship.

High bias typically leads to **underfitting**.

Examples:

* using a linear model for a strongly nonlinear problem
* using a very shallow decision tree
* using an overly restrictive model

---

## Variance

**Variance** measures how much a model's predictions change when trained on different samples of the data.

High variance typically leads to **overfitting**.

Examples:

* a very deep decision tree
* a highly complex polynomial model
* a model that memorizes the training data

---

## Model Complexity

As model complexity increases:

$$
\text{Bias} \downarrow
$$

while typically:

$$
\text{Variance} \uparrow
$$

A very simple model has high bias and low variance.

A very complex model has low bias and high variance.

The goal is to find a model complexity that provides a good balance.

---

## Expected Prediction Error

Under the standard squared-error decomposition:

$$
\text{Expected Error}
=

\text{Bias}^2
+
\text{Variance}
+
\text{Irreducible Error}
$$

The **irreducible error** comes from noise in the data and cannot be eliminated by choosing a better model.

---

## Example

Consider polynomial regression.

A degree-1 polynomial:

$$
f(x)=a_0+a_1x
$$

may be too simple and therefore have high bias.

A very high-degree polynomial may fit the training data extremely closely, resulting in high variance.

An intermediate degree may achieve a better balance:

$$
\boxed{\text{Low Bias} + \text{Low Variance}}
$$

---

## Underfitting and Overfitting

| Model                  | Bias     | Variance | Typical behavior    |
| ---------------------- | -------- | -------- | ------------------- |
| Too simple             | High     | Low      | Underfitting        |
| Appropriate complexity | Moderate | Moderate | Good generalization |
| Too complex            | Low      | High     | Overfitting         |

---

## Reducing Bias

Bias can often be reduced by:

* increasing model complexity
* adding relevant features
* using a more expressive model
* reducing overly strong regularization

## Reducing Variance

Variance can often be reduced by:

* increasing the training dataset
* using regularization
* reducing model complexity
* feature selection
* ensemble methods such as bagging
* cross-validation for model selection

---

## Key Idea

The **bias-variance trade-off** is the fundamental tension between models that are too simple and models that are too sensitive to the training data.

$$
\boxed{
\text{Good Generalization}
\approx
\text{appropriate bias-variance balance}
}
$$
