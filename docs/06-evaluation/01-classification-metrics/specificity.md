# Specificity

## TL;DR (30 seconds)

**Specificity** is a classification metric that measures the proportion of **actual negative samples** that are correctly identified by the model.

$$
Specificity = \frac{TN}{TN + FP}
$$

where:

* **TN** = True Negatives
* **FP** = False Positives

---

## Interpretation

Specificity answers the question:

> **"Of all actual negative samples, how many did the model correctly identify as negative?"**

For example, if there are 100 actual negative cases and the model correctly identifies 90:

$$
Specificity = \frac{90}{100} = 0.9
$$

The model has a **specificity of 90%**.

**Higher specificity is better.**

---

## False Positives

Specificity is particularly concerned with **false positives**.

A model with low specificity incorrectly classifies many negative samples as positive.

```text
Actual Negative
      │
      ├── True Negative  ✓
      │
      └── False Positive ✗
```

High specificity is important when **false alarms are costly**.

Examples include:

* medical diagnosis
* fraud detection
* spam detection
* quality control

---

## Specificity vs. Recall

Specificity and recall focus on opposite classes:

|             | Specificity              | Recall                   |
| ----------- | ------------------------ | ------------------------ |
| Focus       | Actual negatives         | Actual positives         |
| Also called | True Negative Rate (TNR) | True Positive Rate (TPR) |
| Avoids      | False positives          | False negatives          |
| Formula     | $\frac{TN}{TN+FP}$       | $\frac{TP}{TP+FN}$       |

Specificity and recall can be adjusted by changing the **classification threshold**.

---

## Python

With scikit-learn:

```python id="n5x8k2"
from sklearn.metrics import recall_score

specificity = recall_score(
    y_test,
    y_pred,
    pos_label=0
)
```

This calculates recall for the **negative class**, which is equivalent to specificity in binary classification.

---

## Key Takeaways

1. **Specificity measures how well a model identifies negative samples.**
2. It focuses on **false positives**.
3. Specificity is also called the **True Negative Rate (TNR)**.
4. **Higher specificity is better.**
5. Specificity is often considered together with **recall (sensitivity)**.
