# Namespaces

## TL;DR

A **Namespace** provides a logical boundary for resources inside a Kubernetes cluster.

Namespaces are commonly used to separate applications, teams, or environments.

```text
Kubernetes Cluster
│
├── development
│   ├── Pods
│   ├── Services
│   └── Deployments
│
├── staging
│   ├── Pods
│   ├── Services
│   └── Deployments
│
└── production
    ├── Pods
    ├── Services
    └── Deployments
```

---

## Creating a Namespace

A Namespace can be defined using YAML:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: development
```

Or created using `kubectl`:

```bash
kubectl create namespace development
```

---

## Resource Isolation

Resources can belong to a specific Namespace.

For example:

```yaml
metadata:
  name: my-app
  namespace: development
```

The same resource name can therefore exist in different Namespaces:

```text
development/my-app
production/my-app
```

---

## Namespaces and Services

Services are typically addressed within their Namespace.

For example:

```text
my-service
```

refers to a Service in the current Namespace, while:

```text
my-service.production.svc.cluster.local
```

can be used to address a Service in the `production` Namespace.

---

## Resource Management

Namespaces can be used together with:

* **RBAC** for access control
* **ResourceQuotas** for resource limits
* **NetworkPolicies** for network isolation

This makes Namespaces useful for separating workloads and controlling access.

---

## Key Idea

A Namespace is a **logical partition of a Kubernetes cluster**.

$$
\boxed{
\text{Cluster}
\rightarrow
\text{Namespace}
\rightarrow
\text{Resources}
}
$$

Namespaces provide organization and isolation, but they do **not** create separate Kubernetes clusters.
