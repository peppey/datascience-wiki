# Cross-Validation

## TL;DR

**Cross-Validation** evaluates a model by repeatedly splitting the data into training and validation sets.

In **k-fold cross-validation**, the data is divided into $k$ folds. Each fold is used once for validation.

```text
Fold 1: [Validation] [Train] [Train] [Train] [Train]
Fold 2: [Train] [Validation] [Train] [Train] [Train]
Fold 3: [Train] [Train] [Validation] [Train] [Train]
...
```

The final score is usually the mean of the validation scores.

---

## Stratified Cross-Validation

For classification, **Stratified K-Fold** preserves the class proportions in each fold.

This is particularly useful for imbalanced datasets.

---

## Time Series Cross-Validation

Standard random splitting must generally **not** be used for time series because it can cause information from the future to leak into the training data.

Instead, the training set grows over time:

```text
Train → Test
Train → Train → Test
Train → Train → Train → Test
```

This is often called **walk-forward** or **expanding-window validation**.

---

## Other Variants

Common variants include:

* **Leave-One-Out (LOOCV)** — one observation is used for validation at a time.
* **Group K-Fold** — observations from the same group remain in the same fold.
* **Stratified K-Fold** — preserves class proportions.
* **Time Series Split** — respects temporal ordering.

---

## Key Idea

Cross-validation estimates how well a model generalizes to unseen data.

$$
\boxed{
\text{Train}
\rightarrow
\text{Validate}
\rightarrow
\text{Repeat}
\rightarrow
\text{Average Score}
}
$$

The splitting strategy must match the structure of the data to avoid **data leakage**.
