# Kubernetes Foundations

## TL;DR

**Kubernetes** is a platform for deploying, managing, and scaling containerized applications.

The core idea is to describe the **desired state** of an application, while Kubernetes continuously works to make the actual cluster match that state.

A simplified architecture is:

```text
                    Kubernetes Cluster
                           │
             ┌─────────────┴─────────────┐
             │                           │
        Control Plane                 Worker Nodes
             │                           │
      ┌──────┴──────┐             ┌──────┴──────┐
      │             │             │             │
   API Server   Scheduler       Pod           Pod
      │                           │             │
      │                         Container     Container
      │
   etcd
```

The basic deployment hierarchy is:

$$
\boxed{
\text{Cluster}
\rightarrow
\text{Node}
\rightarrow
\text{Pod}
\rightarrow
\text{Container}
}
$$

---

## Kubernetes Cluster

A **Kubernetes cluster** is a collection of machines that run containerized workloads.

It consists of:

* a **Control Plane**, which manages the cluster
* **Worker Nodes**, which run applications

```text
Kubernetes Cluster
│
├── Control Plane
│
└── Worker Nodes
    ├── Node
    │   ├── Pod
    │   └── Pod
    │
    └── Node
        ├── Pod
        └── Pod
```

---

## Control Plane

The **Control Plane** is responsible for managing the Kubernetes cluster.

Important components include:

* **API Server**
* **Scheduler**
* **Controller Manager**
* **etcd**

```text
                 Control Plane
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   API Server      Scheduler      Controllers
        │
        ▼
      etcd
```

### API Server

The **API Server** is the main entry point to Kubernetes.

Tools such as `kubectl`, controllers, and other Kubernetes components communicate with the API Server.

```text
kubectl
   │
   ▼
API Server
   │
   ▼
Kubernetes API
```

For example:

```bash
kubectl get pods
```

asks the API Server for information about Pods.

---

## etcd

**etcd** is a distributed key-value store that contains the Kubernetes cluster state.

It stores information such as:

* Pods
* Deployments
* Services
* ConfigMaps
* Secrets
* cluster configuration

Conceptually:

```text
Kubernetes Objects
       │
       ▼
     etcd
```

The desired state of the cluster is persisted in etcd.

---

## Scheduler

The **Scheduler** decides which Worker Node should run a newly created Pod.

For example:

```text
Pod
 │
 ▼
Scheduler
 │
 ├── Node 1
 ├── Node 2
 └── Node 3
```

The Scheduler considers factors such as:

* available resources
* node constraints
* affinity and anti-affinity
* taints and tolerations

It does not itself run the Pod. It selects the appropriate Node.

---

## Controllers

Kubernetes uses **controllers** to continuously compare the desired state with the actual state.

For example, a Deployment might specify:

```yaml
replicas: 3
```

If only two Pods are running:

```text
Desired: 3 Pods

Actual:  2 Pods

Controller
    │
    ▼
Create another Pod
```

Controllers therefore implement Kubernetes' reconciliation model.

```text
Desired State
      │
      ▼
  Controller
      │
      ▼
Actual State
      │
      │
      └── reconcile
```

---

## Worker Nodes

**Worker Nodes** are the machines that run application workloads.

A Node typically contains:

* **kubelet**
* a **container runtime**
* **kube-proxy** or equivalent networking components

```text
Worker Node
│
├── kubelet
├── Container Runtime
│
└── Pods
    ├── Container
    └── Container
```

---

## kubelet

The **kubelet** is the Kubernetes agent running on each Worker Node.

It communicates with the Control Plane and ensures that the Pods assigned to the Node are running.

```text
Control Plane
      │
      ▼
  API Server
      │
      ▼
   kubelet
      │
      ▼
    Pods
```

The kubelet does not normally create Pods based on its own decisions. It receives the desired state from Kubernetes and ensures that the Node conforms to it.

---

## Pods

A **Pod** is the smallest deployable unit in Kubernetes.

A Pod contains one or more containers that share:

* network namespace
* IP address
* storage volumes

Most applications use one main container per Pod:

```text
Pod
│
└── Application Container
```

A Pod with multiple containers might look like:

```text
Pod
│
├── Application Container
└── Sidecar Container
```

Containers inside the same Pod can communicate through `localhost`.

---

## Pods vs. Containers

A Pod is **not** the same thing as a container.

The relationship is:

```text
Pod
│
├── Container
├── Container
└── Container
```

Kubernetes schedules **Pods**, while containers are executed inside those Pods.

Therefore:

$$
\boxed{
\text{Kubernetes schedules Pods, not individual Containers}
}
$$

---

## Deployments

A **Deployment** manages a set of replicated Pods.

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
        - name: app
          image: my-app:1.0
```

This describes the desired state:

```text
Deployment
    │
    ▼
3 Pods
├── Pod
├── Pod
└── Pod
```

The Deployment controller ensures that the requested number of Pods exists.

---

## ReplicaSets

A Deployment normally creates and manages a **ReplicaSet**.

The relationship is:

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

The ReplicaSet ensures that the desired number of Pod replicas is running.

The Deployment adds higher-level functionality such as:

* rolling updates
* version management
* rollbacks

---

## Services

Pods are ephemeral and their IP addresses can change.

A **Service** provides a stable network endpoint for a group of Pods.

```text
Service
   │
   ├── Pod
   ├── Pod
   └── Pod
```

For example:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app
spec:
  selector:
    app: my-app
  ports:
    - port: 80
      targetPort: 8080
```

The Service selects Pods using labels.

```text
Service
   │
   │ selector: app=my-app
   │
   ├── Pod
   ├── Pod
   └── Pod
```

---

## Labels and Selectors

**Labels** attach metadata to Kubernetes objects.

For example:

```yaml
labels:
  app: my-app
  environment: production
```

A selector can then find objects with matching labels:

```yaml
selector:
  app: my-app
```

This mechanism is fundamental to Kubernetes.

For example:

```text
Service
   │
   │ selector: app=my-app
   ▼
┌───────────────┐
│ Pod           │
│ app=my-app    │
└───────────────┘
```

---

## Namespaces

A **Namespace** provides logical separation inside a Kubernetes cluster.

For example:

```text
Cluster
│
├── namespace: development
│   ├── Deployment
│   └── Service
│
├── namespace: staging
│   ├── Deployment
│   └── Service
│
└── namespace: production
    ├── Deployment
    └── Service
```

Namespaces are useful for:

* separating environments
* organizing applications
* applying access control
* applying resource limits

---

## ConfigMaps

A **ConfigMap** stores non-sensitive configuration data.

For example:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  LOG_LEVEL: "INFO"
  API_URL: "https://api.example.com"
```

Applications can consume this configuration through environment variables or mounted files.

```text
ConfigMap
    │
    ▼
   Pod
    │
    ▼
Application
```

---

## Secrets

A **Secret** is used for sensitive configuration such as:

* passwords
* API keys
* tokens
* certificates

For example:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: database-secret
type: Opaque
data:
  username: ...
  password: ...
```

Secrets can be exposed to containers as environment variables or mounted files.

---

## Storage

Containers are generally ephemeral, so Kubernetes provides storage abstractions for persistent data.

A common hierarchy is:

```text
PersistentVolumeClaim
          │
          ▼
PersistentVolume
          │
          ▼
   Physical Storage
```

A **PersistentVolumeClaim (PVC)** requests persistent storage for a Pod.

For example:

```text
Pod
 │
 ▼
PVC
 │
 ▼
PV
 │
 ▼
Storage
```

This allows application data to survive Pod restarts and rescheduling.

---

## Resource Requests and Limits

Containers can specify CPU and memory requirements.

For example:

```yaml
resources:
  requests:
    cpu: "500m"
    memory: "256Mi"
  limits:
    cpu: "1"
    memory: "512Mi"
```

A **request** describes the resources required for scheduling.

A **limit** defines the maximum amount of a resource the container may use.

```text
Request
   │
   ▼
Scheduler uses this for placement

Limit
   │
   ▼
Runtime resource constraint
```

---

## Desired State

Kubernetes is fundamentally based on **declarative configuration**.

Instead of specifying every step required to start an application, you describe the desired state.

For example:

```yaml
replicas: 3
```

means:

> I want three replicas of this application.

Kubernetes then continuously works toward that state.

```text
Desired State
     │
     ▼
Kubernetes
     │
     ▼
Actual State
```

If a Pod crashes:

```text
Desired: 3 Pods

Actual:  2 Pods

Controller
    │
    ▼
Create replacement Pod
```

---

## Reconciliation

The process of continuously bringing the actual state toward the desired state is called **reconciliation**.

Conceptually:

$$
\boxed{
\text{Desired State}
\rightarrow
\text{Controller}
\rightarrow
\text{Actual State}
}
$$

If the actual state changes, Kubernetes attempts to correct the difference.

This is one of the central ideas behind Kubernetes.

---

## kubectl

`kubectl` is the standard command-line client for Kubernetes.

Examples:

```bash
kubectl get pods
```

```bash
kubectl get deployments
```

```bash
kubectl describe pod my-app
```

```bash
kubectl logs my-app
```

```bash
kubectl apply -f deployment.yaml
```

The general workflow is:

```text
kubectl
   │
   ▼
API Server
   │
   ▼
Kubernetes Objects
```

---

## Typical Application Architecture

A typical Kubernetes application might look like:

```text
                         Internet
                            │
                            ▼
                         Ingress
                            │
                            ▼
                         Service
                            │
                  ┌─────────┴─────────┐
                  ▼                   ▼
                 Pod                 Pod
                  │                   │
             Container           Container
```

The Pods are commonly managed by a Deployment:

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

---

## Kubernetes Object Hierarchy

A simplified view of the most important objects is:

```text
Cluster
│
├── Namespace
│   │
│   ├── Deployment
│   │      │
│   │      └── ReplicaSet
│   │             │
│   │             ├── Pod
│   │             └── Pod
│   │
│   ├── Service
│   │
│   ├── ConfigMap
│   │
│   └── Secret
│
└── Worker Nodes
```

Not all Kubernetes resources form a strict hierarchy. Instead, they are connected through references, labels, selectors, and controllers.

---

## Core Request Flow

For an externally accessible application, the typical request path is:

```text
Internet
   │
   ▼
Ingress
   │
   ▼
Service
   │
   ▼
Pod
   │
   ▼
Container
```

The application lifecycle is managed by Kubernetes:

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

---

## Key Idea

Kubernetes provides a **declarative system for managing containerized applications**.

The most important concepts are:

* **Cluster** — the complete Kubernetes environment
* **Control Plane** — manages the cluster
* **Node** — runs workloads
* **Pod** — smallest deployable unit
* **Deployment** — manages replicated application Pods
* **Service** — provides stable network access to Pods
* **Ingress** — routes external HTTP/HTTPS traffic
* **ConfigMap** — stores non-sensitive configuration
* **Secret** — stores sensitive configuration
* **PVC** — requests persistent storage
* **Controller** — reconciles desired and actual state

The central Kubernetes model is:

$$
\boxed{
\text{Desired State}
\rightarrow
\text{Controllers}
\rightarrow
\text{Actual State}
}
$$

And a typical application can be understood as:

$$
\boxed{
\text{Ingress}
\rightarrow
\text{Service}
\rightarrow
\text{Deployment}
\rightarrow
\text{Pod}
\rightarrow
\text{Container}
}
$$
