# KNN Imputation

## TL;DR

**KNN Imputation** replaces missing values by looking at similar data points (**neighbors**) and using their values to estimate the missing entry.

It is a more flexible alternative to simple methods like mean or median imputation because it considers relationships between features.

---

## Idea

For a data point with a missing value:

1. Find the **k most similar samples** in the dataset.
2. Use the values of these neighbors to estimate the missing value.
3. Replace the missing value with the estimated value.

Similarity is usually measured using a distance metric such as **Euclidean distance**.

---

## Example

Given a dataset:

| Age | Income | Missing Feature |
|---|---|---|
| 25 | 40000 | 5 |
| 30 | 50000 | ? |
| 27 | 45000 | 6 |
| 29 | 48000 | 5 |

For the missing value, KNN looks for rows with similar `Age` and `Income`.

If the nearest neighbors have values:
5, 6, 5

the missing value might be replaced by:
(5 + 6 + 5) / 3 = 5.33

---

## Advantages

- Captures relationships between features
- Works well when missingness depends on similar samples
- Does not assume a specific data distribution

---

## Disadvantages

- Computationally expensive for large datasets
- Sensitive to feature scaling
- Choice of `k` affects results

---

## Feature Scaling

Because KNN uses distances, features should usually be normalized:

Example:
Age: 20 - 80
Income: 20000 - 200000

Without scaling, income would dominate the distance calculation.

---

## Python Example

Using `scikit-learn`:

```python
from sklearn.impute import KNNImputer

imputer = KNNImputer(
    n_neighbors=5
)

X_imputed = imputer.fit_transform(X)
When to Use KNN Imputation
KNN Imputation is useful when:
the dataset is small or medium-sized
features are correlated
missing values cannot simply be replaced by averages
For very large datasets, simpler methods or model-based imputation are often preferred.
```

## When to Use KNN Imputation

KNN Imputation is useful when:
- the dataset is small or medium-sized
- features are correlated
- missing values cannot simply be replaced by averages

For very large datasets, simpler methods or model-based imputation are often preferred.
