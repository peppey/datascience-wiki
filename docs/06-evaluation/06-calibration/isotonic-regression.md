# Isotonic Regression

## TL;DR

**Isotonic Regression** is a non-parametric method that can be used to **calibrate the scores of a classification model**.

It learns a monotonic function that maps model scores to probabilities:

$$
P(y=1\mid x)=g(f(x))
$$

where $f(x)$ is the original model score and $g$ is a monotonically increasing function.

Unlike Platt Scaling, Isotonic Regression does not assume that the relationship is sigmoid-shaped.

---

## Calibration

A classifier may produce scores that do not correspond well to actual probabilities.

For example:

```text
Model Score
    │
    ▼
0.2 → 0.10
0.4 → 0.30
0.6 → 0.55
0.8 → 0.85
```

The calibration model learns this mapping from a separate calibration dataset.

```text
Model
  │
  ▼
Score
  │
  ▼
Isotonic Regression
  │
  ▼
Calibrated Probability
```

---

## Monotonicity

The main assumption is that higher model scores should not result in lower probabilities.

For scores

$$
f_1 < f_2 < \dots < f_n
$$

the calibrated probabilities must satisfy

$$
g(f_1)\leq g(f_2)\leq\dots\leq g(f_n).
$$

The function does not need to be linear or sigmoid-shaped.

---

## Fitting the Model

Given model scores $f_i$ and binary labels $y_i$, Isotonic Regression finds a monotonic function that minimizes the squared error:

$$
\min_g
\sum_{i=1}^{n}
(y_i-g(f_i))^2
$$

subject to:

$$
f_i < f_j
\Rightarrow
g(f_i)\leq g(f_j).
$$

The resulting function is typically piecewise constant.

---

## Example

Suppose a model produces:

| Score | Label |
| ----: | ----: |
|   0.1 |     0 |
|   0.2 |     0 |
|   0.3 |     1 |
|   0.4 |     0 |
|   0.5 |     1 |
|   0.6 |     1 |
|   0.8 |     1 |

Isotonic Regression finds a monotonic mapping from these scores to probabilities.

Conceptually:

```text
Score
 │
 ├── 0.1 → 0.0
 ├── 0.2 → 0.0
 ├── 0.3 → 0.3
 ├── 0.4 → 0.3
 ├── 0.5 → 0.7
 ├── 0.6 → 0.7
 └── 0.8 → 1.0
```

The mapping is constrained to never decrease.

---

## Calibration Data

The calibration function should generally be learned using data that was **not used to train the original model**.

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
Isotonic Regression
```

Using the training data directly can lead to overfitting.

---

## Isotonic Regression vs. Platt Scaling

Both methods can calibrate classification scores.

|                  | Platt Scaling                | Isotonic Regression         |
| ---------------- | ---------------------------- | --------------------------- |
| Function         | Sigmoid                      | Monotonic                   |
| Assumption       | Sigmoid relationship         | Only monotonic relationship |
| Flexibility      | Lower                        | Higher                      |
| Overfitting risk | Lower                        | Higher                      |
| Typical use      | Smaller calibration datasets | Larger calibration datasets |

Platt Scaling assumes:

$$
P(y=1\mid x)=\sigma(Af(x)+B)
$$

while Isotonic Regression learns:

$$
P(y=1\mid x)=g(f(x)).
$$

---

## Key Idea

Isotonic Regression calibrates model scores by learning a **monotonically increasing mapping** from scores to probabilities.

$$
\boxed{
\text{Model Score}
\rightarrow
\text{Monotonic Mapping}
\rightarrow
\text{Calibrated Probability}
}
$$

Its main advantage over Platt Scaling is its **flexibility**. Its main disadvantage is that this flexibility can lead to **overfitting when little calibration data is available**.
