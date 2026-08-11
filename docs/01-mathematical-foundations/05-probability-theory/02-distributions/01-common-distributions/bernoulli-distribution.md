# Bernoulli Distribution

## TL;DR

The **Bernoulli distribution** is a discrete probability distribution for a **single binary experiment** with two possible outcomes:

* success: $X=1$
* failure: $X=0$

It is defined by the parameter:

$$
p=P(X=1)
$$

and written as:

$$
X\sim\operatorname{Bernoulli}(p)
$$

---

## Probability Mass Function

The probability mass function is:

$$
P(X=x)
=

p^x(1-p)^{1-x},
\qquad x\in{0,1}
$$

Therefore:

$$
P(X=1)=p
$$

and:

$$
P(X=0)=1-p
$$

---

## Expected Value and Variance

The expected value is:

$$
\mathbb{E}[X]=p
$$

The variance is:

$$
\operatorname{Var}(X)=p(1-p)
$$

---

## Example

Consider flipping a coin once.

Let:

$$
X=
\begin{cases}
1 & \text{if heads}\
0 & \text{if tails}
\end{cases}
$$

For a fair coin:

$$
X\sim\operatorname{Bernoulli}(0.5)
$$

Thus:

$$
P(X=1)=0.5
$$

and:

$$
P(X=0)=0.5
$$

---

## Bernoulli vs. Binomial Distribution

The Bernoulli distribution describes **one trial**.

The **binomial distribution** describes the number of successes in $n$ independent Bernoulli trials.

If:

$$
X_1,\ldots,X_n
\sim\operatorname{Bernoulli}(p)
$$

independently, then:

$$
\sum_{i=1}^{n}X_i
\sim
\operatorname{Binomial}(n,p)
$$

Thus, the Bernoulli distribution can be viewed as the building block of the binomial distribution.

---

## Applications

Bernoulli distributions are commonly used for:

* binary classification
* success/failure experiments
* coin flips
* click/no-click events
* conversion/no-conversion events
* binary outcomes
* Bernoulli trials

In machine learning, binary labels are often modeled using a Bernoulli distribution.

---

## Related Concepts

* [Binomial Distribution](binomial-distribution.md)
* [Categorical Distribution](categorical-distribution.md)
* [Random Variables](random-variables.md)
* [Expected Value](expected-value.md)
* [Variance](variance.md)
