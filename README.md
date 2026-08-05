## Table of Contents

<!-- TOC_START -->
```text
data-science-wiki/
├── README.md
├── docs/
│   ├── 01-mathematical-foundations/
│   │   ├── 01-linear-algebra/
│   │   │   ├── norms/
│   │   │   │   ├── foundations.md
│   │   │   │   ├── lp-norms.md
│   │   │   │   └── max-norm.md
│   │   │   ├── basis.md
│   │   │   ├── complex-numbers.md
│   │   │   ├── determinants.md
│   │   │   ├── eigenvalues.md
│   │   │   ├── inverse.md
│   │   │   ├── matrix-factorizations.md
│   │   │   ├── matrizes.md
│   │   │   ├── orthogonality.md
│   │   │   ├── pseudoinverse.md
│   │   │   ├── scalar-product.md
│   │   │   ├── singular-value-decomposition.md
│   │   │   └── vector-spaces.md
│   │   ├── 02-analysis/
│   │   │   ├── derivatives/
│   │   │   │   ├── foundations.md
│   │   │   │   ├── gradient.md
│   │   │   │   ├── hessian.md
│   │   │   │   └── jacobian.md
│   │   │   ├── differential-equations/
│   │   │   ├── fourier-analysis/
│   │   │   │   ├── fourier-series.md
│   │   │   │   └── fourier-transform.md
│   │   │   ├── continuity.md
│   │   │   ├── convexity.md
│   │   │   ├── integral.md
│   │   │   ├── laplacian.md
│   │   │   ├── limits.md
│   │   │   ├── maps.md
│   │   │   ├── sequences-and-series.md
│   │   │   ├── set-theory.md
│   │   │   ├── taylor-series.md
│   │   │   └── trigonometry.md
│   │   ├── 03-functional-analysis/
│   │   │   ├── banach-spaces.md
│   │   │   ├── hilbert-spaces.md
│   │   │   └── orthonormal-bases.md
│   │   ├── 03-optimization/
│   │   │   ├── discrete-optimization/
│   │   │   │   ├── branch-and-bound.md
│   │   │   │   ├── combinatorial-optimization.md
│   │   │   │   ├── greedy-algorithms.md
│   │   │   │   └── integer-programming.md
│   │   │   ├── gradient-descent/
│   │   │   │   ├── exploding-gradient.md
│   │   │   │   ├── foundations.md
│   │   │   │   └── vanishing-gradient.md
│   │   │   ├── nonlinear-optimization/
│   │   │   │   ├── constrained-optimization/
│   │   │   │   ├── lagrange-multipliers.md
│   │   │   │   ├── newton-method.md
│   │   │   │   └── saddle-points.md
│   │   │   ├── stochastic-optimization/
│   │   │   │   ├── momentum.md
│   │   │   │   └── stochastic-gradient-descent.md
│   │   │   ├── duality.md
│   │   │   ├── foundations.md
│   │   │   └── kkt-conditions.md │
│   │   ├── 04-geometry/
│   │   │   ├── differential-geometry/
│   │   │   │   └── curves.md
│   │   │   ├── euclidean-geometry/
│   │   │   │   ├── distances-and-metrics.md
│   │   │   │   └── euclidean-space.md
│   │   │   ├── projective-geometry/
│   │   │   │   ├── conic-section.md
│   │   │   │   ├── homogenous-coordinates.md
│   │   │   │   └── projective-spaces.md
│   │   │   └── what-is-geometry.md
│   │   ├── 05-probability-theory/
│   │   │   ├── common-distributions/
│   │   │   │   ├── bernoulli-distribution.md
│   │   │   │   ├── binomial-distribution.md
│   │   │   │   ├── exponential-distribution.md
│   │   │   │   ├── exponentional-distribution.md
│   │   │   │   ├── normal-distribution.md
│   │   │   │   ├── poisson-distribution.md
│   │   │   │   └── student-t-distribution.md
│   │   │   ├── bayes-theorem.md
│   │   │   ├── central-limit-theorem.md
│   │   │   ├── chebyshev-inequality.md
│   │   │   ├── conditional-distributions.md
│   │   │   ├── conditional-expectation.md
│   │   │   ├── correlation.md
│   │   │   ├── covariance.md
│   │   │   ├── independence.md
│   │   │   ├── joint-distributions.md
│   │   │   ├── law-of-large-numbers.md
│   │   │   ├── marginal-distributions.md
│   │   │   ├── markov-inequality.md
│   │   │   ├── probability-space.md
│   │   │   ├── random-variable.md
│   │   │   ├── random-vectors.md
│   │   │   ├── stochastic-convergence.md
│   │   │   ├── transformations-of-random-variables.md
│   │   │   └── variance.md
│   │   ├── 06-statistics/
│   │   │   ├── bayesian-inference/
│   │   │   │   └── what-is-bayesian-inference.md
│   │   │   ├── causal-inference/
│   │   │   ├── computational-statistics/
│   │   │   │   ├── bootstrap.md
│   │   │   │   ├── markov-chain-monte-carlo.md
│   │   │   │   └── monte-carlo-methods.md
│   │   │   ├── estimation/
│   │   │   │   ├── maximum-likelihood-estimation.md
│   │   │   │   ├── method-of-moments.md
│   │   │   │   └── point-estimation.md
│   │   │   ├── hypothesis-testing/
│   │   │   │   ├── chi-square-test.md
│   │   │   │   ├── foundations.md
│   │   │   │   ├── homogeneity-test.md
│   │   │   │   ├── p-values.md
│   │   │   │   ├── t-test.md
│   │   │   │   └── z-test.md
│   │   │   ├── time-series/
│   │   │   │   ├── autocorrelation.md
│   │   │   │   ├── foundations.md
│   │   │   │   ├── stationarity.md
│   │   │   │   ├── time-series-decomposition.md
│   │   │   │   └── trend-and-seasonality.md
│   │   │   ├── bias.md
│   │   │   ├── confidence-intervals.md
│   │   │   ├── method-of-least-squares.md
│   │   │   └── statistical-power.md
│   │   ├── 07-topology/
│   │   │   ├── distances/
│   │   │   │   ├── bottleneck-distance.md
│   │   │   │   └── wasserstein-distance.md
│   │   │   ├── homology/
│   │   │   │   ├── alexander-duality.md
│   │   │   │   ├── betti-numbers.md
│   │   │   │   ├── chain-complexes.md
│   │   │   │   ├── fundamental-lemma-of-homology.md
│   │   │   │   ├── homology-groups.md
│   │   │   │   └── what-is-homology.m d
│   │   │   ├── homotopy/
│   │   │   │   ├── fundamental-group.md
│   │   │   │   ├── homotopy-equivalence.md
│   │   │   │   ├── homotopy-groups.md
│   │   │   │   ├── homotopy-type.md
│   │   │   │   └── what-is-homotopy.md
│   │   │   ├── topological-spaces/
│   │   │   │   ├── important-manifolds/
│   │   │   │   │   ├── klein-bottle.md
│   │   │   │   │   ├── möbius-strip.md
│   │   │   │   │   ├── sphere.md
│   │   │   │   │   └── torus.md
│   │   │   │   ├── triangulations.md
│   │   │   │   ├── what-are-manifolds.md
│   │   │   │   └── what-are-topological-spaces.md
│   │   │   ├── euler-characteristic.md
│   │   │   ├── topological-equivalence.md
│   │   │   ├── topological-stability.md
│   │   │   └── what-is-topology.md
│   │   ├── 08-graph-theory/
│   │   │   ├── search-algorithms/
│   │   │   │   ├── a-star.md
│   │   │   │   ├── breadth-first-search.md
│   │   │   │   ├── depth-first-search.md
│   │   │   │   └── dijkstra.md
│   │   │   ├── graph-traversal.md
│   │   │   ├── graphs.md
│   │   │   ├── random-graphs.md
│   │   │   ├── shortest-paths.md
│   │   │   └── trees.md
│   │   └── 09-information-theory/
│   │       ├── cross-entropy.md
│   │       ├── information-entropy.md
│   │       ├── information-gain.md
│   │       ├── kl-divergence.md
│   │       └── mutual-information.md
│   ├── 02-ml-models-theory/
│   │   ├── 01-ml-foundations/
│   │   │   ├── bias-variance-tradeoff.md
│   │   │   ├── calibration.md
│   │   │   ├── classification-of-ml-models.md
│   │   │   ├── curse-of-dimensionality.md
│   │   │   ├── data-distribution-shift.md
│   │   │   ├── empirical-risk-minimization.md
│   │   │   ├── hypothesis-space.md
│   │   │   ├── inductive-bias.md
│   │   │   ├── kernel-methods.md
│   │   │   ├── no-free-lunch-theorem.md
│   │   │   ├── overfitting-and-underfitting.md
│   │   │   ├── pac-learning.md
│   │   │   ├── regularization.md
│   │   │   ├── uniform-convergence.md
│   │   │   ├── universal-approximation-theorem.md
│   │   │   ├── vc-dimension.md
│   │   │   └── what-is-machine-learning.md
│   │   ├── 02-ml-tasks/
│   │   │   ├── anomaly-detection/
│   │   │   ├── classification/
│   │   │   ├── clustering/
│   │   │   ├── computer-vision/
│   │   │   ├── dimensionality-reduction/
│   │   │   ├── forecasting/
│   │   │   ├── generative-modeling/
│   │   │   ├── natural-language-processing/
│   │   │   │   ├── anonymization.md
│   │   │   │   ├── bag-of-words.md
│   │   │   │   ├── count-vectorizer.md
│   │   │   │   ├── named-entity-recognition.md
│   │   │   │   ├── stopwords-and-stemming.md
│   │   │   │   └── tf-idf.md
│   │   │   ├── ranking/
│   │   │   ├── recommendation-systems/
│   │   │   ├── regression/
│   │   │   └── topic-modelling/
│   │   ├── 03-traditional-ml-models/
│   │   │   ├── 01-supervised/
│   │   │   │   ├── linear-models/
│   │   │   │   │   ├── elastic-net.md
│   │   │   │   │   ├── lasso-regression.md
│   │   │   │   │   ├── linear-regression.md
│   │   │   │   │   └── ridge-regression.md
│   │   │   │   ├── nearest-neighbors/
│   │   │   │   │   └── knn-classification.md
│   │   │   │   ├── tree-based-methods/
│   │   │   │   │   ├── decision-trees.md
│   │   │   │   │   ├── random-forest.md
│   │   │   │   │   └── xgboost.md
│   │   │   │   ├── gaussian-processes.md
│   │   │   │   ├── naive-bayes.md
│   │   │   │   └── svm.md
│   │   │   ├── 02-unsupervised/
│   │   │   │   ├── clustering/
│   │   │   │   │   ├── dbscan.md
│   │   │   │   │   ├── density-estimation.md
│   │   │   │   │   ├── hierarchical-clustering.md
│   │   │   │   │   └── k-means.md
│   │   │   │   └── dimenstionality-reduction/
│   │   │   │       ├── pca.md
│   │   │   │       └── umap.md
│   │   │   ├── 03-probabilistic/
│   │   │   │   ├── bayesian-networks.md
│   │   │   │   ├── gaussian-mixture-models.md
│   │   │   │   └── hidden-markov-models.md
│   │   │   └── 04-time-series-models/
│   │   │       ├── arima.md
│   │   │       ├── autoregressive-models.md
│   │   │       └── kalman-filter.md
│   │   ├── 04-deep-learning-models/
│   │   │   ├── 01-architectures/
│   │   │   │   ├── activation-functions/
│   │   │   │   │   ├── leaky-relu.md
│   │   │   │   │   ├── relu.md
│   │   │   │   │   ├── sigmoid.md
│   │   │   │   │   ├── softmax.md
│   │   │   │   │   └── tanh.md
│   │   │   │   ├── autoencoders.md
│   │   │   │   ├── cnn-architectures.md
│   │   │   │   ├── graph-neural-networks.md
│   │   │   │   ├── neural-network-basics.md
│   │   │   │   ├── rnn-lstm.md
│   │   │   │   ├── siamese-architecture.md
│   │   │   │   └── transformers.md
│   │   │   ├── 02-generative-models/
│   │   │   │   ├── autoregressive-models.md
│   │   │   │   ├── diffusion-models.md
│   │   │   │   ├── energy-based-models.md
│   │   │   │   ├── generative-adversarial-networks.md
│   │   │   │   ├── multimodal-generative-models.md
│   │   │   │   ├── normalizing-flows.md
│   │   │   │   ├── score-based-models.md
│   │   │   │   └── variational-autoencoders.md
│   │   │   ├── 03-learning-paradigms/
│   │   │   │   ├── federated-learning.md
│   │   │   │   ├── few-shot-learning.md
│   │   │   │   ├── meta-learning.md
│   │   │   │   ├── self-supervised-learning.md
│   │   │   │   └── transfer-learning.md
│   │   │   └── 04-representation-learning/
│   │   │       ├── embeddings.md
│   │   │       ├── sentence-embeddings.md
│   │   │       └── word-embeddings.md
│   │   ├── 05-reinforcement-learning/
│   │   │   ├── agents.md
│   │   │   └── policy-gradient-methods.md
│   │   └── 06-llms/
│   │       ├── 01-foundations/
│   │       │   ├── tokenization.md
│   │       │   └── what-are-llms.md
│   │       ├── 02-transformer-architecture/
│   │       │   ├── decoder-only-models.md
│   │       │   ├── multi-head-attention.md
│   │       │   ├── positional-encoding.md
│   │       │   └── self-attention.md
│   │       ├── 03-model-architectures/
│   │       │   ├── gpt-family.md
│   │       │   ├── llama-family.md
│   │       │   ├── mixture-of-experts.md
│   │       │   └── multimodal-llms.md
│   │       └── 05-llm-applications/
│   │           └── rag.md
│   ├── 03-data-exploration/
│   │   ├── 01-chart-types/
│   │   │   ├── bar-chart.md
│   │   │   ├── box-plots.md
│   │   │   ├── bubble-chart.md
│   │   │   ├── correlation-matrix.md
│   │   │   ├── heatmap.md
│   │   │   ├── histograms.md
│   │   │   ├── line-chart.md
│   │   │   ├── pie-chart.md
│   │   │   ├── scatter-plot.md
│   │   │   └── violin-plot.md
│   │   ├── 02-statistical-analysis/
│   │   │   ├── correlation.md
│   │   │   ├── kurtosis.md
│   │   │   ├── outliers.md
│   │   │   └── skewness.md
│   │   ├── 03-data-quality/
│   │   │   ├── missing-data.md/
│   │   │   └── duplicate-detection-techniques.md
│   │   ├── data-types.md
│   │   └── visualization-best-practices.md
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
│   │   │   └── confidence.md
│   │   ├── 05-interpretability/
│   │   │   ├── feature-importance.md
│   │   │   └── shap.md
│   │   ├── 06-calibration/
│   │   ├── 07-llm-evaluation/
│   │   │   ├── human-evaluation.md
│   │   │   ├── llm-as-a-judge.md
│   │   │   ├── quality-metrics.md
│   │   │   ├── rag-evaluation.md
│   │   │   └── safety-and-reliability.md
│   │   ├── cross-validation.md
│   │   ├── fairness-bias.md
│   │   └── model-selection.md
│   ├── 05-data-engineering/
│   │   ├── 01-data-pipelines/
│   │   ├── 02-data-preprocessing/
│   │   │   ├── 01-data-cleaning/
│   │   │   │   └── 02-/
│   │   │   ├── 02-data-transformation/
│   │   │   ├── 03-imputation/
│   │   │   │   ├── knn-imputation.md
│   │   │   │   └── mean-imputation.md
│   │   │   ├── 04-outlier-detection/
│   │   │   └── 05-data-normalization/
│   │   ├── 03-data-versioning/
│   │   ├── 04-distributed-processing/
│   │   │   ├── hadoop/
│   │   │   └── spark/
│   │   └── 05-feature-engineering/
│   ├── 05-training-and-optimizing-ml-models/
│   │   ├── 01-traditional-ml/
│   │   │   ├── hyperparameter-tuning/
│   │   │   └── common-issues.md
│   │   ├── 02-deep-learning/
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
│   │   │   ├── 04-data-strategies/
│   │   │   │   └── data-augmentation.md/
│   │   │   ├── 05-activation-functions/
│   │   │   └── common-issues.md
│   │   └── 03-llms/
│   │       ├── finetuning/
│   │       ├── promt-engineering/
│   │       └── tools/
│   ├── 07-databases/
│   │   ├── 01-sql-databases/
│   │   │   ├── joins.md
│   │   │   └── relational-model.md
│   │   ├── 02-nosql-databses/
│   │   ├── 03-vector-databases.md/
│   │   ├── 04-search-engines/
│   │   │   ├── elasticsearch.md
│   │   │   └── vector-search.md
│   │   ├── 05-data-warehouses/
│   │   └── 06-datalakes/
│   ├── 08-deployment/
│   │   ├── 01-fundamentals/
│   │   │   ├── api-design.md
│   │   │   ├── caching.md
│   │   │   ├── containerization.md
│   │   │   ├── inference-endpoints.md
│   │   │   ├── model-serialization.md
│   │   │   └── model-serving.md
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
│   │   ├── 04-cloud-native/
│   │   │   ├── destination-rule.md
│   │   │   ├── gateways.md
│   │   │   ├── istio.md
│   │   │   ├── s3.md
│   │   │   ├── service-mesh.md
│   │   │   └── virtual-service.md
│   │   ├── 05-openshift/
│   │   │   ├── foundations.md
│   │   │   ├── operators.md
│   │   │   └── routes.md
│   │   └── 06-ml-serving/
│   │       ├── inference-services.md
│   │       ├── kserve.md
│   │       ├── model-serving.md
│   │       └── serving-architecture.md
│   ├── 09-mlops/
│   │   ├── 01-ci-cd/
│   │   │   ├── github-actions.md
│   │   │   └── jenkins.md
│   │   ├── 02-experiment-tracking/
│   │   │   └── mlflow.md
│   │   ├── 03-model-registry/
│   │   │   └── model-artifacts.md
│   │   ├── 04-orchestration/
│   │   │   ├── argo-cd.md
│   │   │   ├── argo-workflows.md
│   │   │   └── kubeflow.md
│   │   ├── 05-monitoring/
│   │   │   ├── alerts.md
│   │   │   ├── grafana-foundations.md
│   │   │   ├── metrics.md
│   │   │   ├── model-monitoring.md
│   │   │   └── performance-monitoring.md
│   │   └── 06-ml-pipelines/
│   │       ├── kubeflow-pipelines.md
│   │       └── pipeline-foundations.md
│   ├── 10-software-engineering/
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
│   │   ├── 08-security-and-data-protection/
│   │   │   ├── anonymization-and-pseudonomysation.md
│   │   │   ├── authentication.md
│   │   │   ├── authorization.md
│   │   │   ├── dependency-security.md
│   │   │   ├── dsvgo-basics.md
│   │   │   ├── llm-safety.md
│   │   │   ├── policy-management.md
│   │   │   └── secrets-management.md
│   │   ├── 09-architectures/
│   │   │   ├── honeycomb-architecture.md
│   │   │   └── monolith-vs-microservices.md
│   │   ├── 10-debugging/
│   │   │   ├── debugging-deployments.md
│   │   │   ├── debugging-ml-models.md
│   │   │   ├── logging.md
│   │   │   └── profiling.md
│   │   ├── 11-web-development/
│   │   │   ├── api-testing.md
│   │   │   ├── openapi-swagger.md
│   │   │   └── rest-api-foundations.md
│   │   └── 12-data-structures/
│   │       ├── heap.md
│   │       └── linked-list.md
│   └── 11-tda/
│       ├── perstistent-homology/
│       │   ├── applications/
│       │   │   ├── ts-classification.md
│       │   │   └── ts-forecasting.md
│       │   ├── barcodes.md
│       │   ├── cech-complex.md
│       │   ├── filtrations.md
│       │   ├── nerve-complexes.md
│       │   ├── persistence-diagrams.md
│       │   ├── vietoris-rips-complex.md
│       │   └── why-persistence-homology-works.md
│       └── mapper-algorithm.md
├── assets/
└── scripts/
    └── generate-toc.py
```
<!-- TOC_END -->
