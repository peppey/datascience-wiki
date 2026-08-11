# Efficiency

## TL;DR

In statistics, **efficiency** describes how precisely an estimator estimates an unknown parameter.

For unbiased estimators, an estimator with **lower variance** is generally considered more efficient.

---

## Relative Efficiency

Suppose $\hat{\theta}_1$ and $\hat{\theta}_2$ are two unbiased estimators of the same parameter $\theta$.

The **relative efficiency** of $\hat{\theta}_1$ compared with $\hat{\theta}_2$ can be defined as:

$$
\operatorname{Eff}(\hat{\theta}_1,\hat{\theta}_2)
=

\frac{\operatorname{Var}(\hat{\theta}_2)}
{\operatorname{Var}(\hat{\theta}_1)}.
$$

If this value is greater than $1$, $\hat{\theta}_1$ has lower variance and is therefore more efficient.

---

## Efficient Estimator

An estimator is **efficient** if it achieves the smallest possible variance among a specified class of estimators.

For an unbiased estimator, a common benchmark is the **Cramér-Rao lower bound**:

$$
\operatorname{Var}(\hat{\theta})
\geq
\frac{1}{I(\theta)}
$$

where $I(\theta)$ is the **Fisher information**.

An unbiased estimator that reaches this bound is called **efficient**.

---

## Example

Suppose two unbiased estimators estimate the same parameter:

$$
\operatorname{Var}(\hat{\theta}_1)=2
$$

and

$$
\operatorname{Var}(\hat{\theta}_2)=5.
$$

Then $\hat{\theta}_1$ is more efficient because it has lower variance.

Its estimates tend to fluctuate less between different samples.

---

## Efficiency vs. Bias

Efficiency is often discussed for **unbiased estimators**, where lower variance directly means greater efficiency.

For biased estimators, variance alone is not sufficient. The **mean squared error (MSE)** is often more useful:

$$
\operatorname{MSE}(\hat{\theta})
=

\operatorname{Bias}(\hat{\theta})^2
+
\operatorname{Var}(\hat{\theta}).
$$

A slightly biased estimator can therefore be preferable if its reduction in variance leads to a lower MSE.

---

## Key Idea

An efficient estimator extracts as much information as possible from the available data.

For unbiased estimators:

$$
\boxed{
\text{Higher efficiency}
;\Longleftrightarrow;
\text{Lower variance}
}
$$

Efficiency is closely related to **variance, Fisher information, and the Cramér-Rao lower bound**.
