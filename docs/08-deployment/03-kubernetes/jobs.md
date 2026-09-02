# Kubernetes Jobs

## TL;DR (30 seconds)

A **Kubernetes Job** is a resource used to **run a task until it successfully completes**.

The key idea:

> **A Job creates one or more Pods and ensures that a specified number of successful completions is reached.**

Jobs are useful for tasks such as:

* data processing
* database migrations
* batch processing
* model training
* scripts
* one-time computations

Unlike a Deployment, a Job is designed for **finite tasks** rather than continuously running applications.

---

## Job vs. Deployment

A **Deployment** manages applications that should keep running.

A **Job** manages tasks that should eventually finish.

```text
Deployment:

Pod → running
Pod → running
Pod → running
       ↑
   continuously
```

```text
Job:

Pod → running → completed
```

The main difference is therefore:

| Deployment                | Job                              |
| ------------------------- | -------------------------------- |
| Long-running applications | Finite tasks                     |
| Pods should keep running  | Pods should eventually terminate |
| Maintains replicas        | Ensures successful completions   |
| Example: web server       | Example: database migration      |

---

## Basic Job

A simple Job can look like this:

```yaml
apiVersion: batch/v1
kind: Job

metadata:
  name: my-job

spec:
  template:
    spec:
      containers:
        - name: my-task
          image: my-image:1.0
          command:
            - python
            - script.py

      restartPolicy: Never
```

The Job creates a Pod that runs:

```bash
python script.py
```

When the command finishes successfully, the Job is completed.

---

## Job Lifecycle

A simplified Job lifecycle looks like this:

```text
Job
 │
 ▼
Pod created
 │
 ▼
Running
 │
 ├── success ──→ Completed
 │
 └── failure ──→ Retry / Failed
```

For example:

```text
Job
 │
 ▼
Pod 1
 │
 ├── fails
 │
 ▼
Pod 2
 │
 ├── succeeds
 │
 ▼
Job Completed
```

The Job controller is responsible for creating new Pods when necessary.

---

## Completions

The `completions` field specifies how many Pods must successfully complete.

```yaml
spec:
  completions: 3
```

This means that Kubernetes needs **3 successful completions**.

For example:

```text
Job
 │
 ├── Pod 1 → ✓
 ├── Pod 2 → ✓
 └── Pod 3 → ✓
```

After three successful completions, the Job is considered complete.

---

## Parallelism

The `parallelism` field specifies how many Pods may run simultaneously.

```yaml
spec:
  completions: 6
  parallelism: 3
```

This means:

* 6 successful completions are required
* up to 3 Pods can run at the same time

Conceptually:

```text
             Job
              │
      ┌───────┼───────┐
      ▼       ▼       ▼
    Pod 1   Pod 2   Pod 3
      ✓       ✓       ✓
              │
              ▼
        more Pods...
              │
              ▼
        6 completions
```

This is particularly useful for **parallel batch processing**.

---

## Backoff Limit

A Job can fail.

The `backoffLimit` specifies how many retries are allowed before the Job is considered failed.

```yaml
spec:
  backoffLimit: 3
```

For example:

```text
Pod 1 → Failed
Pod 2 → Failed
Pod 3 → Failed
Pod 4 → Failed
          │
          ▼
      Job Failed
```

The exact retry behavior depends on the Job configuration and Pod restart policy.

---

## Restart Policy

Jobs require a Pod restart policy of either:

```yaml
restartPolicy: Never
```

or:

```yaml
restartPolicy: OnFailure
```

### `Never`

A failed Pod is not restarted. Kubernetes can create another Pod to retry the Job.

### `OnFailure`

The containers in the Pod are restarted when they fail.

For batch workloads, `Never` is often useful when each attempt should be represented by a separate Pod.

---

## Job Completion

When the required number of successful completions has been reached, the Job becomes complete.

For example:

```yaml
spec:
  completions: 3
```

After:

```text
Pod 1 → Succeeded
Pod 2 → Succeeded
Pod 3 → Succeeded
```

the Job reaches:

```text
Job → Complete
```

The completed Pods may remain in the cluster so that their logs and status can be inspected.

---

## Job Failure

A Job can also fail permanently.

For example:

```text
Job
 │
 ├── Pod 1 → Failed
 ├── Pod 2 → Failed
 ├── Pod 3 → Failed
 └── retry limit reached
          │
          ▼
      Job Failed
```

A Job can fail because:

* the application repeatedly crashes
* an image cannot be started
* required resources are unavailable
* the task repeatedly exits with an error
* the retry limit is reached

---

## Parallel Jobs

Jobs are especially useful for **batch processing**.

Suppose a dataset consists of six independent parts:

```text
Dataset
├── Part 1
├── Part 2
├── Part 3
├── Part 4
├── Part 5
└── Part 6
```

A Job can process these parts in parallel:

```text
             Job
              │
      ┌───────┼───────┐
      ▼       ▼       ▼
    Pod 1   Pod 2   Pod 3
   Part 1   Part 2   Part 3
      │       │       │
      ▼       ▼       ▼
   Pod 4   Pod 5   Pod 6
   Part 4   Part 5   Part 6
```

The exact parallelization strategy depends on how the application assigns work to each Pod.

---

## Indexed Jobs

For parallel workloads, Kubernetes supports **Indexed Jobs**.

For example:

```yaml
spec:
  completions: 6
  parallelism: 3
  completionMode: Indexed
```

Each Pod receives a unique index:

```text
Pod 0 → index 0
Pod 1 → index 1
Pod 2 → index 2
...
Pod 5 → index 5
```

This is useful when each Pod should process a specific part of a larger task.

For example:

```text
Index 0 → data_000.parquet
Index 1 → data_001.parquet
Index 2 → data_002.parquet
...
```

---

## Job vs. CronJob

A **Job** runs a task when it is created.

A **CronJob** creates Jobs according to a schedule.

```text
Job:

create
  │
  ▼
run task
  │
  ▼
complete
```

```text
CronJob:

schedule
  │
  ├── Job → complete
  │
  ├── Job → complete
  │
  └── Job → complete
```

For example, a CronJob could run a data processing task every night.

---

## Job and Pod

A Job does not directly execute a command itself.

Instead, it creates a **Pod** containing the container that performs the task.

```text
Job
 │
 ▼
Pod
 │
 ▼
Container
 │
 ▼
Application
```

For example:

```yaml
spec:
  template:
    spec:
      containers:
        - name: processor
          image: processor:1.0
          command:
            - python
            - process.py
```

The container runs the actual task, while the Job manages its successful completion.

---

## Job and Deployment

A Job and Deployment both create Pods, but they have different purposes.

```text
Deployment
    │
    ▼
ReplicaSet
    │
    ▼
Pods
    │
    └── keep running
```

```text
Job
    │
    ▼
Pods
    │
    └── run to completion
```

A web server would typically use a Deployment:

```text
Deployment → API server → keeps running
```

A database migration would typically use a Job:

```text
Job → migration script → completes
```

---

## Useful Commands

List Jobs:

```bash
kubectl get jobs
```

Get details about a Job:

```bash
kubectl describe job my-job
```

View the Pods created by a Job:

```bash
kubectl get pods
```

View the logs of a Job:

```bash
kubectl logs job/my-job
```

Delete a Job:

```bash
kubectl delete job my-job
```

---

## Important Concepts

| Concept            | Meaning                                        |
| ------------------ | ---------------------------------------------- |
| **Job**            | Runs a finite task until successful completion |
| **Completion**     | Successful execution of a Job Pod              |
| **Completions**    | Number of successful executions required       |
| **Parallelism**    | Maximum number of Pods running simultaneously  |
| **Backoff Limit**  | Number of allowed failed attempts              |
| **Restart Policy** | Determines how failed containers are handled   |
| **Indexed Job**    | Assigns an index to each completion            |
| **CronJob**        | Creates Jobs according to a schedule           |
| **Pod**            | Executes the actual workload of the Job        |

---

## Summary

A Kubernetes Job is designed for **finite workloads that should eventually complete**.

The basic relationship is:

```text
Job
 │
 ▼
Pod
 │
 ▼
Container
 │
 ▼
Task
 │
 ▼
Completed
```

Jobs can also be configured for retries and parallel execution:

```text
             Job
              │
      ┌───────┼───────┐
      ▼       ▼       ▼
    Pod 1   Pod 2   Pod 3
      ✓       ✓       ✓
              │
              ▼
         Job Complete
```

> **A Kubernetes Job ensures that a specified task is successfully completed, potentially using multiple Pods and retries.**
