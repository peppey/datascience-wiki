# F1 Score

## TL;DR (30 seconds)

**F1 Score** combines **precision and recall** into a single metric using their harmonic mean.

$$
F_1 = 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}
$$

It ranges from **0 to 1**, where **1 is perfect**.

---

## Interpretation

F1 answers the question:

> **"How well does the model balance precision and recall?"**

For example:

```text
Precision = 0.8
Recall    = 0.6

F1 = 2 · (0.8 · 0.6) / (0.8 + 0.6)
   ≈ 0.69
```

The harmonic mean ensures that a very low precision or recall strongly reduces the F1 Score.

---

## Precision vs. Recall vs. F1

| Metric        | Focus                          |
| ------------- | ------------------------------ |
| **Precision** | Avoiding false positives       |
| **Recall**    | Avoiding false negatives       |
| **F1 Score**  | Balancing precision and recall |

F1 is particularly useful when **both false positives and false negatives matter** and a single metric is needed.

---

## Threshold Dependence

For probabilistic classifiers, F1 depends on the **classification threshold**.

```text
Lower threshold
      ↓
More positive predictions
      ↓
Recall ↑
Precision may ↓
      ↓
       F1
```

The threshold can therefore be tuned to maximize F1 on a validation set.

---

## Python

With scikit-learn:

```python
from sklearn.metrics import f1_score

f1 = f1_score(y_test, y_pred)
```

For multiclass classification, averaging strategies such as `macro`, `micro`, or `weighted` can be specified.

---

## Key Takeaways

1. **F1 Score combines precision and recall.**
2. It uses the **harmonic mean**, not the arithmetic mean.
3. F1 ranges from **0 to 1**.
4. A high F1 requires both **high precision and high recall**.
5. F1 is useful when **false positives and false negatives both matter**.
6. F1 depends on the chosen **classification threshold**.
