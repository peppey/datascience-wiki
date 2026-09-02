# Gateways

## TL;DR (30 seconds)

A **Gateway** controls how network traffic enters or leaves a Kubernetes cluster or service mesh.

The key idea:

> A Gateway defines **where traffic enters or exits**, while routing resources such as an Istio `VirtualService` define **where that traffic should go**.

---

## What is a Gateway?

A Gateway is a network entry or exit point.

In an Istio service mesh, a Gateway defines how traffic from outside the mesh can enter the cluster.

```text id="w6z5pk"
Internet
   │
   │ HTTP/HTTPS
   ▼
Gateway
   │
   ▼
VirtualService
   │
   ▼
Service
   │
   ▼
Pod
```

The Gateway is therefore concerned with the **network interface**, while the VirtualService is concerned with **routing**.

---

## Istio Gateway

An Istio Gateway is a Kubernetes Custom Resource:

```yaml id="c9j4mv"
apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: my-gateway
spec:
  selector:
    istio: ingressgateway

  servers:
    - port:
        number: 80
        name: http
        protocol: HTTP
      hosts:
        - example.com
```

The important parts are:

* `selector` → selects the Istio Gateway workload
* `servers` → defines ports and protocols
* `hosts` → specifies which hostnames are accepted

---

## Gateway vs. VirtualService

These two resources are often used together.

### Gateway

Defines:

> **How does traffic enter?**

For example:

```text
HTTPS
port 443
host example.com
```

### VirtualService

Defines:

> **Where should the traffic go?**

For example:

```text
/example
    ↓
my-service
```

Together:

```text id="17x2uq"
Client
  │
  │ HTTPS
  ▼
Gateway
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

## Gateway and Kubernetes Service

A Gateway is not the same thing as a Kubernetes Service.

|                          | Gateway            | Service                          |
| ------------------------ | ------------------ | -------------------------------- |
| Purpose                  | Network entry/exit | Stable access to Pods            |
| Layer                    | Traffic management | Service discovery/load balancing |
| Defines external access  | ✅                  | 🟡                               |
| Selects Pods             | ❌                  | ✅                                |
| Routing rules            | ❌/limited          | ❌                                |
| Used with VirtualService | ✅                  | Often                            |

A simplified flow is:

```text id="y8p6v5"
External Client
      ↓
   Gateway
      ↓
VirtualService
      ↓
   Service
      ↓
     Pods
```

---

## Gateway Selector

An Istio Gateway usually selects an existing Gateway workload:

```yaml id="t1y2u3"
selector:
  istio: ingressgateway
```

The selector connects the Gateway configuration to the corresponding Istio ingress gateway Pods.

```text id="v5x6z7"
Gateway Resource
      │
      │ selector
      ▼
Istio Ingress Gateway
      │
      ▼
    Pods
```

This is an important distinction:

> The `Gateway` resource describes configuration; the ingress gateway workload actually processes the traffic.

---

## Gateway Servers

The `servers` section defines how traffic should be accepted.

For example:

```yaml id="p4q5r6"
servers:
  - port:
      number: 443
      name: https
      protocol: HTTPS
    hosts:
      - example.com
```

A server can define:

* port
* protocol
* hostname
* TLS configuration

Common protocols include:

```text
HTTP
HTTPS
TCP
TLS
```

---

## TLS Termination

A Gateway can also handle TLS configuration.

For example:

```text id="a7b8c9"
Client
  │
  │ HTTPS
  ▼
Gateway
  │
  │ HTTP
  ▼
Service
```

The Gateway terminates the TLS connection and forwards the request into the service mesh.

This is called **TLS termination**.

---

## Gateway + VirtualService Example

Gateway:

```yaml id="d1e2f3"
apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: app-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
    - port:
        number: 80
        name: http
        protocol: HTTP
      hosts:
        - app.example.com
```

VirtualService:

```yaml id="g4h5i6"
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: app
spec:
  hosts:
    - app.example.com

  gateways:
    - app-gateway

  http:
    - route:
        - destination:
            host: app-service
```

The relationship is:

```text id="j7k8l9"
app.example.com
       │
       ▼
  app-gateway
       │
       ▼
VirtualService
       │
       ▼
 app-service
       │
       ▼
     Pods
```

The `gateways` field in the VirtualService connects the routing rules to the Gateway.

---

## Ingress Gateway

An **Ingress Gateway** handles traffic entering the service mesh.

```text id="m1n2o3"
                 Istio Mesh
                     │
Internet ──→ Ingress Gateway
                     │
                     ▼
                Application
```

The ingress gateway is typically deployed as a set of Pods.

These Pods receive external traffic and forward it to services inside the mesh.

---

## Egress Gateway

An **Egress Gateway** handles traffic leaving the service mesh.

```text id="p4q5r6"
Application
     │
     ▼
Egress Gateway
     │
     ▼
External Service
```

This can be useful when outbound traffic needs to be:

* controlled
* monitored
* logged
* routed through a central point

---

## Gateway API

Kubernetes also has a standardized **Gateway API**.

It provides resources such as:

```text id="s7t8u9"
GatewayClass
     │
     ▼
  Gateway
     │
     ▼
 HTTPRoute
```

The Gateway API is separate from Istio's original `networking.istio.io/Gateway` resource, although Istio supports the Gateway API as well.

The general concept is similar:

```text
Gateway → where/how traffic enters
Route   → where traffic goes
```

---

## Gateway Architecture

A typical Istio setup can look like:

```text
                         Kubernetes Cluster
┌──────────────────────────────────────────────────┐
│                                                  │
│  External Client                                 │
│       │                                          │
│       ▼                                          │
│  Ingress Gateway                                 │
│       │                                          │
│       ▼                                          │
│  VirtualService                                  │
│       │                                          │
│       ▼                                          │
│  Kubernetes Service                              │
│       │                                          │
│       ▼                                          │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐      │
│  │   Pod   │    │   Pod   │    │   Pod   │      │
│  └─────────┘    └─────────┘    └─────────┘      │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## Key Takeaways

1. A **Gateway controls network entry and exit**.
2. An Istio Gateway defines accepted **ports, protocols, hosts, and TLS settings**.
3. A Gateway resource is configuration; the **Gateway workload processes the traffic**.
4. A **VirtualService defines routing rules**.
5. A Kubernetes **Service provides stable access to Pods**.
6. An **Ingress Gateway** handles incoming traffic.
7. An **Egress Gateway** handles outgoing traffic.
8. Istio Gateways and the Kubernetes **Gateway API** are related concepts but different APIs.
