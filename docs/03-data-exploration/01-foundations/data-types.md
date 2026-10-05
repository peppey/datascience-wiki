# Data Types

A **data type** describes what kind of information a variable contains and what operations and interpretations are meaningful for that information.

In Data Science, the term *data type* can refer to several related but distinct concepts:

* the **technical data type** used to store a value, e.g. `int`, `float`, or `string`
* the **statistical type** of a variable, e.g. nominal, ordinal, or continuous
* the **semantic meaning** of a variable, e.g. age, country, or temperature

These distinctions matter because the way a variable is stored does not necessarily tell us how it should be analyzed.

For example, a survey response might be stored as the integers `1`, `2`, `3`, `4`, and `5`. Technically, these are integers. Statistically, however, they may represent an **ordinal variable** rather than a numerical measurement.

---

## 1. Numerical Data

Numerical data represent quantities for which arithmetic operations are meaningful.

They can broadly be divided into **discrete** and **continuous** data.

### 1.1 Discrete Data

Discrete variables can take distinct, countable values.

Examples:

* number of customers
* number of accidents
* number of children
* number of purchases
* number of defects

A number of customers can be `0`, `1`, `2`, ... but not `2.5`.

Discrete variables are often represented as integers:

```python
number_of_customers = 42
```

However, the fact that a variable is stored as an integer does not automatically make it discrete in the statistical sense.

### 1.2 Continuous Data

Continuous variables can theoretically take any value within an interval.

Examples:

* height
* weight
* temperature
* duration
* voltage
* concentration

For example, a temperature might be:

```text
20.0
20.01
20.013
20.0137
...
```

In practice, measurements are always limited by the precision of the measurement device.

Continuous variables are commonly represented using floating-point numbers:

```python
temperature = 20.5
```

---

## 2. Categorical Data

Categorical variables represent membership in a set of categories.

Examples:

* country
* blood type
* product category
* department
* animal species
* payment method

```text
Germany
France
Italy
Germany
Spain
```

The values themselves do not necessarily have numerical meaning.

For example, encoding

```text
Germany → 1
France  → 2
Italy   → 3
```

does **not** mean that Italy is "greater" than France.

This distinction is particularly important when categorical variables are encoded for machine learning.

### 2.1 Nominal Data

**Nominal variables** contain categories without an inherent ordering.

Examples:

* eye color
* nationality
* operating system
* product type

```text
Windows
Linux
macOS
```

There is no meaningful statement such as:

```text
Linux > Windows
```

even if the categories are represented by numbers internally.

### 2.2 Ordinal Data

**Ordinal variables** contain categories with a meaningful order, but the distances between categories are not necessarily meaningful.

Examples:

* education level
* satisfaction rating
* severity level
* Likert scales

For example:

```text
Very dissatisfied
Dissatisfied
Neutral
Satisfied
Very satisfied
```

We know that:

```text
Satisfied > Neutral
```

in terms of the underlying order.

However, we generally cannot assume that the difference between

```text
Very dissatisfied → Dissatisfied
```

is exactly the same as

```text
Satisfied → Very satisfied
```

as would be the case for an interval scale.

---

## 3. Binary Data

A **binary variable** has only two possible states.

Examples:

* yes / no
* true / false
* present / absent
* success / failure
* 0 / 1

In Python, binary variables are often represented using `bool`:

```python
is_customer = True
```

or numerically:

```text
0
1
```

Binary variables are particularly common as target variables in **binary classification**.

For example:

```text
fraud
0 = legitimate transaction
1 = fraudulent transaction
```

A binary variable can be considered a special case of categorical data.

---

## 4. Text Data

Text data consists of sequences of characters.

Examples:

* names
* addresses
* product descriptions
* customer reviews
* documents
* chat messages

In Python, text is generally represented using `str`:

```python
text = "Machine learning is useful."
```

Text is different from categorical data even when it is stored in the same technical type.

For example:

```text
country = "Germany"
```

is categorical, while

```text
review = "The product arrived quickly and works well."
```

is unstructured text.

Text data usually requires additional processing before it can be used by traditional machine-learning algorithms.

Common representations include:

* bag-of-words
* TF-IDF
* word embeddings
* sentence embeddings
* transformer representations

---

## 5. Date and Time Data

Temporal data represents points in time, dates, times of day, or durations.

Common examples include:

```text
2026-10-05
2026-10-05 14:32:17
14:32:17
```

It is important to distinguish between different temporal concepts.

### Date

A date represents a calendar day:

```text
2026-10-05
```

### Time

A time represents a time of day:

```text
14:32:17
```

### Datetime / Timestamp

A datetime combines a date and a time:

```text
2026-10-05 14:32:17
```

A timestamp may additionally contain timezone information.

### Duration

A duration represents an amount of elapsed time:

```text
3 minutes
2.5 hours
14 days
```

Temporal data is particularly important in **time-series analysis**, where observations are ordered according to time.

---

## 6. Missing Data

Missingness is not usually a data type in the same sense as numerical or categorical data. It is instead a property of an observation.

A dataset may contain:

```text
age
---
23
41
NaN
35
```

The third observation has no recorded value for `age`.

Common representations include:

* `NaN`
* `None`
* `NULL`
* `NA`

Missing data must be distinguished from valid values.

For example:

```text
0
```

is not necessarily missing.

A value of zero may have a meaningful interpretation:

```text
number_of_children = 0
```

Similarly, an empty string may or may not represent missing data depending on the dataset.

Missingness can itself contain information. For example, a medical measurement might only be recorded for patients for whom a doctor considered it necessary.

---

## 7. Structured and Unstructured Data

Another useful distinction is between **structured**, **semi-structured**, and **unstructured** data.

### Structured Data

Structured data follows a predefined schema.

A relational table is a typical example:

| customer_id | age | country | revenue |
| ----------- | --: | ------- | ------: |
| 1           |  32 | Germany | 1200.50 |
| 2           |  45 | France  |  830.00 |
| 3           |  27 | Germany | 1540.20 |

Each column has a defined meaning and usually a defined data type.

### Semi-structured Data

Semi-structured data does not follow a rigid tabular schema but contains structural information.

Examples:

* JSON
* XML
* HTML
* log files

For example:

```json
{
  "name": "Alice",
  "age": 32,
  "country": "Germany"
}
```

Different records may contain different fields.

### Unstructured Data

Unstructured data does not naturally conform to a predefined tabular schema.

Examples:

* documents
* images
* audio
* video
* free-form text

Modern Data Science and AI systems increasingly work with these data types.

---

## 8. Images, Audio and Video

Some data types are inherently multidimensional or high-dimensional.

### Images

An image can be represented as a tensor of pixel values.

A grayscale image might have the shape:

```text
(height, width)
```

A color image commonly has:

```text
(height, width, channels)
```

For an RGB image:

```text
224 × 224 × 3
```

The three channels correspond to red, green, and blue.

### Audio

Audio data can be represented as a sequence of measurements over time.

For example, a recording can be represented as a one-dimensional waveform:

```text
x(t)
```

Additional representations such as spectrograms transform the signal into a two-dimensional time-frequency representation.

### Video

Video can be understood as a sequence of images:

```text
(time, height, width, channels)
```

This makes video data inherently spatiotemporal.

---

## 9. Vectors, Matrices and Tensors

Machine learning frequently represents data as mathematical objects rather than individual scalar values.

### Scalar

A scalar is a single value:

```text
x = 5
```

### Vector

A vector is an ordered collection of values:

$$
\mathbf{x} =
\begin{pmatrix}
2 \\
4 \\
7
\end{pmatrix}
$$

In machine learning, a vector can represent the features of one observation:

```text
age = 32
income = 50000
height = 174
```

which can be represented as:

$$
\mathbf{x} =
\begin{pmatrix}
32 \\
50000 \\
174
\end{pmatrix}
$$

### Matrix

A matrix is a two-dimensional array:

$$
X =
\begin{pmatrix}
x_{11} & x_{12} & x_{13} \\
x_{21} & x_{22} & x_{23}
\end{pmatrix}
$$

A typical tabular dataset can be represented as a matrix where rows correspond to observations and columns correspond to features.

### Tensor

A tensor generalizes vectors and matrices to arbitrary numbers of dimensions.

For example:

```text
scalar → 0 dimensions
vector → 1 dimension
matrix → 2 dimensions
tensor → 3+ dimensions
```

Deep-learning frameworks such as PyTorch and TensorFlow use tensors as their fundamental data structure.

---

## 10. Technical Type vs. Statistical Type

One of the most important distinctions in Data Science is between **how data is stored** and **what the data means**.

Consider:

```python
rating = 5
```

Technically:

```text
int
```

Semantically, however, the value might represent:

```text
Very satisfied
```

In that case, the variable is **ordinal**, not simply numerical.

Similarly:

```python
postal_code = 80331
```

is technically an integer, but treating it as a continuous numerical variable would usually be wrong.

The difference can be summarized as:

| Variable     | Technical representation | Statistical interpretation |
| ------------ | ------------------------ | -------------------------- |
| Age          | integer                  | numerical                  |
| Temperature  | float                    | continuous                 |
| Country      | string                   | nominal                    |
| Satisfaction | integer                  | ordinal                    |
| Customer ID  | integer/string           | identifier                 |
| Postal code  | integer/string           | categorical                |
| Review       | string                   | text                       |
| Is customer  | boolean                  | binary                     |
| Timestamp    | datetime                 | temporal                   |

**The technical representation alone does not determine the appropriate statistical treatment.**

---

## 11. Why Data Types Matter for Machine Learning

The data type of a variable influences almost every stage of a machine-learning workflow.

### Exploratory Data Analysis

Different types require different visualizations.

For example:

| Data type  | Typical visualizations                   |
| ---------- | ---------------------------------------- |
| Continuous | histogram, density plot, box plot        |
| Discrete   | histogram, bar plot                      |
| Nominal    | bar plot                                 |
| Ordinal    | ordered bar plot                         |
| Temporal   | line plot                                |
| Geographic | map                                      |
| Text       | word frequencies, embeddings, similarity |
| Image      | image grids                              |

### Preprocessing

Different variables require different transformations.

Examples:

```text
Numerical → scaling / transformation
Categorical → one-hot encoding / target encoding
Ordinal → ordinal encoding
Text → tokenization / embeddings
Datetime → temporal features
Images → normalization / augmentation
```

Applying the wrong transformation can introduce misleading assumptions.

For example, applying ordinary numerical scaling to a nominal category encoded as integers does not make the categories numerical.

### Model Choice

The type and structure of the input data also influence which models are appropriate.

Examples:

* tabular numerical data → linear models, tree-based models, neural networks
* time series → statistical forecasting models, temporal neural networks
* text → NLP models and transformers
* images → convolutional or vision transformer models
* graphs → graph neural networks

---

## 12. A Practical Classification Checklist

When encountering a new variable, ask:

1. **What does the variable represent?**
2. **Is it numerical, categorical, textual, temporal, spatial, or another type of data?**
3. **If it is categorical, is there a meaningful ordering?**
4. **Are arithmetic operations meaningful?**
5. **Is the variable discrete or continuous?**
6. **Could the variable's missingness itself contain information?**
7. **How is the variable technically stored?**
8. **Does the technical representation match its semantic meaning?**
9. **What preprocessing is appropriate?**
10. **Which visualizations and models make sense for this type?**

A useful rule is:

> **Understand the meaning of a variable before deciding how to encode or transform it.**

---

## Summary

Data types in Data Science have several layers.

At the **technical level**, values may be stored as integers, floating-point numbers, strings, booleans, datetimes, arrays, or other structures.

At the **statistical level**, variables may be:

* numerical
* discrete
* continuous
* nominal
* ordinal
* binary
* temporal

At the **data-structure level**, data may be represented as:

* scalars
* vectors
* matrices
* tensors
* tables
* JSON and other semi-structured formats

And at the **semantic level**, the same technical type can represent very different concepts.

Correctly identifying these types is therefore an important part of data understanding, exploratory analysis, preprocessing, and machine learning.
