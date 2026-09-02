# ConfigMaps

## TL;DR (30 seconds)

A **ConfigMap** is a Kubernetes resource for storing **non-sensitive configuration data** separately from an application's container image.

The key idea:

> Put configuration in Kubernetes resources instead of hardcoding it into the application or container image.

---

## What is a ConfigMap?

A ConfigMap stores configuration as **key-value pairs**:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_ENV: production
  LOG_LEVEL: info
  API_URL: https://api.example.com
```

The application can then access these values from a Pod.

---

## Using a ConfigMap as Environment Variables

A ConfigMap can provide environment variables to a container:

```yaml
containers:
  - name: app
    image: my-app:1.0
    env:
      - name: APP_ENV
        valueFrom:
          configMapKeyRef:
            name: app-config
            key: APP_ENV
```

The container receives:

```text
APP_ENV=production
```

---

## Using an Entire ConfigMap

All entries can also be exposed as environment variables:

```yaml
containers:
  - name: app
    image: my-app:1.0
    envFrom:
      - configMapRef:
          name: app-config
```

For the previous ConfigMap:

```text
APP_ENV=production
LOG_LEVEL=info
API_URL=https://api.example.com
```

---

## Using a ConfigMap as a File

A ConfigMap can also be mounted as a volume.

For example:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  config.yaml: |
    log_level: info
    environment: production
```

The ConfigMap can be mounted into a container:

```yaml
volumeMounts:
  - name: config
    mountPath: /etc/app

volumes:
  - name: config
    configMap:
      name: app-config
```

The application then sees:

```text
/etc/app/config.yaml
```

with the contents stored in the ConfigMap.

---

## ConfigMap vs. Secret

ConfigMaps are intended for **non-sensitive configuration**.

|                        | ConfigMap | Secret |
| ---------------------- | --------- | ------ |
| Configuration          | ✅         | ✅      |
| Passwords              | ❌         | ✅      |
| API keys               | ❌         | ✅      |
| URLs                   | ✅         | 🟡     |
| Log levels             | ✅         | ❌      |
| Non-sensitive settings | ✅         | ❌      |

For example:

```text
ConfigMap
├── LOG_LEVEL=info
├── APP_ENV=production
└── API_URL=...

Secret
├── DATABASE_PASSWORD=...
└── API_KEY=...
```

A ConfigMap should **not** be used as a replacement for a Secret when data is sensitive.

---

## ConfigMap and Container Images

Without a ConfigMap:

```text
Container Image
└── Application
      └── hardcoded configuration
```

With a ConfigMap:

```text
Container Image
└── Application
       ↑
       │ configuration
       │
   ConfigMap
```

This allows the same image to be deployed in different environments:

```text
             same image
                 │
        ┌────────┼────────┐
        ↓        ↓        ↓
    Development Staging Production
      ConfigMap ConfigMap ConfigMap
```

The application image does not need to change between environments.

---

## Updating a ConfigMap

A ConfigMap can be updated independently of the application image:

```bash
kubectl edit configmap app-config
```

However, the behavior depends on how the ConfigMap is consumed.

* **Environment variables:** existing Pods do not automatically receive the new values.
* **Mounted files:** Kubernetes can update the mounted data eventually.
* Applications may still need to reload the configuration.

In practice, deployments often trigger a **Pod restart/rollout** when configuration changes.

---

## Creating a ConfigMap

From literal values:

```bash
kubectl create configmap app-config \
  --from-literal=LOG_LEVEL=info \
  --from-literal=APP_ENV=production
```

From a file:

```bash
kubectl create configmap app-config \
  --from-file=config.yaml
```

Or declaratively using a Kubernetes manifest.

---

## ConfigMap in a Deployment

A common pattern is:

```text
Deployment
    │
    └── Pod
         │
         └── Container
              ↑
              │
         ConfigMap
```

The Deployment defines the Pod, while the ConfigMap provides configuration to the container.

---

## Key Takeaways

1. **ConfigMaps store non-sensitive configuration.**
2. They separate configuration from container images.
3. Values can be exposed as **environment variables**.
4. Configuration can also be mounted as **files**.
5. Use **Secrets** for sensitive information such as passwords and API keys.
6. ConfigMaps make it easier to use the same container image across different environments.
