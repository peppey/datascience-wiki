# Precision

## TL;DR (30 seconds)

**Precision** is a classification metric that measures the proportion of predicted positive samples that are actually positive.

$$
Precision = \frac{TP}{TP + FP}
$$

where:

* **TP** = True Positives
* **FP** = False Positives

---

## Interpretation

Precision answers the question:

> **"Of all samples predicted as positive, how many are actually positive?"**

For example, if a model identifies 100 emails as spam and 80 of them are actually spam:

$$
Precision = \frac{80}{100} = 0.8
$$

The model has a **precision of 80%**.

**Higher precision is better.**

---

## False Positives

Precision is particularly concerned with **false positives**.

A model with low precision produces many positive predictions that are actually negative.

```text
Predicted Positive
       │
       ├── True Positive  ✓
       │
       └── False Positive ✗
```

High precision is important when **false positives are costly**.

Examples include:

* spam detection
* fraud detection
* medical screening
* information retrieval

---

## Precision vs. Recall

Precision and recall focus on different aspects of classification:

|          | Precision                                 | Recall                                |
| -------- | ----------------------------------------- | ------------------------------------- |
| Focus    | False positives                           | False negatives                       |
| Question | How many predicted positives are correct? | How many actual positives were found? |
| Formula  | $\frac{TP}{TP+FP}$                        | $\frac{TP}{TP+FN}$                    |

Increasing precision can sometimes reduce recall, and vice versa. The appropriate balance depends on the application.

---

## Python

With scikit-learn:

```python
from sklearn.metrics import precision_score

precision = precision_score(y_test, y_pred)
```

For multiclass classification, averaging strategies such as `macro`, `micro`, or `weighted` can be specified.

---

## Key Takeaways

1. **Precision measures the correctness of positive predictions.**
2. It focuses on **false positives**.
3. **Higher precision is better.**
4. Precision is especially important when false positives are costly.
5. Precision should often be considered together with **recall**.
