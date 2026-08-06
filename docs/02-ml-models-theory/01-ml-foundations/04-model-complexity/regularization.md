# Regularization

## TL;DR (30 seconds)

**Regularization** is a set of techniques used in machine learning to reduce **overfitting** by preventing models from becoming too complex.

The idea:

> A model should not only fit the training data well, but also generalize to unseen data.

Regularization adds an additional **penalty term** to the training objective that discourages overly complex models.

Common methods:

- **L1 regularization (Lasso)** → encourages sparse models by setting some weights exactly to zero
- **L2 regularization (Ridge / Weight Decay)** → keeps weights small
- **Dropout** → randomly disables neurons during training
- **Early stopping** → stops training before the model overfits

---

## Motivation: Overfitting

A machine learning model tries to minimize an error function:

$$
\min_\theta L(\theta)
$$

where:

- $\theta$ are the model parameters
- $L(\theta)$ is the training loss

A model with many parameters can memorize the training data instead of learning general patterns.

Example:

- A linear model with few parameters may underfit
- A very deep neural network may perfectly fit the training data but fail on new examples

This is called **overfitting**.

Regularization introduces a preference for simpler models.

---

## Regularized Objective Function

Instead of minimizing only the training loss:

$$
\min_\theta L(\theta)
$$

we optimize:

$$
\min_\theta L(\theta) + \lambda R(\theta)
$$

where:

- $L(\theta)$ = data loss
- $R(\theta)$ = regularization term
- $\lambda$ = regularization strength

The parameter $\lambda$ controls the trade-off:

- small $\lambda$ → focus more on fitting the data
- large $\lambda$ → stronger penalty, simpler model

---

## Regularization and Generalization

Regularization improves the ability of a model to generalize.
The relationship:

```text
Low complexity
      │
      ▼
Underfitting
      │
      ▼
Good generalization
      │
      ▼
Overfitting
      │
      ▼
High complexity
```


Regularization shifts the model toward the middle:
enough complexity to learn patterns
not enough complexity to memorize noise


## Connection to Bias-Variance Trade-off

Regularization increases **bias** but reduces **variance**.

Without regularization:

- Low training error
- High variance
- Poor generalization

With regularization:

- Slightly higher training error
- Lower variance
- Better test performance

Therefore, regularization is a way to control the **bias-variance trade-off**.

---

## Examples

## Linear Regression

Without regularization:

$$
\hat{y}=w_1x_1+w_2x_2+...+w_nx_n
$$

Large weights can cause instability and make the model sensitive to noise.

With L2 regularization:

$$
\min_w ||Xw-y||^2+\lambda||w||^2
$$

The penalty term discourages large weights and leads to a more stable model.

---

## Neural Networks

A deep neural network can have millions of parameters and may memorize the training data instead of learning general patterns.

Regularization techniques include:

- **Dropout**
- **Weight decay**
- **Data augmentation**
- **Early stopping**

These methods help the network learn more robust representations and improve generalization to unseen data.

---

## Overview

| Method | Idea | Main Effect |
|---|---|---|
| L1 regularization | Penalize absolute weights | Sparse models |
| L2 regularization | Penalize squared weights | Smaller weights |
| Elastic Net | Combine L1 + L2 | Sparse and stable models |
| Dropout | Remove neurons randomly | Robust representations |
| Early stopping | Stop training early | Prevent memorization |

Regularization is a fundamental concept in machine learning because it allows complex models to achieve good performance on unseen data.