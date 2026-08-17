# OpenShift Foundations

## TL;DR

**OpenShift** is a Kubernetes-based platform for deploying, managing, and operating containerized applications.

It extends Kubernetes with additional features for:

* security
* networking
* developer workflows
* monitoring
* application management
* cluster administration

The basic architecture is:

```text
                    OpenShift Cluster
                           │
             ┌─────────────┴─────────────┐
             │                           │
        Control Plane                 Worker Nodes
             │                           │
      Kubernetes API               ┌─────┴─────┐
             │                     ▼           ▼
          etcd                    Pod         Pod
             │                     │           │
        OpenShift                 Container   Container
        Components
```

OpenShift therefore builds on the Kubernetes foundation:

$$
\boxed{
\text{OpenShift}
=

\text{Kubernetes}
+
\text{Platform Features}
}
$$

---

## OpenShift and Kubernetes

OpenShift is built on Kubernetes.

Kubernetes provides the core orchestration functionality:

* Pods
* Deployments
* Services
* ConfigMaps
* Secrets
* Namespaces
* Controllers
* Scheduling

OpenShift adds additional platform capabilities around these concepts.

```text
OpenShift
│
├── Kubernetes
│   ├── Pods
│   ├── Deployments
│   ├── Services
│   ├── Namespaces
│   └── Controllers
│
└── OpenShift Features
    ├── Routes
    ├── Security
    ├── Operators
    ├── Web Console
    └── Developer Tools
```

The important distinction is:

> OpenShift is not a replacement for Kubernetes. It is a Kubernetes platform.

---

## OpenShift Cluster

An OpenShift cluster consists primarily of:

* **Control Plane Nodes**
* **Worker Nodes**

```text
OpenShift Cluster
│
├── Control Plane
│   ├── API Server
│   ├── Scheduler
│   ├── Controllers
│   └── etcd
│
└── Worker Nodes
    ├── Pod
    ├── Pod
    └── Pod
```

The Control Plane manages the cluster, while Worker Nodes run application workloads.

---

## API Server

The **Kubernetes API Server** is the central interface for the cluster.

OpenShift provides additional APIs and resources on top of the Kubernetes API.

For example:

```text
oc / kubectl
      │
      ▼
   API Server
      │
      ├── Kubernetes API
      │
      └── OpenShift APIs
```

Users and applications can therefore interact with the cluster through the API.

---

## `oc` CLI

OpenShift provides the `oc` command-line interface.

It is similar to `kubectl` but includes additional OpenShift-specific functionality.

For example:

```bash
oc get pods
```

```bash
oc get projects
```

```bash
oc get routes
```

```bash
oc logs my-app
```

```bash
oc apply -f deployment.yaml
```

Because OpenShift is Kubernetes-based, many `kubectl` commands also work with OpenShift.

The general workflow is:

```text
oc
 │
 ▼
OpenShift API
 │
 ▼
Kubernetes / OpenShift Resources
```

---

## Projects

An OpenShift **Project** is closely related to a Kubernetes **Namespace**.

A Project provides a logical boundary for application resources.

For example:

```text
OpenShift Cluster
│
├── project: development
│   ├── Deployment
│   ├── Service
│   └── Pod
│
├── project: staging
│   ├── Deployment
│   ├── Service
│   └── Pod
│
└── project: production
    ├── Deployment
    ├── Service
    └── Pod
```

Projects are commonly used to separate applications, teams, or environments.

Conceptually:

$$
\boxed{
\text{OpenShift Project}
\approx
\text{Kubernetes Namespace}
}
$$

OpenShift adds additional project-oriented functionality and policies around the namespace concept.

---

## Pods

A **Pod** remains the fundamental deployment unit in OpenShift.

A Pod contains one or more containers:

```text
Pod
│
├── Application Container
└── Sidecar Container
```

OpenShift uses the same Kubernetes Pod model.

For example:

```bash
oc get pods
```

might return:

```text
NAME                         READY   STATUS
my-app-7d8f9c6f7b-x2k9m     1/1     Running
my-app-7d8f9c6f7b-p4n8q     1/1     Running
```

---

## Deployments

OpenShift uses Kubernetes **Deployments** to manage replicated application Pods.

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

For example:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
```

The Deployment controller ensures that the desired number of Pods is running.

---

## Services

A Kubernetes **Service** provides stable network access to a group of Pods.

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

The Service provides an internal endpoint for the application.

---

## Routes

One of the most important OpenShift-specific concepts is the **Route**.

A Route exposes a Service externally using HTTP or HTTPS.

```text
Internet
   │
   ▼
 Route
   │
   ▼
Service
   │
   ▼
Pods
```

For example:

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: my-app
spec:
  to:
    kind: Service
    name: my-app
```

A Route can provide a hostname such as:

```text
https://my-app.example.com
```

---

## Route vs. Ingress

Both **Routes** and **Ingresses** can expose HTTP/HTTPS applications.

The conceptual difference is:

```text
Kubernetes:

Internet
   │
   ▼
Ingress
   │
   ▼
Service
```

```text
OpenShift:

Internet
   │
   ▼
Route
   │
   ▼
Service
```

OpenShift Routes are an OpenShift-native resource and are tightly integrated with the OpenShift networking stack.

OpenShift also supports the Kubernetes Ingress API.

---

## OpenShift Router

The **OpenShift Router** implements external HTTP/HTTPS routing.

Conceptually:

```text
Internet
   │
   ▼
OpenShift Router
   │
   ▼
Route
   │
   ▼
Service
   │
   ▼
Pod
```

The router is typically implemented using HAProxy-based infrastructure.

The Route defines how the external hostname should be associated with a Service, while the router handles the actual traffic.

---

## Security Context Constraints

OpenShift places strong emphasis on container security.

A major OpenShift-specific security mechanism is the **Security Context Constraint (SCC)**.

SCCs control what Pods and containers are allowed to do.

They can restrict things such as:

* running as root
* Linux capabilities
* host networking
* host filesystem access
* privileged containers

Conceptually:

```text
Pod
 │
 ▼
Security Context
 │
 ▼
SCC
 │
 ▼
Allowed / Denied
```

This is an important difference when deploying applications to OpenShift compared with a less restrictive Kubernetes environment.

---

## Service Accounts

A **ServiceAccount** represents an identity used by workloads running inside the cluster.

For example:

```text
Pod
 │
 ▼
ServiceAccount
 │
 ▼
Permissions
 │
 ▼
Kubernetes API
```

Service accounts can be granted permissions using **RBAC**.

For example, a Pod might use a ServiceAccount to access specific Kubernetes resources.

---

## RBAC

**Role-Based Access Control (RBAC)** determines which users, groups, and ServiceAccounts are allowed to perform specific actions.

For example:

```text
User
 │
 ▼
Role / ClusterRole
 │
 ▼
Permissions
 │
 ├── get
 ├── list
 ├── create
 └── delete
```

Permissions can be bound to identities using:

* RoleBinding
* ClusterRoleBinding

A Role is generally scoped to a Project/Namespace, while a ClusterRole can define cluster-wide permissions.

---

## Operators

**Operators** are one of the defining concepts of OpenShift.

An Operator extends Kubernetes with domain-specific automation.

For example, an Operator can manage:

* databases
* monitoring systems
* storage systems
* networking components
* application platforms

Conceptually:

```text
Custom Resource
      │
      ▼
   Operator
      │
      ▼
Kubernetes Resources
```

Instead of manually managing many Kubernetes resources, users interact with a higher-level custom resource.

---

## Custom Resources

A **Custom Resource (CR)** extends the Kubernetes API with a new resource type.

For example, an Operator might introduce:

```yaml
apiVersion: example.com/v1
kind: MyDatabase
metadata:
  name: database
spec:
  replicas: 3
```

The Operator watches this resource and creates or manages the required underlying resources.

```text
MyDatabase
    │
    ▼
 Operator
    │
    ├── Deployment
    ├── Service
    ├── ConfigMap
    └── PersistentVolumeClaim
```

This is the foundation of the Kubernetes Operator pattern.

---

## OpenShift Web Console

OpenShift provides a web-based **Web Console** for managing the cluster.

It allows users to inspect and manage:

* Projects
* Pods
* Deployments
* Services
* Routes
* ConfigMaps
* Secrets
* Operators
* workloads
* cluster resources

Conceptually:

```text
Browser
   │
   ▼
OpenShift Web Console
   │
   ▼
OpenShift API
   │
   ▼
Cluster
```

The Web Console provides a graphical alternative to using `oc` and `kubectl`.

---

## Image Registry

OpenShift can integrate with container image registries.

An image might be stored in a registry:

```text
Container Image
      │
      ▼
   Registry
      │
      ▼
    OpenShift
      │
      ▼
     Pod
```

For example:

```text
registry.example.com/my-team/my-app:1.0
```

The Pod uses the image to create its application container.

OpenShift also supports its own integrated image registry in appropriate cluster configurations.

---

## ImageStreams

OpenShift provides an additional abstraction called an **ImageStream**.

An ImageStream tracks container images and can help integrate image updates with OpenShift workloads.

Conceptually:

```text
Container Registry
        │
        ▼
   ImageStream
        │
        ▼
    Application
```

This allows OpenShift to react to changes in image versions without requiring every deployment workflow to manually manage image metadata.

---

## Build and Deployment Workflows

OpenShift supports different approaches for building and deploying applications.

A common modern workflow is:

```text
Source Code
    │
    ▼
CI Pipeline
    │
    ▼
Container Image
    │
    ▼
Container Registry
    │
    ▼
OpenShift
    │
    ▼
Deployment
    │
    ▼
Pods
```

OpenShift can therefore be integrated with CI/CD and GitOps systems such as Jenkins and Argo CD.

---

## Monitoring

OpenShift provides integrated monitoring capabilities.

A simplified architecture is:

```text
Applications
     │
     ▼
Metrics
     │
     ▼
Monitoring Stack
     │
     ├── Prometheus
     └── Alerting
```

Metrics can be used to monitor:

* CPU usage
* memory usage
* Pod health
* application metrics
* cluster resources

The OpenShift Web Console provides interfaces for inspecting monitoring information.

---

## OpenShift Networking

OpenShift provides networking between:

* Pods
* Services
* Projects
* external clients

A simplified request path is:

```text
External Client
      │
      ▼
    Route
      │
      ▼
   Service
      │
      ▼
     Pod
```

Inside the cluster, Pods can communicate through the Kubernetes networking model.

---

## Secrets and ConfigMaps

OpenShift uses the same Kubernetes mechanisms for application configuration.

**ConfigMaps** contain non-sensitive configuration:

```text
ConfigMap
    │
    ▼
   Pod
```

**Secrets** contain sensitive configuration:

```text
Secret
   │
   ▼
  Pod
```

For example:

```yaml
env:
  - name: DATABASE_URL
    valueFrom:
      secretKeyRef:
        name: database-secret
        key: url
```

---

## Persistent Storage

OpenShift uses Kubernetes storage abstractions such as:

* PersistentVolumes
* PersistentVolumeClaims
* StorageClasses

The typical relationship is:

```text
Pod
 │
 ▼
PVC
 │
 ▼
StorageClass
 │
 ▼
PersistentVolume
 │
 ▼
Physical Storage
```

This allows workloads to use persistent storage independently of the underlying storage implementation.

---

## OpenShift Resource Model

A simplified OpenShift application can be represented as:

```text
OpenShift Cluster
│
└── Project
    │
    ├── Deployment
    │    │
    │    └── Pods
    │
    ├── Service
    │
    ├── Route
    │
    ├── ConfigMap
    │
    ├── Secret
    │
    └── PersistentVolumeClaim
```

The main relationships are:

```text
Route
  │
  ▼
Service
  │
  ▼
Pods
  ▲
  │
Deployment
```

---

## Typical OpenShift Architecture

A typical externally accessible application might look like:

```text
                         Internet
                            │
                            ▼
                         Route
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

The application itself is usually managed by a Deployment:

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

Configuration and storage can be attached separately:

```text
                Deployment
                    │
                    ▼
                   Pods
                 ┌──┼──┐
                 │  │  │
                 ▼  ▼  ▼
            ConfigMap Secret PVC
```

---

## Kubernetes vs. OpenShift

The relationship can be summarized as:

| Kubernetes       | OpenShift           |
| ---------------- | ------------------- |
| Pod              | Pod                 |
| Deployment       | Deployment          |
| Service          | Service             |
| Namespace        | Project / Namespace |
| Ingress          | Ingress + Route     |
| RBAC             | RBAC                |
| ConfigMap        | ConfigMap           |
| Secret           | Secret              |
| PersistentVolume | PersistentVolume    |
| Custom Resource  | Custom Resource     |
| Operators        | Operators           |
| `kubectl`        | `oc` + `kubectl`    |

OpenShift therefore retains the Kubernetes object model while adding platform-specific resources and operational features.

---

## Key Idea

OpenShift is a **Kubernetes-based application platform** that adds security, networking, automation, developer tooling, and cluster management capabilities.

The most important concepts are:

* **Cluster** — the complete OpenShift environment
* **Project** — a logical application boundary
* **Pod** — the smallest deployable unit
* **Deployment** — manages application Pods
* **Service** — provides stable internal networking
* **Route** — exposes HTTP/HTTPS applications externally
* **Operator** — automates management of complex applications
* **SCC** — controls container security capabilities
* **RBAC** — controls access to cluster resources
* **Web Console** — graphical cluster management interface
* **`oc`** — OpenShift command-line interface

The typical application request path is:

$$
\boxed{
\text{Internet}
\rightarrow
\text{Route}
\rightarrow
\text{Service}
\rightarrow
\text{Pod}
\rightarrow
\text{Container}
}
$$

And the relationship to Kubernetes can be summarized as:

$$
\boxed{
\text{OpenShift}
=

\text{Kubernetes}
+
\text{Security}
+
\text{Networking}
+
\text{Operators}
+
\text{Developer Tools}
+
\text{Platform Management}
}
$$
