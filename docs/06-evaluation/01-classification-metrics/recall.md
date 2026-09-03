# Recall

## TL;DR (30 seconds)

**Recall** is a classification metric that measures the proportion of actual positive samples that are correctly identified by the model.

$$
Recall = \frac{TP}{TP + FN}
$$

where:

* **TP** = True Positives
* **FN** = False Negatives

---

## Interpretation

Recall answers the question:

> **"Of all actual positive samples, how many did the model find?"**

For example, if there are 100 actual positive cases and the model correctly identifies 80:

$$
Recall = \frac{80}{100} = 0.8
$$

The model has a **recall of 80%**.

**Higher recall is better.**

---

## False Negatives

Recall is particularly concerned with **false negatives**.

A model with low recall misses many positive cases.

```text id="q3j8fd"
Actual Positive
      │
      ├── True Positive  ✓
      │
      └── False Negative ✗
```

High recall is important when **missing a positive case is costly**.

Examples include:

* disease detection
* fraud detection
* safety-critical systems
* detecting relevant documents

---

## Recall vs. Precision

|          | Recall                                | Precision                                 |
| -------- | ------------------------------------- | ----------------------------------------- |
| Focus    | False negatives                       | False positives                           |
| Question | How many actual positives were found? | How many predicted positives are correct? |
| Formula  | $\frac{TP}{TP+FN}$                    | $\frac{TP}{TP+FP}$                        |

There is often a **trade-off between precision and recall**. Changing the classification threshold can increase one while decreasing the other.

---

## Python

With scikit-learn:

```python id="z8jv2k"
from sklearn.metrics import recall_score

recall = recall_score(y_test, y_pred)
```

For multiclass classification, averaging strategies such as `macro`, `micro`, or `weighted` can be specified.

---

## Key Takeaways

1. **Recall measures how many actual positives are detected.**
2. It focuses on **false negatives**.
3. **Higher recall is better.**
4. Recall is important when missing positive cases is costly.
5. Recall should often be considered together with **precision**.
