# Grid Search

## TL;DR

**Grid Search** systematically evaluates different combinations of **hyperparameters** to find a well-performing configuration.

Given a set of possible values:

```text
Parameter A: [0.01, 0.1, 1.0]
Parameter B: [10, 50, 100]
```

Grid Search evaluates all combinations:

```text
(0.01, 10)   (0.01, 50)   (0.01, 100)
(0.1,  10)   (0.1,  50)   (0.1,  100)
(1.0,  10)   (1.0,  50)   (1.0,  100)
```

The combination with the best validation score is selected.

---

## Grid Search with Cross-Validation

Grid Search is commonly combined with **Cross-Validation**.

Each hyperparameter combination is evaluated using cross-validation, and the mean validation score is used for comparison.

$$
\boxed{
\text{Hyperparameter Grid}
\rightarrow
\text{Cross-Validation}
\rightarrow
\text{Best Configuration}
}
$$

---

## Advantages and Disadvantages

**Advantages:**

* Simple and systematic
* Easy to implement
* Can find the best configuration within the specified grid

**Disadvantages:**

* Can become computationally expensive
* Only evaluates explicitly specified values
* Becomes inefficient with many hyperparameters

---

## Key Idea

Grid Search is a **hyperparameter optimization** method that exhaustively evaluates a predefined set of parameter combinations.
