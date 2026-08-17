# Random Search

## TL;DR

**Random Search** is a hyperparameter optimization method that randomly samples combinations of hyperparameter values.

Instead of evaluating every possible combination, a fixed number of configurations is selected randomly:

```text
Parameter A: [0.01, 0.1, 1.0]
Parameter B: [10, 50, 100]

Random samples:
(0.1, 50)
(1.0, 10)
(0.01, 100)
...
```

The configuration with the best validation score is selected.

---

## Random Search with Cross-Validation

Random Search is commonly combined with **Cross-Validation**.

Each randomly sampled configuration is evaluated using cross-validation, and the mean validation score is used for comparison.

$$
\boxed{
\text{Random Samples}
\rightarrow
\text{Cross-Validation}
\rightarrow
\text{Best Configuration}
}
$$

---

## Advantages and Disadvantages

**Advantages:**

* Usually faster than Grid Search
* Works well with many hyperparameters
* Can explore large search spaces efficiently
* Can sample continuous parameter ranges

**Disadvantages:**

* Does not guarantee finding the best configuration
* Results depend on the random samples
* Important regions of the search space may be missed

---

## Key Idea

Random Search trades exhaustive evaluation for **broader and more efficient exploration** of the hyperparameter space.

It is often preferable to Grid Search when the number of hyperparameters or possible values is large.
