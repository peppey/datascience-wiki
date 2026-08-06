# Stacking

## TL;DR (30 seconds)

**Stacking** (auch **Stacked Generalization**) is an **ensemble learning** technique that combines multiple different models by training a second model to learn how to combine their predictions.

Instead of manually averaging models, Stacking uses a **meta-model** that learns which base models are reliable for different types of inputs.

---

## Why is Stacking useful?

Different models often have different strengths and weaknesses.

For example:

- A **Random Forest** may capture complex patterns in tabular data.
- A **Linear Model** may generalize well on simple relationships.
- A **Neural Network** may learn nonlinear structures.

Stacking combines these complementary strengths to create a stronger overall model.

---

## How it works

Stacking consists of multiple layers:

1. Train several different base models on the training data.
2. Generate predictions from each model.
3. Use these predictions as new features.
4. Train a meta-model that learns how to combine these predictions.
5. Use the meta-model for the final prediction.


```text
              Training Data
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
 Random Forest   XGBoost   Neural Network
       │           │           │
       ▼           ▼           ▼
 Prediction    Prediction   Prediction
       │           │           │
       └───────────┼───────────┘
                   ▼
              Meta Model
                   │
                   ▼
          Final Prediction
```

## Example

Suppose we want to predict house prices:

- A Random Forest predicts: **450,000 €**
- An XGBoost model predicts: **470,000 €**
- A Linear Regression predicts: **430,000 €**

Instead of simply averaging:
(450k + 470k + 430k) / 3 = 450k

a meta-model learns that:

- XGBoost might perform better for large houses
- Linear Regression might work better for simple cases
- Random Forest might handle unusual cases better

and combines the predictions accordingly.

---

## Training the meta-model

To avoid overfitting, the meta-model is usually trained on **out-of-fold predictions**:

1. Split the training data using cross-validation.
2. Train base models on parts of the data.
3. Generate predictions for unseen validation parts.
4. Use these predictions to train the meta-model.

This prevents the meta-model from simply memorizing the training data.

---

## Advantages

- Combines strengths of different algorithms
- Often improves predictive performance
- Can work with very different types of models
- More flexible than simple averaging or voting

---

## Disadvantages

- More complex pipeline
- Requires training multiple models
- Higher computational cost
- Risk of overfitting if the meta-model is not carefully trained

---

## Stacking vs. Bagging vs. Boosting

| Bagging | Boosting | Stacking |
|---------|----------|----------|
| Models trained independently | Models trained sequentially | Models trained in layers |
| Reduces variance | Reduces bias and variance | Learns optimal combination |
| Usually same model type | Usually same model type | Often different model types |
| Example: Random Forest | Example: XGBoost | Example: Random Forest + XGBoost + Logistic Regression |

---

## Related Topics

- Ensemble Learning
- Bagging
- Boosting
- Random Forests
- Gradient Boosting
- Cross-Validation
- Model Calibration
