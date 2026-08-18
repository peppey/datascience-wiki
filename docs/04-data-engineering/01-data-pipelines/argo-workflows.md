# Argo Workflows

## TL;DR

**Argo Workflows** is a Kubernetes-native workflow engine for running **multi-step jobs and pipelines**.

A workflow consists of a sequence or graph of **tasks**, where each task typically runs as a Kubernetes Pod.

It is commonly used for:

* data processing
* machine learning pipelines
* batch jobs
* CI/CD workflows
* automation

---

## Basic Structure

An Argo Workflow is defined using a Kubernetes YAML resource:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: example-
spec:
  entrypoint: main

  templates:
    - name: main
      steps:
        - - name: hello
            template: hello

    - name: hello
      container:
        image: alpine
        command: [echo]
        args: ["Hello World"]
```

The workflow is submitted to the Kubernetes cluster, where the **Argo Workflow Controller** manages its execution.

---

## Templates

A workflow consists of reusable **templates**.

A template can define, for example:

* a container
* a sequence of steps
* a DAG
* inputs and outputs
* scripts

For example:

```yaml
- name: train-model
  container:
    image: my-training-image
    command: ["python"]
    args: ["train.py"]
```

---

## Steps

**Steps** execute tasks sequentially or in parallel.

```yaml
steps:
  - - name: preprocess
      template: preprocess

  - - name: train
      template: train
    - name: evaluate
      template: evaluate
```

Here, `preprocess` runs first.

Afterwards, `train` and `evaluate` can run in parallel.

---

## DAG

For more complex dependencies, Argo Workflows supports **DAGs (Directed Acyclic Graphs)**.

```yaml
dag:
  tasks:
    - name: preprocess
      template: preprocess

    - name: train
      template: train
      dependencies:
        - preprocess

    - name: evaluate
      template: evaluate
      dependencies:
        - train
```

The dependency graph is:

$$
\text{preprocess}
\rightarrow
\text{train}
\rightarrow
\text{evaluate}
$$

DAGs are useful when workflows contain complex dependencies between tasks.

---

## Workflow Execution

The basic lifecycle is:

$$
\boxed{
\text{Workflow YAML}
\rightarrow
\text{Submit}
\rightarrow
\text{Pods}
\rightarrow
\text{Tasks}
\rightarrow
\text{Workflow Result}
}
$$

The **Workflow Controller** watches workflow resources and creates the required Kubernetes resources.

---

## Inputs and Outputs

Tasks can exchange parameters and artifacts.

For example:

```text
preprocess
    ↓
data.csv
    ↓
train
    ↓
model.pkl
    ↓
evaluate
```

Artifacts can be stored in object storage such as **S3**.

This makes Argo Workflows useful for data and ML pipelines.

---

## CronWorkflows

A **CronWorkflow** runs a workflow according to a schedule.

For example:

```yaml
schedule: "0 2 * * *"
```

This can be used to execute a workflow every day at 02:00.

Typical use cases include:

* scheduled data processing
* model retraining
* periodic batch jobs
* maintenance tasks

---

## Argo Workflows vs. Kubernetes Jobs

A **Kubernetes Job** primarily represents a single batch workload.

An **Argo Workflow** can coordinate many Kubernetes workloads with dependencies:

```text
Job
  ↓
Job
  ↓
Job
```

Therefore:

* **Job** → run a batch task
* **Workflow** → orchestrate multiple tasks

---

## Argo Workflows vs. Argo CD

These two Argo projects serve different purposes.

**Argo Workflows**:

> Executes workflows and jobs.

**Argo CD**:

> Continuously synchronizes Kubernetes resources from Git.

A typical setup might therefore use:

$$
\text{Git}
\xrightarrow{\text{Argo CD}}
\text{Kubernetes}
\xrightarrow{\text{Argo Workflows}}
\text{Workflow Execution}
$$

---

## Key Takeaway

Argo Workflows is a Kubernetes-native engine for orchestrating **multi-step workflows**.

The central concepts are:

* **Workflow** — complete workflow definition
* **Template** — definition of a task or workflow component
* **Step** — sequential/parallel execution
* **DAG** — dependency graph
* **Artifact** — data exchanged between tasks
* **CronWorkflow** — scheduled workflow

Its main advantage is that workflow execution is directly integrated with **Kubernetes**.
