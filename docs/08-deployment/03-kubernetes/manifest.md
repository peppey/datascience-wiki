# Kubernetes Manifests

## TL;DR (30 seconds)

**Kubernetes manifests** are **YAML or JSON files that declaratively describe Kubernetes resources**.

A manifest specifies the desired state of a resource, such as a `Deployment`, `Service`, `Pod`, or `ConfigMap`.

The key idea:

> **A Kubernetes manifest describes what a resource should look like, rather than the individual steps needed to create it.**

For example:

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
```

---

## Declarative Configuration

Kubernetes uses a **declarative approach**.

Instead of specifying every action that should be performed, a manifest describes the desired end state.

For example:

```yaml
spec:
  replicas: 3
```

means:

> The Deployment should have 3 replicas (identical pod instances).

Kubernetes continuously works towards this desired state.

This differs from an imperative approach such as:

```bash
kubectl scale deployment my-app --replicas=3
```

Here, the command explicitly tells Kubernetes what action to perform.

---

## Structure of a Manifest

Most Kubernetes manifests contain four important fields:

```yaml
apiVersion: apps/v1
kind: Deployment

metadata:
  name: my-app

spec:
  replicas: 3
```

### `apiVersion`

Specifies which Kubernetes API version should be used.

```yaml
apiVersion: apps/v1
```

The API version depends on the resource type.

For example:

```yaml
apiVersion: v1
```

is commonly used for resources such as `Pod` and `Service`, while:

```yaml
apiVersion: apps/v1
```

is used for `Deployment`.

---

### `kind`

Specifies the type of Kubernetes resource.

```yaml
kind: Deployment
```

Common resource types include:

* `Pod`
* `Deployment`
* `Service`
* `ConfigMap`
* `Secret`
* `Namespace`
* `Job`
* `CronJob`
* `PersistentVolumeClaim`

---

### `metadata`

Contains information that identifies the resource.

```yaml
metadata:
  name: my-app
  namespace: production
```

Metadata can also contain labels and annotations:

```yaml
metadata:
  name: my-app
  labels:
    app: my-app
    environment: production
```

---

### `spec`

The `spec` describes the **desired configuration** of the resource.

For example:

```yaml
spec:
  replicas: 3
```

For a Deployment, the `spec` can also define the container image:

```yaml
spec:
  template:
    spec:
      containers:
        - name: my-app
          image: my-app:1.0
```

The exact structure of `spec` depends on the resource type.

---

## Example: Deployment Manifest

A simple Deployment manifest might look like this:

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

This describes a Deployment with:

* 3 replicas
* a container called `my-app`
* the image `my-app:1.0`
* a container port of `8080`

---

## Applying Manifests

A manifest can be applied to a Kubernetes cluster using `kubectl`:

```bash
kubectl apply -f deployment.yaml
```

Kubernetes compares the desired state described by the manifest with the current state of the cluster and makes the necessary changes.

Other useful commands include:

```bash
kubectl get deployment my-app
```

and:

```bash
kubectl describe deployment my-app
```

To delete the resource defined by a manifest:

```bash
kubectl delete -f deployment.yaml
```

---

## Multiple Manifests in One File

A YAML file can contain multiple Kubernetes resources.

Resources are separated using `---`:

```yaml
apiVersion: apps/v1
kind: Deployment

metadata:
  name: my-app

# ...

---

apiVersion: v1
kind: Service

metadata:
  name: my-app

# ...
```

This allows related resources to be managed together.

---

## Labels and Selectors

**Labels** are key-value pairs attached to Kubernetes resources.

```yaml
metadata:
  labels:
    app: my-app
```

Other resources can use **selectors** to identify resources with particular labels.

For example:

```yaml
selector:
  matchLabels:
    app: my-app
```

Labels are commonly used to connect Kubernetes resources such as Deployments and Services.

---

## Namespaces

A manifest can specify the namespace in which a resource should exist:

```yaml
metadata:
  name: my-app
  namespace: production
```

If no namespace is specified, Kubernetes generally uses the namespace selected in the current context.

Namespaces are commonly used to separate applications, teams, or environments.

---

## Manifests and GitOps

Kubernetes manifests are particularly important for **GitOps**.

They can be stored in a Git repository:

```text
my-app/
├── deployment.yaml
├── service.yaml
└── configmap.yaml
```

A GitOps tool such as **Argo CD** can use these manifests as the desired state of the Kubernetes cluster.

```text
Git Repository
      │
      │ Kubernetes manifests
      ▼
   Argo CD
      │
      │ synchronization
      ▼
Kubernetes Cluster
```

This makes the Kubernetes configuration:

* version-controlled
* reproducible
* reviewable
* auditable

---

## Manifests vs. Helm Charts

A Kubernetes manifest is a concrete Kubernetes resource definition.

For example:

```yaml
replicas: 3
image: my-app:1.0
```

A **Helm chart**, on the other hand, can be used to generate manifests dynamically using templates and values.

For example:

```text
Helm Chart
    │
    ├── templates/
    ├── values.yaml
    └── Chart.yaml
           │
           ▼
   Kubernetes Manifests
           │
           ▼
      Kubernetes
```

Therefore:

> **Helm is a templating and packaging mechanism, while manifests are the actual Kubernetes resource definitions.**

---

## Common Manifest Resources

| Resource                | Purpose                                     |
| ----------------------- | ------------------------------------------- |
| `Pod`                   | Runs one or more containers                 |
| `Deployment`            | Manages replicated Pods and updates         |
| `Service`               | Provides stable network access to Pods      |
| `ConfigMap`             | Stores non-sensitive configuration          |
| `Secret`                | Stores sensitive configuration data         |
| `PersistentVolumeClaim` | Requests persistent storage                 |
| `Ingress`               | Defines external HTTP/HTTPS routing         |
| `Job`                   | Runs a task to completion                   |
| `CronJob`               | Runs Jobs on a schedule                     |
| `Namespace`             | Provides logical isolation within a cluster |

---

## Summary

Kubernetes manifests are **declarative configuration files** that describe the desired state of Kubernetes resources.

The basic structure is:

```text
apiVersion
kind
metadata
spec
```

A manifest can be:

```text
written
   ↓
stored in Git
   ↓
applied with kubectl
   ↓
or synchronized by Argo CD
   ↓
Kubernetes cluster
```

> **A Kubernetes manifest describes the desired state of a Kubernetes resource in a declarative format.**
