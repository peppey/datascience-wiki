# Mean Imputation

## TL;DR

**Mean Imputation** replaces missing values with the average value of the observed data.

---

## Idea

For a feature:
[10, 12, ?, 14, 16]

the mean of the available values is calculated:
(10 + 12 + 14 + 16) / 4 = 13

The missing value is replaced:
[10, 12, 13, 14, 16]

---

## Advantages

- Simple and fast
- Easy to implement
- Works well for few missing values

---

## Disadvantages

- Reduces variance
- Can distort correlations
- Sensitive to outliers

---

## Python

```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="mean")

X_imputed = imputer.fit_transform(X)
```

## Use When

Use mean imputation as a simple baseline when missing values are limited and the feature distribution is not heavily skewed.
