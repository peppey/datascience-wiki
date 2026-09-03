# XGBoost

## TL;DR (30 seconds)

**XGBoost (Extreme Gradient Boosting)** is a gradient boosting algorithm that combines many **decision trees sequentially** to build a strong predictive model.

```text
Training data
     │
     ▼
 Tree 1 ──► errors
              │
              ▼
           Tree 2 ──► remaining errors
                       │
                       ▼
                    Tree 3
                       │
                       ▼
                  Final prediction
```

Unlike **Random Forest**, where trees are trained independently, XGBoost trains trees **sequentially**, with each new tree improving the previous model.

---

## 1. Gradient Boosting

The model is built iteratively:

$$
F_m(x) = F_{m-1}(x) + \eta h_m(x)
$$

where:

* $F_m$ is the model after iteration $m$
* $h_m$ is the new decision tree
* $\eta$ is the **learning rate**

Each tree is trained to reduce the current model's errors.

---

## 2. Important Parameters

| Parameter          | Meaning                            |
| ------------------ | ---------------------------------- |
| `n_estimators`     | Number of boosting rounds / trees  |
| `max_depth`        | Maximum tree depth                 |
| `learning_rate`    | Contribution of each tree          |
| `subsample`        | Fraction of samples used per tree  |
| `colsample_bytree` | Fraction of features used per tree |
| `reg_alpha`        | L1 regularization                  |
| `reg_lambda`       | L2 regularization                  |

A smaller `learning_rate` often requires more trees.

---

## 3. XGBoost vs Random Forest

|                     | Random Forest                | XGBoost                         |
| ------------------- | ---------------------------- | ------------------------------- |
| Training            | Parallel / independent trees | Sequential trees                |
| Main idea           | Reduce variance              | Reduce errors iteratively       |
| Randomization       | Strong                       | Optional subsampling            |
| Typical strength    | Robust baseline              | High predictive performance     |
| Overfitting control | Mainly averaging             | Regularization + early stopping |

Both methods work particularly well for **tabular data**.

---

## 4. Regularization

XGBoost includes several mechanisms to reduce overfitting:

* tree-depth restrictions
* learning rate
* row and feature subsampling
* L1/L2 regularization
* minimum split requirements
* **early stopping**

Early stopping stops training when performance on a validation set no longer improves.

---

## 5. Classification

XGBoost can be used for binary and multiclass classification.

```python
from xgboost import XGBClassifier

model = XGBClassifier(
    n_estimators=300,
    max_depth=6,
    learning_rate=0.05
)

model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

---

## 6. Regression

For regression, `XGBRegressor` can be used:

```python
from xgboost import XGBRegressor

model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=6
)

model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

---

## 7. Advantages and Disadvantages

| Advantages                             | Disadvantages                                    |
| -------------------------------------- | ------------------------------------------------ |
| Excellent performance on tabular data  | More hyperparameters than Random Forest          |
| Handles nonlinear relationships        | Can overfit without regularization               |
| Supports feature and row subsampling   | Less interpretable than a single tree            |
| Built-in regularization                | Sequential training can be harder to parallelize |
| Supports classification and regression | Usually requires hyperparameter tuning           |

---

## Key Takeaways

1. **XGBoost is a gradient boosting algorithm based on decision trees.**
2. Trees are trained **sequentially**, each improving the previous model.
3. The **learning rate** controls the contribution of each tree.
4. XGBoost provides several forms of **regularization**.
5. **Early stopping** can prevent unnecessary boosting rounds.
6. XGBoost is particularly strong for **structured/tabular data**.
7. Compared with Random Forest, XGBoost focuses on **iteratively correcting errors rather than independently averaging trees**.
