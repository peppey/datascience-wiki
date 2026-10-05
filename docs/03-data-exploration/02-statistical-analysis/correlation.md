# Correlation

**Correlation** describes the statistical relationship between two variables. It measures whether changes in one variable tend to be associated with changes in another.

For example, height and weight often have a positive correlation: taller people tend to weigh more.

Correlation is about **association**, not causation. A strong correlation between two variables does not by itself tell us that one variable causes the other.

---

## 1. What Does Correlation Measure?

Consider two variables \(X\) and \(Y\).

If large values of \(X\) tend to occur together with large values of \(Y\), the variables have a **positive correlation**.

If large values of \(X\) tend to occur together with small values of \(Y\), they have a **negative correlation**.

If there is no systematic relationship, the correlation is close to zero.

The strength of a correlation is usually expressed by a number between \(-1\) and \(1\):

$$
-1 \leq r \leq 1
$$

where:

* \(r = 1\): perfect positive linear correlation
* \(r = -1\): perfect negative linear correlation
* \(r = 0\): no linear correlation

Values closer to \(-1\) or \(1\) indicate stronger **linear** association.

---

## 2. Pearson Correlation

The most common correlation coefficient is the **Pearson correlation coefficient**.

For two variables \(X\) and \(Y\):

$$
r =
\frac{\operatorname{cov}(X,Y)}
{\sigma_X \sigma_Y}
$$

where:

* \(\operatorname{cov}(X,Y)\) is the covariance between \(X\) and \(Y\)
* \(\sigma_X\) is the standard deviation of \(X\)
* \(\sigma_Y\) is the standard deviation of \(Y\)

For \(n\) observations, this can also be written as:

$$
r =
\frac{
\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})
}{
\sqrt{\sum_{i=1}^{n}(x_i-\bar{x})^2}
\sqrt{\sum_{i=1}^{n}(y_i-\bar{y})^2}
}
$$

The numerator measures how the two variables vary together, while the denominator normalizes the result by their variability.

---

## 3. Interpreting the Sign

The **sign** of the correlation indicates its direction.

### Positive correlation

$$
r > 0
$$

Higher values of one variable tend to be associated with higher values of the other.

Example:

```text
study time ↑  →  exam score ↑
```

### Negative correlation

$$
r < 0
$$

Higher values of one variable tend to be associated with lower values of the other.

Example:

```text
price ↑  →  demand ↓
```

### No linear correlation

$$
r \approx 0
$$

There is no substantial **linear** relationship between the variables.

Importantly, this does **not** necessarily mean that the variables are independent or unrelated.

---

## 4. Strength of Correlation

There is no universally correct set of thresholds for describing a correlation as "weak" or "strong".

As a rough heuristic, one might use the absolute value:

| \(|r|\) | Approximate interpretation |
|---:|---|
| 0–0.2 | very weak |
| 0.2–0.4 | weak |
| 0.4–0.6 | moderate |
| 0.6–0.8 | strong |
| 0.8–1.0 | very strong |

These thresholds are context-dependent.

A correlation of \(r=0.4\) may be highly informative in one scientific field and relatively weak in another.

It is therefore usually better to report the actual correlation coefficient rather than relying only on labels such as "strong".

---

## 5. Correlation and Covariance

Correlation is closely related to **covariance**.

Covariance measures whether two variables tend to deviate from their means in the same direction:

$$
\operatorname{cov}(X,Y)
=
\frac{1}{n-1}
\sum_{i=1}^{n}
(x_i-\bar{x})(y_i-\bar{y})
$$

Positive covariance means that the variables tend to increase and decrease together.

Negative covariance means that they tend to move in opposite directions.

However, covariance depends on the units of the variables.

For example, changing a variable from meters to centimeters changes its covariance with another variable.

Correlation removes this dependence on scale by standardizing covariance:

$$
r =
\frac{\operatorname{cov}(X,Y)}
{\sigma_X\sigma_Y}
$$

Therefore, correlation is **unitless** and always lies between \(-1\) and \(1\).

---

## 6. Pearson vs. Spearman Correlation

Pearson correlation is not the only measure of correlation.

Two important alternatives are **Spearman's rank correlation** and **Kendall's rank correlation**.

### Pearson correlation

Pearson correlation measures the strength of a **linear relationship** between two numerical variables.

It is sensitive to:

* outliers
* nonlinear relationships
* assumptions about the data-generating process in statistical inference

### Spearman correlation

Spearman's rank correlation first replaces the observations with their ranks and then computes the correlation of those ranks.

It measures whether there is a **monotonic relationship** between two variables.

A monotonic relationship consistently moves in one direction, but does not have to be linear.

For example:

$$
Y = X^2
$$

is nonlinear. If \(X\) is restricted to positive values, however, \(Y\) still increases monotonically with \(X\).

Spearman correlation can therefore detect relationships that Pearson correlation may not capture well.

### Kendall's tau

Kendall's tau is another rank-based measure.

It is based on the relative ordering of pairs of observations and is particularly useful for ordinal data and smaller datasets.

---

## 7. Pearson vs. Spearman: Example

Consider a relationship like:

$$
Y = X^2
$$

for positive \(X\).

The relationship is clearly systematic and monotonic, but it is nonlinear.

Pearson correlation measures how closely the points follow a straight line.

Spearman correlation instead considers their ranks and can therefore capture the monotonic relationship more directly.

This illustrates an important principle:

> **A correlation coefficient always measures a particular kind of relationship.**

A correlation close to zero does not necessarily mean that there is no relationship.

---

## 8. Correlation Does Not Imply Causation

One of the most important principles in statistics is:

> **Correlation does not imply causation.**

Suppose ice cream sales and the number of sunburn cases are positively correlated.

This does not mean that eating ice cream causes sunburn.

A more plausible explanation is a **confounding variable**:

```text
              Temperature
              /          \
             ↓            ↓
      Ice cream sales   Sunburns
```

Hot weather increases both ice cream consumption and time spent in the sun.

The correlation between ice cream sales and sunburns is therefore partly explained by temperature.

### Three possibilities

When two variables are correlated, several explanations are possible:

1. \(X\) causes \(Y\)
2. \(Y\) causes \(X\)
3. a third variable causes both

There can also be more complicated causal structures.

Correlation alone cannot distinguish these possibilities.

---

## 9. Confounding Variables

A **confounder** is a variable that is associated with both variables being studied and can create or distort their apparent relationship.

For example:

```text
Education ───────→ Income
     ↑
     │
Socioeconomic background
```

If socioeconomic background affects both education and income, simply observing a correlation between education and income does not establish the complete causal mechanism.

Confounding is especially important in observational studies.

Methods such as:

* randomized experiments
* stratification
* regression adjustment
* matching
* instrumental variables
* causal graphs

can be used to investigate causal relationships more rigorously.

---

## 10. Correlation Is Not the Same as Independence

For general variables:

$$
r = 0
$$

does **not** imply statistical independence.

Two variables can have zero Pearson correlation while still having a strong nonlinear relationship.

For example, let:

$$
Y = X^2
$$

and suppose \(X\) is symmetrically distributed around zero.

Large positive and negative values of \(X\) both produce large values of \(Y\). The linear correlation can therefore be close to zero even though \(Y\) is completely determined by \(X\).

Independence is a much stronger condition:

$$
X \perp Y
$$

If two variables are independent, their Pearson correlation is zero (assuming the correlation exists).

The converse is generally not true.

---

## 11. Correlation and Nonlinear Relationships

Correlation coefficients can be misleading when the relationship is nonlinear.

Consider:

```text
        •       •
      •           •
    •               •
      •           •
        •       •
```

The variables clearly have a relationship, but it is not linear.

Pearson correlation may be close to zero.

Therefore, correlation should generally be accompanied by a **visual inspection of the data**, especially a scatter plot.

A useful workflow is:

1. calculate the correlation
2. plot the variables
3. inspect the relationship
4. investigate potential outliers
5. consider whether a nonlinear relationship is plausible

---

## 12. Outliers

Correlation can be strongly affected by outliers.

Consider a dataset with a moderate relationship:

```text
      •
    • •
   •  •
  •   •
```

Adding one extreme observation can substantially increase or decrease Pearson's correlation.

Therefore, a large correlation coefficient may sometimes be driven primarily by a small number of observations.

Scatter plots are useful for identifying this problem.

Robust or rank-based methods such as Spearman correlation can sometimes be more appropriate when extreme observations are present, although rank-based methods are not automatically immune to all outlier problems.

---

## 13. Correlation Matrices

When a dataset contains many numerical variables, correlations can be calculated pairwise.

For example:

|          |   Age | Income | Spending |  Debt |
| -------- | ----: | -----: | -------: | ----: |
| Age      |  1.00 |   0.42 |     0.18 | -0.21 |
| Income   |  0.42 |   1.00 |     0.57 |  0.31 |
| Spending |  0.18 |   0.57 |     1.00 | -0.05 |
| Debt     | -0.21 |   0.31 |    -0.05 |  1.00 |

This is called a **correlation matrix**.

The diagonal is always:

$$
r(X,X)=1
$$

because every variable is perfectly correlated with itself.

The matrix is symmetric:

$$
r(X,Y)=r(Y,X)
$$

Therefore, the upper and lower triangles contain the same information.

Correlation matrices are frequently visualized as **heatmaps**.

---

## 14. Correlation in Feature Analysis

Correlation is commonly used during exploratory data analysis and feature engineering.

For example, suppose a dataset contains:

```text
age
income
number_of_purchases
customer_lifetime_value
```

A correlation matrix can reveal potentially interesting relationships.

Highly correlated features can sometimes indicate **multicollinearity**.

For example:

$$
\operatorname{corr}(X_1,X_2)=0.95
$$

means that \(X_1\) and \(X_2\) contain very similar linear information.

This can be problematic for some models, particularly linear regression.

However, high feature correlation does **not** automatically mean that one feature should be removed.

The decision depends on:

* the model
* the purpose of the analysis
* interpretability requirements
* predictive performance
* domain knowledge

Tree-based models, for example, generally handle correlated features differently from linear models.

---

## 15. Correlation with the Target

A common feature-selection technique is to calculate the correlation between numerical features and a numerical target.

For example:

```python
df.corr(numeric_only=True)["target"]
```

This can be useful for exploratory analysis.

However, selecting features solely based on their correlation with the target has important limitations.

A feature can have:

* low linear correlation but strong nonlinear predictive power
* high correlation due to data leakage
* high correlation caused by a confounder
* high correlation in the training data but not in new data

Therefore, correlation should be treated as an **exploratory diagnostic**, not as a complete feature-selection method.

---

## 16. Correlation and Data Leakage

A surprisingly high correlation can sometimes be a warning sign.

Suppose a model is supposed to predict whether a company will be visited in the future.

If a feature records information that only becomes available **after the visit**, that feature may be strongly associated with the target.

The correlation may look useful during development while actually representing **data leakage**.

This is why correlations should always be interpreted in the context of:

* when the data was generated
* when the feature became available
* what the prediction task is
* what information would actually be available at prediction time

A high correlation is not automatically a good feature.

---

## 17. Statistical Significance

When estimating a correlation from a sample, we may want to know whether the observed association could plausibly have arisen by chance.

A statistical test can be used to test:

$$
H_0: \rho = 0
$$

where \(\rho\) is the population correlation.

The resulting **p-value** measures how incompatible the observed data are with the null hypothesis under the assumptions of the test.

However:

> **Statistical significance is not the same as practical significance.**

With a sufficiently large dataset, even a very small correlation can have a very small p-value.

Therefore, it is important to report the **effect size** (the correlation coefficient) alongside uncertainty or statistical significance.

---

## 18. Correlation vs. Regression

Correlation and regression are closely related but answer different questions.

**Correlation** asks:

> How strongly are \(X\) and \(Y\) associated?

**Regression** asks:

> How does \(Y\) change as a function of \(X\), and can we use \(X\) to predict \(Y\)?

For simple linear regression:

$$
Y = \beta_0 + \beta_1X + \epsilon
$$

the slope \(\beta_1\) describes the expected change in \(Y\) for a one-unit change in \(X\).

Correlation is symmetric:

$$
r(X,Y)=r(Y,X)
$$

Regression is not.

Regressing \(Y\) on \(X\) is a different model from regressing \(X\) on \(Y\).

---

## 19. Practical Example in Python

Pearson correlation can be calculated with pandas:

```python
import pandas as pd

correlation = df["height"].corr(df["weight"])
print(correlation)
```

By default, pandas uses Pearson correlation.

Spearman correlation can be calculated with:

```python
correlation = df["height"].corr(
    df["weight"],
    method="spearman",
)
```

A correlation matrix can be calculated with:

```python
correlation_matrix = df.corr(numeric_only=True)
```

For a visual inspection, a scatter plot is often useful:

```python
import matplotlib.pyplot as plt

plt.scatter(df["height"], df["weight"])
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()
```

The numerical correlation should be interpreted together with the visualization.

---

## 20. Common Mistakes

### Mistake 1: "High correlation means causation"

It does not.

A confounding variable or reverse causality may explain the relationship.

### Mistake 2: "Zero correlation means no relationship"

Not necessarily.

The relationship may simply be nonlinear.

### Mistake 3: Looking only at the correlation coefficient

Always consider the underlying data, sample size, outliers, and visualization.

### Mistake 4: Treating encoded categories as numerical variables

If:

```text
Germany = 1
France = 2
Italy = 3
```

then calculating Pearson correlation on these codes generally has no meaningful interpretation.

### Mistake 5: Assuming correlation is stable

A relationship observed in one dataset or time period may not hold in another.

Correlation can change because of:

* population changes
* distribution shifts
* temporal effects
* measurement changes
* interventions

### Mistake 6: Interpreting statistical significance as importance

A statistically significant correlation can still be practically negligible.

---

## 21. Summary

Correlation measures the degree to which two variables are associated.

The most common measure, **Pearson correlation**, measures linear association and ranges from \(-1\) to \(1\).

Key concepts:

* \(r>0\): positive linear association
* \(r<0\): negative linear association
* \(r\approx0\): little or no linear association
* correlation is unitless
* covariance is related to correlation but depends on scale
* Spearman and Kendall measure rank-based relationships
* zero correlation does not imply independence
* correlation does not imply causation
* outliers can strongly affect correlation
* nonlinear relationships may not be captured by Pearson correlation
* correlation matrices summarize pairwise relationships between variables
* correlation can be useful for EDA and feature analysis, but should not be used blindly for feature selection

The most important practical principle is:

> **Do not interpret a correlation coefficient in isolation. Understand the data-generating process, visualize the relationship, and distinguish association from causation.**
