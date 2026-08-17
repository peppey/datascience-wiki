# MLflow

## TL;DR

**MLflow** is an open-source platform for managing the **machine learning lifecycle**.

It can be used to track experiments, store models, manage datasets and artifacts, and support model deployment.

The basic workflow is:

$$
\boxed{
\text{Experiment}
\rightarrow
\text{Run}
\rightarrow
\text{Metrics}
\rightarrow
\text{Model}
}
$$

---

## Experiments

An **experiment** groups related ML runs.

For example:

```text
Experiment: Image Classification
        │
        ├── Run 1
        ├── Run 2
        └── Run 3
```

Experiments make it easier to compare different approaches.

---

## Runs

A **run** represents one execution of an ML experiment.

A run can store:

* Parameters
* Metrics
* Artifacts
* Model
* Metadata

For example:

```python
import mlflow

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.001)
    mlflow.log_metric("accuracy", 0.94)
```

---

## Parameters and Metrics

**Parameters** describe the configuration of a model:

```text
learning_rate = 0.001
batch_size    = 32
max_depth     = 10
```

**Metrics** describe the model's performance:

```text
accuracy = 0.94
loss     = 0.12
f1       = 0.91
```

MLflow stores these values so different runs can be compared.

---

## Artifacts

**Artifacts** are files produced during an ML run.

Examples include:

```text
model.pkl
plots.png
metrics.json
requirements.txt
```

They can be logged with:

```python
mlflow.log_artifact("plot.png")
```

---

## Model Tracking

MLflow can log trained models:

```python
mlflow.sklearn.log_model(
    model,
    "model"
)
```

This connects the trained model to the parameters and metrics of the corresponding run.

```text
Run
 │
 ├── Parameters
 ├── Metrics
 ├── Artifacts
 └── Model
```

---

## Model Registry

The **Model Registry** provides a central place to manage models.

A model can move through different lifecycle stages:

```text
Training
   │
   ▼
Registered Model
   │
   ▼
Validation
   │
   ▼
Production
```

This makes it easier to track which model version is currently deployed.

---

## MLflow Tracking Server

MLflow can use a central **Tracking Server** to store experiment information.

```text
┌──────────────┐
│ ML Training  │
└──────┬───────┘
       │
       ▼
┌─────────────────┐
│ MLflow Tracking │
│     Server      │
└──────┬──────────┘
       │
       ├── Metrics
       ├── Parameters
       └── Artifacts
```

This allows multiple users or training jobs to share experiment information.

---

## MLflow in CI/CD

MLflow can be integrated into ML pipelines:

```text
Git
 │
 ▼
CI Pipeline
 │
 ▼
Train Model
 │
 ▼
MLflow
 │
 ├── Log Metrics
 ├── Log Artifacts
 └── Register Model
        │
        ▼
     Deploy
```

For example, Jenkins or GitHub Actions can trigger training and log the resulting model to MLflow.

---

## Key Idea

MLflow helps make machine learning experiments **trackable, reproducible, and manageable**.

The central concept is:

```text
Experiment
    │
    ▼
   Run
    │
    ├── Parameters
    ├── Metrics
    ├── Artifacts
    └── Model
```

MLflow is therefore commonly used as the **experiment tracking and model management component of an ML platform**.
