# Kurtosis

**Kurtosis** is a statistical measure that describes aspects of the shape of a probability distribution, particularly the behavior of its tails.

It is the standardized fourth central moment of a random variable.

Kurtosis is often introduced as a measure of "tailedness", although it is also commonly—and somewhat misleadingly—described as a measure of the "peakedness" of a distribution.

---

## 1. Definition

For a random variable \(X\) with mean \(\mu\) and standard deviation \(\sigma\), kurtosis is defined as

$$
\operatorname{Kurt}(X)
=
\frac{\mathbb{E}[(X-\mu)^4]}{\sigma^4}
$$

The fourth power means that large deviations from the mean receive much greater weight than small deviations.

For a sample, the corresponding empirical quantity is based on

$$
\frac{1}{n}
\sum_{i=1}^{n}
\left(
\frac{x_i-\bar{x}}{s}
\right)^4
$$

with the exact sample estimator depending on the statistical convention being used.

---

## 2. Why the Fourth Power?

Compare the contribution of different standardized deviations:

$$
1^4 = 1
$$

$$
2^4 = 16
$$

$$
3^4 = 81
$$

$$
4^4 = 256
$$

Because deviations are raised to the fourth power, observations far from the mean have a disproportionately large influence on kurtosis.

This makes kurtosis particularly sensitive to **extreme observations and heavy tails**.

---

## 3. Kurtosis of the Normal Distribution

The normal distribution has a kurtosis of

$$
3.
$$

This value is used as a reference point.

A distribution can therefore be classified as:

* **mesokurtic**: kurtosis approximately \(3\)
* **leptokurtic**: kurtosis greater than \(3\)
* **platykurtic**: kurtosis less than \(3\)

However, statistical software often reports **excess kurtosis** rather than kurtosis itself.

---

## 4. Excess Kurtosis

**Excess kurtosis** is defined as

$$
\operatorname{ExcessKurt}(X)
=
\operatorname{Kurt}(X)-3
$$

The normal distribution therefore has:

$$
\operatorname{ExcessKurt}=0
$$

This gives the commonly used interpretation:

| Excess kurtosis | Interpretation                             |
| --------------: | ------------------------------------------ |
|          \(>0\) | heavier tails than the normal distribution |
|          \(=0\) | same kurtosis as the normal distribution   |
|          \(<0\) | lighter tails than the normal distribution |

The terminology is important because "kurtosis = 0" and "excess kurtosis = 0" mean very different things.

---

## 5. Kurtosis vs. Excess Kurtosis

The two quantities are simply shifted by 3:

$$
K = 3 + K_{\text{excess}}
$$

For example:

| Distribution                  | Kurtosis | Excess kurtosis |
| ----------------------------- | -------: | --------------: |
| Normal                        |        3 |               0 |
| Uniform                       |      1.8 |            -1.2 |
| Distribution with heavy tails |       >3 |              >0 |

When reporting kurtosis, always check which convention is being used.

Many statistical libraries return **excess kurtosis** by default.

---

## 6. What Does Kurtosis Actually Measure?

A common explanation is:

> "Kurtosis measures how peaked a distribution is."

This is not a particularly good interpretation.

Kurtosis is mathematically related to the **fourth moment** and is especially sensitive to observations far from the mean.

A better practical interpretation is:

> **Kurtosis describes how strongly a distribution's fourth moment is influenced by extreme deviations, relative to a reference distribution such as the normal distribution.**

High kurtosis is generally associated with **heavier tails and more extreme observations**.

However, kurtosis is a global summary statistic and does not uniquely determine the shape of the distribution.

---

## 7. Heavy Tails

A distribution has **heavy tails** when extreme values occur more frequently than they would under a light-tailed reference distribution such as the normal distribution.

For example, financial returns often exhibit more extreme observations than a normal distribution would predict.

A distribution with heavy tails can therefore have high kurtosis.

Conceptually:

```text
Normal distribution
        │
        ├── relatively few extreme observations
        │
Heavy-tailed distribution
        │
        └── more extreme observations
```

High kurtosis can therefore be particularly relevant when analyzing data where rare extreme events matter.

---

## 8. Low Kurtosis

A distribution with low kurtosis has less contribution from extreme deviations than the normal distribution.

A standard example is the uniform distribution.

For a continuous uniform distribution,

$$
X \sim U(a,b)
$$

the kurtosis is

$$
\frac{9}{5}=1.8
$$

and the excess kurtosis is

$$
-1.2.
$$

The distribution has relatively light tails compared with the normal distribution.

---

## 9. Kurtosis and Outliers

Because deviations are raised to the fourth power, kurtosis is highly sensitive to outliers.

Suppose a dataset contains:

```text
10, 11, 10, 12, 11, 10, 11
```

and one extreme observation is added:

```text
10, 11, 10, 12, 11, 10, 11, 100
```

The extreme observation can have a very large effect on the kurtosis.

This makes kurtosis useful when investigating whether a dataset contains unusually extreme observations.

However, it also means that the estimated kurtosis can be unstable in small samples.

---

## 10. Kurtosis Does Not Tell You Everything About the Distribution

Two distributions can have the same kurtosis while having very different shapes.

Kurtosis is only one number summarizing one aspect of a distribution.

It does not tell you:

* whether the distribution is symmetric
* whether it is unimodal or multimodal
* where the modes are
* whether it is skewed
* whether there are distinct subpopulations

For example, **skewness** measures asymmetry, whereas kurtosis is related to the fourth central moment.

Therefore, kurtosis should generally be interpreted together with other descriptive statistics and visualizations.

---

## 11. Kurtosis vs. Skewness

Skewness and kurtosis both describe aspects of a distribution's shape, but they measure different things.

### Skewness

Skewness is based on the **third central moment**:

$$
\operatorname{Skew}(X)
=
\frac{\mathbb{E}[(X-\mu)^3]}{\sigma^3}
$$

It measures asymmetry.

### Kurtosis

Kurtosis is based on the **fourth central moment**:

$$
\operatorname{Kurt}(X)
=
\frac{\mathbb{E}[(X-\mu)^4]}{\sigma^4}
$$

It is particularly sensitive to extreme deviations.

In simplified terms:

```text
Skewness → asymmetry
Kurtosis → influence of extreme deviations / tail behavior
```

A distribution can therefore be:

* symmetric with high kurtosis
* symmetric with low kurtosis
* skewed with high kurtosis
* skewed with low kurtosis

These are separate properties.

---

## 12. Relationship to Moments

Kurtosis is the **fourth standardized central moment**.

The first four central moments are commonly described as:

| Moment | Description                         |
| ------ | ----------------------------------- |
| 1st    | mean-related / zero after centering |
| 2nd    | variance                            |
| 3rd    | skewness                            |
| 4th    | kurtosis                            |

More precisely, variance is the second central moment, while skewness and kurtosis are standardized versions of the third and fourth central moments.

The fourth moment gives greater weight to large deviations than the second moment because of the fourth power.

---

## 13. Kurtosis in Python

Using pandas:

```python
import pandas as pd

kurtosis = df["value"].kurt()
print(kurtosis)
```

Pandas returns **Fisher's definition of kurtosis**, i.e. excess kurtosis.

Therefore:

```text
0
```

corresponds approximately to the kurtosis of a normal distribution.

SciPy also provides functions for calculating kurtosis:

```python
from scipy.stats import kurtosis

kurtosis(df["value"])
```

SciPy's default also returns excess kurtosis.

The `fisher` parameter can be used to choose between excess kurtosis and ordinary kurtosis:

```python
kurtosis(df["value"], fisher=True)
```

returns excess kurtosis, while:

```python
kurtosis(df["value"], fisher=False)
```

returns ordinary kurtosis.

Always check the definition used by the library before interpreting the result.

---

## 14. Example

Consider three distributions:

```text
Distribution A:
approximately normal

Distribution B:
heavy-tailed

Distribution C:
light-tailed
```

Their excess kurtosis might look approximately like:

| Distribution | Excess kurtosis |
| ------------ | --------------: |
| A            |               0 |
| B            |             2.5 |
| C            |            -1.0 |

This suggests that:

* A has approximately normal kurtosis
* B has substantially heavier tails
* C has lighter tails

The exact value should not be interpreted independently of the sample size and the underlying distribution.

---

## 15. Why Kurtosis Matters in Data Science

Kurtosis can be useful during exploratory data analysis.

A high kurtosis may indicate that a variable contains more extreme observations than expected under a normal reference model.

This can matter for:

### Outlier analysis

Extreme observations may require investigation.

They could represent:

* genuine rare events
* measurement errors
* data-entry errors
* unusual but valid cases

### Financial data

Asset returns often exhibit heavy tails, meaning that extreme changes occur more frequently than a normal model would suggest.

### Risk analysis

When extreme events matter, assuming a normal distribution can underestimate tail risk.

### Statistical modeling

Some statistical methods make assumptions about the distribution of residuals or errors.

Strongly non-normal residuals may therefore motivate further investigation.

---

## 16. Kurtosis and Normality

Kurtosis can be used as one component of assessing whether data are approximately normally distributed.

A normal distribution has:

$$
\text{excess kurtosis}=0
$$

However, a kurtosis close to zero does **not** prove that the data are normally distributed.

Likewise, a nonzero kurtosis does not necessarily make a statistical model invalid.

Normality should be assessed using multiple pieces of evidence, such as:

* histograms
* Q-Q plots
* skewness
* kurtosis
* formal normality tests
* domain knowledge

A Q-Q plot is often much more informative than looking at kurtosis alone.

---

## 17. Sample Kurtosis

The theoretical definition applies to a probability distribution.

For a finite sample, kurtosis has to be **estimated**.

Different estimators exist, and they can differ in their treatment of:

* sample size
* bias correction
* normalization
* whether ordinary or excess kurtosis is reported

For example, some implementations use a bias-corrected estimator.

Therefore, two statistical packages can sometimes produce slightly different results for the same dataset.

When reproducibility matters, specify the definition or estimator being used.

---

## 18. Limitations

Kurtosis is useful, but it should not be overinterpreted.

### It is sensitive to outliers

A small number of extreme observations can strongly affect the estimate.

### It requires sufficient data

Estimates can be unstable for small samples.

### It does not uniquely describe a distribution

Different distributions can have the same kurtosis.

### It does not directly measure "peakedness"

The common peakedness interpretation can be misleading.

### It does not establish normality

A kurtosis value near the normal reference value does not prove that a dataset is normally distributed.

---

## 19. Practical Workflow

When analyzing a numerical variable, a useful workflow is:

1. Plot the distribution.
2. Check for obvious data-quality problems.
3. Calculate summary statistics.
4. Calculate skewness and kurtosis.
5. Inspect extreme observations.
6. Consider whether the tails are relevant to the analysis.
7. Use an appropriate statistical model rather than relying on kurtosis alone.

For example:

```python
import matplotlib.pyplot as plt

x = df["value"]

print("Skewness:", x.skew())
print("Excess kurtosis:", x.kurt())

plt.hist(x, bins=30)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

The numerical values become much more informative when combined with the visualization.

---

## 20. Summary

Kurtosis is the **fourth standardized central moment** of a distribution:

$$
\operatorname{Kurt}(X)
=
\frac{\mathbb{E}[(X-\mu)^4]}{\sigma^4}
$$

The normal distribution has a kurtosis of \(3\), or an excess kurtosis of \(0\).

Key points:

* kurtosis is highly sensitive to extreme observations
* high kurtosis is generally associated with heavier tails
* low kurtosis is generally associated with lighter tails
* excess kurtosis subtracts \(3\) from ordinary kurtosis
* the normal distribution has excess kurtosis \(0\)
* kurtosis is different from skewness
* kurtosis does not simply measure "peakedness"
* zero excess kurtosis does not prove normality
* kurtosis can be useful for detecting unusual tail behavior
* sample kurtosis depends on the estimator and convention used

The most important practical principle is:

> **Use kurtosis as one descriptive statistic among several, and interpret it together with the actual distribution and its extreme observations.**
