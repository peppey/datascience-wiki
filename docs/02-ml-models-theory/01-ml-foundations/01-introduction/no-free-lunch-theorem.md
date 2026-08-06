# No Free Lunch Theorem

## TL;DR

The **No Free Lunch (NFL) Theorem** states that no machine learning algorithm is universally better than all others.  
An algorithm can only perform well when it makes assumptions about the data.

---

## Main Idea

Without any assumptions about the data distribution, all learning algorithms perform equally well on average.

This means:

- There is no "best" model for every problem.
- A model that works well for one dataset may fail on another.
- Good performance comes from matching model assumptions to the problem.

---

## Example

A linear model assumes:

- relationships are approximately linear
- simple patterns are sufficient

A neural network assumes:

- complex nonlinear patterns may exist
- enough data is available

Neither model is always better. Their success depends on whether their assumptions fit the data.

---

## Connection to Machine Learning

The theorem explains why **inductive bias** is necessary.

Every ML model has assumptions about the world:

- Decision trees prefer rule-like structures.
- SVMs prefer large-margin boundaries.
- Neural networks can learn complex representations.

These assumptions allow models to generalize from training data to unseen data.

---

## Key Takeaway

> There is no universally best machine learning algorithm.  
> The best model depends on the data, the task, and the assumptions built into the model.