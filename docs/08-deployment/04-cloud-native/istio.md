# Istio

## TL;DR (30 seconds)

**Istio** is a **service mesh** for managing communication between services in a Kubernetes cluster.

The key idea:

> Istio adds networking, security, observability, and traffic-management capabilities to services **without requiring the application code to implement them**.

---

## What is a Service Mesh?

A service mesh manages communication between services in a distributed application.

Without Istio:

```text id="8q1x2a"
Service A ──────────→ Service B
              HTTP
```

With Istio:

```text id="7m3k9p"
Service A                  Service B
    │                           │
    ▼                           ▼
┌────────┐                  ┌────────┐
│ Sidecar│ ───────────────→ │ Sidecar│
└────────┘                  └────────┘
       \                      /
        └────── Istio ───────┘
```

The service mesh can manage the communication between the services.

---

## Istio Architecture

Istio consists of two main conceptual parts:

```text id="2h8k4w"
                Istio
                  │
        ┌─────────┴─────────┐
        │                   │
     Control Plane       Data Plane
        │                   │
        │              ┌────┴────┐
        │              │         │
        ▼              ▼         ▼
   Configuration    Proxy     Proxy
                    (Pod A)   (Pod B)
```

### Control Plane

The **control plane** manages configuration and provides it to the proxies.

### Data Plane

The **data plane** consists of the proxies that actually handle network traffic.

---

## Sidecar Proxy

Traditionally, Istio uses a proxy alongside each application container.

```text id="6f4j2k"
Pod
┌──────────────────────────────┐
│                              │
│  Application Container       │
│         │                    │
│         ▼                    │
│      localhost               │
│         │                    │
│         ▼                    │
│  Envoy Sidecar Proxy         │
│                              │
└──────────────────────────────┘
```

The proxy intercepts network traffic and can apply Istio's networking policies.

The proxy used by Istio is based on **Envoy**.

---

## Traffic Management

Istio allows traffic to be controlled without changing application code.

For example, traffic can be routed based on:

* hostname
* URL path
* HTTP headers
* weights
* service versions

A typical setup:

```text id="9s7d1f"
Client
  │
  ▼
Gateway
  │
  ▼
VirtualService
  │
  ├──────────→ v1
  │
  └──────────→ v2
```

For example, 90% of requests can go to version 1 and 10% to version 2.

This is useful for **canary deployments**.

---

## VirtualService

A `VirtualService` defines **routing rules**.

For example:

```yaml id="a1b2c3"
http:
  - route:
      - destination:
          host: my-service
          subset: v1
        weight: 90

      - destination:
          host: my-service
          subset: v2
        weight: 10
```

The VirtualService decides where matching requests should go.

---

## Gateway

A `Gateway` defines how traffic enters or leaves the service mesh.

```text id="d4e5f6"
Internet
   │
   ▼
Gateway
   │
   ▼
VirtualService
   │
   ▼
Service
```

A Gateway can define:

* ports
* protocols
* hostnames
* TLS configuration

The Gateway and VirtualService are often used together.

---

## DestinationRule

A `DestinationRule` defines policies for traffic **after it has been routed to a destination**.

It can define **subsets** of a service.

For example:

```yaml id="g7h8i9"
spec:
  host: my-service
  subsets:
    - name: v1
      labels:
        version: v1

    - name: v2
      labels:
        version: v2
```

This allows a VirtualService to route traffic specifically to:

```text id="j1k2l3"
my-service
    │
    ├── v1
    │
    └── v2
```

---

## Security

Istio can provide security features for service-to-service communication.

These include:

* mutual TLS (mTLS)
* authentication
* authorization
* encrypted service communication

With mTLS:

```text id="m4n5o6"
Service A
   │
   │ encrypted + authenticated
   ▼
Service B
```

The application itself does not need to implement TLS for this communication.

---

## Observability

Istio can provide information about service communication.

For example:

```text id="p7q8r9"
Service A ──→ Service B
    │
    ├── latency
    ├── request count
    ├── error rate
    └── traffic volume
```

This information can be integrated with observability systems such as:

* Prometheus
* Grafana
* Jaeger
* Kiali

This makes it easier to understand how services communicate.

---

## Retries and Timeouts

Istio can configure network behavior such as retries and timeouts.

For example:

```yaml id="s1t2u3"
http:
  - timeout: 5s
    retries:
      attempts: 3
      perTryTimeout: 2s
```

Conceptually:

```text id="v4w5x6"
Request
   │
   ▼
Service B
   │
   ├── failure
   │
   ▼
 retry
   │
   ▼
Service B
```

This allows some resilience behavior to be configured independently of application code.

---

## Istio and Kubernetes

Istio extends Kubernetes rather than replacing it.

```text id="y7z8a9"
Kubernetes
│
├── Pods
├── Services
├── Deployments
└── ...
       │
       ▼
     Istio
       │
       ├── Traffic management
       ├── Security
       └── Observability
```

Istio uses Kubernetes resources as well as its own Custom Resources.

---

## Important Istio Resources

Some important Istio resources are:

| Resource              | Purpose                                  |
| --------------------- | ---------------------------------------- |
| `Gateway`             | Defines network entry/exit               |
| `VirtualService`      | Defines traffic routing                  |
| `DestinationRule`     | Defines destination policies and subsets |
| `ServiceEntry`        | Adds external services to the mesh       |
| `AuthorizationPolicy` | Controls access between workloads        |
| `PeerAuthentication`  | Configures workload authentication/mTLS  |

---

## Example Architecture

A typical Istio deployment can look like:

```text id="b1c2d3"
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
                ┌───────────┼───────────┐
                ▼           ▼           ▼
             Pod v1      Pod v1      Pod v2
                │           │           │
             Envoy        Envoy        Envoy
                │           │           │
                └───────────┴───────────┘
                         Istio
```

---

## Istio vs. Kubernetes

Kubernetes primarily manages **workloads and their basic networking**.

Istio adds advanced **service-to-service communication management**.

```text id="e4f5g6"
Kubernetes
    │
    ├── Run containers
    ├── Manage Pods
    ├── Manage Services
    └── Schedule workloads

Istio
    │
    ├── Route traffic
    ├── Secure communication
    ├── Observe traffic
    └── Control service communication
```

---

## Key Takeaways

1. **Istio is a service mesh for Kubernetes and other environments.**
2. It manages communication between services.
3. Its **data plane** handles traffic, traditionally using Envoy proxies.
4. Its **control plane** distributes configuration to the data plane.
5. `VirtualService` controls routing.
6. `Gateway` controls network entry and exit.
7. `DestinationRule` defines destination policies and subsets.
8. Istio provides additional **security, observability, and traffic-management** capabilities.
