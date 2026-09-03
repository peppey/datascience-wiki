# MSE (Mean Squared Error)

## TL;DR (30 seconds)

**MSE** measures the average **squared difference** between actual and predicted values.

$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

where:

* $y_i$ = actual value
* $\hat{y}_i$ = predicted value
* $n$ = number of observations

---

## Interpretation

MSE measures the size of prediction errors, but because the errors are **squared**, large errors have a much stronger influence.

**Lower MSE is better.**

Unlike MAE and RMSE, MSE is expressed in **squared units** of the target variable.

For example, if the target is measured in euros, MSE is measured in **euros²**, which makes it less intuitive to interpret directly.

---

## MSE vs. MAE and RMSE

|                       | MSE     | MAE      | RMSE                  |
| --------------------- | ------- | -------- | --------------------- |
| Error calculation     | Squared | Absolute | Squared + square root |
| Sensitive to outliers | More    | Less     | More                  |
| Same units as target  | No      | Yes      | Yes                   |
| Lower is better       | ✓       | ✓        | ✓                     |

RMSE is simply the square root of MSE:

$$
RMSE = \sqrt{MSE}
$$

---

## Python

With scikit-learn:

```python
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
```

---

## Key Takeaways

1. **MSE measures the average squared prediction error.**
2. **Lower MSE is better.**
3. Squaring errors makes MSE particularly sensitive to **large errors and outliers**.
4. MSE is expressed in **squared units**, making RMSE easier to interpret.
5. **RMSE is the square root of MSE.**
