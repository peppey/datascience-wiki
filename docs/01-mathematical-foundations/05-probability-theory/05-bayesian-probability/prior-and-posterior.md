# Prior and Posterior

## TL;DR

In **Bayesian inference**, the **prior** represents what is believed about an unknown quantity before observing data, while the **posterior** represents the updated belief after observing data.

Bayes' theorem connects them:

$$
p(\theta\mid D)
=

\frac{p(D\mid\theta)p(\theta)}
{p(D)}
$$

where:

* $p(\theta)$ — **prior**
* $p(D\mid\theta)$ — **likelihood**
* $p(\theta\mid D)$ — **posterior**
* $p(D)$ — **evidence** or **marginal likelihood**

## Prior

The **prior distribution** describes assumptions or knowledge about a parameter $\theta$ before observing the data:

$$
p(\theta)
$$

For example, before observing any data, we might believe that a parameter is likely to be close to zero.

Priors can incorporate previous experiments, domain knowledge, or other assumptions.

## Posterior

After observing data $D$, the prior is updated using the likelihood:

$$
p(\theta\mid D)
\propto
p(D\mid\theta)p(\theta).
$$

The resulting distribution is the **posterior distribution**.

It represents our updated uncertainty about $\theta$ after taking the observed data into account.

## Bayesian Updating

The Bayesian workflow can be summarized as:

$$
\boxed{
\text{Prior}
+
\text{Data}
\rightarrow
\text{Posterior}
}
$$

More precisely:

$$
p(\theta)
\xrightarrow{\text{observe }D}
p(\theta\mid D).
$$

As more data becomes available, the posterior can be used as the prior for the next update.

## Example

Suppose $\theta$ represents the probability that a coin lands heads.

Before observing any flips, we specify a prior:

$$
\theta\sim\operatorname{Beta}(\alpha,\beta).
$$

After observing $h$ heads and $t$ tails, the posterior is:

$$
\theta\mid D
\sim
\operatorname{Beta}(\alpha+h,\beta+t).
$$

The posterior therefore combines the initial assumption with the observed evidence.

## Prior vs. Posterior

|                          | Prior           | Posterior       |
| ------------------------ | --------------- | --------------- |
| Before data              | ✓               |                 |
| After data               |                 | ✓               |
| Represents               | Initial beliefs | Updated beliefs |
| Depends on observed data | No              | Yes             |

The **posterior** is the central object in Bayesian inference and can be used to make predictions, estimate parameters, and quantify uncertainty.
