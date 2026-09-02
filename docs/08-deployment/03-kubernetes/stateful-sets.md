# StatefulSets

## TL;DR (30 seconds)

A **StatefulSet** is a Kubernetes resource for managing **stateful applications** that need stable identities, persistent storage, or ordered operations.

The key idea:

> A Deployment manages interchangeable Pods, while a StatefulSet gives each Pod a **stable identity and persistent state**.

---

## StatefulSet vs. Deployment

|              | Deployment                              | StatefulSet                    |
| ------------ | --------------------------------------- | ------------------------------ |
| Pod identity | interchangeable                         | stable                         |
| Pod names    | random/generated                        | predictable                    |
| Storage      | usually ephemeral or separately managed | persistent per Pod             |
| Ordering     | generally irrelevant                    | can be controlled              |
| Typical use  | stateless APIs, web apps                | databases, distributed systems |

For example:

```text
Deployment:

my-app-7d8f9c-x1a2
my-app-7d8f9c-b3c4
my-app-7d8f9c-d5e6

StatefulSet:

database-0
database-1
database-2
```

The StatefulSet Pods keep their identities even when they are recreated.

---

## Stable Pod Identity

StatefulSet Pods receive predictable names based on their ordinal index:

```text
database-0
database-1
database-2
```

If `database-1` is deleted, Kubernetes recreates:

```text
database-1
```

rather than creating a completely new identity.

This is important for distributed applications where instances may need to know **which instance they are communicating with**.

---

## Persistent Storage

StatefulSets are commonly used together with **PersistentVolumeClaims (PVCs)**.

A StatefulSet can define a `volumeClaimTemplates`:

```yaml
volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 10Gi
```

For three replicas, Kubernetes creates separate storage:

```text
database-0 → data-database-0
database-1 → data-database-1
database-2 → data-database-2
```

The storage belongs to the Pod's identity rather than to an arbitrary Pod instance.

---

## Headless Services

StatefulSets are often used with a **headless Service**:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: database
spec:
  clusterIP: None
```

This allows Kubernetes DNS to provide stable addresses such as:

```text
database-0.database
database-1.database
database-2.database
```

This is useful when applications need to communicate with **specific instances** rather than simply sending traffic to any available Pod.

---

## Scaling

If a StatefulSet is scaled from 2 to 3 replicas:

```text
database-0
database-1
database-2  ← new
```

The ordinal numbering remains stable.

When scaling down, higher-numbered Pods are removed first:

```text
database-0
database-1
database-2
database-3

        ↓ scale to 2

database-0
database-1
```

---

## Ordered Operations

StatefulSets can control the order in which Pods are created and terminated.

With the default `OrderedReady` policy:

```text
create database-0
        ↓
database-0 ready
        ↓
create database-1
        ↓
database-1 ready
        ↓
create database-2
```

This can be important for distributed systems that require instances to start in a specific order.

With `podManagementPolicy: Parallel`, Pods can instead be created in parallel.

---

## Updating a StatefulSet

StatefulSets support rolling updates.

For example:

```text
database-2
    ↓
database-1
    ↓
database-0
```

The exact update order can be controlled using `podManagementPolicy` and `updateStrategy`.

The default update strategy is:

```yaml
updateStrategy:
  type: RollingUpdate
```

---

## Typical Use Cases

StatefulSets are useful for applications such as:

* databases
* Kafka
* ZooKeeper
* Elasticsearch
* distributed storage systems
* clustered applications requiring stable identities

They are generally **not necessary for ordinary stateless web applications**.

---

## StatefulSet Structure

```text
StatefulSet
    │
    ├── Pod: database-0
    │       └── PVC: data-database-0
    │
    ├── Pod: database-1
    │       └── PVC: data-database-1
    │
    └── Pod: database-2
            └── PVC: data-database-2
```

A Service can provide stable DNS names for these Pods:

```text
database-0.database
database-1.database
database-2.database
```

---

## Minimal Example

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: database
spec:
  serviceName: database
  replicas: 3

  selector:
    matchLabels:
      app: database

  template:
    metadata:
      labels:
        app: database
    spec:
      containers:
        - name: database
          image: postgres:16

  volumeClaimTemplates:
    - metadata:
        name: data
      spec:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 10Gi
```

The important fields are:

* `serviceName` → Service used for the StatefulSet's network identity
* `replicas` → number of Pods
* `selector` → identifies the Pods managed by the StatefulSet
* `template` → defines the Pod
* `volumeClaimTemplates` → creates persistent storage for each Pod

---

## Key Takeaways

1. **StatefulSets are for stateful applications.**
2. Each Pod gets a **stable, predictable identity**.
3. Pods can have **individual persistent storage**.
4. Pods can be created, updated, and terminated in a controlled order.
5. StatefulSets are often combined with **headless Services**.
6. For ordinary stateless applications, a **Deployment** is usually the better choice.
