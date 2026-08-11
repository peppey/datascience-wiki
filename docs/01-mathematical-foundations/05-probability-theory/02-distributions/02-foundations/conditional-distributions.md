# Conditional Distributions

## TL;DR

A **conditional distribution** describes the probability distribution of a random variable **given that another variable or event is known**.

For random variables $X$ and $Y$, the conditional distribution of $X$ given $Y=y$ is written as:

$$
P(X=x\mid Y=y)
$$

For continuous variables, the conditional probability density is:

$$
f_{X\mid Y}(x\mid y)
=

\frac{f_{X,Y}(x,y)}{f_Y(y)}
$$

when $f_Y(y)>0$.

---

## Discrete Case

For discrete random variables:

$$
P(X=x\mid Y=y)
=
\frac{P(X=x,Y=y)}{P(Y=y)}
$$

where:

$$
P(Y=y)>0
$$

The numerator is the **joint probability**, while the denominator normalizes the distribution.

---

## Continuous Case

For continuous random variables:

$$
f_{X\mid Y}(x\mid y)
=

\frac{f_{X,Y}(x,y)}
{f_Y(y)}
$$

where:

$$
f_Y(y)
=

\int_{-\infty}^{\infty}
f_{X,Y}(x,y),dx
$$

The conditional density integrates to $1$ over $x$.

---

## Example

Suppose $X$ represents a person's height and $Y$ represents their gender.

The distribution:

$$
P(X=x)
$$

describes the overall distribution of heights.

The conditional distribution:

$$
P(X=x\mid Y=\text{female})
$$

describes the distribution of heights **given that the person is female**.

The additional information about $Y$ changes the distribution of $X$.

---

## Conditional Expectation

Conditional distributions can be used to define the **conditional expectation**:

$$
\mathbb{E}[X\mid Y=y]
$$

For discrete variables:

$$
\mathbb{E}[X\mid Y=y]
=====================

\sum_x
xP(X=x\mid Y=y)
$$

For continuous variables:

$$
\mathbb{E}[X\mid Y=y]
=====================

\int
x f_{X\mid Y}(x\mid y),dx
$$

---

## Relation to Bayes' Theorem

Conditional distributions are closely related to **Bayes' theorem**:

$$
P(X\mid Y)
==========

\frac{P(Y\mid X)P(X)}
{P(Y)}
$$

Bayesian inference uses this relationship to update a distribution after observing new information.

---

## Independence

If $X$ and $Y$ are independent, then knowing $Y$ does not change the distribution of $X$:

$$
P(X=x\mid Y=y)=P(X=x)
$$

Similarly:

$$
f_{X\mid Y}(x\mid y)=f_X(x)
$$

Thus, conditional distributions provide a way to express **dependence between random variables**.

---

## Applications

Conditional distributions are fundamental in:

* Bayesian inference
* probabilistic graphical models
* regression
* classification
* generative models
* Markov models
* time series
* machine learning

For example, classification can be viewed as modeling:

$$
P(Y\mid X)
$$

the distribution of a target $Y$ given observed features $X$.

---

## Related Concepts

* [Joint Distributions](joint-distributions.md)
* [Marginal Distributions](marginal-distributions.md)
* [Conditional Probability](conditional-probability.md)
* [Bayes' Theorem](bayes-theorem.md)
* [Independence](independence.md)
* [Conditional Expectation](conditional-expectation.md)
