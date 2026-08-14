# OpenShift AI

## TL;DR

**Red Hat OpenShift AI** is an AI/ML platform built on OpenShift that provides tools for the ML lifecycle, including **workbenches, pipelines, model registries, model serving, and monitoring**.

For pipelines and model registries, OpenShift AI provides a UI on top of underlying services:

```text
                    OpenShift AI
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
   AI Pipelines                   Model Registry
          │                             │
          ▼                             ▼
 Kubeflow Pipelines              Model Metadata
          │                             │
          ▼                             ▼
    Kubernetes                    MySQL Database
```

This makes it possible to manage ML workflows and models directly from the OpenShift AI dashboard.

---

## AI Pipelines

OpenShift AI provides an **AI Pipelines** interface based on **Kubeflow Pipelines 2.x**. Pipelines can be defined using the Kubeflow Pipelines SDK and compiled into YAML.

The workflow is:

```text
Python Pipeline
      │
      ▼
Kubeflow Pipelines SDK
      │
      ▼
Pipeline YAML
      │
      ▼
OpenShift AI
      │
      ▼
Pipeline Server
      │
      ▼
Pipeline Runs
```

---

## Pipeline Server

To use pipelines in an OpenShift AI project, a **Pipeline Server** must be configured for the project. The server hosts the pipelines and their metadata.

A typical setup is:

```text
OpenShift AI Project
        │
        ▼
 Pipeline Server
     ┌──┴──┐
     ▼     ▼
  Storage  Database
     │
     ▼
Pipeline Artifacts
```

OpenShift AI supports S3-compatible object storage for pipeline artifacts. Pipeline metadata and run information can be stored in a database.

---

## Showing a Kubeflow Pipeline in OpenShift AI

A pipeline is normally written with the **Kubeflow Pipelines SDK**:

```python
from kfp import dsl

@dsl.pipeline
def training_pipeline():
    preprocess = preprocess_component()

    train = train_component(
        data=preprocess.output
    )
```

The pipeline is then compiled:

```python
from kfp import compiler

compiler.Compiler().compile(
    training_pipeline,
    "training-pipeline.yaml"
)
```

The resulting YAML can be imported into the OpenShift AI dashboard. OpenShift AI then displays the pipeline and allows it to be run, scheduled, versioned, and monitored.

```text
training_pipeline.py
        │
        ▼
   KFP Compiler
        │
        ▼
training-pipeline.yaml
        │
        ▼
   OpenShift AI
        │
        ▼
     Pipeline
        │
        ├── Versions
        ├── Runs
        └── Experiments
```

---

## Kubernetes-Native Pipelines

OpenShift AI can also store pipeline definitions as **Kubernetes resources** instead of relying only on the internal pipeline database.

This is particularly useful for GitOps:

```text
Git Repository
      │
      ▼
Pipeline YAML / CRs
      │
      ▼
   Argo CD
      │
      ▼
  Kubernetes
      │
      ▼
OpenShift AI
```

This allows pipeline definitions and versions to be managed through Git and deployed using tools such as OpenShift GitOps/Argo CD.

---

## Model Registry

OpenShift AI also provides a **Model Registry** for storing and managing model metadata.

A registry can contain:

```text
Model
 │
 ├── Version 1
 ├── Version 2
 └── Version 3
```

Each version can contain metadata such as:

* Model format
* Model location
* Labels
* Description
* Properties
* Deployment information

The registry provides a central place to **register, version, track, and deploy models**.

---

## Enabling the Model Registry

The Model Registry component must be enabled in the OpenShift AI installation.

In OpenShift AI 2.25, for example, this is controlled through the `DataScienceCluster` resource:

```yaml
spec:
  components:
    modelregistry:
      managementState: Managed
      registriesNamespace: rhoai-model-registries
```

New OpenShift AI 2.25 installations have the component enabled by default, while upgraded installations may require it to be enabled.

---

## Creating a Model Registry

An OpenShift AI administrator can create a model registry from the OpenShift AI dashboard.

The registry uses an external database for storing its model metadata. Red Hat recommends MySQL 8.x for this purpose.

Conceptually:

```text
             OpenShift AI
                  │
                  ▼
            Model Registry
                  │
                  ▼
             MySQL Database
```

The actual model files do not necessarily have to be stored inside the registry. The registry primarily manages **metadata and references to model artifacts**.

---

## Registering a Model

A trained model can be registered through the OpenShift AI dashboard:

```text
Trained Model
     │
     ▼
Model Registry
     │
     ├── Model
     │    ├── Version 1
     │    └── Version 2
     │
     └── Metadata
```

A model version can reference a model stored in object storage and contain information such as its format and version.

---

## Pipeline + Model Registry

The two components can be combined into an end-to-end MLOps workflow:

```text
                 Git
                  │
                  ▼
             KFP Pipeline
                  │
          ┌───────┴────────┐
          ▼                ▼
     Preprocessing       Training
                           │
                           ▼
                       Evaluation
                           │
                     ┌─────┴─────┐
                     │           │
                   Failed      Passed
                     │           │
                     ▼           ▼
                    Stop    Model Registry
                                  │
                                  ▼
                              Model v2
                                  │
                                  ▼
                             Model Serving
```

The pipeline can therefore train and evaluate a model and then register the resulting model in the OpenShift AI Model Registry.

---

## MLflow vs. OpenShift AI Model Registry

It is useful to distinguish **experiment tracking** from **model registration**:

```text
MLflow
├── Experiments
├── Runs
├── Parameters
├── Metrics
└── Artifacts

OpenShift AI Model Registry
├── Models
├── Model Versions
├── Metadata
└── Deployment Information
```

They can be used together. For example, a Kubeflow Pipeline can use MLflow for experiment tracking and the OpenShift AI Model Registry for model lifecycle management.

---

## OpenShift AI Architecture

The relevant components can be viewed as:

```text
                         OpenShift AI
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
   Workbenches          AI Pipelines          Model Registry
                              │                     │
                              ▼                     ▼
                     Kubeflow Pipelines          MySQL
                              │
                              ▼
                         Kubernetes
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
                Training            Model Serving
```

OpenShift AI therefore provides a common interface for managing these components rather than requiring users to interact with every underlying service separately.

---

## Key Idea

OpenShift AI does **not replace Kubeflow Pipelines**. Instead, its AI Pipelines functionality provides an OpenShift AI interface for working with Kubeflow Pipelines-based workflows.

The same idea applies to the Model Registry:

```text
                    OpenShift AI
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
     AI Pipelines                 Model Registry
          │                             │
          ▼                             ▼
 Kubeflow Pipelines             Model Metadata
          │                             │
          └──────────────┬──────────────┘
                         ▼
                    MLOps Platform
```

This allows an OpenShift-based ML platform to combine **pipeline orchestration, experiment workflows, model management, and model serving** in one environment.
