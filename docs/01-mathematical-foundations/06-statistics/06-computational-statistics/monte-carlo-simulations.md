# Monte Carlo Simulations

## TL;DR

**Monte Carlo simulation** uses repeated random sampling to approximate quantities that are difficult to compute analytically.

It is widely used in:

* probability
* statistics
* numerical integration
* optimization
* finance
* machine learning

---

## Basic Idea

Suppose we want to estimate an expected value:

$$
\mathbb{E}[f(X)].
$$

Generate independent samples:

$$
X_1,\ldots,X_N
$$

and approximate the expectation using the sample mean:

$$
\mathbb{E}[f(X)]
\approx
\frac{1}{N}
\sum_{i=1}^{N}f(X_i).
$$

As $N$ increases, the estimate converges to the true expectation under suitable conditions.

---

## Example: Estimating $\pi$

Generate random points uniformly in the square:

$$
[-1,1]\times[-1,1].
$$

Count how many fall inside the unit circle:

$$
x^2+y^2\leq1.
$$

The ratio of points inside the circle approximates:

$$
\frac{\pi}{4}.
$$

Therefore:

$$
\pi
\approx
4\frac{N_{\text{inside}}}{N}.
$$

---

## Monte Carlo Integration

An integral can be estimated by sampling points.

For:

$$
I=\int_a^b f(x),dx,
$$

sample:

$$
X_i\sim U(a,b).
$$

Then:

$$
I
\approx
(b-a)
\frac{1}{N}
\sum_{i=1}^{N}f(X_i).
$$

This generalizes naturally to higher dimensions.

---

## Convergence

The **Law of Large Numbers** guarantees convergence of the sample average under appropriate assumptions:

$$
\frac{1}{N}
\sum_{i=1}^{N}f(X_i)
\xrightarrow{P}
\mathbb{E}[f(X)].
$$

The standard Monte Carlo error typically decreases at the rate:

$$
O\left(\frac{1}{\sqrt{N}}\right).
$$

This rate is largely independent of the dimensionality, which makes Monte Carlo methods attractive for high-dimensional problems.

---

## Variance Reduction

Monte Carlo estimates can be improved using techniques such as:

* **importance sampling**
* **stratified sampling**
* **control variates**
* **antithetic variates**
* **common random numbers**

These methods reduce the variance of the estimator without necessarily increasing the number of samples.

---

## Markov Chain Monte Carlo

When direct sampling is difficult, **Markov Chain Monte Carlo (MCMC)** constructs a Markov chain whose stationary distribution is the desired distribution.

Common algorithms include:

* Metropolis-Hastings
* Gibbs sampling
* Hamiltonian Monte Carlo

MCMC is particularly important in **Bayesian statistics**.

---

## Key Idea

Monte Carlo methods replace difficult analytical calculations with repeated random experiments:

$$
\boxed{
\text{Random Sampling}
\rightarrow
\text{Empirical Average}
\rightarrow
\text{Approximation}
}
$$

Their main advantage is flexibility, especially for **high-dimensional and probabilistic problems**.
