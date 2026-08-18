# Pods

## TL;DR

A **Pod** is the smallest deployable unit in Kubernetes.

A Pod represents one or more **containers that are deployed and run together on the same Kubernetes node**. Containers inside a Pod share:

* network namespace and therefore an IP address
* ports
* optionally volumes
* lifecycle and scheduling context

The most common case is a Pod containing **exactly one application container**.

The basic relationship is:

$$
\boxed{
\text{Deployment}
\rightarrow
\text{Pod}
\rightarrow
\text{Container}
}
$$

Pods are usually **not created directly**. Higher-level Kubernetes resources such as Deployments, StatefulSets or Jobs manage them.

---

## What Is a Pod?

A Pod is a wrapper around one or more containers.

For example:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-app
spec:
  containers:
    - name: app
      image: my-app:1.0
```

This defines a Pod containing one container.

Kubernetes schedules the **Pod**, not the individual container.

```text
Kubernetes Node
└── Pod
    └── Container
```

With multiple containers:

```text
Kubernetes Node
└── Pod
    ├── Application Container
    └── Sidecar Container
```

---

## Pod vs. Container

A container is an isolated process environment.

A Pod provides the Kubernetes execution context around one or more containers.

For example:

```text
Pod
│
├── Container A
├── Container B
│
├── Network namespace
├── Volumes
└── Pod lifecycle
```

Containers inside the same Pod are therefore more tightly coupled than containers running in different Pods.

---

# Pod Networking

All containers within a Pod share the same network namespace.

Consequently, they share the same **IP address**.

For example:

```text
Pod IP: 10.0.1.42

┌─────────────────────────┐
│          Pod            │
│                         │
│  Container A : 8080     │
│  Container B : 9000     │
│                         │
└─────────────────────────┘
```

The containers can communicate through `localhost`.

For example, Container A can reach Container B using:

```text
localhost:9000
```

This is one of the main reasons why multiple containers are sometimes placed in the same Pod.

---

## Ports

Because containers in a Pod share the network namespace, they cannot normally bind to the same port.

For example, this would cause a conflict:

```text
Container A → :8080
Container B → :8080
```

Different ports are required:

```text
Container A → :8080
Container B → :9000
```

---

# Pod Storage

Containers inside a Pod can share volumes.

For example:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-app
spec:
  containers:
    - name: app
      image: my-app:1.0
      volumeMounts:
        - name: shared-data
          mountPath: /data

    - name: sidecar
      image: helper:1.0
      volumeMounts:
        - name: shared-data
          mountPath: /data

  volumes:
    - name: shared-data
      emptyDir: {}
```

Both containers can access:

```text
/data
```

This allows containers to exchange files through a shared volume.

---

# Multi-Container Pods

Although a Pod can contain multiple containers, **one container per Pod is the standard pattern**.

Multiple containers are useful when the containers are tightly coupled and need to share:

* networking
* storage
* lifecycle
* scheduling

A common pattern is the **sidecar pattern**.

```text
Pod
├── Main Application
└── Sidecar
```

For example:

```text
Application
    ↓
writes logs
    ↓
shared volume
    ↓
Log Sidecar
    ↓
log collection
```

The sidecar performs an auxiliary function for the main application.

Other examples include:

* proxies
* log collectors
* monitoring agents
* configuration reloaders

---

# Pod Lifecycle

Pods have a lifecycle.

Common Pod phases include:

| Phase       | Meaning                                                      |
| ----------- | ------------------------------------------------------------ |
| `Pending`   | Pod has not yet started running                              |
| `Running`   | Pod has been scheduled and at least one container is running |
| `Succeeded` | All containers terminated successfully                       |
| `Failed`    | Containers terminated unsuccessfully                         |
| `Unknown`   | Pod state cannot currently be determined                     |

A Pod can also have individual **container states** such as:

* `Waiting`
* `Running`
* `Terminated`

These are different concepts from the Pod phase.

---

# Pod Scheduling

Kubernetes schedules a Pod onto a node.

Conceptually:

```text
Kubernetes Cluster
│
├── Node 1
│   └── Pod A
│
├── Node 2
│   ├── Pod B
│   └── Pod C
│
└── Node 3
    └── Pod D
```

The scheduler considers factors such as:

* available CPU
* available memory
* resource requests
* node selectors
* affinity and anti-affinity
* taints and tolerations
* topology constraints

Once scheduled, all containers belonging to the Pod run on the **same node**.

---

# Pod Resources

Resource requirements are normally specified for containers.

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

The Pod's resource requirements are derived from the resource requirements of its containers.

For example:

$$
CPU_{Pod}
=========

\sum_i CPU_i
$$

and approximately:

$$
Memory_{Pod}
============

\sum_i Memory_i
$$

for the declared container requests.

---

# Pod IP Address

Each Pod normally receives its own IP address.

For example:

```text
Pod A → 10.0.1.10
Pod B → 10.0.1.11
Pod C → 10.0.1.12
```

Pods are therefore individually addressable within the cluster.

However, Pod IPs are generally **ephemeral**.

If a Pod is deleted and recreated, the new Pod may receive a different IP address.

For this reason, applications should generally not communicate with Pods directly.

Instead, Kubernetes **Services** provide a stable network endpoint.

```text
Client
  ↓
Service
  ↓
┌─────────┬─────────┬─────────┐
│ Pod A   │ Pod B   │ Pod C   │
└─────────┴─────────┴─────────┘
```

---

# Pods and Services

A **Service** provides stable networking for a set of Pods.

Pods are commonly selected using labels.

For example, Pods might have:

```yaml
labels:
  app: my-app
```

A Service can select them:

```yaml
selector:
  app: my-app
```

The Service then distributes traffic to matching Pods.

This allows Pods to be replaced without requiring clients to know their individual IP addresses.

---

# Pods and Deployments

Pods are usually managed by higher-level Kubernetes resources.

The most common example is a **Deployment**.

```text
Deployment
    ↓
ReplicaSet
    ↓
Pods
    ↓
Containers
```

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

The Deployment does not directly "run" the containers. Instead, it manages ReplicaSets, which create and maintain the desired number of Pods.

If:

```yaml
replicas: 3
```

the desired state is:

```text
Deployment
    ↓
ReplicaSet
    ↓
Pod A
Pod B
Pod C
```

---

# Pod Replacement

Pods are generally considered **ephemeral**.

If a Pod crashes or is deleted, a controller such as a Deployment can create a replacement.

For example:

```text
Pod A
  ↓
deleted
  ↓
Pod D created
```

The new Pod is a new object and may have:

* a different IP address
* a different name
* a different node

This is why persistent state should generally not be stored only inside the Pod's container filesystem.

Persistent data should instead use Kubernetes storage mechanisms such as **PersistentVolumes**.

---

# Pod Restarts

A container inside a Pod can be restarted without necessarily creating a new Pod.

For example:

```text
Pod A
└── Container
      ↓
    crashes
      ↓
  container restarted
```

The Pod itself can remain the same.

This distinction is important:

```text
Container restart
≠
Pod replacement
```

The exact behavior depends on the Pod's `restartPolicy` and the controller managing it.

---

# Init Containers

A Pod can contain **init containers**.

Init containers run before the regular application containers start.

For example:

```text
Pod
│
├── Init Container
│       ↓
│   initialization
│
└── Application Container
        ↓
      application
```

A common use case is preparing configuration or waiting for a required condition before starting the application.

Example:

```yaml
initContainers:
  - name: init
    image: busybox
    command: ["sh", "-c", "echo initializing"]
```

All init containers must complete successfully before normal containers start.

---

# Sidecar Containers

A **sidecar** is a secondary container running alongside the main application container.

```text
Pod
├── Application
└── Sidecar
```

The containers share the Pod's network and can optionally share volumes.

A sidecar can therefore extend the functionality of the application without modifying the application itself.

---

# Probes

Kubernetes can use **probes** to determine the state of a container.

Important probes include:

### Liveness Probe

Determines whether the container is still functioning.

If the liveness probe repeatedly fails, Kubernetes can restart the container.

### Readiness Probe

Determines whether the application is ready to receive traffic.

A Pod can therefore be running but not ready.

```text
Running
   ≠
Ready
```

### Startup Probe

Allows slow-starting applications additional time to initialize before liveness and readiness checks become active.

---

# Pod YAML Structure

A simplified Pod definition looks like:

```yaml
apiVersion: v1
kind: Pod

metadata:
  name: my-app
  labels:
    app: my-app

spec:
  containers:
    - name: app
      image: my-app:1.0
      ports:
        - containerPort: 8080
```

The important structure is:

```text
Pod
├── metadata
│   ├── name
│   └── labels
│
└── spec
    └── containers
        └── container
```

---

# Inspecting Pods

Pods can be inspected using `kubectl`.

List Pods:

```bash
kubectl get pods
```

More detailed information:

```bash
kubectl describe pod my-app
```

View logs:

```bash
kubectl logs my-app
```

For a multi-container Pod:

```bash
kubectl logs my-app -c sidecar
```

Execute a command inside a container:

```bash
kubectl exec -it my-app -- /bin/sh
```

---

# Pods in OpenShift

OpenShift uses the same fundamental Kubernetes Pod concept.

Pods can be inspected using:

```bash
oc get pods
```

or:

```bash
oc describe pod <pod-name>
```

In the OpenShift UI, Pods are typically visible within the project's workload resources.

A common hierarchy is:

```text
OpenShift Project / Namespace
        ↓
    Deployment
        ↓
    ReplicaSet
        ↓
       Pod
        ↓
    Container(s)
```

---

# Pod vs. Deployment vs. Service

These resources have different responsibilities:

| Resource             | Main responsibility                  |
| -------------------- | ------------------------------------ |
| **Pod**              | Runs one or more containers          |
| **Deployment**       | Manages replicated, replaceable Pods |
| **Service**          | Provides stable networking to Pods   |
| **Ingress**          | Provides external HTTP/HTTPS routing |
| **ConfigMap**        | Provides configuration               |
| **Secret**           | Provides sensitive configuration     |
| **PersistentVolume** | Provides persistent storage          |

A typical web application therefore looks like:

```text
                Ingress
                   ↓
                Service
                   ↓
        ┌──────────┼──────────┐
        ↓          ↓          ↓
      Pod A      Pod B      Pod C
        │          │          │
    Container  Container  Container
```

---

# Key Idea

A Pod is the **execution and networking unit of Kubernetes**.

It should not be thought of simply as "a container". Instead:

$$
\boxed{
\text{Pod}
==========

\text{one or more containers}
+
\text{shared network}
+
\text{shared storage}
+
\text{shared lifecycle context}
}
$$

In practice, most Pods contain a single application container and are managed indirectly by controllers such as **Deployments**, **StatefulSets** or **Jobs**.

The most important relationship to remember is:

```text
Deployment
    ↓
ReplicaSet
    ↓
Pod
    ↓
Container
```

and for networking:

```text
Client
   ↓
Service
   ↓
Pods
   ↓
Containers
```
