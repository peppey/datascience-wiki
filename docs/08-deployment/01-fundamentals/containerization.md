# Containers

## TL;DR (30 seconds)

A **container** is an isolated environment in which an application and its dependencies can run.

The key idea:

> **A container packages an application together with everything it needs to run, while sharing the host operating system's kernel.**

Containers are commonly created from **container images** using tools such as Docker or containerd.

In Kubernetes, containers run **inside Pods**:

```text
Kubernetes
    │
    ▼
   Pod
    │
    ├── Container
    └── Container
```

---

## Container vs. Virtual Machine

Containers are different from virtual machines.

A virtual machine contains a complete guest operating system:

```text
Virtual Machine
├── Application
├── Libraries
└── Guest OS
       │
    Hypervisor
       │
    Host OS
```

Containers share the host operating system's kernel:

```text
Container
├── Application
└── Libraries
       │
   Container Runtime
       │
   Host OS Kernel
```

As a result, containers are generally **lighter and faster to start** than virtual machines.

---

## Container Images

A **container image** is a packaged, immutable template from which containers are created.

An image typically contains:

* application code
* dependencies
* libraries
* configuration
* filesystem contents
* instructions for starting the application

For example:

```text
Container Image
├── Python
├── Libraries
├── Application code
└── Dependencies
```

A container is a **running instance of an image**.

```text
Image
  │
  │ create
  ▼
Container
```

The same image can be used to create multiple containers:

```text
             Image
               │
       ┌───────┼───────┐
       ▼       ▼       ▼
   Container Container Container
```

---

## Container Runtime

A **container runtime** is the software responsible for running containers.

Common runtimes include:

* **containerd**
* **CRI-O**
* Docker Engine

In Kubernetes, the Kubernetes node uses a container runtime to create and manage containers.

```text
Kubernetes
    │
    ▼
Container Runtime
    │
    ▼
Container
```

---

## Containers in Kubernetes

Kubernetes does not normally deploy containers directly.

Instead, containers run inside **Pods**.

A Pod can contain one or more containers:

```yaml
spec:
  containers:
    - name: my-app
      image: my-app:1.0
```

This means that the Pod should contain a container called `my-app` created from the `my-app:1.0` image.

The hierarchy is:

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
Container
```

---

## Container Image

The `image` field specifies which container image should be used.

For example:

```yaml
containers:
  - name: my-app
    image: nginx:1.27
```

The image consists of:

```text
Registry / Repository : Tag

nginx                 : 1.27
```

A complete image reference can also contain a registry:

```yaml
image: registry.example.com/my-project/my-app:1.0
```

Here:

| Part                   | Meaning               |
| ---------------------- | --------------------- |
| `registry.example.com` | Container registry    |
| `my-project`           | Repository or project |
| `my-app`               | Image name            |
| `1.0`                  | Image tag             |

---

## Container Ports

A container can declare the port on which an application listens:

```yaml
containers:
  - name: my-app
    image: my-app:1.0
    ports:
      - containerPort: 8080
```

This documents that the application inside the container listens on port `8080`.

A Kubernetes **Service** can then provide network access to the Pods.

```text
Client
  │
  ▼
Service
  │
  ▼
Pod
  │
  ▼
Container :8080
```

Declaring `containerPort` by itself does **not** expose the container outside the Pod.

---

## Environment Variables

Containers can receive configuration through environment variables.

For example:

```yaml
containers:
  - name: my-app
    image: my-app:1.0
    env:
      - name: ENVIRONMENT
        value: production
```

The application inside the container can then access:

```text
ENVIRONMENT=production
```

Environment variables can also be populated from Kubernetes resources such as ConfigMaps and Secrets.

---

## Resource Requests and Limits

Kubernetes allows CPU and memory resources to be specified for containers.

For example:

```yaml
resources:
  requests:
    cpu: "500m"
    memory: "512Mi"

  limits:
    cpu: "1"
    memory: "1Gi"
```

### Requests

A **request** specifies how much CPU or memory the container is expected to need.

Kubernetes uses requests when scheduling the Pod onto a node.

### Limits

A **limit** specifies the maximum amount of a resource the container can use.

Conceptually:

```text
Container
   │
   ├── CPU request: 500m
   ├── CPU limit:    1
   │
   ├── Memory request: 512Mi
   └── Memory limit:    1Gi
```

---

## Container Lifecycle

A container goes through different states during its lifecycle.

A simplified lifecycle is:

```text
Created
   │
   ▼
Running
   │
   ├── application exits
   │
   ▼
Terminated
```

Kubernetes can automatically restart containers depending on the Pod's restart policy.

For example, if an application crashes, Kubernetes may restart the container.

---

## Container Probes

Kubernetes can use **probes** to determine whether an application inside a container is working correctly.

### Liveness Probe

Checks whether the application is still alive.

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8080
```

If the liveness probe repeatedly fails, Kubernetes can restart the container.

### Readiness Probe

Checks whether the application is ready to receive traffic.

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
```

A container that is not ready can be temporarily removed from Service traffic without necessarily being restarted.

---

## Multiple Containers in a Pod

A Pod can contain multiple containers.

For example:

```text
Pod
├── Application Container
└── Sidecar Container
```

Containers within the same Pod share:

* network namespace
* IP address
* localhost
* optionally volumes

This is useful for patterns such as **sidecar containers**.

For example:

```text
Pod
├── Application
│      │
│      └── localhost
│
└── Proxy
       │
       └── localhost
```

Istio commonly uses sidecar proxies to handle network traffic for application containers.

---

## Container Filesystem

Containers have their own filesystem view.

Changes made inside a running container are generally **ephemeral**.

For example:

```text
Container
├── /app
├── /tmp
└── /data
```

If the container is deleted and recreated, changes made to its writable filesystem can disappear.

For persistent data, Kubernetes can mount a **Volume** or **PersistentVolumeClaim** into the container.

```text
Container
     │
     │ mounted volume
     ▼
Persistent Storage
```

---

## Containers and Deployments

A Deployment defines a Pod template, and the Pod template defines the containers.

```text
Deployment
    │
    ▼
ReplicaSet
    │
    ▼
Pod
    │
    └── Container
          │
          └── Image
```

For example:

```yaml
kind: Deployment

spec:
  replicas: 3

  template:
    spec:
      containers:
        - name: my-app
          image: my-app:1.0
```

This results in:

```text
Deployment
    │
    ├── Pod 1 ── Container ── my-app:1.0
    ├── Pod 2 ── Container ── my-app:1.0
    └── Pod 3 ── Container ── my-app:1.0
```

---

## Containers vs. Pods

A **container** is the environment in which an application process runs.

A **Pod** is the Kubernetes unit that groups one or more containers.

| Container                                  | Pod                                           |
| ------------------------------------------ | --------------------------------------------- |
| Runs an application process                | Runs one or more containers                   |
| Created from an image                      | Created from a Pod specification              |
| Has its own filesystem                     | Provides shared networking for its containers |
| Managed by a container runtime             | Managed by Kubernetes                         |
| Usually one main application per container | Smallest deployable Kubernetes unit           |

The relationship is:

```text
Kubernetes
    │
    ▼
   Pod
    │
    ├── Container
    └── Container
```

---

## Important Concepts

| Concept                  | Meaning                                           |
| ------------------------ | ------------------------------------------------- |
| **Container**            | Isolated environment for running an application   |
| **Container Image**      | Immutable template used to create containers      |
| **Container Runtime**    | Software that runs containers                     |
| **Registry**             | Stores and distributes container images           |
| **Pod**                  | Kubernetes unit containing one or more containers |
| **Port**                 | Network port on which an application listens      |
| **Environment Variable** | Configuration passed to a container               |
| **Resource Request**     | Amount of CPU/memory requested by a container     |
| **Resource Limit**       | Maximum CPU/memory a container can use            |
| **Liveness Probe**       | Checks whether a container should be restarted    |
| **Readiness Probe**      | Checks whether a container is ready for traffic   |
| **Volume**               | Storage mounted into a container                  |

---

## Summary

A container packages an application and its dependencies into an isolated runtime environment.

In Kubernetes, the hierarchy is:

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
Container
    │
    ▼
Container Image
```

> **A container runs an application from an image, while Kubernetes uses Pods to manage and organize containers.**
