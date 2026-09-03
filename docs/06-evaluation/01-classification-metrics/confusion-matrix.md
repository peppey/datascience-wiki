# Confusion Matrix

## TL;DR (30 seconds)

A **confusion matrix** summarizes the predictions of a classification model by comparing **predicted classes** with the **actual classes**.

For binary classification, it consists of four outcomes:

```text
                    Predicted
                  Negative  Positive
Actual Negative      TN        FP
       Positive      FN        TP
```

* **TP (True Positive)** – correctly predicted positive
* **TN (True Negative)** – correctly predicted negative
* **FP (False Positive)** – negative incorrectly predicted as positive
* **FN (False Negative)** – positive incorrectly predicted as negative

---

## Interpretation

The confusion matrix shows **what types of errors** a classifier makes.

For example:

```text
                    Predicted
                  Negative  Positive
Actual Negative      80        10
       Positive       5        55
```

The model correctly classified:

* 80 negative samples → **TN**
* 55 positive samples → **TP**

It made:

* 10 false positive predictions → **FP**
* 5 false negative predictions → **FN**

---

## Classification Metrics

Many common classification metrics are calculated directly from the confusion matrix:

| Metric                   | Formula                                            |
| ------------------------ | -------------------------------------------------- |
| **Precision**            | $\frac{TP}{TP+FP}$                                 |
| **Recall / Sensitivity** | $\frac{TP}{TP+FN}$                                 |
| **Specificity**          | $\frac{TN}{TN+FP}$                                 |
| **Accuracy**             | $\frac{TP+TN}{TP+TN+FP+FN}$                        |
| **F1 Score**             | $2\frac{Precision \cdot Recall}{Precision+Recall}$ |

---

## Multiclass Classification

For more than two classes, the confusion matrix contains one row and one column for each class.

```text
              Predicted
              Cat  Dog  Bird
Actual Cat     8    1     1
       Dog     0    9     1
       Bird    1    0     9
```

The **diagonal** contains correct predictions, while off-diagonal values represent misclassifications.

---

## Python

With scikit-learn:

```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
```

It can also be visualized using `ConfusionMatrixDisplay`.

---

## Key Takeaways

1. A **confusion matrix** summarizes classification results.
2. It distinguishes **TP, TN, FP, and FN**.
3. Precision, recall, specificity, accuracy, and F1 can be derived from it.
4. The **diagonal represents correct predictions**.
5. Off-diagonal values represent **classification errors**.
