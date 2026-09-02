# Deployments

## TL;DR (30 seconds)

A **Kubernetes Deployment** is a resource used to **manage and update a set of identical Pods**.

The key idea:

> **A Deployment describes how many replicas of an application should run and which container configuration they should use.**

A Deployment typically manages:

* the number of **replicas**
* the **Pod template**
* container images
* rolling updates
* replacement of failed Pods
* scaling

---

## Deployment Structure

A basic Deployment looks like this:

```yaml
apiVersion: apps/v1
kind: Deployment

metadata:
  name: my-app

spec:
  replicas: 3

  selector:
    matchLabels:
      app: my-app

  template:
    metadata:
      labels:
        app: my-app

    spec:
      containers:
        - name: my-app
          image: my-app:1.0
          ports:
            - containerPort: 8080
```

The important parts are:

```text
Deployment
├── replicas
├── selector
└── template
      └── Pod specification
```

---

## Replicas

The `replicas` field specifies how many identical Pods should run.

```yaml
spec:
  replicas: 3
```

This results in:

```text
Deployment
    │
    ├── Pod 1
    ├── Pod 2
    └── Pod 3
```

Kubernetes continuously tries to maintain the desired number of replicas.

If one Pod fails:

```text
Desired: 3

Pod 1  ✓
Pod 2  ✗
Pod 3  ✓
```

the Deployment creates a replacement:

```text
Pod 1  ✓
Pod 2  → replacement
Pod 3  ✓
```

---

## Pod Template

The `template` defines how the Pods managed by the Deployment should look.

For example:

```yaml
template:
  metadata:
    labels:
      app: my-app

  spec:
    containers:
      - name: my-app
        image: my-app:1.0
```

Every replica is created from this template.

Conceptually:

```text
             Deployment
                  │
             Pod Template
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
      Pod 1     Pod 2     Pod 3
```

The Pods are therefore not individually configured in the Deployment.

---

## Selectors and Labels

The `selector` specifies which Pods belong to the Deployment.

```yaml
selector:
  matchLabels:
    app: my-app
```

The Pod template must use matching labels:

```yaml
template:
  metadata:
    labels:
      app: my-app
```

The relationship is:

```text
Deployment
    │
    │ selector: app=my-app
    ▼
Pods with label:
app=my-app
```

Selectors allow Kubernetes to determine which Pods are managed by the Deployment.

---

## Container Image

The Pod template specifies which container image should be used.

```yaml
containers:
  - name: my-app
    image: my-app:1.0
```

Changing the image in the Deployment:

```yaml
image: my-app:1.0
```

to:

```yaml
image: my-app:2.0
```

causes Kubernetes to update the Pods.

---

## Rolling Updates

Deployments support **rolling updates**.

Instead of deleting all old Pods at once, Kubernetes gradually replaces them with new Pods.

For example:

```text
Before:

v1   v1   v1
│    │    │
└────┴────┴── 3 replicas
```

During the update:

```text
v1   v1   v2
│    │    │
└────┴────┴──
```

Eventually:

```text
v2   v2   v2
│    │    │
└────┴────┴── 3 replicas
```

This allows the application to remain available during an update.

---

## Deployment Strategy

The default update strategy for a Deployment is `RollingUpdate`.

```yaml
strategy:
  type: RollingUpdate
```

Two important parameters control the update:

```yaml
strategy:
  type: RollingUpdate

  rollingUpdate:
    maxUnavailable: 1
    maxSurge: 1
```

### `maxUnavailable`

Specifies how many Pods may be unavailable during the update.

### `maxSurge`

Specifies how many additional Pods may temporarily be created above the desired number of replicas.

For example, with:

```yaml
replicas: 3
maxSurge: 1
```

Kubernetes may temporarily run 4 Pods during the update.

---

## Scaling

Deployments can be scaled by changing the number of replicas.

For example:

```yaml
replicas: 5
```

or using `kubectl`:

```bash
kubectl scale deployment my-app --replicas=5
```

The Deployment then creates or removes Pods to reach the desired number.

```text
replicas: 3

Pod 1
Pod 2
Pod 3

        ↓ scale up

replicas: 5

Pod 1
Pod 2
Pod 3
Pod 4
Pod 5
```

---

## Self-Healing

Deployments maintain the desired number of Pods.

If a Pod crashes or is deleted:

```text
Desired: 3

Running:
Pod 1 ✓
Pod 2 ✗
Pod 3 ✓
```

the Deployment creates another Pod.

```text
Pod 1 ✓
Pod 2 → new Pod
Pod 3 ✓
```

This makes Deployments an important mechanism for **fault tolerance**.

---

## Deployment and ReplicaSet

A Deployment does not directly manage Pods.

Instead, it manages a **ReplicaSet**, which manages the Pods.

```text
Deployment
     │
     ▼
ReplicaSet
     │
     ├── Pod
     ├── Pod
     └── Pod
```

When the Deployment is updated, Kubernetes creates a new ReplicaSet.

For example:

```text
Deployment
    │
    ├── ReplicaSet v1
    │      ├── Pod v1
    │      └── Pod v1
    │
    └── ReplicaSet v2
           ├── Pod v2
           └── Pod v2
```

During a rolling update, the old ReplicaSet is gradually scaled down while the new ReplicaSet is scaled up.

---

## Deployment and Service

A Deployment manages Pods, but it does not provide a stable network endpoint.

A **Service** can be used to expose the Pods:

```text
                Service
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
        Pod 1    Pod 2    Pod 3
          ▲        ▲        ▲
          └────────┼────────┘
                   │
              Deployment
```

The Service selects the Pods using labels.

Therefore:

> **Deployment = manages Pods**

> **Service = provides network access to Pods**

---

## Deployment Status

A Deployment can have different states during its lifecycle.

For example:

### Progressing

The Deployment is currently creating or updating Pods.

### Available

The required number of Pods is available.

### Failed / Degraded

The Deployment cannot reach its desired state.

For example, this can happen when Pods repeatedly crash:

```text
Deployment
    │
    ▼
ReplicaSet
    │
    ▼
Pod
    │
    ▼
CrashLoopBackOff
```

---

## Common Commands

List Deployments:

```bash
kubectl get deployments
```

Get details:

```bash
kubectl describe deployment my-app
```

View the Pods:

```bash
kubectl get pods
```

Scale a Deployment:

```bash
kubectl scale deployment my-app --replicas=5
```

Update a container image:

```bash
kubectl set image deployment/my-app my-app=my-app:2.0
```

View rollout status:

```bash
kubectl rollout status deployment/my-app
```

Roll back a Deployment:

```bash
kubectl rollout undo deployment/my-app
```

---

## Deployment Workflow

A simplified Deployment workflow looks like this:

```text
Deployment
    │
    │ defines desired state
    ▼
ReplicaSet
    │
    │ creates/manages
    ▼
Pods
    │
    │ run
    ▼
Containers
```

When the Deployment configuration changes:

```text
Deployment updated
        │
        ▼
New ReplicaSet
        │
        ▼
New Pods
        │
        ▼
Old ReplicaSet
        │
        ▼
Old Pods gradually removed
```

---

## Important Concepts

| Concept            | Meaning                                         |
| ------------------ | ----------------------------------------------- |
| **Deployment**     | Manages a set of identical Pods                 |
| **Replica**        | One desired instance of a Pod                   |
| **Pod Template**   | Defines how Pods should be created              |
| **Selector**       | Identifies the Pods managed by the Deployment   |
| **ReplicaSet**     | Ensures the desired number of Pods exists       |
| **Rolling Update** | Gradually replaces old Pods with new ones       |
| **Scaling**        | Increasing or decreasing the number of replicas |
| **Self-Healing**   | Replacing failed or deleted Pods                |
| **Service**        | Provides stable network access to Pods          |

---

## Summary

A Kubernetes Deployment manages the lifecycle of replicated Pods.

The main relationship is:

```text
Deployment
     │
     ▼
ReplicaSet
     │
     ▼
  Pods
     │
     ▼
Containers
```

A Deployment defines the **desired number of replicas** and the **configuration of those Pods**. Kubernetes then continuously works to maintain that desired state.

> **A Deployment manages replicated Pods and provides mechanisms for scaling, self-healing, and rolling updates.**
