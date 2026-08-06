# Bagging (Bootstrap Aggregating)

## TL;DR (30 seconds)

**Bagging** is an **ensemble learning** technique that improves model stability and reduces overfitting by training multiple models on different random subsets of the training data and combining their predictions.

It is most commonly used with **Decision Trees**, resulting in the **Random Forest** algorithm.

---

## Why is Bagging useful?

A single model, especially a decision tree, can be sensitive to small changes in the training data.

Bagging reduces this variance by averaging the predictions of many independently trained models.

---

## How it works

1. Draw multiple **bootstrap samples** (random samples with replacement) from the training data.
2. Train one model on each sample.
3. Combine their predictions:
   - **Classification:** Majority vote
   - **Regression:** Average prediction

---

## Example

Instead of training one decision tree:

```
Training Data
      │
      ▼
Decision Tree
      │
Prediction
```

Bagging trains many trees:

```
Training Data
      │
 ┌────┼────┐
 ▼    ▼    ▼
Tree Tree Tree ...
 │    │    │
 └────┼────┘
      ▼
Average / Majority Vote
```

---

## Advantages

- Reduces overfitting
- Improves robustness
- Works well with unstable models (e.g. Decision Trees)
- Easy to parallelize

---

## Disadvantages

- Higher computational cost
- Less interpretable than a single model
- Little benefit for already stable models (e.g. Linear Regression)

---

## Related Topics

- Bootstrap Sampling
- Decision Trees
- Random Forests
- Ensemble Learning
- Boosting