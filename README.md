## Table of Contents

<!-- TOC_START -->
```text
data-science-wiki/
├── README.md
├── docs/
│   ├── 01-mathematical-foundations/
│   │   ├── 02-functional-analysis/
│   │   │   ├── banach-spaces.md
│   │   │   └── hilbert-spaces.md
│   │   ├── 02-linear-algebra/
│   │   │   ├── norms/
│   │   │   └── eigenvalues.md
│   │   ├── 03-optimization/
│   │   │   ├── convexity.md
│   │   │   └── gradients.md
│   │   ├── 04-geometry/
│   │   ├── 04-probability-theory/
│   │   │   ├── common-distributions/
│   │   │   │   ├── bernoulli-distribution.md
│   │   │   │   ├── binomial-distribution.md
│   │   │   │   ├── exponential-distribution.md
│   │   │   │   ├── exponentional-distribution.md
│   │   │   │   ├── normal-distribution.md
│   │   │   │   └── poisson-distribution.md
│   │   │   ├── central-limit-theorem.md
│   │   │   ├── correlation.md
│   │   │   ├── covariance.md
│   │   │   ├── law-of-large-numbers.md
│   │   │   └── variance.md
│   │   ├── 05-statistics/
│   │   │   ├── time-series/
│   │   │   │   ├── autocorrelation.md
│   │   │   │   ├── foundations.md
│   │   │   │   ├── stationarity.md
│   │   │   │   ├── time-series-decomposition.md
│   │   │   │   └── trend-and-seasonality.md
│   │   │   ├── bayesian-inference.md
│   │   │   ├── causal-inference.md
│   │   │   └── statistical-testing.md
│   │   └── 06-topology/
│   │       ├── homology/
│   │       ├── homotopy/
│   │       ├── important-manifolds/
│   │       ├── manifolds.md
│   │       ├── overview.md
│   │       └── topological-spaces.md
│   ├── 02-ml-models-theory/
│   │   ├── 01-ml-foundations/
│   │   │   ├── bias-variance-tradeoff.md
│   │   │   ├── classification-of-ml-models.md
│   │   │   ├── empirical-risk-minimization.md
│   │   │   ├── kernel-methods.md
│   │   │   ├── overfitting-and-underfitting.md
│   │   │   ├── pac-learning.md
│   │   │   ├── regularization.md
│   │   │   ├── uniform-convergence.md
│   │   │   ├── universal-approximation-theorem.md
│   │   │   ├── vc-dimension.md
│   │   │   └── what-is-machine-learning.md
│   │   ├── 02-traditional-ml-models/
│   │   │   ├── 01-supervised/
│   │   │   │   ├── linear-models/
│   │   │   │   │   └── linear-regression.md
│   │   │   │   ├── tree-based-methods/
│   │   │   │   ├── gaussian-processes.md
│   │   │   │   ├── naive-bayes.md
│   │   │   │   ├── nearest-neighbors.md
│   │   │   │   └── svm.md
│   │   │   ├── 02-unsupervised/
│   │   │   │   ├── clustering/
│   │   │   │   │   └── pca.md
│   │   │   │   ├── dimenstionality-reduction/
│   │   │   │   └── anomality-reduction.md
│   │   │   ├── 03-probabilistic/
│   │   │   │   ├── bayesian-networks.md
│   │   │   │   ├── gaussian-mixture-models.md
│   │   │   │   └── hidden-markov-models.md
│   │   │   └── 04-time-series-models/
│   │   │       ├── arima.md
│   │   │       ├── autoregressive-models.md
│   │   │       └── kalman-filter.md
│   │   ├── 03-deep-learning-models/
│   │   │   ├── 01-architectures/
│   │   │   │   ├── autoencoders.md
│   │   │   │   ├── cnn-architectures.md
│   │   │   │   ├── graph-neural-networks.md
│   │   │   │   ├── neural-network-basics.md
│   │   │   │   └── rnn-lstm.md
│   │   │   ├── 02-generative-models/
│   │   │   │   ├── autoregressive-models.md
│   │   │   │   ├── diffusion-models.md
│   │   │   │   ├── energy-based-models.md
│   │   │   │   ├── generative-adversarial-networks.md
│   │   │   │   ├── multimodal-generative-models.md
│   │   │   │   ├── normalizing-flows.md
│   │   │   │   ├── score-based-models.md
│   │   │   │   └── variational-autoencoders.md
│   │   │   └── 03-learning-paradigms/
│   │   │       ├── federated-learning.md
│   │   │       ├── few-shot-learning.md
│   │   │       ├── meta-learning.md
│   │   │       ├── self-supervised-learning.md
│   │   │       └── transfer-learning.md
│   │   └── 04-llms/
│   │       ├── 01-foundations/
│   │       │   ├── tokenization.md
│   │       │   └── what-are-llms.md
│   │       ├── 02-transformer-architecture/
│   │       │   ├── decoder-only-models.md
│   │       │   ├── multi-head-attention.md
│   │       │   ├── positional-encoding.md
│   │       │   └── self-attention.md
│   │       └── 03-model-architectures/
│   │           ├── gpt-family.md
│   │           ├── llama-family.md
│   │           ├── mixture-of-experts.md
│   │           └── multimodal-llms.md
│   ├── 03-training-and-optimizing-ml-models/
│   │   ├── 01-traditional-ml/
│   │   │   └── hyperparameter-tuning/
│   │   ├── 02-dl/
│   │   │   ├── 01-loss-functions/
│   │   │   ├── 02-optimization/
│   │   │   │   ├── batch-normalization.md
│   │   │   │   ├── learning-rate-scheduling.md
│   │   │   │   └── optimization-algorithms.md
│   │   │   ├── 03-regularization/
│   │   │   │   ├── dropout.md
│   │   │   │   ├── early-stopping.md
│   │   │   │   ├── l1-l2-regularization.md
│   │   │   │   └── weight-decay.md
│   │   │   └── 04-data-strategies/
│   │   │       └── data-augmentation.md/
│   │   └── 03-llms/
│   │       ├── finetuning/
│   │       └── promt-engineering/
│   ├── 04-evaluation/
│   │   ├── 01-classification-metrics/
│   │   │   ├── accuracy.md
│   │   │   ├── confusion-matrix.md
│   │   │   ├── f1-score.md
│   │   │   ├── log-loss.md
│   │   │   ├── multiclass-metrics.md
│   │   │   ├── precision-recall-auc.md
│   │   │   ├── precision.md
│   │   │   ├── recall-sensitivity.md
│   │   │   ├── roc-auc.md
│   │   │   └── specificity.md
│   │   ├── 02-regression-metrics/
│   │   │   ├── adjusted-r-squared.md
│   │   │   ├── mae.md
│   │   │   ├── mse.md
│   │   │   ├── r-squared.md
│   │   │   └── rmse.md
│   │   ├── 03-model-diagnostics/
│   │   │   ├── bias-detection.md
│   │   │   ├── calibration-analysis.md
│   │   │   └── residual-analysis.md
│   │   ├── 04-uncertainty-quantification/
│   │   ├── cross-validation.md
│   │   ├── fairness-bias.md
│   │   └── model-selection.md
│   ├── 05-data-engineering/
│   │   ├── 01-data-pipelines/
│   │   ├── 02-data-preprocessing/
│   │   │   ├── 01-data-cleaning/
│   │   │   │   └── 02-/
│   │   │   ├── 02-data-transformation/
│   │   │   ├── 03-missing-data-handling/
│   │   │   ├── 04-outlier-detection/
│   │   │   └── 05-data-normalization/
│   │   ├── 03-data-versioning/
│   │   ├── 04-distributed-processing/
│   │   │   ├── hadoop/
│   │   │   └── spark/
│   │   └── 05-feature-engineering/
│   ├── 06-databases/
│   │   ├── 01-sql-databases/
│   │   ├── 02-nosql-databses/
│   │   └── 03-vector-databases.md/
│   ├── 07-deployment/
│   │   ├── 01-fundamentals/
│   │   │   ├── api-design.md
│   │   │   ├── containerization.md
│   │   │   └── model-serialization.md
│   │   ├── 02-containers/
│   │   │   ├── docker-compose.md
│   │   │   └── docker.md
│   │   ├── 03-kubernetes/
│   │   │   ├── configmaps.md
│   │   │   ├── deployments.md
│   │   │   ├── foundations.md
│   │   │   ├── ingress.md
│   │   │   ├── namespaces.md
│   │   │   ├── pods.md
│   │   │   ├── secrets.md
│   │   │   └── services.md
│   │   └── 04-cloud-deployment/
│   │       └── s3.md
│   ├── 08-mlops/
│   │   ├── 01-ci-cd/
│   │   │   ├── github-actions.md
│   │   │   └── jenkins.md
│   │   ├── 02-experiment-tracking/
│   │   ├── 03-model-registry/
│   │   ├── 04-orchestration/
│   │   ├── 05-monitoring/
│   │   └── 06-ml-pipelines/
│   ├── 09-software-engineering/
│   │   ├── 01-clean-code/
│   │   ├── 02-testing/
│   │   │   ├── 01-unit-tests/
│   │   │   ├── 02-integration-tests/
│   │   │   └── 03-e2e-tests/
│   │   ├── 03-documentation/
│   │   ├── 04-version-control/
│   │   ├── 05-software-design/
│   │   │   └── design-patterns/
│   │   ├── 06-build-and-dependency-management/
│   │   │   ├── poetry.md
│   │   │   └── uv.md
│   │   ├── 07-performance/
│   │   │   ├── optimization.md
│   │   │   └── parallel-programming.md
│   │   ├── 08-security/
│   │   │   ├── authentication.md
│   │   │   ├── authorization.md
│   │   │   ├── dependency-security.md
│   │   │   └── secrets-management.md
│   │   └── 09-architectures/
│   │       ├── honeycomb architecture.md
│   │       └── monolith-vs-microservices.md
│   └── 10-tda/
│       └── 01-persistence-homology/
├── assets/
└── scripts/
    └── generate-toc.py
```
<!-- TOC_END -->
