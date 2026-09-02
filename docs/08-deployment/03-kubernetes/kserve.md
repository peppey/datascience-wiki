# KServe

## TL;DR (30 seconds)

**KServe** is a Kubernetes-based platform for **deploying and serving machine learning models**.

The key idea:

> KServe provides the infrastructure and abstractions needed to turn a trained ML model into a scalable inference service.

---

## What is KServe?

KServe extends Kubernetes with **Custom Resources** for machine learning model serving.

Instead of manually configuring all Kubernetes resources needed to serve a model, KServe provides higher-level abstractions.

```text
Trained Model
     │
     ▼
   KServe
     │
     ├── Model Serving
     ├── Scaling
     ├── Networking
     ├── Model Loading
     └── Inference
          │
          ▼
     Inference Endpoint
```

The central resource is the **InferenceService**.

---

## KServe and Kubernetes

KServe runs on top of Kubernetes:

```text
Kubernetes
│
├── Pods
├── Services
├── Deployments
└── ...
       │
       ▼
     KServe
       │
       ├── InferenceService
       ├── Predictor
       └── Transformer
```

KServe's controller watches its Custom Resources and creates or manages the required Kubernetes resources.

---

## InferenceService

The main KServe resource is an `InferenceService`.

```yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: my-model
spec:
  predictor:
    model:
      modelFormat:
        name: sklearn
      storageUri: s3://models/my-model
```

It describes the desired serving configuration for a model.

For example:

```text
InferenceService
      │
      ▼
   Predictor
      │
      ▼
 Model Server
      │
      ▼
    Model
```

See the separate **InferenceService** article for details.

---

## Model Serving

KServe supports different model frameworks and serving runtimes.

Examples include:

* scikit-learn
* XGBoost
* TensorFlow
* PyTorch
* ONNX
* custom model servers

The model can be stored externally, for example in S3:

```text
S3
 │
 │ model files
 ▼
KServe
 │
 ▼
Model Server
 │
 ▼
Inference Pod
```

---

## Predictor

The **Predictor** is the component responsible for serving the model.

It typically:

* loads the model
* receives inference requests
* executes the model
* returns predictions

Conceptually:

```text
HTTP Request
     │
     ▼
 Predictor
     │
     ▼
   Model
     │
     ▼
 Prediction
```

---

## Transformer

KServe can optionally include a **Transformer**.

A Transformer is useful for preprocessing and postprocessing.

```text
Client
  │
  ▼
Transformer
  │
  │ preprocessing
  ▼
Predictor
  │
  │ inference
  ▼
Transformer
  │
  │ postprocessing
  ▼
Client
```

For example, a Transformer might convert:

```text
Raw JSON
   ↓
Feature extraction
   ↓
Model input
```

and transform the model output back into an API response.

---

## Explainer

KServe can also provide an **Explainer** for model explainability.

Conceptually:

```text
Request
   │
   ▼
Predictor ──────► Prediction
   │
   ▼
Explainer
   │
   ▼
Explanation
```

Depending on the setup, explainability methods can be used to understand why a model produced a particular prediction.

---

## Scaling

KServe can automatically scale model-serving workloads based on demand.

Conceptually:

```text
Low traffic:

       Predictor
          │
        Pod


High traffic:

       Predictor
          │
    ┌─────┼─────┐
    ▼     ▼     ▼
   Pod   Pod   Pod
```

This allows resources to be increased when inference traffic grows.

Depending on the deployment configuration, KServe can also **scale workloads down when they are not being used**.

---

## Serverless vs. Standard Deployment

KServe supports different deployment modes.

A deployment can use a serverless architecture based on components such as **Knative**, or a more traditional Kubernetes deployment.

Conceptually:

```text
Serverless

InferenceService
      │
      ▼
   Knative
      │
      ▼
    Pods
```

or:

```text
Standard

InferenceService
      │
      ▼
 Kubernetes resources
      │
      ▼
    Pods
```

The appropriate mode depends on the Kubernetes environment and the operational requirements.

---

## KServe Request Flow

A typical inference request can look like:

```text
                    KServe
                       │
Client
  │                    │
  │ HTTP request       │
  ▼                    ▼
Ingress / Gateway → Transformer
                         │
                         ▼
                      Predictor
                         │
                         ▼
                       Model
                         │
                         ▼
                     Prediction
                         │
                         ▼
                       Client
```

The exact networking components depend on the Kubernetes and KServe configuration.

---

## KServe on OpenShift

KServe can also be used on **OpenShift**.

A typical setup might look like:

```text
OpenShift
│
├── KServe
│    │
│    └── InferenceService
│           │
│           ├── Predictor
│           │     └── Model Server
│           │
│           └── Transformer
│
├── Services
├── Routes / Ingress
└── Pods
```

The external endpoint is provided through the networking configuration of the cluster.

---

## KServe vs. Kubernetes Deployment

A Kubernetes Deployment is a general-purpose mechanism for running containers.

KServe provides ML-specific abstractions on top of Kubernetes.

|                      | Kubernetes Deployment | KServe    |
| -------------------- | --------------------- | --------- |
| General applications | ✅                     | 🟡        |
| ML model serving     | Manual                | ✅         |
| Model storage        | Manual                | Supported |
| Predictor            | ❌                     | ✅         |
| Transformer          | ❌                     | ✅         |
| Explainer            | ❌                     | ✅         |
| ML-specific serving  | ❌                     | ✅         |
| Autoscaling          | Kubernetes-based      | Supported |

KServe is therefore especially useful when **model serving is the main purpose of the workload**.

---

## KServe Architecture

A simplified architecture:

```text
                   KServe
                      │
             ┌────────┼────────┐
             │        │        │
             ▼        ▼        ▼
         Predictor Transformer Explainer
             │        │
             ▼        ▼
          Model    Pre/Postprocessing
             │
             ▼
       Inference Endpoint
```

KServe integrates these components with Kubernetes infrastructure for networking, scaling, and resource management.

---

## Key Takeaways

1. **KServe is a Kubernetes-based model-serving platform.**
2. It provides ML-specific abstractions on top of Kubernetes.
3. The central resource is the **InferenceService**.
4. The **Predictor** serves the model.
5. A **Transformer** handles preprocessing and postprocessing.
6. An **Explainer** can provide model explanations.
7. KServe supports model storage, inference endpoints, and scaling.
8. It can be used with Kubernetes-based platforms such as **OpenShift**.
