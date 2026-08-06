# Bayes' Theorem

## TL;DR (30 seconds)

**Bayes' Theorem** describes how to update the probability of a hypothesis when new evidence becomes available.

It is the mathematical foundation of **Bayesian inference**, where we continuously update our beliefs based on observed data.

---

## Formula

$$
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
$$

Where:

- $P(A|B)$ → **Posterior probability**  
  Probability of hypothesis $A$ after observing evidence $B$

- $P(B|A)$ → **Likelihood**  
  Probability of observing evidence $B$ if hypothesis $A$ is true

- $P(A)$ → **Prior probability**  
  Initial belief about hypothesis $A$

- $P(B)$ → **Evidence**  
  Overall probability of observing the data

---

## Intuition

Bayes' Theorem answers:

> "Given that I observed something, how likely is my original assumption now?"

Example:

A medical test is positive.

- Hypothesis $A$: The person has a disease
- Evidence $B$: The test is positive

Bayes' theorem calculates:

> How likely is the person actually sick given a positive test?

---

## Example

Assume:

- 1% of people have a disease:

$$
P(Disease)=0.01
$$

- The test detects the disease correctly 99% of the time:

$$
P(Positive|Disease)=0.99
$$

- The false positive rate is 5%:

$$
P(Positive|No Disease)=0.05
$$

Bayes' theorem combines these probabilities to calculate:

$$
P(Disease|Positive)
$$

The result is the probability that a person is actually sick after receiving a positive test.

---

## Applications in Machine Learning

Bayes' theorem is used in many ML methods:

- **Naive Bayes classifiers**
  - Classification based on probability
  - Used for text classification and spam detection

- **Bayesian inference**
  - Updating model parameters with new data

- **Bayesian optimization**
  - Efficient hyperparameter search

- **Probabilistic models**
  - Modeling uncertainty in predictions

---

## Key Idea

Bayes' theorem allows models to combine:

```text
Prior knowledge
+
New evidence
↓
Updated belief (posterior)
```


It provides a mathematical framework for learning from data while incorporating existing knowledge.
