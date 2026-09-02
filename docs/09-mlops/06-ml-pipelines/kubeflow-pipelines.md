# Kubeflow Pipelines

## TL;DR (30 seconds)

**Kubeflow Pipelines (KFP)** is a platform for defining, running, and monitoring **machine learning workflows on Kubernetes**.

A workflow is defined as a **DAG (Directed Acyclic Graph)** consisting of individual **components**:

```text id="kbe9sl"
Dataset
   │
   ▼
Preprocessing
   │
   ▼
Training
   │
   ├──────────────┐
   ▼              ▼
Evaluation      Model
   │
   ▼
Deployment
```

Each step typically runs in its own container or Pod. KFP handles orchestration, dependencies, artifacts, logs, and execution of the pipeline.

---

## 1. Pipeline

A **Pipeline** describes an entire ML workflow and defines:

* which steps are executed
* the order in which they are executed
* which data is passed between steps
* which parameters are used
* which steps can run in parallel

A pipeline can be defined using the KFP Python SDK:

```python id="q7k3p1"
from kfp import dsl

@dsl.pipeline
def ml_pipeline():
    preprocess = preprocess_data()
    train = train_model(dataset=preprocess.output)
    evaluate = evaluate_model(model=train.output)
```

The function describes the workflow. It does not directly execute the steps. The pipeline is first compiled and then submitted to the KFP backend.

---

## 2. Components

**Components** are the individual building blocks of a pipeline.

```text id="7ari7g"
Component
    │
    ├── Input
    │
    ▼
 Python code
    │
    ▼
 Output
```

For example:

```python id="k2m8x4"
from kfp import dsl

@dsl.component
def preprocess(data_path: str) -> str:
    # preprocessing
    return "processed_data.csv"
```

Components can perform tasks such as:

* loading data
* preprocessing
* feature engineering
* model training
* model evaluation
* model storage
* model deployment

A component typically runs as a container when the pipeline is executed.

---

## 3. Tasks

When a component is used inside a pipeline, it creates a **Task**.

```python id="f5n2c8"
task = preprocess(data_path="data.csv")
```

The task represents a concrete execution of a component with specific inputs.

Tasks can depend on each other:

```text id="bymf4n"
Task A
  │
  ▼
Task B
  │
  ▼
Task C
```

Tasks without dependencies can run in parallel.

---

## 4. Parameters and Artifacts

Data can be passed between components in two main ways.

### Parameters

Parameters are used for relatively small values:

```text id="qngqaw"
learning_rate = 0.01
epochs = 10
model_name = "xgboost"
```

For example:

```python id="r8v4m2"
@dsl.component
def train(learning_rate: float, epochs: int):
    ...
```

### Artifacts

**Artifacts** represent larger files or ML outputs:

```text id="551wcb"
Dataset
Model
Metrics
HTML
Markdown
```

For example:

```text id="vl4c1t"
Preprocessing
     │
     │ Dataset
     ▼
Training
     │
     │ Model
     ▼
Evaluation
     │
     │ Metrics
     ▼
```

KFP provides artifact types such as `Dataset`, `Model`, and `Metrics`.

---

## 5. Pipeline Runs

A Pipeline is a **definition**. A **Run** is one concrete execution of that pipeline.

```text id="bgkaqq"
Pipeline
   │
   ├── Run 1 → Dataset A, parameters A
   ├── Run 2 → Dataset B, parameters B
   └── Run 3 → Dataset C, parameters C
```

A run can contain information such as:

* task status
* logs
* execution time
* parameters
* artifacts
* metadata

This makes individual pipeline executions reproducible and traceable.

---

## 6. Experiments

**Experiments** group multiple pipeline runs.

```text id="b30ddr"
Experiment: XGBoost Hyperparameter Search
│
├── Run 1: learning_rate = 0.01
├── Run 2: learning_rate = 0.05
└── Run 3: learning_rate = 0.10
```

This is useful when running the same ML workflow with different parameters.

---

## 7. Pipeline Compilation

The Python pipeline is not directly executed as Python code.

Instead, it is compiled:

```text id="1lzyhp"
Python Pipeline
      │
      ▼
KFP Compiler
      │
      ▼
Pipeline IR
      │
      ▼
KFP Backend
      │
      ▼
Kubernetes Pods
```

The **KFP compiler** converts the pipeline definition into an intermediate representation that can be submitted to the KFP backend.

---

## 8. Execution on Kubernetes

KFP orchestrates the pipeline on Kubernetes.

For example:

```text id="7ad2uk"
KFP Pipeline
     │
     ▼
┌───────────────┐
│ Preprocessing │ ──► Pod
└───────────────┘
        │
        ▼
┌───────────────┐
│   Training    │ ──► Pod
└───────────────┘
        │
        ▼
┌───────────────┐
│  Evaluation   │ ──► Pod
└───────────────┘
```

Each step can use its own container image and dependencies.

---

## 9. Caching

KFP can **cache the results of previously executed tasks**.

If a task is executed again with the same relevant inputs, its previous result can potentially be reused:

```text id="tnw4c8"
Run 1
Training
   │
   ▼
Model A

Run 2
Training
   │
   └── same inputs
          │
          ▼
       Cache Hit
          │
          ▼
       Model A
```

This is particularly useful for expensive operations such as model training.

---

## 10. Recurring Runs

A pipeline can also be executed on a recurring schedule.

For example:

```text id="aanl7i"
         daily
           │
           ▼
      ┌──────────┐
      │ Pipeline │
      └──────────┘
           │
     ┌─────┼─────┐
     ▼     ▼     ▼
    Run   Run   Run
```

This can be useful for regular data processing or model retraining.

---

## 11. Typical ML Workflow

A production ML pipeline might look like this:

```text id="nrual6"
             Dataset
                │
                ▼
        ┌──────────────┐
        │ Preprocessing│
        └──────────────┘
                │
                ▼
        ┌──────────────┐
        │   Training   │
        └──────────────┘
                │
                ▼
        ┌──────────────┐
        │  Evaluation  │
        └──────────────┘
             │      │
          failed   passed
             │      │
             ▼      ▼
           Stop    Model
                    │
                    ▼
                Deployment
```

This allows the complete ML process to be described and executed in a reproducible way.

---

## 12. KFP vs. Kubernetes

Kubernetes provides the underlying infrastructure:

```text id="v8o55h"
Kubernetes
├── Pods
├── Services
├── Deployments
├── Storage
└── Networking
```

Kubeflow Pipelines adds ML-specific workflow orchestration:

```text id="e7udrj"
Kubeflow Pipelines
├── Pipelines
├── Components
├── Tasks
├── Runs
├── Experiments
└── Artifacts
```

KFP therefore abstracts much of the low-level Kubernetes orchestration required for ML workflows.

---

## 13. KFP vs. KServe

The two tools have different purposes:

|               | Kubeflow Pipelines       | KServe                   |
| ------------- | ------------------------ | ------------------------ |
| Main purpose  | Orchestrate ML workflows | Serve ML models          |
| Typical stage | Training / Processing    | Inference                |
| Example       | Train a model            | Expose a model as an API |
| Main resource | Pipeline                 | InferenceService         |
| Result        | Model artifact           | Inference endpoint       |

They can be combined:

```text id="48v024"
Kubeflow Pipeline
      │
      ├── Data Processing
      │
      ├── Training
      │
      ├── Evaluation
      │
      └── Model Artifact
               │
               ▼
             KServe
               │
               ▼
        Inference Endpoint
```

## Key Takeaways

1. **Kubeflow Pipelines** orchestrates ML workflows on Kubernetes.
2. A pipeline consists of **components** that are executed as tasks.
3. Components typically run in **containers/Pods**.
4. **Parameters** transfer small values, while **artifacts** represent larger ML data and results.
5. A **Run** is a concrete execution of a pipeline.
6. KFP supports features such as **caching, parallel execution, retries, and recurring runs**.
7. KFP is primarily used for **ML workflows**, while KServe is used for **model serving**.
