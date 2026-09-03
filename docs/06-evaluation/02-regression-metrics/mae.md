# MAE (Mean Absolute Error)

## TL;DR (30 seconds)

**MAE** measures the average absolute difference between the actual and predicted values.

$$
MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
$$

where:

* $y_i$ = actual value
* $\hat{y}_i$ = predicted value
* $n$ = number of observations

---

## Interpretation

MAE is expressed in the **same units as the target variable**.

For example, an MAE of **€10,000** for a house-price model means that the predictions are off by **€10,000 on average**.

**Lower MAE is better.**

---

## MAE vs. RMSE

The main difference is how the metrics treat large errors:

|                       | MAE            | RMSE           |
| --------------------- | -------------- | -------------- |
| Error calculation     | Absolute       | Squared        |
| Sensitive to outliers | Less           | More           |
| Units                 | Same as target | Same as target |
| Lower is better       | ✓              | ✓              |

MAE is often preferred when **all errors should be treated more equally** and large errors should not dominate the metric.

---

## Python

With scikit-learn:

```python
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, y_pred)
```

---

## Key Takeaways

1. **MAE measures the average prediction error.**
2. It is expressed in the **same units as the target**.
3. **Lower MAE is better.**
4. MAE is **less sensitive to outliers** than RMSE.
5. MAE is useful when prediction errors should be treated relatively equally.
