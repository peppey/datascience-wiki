# Ingress

## TL;DR

**Ingress** is a Kubernetes resource that defines how external HTTP/HTTPS traffic is routed to services inside a cluster.

It provides a single entry point for exposing multiple applications:

```text
Internet
   │
   ▼
Ingress
   │
   ├── /app  → app-service
   └── /api  → api-service
```

---

## Ingress Resource

An Ingress defines routing rules.

For example:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-app
spec:
  rules:
    - host: example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: app-service
                port:
                  number: 8080
```

This routes requests to `example.com` to `app-service`.

---

## Ingress Controller

An Ingress resource alone does not route traffic.

An **Ingress Controller** watches Ingress resources and implements the routing.

```text
                 Kubernetes
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
      Ingress               Ingress
       Rules                 Rules
          │                     │
          └──────────┬──────────┘
                     ▼
             Ingress Controller
                     │
                     ▼
                  Services
```

Common Ingress Controllers include:

* NGINX Ingress Controller
* Traefik
* HAProxy
* Kong

---

## Host-Based Routing

Ingress can route traffic based on the hostname.

```text
app.example.com  → app-service
api.example.com  → api-service
```

For example:

```yaml
rules:
  - host: app.example.com
    http:
      paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: app-service
              port:
                number: 8080

  - host: api.example.com
    http:
      paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: api-service
              port:
                number: 8080
```

---

## Path-Based Routing

Ingress can also route requests based on the URL path.

```text
example.com/
       │
       ├── /app → app-service
       │
       └── /api → api-service
```

For example:

```yaml
paths:
  - path: /app
    pathType: Prefix
    backend:
      service:
        name: app-service
        port:
          number: 8080

  - path: /api
    pathType: Prefix
    backend:
      service:
        name: api-service
        port:
          number: 8080
```

---

## Ingress and Services

Ingress normally routes traffic to a **Service**, not directly to a Pod.

```text
External Request
       │
       ▼
    Ingress
       │
       ▼
    Service
       │
       ▼
     Pods
```

The Service then distributes traffic to the appropriate Pods.

---

## TLS

Ingress can terminate HTTPS connections.

For example:

```yaml
tls:
  - hosts:
      - example.com
    secretName: example-tls
```

The TLS certificate is stored in a Kubernetes Secret.

```text
HTTPS Request
     │
     ▼
  Ingress
     │
     │ TLS termination
     ▼
  Service
     │
     ▼
   Pods
```

---

## Ingress vs. Service

A **Service** provides stable network access to Pods inside the cluster.

An **Ingress** provides HTTP/HTTPS routing from outside the cluster.

```text
Ingress
   │
   ▼
Service
   │
   ▼
Pods
```

A Service answers:

> How do I reach these Pods?

An Ingress answers:

> Where should this external HTTP request go?

---

## Ingress vs. LoadBalancer

A `LoadBalancer` Service can expose an application externally:

```text
Internet
   │
   ▼
LoadBalancer Service
   │
   ▼
Pods
```

Ingress provides more advanced HTTP/HTTPS routing:

```text
Internet
   │
   ▼
Ingress
   ├── app.example.com → app-service
   └── api.example.com → api-service
```

Ingress is therefore useful when multiple HTTP services share an external entry point.

---

## Typical Architecture

A typical Kubernetes application might look like:

```text
                 Internet
                    │
                    ▼
                Ingress
             ┌──────┴──────┐
             ▼             ▼
        app-service    api-service
             │             │
          ┌──┴──┐       ┌──┴──┐
          ▼     ▼       ▼     ▼
        Pod   Pod     Pod   Pod
```

---

## Key Idea

Ingress provides **HTTP/HTTPS routing into a Kubernetes cluster**.

The typical request path is:

$$
\boxed{
\text{Internet}
\rightarrow
\text{Ingress}
\rightarrow
\text{Service}
\rightarrow
\text{Pod}
}
$$

The **Ingress resource** defines the routing rules, while an **Ingress Controller** implements those rules.
