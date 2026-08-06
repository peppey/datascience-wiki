# Random Forest

## TL;DR (30 seconds)

A **Random Forest** is an ensemble learning method that combines many decision trees to make more accurate and robust predictions.

Each tree is trained on a different random subset of the data and features. The final prediction is obtained by aggregating the predictions of all trees.

---

## How it works

A Random Forest builds multiple decision trees instead of relying on a single one.

For each tree:

1. A **bootstrap sample** (random sample with replacement) of the training data is created.
2. At each split, only a **random subset of features** is considered.
3. The tree is grown independently of the others.

Prediction:

- **Classification:** Majority vote of all trees.
- **Regression:** Average of all tree predictions.

```text
Training Data
      │
      ├──────────────┬──────────────┬──────────────┐
      │              │              │
   Tree 1         Tree 2         Tree 3        ...
      │              │              │
      └──────────────┴──────────────┴──────────────┘
                     │
             Aggregate Predictions
                     │
              Final Prediction
```

---

## Why does it work?

Individual decision trees tend to overfit the training data.

By averaging the predictions of many diverse trees, Random Forests:

- reduce variance,
- improve generalization,
- become more robust to noise.

The random selection of both samples and features helps ensure that the trees make different errors.

---

## Important Hyperparameters

Common hyperparameters include:

- `n_estimators` – number of trees
- `max_depth` – maximum tree depth
- `max_features` – number of features considered at each split
- `min_samples_split`
- `min_samples_leaf`
- `bootstrap`

---

## Advantages

- High predictive performance
- Less prone to overfitting than a single decision tree
- Handles high-dimensional data well
- Works for classification and regression
- Provides feature importance estimates
- Requires little data preprocessing

---

## Disadvantages

- Less interpretable than a single decision tree
- Larger memory and computational requirements
- Slower inference with many trees
- Feature importance can be biased toward high-cardinality features

---

## Applications

Random Forests are commonly used for:

- Classification
- Regression
- Feature selection
- Anomaly detection
- Credit risk assessment
- Medical diagnosis

---

## Related Topics

- Decision Trees
- Bagging
- Bootstrap Sampling
- Ensemble Learning
- Feature Importance
- XGBoost
- Gradient Boosting