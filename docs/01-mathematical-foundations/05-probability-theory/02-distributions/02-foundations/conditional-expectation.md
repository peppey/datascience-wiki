# Conditional Expectation

## TL;DR

**Conditional expectation** is the expected value of a random variable given information about another random variable or event.

For random variables $X$ and $Y$:

$$
\mathbb{E}[X\mid Y]
$$

denotes the expected value of $X$ given $Y$.

## Conditioning on an Event

For an event $A$ with $\mathbb{P}(A)>0$:

$$
\mathbb{E}[X\mid A]
=

\frac{\mathbb{E}[X\mathbf{1}_A]}{\mathbb{P}(A)}
$$

where $\mathbf{1}_A$ is the indicator function of $A$.

## Discrete Random Variables

If $X$ and $Y$ are discrete, then:

$$
\mathbb{E}[X\mid Y=y]
=
\sum_x x,\mathbb{P}(X=x\mid Y=y)
$$

Thus, conditional expectation is the weighted average of possible values of $X$ using the conditional distribution.

## Continuous Random Variables

For continuous variables:

$$
\mathbb{E}[X\mid Y=y]
=

\int_{-\infty}^{\infty}
x,f_{X\mid Y}(x\mid y),dx
$$

where $f_{X\mid Y}(x\mid y)$ is the conditional density of $X$ given $Y=y$.

## Conditional Expectation as a Random Variable

When conditioning on $Y$, the quantity

$$
\mathbb{E}[X\mid Y]
$$

is itself a random variable and can be viewed as a function of $Y$:

$$
\mathbb{E}[X\mid Y]=g(Y).
$$

It represents the best prediction of $X$ based only on the information contained in $Y$, when prediction error is measured by squared error.

## Law of Total Expectation

Conditional expectation satisfies the **law of total expectation**:

$$
\mathbb{E}[X]
=

\mathbb{E}\left[\mathbb{E}[X\mid Y]\right].
$$

For a discrete $Y$:

$$
\mathbb{E}[X]
=

\sum_y
\mathbb{E}[X\mid Y=y]\mathbb{P}(Y=y).
$$

## Example

Suppose a fair six-sided die is rolled and $X$ is the outcome.

If we know that the result is even, then:

$$
\mathbb{E}[X\mid X\text{ is even}]
=

\frac{2+4+6}{3}

4.

$$

Without this information:

$$
\mathbb{E}[X]=3.5.
$$

Thus, conditioning changes the expected value by incorporating additional information.
