# PDF and CDF

## TL;DR

A **probability density function (PDF)** describes how probability is distributed over continuous values.

A **cumulative distribution function (CDF)** gives the probability that a random variable is less than or equal to a given value.

For a continuous random variable $X$:

$$
F_X(x) = P(X \leq x)
$$

and, if a density exists,

$$
F_X(x) = \int_{-\infty}^{x} f_X(t)\,dt
$$

---

## Probability Density Function

The **probability density function** $f_X(x)$ describes the density of probability around $x$.

For a continuous random variable:

$$
P(a \leq X \leq b)
=
\int_a^b f_X(x)\,dx
$$

A PDF must satisfy:

$$
f_X(x) \geq 0
$$

and

$$
\int_{-\infty}^{\infty} f_X(x)\,dx = 1
$$

Importantly, for continuous variables:

$$
P(X=x)=0
$$

The value of the PDF itself is **not a probability**.

---

## Cumulative Distribution Function

The **cumulative distribution function (CDF)** is defined as:

$$
F_X(x) = P(X \leq x)
$$

It gives the accumulated probability up to $x$.

For any random variable:

$$
0 \leq F_X(x) \leq 1
$$

and $F_X(x)$ is monotonically non-decreasing.

For a continuous distribution with density $f_X$:

$$
F_X(x)
=
\int_{-\infty}^{x} f_X(t)\,dt
$$

If the CDF is differentiable:

$$
f_X(x) = F_X'(x)
$$

---

## PDF vs. CDF

| | PDF | CDF |
|---|---|---|
| Name | Probability Density Function | Cumulative Distribution Function |
| Meaning | Probability density at $x$ | Probability up to $x$ |
| Range | $[0,\infty)$ | $[0,1]$ |
| Probability directly? | No | Yes |
| Continuous case | Integrate to get probabilities | Directly gives cumulative probabilities |

For example:

$$
P(a \leq X \leq b)
=
F_X(b)-F_X(a)
$$

---

## Discrete Distributions

For a **discrete** random variable, probability is described by a **probability mass function (PMF)**:

$$
p_X(x)=P(X=x)
$$

The CDF is still defined as:

$$
F_X(x)=P(X\leq x)
$$

but is obtained by summation:

$$
F_X(x)
=
\sum_{t\leq x}p_X(t)
$$

Thus:

- **Continuous:** probabilities are obtained by integrating a PDF.
- **Discrete:** probabilities are obtained by summing a PMF.
- **Both:** have a CDF.

---

## Example

Suppose $X$ is uniformly distributed on $[0,1]$.

Its density is:

$$
f_X(x)=
\begin{cases}
1 & 0\leq x\leq1\\
0 & \text{otherwise}
\end{cases}
$$

The CDF is:

$$
F_X(x)=
\begin{cases}
0 & x<0\\
x & 0\leq x\leq1\\
1 & x>1
\end{cases}
$$

Therefore:

$$
P(0.2\leq X\leq0.7)
=
F_X(0.7)-F_X(0.2)
=
0.5
$$

---

## Key Relationship

For continuous distributions:

$$
\boxed{
F_X(x)=\int_{-\infty}^{x}f_X(t)\,dt
}
$$

and, when differentiable,

$$
\boxed{
f_X(x)=\frac{d}{dx}F_X(x)
}
$$

The PDF describes **local probability density**, while the CDF describes **accumulated probability**.