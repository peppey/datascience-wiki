# Markov Chain Monte Carlo

## TL;DR

**Markov Chain Monte Carlo (MCMC)** is a family of methods for generating samples from probability distributions that are difficult to sample from directly.

MCMC constructs a **Markov chain** whose stationary distribution is the desired target distribution.

It is widely used in:

* Bayesian statistics
* probabilistic modeling
* statistical physics
* computational statistics

---

## Basic Idea

Suppose we want samples from a target distribution:

$$
\pi(x).
$$

Instead of sampling directly from $\pi$, construct a Markov chain:

$$
X_0,X_1,X_2,\ldots
$$

with transition probabilities chosen so that:

$$
X_n
\overset{d}{\longrightarrow}
\pi
$$

under suitable conditions.

After an initial **burn-in** period, the generated states can be used as approximate samples from $\pi$.

---

## Markov Property

A Markov chain satisfies:

$$
P(X_{n+1}\mid X_n,X_{n-1},\ldots,X_0)
=

P(X_{n+1}\mid X_n).
$$

The next state therefore depends only on the current state.

---

## Metropolis-Hastings

A common MCMC algorithm is **Metropolis-Hastings**.

Given the current state $x$:

1. Propose a new state $x'$ from a proposal distribution:

$$
x'\sim q(x'\mid x).
$$

2. Compute the acceptance probability:

$$
\alpha(x,x')
============

\min\left(
1,
\frac{\pi(x')q(x\mid x')}
{\pi(x)q(x'\mid x)}
\right).
$$

3. Accept $x'$ with probability $\alpha$; otherwise remain at $x$.

The resulting Markov chain has $\pi$ as its stationary distribution under suitable conditions.

---

## Gibbs Sampling

**Gibbs sampling** is useful when sampling from the full joint distribution is difficult, but sampling from conditional distributions is easy.

For variables $X=(X_1,\ldots,X_d)$, repeatedly sample:

$$
X_1\sim p(X_1\mid X_2,\ldots,X_d)
$$

$$
X_2\sim p(X_2\mid X_1,X_3,\ldots,X_d)
$$

and so on.

Gibbs sampling is particularly common in Bayesian models.

---

## Burn-in and Convergence

The initial states of a Markov chain may not resemble the target distribution.

The initial part of the chain is therefore often discarded as **burn-in**.

A typical workflow is:

$$
\text{Initialize}
\rightarrow
\text{Burn-in}
\rightarrow
\text{Sampling}
\rightarrow
\text{Inference}.
$$

Convergence diagnostics can be used to assess whether the chain has sufficiently explored the target distribution.

---

## Autocorrelation

MCMC samples are generally **not independent**.

Consecutive samples tend to be correlated:

$$
X_t\not!\perp X_{t+1}.
$$

This reduces the amount of independent information contained in the samples.

The **effective sample size (ESS)** measures the approximate number of independent samples represented by the correlated chain.

---

## Bayesian Inference

MCMC is especially useful when the posterior distribution:

$$
p(\theta\mid D)
\propto
p(D\mid\theta)p(\theta)
$$

cannot be normalized or sampled from analytically.

MCMC can generate samples:

$$
\theta^{(1)},\ldots,\theta^{(N)}
\approx
p(\theta\mid D).
$$

Posterior quantities can then be estimated from these samples.

---

## Hamiltonian Monte Carlo

**Hamiltonian Monte Carlo (HMC)** introduces auxiliary momentum variables and uses gradients of the target density to propose distant states efficiently.

It can explore high-dimensional continuous distributions much more efficiently than basic random-walk methods.

**No-U-Turn Sampler (NUTS)** is a widely used adaptive variant of HMC.

---

## Key Idea

MCMC converts a difficult sampling problem into a problem of constructing a suitable Markov chain:

$$
\boxed{
\text{Target Distribution}
\rightarrow
\text{Markov Chain}
\rightarrow
\text{Approximate Samples}
}
$$

The central challenge is obtaining a chain that **mixes well** and explores the target distribution efficiently.
