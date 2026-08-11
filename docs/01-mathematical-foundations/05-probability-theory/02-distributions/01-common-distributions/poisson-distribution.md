# Poisson Distribution

## TL;DR

The **Poisson distribution** is a discrete probability distribution that models the **number of events occurring within a fixed interval** when events happen independently at a constant average rate.

It is defined by the parameter:

$$
\lambda > 0
$$

and written as:

$$
X\sim\operatorname{Poisson}(\lambda)
$$

Its probability mass function is:

$$
P(X=k)
=

\frac{\lambda^k e^{-\lambda}}{k!},
\qquad k=0,1,2,\ldots
$$

---

## Parameters

The parameter $\lambda$ represents the **expected number of events** in the given interval.

For a Poisson-distributed random variable:

$$
\mathbb{E}[X]=\lambda
$$

and:

$$
\operatorname{Var}(X)=\lambda
$$

Thus, the mean and variance are equal.

---

## Example

Suppose a server receives an average of 5 requests per minute.

The number of requests $X$ in one minute can be modeled as:

$$
X\sim\operatorname{Poisson}(5)
$$

The probability of receiving exactly 3 requests is:

$$
P(X=3)
======

\frac{5^3e^{-5}}{3!}
$$

---

## Cumulative Probability

The probability of observing at most $k$ events is:

$$
P(X\leq k)
=
\sum_{i=0}^{k}
\frac{\lambda^i e^{-\lambda}}{i!}
$$

The probability of observing at least one event is:

$$
P(X\geq1)
= 1-P(X=0)

1-e^{-\lambda}
$$

---

## Poisson Process

The Poisson distribution is closely related to the **Poisson process**.

If events occur according to a Poisson process with rate $\lambda$, then the number of events observed during a time interval of length $t$ follows:

$$
N(t)\sim\operatorname{Poisson}(\lambda t)
$$

The corresponding waiting time between events follows an **exponential distribution**:

$$
T\sim\operatorname{Exp}(\lambda)
$$

Thus:

* **Poisson distribution** → number of events
* **Exponential distribution** → waiting time between events

---

## Assumptions

A classical Poisson model assumes that:

* events occur independently
* events occur at a constant average rate
* two events do not occur at exactly the same instant
* the probability of an event in a small interval is proportional to the interval's length

---

## Applications

The Poisson distribution is commonly used for:

* website requests
* customer arrivals
* phone calls
* insurance claims
* equipment failures
* defects in manufacturing
* mutations
* traffic accidents
* event counts in a fixed time or space interval
