# R² (Coefficient of Determination)

## TL;DR (30 seconds)

**R² (R-squared)** is a regression metric that measures how much of the variance in the target variable is explained by the model.

$$
R^2 = 1 - \frac{\sum_i (y_i-\hat{y}_i)^2}
{\sum_i (y_i-\bar{y})^2}
$$

where:

* $y_i$ = actual value
* $\hat{y}_i$ = predicted value
* $\bar{y}$ = mean of the actual values

---

## Interpretation

R² compares the model against a simple baseline that always predicts the **mean** of the target.

|    R² | Interpretation                          |
| ----: | --------------------------------------- |
|   `1` | Perfect predictions                     |
|   `0` | No improvement over predicting the mean |
| `< 0` | Worse than predicting the mean          |

For example, an **R² of 0.8** means that the model explains about **80% of the variance** in the target relative to the mean baseline.

---

## Important Caveat

R² does **not** directly measure the size of prediction errors.

A model can have a high R² while still making practically large errors, depending on the scale and distribution of the target.

Therefore, R² is often used together with metrics such as:

* **MAE** – Mean Absolute Error
* **MSE** – Mean Squared Error
* **RMSE** – Root Mean Squared Error

---

## Python

With scikit-learn:

```python
from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
```

R² can be used for both **model evaluation** and **comparing regression models** on the same dataset.

---

## Adjusted R²

**Adjusted R²** extends R² by taking the **number of predictors** in the model into account.

Adding more features can only increase or leave unchanged the ordinary R², even if those features provide little useful information. Adjusted R² penalizes this complexity.

$$
R^2_{\text{adj}}
=
1-(1-R^2)\frac{n-1}{n-p-1}
$$

where:

* $n$ = number of observations
* $p$ = number of predictors

Unlike ordinary R², **Adjusted R² can decrease when an additional feature does not sufficiently improve the model**.

It is therefore useful when comparing regression models with **different numbers of predictors**.

```text
More predictors
      │
      ▼
    R² ↑ or =
      │
      ▼
Adjusted R²
      │
      ├── useful feature → may increase
      └── unnecessary feature → may decrease
```

**Note:** Adjusted R² is mainly useful for comparing models fitted to the same target and dataset. It does not replace error-based metrics such as MAE or RMSE.


## Key Takeaways

1. **R² measures explained variance** in a regression model.
2. `R² = 1` indicates perfect predictions.
3. `R² = 0` means the model performs like the mean baseline.
4. R² can be **negative**.
5. R² does not directly tell you how large the prediction errors are.
6. Use R² together with **MAE or RMSE** when evaluating regression models.
