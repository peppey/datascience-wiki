# Decision Trees

## TL;DR (30 seconds)

A **Decision Tree** is a supervised machine learning model that makes predictions by recursively splitting the data into smaller subsets based on feature values.

Decision trees are easy to interpret, require little data preprocessing, and can be used for both **classification** and **regression** tasks.

---

## How it works

A decision tree starts with the entire dataset at the **root node**.

At each node, it chooses the feature and split that best separates the data according to a chosen criterion (e.g. Gini Impurity or Information Gain).

This process continues until a stopping criterion is met.

Example:

```text
                 Age < 30?
                 /      \
              Yes        No
             /            \
     Student?         Income > 80k?
        /   \             /      \
      Yes   No         Yes       No
      Buy   Don't      Buy      Don't
```

Each internal node represents a decision, while each leaf node contains the final prediction.

---

## Splitting Criteria

Common criteria for choosing the best split are:

- **Gini Impurity** (used by CART)
- **Information Gain** (based on entropy)
- **Variance Reduction** (for regression trees)

The goal is to create child nodes that are as "pure" as possible.

---

## Advantages

- Easy to understand and visualize
- Little preprocessing required
- Handles numerical and categorical features
- Captures non-linear relationships
- Performs automatic feature selection

---

## Disadvantages

- Prone to overfitting
- Small changes in the data can produce different trees
- Often less accurate than ensemble methods
- Greedy training does not guarantee the globally optimal tree

---

## Preventing Overfitting

Common techniques include:

- Limiting the maximum tree depth
- Requiring a minimum number of samples per leaf
- Pruning unnecessary branches
- Using ensemble methods such as Random Forests

---

## Applications

Decision trees are commonly used for:

- Classification
- Regression
- Credit scoring
- Medical diagnosis
- Customer segmentation
- Fraud detection

---

## Related Topics

- Random Forest
- XGBoost
- Information Gain
- Gini Impurity
- Entropy
- Classification
- Regression
