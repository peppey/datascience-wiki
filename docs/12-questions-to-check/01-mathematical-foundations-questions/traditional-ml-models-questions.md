## Linear Regression

### Question 1

What assumptions does linear regression make?

---

### Question 2

Why does ordinary least squares have a closed-form solution?

---

### Question 3

What is the geometric interpretation of linear regression?

---

### Question 4

What is the difference between linear regression and logistic regression?

---

### Question 5

Why can logistic regression be used for classification?

---

### Question 6

What does the decision boundary of logistic regression look like?

---

### Question 7

What is the effect of L1 regularization on a linear model?

---

### Question 8

What is the effect of L2 regularization on a linear model?

---

### Question 9

What is the difference between Ridge, Lasso, and Elastic Net?

---

### Question 10

When would you prefer a linear model over a more complex model?

---

## Support Vector Machines

### Question 1

What is the maximum-margin principle?

---

### Question 2

Why does maximizing the margin improve generalization?

---

### Question 3

What is the difference between hard-margin and soft-margin SVM?

---

### Question 4

What does the parameter $C$ control?

---

### Question 5

What are support vectors?

---

### Question 6

Why do only the support vectors determine the decision boundary?

---

### Question 7

How does the kernel trick allow SVMs to model nonlinear decision boundaries?

---

### Question 8

What is the relationship between SVMs and kernel methods?

---

### Question 9

When are SVMs particularly useful?

---

## Decision Trees

### Question 1

How does a decision tree choose a split?

---

### Question 2

What are Gini impurity and entropy?

---

### Question 3

Why do decision trees tend to overfit?

---

### Question 4

What does tree depth control?

---

### Question 5

What is pruning?

---

### Question 6

Why are decision trees invariant to monotonic transformations of features?

---

### Question 7

What are the advantages and disadvantages of decision trees compared with linear models?

---

## Random Forests

### Question 1

How does a random forest combine multiple decision trees?

---

### Question 2

What is the difference between bagging and random feature selection?

---

### Question 3

Why does randomization reduce correlation between trees?

---

### Question 4

Why can a random forest generalize better than a single decision tree?

---

### Question 5

What is the out-of-bag estimate?

---

### Question 6

How can feature importance be estimated in a random forest?

---

### Question 7

What are the main limitations of random forests?

---

## Gradient Boosting

### Question 1

What is the basic idea behind boosting?

---

### Question 2

How does gradient boosting differ from bagging?

---

### Question 3

Why are trees trained sequentially in boosting?

---

### Question 4

What does each new tree try to learn?

---

### Question 5

How is the gradient of the loss used?

---

### Question 6

What is the role of the learning rate?

---

### Question 7

What is the difference between gradient boosting and XGBoost?

---

### Question 8

Which hyperparameters control the complexity of a boosted tree model?

---

### Question 9

Why can boosting overfit?

---

### Question 10

When would you choose XGBoost over a random forest?

---

## k-Nearest Neighbors

### Question 1

How does k-NN make a prediction?

---

### Question 2

Why is feature scaling important for k-NN?

---

### Question 3

What is the effect of increasing $k$?

---

### Question 4

How does the choice of distance metric affect k-NN?

---

### Question 5

Why is k-NN called a lazy learning algorithm?

---

### Question 6

What is the curse of dimensionality in k-NN?

---

### Question 7

When does k-NN work well, and when does it perform poorly?

---

## Naive Bayes

### Question 1

What is the Naive Bayes assumption?

---

### Question 2

Why is the assumption called "naive"?

---

### Question 3

How does Bayes' theorem lead to the Naive Bayes classifier?

---

### Question 4

Why can Naive Bayes work well even when its independence assumption is violated?

---

### Question 5

What are Gaussian, Multinomial, and Bernoulli Naive Bayes?

---

### Question 6

Why is Naive Bayes particularly common in text classification?

---

## Gaussian Processes

### Question 1

What is a Gaussian process?

---

### Question 2

How does a Gaussian process differ from a Gaussian distribution?

---

### Question 3

What does a kernel define in a Gaussian process?

---

### Question 4

How does a Gaussian process make predictions?

---

### Question 5

Why does a Gaussian process provide uncertainty estimates?

---

### Question 6

What is the relationship between Gaussian processes and kernel methods?

---

### Question 7

Why do Gaussian processes become computationally expensive for large datasets?

---

## k-Means

### Question 1

What objective does k-means optimize?

---

### Question 2

Why does k-means depend on the initialization?

---

### Question 3

What does the number $k$ represent?

---

### Question 4

Why is feature scaling important for k-means?

---

### Question 5

What assumptions does k-means make about clusters?

---

### Question 6

Why does k-means struggle with non-spherical clusters?

---

### Question 7

How can the appropriate number of clusters be selected?

---

## Hierarchical Clustering

### Question 1

What is the difference between agglomerative and divisive clustering?

---

### Question 2

What is a linkage criterion?

---

### Question 3

What are single, complete, average, and Ward linkage?

---

### Question 4

How does a dendrogram represent the clustering?

---

### Question 5

When is hierarchical clustering preferable to k-means?

---

## DBSCAN

### Question 1

How does DBSCAN define a cluster?

---

### Question 2

What are core points, border points, and noise points?

---

### Question 3

What do $\epsilon$ and `min_samples` control?

---

### Question 4

Why can DBSCAN detect arbitrarily shaped clusters?

---

### Question 5

Why does DBSCAN naturally identify outliers?

---

### Question 6

What are the limitations of DBSCAN?

---

## Density Estimation

### Question 1

What is density estimation?

---

### Question 2

What is the difference between parametric and non-parametric density estimation?

---

### Question 3

How does Kernel Density Estimation work?

---

### Question 4

What role does the bandwidth play in KDE?

---

### Question 5

How can density estimation be used for anomaly detection?

---

## Principal Component Analysis

### Question 1

What does PCA optimize?

---

### Question 2

Why are the principal components orthogonal?

---

### Question 3

How is PCA related to eigenvectors and eigenvalues?

---

### Question 4

Why is PCA equivalent to finding directions of maximum variance?

---

### Question 5

What is the relationship between PCA and SVD?

---

### Question 6

How does dimensionality reduction affect information loss?

---

### Question 7

Why should features often be standardized before PCA?

---

## UMAP

### Question 1

What problem does UMAP try to solve?

---

### Question 2

How does UMAP differ conceptually from PCA?

---

### Question 3

What is the role of the local neighborhood graph?

---

### Question 4

What do `n_neighbors` and `min_dist` control?

---

### Question 5

Why should UMAP plots not automatically be interpreted as faithful global geometry?

---

### Question 6

When would you use UMAP instead of PCA?

---

## Gaussian Mixture Models

### Question 1

What is a Gaussian mixture model?

---

### Question 2

How does a GMM differ from k-means?

---

### Question 3

What does each Gaussian component represent?

---

### Question 4

What are the mixture weights?

---

### Question 5

How does a GMM perform soft clustering?

---

### Question 6

Why is the Expectation-Maximization algorithm used to train GMMs?

---

### Question 7

What does the E-step compute?

---

### Question 8

What does the M-step optimize?

---

### Question 9

How can GMMs be used for density estimation and anomaly detection?

---

## Bayesian Networks

### Question 1

What does a Bayesian network represent?

---

### Question 2

How does a directed acyclic graph encode conditional dependencies?

---

### Question 3

What is conditional independence?

---

### Question 4

How can the joint distribution be factorized using a Bayesian network?

---

### Question 5

What is the difference between Bayesian networks and Markov random fields?

---

### Question 6

How can Bayesian networks be used for inference?

---

## Hidden Markov Models

### Question 1

What is the hidden state in an HMM?

---

### Question 2

What are transition and emission probabilities?

---

### Question 3

What assumptions does an HMM make?

---

### Question 4

What is the difference between the forward and Viterbi algorithms?

---

### Question 5

What problem does the forward-backward algorithm solve?

---

### Question 6

How are HMM parameters learned?

---

### Question 7

When are HMMs useful for sequential data?

---

## Autoregressive Models

### Question 1

What does an autoregressive model assume about a time series?

---

### Question 2

What does the parameter $p$ represent in an AR($p$) model?

---

### Question 3

What does stationarity mean for an autoregressive process?

---

### Question 4

What is the role of the autocorrelation function?

---

### Question 5

When is an AR model appropriate?

---

## ARIMA

### Question 1

What do the AR, I, and MA components represent?

---

### Question 2

Why is differencing used in ARIMA?

---

### Question 3

What does stationarity have to do with ARIMA?

---

### Question 4

How are the parameters $p$, $d$, and $q$ selected?

---

### Question 5

What is seasonal ARIMA?

---

### Question 6

When would ARIMA be preferable to a machine learning model?

---

## Kalman Filter

### Question 1

What problem does the Kalman filter solve?

---

### Question 2

What are the state and observation models?

---

### Question 3

What is the difference between prediction and update?

---

### Question 4

How does the Kalman filter combine model predictions with noisy observations?

---

### Question 5

What assumptions does the classical Kalman filter make?

---

### Question 6

How is the Kalman filter related to Bayesian filtering?

---

## Bagging

### Question 1

What is the basic idea behind bagging?

---

### Question 2

Why are bootstrap samples used?

---

### Question 3

How does bagging reduce variance?

---

### Question 4

Why does averaging many models help?

---

### Question 5

What is the relationship between bagging and random forests?

---

## Boosting

### Question 1

What is the fundamental idea behind boosting?

---

### Question 2

Why are weak learners trained sequentially?

---

### Question 3

How does boosting reduce bias?

---

### Question 4

What is the difference between AdaBoost and gradient boosting?

---

### Question 5

Why can boosting be sensitive to noise?

---

## Voting

### Question 1

What is hard voting?

---

### Question 2

What is soft voting?

---

### Question 3

When is soft voting preferable?

---

### Question 4

Why can combining different models improve performance?

---

## Stacking

### Question 1

What is stacking?

---

### Question 2

What is the role of the meta-model?

---

### Question 3

Why must predictions for the meta-model be generated without data leakage?

---

### Question 4

How does stacking differ from voting?

---

### Question 5

When is stacking useful?

---

## Cross-Model Questions

### Question 1

Which traditional ML models are parametric and which are non-parametric?

---

### Question 2

Which models are particularly sensitive to feature scaling?

---

### Question 3

Which models can naturally model nonlinear relationships?

---

### Question 4

Which models provide probabilistic predictions?

---

### Question 5

Which models provide uncertainty estimates?

---

### Question 6

Which models are particularly sensitive to outliers?

---

### Question 7

Which models are computationally expensive at prediction time?

---

### Question 8

Which models scale poorly with the number of training samples?

---

### Question 9

Which models work well with high-dimensional sparse data?

---

### Question 10

Which models work well with small datasets?

---

### Question 11

Which models are naturally interpretable?

---

### Question 12

Which models are sensitive to the choice of distance metric?

---

### Question 13

Which models are sensitive to hyperparameter initialization?

---

### Question 14

Which models can handle missing values natively?

---

### Question 15

Which models are particularly suitable for tabular data?

---

### Question 16

When would you choose a linear model over a tree-based model?

---

### Question 17

When would you choose a random forest over gradient boosting?

---

### Question 18

When would you choose k-NN over a parametric model?

---

### Question 19

When would you choose a probabilistic model instead of a discriminative model?

---

### Question 20

How does the inductive bias differ between linear models, trees, nearest-neighbor methods, and probabilistic models?

