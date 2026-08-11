# Marginal Distributions

## TL;DR

A **marginal distribution** describes the distribution of one variable without conditioning on the values of other variables.

For a joint distribution of $X$ and $Y$, the marginal distribution of $X$ is obtained by **summing or integrating out** $Y$.

---

## Joint Distribution

Suppose $X$ and $Y$ have a joint probability distribution.

For discrete variables:

$$
P(X=x,Y=y)
$$

For continuous variables, the joint probability density function is:

$$
f_{X,Y}(x,y)
$$

The joint distribution describes how $X$ and $Y$ behave **together**.

---

## Marginal Distribution

The **marginal distribution** of $X$ ignores the value of $Y$.

### Discrete Variables

For discrete variables, sum over all possible values of $Y$:

$$
P(X=x)
=
\sum_y P(X=x,Y=y)
$$

Similarly:

$$
P(Y=y)
=
\sum_x P(X=x,Y=y)
$$

### Continuous Variables

For continuous variables, integrate over the other variable:

$$
f_X(x)
=
\int_{-\infty}^{\infty}
f_{X,Y}(x,y)\,dy
$$

Similarly:

$$
f_Y(y)
=
\int_{-\infty}^{\infty}
f_{X,Y}(x,y)\,dx
$$

This process is called **marginalization**.

---

## Example

Consider the joint probability table:

| $X \backslash Y$ | $0$ | $1$ | Marginal $P(X)$ |
|---|---:|---:|---:|
| $0$ | $0.2$ | $0.3$ | $0.5$ |
| $1$ | $0.1$ | $0.4$ | $0.5$ |
| **Marginal $P(Y)$** | **0.3** | **0.7** | **1.0** |

The marginal distribution of $X$ is:

$$
P(X=0)=0.2+0.3=0.5
$$

$$
P(X=1)=0.1+0.4=0.5
$$

The marginal distribution of $Y$ is:

$$
P(Y=0)=0.2+0.1=0.3
$$

$$
P(Y=1)=0.3+0.4=0.7
$$

---

## Marginal vs. Conditional Distribution

Marginal and conditional distributions answer different questions.

### Marginal

> What is the distribution of $X$ overall?

$$
P(X=x)
$$

### Conditional

> What is the distribution of $X$ given that $Y=y$?

$$
P(X=x\mid Y=y)
$$

The conditional distribution depends on a particular value of $Y$, while the marginal distribution averages over all possible values of $Y$.

---

## Relationship to Joint Distributions

A joint distribution can be used to obtain marginal distributions:

$$
P(X=x)
=
\sum_y P(X=x,Y=y)
$$

and

$$
P(Y=y)
=
\sum_x P(X=x,Y=y)
$$

For continuous variables:

$$
f_X(x)
=
\int f_{X,Y}(x,y)\,dy
$$

Marginal distributions therefore contain **less information** than the corresponding joint distribution because they ignore relationships between variables.

---

## Key Idea

Marginalization means **summing or integrating out variables that are not of interest**.

$$
\boxed{
\text{Joint distribution}
\;\xrightarrow{\text{sum/integrate out}}\;
\text{Marginal distribution}
}
$$

This concept is fundamental in **probability, Bayesian inference, graphical models, and machine learning**.