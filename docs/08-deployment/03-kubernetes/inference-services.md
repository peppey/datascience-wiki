# KServe InferenceService

## TL;DR (30 seconds)

An **InferenceService** is a KServe custom resource for deploying and exposing a **machine learning model for inference on Kubernetes**.

The key idea:

> An InferenceService describes **which model should be served and how it should be exposed**. KServe handles the underlying Kubernetes resources needed to run it.

---

## What is an InferenceService?

An InferenceService is a Kubernetes custom resource provided by **KServe**.

Instead of manually creating Deployments, Services, Pods, and networking configuration for a model, you can describe the desired model-serving setup:

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

KServe uses this specification to create and manage the required resources.

---

## Basic Architecture

A simplified setup looks like:

```text
InferenceService
       │
       ▼
   Predictor
       │
       ▼
      Pod
       │
       ├── Model Server
       │
       └── Model
```

The **InferenceService** is the high-level resource.

The **Predictor** contains the actual model-serving component.

---

## Predictor

The `predictor` defines how the model should be served.

For example:

```yaml
spec:
  predictor:
    model:
      modelFormat:
        name: sklearn
      storageUri: s3://models/my-model
```

The predictor is responsible for:

* loading the model
* running inference
* exposing the inference endpoint
* handling inference requests

KServe supports different model serving runtimes, such as:

* scikit-learn
* XGBoost
* TensorFlow
* PyTorch
* ONNX
* custom model servers

---

## Model Storage

The model can be loaded from external storage:

```yaml
storageUri: s3://models/my-model
```

Common storage locations include:

```text
S3
GCS
Azure Blob Storage
Persistent Volumes
```

KServe downloads or mounts the model so that the serving container can load it.

For example:

```text
S3
 │
 │ model files
 ▼
KServe
 │
 ▼
Inference Pod
 │
 └── Model Server
```

---

## Inference Endpoint

Once deployed, the InferenceService provides an endpoint through which clients can send prediction requests.

Conceptually:

```text
Client
   │
   │ HTTP request
   ▼
InferenceService
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

The exact externally reachable URL depends on the Kubernetes/KServe networking configuration.

---

## Transformer

KServe can optionally use a **Transformer** before and/or after the model server.

```text
Client
   │
   ▼
Transformer
   │
   │ preprocessing
   ▼
Model Server
   │
   │ prediction
   ▼
Transformer
   │
   │ postprocessing
   ▼
Client
```

A Transformer is useful when the API input does not directly match the format expected by the model.

For example:

```text
JSON request
     ↓
Transformer
     ↓
feature extraction
     ↓
Model
     ↓
prediction
     ↓
Transformer
     ↓
JSON response
```

A Transformer can be implemented as a custom container.

---

## InferenceService with Transformer

A simplified configuration can contain both:

```yaml
spec:
  predictor:
    containers:
      - name: kserve-container
        image: my-model-server:latest

  transformer:
    containers:
      - name: transformer-container
        image: my-transformer:latest
```

The two components have different responsibilities:

| Component   | Responsibility                 |
| ----------- | ------------------------------ |
| Transformer | preprocessing / postprocessing |
| Predictor   | model inference                |

---

## InferenceService and Kubernetes

An InferenceService is **not itself a Pod**.

It is a Kubernetes **Custom Resource**:

```text
InferenceService
       │
       ▼
KServe Controller
       │
       ├── Kubernetes resources
       │
       ├── Predictor
       │
       ├── Service
       │
       └── Networking
              │
              ▼
            Pods
```

The KServe controller watches the InferenceService and creates or updates the underlying resources.

---

## InferenceService vs. Deployment

A Deployment is a generic Kubernetes resource for running replicated Pods.

An InferenceService is specifically designed for **model serving**.

|                     | Deployment           | InferenceService  |
| ------------------- | -------------------- | ----------------- |
| Purpose             | General applications | ML inference      |
| Kubernetes resource | Built-in             | KServe CRD        |
| Model serving       | Manual               | Built-in concepts |
| Model storage       | Manual               | Supported         |
| Predictor           | ❌                    | ✅                 |
| Transformer         | ❌                    | ✅                 |
| Inference endpoint  | Manual configuration | KServe-managed    |

You can think of an InferenceService as a **higher-level abstraction for deploying ML models**.

---

## Status

KServe exposes status information for an InferenceService.

For example:

```yaml
status:
  conditions:
    - type: IngressReady
      status: "True"

    - type: PredictorReady
      status: "True"
```

Common conditions indicate whether components such as the predictor or ingress are ready.

This makes it possible to determine whether the model is actually ready to receive inference requests.

---

## Example

A simple scikit-learn model:

```yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: iris-model
spec:
  predictor:
    model:
      modelFormat:
        name: sklearn
      storageUri: s3://models/iris
```

Conceptually:

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
                    sklearn model
                           │
                           ▲
                           │
                      S3 storage
```

A client can then send an inference request to the exposed endpoint.

---

## Key Takeaways

1. **InferenceService is a KServe Custom Resource for ML model serving.**
2. It describes the desired state of a model deployment.
3. The **Predictor** performs model inference.
4. Models can be loaded from external storage such as S3.
5. A **Transformer** can perform preprocessing and postprocessing.
6. KServe creates and manages the underlying Kubernetes resources.
7. The InferenceService provides a model-serving endpoint.
