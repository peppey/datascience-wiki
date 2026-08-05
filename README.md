## Table of Contents

<!-- TOC_START -->
```text
data-science-wiki/
├── README.md
├── docs/
│   ├── 01-mathematical-foundations/
│   │   ├── 01-functional-analysis/
│   │   │   └── hilbert-spaces.md
│   │   ├── 02-optimization/
│   │   ├── 03-statistics/
│   │   │   ├── bayesian-inference.md
│   │   │   ├── causal-inference.md
│   │   │   └── statistical-testing.md
│   │   ├── 04-topology/
│   │   └── 05-geometry/
│   ├── 02-ml-models-theory/
│   │   ├── 01-ml-foundations/
│   │   │   ├── 01-what-is-machine-learning
│   │   │   ├── 02-classification-of-ml-models.md
│   │   │   ├── bias-variance-tradeoff.md
│   │   │   ├── empirical-risk-minimization.md
│   │   │   ├── kernel-methods.md
│   │   │   ├── pac-learning.md
│   │   │   ├── regularization.md
│   │   │   ├── uniform-convergence.md
│   │   │   ├── universal-approximation-theorem.md
│   │   │   └── vc-dimension.md
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
│   │   │   └── 03-probabilistic/
│   │   │       ├── bayesian-networks.md
│   │   │       ├── gaussian-mixture-models.md
│   │   │       └── hidden-markov-models.md
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
│   │   ├── 02-regression-metrics/
│   │   ├── 03-uncertainty-quantification/
│   │   ├── cross-validation.md
│   │   ├── fairness-bias.md
│   │   └── model-selection.md
│   ├── 05-data-engineering/
│   │   ├── 01-data-pipelines/
│   │   ├── 02-feature-engineering/
│   │   └── 03-data-versioning/
│   ├── 06-databases/
│   │   ├── 01-sql-databases/
│   │   ├── 02-nosql-databses/
│   │   └── 03-vector-databases.md/
│   ├── 07-deployment/
│   │   └── 01-fundamentals/
│   │       ├── api-design.md
│   │       ├── containerization.md
│   │       └── model-serialization.md
│   ├── 08-mlops/
│   │   ├── 01-ci-cd/
│   │   │   ├── github-actions.md
│   │   │   └── jenkins.md
│   │   ├── 02-experiment-tracking/
│   │   ├── 03-model-registry/
│   │   ├── 04-orchestration/
│   │   └── 05-monitoring/
│   ├── 09-software-engineering/
│   │   ├── 01-clean-code/
│   │   ├── 02-testing/
│   │   │   ├── 01-unit-tests/
│   │   │   ├── 02-integration-tests/
│   │   │   └── 03-e2e-tests/
│   │   ├── 03-documentation/
│   │   ├── 04-reproducibility/
│   │   └── 06-design-patterns/
│   └── 10-tda/
│       └── 01-persistence-homology/
├── assets/
└── scripts/
    └── generate-toc.py
```
<!-- TOC_END -->
