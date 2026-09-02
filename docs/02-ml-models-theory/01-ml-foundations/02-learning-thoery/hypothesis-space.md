# Hypothesis Spaces

## TL;DR (30 seconds)

A **hypothesis space** is the set of all possible models that a machine learning algorithm can choose from.

The key idea:

> A machine learning algorithm searches a predefined space of possible functions for a hypothesis that explains the training data well.

The hypothesis space determines **what kinds of relationships a model can learn** and is therefore closely related to **model complexity, overfitting, and generalization**.

---

## What Is a Hypothesis?

A **hypothesis** is a function that maps inputs to predictions:

$$
h: X \rightarrow Y
$$

where:

* $X$ = input space
* $Y$ = output space
* $h$ = hypothesis

For example, a linear regression model can be written as:

$$
h(x) = w^T x + b
$$

A particular choice of $w$ and $b$ defines one specific hypothesis.

---

## Definition of a Hypothesis Space

The **hypothesis space** $\mathcal{H}$ is the set of all hypotheses that a learning algorithm is able to consider:

$$
\mathcal{H} = \{h: X \rightarrow Y\}
$$

In practice, $\mathcal{H}$ is restricted by the chosen model class.

For example, if we use linear regression:

$$
\mathcal{H}_{linear}
=
\{h(x)=w^Tx+b \mid w,b\}
$$

The hypothesis space therefore contains **all possible linear functions** that can be represented by the model.

---

## Hypothesis Space vs. Parameter Space

These concepts are closely related but describe different things.

The **parameter space** contains possible parameter values:

$$
\Theta = \{\theta\}
$$

A parameter vector $\theta$ defines a hypothesis:

$$
h_\theta(x)
$$

The hypothesis space is therefore:

$$
\mathcal{H}
=
\{h_\theta \mid \theta \in \Theta\}
$$

For example, in linear regression:

$$
\theta = (w,b)
$$

and

$$
h_\theta(x)=w^Tx+b
$$

The parameter space describes **which parameter values are possible**, while the hypothesis space describes **which functions can be represented**.

---

## Examples of Hypothesis Spaces

Different model classes define different hypothesis spaces.

| Model                 | Hypothesis Space                                           |
| --------------------- | ---------------------------------------------------------- |
| Linear regression     | All linear functions                                       |
| Logistic regression   | All linear decision boundaries                             |
| Polynomial regression | All polynomials up to a given degree                       |
| Decision tree         | Functions representable by the allowed tree structures     |
| k-NN                  | Functions induced by the training data and distance metric |
| Neural network        | Functions representable by the given architecture          |

The choice of model therefore determines which hypotheses are available to the learning algorithm.

---

## Training as Search

Training can be viewed as a search through the hypothesis space.

Given a loss function $\ell$, the algorithm tries to find a hypothesis with low empirical risk:

$$
\hat{h}
=
\arg\min_{h\in\mathcal{H}}
\hat{R}(h)
$$

where:

$$
\hat{R}(h)
=
\frac{1}{n}
\sum_{i=1}^{n}
\ell(h(x_i),y_i)
$$

The learning algorithm therefore answers:

> Which hypothesis in $\mathcal{H}$ best explains the training data?

Different optimization algorithms may search the same hypothesis space in different ways.

---

## Size and Complexity of the Hypothesis Space

The **complexity** of a hypothesis space describes how expressive it is.

A simple hypothesis space may contain only a small number of possible functions.

A complex hypothesis space can contain a very large number of highly flexible functions.

For example:

$$
\mathcal{H}_{linear}
\subset
\mathcal{H}_{quadratic}
\subset
\mathcal{H}_{cubic}
$$

for polynomial regression.

Increasing the polynomial degree therefore increases the hypothesis space.

A more expressive hypothesis space can represent more complex relationships.

---

## Hypothesis Space and Underfitting

If the hypothesis space is too restrictive, it may not contain a function that adequately describes the underlying data.

This can lead to **underfitting**.

For example, suppose the true relationship is nonlinear:

$$
y = x^2
$$

but the model is restricted to linear functions:

$$
\mathcal{H}
=
\{w x+b\}
$$

No hypothesis in this space can represent the quadratic relationship exactly.

The model therefore has a **high bias**.

---

## Hypothesis Space and Overfitting

A very expressive hypothesis space can represent extremely complex functions.

This can lead to **overfitting**.

For example, a high-degree polynomial can potentially fit every training point:

$$
\hat{R}(h) \approx 0
$$

while performing poorly on unseen data:

$$
R(h) \gg \hat{R}(h)
$$

The model has enough flexibility to fit not only the underlying pattern but also noise in the training data.

---

## Regularization and Hypothesis Spaces

Regularization can be understood as a way of **restricting or controlling the effective set of preferred hypotheses**.

For example, ridge regression minimizes:

$$
\hat{R}(h)
+
\lambda \|w\|_2^2
$$

Instead of simply choosing the hypothesis with the lowest training error, the algorithm also penalizes large parameter values.

This favors simpler hypotheses.

Regularization therefore introduces a preference for certain regions of the hypothesis space rather than treating all hypotheses equally.

---

## Hypothesis Space and Generalization

The goal is not to find a hypothesis that only performs well on the training data.

The hypothesis should also perform well on unseen data.

Ideally:

$$
\hat{R}(h) \approx R(h)
$$

where:

* $\hat{R}(h)$ = empirical risk
* $R(h)$ = true risk

The complexity of $\mathcal{H}$ plays an important role in determining whether good training performance generalizes.

This is one reason why learning theory studies the complexity of hypothesis classes.

---

## Measuring Hypothesis Space Complexity

Several concepts are used to characterize the complexity of a hypothesis space.

### VC Dimension

The **VC dimension** measures the capacity of a hypothesis class to represent different classification patterns.

A higher VC dimension generally indicates a more expressive hypothesis class.

It is used to derive theoretical **generalization bounds**.

---

### Rademacher Complexity

**Rademacher complexity** measures how well a hypothesis class can correlate with random noise.

Higher Rademacher complexity generally means that the hypothesis class is more flexible and potentially more prone to overfitting.

It is another tool for deriving generalization guarantees.

---

## Example: Polynomial Regression

Consider the hypothesis:

$$
h(x)
=
w_0+w_1x+w_2x^2+\dots+w_dx^d
$$

For degree $1$:

$$
\mathcal{H}_1
=
\{w_0+w_1x\}
$$

For degree $2$:

$$
\mathcal{H}_2
=
\{w_0+w_1x+w_2x^2\}
$$

For degree $3$:

$$
\mathcal{H}_3
=
\{w_0+w_1x+w_2x^2+w_3x^3\}
$$

Thus:

$$
\mathcal{H}_1
\subset
\mathcal{H}_2
\subset
\mathcal{H}_3
$$

Increasing the degree expands the hypothesis space and allows increasingly complex functions.

---

## Hypothesis Space and Inductive Bias

A learning algorithm usually cannot determine the correct hypothesis from the training data alone.

It therefore relies on **inductive bias**: assumptions about which hypotheses are more plausible.

Examples:

* Linear regression assumes linear relationships.
* Decision trees prefer hierarchical feature splits.
* Convolutional neural networks exploit spatial locality and translation-related structure.
* k-NN assumes that nearby points tend to have similar outputs.

The model architecture and learning algorithm therefore impose a particular structure on the hypothesis space.

---

## Connection to Uniform Convergence

Uniform convergence considers whether empirical and true risk are close **for all hypotheses in a hypothesis class**:

$$
\sup_{h\in\mathcal{H}}
|\hat{R}(h)-R(h)|
\rightarrow 0
$$

The complexity of the hypothesis space is important here.

Very large or complex hypothesis classes generally require more data to obtain strong uniform convergence guarantees.

Thus:

$$
\text{Hypothesis Space}
\rightarrow
\text{Model Complexity}
\rightarrow
\text{Generalization}
$$

This connects hypothesis spaces directly to learning-theoretic concepts such as **VC dimension, Rademacher complexity, and uniform convergence**.

---

## Summary

| Concept                        | Meaning                                   |
| ------------------------------ | ----------------------------------------- |
| Hypothesis                     | A possible function/model                 |
| Hypothesis space $\mathcal{H}$ | Set of possible hypotheses                |
| Parameter space $\Theta$       | Set of possible parameter values          |
| Model complexity               | Expressiveness of the hypothesis space    |
| Inductive bias                 | Assumptions favoring certain hypotheses   |
| VC dimension                   | Measure of hypothesis class capacity      |
| Rademacher complexity          | Measure of ability to fit random patterns |
| Underfitting                   | Hypothesis space too restrictive          |
| Overfitting                    | Hypothesis space too expressive           |

The central idea is:

$$
\boxed{
\text{A hypothesis space defines what a model is capable of learning.}
}
$$

Training then searches this space for a hypothesis that fits the data well while ideally **generalizing to unseen data**.
