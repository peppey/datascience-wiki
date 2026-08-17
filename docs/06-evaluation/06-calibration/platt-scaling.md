# Platt Scaling

## TL;DR

**Platt Scaling** is a method for **calibrating the scores of a classification model**.

A model may produce scores that are useful for ranking predictions but do not represent well-calibrated probabilities.

Platt Scaling learns a logistic transformation:

$$
\boxed{
P(y=1\mid x)
=

\sigma(Af(x)+B)
}
$$

where:

* $f(x)$ is the original model score
* $A$ and $B$ are learned parameters
* $\sigma$ is the sigmoid function

The result is a probability estimate that is typically better calibrated.

---

## Why Calibration?

A classifier might output:

```text
Prediction: class 1
Score:      0.9
```

A score of `0.9` does not necessarily mean that approximately 90% of such predictions are correct.

A **calibrated** classifier should satisfy:

> Among predictions with probability 0.9, approximately 90% should be correct.

Calibration is therefore different from classification accuracy.

```text
Accuracy
→ Are the predictions correct?

Calibration
→ Do the predicted probabilities reflect actual frequencies?
```

---

## Original Model Score

Suppose a binary classifier produces a score:

$$
f(x)
$$

The score could be:

* a decision function
* a margin
* a logit
* another model-specific confidence score

Platt Scaling transforms this score into a probability.

```text
Model
  │
  ▼
Score f(x)
  │
  ▼
Platt Scaling
  │
  ▼
Calibrated Probability
```

---

## Logistic Transformation

Platt Scaling fits a logistic regression model on the original model scores:

$$
P(y=1\mid x)
=

\frac{1}{1+\exp(-(Af(x)+B))}
$$

The parameters $A$ and $B$ are learned from a separate calibration dataset.

```text
Original Score
      │
      ▼
  Af(x) + B
      │
      ▼
   Sigmoid
      │
      ▼
Probability
```

---

## Example

Suppose a classifier produces the following scores:

| Sample | Model Score | True Class |
| ------ | ----------: | ---------: |
| A      |         2.1 |          1 |
| B      |         1.4 |          1 |
| C      |         0.2 |          0 |
| D      |        -1.3 |          0 |

Platt Scaling learns $A$ and $B$ from such examples.

After calibration, a score might become:

$$
f(x)=1.4
\quad\rightarrow\quad
P(y=1\mid x)=0.87
$$

The calibrated value can then be interpreted as a probability estimate.

---

## Calibration Dataset

The parameters should generally be learned on data **separate from the data used to train the original model**.

```text
Training Data
      │
      ▼
Original Model
      │
      ▼
Calibration Data
      │
      ▼
Platt Scaling
```

Using the same data for both steps can lead to overfitting and overly optimistic calibration.

Cross-validation can be used when the available dataset is limited.

---

## Calibration vs. Classification

Calibration does not necessarily change the predicted class.

For example:

```text
Before:
score = 0.95 → class 1

After:
probability = 0.82 → class 1
```

The ranking or classification decisions may remain similar while the confidence estimates become more meaningful.

Therefore:

$$
\boxed{
\text{Calibration}
\neq
\text{Improving Classification Accuracy}
}
$$

---

## Binary Classification

Classic Platt Scaling is primarily designed for **binary classification**.

For a binary classifier:

$$
y\in{0,1}
$$

the calibrated probability is:

$$
P(y=1\mid x)
=
\sigma(Af(x)+B)
$$

For multiclass classification, additional calibration strategies are required, such as one-vs-rest calibration or other multiclass calibration methods.

---

## Key Idea

Platt Scaling converts an arbitrary classification score into a calibrated probability using a learned sigmoid transformation.

$$
\boxed{
\text{Model Score}
\rightarrow
\text{Sigmoid Transformation}
\rightarrow
\text{Calibrated Probability}
}
$$

It is especially useful when a model's **confidence scores should have a probabilistic interpretation**.
