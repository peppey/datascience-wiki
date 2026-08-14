# Deployment Repositories

## TL;DR

A **deployment repository** contains the configuration that defines how an application should be deployed.

It is often separated from the application repository, especially in **Kubernetes and GitOps** environments.

```text
Application Repository
        │
        ▼
     CI / Build
        │
        ▼
Container Registry
        │
        ▼
Deployment Repository
        │
        ▼
    Kubernetes
```

---

## Application vs. Deployment Repository

The application repository contains the source code:

```text
application-repo/
├── src/
├── tests/
├── Dockerfile
└── requirements.txt
```

The deployment repository contains deployment configuration:

```text
deployment-repo/
├── dev/
├── staging/
└── production/
```

This separates **what the application is** from **how it is deployed**.

---

## Deployment Configuration

A deployment repository can contain:

* Kubernetes manifests
* Helm charts
* Kustomize configurations
* ConfigMaps
* Secrets references
* Ingress configuration
* Environment-specific settings

For example:

```text
deployment-repo/
├── dev/
│   └── deployment.yaml
├── staging/
│   └── deployment.yaml
└── production/
    └── deployment.yaml
```

---

## Image Versions

The deployment repository commonly specifies which container image should be deployed:

```yaml
spec:
  containers:
    - name: app
      image: registry.example.com/my-app:1.4.0
```

The application repository builds the image, while the deployment repository determines which version runs.

```text
Application Repo
      │
      ▼
     CI
      │
      ▼
Container Registry
      │
      ▼
Deployment Repo
      │
      ▼
 Kubernetes
```

---

## Deployment Repository with GitOps

Deployment repositories are particularly useful with GitOps tools such as Argo CD.

```text
Deployment Repository
        │
        │ Desired State
        ▼
      Argo CD
        │
        ▼
    Kubernetes
```

A change to the deployment repository can therefore trigger a deployment.

---

## Benefits

Separating deployment configuration provides:

* Clear separation of responsibilities
* Version-controlled infrastructure
* Auditable deployment changes
* Environment-specific configuration
* Easier GitOps integration

It also allows application developers and platform teams to manage their respective repositories independently.

---

## Key Idea

A deployment repository stores the **desired deployment state** of an application.

```text
Application Repo
└── Build the application

Deployment Repo
└── Define how the application runs
```

This pattern is especially common in **Kubernetes-based GitOps architectures**.
