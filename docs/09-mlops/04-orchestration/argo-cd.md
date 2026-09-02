# Argo CD

## TL;DR (30 seconds)

**Argo CD** is a **GitOps tool for Kubernetes** that continuously compares the desired state defined in a Git repository with the actual state of a Kubernetes cluster.

The key idea:

> **Git defines how the Kubernetes cluster should look. Argo CD makes sure that the cluster matches this state.**

Argo CD can automatically deploy changes, detect configuration drift and restore the desired state.

---

## GitOps

**GitOps** is the principle of managing infrastructure and applications through Git.

Kubernetes resources such as Deployments, Services or ConfigMaps are stored in a Git repository:

```text
my-app/
├── deployment.yaml
├── service.yaml
└── configmap.yaml
```

These files describe the **desired state** of the application.

Argo CD continuously compares this state with the state running in Kubernetes.

---

## Desired State vs. Live State

Argo CD distinguishes between two states.

### Desired State

The **desired state** is defined by the Git repository.

For example:

```yaml
spec:
  replicas: 3
```

### Live State

The **live state** is the state currently running in Kubernetes.

For example:

```yaml
spec:
  replicas: 2
```

Argo CD detects the difference:

```text
Desired State       Live State
3 replicas    ≠     2 replicas
       │
       ▼
   OutOfSync
```

---

## Application

The central resource in Argo CD is an **Application**.

An Application defines:

* the Git repository
* the path containing the configuration
* the Git revision
* the target Kubernetes cluster
* the target namespace
* the synchronization policy

Example:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
spec:
  source:
    repoURL: https://git.example.com/my-project.git
    targetRevision: main
    path: kubernetes

  destination:
    server: https://kubernetes.default.svc
    namespace: my-app

  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

The Application connects the **Git source** with a **Kubernetes destination**.

---

## Sync

A **Sync** applies the desired state from Git to the Kubernetes cluster.

```text
Git
 │
 │ desired state
 ▼
Argo CD
 │
 │ Sync
 ▼
Kubernetes
```

After a successful synchronization:

```text
Desired State = Live State
        │
        ▼
      Synced
```

Synchronization can be triggered **manually** or **automatically**.

---

## Automated Sync

Argo CD can automatically synchronize changes from Git:

```yaml
syncPolicy:
  automated: {}
```

For example, changing:

```yaml
replicas: 2
```

to:

```yaml
replicas: 3
```

in Git can cause Argo CD to automatically update the Kubernetes Deployment.

---

## Self-Healing

With `selfHeal`, Argo CD automatically corrects changes made directly in the cluster.

For example:

```text
Git:
replicas = 3

Kubernetes:
replicas = 5
```

Argo CD detects the difference and restores:

```text
Kubernetes:
replicas = 3
```

This allows Argo CD to automatically correct **configuration drift**.

---

## Pruning

**Pruning** removes resources from Kubernetes that are no longer defined in Git.

For example, if a Service is deleted from Git:

```text
Git
├── deployment.yaml
└── service.yaml  ← deleted
```

Argo CD can also remove the corresponding Service from Kubernetes.

Pruning is enabled with:

```yaml
syncPolicy:
  automated:
    prune: true
```

---

## Reconciliation

The continuous comparison between the desired state and the live state is called **reconciliation**.

```text
       Git
        │
        │ Desired State
        ▼
     Argo CD
        │
        │ compare
        ▼
 Kubernetes
        │
        │ Live State
        └─────────────┐
                      │
                      ▼
                  difference?
                      │
                ┌─────┴─────┐
               No           Yes
                │             │
             Synced        OutOfSync
                              │
                              ▼
                             Sync
```

Argo CD repeatedly performs this comparison.

---

## Sync Status

The sync status describes whether the live state matches the desired state.

### Synced

```text
Git == Kubernetes
```

The desired state and live state match.

### OutOfSync

```text
Git != Kubernetes
```

The desired state and live state differ.

An `OutOfSync` Application does not necessarily mean that the application is broken. It only means that the configuration differs from the desired state.

---

## Health Status

Argo CD also evaluates the health of Kubernetes resources.

Common states include:

| Status          | Meaning                                    |
| --------------- | ------------------------------------------ |
| **Healthy**     | Resource is operating normally             |
| **Progressing** | Resource is currently changing or starting |
| **Degraded**    | Resource is not operating as expected      |
| **Suspended**   | Resource has been intentionally paused     |
| **Missing**     | Expected resource does not exist           |

For example, a Deployment with Pods repeatedly entering `CrashLoopBackOff` may be considered **Degraded**.

---

## Synced vs. Healthy

**Sync status** and **health status** describe different properties.

An application can be:

```text
Synced + Healthy
```

The configuration matches Git and the application is running correctly.

It can also be:

```text
Synced + Degraded
```

The configuration matches Git, but the application is not healthy.

Or:

```text
OutOfSync + Healthy
```

The application is currently working, but its configuration differs from the desired state in Git.

---

## Helm and Kustomize

Argo CD supports different ways of defining Kubernetes resources.

Common options include:

* Kubernetes YAML
* **Helm**
* **Kustomize**
* Jsonnet

For example, a Helm application might have the following structure:

```text
my-chart/
├── Chart.yaml
├── values.yaml
└── templates/
    ├── deployment.yaml
    └── service.yaml
```

Argo CD renders the Helm chart and synchronizes the resulting Kubernetes resources.

---

## Typical Workflow

A typical GitOps workflow looks like this:

```text
1. Developer changes configuration
              │
              ▼
2. Commit / Pull Request
              │
              ▼
3. Change is merged into Git
              │
              ▼
4. Argo CD detects the change
              │
              ▼
5. Application becomes OutOfSync
              │
              ▼
6. Argo CD synchronizes
              │
              ▼
7. Kubernetes is updated
              │
              ▼
8. Application becomes Synced
```

With automated synchronization, the deployment can happen without manually triggering a Sync.

---

## Important Concepts

| Concept            | Meaning                                       |
| ------------------ | --------------------------------------------- |
| **GitOps**         | Managing the desired system state through Git |
| **Application**    | Argo CD resource connecting Git to Kubernetes |
| **Desired State**  | State defined by Git                          |
| **Live State**     | Actual state in Kubernetes                    |
| **Sync**           | Applying the desired state to the cluster     |
| **Synced**         | Desired and live state match                  |
| **OutOfSync**      | Desired and live state differ                 |
| **Self-Heal**      | Automatically correcting configuration drift  |
| **Prune**          | Removing resources deleted from Git           |
| **Reconciliation** | Continuously comparing and reconciling states |
| **Healthy**        | Resource is operating correctly               |
| **Degraded**       | Resource is not operating correctly           |

---

## Summary

Argo CD implements the **GitOps principle for Kubernetes**:

```text
Git = Desired State
        │
        ▼
     Argo CD
        │
        ▼
Kubernetes = Live State
```

Argo CD continuously compares both states and synchronizes the cluster when necessary.

> **Git defines the desired state, while Argo CD continuously reconciles Kubernetes with that state.**
