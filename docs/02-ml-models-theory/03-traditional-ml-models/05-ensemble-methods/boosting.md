# Boosting

## TL;DR (30 seconds)

**Boosting** is an **ensemble learning** technique that builds models **sequentially**, where each new model focuses on correcting the mistakes of the previous ones.

The predictions of all models are then combined into a strong predictor. Popular boosting algorithms include **AdaBoost**, **Gradient Boosting**, **XGBoost**, **LightGBM**, and **CatBoost**.

---

## Why is Boosting useful?

Instead of training many independent models like Bagging, Boosting gradually improves performance by paying more attention to examples that are difficult to predict.

This often leads to higher predictive accuracy.

---

## How it works

1. Train an initial weak model.
2. Identify the errors it makes.
3. Train another model that focuses more on these errors.
4. Repeat this process multiple times.
5. Combine all models into a final prediction.

---

## Example

Instead of training all trees independently:

```
Training Data
      │
      ▼
    Tree 1
      │
  Mistakes
      ▼
    Tree 2
      │
  Mistakes
      ▼
    Tree 3
      │
      ▼
Weighted Combination
``` 

---

## Advantages

- Often achieves very high predictive performance
- Learns from previous mistakes
- Works well on structured (tabular) data
- State-of-the-art methods like XGBoost are based on boosting

---

## Disadvantages

- More prone to overfitting than Bagging
- Training is sequential and therefore slower
- Requires more careful hyperparameter tuning

---

## Bagging vs. Boosting

| Bagging | Boosting |
|---------|----------|
| Models are trained independently | Models are trained sequentially |
| Reduces variance | Reduces bias (and often variance) |
| Models have equal importance | Models contribute with different weights |
| Easy to parallelize | Difficult to parallelize |
| Example: Random Forest | Examples: AdaBoost, XGBoost, LightGBM |

---

## Related Topics

- Bagging
- Decision Trees
- Random Forests
- Gradient Boosting
- XGBoost
- Ensemble Learning