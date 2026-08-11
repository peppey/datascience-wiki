# Statistical Power

## TL;DR

**Statistical power** is the probability that a statistical test correctly rejects the null hypothesis when a real effect exists.

It is defined as:

$$
\text{Power} = P(\text{reject } H_0 \mid H_1 \text{ is true})
$$

A common relationship is:

$$
\text{Power} = 1-\beta
$$

where $\beta$ is the probability of a **Type II error**.

---

## Hypothesis Testing

In a hypothesis test:

* $H_0$: null hypothesis
* $H_1$: alternative hypothesis
* $\alpha$: significance level
* $\beta$: probability of a Type II error
* $1-\beta$: statistical power

There are two common types of errors:

| Reality    | Decision             | Error                   |
| ---------- | -------------------- | ----------------------- |
| $H_0$ true | Reject $H_0$         | Type I error ($\alpha$) |
| $H_1$ true | Fail to reject $H_0$ | Type II error ($\beta$) |

---

## Factors Affecting Power

Statistical power generally increases with:

* **Larger sample size**
* **Larger effect size**
* **Lower variability**
* **Higher significance level $\alpha$**

For example, a larger sample makes it easier to distinguish a real effect from random variation.

---

## Sample Size Planning

Power analysis is often used **before collecting data** to determine the required sample size.

Given:

* desired power, e.g. $0.80$
* significance level, e.g. $\alpha=0.05$
* expected effect size
* estimated variability

we can calculate an appropriate sample size.

A commonly used target is:

$$
\text{Power} \geq 0.80
$$

---

## Example

Suppose a study is designed to detect whether a treatment has an effect.

If the statistical power is $0.80$, then:

$$
P(\text{reject } H_0 \mid H_1\text{ true})=0.80
$$

Thus, if the effect really exists, the test has an **80% probability of detecting it**.

The remaining 20% corresponds to the probability of a Type II error:

$$
\beta = 0.20
$$

---

## Key Idea

Statistical power answers the question:

> **If a real effect exists, how likely is my test to detect it?**

High power reduces the probability of missing a real effect.
