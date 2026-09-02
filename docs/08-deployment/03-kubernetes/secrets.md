# Kubernetes Secrets

## TL;DR (30 seconds)

A **Secret** is a Kubernetes resource for storing **sensitive configuration data**, such as passwords, API keys, tokens, and certificates.

The key idea:

> Secrets separate sensitive configuration from the application and container image.

---

## What is a Secret?

A Secret stores sensitive data as key-value pairs:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
stringData:
  DATABASE_USER: myuser
  DATABASE_PASSWORD: mypassword
```

Kubernetes stores the values as Secret data rather than directly in a Pod definition.

---

## Secret vs. ConfigMap

Secrets and ConfigMaps work similarly, but they serve different purposes:

|                             | ConfigMap | Secret |
| --------------------------- | --------- | ------ |
| Non-sensitive configuration | ✅         | 🟡     |
| Passwords                   | ❌         | ✅      |
| API keys                    | ❌         | ✅      |
| Tokens                      | ❌         | ✅      |
| URLs                        | ✅         | 🟡     |
| Log levels                  | ✅         | ❌      |

For example:

```text
ConfigMap
├── LOG_LEVEL=info
├── APP_ENV=production
└── API_URL=...

Secret
├── DATABASE_PASSWORD=...
├── API_KEY=...
└── ACCESS_TOKEN=...
```

---

## Using a Secret as an Environment Variable

A specific value can be injected into a container:

```yaml
containers:
  - name: app
    image: my-app:1.0
    env:
      - name: DATABASE_PASSWORD
        valueFrom:
          secretKeyRef:
            name: app-secret
            key: DATABASE_PASSWORD
```

Inside the container:

```text
DATABASE_PASSWORD=mypassword
```

The application can access it like any other environment variable.

---

## Using an Entire Secret

All keys can be exposed as environment variables:

```yaml
containers:
  - name: app
    image: my-app:1.0
    envFrom:
      - secretRef:
          name: app-secret
```

For example:

```text
DATABASE_USER=myuser
DATABASE_PASSWORD=mypassword
```

---

## Mounting a Secret as a File

Secrets can also be mounted as volumes.

```yaml
volumes:
  - name: credentials
    secret:
      secretName: app-secret
```

```yaml
volumeMounts:
  - name: credentials
    mountPath: /etc/credentials
    readOnly: true
```

The container can then access files such as:

```text
/etc/credentials/DATABASE_USER
/etc/credentials/DATABASE_PASSWORD
```

---

## `data` vs. `stringData`

Secrets support two common ways of specifying values.

### `stringData`

Values can be written directly as strings:

```yaml
stringData:
  API_KEY: my-secret-key
```

Kubernetes handles the encoding.

### `data`

Values under `data` must be **Base64-encoded**:

```yaml
data:
  API_KEY: bXktc2VjcmV0LWtleQ==
```

Important:

> Base64 is **encoding, not encryption**.

Therefore, putting a Base64-encoded password into a YAML file does **not** make the password secure.

---

## Secret Types

Kubernetes provides several Secret types.

| Type                             | Purpose                          |
| -------------------------------- | -------------------------------- |
| `Opaque`                         | Generic key-value data           |
| `kubernetes.io/tls`              | TLS certificates                 |
| `kubernetes.io/dockerconfigjson` | Container registry credentials   |
| `kubernetes.io/basic-auth`       | Basic authentication credentials |
| `kubernetes.io/ssh-auth`         | SSH credentials                  |

The most common general-purpose type is:

```yaml
type: Opaque
```

---

## Secrets and Container Images

Without Secrets:

```text
Container Image
└── Application
      └── password / API key
```

This is problematic because the credential becomes part of the image.

With a Secret:

```text
Container Image
└── Application
       ↑
       │ sensitive configuration
       │
     Secret
```

The same image can therefore be used in different environments with different credentials.

---

## Secret Lifecycle

A typical application might use:

```text
Secret
   │
   ↓
Deployment
   │
   ↓
Pod
   │
   ↓
Container
   │
   ↓
Application
```

For example:

```text
Secret
└── DATABASE_PASSWORD
          │
          ↓
      Container
          │
          ↓
      PostgreSQL
```

---

## Security Considerations

Secrets are intended to provide a controlled way to distribute sensitive data, but simply using a Kubernetes Secret does **not automatically make the data secure**.

Important considerations include:

* restrict access with **RBAC**
* avoid committing Secrets to Git
* use encryption at rest where appropriate
* avoid exposing Secret values in logs
* limit which Pods and users can access Secrets
* consider external secret-management systems for production

For example, instead of storing credentials directly in Git, systems such as **Vault** or external secret managers can be used.

---

## Creating a Secret

From literal values:

```bash
kubectl create secret generic app-secret \
  --from-literal=DATABASE_USER=myuser \
  --from-literal=DATABASE_PASSWORD=mypassword
```

From a file:

```bash
kubectl create secret generic app-secret \
  --from-file=credentials.txt
```

---

## ConfigMap + Secret

An application often needs both:

```text
              Application
              /         \
             /           \
            ↓             ↓
       ConfigMap        Secret
           │               │
     LOG_LEVEL=info    API_KEY=...
     APP_ENV=prod      PASSWORD=...
```

**ConfigMap** → configuration that is safe to treat as non-secret.

**Secret** → credentials and other sensitive values.

---

## Key Takeaways

1. **Secrets store sensitive configuration in Kubernetes.**
2. They can be provided as **environment variables or files**.
3. `stringData` accepts plain strings; `data` uses Base64 encoding.
4. **Base64 is not encryption.**
5. Use RBAC and appropriate encryption/access controls to protect Secrets.
6. Avoid storing real credentials directly in Git.
7. For more advanced setups, external secret-management systems can be used.
