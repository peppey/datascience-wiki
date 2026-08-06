# Linear Regression

## TL;DR

**Linear Regression** is a supervised learning algorithm that models the relationship between input variables and a continuous target variable.

It assumes that the target can be approximated by a linear combination of the input features.

---

## Model

For one feature:

$$
\hat{y} = w_0 + w_1x
$$

For multiple features:

$$
\hat{y} = w_0 + w_1x_1 + w_2x_2 + ... + w_nx_n
$$

where:

- $\hat{y}$ = predicted value
- $x_i$ = input features
- $w_i$ = learned weights
- $w_0$ = bias/intercept

---

## Goal

The model learns parameters that minimize the difference between predictions and actual values.

The most common loss function is **Mean Squared Error (MSE)**:

$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y_i})^2
$$

The optimal parameters are often found using:

- closed-form solution with QR/SVD decomposition
- gradient descent

---

## Example

Predicting house prices:

Features:

- size of the house
- number of rooms
- location

Target:

- price

The model learns how each feature influences the predicted price.

---

## Assumptions

Linear regression works best when:

- the relationship between features and target is approximately linear
- features are not highly correlated (no strong multicollinearity)
- errors have constant variance (homoscedasticity)
- observations are independent

---

## Extensions

Common extensions include:

- **Polynomial Regression**  
  Adds nonlinear features like $x^2$ or $x^3$.

- **Ridge Regression**  
  Adds L2 regularization to reduce overfitting.

- **Lasso Regression**  
  Adds L1 regularization and can set weights to zero for feature selection.

---

## Key Takeaway

Linear Regression is one of the simplest machine learning models.  
It is fast, interpretable, and provides a strong baseline for regression problems.