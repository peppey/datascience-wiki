# Helm

## TL;DR

**Helm** is a package manager for **Kubernetes**. It allows Kubernetes resources to be packaged, configured and deployed as reusable **Helm Charts**.

A Helm Chart typically contains:

* `Chart.yaml` — metadata about the chart
* `values.yaml` — configurable default values
* `templates/` — Kubernetes manifests containing Helm template expressions

The basic concept is:

$$
\boxed{
\text{Chart}
+
\text{Values}
\rightarrow
\text{Rendered Kubernetes YAML}
\rightarrow
\text{Kubernetes}
}
$$

Helm is especially useful when the same application needs to be deployed multiple times with different configurations, for example in different environments such as `dev`, `test` and `prod`.

---

## What Is Helm?

Kubernetes deployments are described using YAML manifests.

For example:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
```

If the same application needs different numbers of replicas in different environments, manually maintaining several YAML files quickly becomes cumbersome.

Helm solves this by separating:

1. **the structure of the Kubernetes resources**
2. **their configurable values**

For example:

```yaml
replicas: {{ .Values.replicaCount }}
```

The value can then be provided through `values.yaml`:

```yaml
replicaCount: 3
```

Helm combines the template and values to generate the final Kubernetes manifest.

---

# Helm Charts

A **Helm Chart** is a package containing everything required to describe a Kubernetes application.

A typical chart looks like:

```text
my-chart/
├── Chart.yaml
├── values.yaml
├── charts/
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   └── _helpers.tpl
└── .helmignore
```

### `Chart.yaml`

Contains metadata about the chart:

```yaml
apiVersion: v2
name: my-app
description: A Helm chart for my application
version: 1.0.0
appVersion: "1.0"
```

Important fields include:

* `name` — name of the chart
* `version` — version of the chart itself
* `appVersion` — version of the application

The two versions are conceptually different:

$$
\text{Chart Version}
\neq
\text{Application Version}
$$

A chart can change without changing the application version, for example when its deployment configuration changes.

---

## `values.yaml`

`values.yaml` contains the default configuration of a chart.

Example:

```yaml
replicaCount: 3

image:
  repository: my-registry/my-app
  tag: "1.2.0"

service:
  type: ClusterIP
  port: 8080
```

Templates can access these values through `.Values`:

```yaml
spec:
  replicas: {{ .Values.replicaCount }}
```

and:

```yaml
image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
```

This allows the same chart to be reused with different configurations.

---

# Helm Values

Values are the main mechanism for **configuring a Helm Chart**.

Suppose `values.yaml` contains:

```yaml
replicaCount: 3
```

A template can use:

```yaml
spec:
  replicas: {{ .Values.replicaCount }}
```

Helm therefore separates the configuration from the Kubernetes resource definition.

### Overriding Values

Default values can be overridden during installation.

For example:

```bash
helm install my-app ./my-chart \
  --set replicaCount=5
```

The resulting value becomes:

```yaml
replicas: 5
```

A YAML file can also be supplied:

```bash
helm install my-app ./my-chart \
  -f values-prod.yaml
```

This is particularly useful for environment-specific deployments.

For example:

```text
values.yaml
values-dev.yaml
values-test.yaml
values-prod.yaml
```

The same chart can therefore be used for multiple environments:

```text
                ┌── values-dev.yaml
                │
Helm Chart ─────┼── values-test.yaml
                │
                └── values-prod.yaml
```

The **chart contains the deployment logic**, while the values describe the environment-specific configuration.

---

# Helm Templates

The files inside `templates/` are Kubernetes manifests containing **Go template expressions**.

For example:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Release.Name }}
spec:
  replicas: {{ .Values.replicaCount }}
```

Helm evaluates these expressions before sending the resulting YAML to Kubernetes.

For example:

```text
Template
   +
Values
   +
Release information
   ↓
Helm rendering
   ↓
Kubernetes YAML
```

The result could be:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
```

---

## Template Expressions

Values are accessed using:

```text
.Values
```

For example:

```yaml
image:
  repository: my-app
  tag: "1.0"
```

can be accessed with:

```yaml
{{ .Values.image.repository }}
{{ .Values.image.tag }}
```

Helm also provides built-in objects such as:

```text
.Values
.Release
.Chart
.Capabilities
```

For example:

```yaml
metadata:
  name: {{ .Release.Name }}
```

`.Release.Name` refers to the name of the Helm release.

---

## Conditionals

Templates can contain conditional logic.

For example:

```yaml
{{- if .Values.ingress.enabled }}
apiVersion: networking.k8s.io/v1
kind: Ingress
...
{{- end }}
```

With:

```yaml
ingress:
  enabled: true
```

the Ingress is rendered.

With:

```yaml
ingress:
  enabled: false
```

it is omitted.

This makes a chart configurable without maintaining completely separate Kubernetes manifests.

---

## Loops

Helm templates can also iterate over values.

For example:

```yaml
{{- range .Values.env }}
- name: {{ .name }}
  value: {{ .value | quote }}
{{- end }}
```

with:

```yaml
env:
  - name: ENVIRONMENT
    value: production
  - name: LOG_LEVEL
    value: info
```

This produces multiple Kubernetes environment variables.

---

## Template Functions

Helm provides many functions for manipulating values.

For example:

```yaml
{{ .Values.name | quote }}
```

or:

```yaml
{{ .Values.name | upper }}
```

Functions can be chained using the pipe operator:

```text
value | function1 | function2
```

A particularly important function is `include`, which is commonly used together with helper templates.

---

## Helper Templates

Reusable template fragments are commonly stored in:

```text
templates/_helpers.tpl
```

For example:

```yaml
{{- define "my-app.fullname" -}}
{{ .Release.Name }}-{{ .Chart.Name }}
{{- end }}
```

The helper can then be used with:

```yaml
metadata:
  name: {{ include "my-app.fullname" . }}
```

This avoids duplicating naming logic across multiple manifests.

---

# Rendering a Chart

Helm can render templates locally without deploying anything.

```bash
helm template my-app ./my-chart
```

This generates the Kubernetes YAML that Helm would produce.

This is extremely useful for debugging templates.

The conceptual process is:

$$
\text{templates/}
+
\text{values.yaml}
+
\text{Helm context}
\rightarrow
\text{Rendered YAML}
$$

---

# Installing a Chart

A chart can be installed using:

```bash
helm install my-app ./my-chart
```

Here:

* `my-app` is the **release name**
* `./my-chart` is the chart

Helm creates a **release** representing this particular installation of the chart.

For example:

```text
Chart
  │
  ├── Release: dev
  ├── Release: test
  └── Release: prod
```

The same chart can therefore be installed multiple times with different configurations.

---

# Releases

A **Helm Release** is an installed instance of a chart.

For example:

```bash
helm install my-app ./my-chart
```

creates a release called:

```text
my-app
```

The release has its own:

* configuration
* Kubernetes resources
* revision history

Installed releases can be listed with:

```bash
helm list
```

Information about a release can be inspected with:

```bash
helm status my-app
```

---

# Upgrading a Release

When the chart or configuration changes, the release can be updated:

```bash
helm upgrade my-app ./my-chart
```

New values can be supplied:

```bash
helm upgrade my-app ./my-chart \
  --set replicaCount=5
```

The general lifecycle is:

```text
helm install
      ↓
helm upgrade
      ↓
helm upgrade
      ↓
helm uninstall
```

Helm also maintains release revisions, which can be useful for rollback.

---

# Rollbacks

If an upgrade causes problems, a previous revision can be restored:

```bash
helm rollback my-app 1
```

The available revisions can be inspected with:

```bash
helm history my-app
```

This makes Helm useful for managing changes to Kubernetes deployments.

---

# Helm Repositories

Charts can be distributed through **Helm repositories**.

A repository contains packaged charts that can be searched and installed.

For example:

```bash
helm repo add my-repo https://example.com/charts
helm repo update
helm search repo my-repo
```

A chart can then be installed from the repository:

```bash
helm install my-app my-repo/my-chart
```

Helm therefore provides both:

* a format for packaging Kubernetes applications
* a mechanism for distributing those packages

---

# Chart Dependencies

A chart can depend on other charts.

Dependencies are commonly declared in:

```text
Chart.yaml
```

For example:

```yaml
dependencies:
  - name: redis
    version: "20.x"
    repository: "https://example.com/charts"
```

Dependencies can be downloaded with:

```bash
helm dependency update
```

This allows complex applications to be composed from multiple charts.

---

# Helm and Kubernetes

Helm does **not replace Kubernetes**.

Instead:

```text
Helm
  ↓
generates/manages
  ↓
Kubernetes manifests
  ↓
Kubernetes API
  ↓
Kubernetes resources
```

Kubernetes ultimately operates on resources such as:

* Deployments
* Services
* ConfigMaps
* Secrets
* Ingresses
* Jobs
* StatefulSets

Helm provides a higher-level packaging and configuration mechanism for these resources.

---

# Helm and GitOps

Helm is frequently used together with **GitOps** tools such as Argo CD.

A Git repository can contain:

```text
my-application/
├── Chart.yaml
├── values.yaml
└── templates/
```

A GitOps tool can then use the chart to generate the desired Kubernetes state.

Conceptually:

```text
Git Repository
      ↓
Helm Chart
      ↓
Helm Rendering
      ↓
Kubernetes Manifests
      ↓
Kubernetes Cluster
```

This is particularly useful when the desired deployment configuration should be version-controlled.

---

# Helm in Different Environments

One of the major advantages of Helm is that a single chart can be reused across environments.

For example:

```text
                 ┌── values-dev.yaml
                 │
my-app Chart ────┼── values-test.yaml
                 │
                 └── values-prod.yaml
```

The templates remain largely identical while values change.

For example:

```yaml
# values-dev.yaml
replicaCount: 1
```

versus:

```yaml
# values-prod.yaml
replicaCount: 5
```

This avoids duplicating entire Kubernetes manifests.

---

# Useful Helm Commands

### Create a chart

```bash
helm create my-chart
```

### Render templates

```bash
helm template my-app ./my-chart
```

### Validate a chart

```bash
helm lint ./my-chart
```

### Install

```bash
helm install my-app ./my-chart
```

### List releases

```bash
helm list
```

### Show release status

```bash
helm status my-app
```

### Upgrade

```bash
helm upgrade my-app ./my-chart
```

### Show release history

```bash
helm history my-app
```

### Roll back

```bash
helm rollback my-app 1
```

### Uninstall

```bash
helm uninstall my-app
```

---

# Key Concepts

| Concept            | Meaning                                              |
| ------------------ | ---------------------------------------------------- |
| **Chart**          | Package containing Kubernetes deployment definitions |
| **Chart.yaml**     | Chart metadata                                       |
| **values.yaml**    | Default configuration                                |
| **Template**       | Kubernetes manifest containing dynamic expressions   |
| **Release**        | Installed instance of a chart                        |
| **Repository**     | Source from which charts can be distributed          |
| **`templates/`**   | Directory containing Kubernetes templates            |
| **`_helpers.tpl`** | Reusable template definitions                        |
| **`--set`**        | Override individual values                           |
| **`-f`**           | Supply an alternative values file                    |

---

# Mental Model

The most important distinction is:

```text
Chart
│
├── templates/       → HOW the resources are structured
│
├── values.yaml      → WHAT can be configured
│
└── Chart.yaml       → WHAT the chart is
```

During deployment:

```text
        Chart
          +
        Values
          ↓
    Helm Templates
          ↓
    Rendered YAML
          ↓
   Kubernetes API
          ↓
 Kubernetes Resources
```

Thus, **Helm is essentially a templating, packaging and release-management layer on top of Kubernetes**.
