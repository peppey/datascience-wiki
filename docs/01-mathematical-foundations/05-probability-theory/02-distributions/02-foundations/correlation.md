# Correlation

## TL;DR

**Correlation** measures the strength and direction of the relationship between two random variables.

The most common measure is the **Pearson correlation coefficient**:

$$
\rho_{X,Y}
=
\frac{\operatorname{Cov}(X,Y)}
{\sigma_X\sigma_Y}
$$

It ranges from $-1$ to $1$.

---

## Pearson Correlation

For random variables $X$ and $Y$:

$$
\rho_{X,Y}
=
\frac{\operatorname{Cov}(X,Y)}
{\sigma_X\sigma_Y}
$$

where:

- $\operatorname{Cov}(X,Y)$ is the covariance
- $\sigma_X$ is the standard deviation of $X$
- $\sigma_Y$ is the standard deviation of $Y$

For a sample, the correlation coefficient is usually denoted by $r$:

$$
r
=
\frac{\sum_i(x_i-\bar{x})(y_i-\bar{y})}
{\sqrt{\sum_i(x_i-\bar{x})^2}
\sqrt{\sum_i(y_i-\bar{y})^2}}
$$

---

## Interpretation

The value of the correlation indicates the direction and strength of a **linear relationship**.

| Correlation | Interpretation |
|---|---|
| $\rho=1$ | Perfect positive linear relationship |
| $\rho\approx1$ | Strong positive relationship |
| $\rho\approx0$ | Little or no linear relationship |
| $\rho\approx-1$ | Strong negative relationship |
| $\rho=-1$ | Perfect negative linear relationship |

A positive correlation means that larger values of one variable tend to be associated with larger values of the other.

A negative correlation means that larger values of one variable tend to be associated with smaller values of the other.

---

## Covariance vs. Correlation

**Covariance** measures whether two variables vary together:

$$
\operatorname{Cov}(X,Y)
=
\mathbb{E}[(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])]
$$

However, covariance depends on the units and scale of the variables.

Correlation normalizes covariance:

$$
\rho_{X,Y}
=
\frac{\operatorname{Cov}(X,Y)}
{\sigma_X\sigma_Y}
$$

Therefore, correlation is **dimensionless** and always lies between $-1$ and $1$.

---

## Correlation and Independence

If two variables are independent, then:

$$
\rho_{X,Y}=0
$$

However, the converse is generally **not true**.

Zero correlation only means that there is no **linear** relationship. Variables can still have a strong nonlinear relationship.

For example:

$$
Y=X^2
$$

can have zero correlation with $X$ for certain symmetric distributions, despite being completely determined by $X$.

---

## Correlation Does Not Imply Causation

A correlation between two variables does not imply that one causes the other.

A correlation may arise because:

- $X$ causes $Y$
- $Y$ causes $X$
- a third variable influences both
- the relationship is coinc