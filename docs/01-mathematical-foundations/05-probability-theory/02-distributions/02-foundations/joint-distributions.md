# Joint Distribution

## TL;DR

A **joint distribution** describes the probability distribution of **multiple random variables together**.

For two random variables $X$ and $Y$, the joint distribution describes how their values occur in combination.

---

## Discrete Variables

For discrete random variables, the **joint probability mass function (PMF)** is:

$$
P(X=x,Y=y)
$$

It gives the probability that both events occur simultaneously.

The probabilities must satisfy:

$$
P(X=x,Y=y)\geq0
$$

and

$$
\sum_x\sum_y P(X=x,Y=y)=1
$$

---

## Continuous Variables

For continuous random variables, the **joint probability density function (PDF)** is:

$$
f_{X,Y}(x,y)
$$

The probability that $(X,Y)$ lies in a region $A$ is:

$$
P((X,Y)\in A)
=
\iint_A f_{X,Y}(x,y)\,dx\,dy
$$

The density must satisfy:

$$
f_{X,Y}(x,y)\geq0
$$

and

$$
\int_{-\infty}^{\infty}
\int_{-\infty}^{\infty}
f_{X,Y}(x,y)\,dx\,dy
=
1
$$

---

## Example

Suppose $X$ represents the outcome of one die and $Y$ the outcome of another die.

If the dice are independent and fair:

$$
P(X=x,Y=y)=\frac{1}{36}
$$

for

$$
x,y\in\{1,2,3,4,5,6\}
$$

The joint distribution therefore describes all $36$ possible combinations.

---

## Marginal Distributions

Marginal distributions can be obtained from a joint distribution by **summing or integrating out** the other variables.

For discrete variables:

$$
P(X=x)
=
\sum_y P(X=x,Y=y)
$$

For continuous variables:

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

---

## Conditional Distributions

A joint distribution also defines conditional distributions.

For discrete variables:

$$
P(X=x\mid Y=y)
=
\frac{P(X=x,Y=y)}{P(Y=y)}
$$

For continuous variables:

$$
f_{X\mid Y}(x\mid y)
=
\frac{f_{X,Y}(x,y)}{f_Y(y)}
$$

provided the denominator is non-zero.

---

## Independence

Two random variables $X$ and $Y$ are **independent** if their joint distribution factorizes into their marginal distributions.

For discrete variables:

$$
P(X=x,Y=y)
=
P(X=x)P(Y=y)
$$

For continuous variables:

$$
f_{X,Y}(x,y)
=
f_X(x)f_Y(y)
$$

If this equality does not hold, the variables are dependent.

---

## Joint vs. Marginal vs. Conditional

| Distribution | Question |
|---|---|
| **Joint** | How do $X$ and $Y$ behave together? |
| **Marginal** | How does $X$ behave on its own? |
| **Conditional** | How does $X$ behave given $Y=y$? |

These distributions are closely related:

$$
\text{Joint}
\rightarrow
\begin{cases}
\text{Marginal}\\
\text{Conditional}
\end{cases}
$$

---

## Key Idea

A joint distribution captures the **complete probabilistic relationship** between multiple random variables.

For two variables:

$$
\boxed{P(X=x,Y=y)}
$$

or, in the continuous case:

$$
\boxed{f_{X,Y}(x,y)}
$$

It is the foundation for deriving **marginal distributions, conditional distributions, independence, covariance, and correlation**.