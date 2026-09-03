# k-Nearest Neighbors (k-NN)

## TL;DR (30 seconds)

**k-Nearest Neighbors (k-NN)** is a supervised learning algorithm that makes predictions based on the **k most similar training samples**.

```text
             Query point
                  ●
              ↙   ↓   ↘
           ●     ●     ●
         nearest neighbors
                  │
                  ▼
             Prediction
```

---

## Basic Idea

For a new data point, k-NN:

1. Calculates the distance to all training points.
2. Selects the **k nearest neighbors**.
3. Uses their labels to make a prediction.

For classification, the most common class among the neighbors is selected.

For regression, the neighbors' values are typically averaged.

---

## Distance

A common distance measure is **Euclidean distance**:

$$
d(x,y) = \sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}
$$

Other distance measures can also be used, such as:

* Manhattan distance
* Cosine distance
* Minkowski distance

The choice of distance measure depends on the data.

---

## Choosing k

The parameter **k** determines how many neighbors are considered.

```text
Small k
  → sensitive to individual points
  → low bias, high variance

Large k
  → smoother predictions
  → higher bias, lower variance
```

A very small `k` can overfit, while a very large `k` can underfit.

`k` is usually selected using **validation or cross-validation**.

---

## Feature Scaling

Distance-based algorithms are sensitive to feature scales.

For example:

```text
Age:       20 – 80
Income:  20,000 – 100,000
```

Income would dominate the distance.

Therefore, features should usually be **standardized or normalized** before applying k-NN.

---

## Classification

For classification, k-NN uses the labels of the nearest neighbors.

Example with `k = 5`:

```text
Nearest neighbors:

● Cat
● Cat
● Dog
● Cat
● Dog

Prediction → Cat
```

A weighted version can give closer neighbors more influence.

---

## Regression

For regression, k-NN typically predicts the average target value of the nearest neighbors.

```text
Neighbors:
10, 12, 11, 15, 12

Prediction:
(10 + 12 + 11 + 15 + 12) / 5 = 12
```

---

## Advantages and Disadvantages

| Advantages                              | Disadvantages                               |
| --------------------------------------- | ------------------------------------------- |
| Simple to understand                    | Prediction can be computationally expensive |
| No explicit training model              | Sensitive to feature scaling                |
| Can model nonlinear relationships       | Sensitive to irrelevant features            |
| Works for classification and regression | Performs poorly in very high dimensions     |

k-NN is sometimes called a **lazy learner** because it does not learn an explicit model during training. Most of the computational work happens when making predictions.

---

## Key Takeaways

1. **k-NN predicts using nearby training samples.**
2. `k` determines how many neighbors are considered.
3. Distance measures determine what "near" means.
4. **Feature scaling is important** for distance-based methods.
5. Small `k` can lead to overfitting; large `k` can lead to underfitting.
6. k-NN can be used for **classification and regression**.
7. k-NN is a **lazy learning algorithm**.
