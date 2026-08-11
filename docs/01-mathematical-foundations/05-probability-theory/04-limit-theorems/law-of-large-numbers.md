# Law of Large Numbers

## TL;DR

The **Law of Large Numbers (LLN)** states that, as the number of observations increases, the sample average converges to the **expected value** of the underlying random variable.

For independent and identically distributed random variables $X_1,\ldots,X_n$ with finite expected value $\mu$:

$$
\bar{X}
=

\frac{1}{n}
\sum_{i=1}^{n}X_i
\rightarrow
\mu
$$

as:

$$
n\rightarrow\infty
$$

---

## Intuition

Consider repeatedly rolling a fair six-sided die.

The expected value is:

$$
\mathbb{E}[X]
=
\frac{1+2+3+4+5+6}{6}

3.5
$$

With only a few rolls, the average can differ substantially from $3.5$.

As the number of rolls increases, the average tends to get closer to $3.5$.

The LLN explains this convergence.

---

## Weak Law of Large Numbers

The **Weak Law of Large Numbers** states that the sample mean converges to the expected value **in probability**:

$$
\bar{X}_n
\xrightarrow{P}
\mu
$$

This means that for every $\varepsilon>0$:

$$
P\left(
|\bar{X}_n-\mu|>\varepsilon
\right)
\rightarrow 0
$$

as $n\rightarrow\infty$.

---

## Strong Law of Large Numbers

The **Strong Law of Large Numbers** states that the sample mean converges to the expected value **almost surely**:

$$
\bar{X}_n
\xrightarrow{a.s.}
\mu
$$

Informally, this means that with probability $1$, the sequence of sample means eventually converges to $\mu$.

---

## LLN vs. Central Limit Theorem

The **Law of Large Numbers** describes the convergence of the sample mean:

$$
\bar{X}_n\rightarrow\mu
$$

The **Central Limit Theorem** describes the distribution of the deviations around the mean:

$$
\frac{\bar{X}_n-\mu}{\sigma/\sqrt{n}}
\rightarrow
\mathcal{N}(0,1)
$$

In short:

|               | Law of Large Numbers          | Central Limit Theorem  |
| ------------- | ----------------------------- | ---------------------- |
| Focus         | Convergence                   | Distribution           |
| Result        | $\bar{X}_n\rightarrow\mu$     | Normal distribution    |
| Main question | Where does the mean converge? | How does it fluctuate? |

---

## Applications

The LLN is fundamental to:

* statistical estimation
* Monte Carlo methods
* simulation
* machine learning
* probability theory
* sampling
* empirical risk minimization

For example, the empirical mean

$$
\frac{1}{n}\sum_{i=1}^{n}f(X_i)
$$

can be used to approximate the expected value:

$$
\mathbb{E}[f(X)].
$$