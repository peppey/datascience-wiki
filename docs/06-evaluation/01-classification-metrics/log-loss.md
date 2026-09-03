# Log Loss

## TL;DR (30 seconds)

**Log Loss** is a classification metric that evaluates the **quality of predicted probabilities**, not just the final class predictions.

For binary classification:

$$
LogLoss =
-\frac{1}{n}
\sum_{i=1}^{n}
\left[
y_i\log(p_i)
+
(1-y_i)\log(1-p_i)
\right]
$$

where:

* $y_i$ = actual class (`0` or `1`)
* $p_i$ = predicted probability for class `1`
* $n$ = number of observations

**Lower Log Loss is better.**

---

## Interpretation

Log Loss rewards predictions that assign **high probability to the correct class** and strongly penalizes confident incorrect predictions.

For an actual positive sample:

```text
Predicted probability
p = 0.99  → very small loss ✓
p = 0.70  → moderate loss
p = 0.01  → very large loss  ✗
```

A prediction of `0.01` for an actual positive is much worse than a prediction of `0.40`, because the model was **very confident and wrong**.

---

## Log Loss vs. Accuracy

Accuracy only considers whether the final class prediction is correct.

Log Loss also considers the **confidence of the prediction**.

```text
Actual class: 1

Model A: P(1) = 0.51
Model B: P(1) = 0.99

Both → correct prediction

Log Loss:
Model B → much lower loss
```

Therefore, Log Loss is particularly useful when **well-calibrated probabilities** are important.

---

## Multiclass Classification

For multiclass classification, Log Loss considers the predicted probability of the **correct class**:

$$
LogLoss =
-\frac{1}{n}
\sum_{i=1}^{n}\log(p_{i,c_i})
$$

where $p_{i,c_i}$ is the probability assigned to the true class.

---

## Python

With scikit-learn:

```python
from sklearn.metrics import log_loss

loss = log_loss(y_test, y_pred_proba)
```

`y_pred_proba` should contain the **predicted probabilities**, not the predicted class labels.

---

## Key Takeaways

1. **Log Loss evaluates predicted probabilities.**
2. **Lower Log Loss is better.**
3. Confident incorrect predictions are **strongly penalized**.
4. Unlike accuracy, Log Loss considers the **confidence** of predictions.
5. It is useful when **probability quality and calibration** matter.
6. Log Loss is also known as **cross-entropy loss** or **logarithmic loss** in this context.
