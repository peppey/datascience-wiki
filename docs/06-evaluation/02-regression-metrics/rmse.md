# RMSE (Root Mean Squared Error)

## TL;DR (30 seconds)

**RMSE** measures the typical size of prediction errors in a regression model. It is the square root of the **Mean Squared Error (MSE)**.

$$
RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
$$

where:

* $y_i$ = actual value
* $\hat{y}_i$ = predicted value
* $n$ = number of observations

---

## Interpretation

RMSE is expressed in the **same units as the target variable**.

For example, if a model predicts house prices in euros and has an RMSE of €20,000, its typical prediction error is roughly on the order of €20,000.

**Lower RMSE is better.**

Because the errors are squared, **large errors have a stronger influence** on RMSE than small errors.

---

## RMSE vs. MAE

Both metrics measure prediction errors, but they treat large errors differently:

|                       | RMSE           | MAE            |
| --------------------- | -------------- | -------------- |
| Error calculation     | Squared        | Absolute       |
| Sensitive to outliers | More           | Less           |
| Units                 | Same as target | Same as target |
| Lower is better       | ✓              | ✓              |

RMSE is useful when **large prediction errors should be penalized more strongly**.

---

## Python

With scikit-learn:

```python
from sklearn.metrics import root_mean_squared_error

rmse = root_mean_squared_error(y_test, y_pred)
```

For older scikit-learn versions, RMSE can also be calculated using:

```python
from sklearn.metrics import mean_squared_error

rmse = mean_squared_error(y_test, y_pred) ** 0.5
```

---

## Key Takeaways

1. **RMSE measures the size of regression errors.**
2. It is expressed in the **same units as the target**.
3. **Lower RMSE is better.**
4. Squaring the errors makes RMSE more sensitive to **large errors and outliers**.
5. RMSE is often used together with **MAE and R²**.
