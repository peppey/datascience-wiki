## Motivation

A model can memorize the training data (**overfitting**). The test set shows whether the model also works on unseen data.

---

## Train-Validation-Test Split

Often, an additional validation set is used:

```text
Dataset
│
├── Training Set (70%)
│
├── Validation Set (15%)
│
└── Test Set (15%)
```

- **Training:** Learn the model parameters
- **Validation:** Select hyperparameters
- **Test:** Final evaluation

---

## Important Points

- Test data must not be used during training.
- For classification tasks, a **stratified split** can preserve the class distribution.
- For time series, data should be split chronologically (**past → future**).
- **Data leakage** must be avoided.

---

## Example

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```
