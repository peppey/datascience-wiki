# Skewness

**Skewness** is a statistical measure of the asymmetry of a probability distribution around its mean.

A symmetric distribution has approximately equal behavior on both sides of its center. A skewed distribution has a longer or heavier tail on one side.

Skewness is based on the **third standardized central moment**.

---

## 1. Definition

For a random variable \(X\) with mean \(\mu\) and standard deviation \(\sigma\), skewness is defined as

$$
\operatorname{Skew}(X)
=
\frac{\mathbb{E}[(X-\mu)^3]}{\sigma^3}
$$

The third power is important because it preserves the sign of deviations:

$$
(-2)^3=-8
$$

while

$$
2^3=8.
$$

This means that deviations to the left and right of the mean contribute with opposite signs.

---

## 2. Interpreting the Sign

The sign of skewness describes the direction of the distribution's asymmetry.

### Positive skewness

$$
\operatorname{Skew}(X)>0
$$

The distribution has a relatively long or heavy **right tail**.

This is also called **right-skewed** or **positively skewed**.

Conceptually:

```text
frequency
   │
   │       ███
   │      █████
   │    ███████
   │  █████████
   │████████████████──────→
   └───────────────────────
                         values
```

Examples can include:

* income
* wealth
* waiting times
* insurance claim sizes

A small number of very large observations can pull the mean to the right.

### Negative skewness

$$
\operatorname{Skew}(X)<0
$$

The distribution has a relatively long or heavy **left tail**.

This is also called **left-skewed** or **negatively skewed**.

```text
frequency
   │             ███
   │            █████
   │           ███████
   │       ███████████
   │──────████████████████
   └───────────────────────
                         values
```

Examples can include certain exam scores where most students perform well but a small number perform very poorly.

### Approximately symmetric

$$
\operatorname{Skew}(X)\approx0
$$

A symmetric distribution has skewness of zero.

The normal distribution is an important example:

$$
\operatorname{Skew}(X)=0.
$$

---

## 3. The Tail Determines the Sign

A common source of confusion is the direction of the skew.

The sign is determined by the **tail**, not by the location of the highest point of the distribution.

A useful rule is:

> **The skew points toward the longer tail.**

Therefore:

```text
long right tail → positive skewness
long left tail  → negative skewness
```

The peak of a positively skewed distribution is usually located toward the left, while the long tail extends toward larger values.

---

## 4. Mean, Median and Mode

Skewness often affects the relationship between the mean, median, and mode.

For a moderately **right-skewed** distribution, it is common to observe:

$$
\text{mode} < \text{median} < \text{mean}
$$

For a moderately **left-skewed** distribution:

$$
\text{mean} < \text{median} < \text{mode}
$$

For a symmetric unimodal distribution:

$$
\text{mean}
\approx
\text{median}
\approx
\text{mode}
$$

These relationships are useful heuristics, but they are not universal mathematical rules for all distributions.

---

## 5. Why the Third Power?

Skewness uses the third central moment:

$$
\mathbb{E}[(X-\mu)^3].
$$

Consider observations that are equally far from the mean:

$$
X-\mu=-3
$$

and

$$
X-\mu=3.
$$

Their contributions are:

$$
(-3)^3=-27
$$

and

$$
3^3=27.
$$

The contributions therefore have opposite signs.

This allows skewness to measure **directional asymmetry**.

By contrast, kurtosis uses the fourth power:

$$
(X-\mu)^4
$$

which is always non-negative.

This is one reason skewness and kurtosis capture different properties of a distribution.

---

## 6. Relationship to Moments

Skewness is the **third standardized central moment**.

The first moments are commonly associated with:

| Moment | Related concept |
| ------ | --------------- |
| 1st    | mean            |
| 2nd    | variance        |
| 3rd    | skewness        |
| 4th    | kurtosis        |

More precisely, variance is the second central moment, while skewness and kurtosis are standardized versions of the third and fourth central moments.

The standardization makes skewness dimensionless.

---

## 7. Skewness vs. Kurtosis

Skewness and kurtosis are often discussed together because both describe aspects of distribution shape.

However, they measure different properties.

### Skewness

Measures **asymmetry**.

$$
\text{third standardized moment}
$$

### Kurtosis

Measures the contribution of extreme deviations and tail behavior.

$$
\text{fourth standardized moment}
$$

A distribution can therefore have:

* high positive skewness and low kurtosis
* high positive skewness and high kurtosis
* approximately zero skewness and high kurtosis
* approximately zero skewness and low kurtosis

They should not be treated as interchangeable measures of non-normality.

---

## 8. Examples

### Example 1: Income

Income is often strongly right-skewed.

Most people have incomes within a relatively broad range, while a small number of people have extremely high incomes.

Conceptually:

```text
many observations                few observations
███████████████████
████████████████
██████████
█████
██
█
────────────────────────────────────────→ income
```

The long right tail produces positive skewness.

---

### Example 2: Waiting Times

Suppose a service usually takes between 5 and 15 minutes, but occasionally takes much longer.

The resulting distribution may have:

$$
\text{Skewness} > 0.
$$

The occasional long waiting times create a right tail.

---

### Example 3: Exam Scores

Suppose an exam is relatively easy.

Most students obtain high scores, while a small number perform poorly.

The distribution can therefore have a long left tail:

$$
\text{Skewness} < 0.
$$

---

## 9. Skewness and Outliers

Skewness is sensitive to extreme observations.

Because deviations are cubed, observations far from the mean receive disproportionately large weight.

For example:

```text
10, 11, 10, 12, 11, 10, 11
```

has relatively little asymmetry.

Adding:

```text
100
```

can substantially increase the estimated skewness.

This makes skewness useful for identifying distributions with extreme asymmetric observations.

However, it also means that a single outlier can strongly affect the statistic.

An extreme value should therefore not automatically be removed simply because it increases skewness.

It may represent a valid and important observation.

---

## 10. Skewness Does Not Mean "Bad Data"

A skewed distribution is not necessarily problematic.

Many real-world quantities are naturally skewed.

Examples include:

* income
* population size
* response times
* transaction values
* insurance claims
* biological measurements

The appropriate response depends on the analysis.

For some statistical models, strong skewness may motivate a transformation. For others, it is simply a property of the data that should be modeled explicitly.

---

## 11. Transformations

Transformations can sometimes reduce skewness.

For a positively skewed variable, common transformations include:

### Log transformation

$$
X'=\log(X)
$$

This is particularly useful for positive variables spanning several orders of magnitude.

For example:

```python
import numpy as np

df["log_income"] = np.log(df["income"])
```

For variables that can contain zero:

$$
X'=\log(1+X)
$$

can be used:

```python
df["log_income"] = np.log1p(df["income"])
```

### Square-root transformation

$$
X'=\sqrt{X}
$$

can also reduce positive skewness, especially for count-like data.

### Power transformations

More general transformations such as **Box-Cox** and **Yeo-Johnson** can be used to find a transformation that makes a variable more symmetric.

However, reducing skewness is not automatically desirable. Transformations should be motivated by the modeling task and interpreted carefully.

---

## 12. Skewness and Machine Learning

Many machine-learning algorithms do not require normally distributed input features.

For example, tree-based models such as:

* decision trees
* random forests
* gradient-boosted trees

are generally not strongly affected by the marginal skewness of individual features.

Other methods can be more sensitive to feature distributions.

Examples include models or preprocessing procedures involving:

* linear regression
* distance calculations
* optimization
* regularization
* methods relying on approximately Gaussian variables

Feature scaling and transformations can therefore sometimes improve numerical behavior or model performance.

But there is no universal rule that every skewed feature should be transformed.

---

## 13. Skewness of Model Residuals

Skewness can also be examined for **model residuals**.

Suppose a regression model produces residuals:

$$
e_i=y_i-\hat{y}_i.
$$

Ideally, under some classical regression assumptions, residuals may be expected to have a particular distribution.

Strong residual skewness can indicate that:

* the model is systematically missing structure
* the target transformation may be inappropriate
* extreme observations are present
* the error distribution is asymmetric

However, residual skewness by itself does not tell you exactly which problem is present.

Residual plots and Q-Q plots should be used alongside numerical diagnostics.

---

## 14. Sample Skewness

The population definition is:

$$
\gamma_1
=
\frac{\mathbb{E}[(X-\mu)^3]}{\sigma^3}.
$$

For a sample, skewness has to be estimated.

A simple moment estimator is:

$$
g_1
=
\frac{m_3}{m_2^{3/2}}
$$

where

$$
m_k=
\frac{1}{n}
\sum_{i=1}^{n}(x_i-\bar{x})^k.
$$

Different statistical software may use different estimators or bias corrections.

For example, a bias-corrected sample skewness is often written as:

$$
G_1
=
\frac{\sqrt{n(n-1)}}{n-2}g_1.
$$

Therefore, small numerical differences between statistical packages can occur.

When reproducibility matters, specify which estimator is being used.

---

## 15. Skewness in Python

Using pandas:

```python
skewness = df["value"].skew()
print(skewness)
```

This calculates the sample skewness using pandas' convention.

SciPy provides:

```python
from scipy.stats import skew

skewness = skew(df["value"])
print(skewness)
```

SciPy also allows the choice of bias correction:

```python
skew(df["value"], bias=True)
```

or:

```python
skew(df["value"], bias=False)
```

Always check the library's documentation when comparing results from different implementations.

---

## 16. Visualizing Skewness

A histogram is often the simplest way to inspect skewness:

```python
import matplotlib.pyplot as plt

plt.hist(df["value"], bins=30)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

A density plot or box plot can also be useful.

For a more complete assessment, combine:

* histogram
* box plot
* mean
* median
* skewness
* relevant domain knowledge

A numerical skewness value without seeing the underlying distribution can be difficult to interpret.

---

## 17. Skewness and Normality

The normal distribution has:

$$
\operatorname{Skew}(X)=0.
$$

However, skewness close to zero does **not** prove that a distribution is normal.

A distribution can be symmetric but:

* multimodal
* heavy-tailed
* light-tailed
* otherwise very different from a normal distribution

For example, kurtosis may differ substantially from the normal distribution even when skewness is zero.

Normality should therefore be assessed using several diagnostics, such as:

* histogram
* Q-Q plot
* skewness
* kurtosis
* formal tests
* domain knowledge

---

## 18. Skewness and Bounded Variables

Some variables are naturally bounded.

For example:

```text
probability: 0 ≤ p ≤ 1
exam score: 0 ≤ score ≤ 100
```

The possible range can create asymmetry.

If most observations are close to an upper or lower boundary, the distribution may become strongly skewed.

This is an important reminder that skewness is not necessarily caused by unusual data—it can arise naturally from the structure of the variable.

---

## 19. Common Mistakes

### Mistake 1: "Positive skew means most values are positive"

No.

Positive skewness means that the distribution has greater asymmetry toward the **right tail**.

A variable can contain mostly negative values and still be positively skewed.

### Mistake 2: "The mean is always greater than the median when skewness is positive"

This is a useful heuristic for many unimodal distributions, but it is not a universal rule.

### Mistake 3: "Skewness should always be zero"

No.

Many real-world variables are naturally skewed.

### Mistake 4: "Skewed data must be transformed"

Not necessarily.

Whether a transformation is useful depends on the analysis and the model.

### Mistake 5: "Zero skewness means the distribution is normal"

It does not.

Zero skewness only describes one aspect of the distribution's shape.

### Mistake 6: Removing outliers because they increase skewness

An extreme observation may be a valid and important part of the population.

Investigate the observation before deciding what to do with it.

---

## 20. Practical Workflow

When analyzing a numerical variable:

1. Plot the distribution.
2. Calculate the mean and median.
3. Calculate skewness.
4. Inspect extreme observations.
5. Consider whether the skewness is expected from the domain.
6. Decide whether the skewness matters for the chosen model.
7. Only then consider a transformation.

For example:

```python
import matplotlib.pyplot as plt

x = df["value"]

print("Mean:", x.mean())
print("Median:", x.median())
print("Skewness:", x.skew())

plt.hist(x, bins=30)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

The combination of numerical and visual diagnostics is generally more informative than skewness alone.

---

## 21. Summary

Skewness measures the **asymmetry of a probability distribution**.

It is based on the third standardized central moment:

$$
\operatorname{Skew}(X)
=
\frac{\mathbb{E}[(X-\mu)^3]}{\sigma^3}.
$$

Key points:

* positive skewness → longer or heavier right tail
* negative skewness → longer or heavier left tail
* approximately zero skewness → approximately symmetric distribution
* skewness is sensitive to extreme observations
* the sign refers to the direction of the tail, not the location of the peak
* skewness and kurtosis measure different aspects of distribution shape
* skewed data are not necessarily problematic
* transformations can sometimes reduce skewness, but are not automatically required
* zero skewness does not imply normality
* sample skewness depends on the estimator and bias correction used

The most useful practical rule is:

> **Look at the distribution before interpreting its skewness, and treat skewness as a description of the data—not automatically as a problem that needs to be fixed.**
