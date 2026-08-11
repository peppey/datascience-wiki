# Exponential Distribution

## TL;DR

The **exponential distribution** is a continuous probability distribution commonly used to model the **waiting time until an event occurs**.

It is defined by a rate parameter:

$$
\lambda > 0
$$

and written as:

$$
X\sim\operatorname{Exp}(\lambda)
$$

Its probability density function is:

$$
f(x)=
\begin{cases}
\lambda e^{-\lambda x}, & x\geq 0\
0, & x<0
\end{cases}
$$

---

## Cumulative Distribution Function

The cumulative distribution function is:

$$
F(x)=P(X\leq x)
=

1-e^{-\lambda x},
\qquad x\geq0
$$

Therefore, the probability of waiting longer than $x$ is:

$$
P(X>x)=e^{-\lambda x}
$$

---

## Parameters

The parameter $\lambda$ is the **rate** of events.

A larger $\lambda$ means that events occur more frequently and the expected waiting time becomes shorter.

The expected value is:

$$
\mathbb{E}[X]=\frac{1}{\lambda}
$$

and the variance is:

$$
\operatorname{Var}(X)=\frac{1}{\lambda^2}
$$

---

## Example

Suppose customers arrive at an average rate of:

$$
\lambda=2
$$

customers per hour.

The waiting time $X$ until the next customer can be modeled as:

$$
X\sim\operatorname{Exp}(2)
$$

The expected waiting time is:

$$
\mathbb{E}[X]=\frac{1}{2}
$$

hours, or 30 minutes.

---

## Memoryless Property

The exponential distribution is **memoryless**.

For $s,t\geq0$:

$$
P(X>s+t\mid X>s)=P(X>t)
$$

In other words, if an event has not occurred yet, the probability distribution of the additional waiting time does not depend on how long we have already waited.

---

## Applications

The exponential distribution is commonly used for:

* waiting times
* customer arrivals
* failure times
* reliability analysis
* queueing systems
* Poisson processes
* survival analysis

It is closely related to the **Poisson distribution**: if events occur according to a Poisson process with rate $\lambda$, the time between consecutive events follows an exponential distribution.