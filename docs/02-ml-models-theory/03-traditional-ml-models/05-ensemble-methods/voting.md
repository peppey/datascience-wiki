# Voting

## TL;DR (30 seconds)

**Voting** is an **ensemble learning** technique that combines the predictions of multiple models by using a voting strategy.

The idea is that several different models can make better decisions together than a single model alone.

There are two common approaches:

- **Hard Voting**: Choose the prediction with the most votes.
- **Soft Voting**: Combine predicted probabilities from all models.

---

## Why is Voting useful?

Different models often make different mistakes.

By combining several models, Voting can reduce the impact of individual errors and create a more robust predictor.

For example:

- A Decision Tree may capture simple rules.
- A Support Vector Machine may find good decision boundaries.
- A Neural Network may detect complex patterns.

Together, they can produce a stronger prediction.

---

## How it works

### Hard Voting

Each model gives a class prediction.

The class with the most votes becomes the final prediction.

```text
              Input Data
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
Decision Tree     SVM    Neural Network
      │           │           │
      ▼           ▼           ▼
   Class A     Class B     Class A
      │           │           │
      └───────────┼───────────┘
                  ▼
            Majority Vote
                  │
                  ▼
               Class A
```

Example:
Model 1: Cat
Model 2: Dog
Model 3: Cat
Final prediction: Cat


---

### Soft Voting

Instead of only using the predicted class, models provide probabilities.

The probabilities are averaged, and the class with the highest combined probability is selected.

Example:

Random Forest:
- Cat: 0.7
- Dog: 0.3

SVM:
- Cat: 0.6
- Dog: 0.4

Neural Network:
- Cat: 0.8
- Dog: 0.2


Average:
- Cat: 0.7
- Dog: 0.3

Final prediction:
Cat

---

## Weighted Voting

Some models may perform better than others.

In weighted voting, models receive different importance weights.

Example:
- Random Forest weight: 0.5
- XGBoost weight: 0.3
- Logistic Regression weight: 0.2

The final prediction is based on the weighted combination of all models.

---

## Example

Suppose we classify whether an email is spam:

| Model | Prediction |
|-------|------------|
| Random Forest | Spam |
| SVM | Not Spam |
| Neural Network | Spam |

Using hard voting:
Spam: 2 votes
Not Spam: 1 vote
Final prediction: Spam


---

## Advantages

- Simple and easy to implement
- Reduces model-specific errors
- Works well when models are diverse
- Can improve robustness compared to a single model

---

## Disadvantages

- Requires multiple models
- Performance depends on model diversity
- Does not learn how models should be combined
- Some models may add little value

---

## Voting vs. Stacking

| Voting | Stacking |
|--------|----------|
| Uses fixed combination rules | Learns how to combine models |
| No additional model needed | Requires a meta-model |
| Simpler and faster | More complex |
| Models usually have equal influence | Models can receive learned importance |
| Example: Random Forest + SVM + NN majority vote | Example: RF + XGBoost → Logistic Regression |

---

## Voting vs. Bagging vs. Boosting

| Bagging | Boosting | Voting |
|---------|----------|--------|
| Same type of models trained independently | Models trained sequentially | Combines different model predictions |
| Reduces variance | Reduces bias and variance | Improves robustness |
| Example: Random Forest | Example: XGBoost | Example: RF + SVM + NN |

---

## Related Topics

- Ensemble Learning
- Bagging
- Boosting
- Stacking
- Random Forests
- Model Calibration
- Cross-Validation
