# Chart Types

## TL;DR (30 seconds)

The idea:
> The right chart is determined by the question you ask and the data type you have, not by what looks nice.

In data exploration, most questions fall into five categories:

- **Distribution** → How are the values spread? (histogram, box plot, violin plot)
- **Relationship** → How do variables depend on each other? (scatter plot, heatmap)
- **Comparison** → How do categories differ? (bar chart, dot plot)
- **Trend** → How does a value change over time? (line chart, area chart)
- **Composition** → What are the parts of a whole? (stacked bar, treemap, pie chart)

---

## Motivation: Why Chart Choice Matters

The same data can lead to very different conclusions depending on how it is visualized.

A famous example is **Anscombe's quartet**: four datasets with nearly identical summary statistics:

- same mean of $x$ and $y$
- same variance of $x$ and $y$
- same correlation $r \approx 0.816$
- same regression line $y \approx 3 + 0.5x$

but completely different structure when plotted:

```
Dataset I        Dataset II       Dataset III      Dataset IV
linear           curved           linear + outlier vertical + outlier
  ·  ·             · ·              ·   ·              ·
 ·  ·            ·     ·           ·  ·               ·
·  ·            ·       ·        ·  ·    ·             ·
                                                    · ·
```

Summary statistics hide structure. A suitable chart reveals it.

Visualization is therefore the first step of **exploratory data analysis (EDA)**: before computing anything, look at the data.

---

## Choosing a Chart: Guiding Questions

Before choosing a chart, answer three questions:

1. **What is the question?** (distribution, relationship, comparison, trend, composition)
2. **What are the data types?** (numerical, categorical, temporal)
3. **How many variables?** (one, two, many)

Simplified decision guide:

```
How many variables?
      │
      ├── 1 variable
      │     ├── numerical   → histogram, box plot, violin plot
      │     └── categorical → bar chart
      │
      ├── 2 variables
      │     ├── num + num   → scatter plot, hexbin plot
      │     ├── num + cat   → box plot, violin plot, bar chart
      │     ├── cat + cat   → heatmap, grouped / stacked bar
      │     └── num + time  → line chart
      │
      └── many variables
            → pair plot, correlation heatmap, parallel coordinates
```

---

## Distribution Charts

Used to understand the **shape** of a single numerical variable: center, spread, skewness, outliers, modality.

### Histogram

A histogram splits the value range into **bins** and counts how many observations fall into each bin.

$$
\hat{f}(x) = \frac{n_j}{n \cdot h} \quad \text{for } x \in \text{bin}_j
$$

where:

- $n_j$ is the number of observations in bin $j$
- $n$ is the total number of observations
- $h$ is the bin width

The bin width has a strong influence on the impression:

- too few bins → hides structure (oversmoothing)
- too many bins → shows noise (undersmoothing)

A common rule is the **Freedman-Diaconis rule**:

$$
h = 2 \cdot \frac{\text{IQR}}{\sqrt[3]{n}}
$$

### Kernel Density Estimate (KDE)

A KDE is a smooth version of the histogram. Each observation contributes a small "bump" (kernel), and all bumps are summed:

$$
\hat{f}_h(x) = \frac{1}{nh} \sum_{i=1}^{n} K\left(\frac{x - x_i}{h}\right)
$$

where $K$ is the kernel (usually Gaussian) and $h$ the bandwidth. The bandwidth plays the same role as the bin width.

### Box Plot

A box plot summarizes a distribution with five numbers:

```
        Q1 - 1.5·IQR                                  Q3 + 1.5·IQR
             │                                             │
     ○       ├─────────┬────────────┬──────────┤            ○   ○
  outlier              Q1        median       Q3               outliers
                       └───── IQR ───────────┘
```

- **Box** → from $Q_1$ to $Q_3$ (interquartile range $\text{IQR} = Q_3 - Q_1$)
- **Line in the box** → median
- **Whiskers** → typically the most extreme points within $1.5 \cdot \text{IQR}$ of the box
- **Points** → outliers beyond the whiskers

Box plots are compact and ideal for **comparing many groups**, but they hide multimodality: a bimodal distribution can look the same as a unimodal one.

### Violin Plot

A violin plot combines a box plot with a KDE: the width of the shape shows the density at each value. It reveals multimodality that a box plot hides.

---

## Relationship Charts

Used to understand how **two or more variables** depend on each other.

### Scatter Plot

Each observation is a point $(x_i, y_i)$. A scatter plot shows:

- direction and strength of a relationship (positive, negative, none)
- shape (linear, nonlinear, clusters)
- outliers
- heteroscedasticity (variance changes with $x$)

Problem: with large $n$, points overlap (**overplotting**). Solutions:

- transparency (alpha blending)
- smaller markers
- **hexbin plot** or 2D histogram (count points per cell)
- sampling

### Bubble Chart

A scatter plot where the **size** (and optionally color) of the points encodes a third variable. Be careful: humans compare areas poorly, so bubble sizes are only suitable for rough comparisons.

### Heatmap

A heatmap displays a matrix of values as colors. Common use cases:

- **Correlation matrix** of numerical features
- **Confusion matrix** of a classifier
- **Missing values** per feature and sample

For correlations, a **diverging colormap** centered at $0$ (e.g. blue-white-red) is used:

$$
r_{ij} = \frac{\text{Cov}(X_i, X_j)}{\sigma_{X_i} \sigma_{X_j}} \in [-1, 1]
$$

### Pair Plot (Scatter Matrix)

A grid of scatter plots for all pairs of variables, with histograms or KDEs on the diagonal. It gives a fast overview of a small dataset (up to about 10 features).

---

## Comparison Charts

Used to compare values **across categories**.

### Bar Chart

The **length** of each bar encodes a value. Length on a common baseline is the most accurately perceived visual encoding, which makes bar charts the safest choice for comparisons.

Rules:

- the baseline must start at **zero** (otherwise differences are exaggerated)
- sort bars by value unless the categories have a natural order
- use horizontal bars for long category labels

Variants:

- **Grouped bar chart** → compare subcategories side by side
- **Stacked bar chart** → show totals and composition (but only the bottom segment is easy to compare)

### Dot Plot / Lollipop Chart

A bar chart reduced to a point (and a thin line). It is useful when the baseline does not need to start at zero or when there are many categories.

---

## Trend Charts

Used to show how values **change over an ordered axis**, usually time.

### Line Chart

Points are connected by lines, which emphasizes **continuity** and **slope**. Line charts are the default for time series.

What to look for in a time series:

- **trend** (long-term direction)
- **seasonality** (regular patterns)
- **outliers and breaks**
- **autocorrelation**

### Area Chart

A line chart with the area below filled. It emphasizes **magnitude** and works well for stacked cumulative values. With multiple overlapping series it becomes hard to read.

---

## Composition Charts

Used to show how a whole is divided into **parts**.

### Pie Chart

Each slice encodes a share of the total through angle and area. Pie charts are only suitable for **few categories** (2 to 4) with clearly different shares, because humans compare angles and areas poorly. In most cases, a bar chart is the better choice.

### Stacked Bar and Stacked Area Chart

Show composition across several groups or over time. A **100% stacked** variant shows only the proportions.

### Treemap

Nested rectangles whose area encodes the value. Suitable for hierarchical data with many categories.

---

## Perception: Why Some Charts Work Better

People decode visual encodings with different accuracy. From most to least accurate:

```
1. Position on a common scale      (scatter plot, bar chart baseline)
2. Position on non-aligned scales  (small multiples)
3. Length                          (bar chart)
4. Angle / slope                   (pie chart, line chart)
5. Area                            (bubble chart, treemap)
6. Color saturation / hue          (heatmap)
```

The consequence: encode the **most important comparison** with position or length, and use area or color only for secondary information.

---

## Common Mistakes

- **Truncated axis in bar charts** → exaggerates differences
- **3D charts** → distort perception, add no information
- **Too many categories in a pie chart** → unreadable
- **Dual y-axes** → can suggest false correlations by choosing the scales
- **Rainbow colormaps** → no natural order, misleading for continuous values
- **Overplotting** → hides the true density of the data
- **Missing labels and units** → chart cannot be interpreted

---

## Examples

### Exploring a Classification Dataset

Typical EDA workflow with the right chart for each question:

| Question                                  | Chart                             |
| ----------------------------------------- | --------------------------------- |
| How is the target distributed?            | Bar chart (class balance)         |
| How is a numerical feature distributed?   | Histogram / KDE                   |
| Does a feature differ between classes?    | Box plot / violin plot per class  |
| Are two features related?                 | Scatter plot colored by class     |
| Which features are redundant?             | Correlation heatmap               |
| Where are values missing?                 | Missing-value heatmap             |

### Evaluating a Model

| Question                                  | Chart                             |
| ----------------------------------------- | --------------------------------- |
| Which classes are confused?               | Confusion matrix (heatmap)        |
| How does training progress?               | Line chart (loss per epoch)       |
| How do thresholds affect performance?     | ROC / precision-recall curve      |
| Are residuals random?                     | Scatter plot of residuals         |

---

## Overview

| Goal         | Chart             | Variables      | Strength                         | Weakness                        |
| ------------ | ----------------- | -------------- | -------------------------------- | ------------------------------- |
| Distribution | Histogram         | 1 numerical    | Shows shape and modality         | Sensitive to bin width          |
| Distribution | Box plot          | 1 num (+ cat)  | Compact, good for many groups    | Hides multimodality             |
| Distribution | Violin plot       | 1 num (+ cat)  | Shows density per group          | Harder to read for beginners    |
| Relationship | Scatter plot      | 2 numerical    | Shows shape, clusters, outliers  | Overplotting for large data     |
| Relationship | Heatmap           | matrix         | Overview of many pairs           | Color is imprecise              |
| Comparison   | Bar chart         | 1 cat + 1 num  | Most accurate comparison         | Needs zero baseline             |
| Trend        | Line chart        | time + num     | Shows trend and seasonality      | Cluttered with many series      |
| Composition  | Stacked bar       | cat + cat      | Shows totals and parts           | Inner segments hard to compare  |
| Composition  | Pie chart         | 1 cat          | Intuitive for simple shares      | Poor perception of angles       |

Choosing a chart type is a fundamental step in data exploration because it determines which patterns in the data become visible and which stay hidden.
