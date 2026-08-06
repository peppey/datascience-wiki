# Accuracy

## TL;DR

**Accuracy** measures the percentage of correct predictions made by a classification model.

$$
\text{Accuracy} =
\frac{\text{Correct Predictions}}
{\text{Total Predictions}}
$$

---

## Definition

Using the confusion matrix:

$$
\text{Accuracy} =
\frac{TP+TN}{TP+TN+FP+FN}
$$

where:

- $TP$ = True Positives
- $TN$ = True Negatives
- $FP$ = False Positives
- $FN$ = False Negatives

---

## Example

A model predicts 100 samples:

- 90 predictions are correct
- 10 predictions are wrong

Therefore:

$$
\text{Accuracy}=0.9=90\%
$$

---

## Limitation

Accuracy can be misleading for **imbalanced datasets**.

Example:

If 99% of samples belong to one class, a model predicting only that class achieves 99% accuracy but may be useless.

For imbalanced problems, metrics like **precision**, **recall**, or **F1-score** are often better.

---

## Summary

- Accuracy = fraction of correct predictions.
- Simple and intuitive.
- Best for balanced classification problems.