# Virtual Services

## TL;DR (30 seconds)

An **Istio VirtualService** is a resource used to define **how incoming traffic is routed to services within an Istio service mesh**.

The key idea:

> **A VirtualService defines routing rules that determine where network traffic should go.**

For example, a VirtualService can route traffic based on:

* URL paths
* HTTP headers
* URI
* ports
* weights

A VirtualService usually works together with an **Istio Gateway** or an Istio-managed service mesh.

---

## VirtualService in Istio

A VirtualService is a **Custom Resource** provided by Istio.

It does not directly expose an application or create a Kubernetes Service.

Instead, it defines **routing rules** for traffic.

```text
Client
   │
   ▼
Istio Gateway
   │
   ▼
VirtualService
   │
   │ routing rules
   ▼
Kubernetes Service
   │
   ▼
Pods
```

---

## Basic VirtualService

A simple VirtualService can route all traffic to a Kubernetes Service:

```yaml
apiVersion: networking.istio.io/v1
kind: VirtualService

metadata:
  name: my-app

spec:
  hosts:
    - my-app.example.com

  http:
    - route:
        - destination:
            host: my-app
            port:
              number: 8080
```

This means:

> Requests for `my-app.example.com` should be routed to the `my-app` Service on port `8080`.

---

## `hosts`

The `hosts` field specifies the hostnames to which the routing rules apply.

```yaml
hosts:
  - my-app.example.com
```

It can also refer to a Kubernetes Service:

```yaml
hosts:
  - my-app
```

The hostname must correspond to the traffic that Istio is handling.

---

## HTTP Routing

VirtualServices can define routing rules for HTTP traffic.

For example:

```yaml
http:
  - match:
      - uri:
          prefix: /api

    route:
      - destination:
          host: my-app
```

This rule means:

```text
/api/users
/api/products
/api/orders
```

are routed to `my-app`.

---

## URI Matching

Traffic can be matched based on the URI.

### Prefix

```yaml
match:
  - uri:
      prefix: /api
```

Matches:

```text
/api
/api/users
/api/products
```

### Exact

```yaml
match:
  - uri:
      exact: /health
```

Only matches:

```text
/health
```

### Regular Expression

```yaml
match:
  - uri:
      regex: "^/api/[0-9]+$"
```

Can match paths such as:

```text
/api/123
/api/456
```

---

## Routing to Different Services

A VirtualService can route different requests to different services.

```yaml
http:
  - match:
      - uri:
          prefix: /api

    route:
      - destination:
          host: backend

  - match:
      - uri:
          prefix: /frontend

    route:
      - destination:
          host: frontend
```

The resulting routing is:

```text
/api/*       → backend
/frontend/*  → frontend
```

---

## Traffic Splitting

VirtualServices can split traffic between different versions of an application.

For example:

```yaml
http:
  - route:
      - destination:
          host: my-app
          subset: v1
        weight: 90

      - destination:
          host: my-app
          subset: v2
        weight: 10
```

This results in approximately:

```text
             ┌── v1 → 90%
Traffic ─────┤
             └── v2 → 10%
```

This can be used for **canary deployments** and gradual rollouts.

---

## Subsets

A **subset** represents a particular group of workloads belonging to a service.

For example:

```text
my-app
├── v1
│   ├── Pod
│   └── Pod
│
└── v2
    ├── Pod
    └── Pod
```

The subsets are usually defined using labels.

For example, Pods might have:

```yaml
labels:
  app: my-app
  version: v1
```

A corresponding Istio `DestinationRule` can define the subsets:

```yaml
apiVersion: networking.istio.io/v1
kind: DestinationRule

metadata:
  name: my-app

spec:
  host: my-app

  subsets:
    - name: v1
      labels:
        version: v1

    - name: v2
      labels:
        version: v2
```

The VirtualService then uses these subsets when routing traffic.

---

## VirtualService and DestinationRule

A **VirtualService** defines **how traffic is routed**.

A **DestinationRule** defines **how traffic should be handled after routing to a destination**.

Conceptually:

```text
                 VirtualService
                       │
                 Where should
                  traffic go?
                       │
                       ▼
                  Destination
                       │
                       ▼
                DestinationRule
                       │
              How should the
              destination behave?
```

For example:

```text
VirtualService
    │
    ├── 90% → my-app:v1
    └── 10% → my-app:v2
                    │
                    ▼
             DestinationRule
             defines v1 / v2
```

---

## VirtualService and Gateway

A VirtualService can also be associated with an **Istio Gateway**.

For example:

```yaml
spec:
  hosts:
    - my-app.example.com

  gateways:
    - my-app-gateway

  http:
    - route:
        - destination:
            host: my-app
```

The Gateway handles the network entry point, while the VirtualService defines what happens to the incoming traffic.

```text
Internet
   │
   ▼
Istio Gateway
   │
   ▼
VirtualService
   │
   ▼
Kubernetes Service
   │
   ▼
Pods
```

---

## VirtualService vs. Kubernetes Service

A Kubernetes **Service** and an Istio **VirtualService** have different purposes.

| Resource               | Purpose                                       |
| ---------------------- | --------------------------------------------- |
| **Kubernetes Service** | Provides a stable network endpoint for Pods   |
| **VirtualService**     | Defines traffic routing rules                 |
| **Gateway**            | Defines how traffic enters or leaves the mesh |
| **DestinationRule**    | Defines policies for traffic to a destination |

A VirtualService does **not** replace a Kubernetes Service.

For example:

```text
VirtualService
      │
      ▼
Kubernetes Service
      │
      ▼
    Pods
```

---

## Typical Use Cases

VirtualServices are commonly used for:

### Path-based routing

```text
/api/*       → backend
/frontend/*  → frontend
```

### Canary deployments

```text
v1 → 90%
v2 → 10%
```

### Header-based routing

```text
Header: x-version=v2
              │
              ▼
             v2
```

### A/B testing

Different users can be routed to different versions of an application.

### Traffic migration

Traffic can gradually be moved from one version to another:

```text
v1: 100% → 90% → 50% → 10% → 0%
v2:   0% → 10% → 50% → 90% → 100%
```

---

## Typical Request Flow

A request through an Istio-managed application can look like:

```text
Client
  │
  │ HTTP request
  ▼
Gateway
  │
  ▼
VirtualService
  │
  │ evaluate routing rules
  ▼
Destination
  │
  ▼
Service / Pods
```

The VirtualService determines which destination should receive the request based on its configured rules.

---

## Important Concepts

| Concept             | Meaning                                                  |
| ------------------- | -------------------------------------------------------- |
| **VirtualService**  | Istio resource defining traffic routing rules            |
| **Host**            | Hostname to which the routing rules apply                |
| **Match**           | Conditions that determine whether a routing rule applies |
| **Route**           | Destination to which matching traffic is sent            |
| **Gateway**         | Defines how traffic enters or leaves the mesh            |
| **DestinationRule** | Defines policies and subsets for a destination           |
| **Subset**          | Group of workloads belonging to a particular version     |
| **Weight**          | Percentage of traffic sent to a destination              |

---

## Summary

An Istio **VirtualService** controls **how traffic is routed** between clients, gateways, services, and application versions.

The basic relationship is:

```text
              Gateway
                 │
                 ▼
          VirtualService
                 │
          routing rules
                 │
                 ▼
      Kubernetes Service
                 │
                 ▼
                Pods
```

> **A VirtualService defines where traffic should go; it does not itself provide the network endpoint.**
