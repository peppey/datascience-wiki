# FastAPI

## TL;DR (30 seconds)

**FastAPI** is a modern Python framework for building **web APIs**.

It uses Python **type hints** to provide:

* request validation
* response validation
* automatic OpenAPI documentation
* high-performance HTTP handling
* dependency injection

FastAPI is particularly common for **ML model APIs**, where a trained model is loaded by a Python service and exposed through an HTTP endpoint.

```text id="f4m8qa"
Client
   │
   │ HTTP Request
   ▼
FastAPI
   │
   ├── Validation
   │
   ▼
ML Model
   │
   ▼
Prediction
   │
   ▼
HTTP Response
```

---

## 1. Creating an API

A minimal FastAPI application looks like this:

```python id="k7p3nc"
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
```

The `@app.get("/")` decorator defines an API endpoint.

The application can then be started with an ASGI server such as Uvicorn:

```bash id="v2m8qx"
uvicorn main:app --reload
```

The API is now available at:

```text id="a6r9kp"
http://localhost:8000
```

---

## 2. Routes and HTTP Methods

FastAPI supports the standard HTTP methods:

```python id="p4n8wm"
@app.get("/models")
def get_models():
    ...

@app.post("/predict")
def predict():
    ...

@app.put("/models/{model_id}")
def update_model(model_id: int):
    ...

@app.delete("/models/{model_id}")
def delete_model(model_id: int):
    ...
```

The route and HTTP method together define an **endpoint**.

```text id="q5c2vb"
POST /predict
     │
     └── Endpoint
```

---

## 3. Path Parameters

Values can be included directly in the URL path:

```python id="m8x3qa"
@app.get("/models/{model_id}")
def get_model(model_id: int):
    return {"model_id": model_id}
```

A request such as:

```text id="r7k4np"
/models/42
```

passes `42` to the `model_id` parameter.

FastAPI uses the type annotation `int` to validate the parameter.

---

## 4. Query Parameters

Query parameters are specified after `?` in the URL.

```python id="c3w9fk"
@app.get("/models")
def get_models(limit: int = 10):
    return {"limit": limit}
```

A request could look like:

```text id="b6m2qx"
/models?limit=20
```

FastAPI parses and validates the parameter automatically.

---

## 5. Request Bodies with Pydantic

For structured request data, FastAPI commonly uses **Pydantic models**.

```python id="n4r8tp"
from pydantic import BaseModel

class PredictionRequest(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(request: PredictionRequest):
    return {"features": request.features}
```

A client can send:

```json id="x5q7mc"
{
    "features": [1.2, 3.4, 5.6]
}
```

FastAPI passes the validated request to the endpoint.

```text id="w8n3ka"
JSON Request
     │
     ▼
FastAPI
     │
     ▼
Pydantic validation
     │
     ▼
PredictionRequest
     │
     ▼
Endpoint
```

---

## 6. Response Models

Response data can also be validated using Pydantic.

```python id="j2v6rp"
class PredictionResponse(BaseModel):
    prediction: float

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    return {"prediction": 0.82}
```

The response is therefore explicitly defined by a schema.

This also allows FastAPI to include the response structure in the generated OpenAPI specification.

---

## 7. Automatic API Documentation

FastAPI automatically generates an **OpenAPI specification** from the Python code.

It also provides interactive documentation.

By default:

```text id="z4m8vc"
/docs
```

opens **Swagger UI**.

FastAPI also provides:

```text id="q7n3ka"
/redoc
```

for **ReDoc**.

The relationship is:

```text id="s6p2mx"
FastAPI Application
        │
        ▼
OpenAPI Specification
        │
   ┌────┴────┐
   ▼         ▼
Swagger UI  ReDoc
```

---

## 8. ML Model Serving

FastAPI can be used to expose a trained ML model as an API.

For example, a model stored as a `joblib` file can be loaded when the application starts:

```python id="d9k4rw"
import joblib
from fastapi import FastAPI

app = FastAPI()

model = joblib.load("model.joblib")

@app.post("/predict")
def predict(features: list[float]):
    prediction = model.predict([features])
    return {"prediction": prediction.tolist()}
```

The resulting architecture is:

```text id="h3q8vn"
Client
   │
   │ POST /predict
   ▼
FastAPI
   │
   ▼
Validation
   │
   ▼
ML Model
   │
   ▼
Prediction
```

This is a simple example of **deploying a model as an API**.

---

## 9. Dependency Injection

FastAPI provides a dependency injection system.

Dependencies are useful for functionality that should be shared between endpoints, such as:

* authentication
* database connections
* configuration
* reusable validation
* shared services

Example:

```python id="t5w8mq"
from fastapi import Depends, FastAPI

app = FastAPI()

def get_model():
    return model

@app.post("/predict")
def predict(
    features: list[float],
    model=Depends(get_model)
):
    return {"prediction": model.predict([features]).tolist()}
```

FastAPI calls the dependency and provides its result to the endpoint.

---

## 10. Middleware

**Middleware** processes HTTP requests and responses before or after they reach an endpoint.

```text id="k8v4qa"
Request
   │
   ▼
Middleware
   │
   ▼
Endpoint
   │
   ▼
Middleware
   │
   ▼
Response
```

Middleware can be used for things such as:

* CORS
* logging
* request timing
* authentication
* adding response headers

---

## 11. Error Handling

FastAPI provides HTTP exceptions for returning appropriate error responses.

```python id="p6r2xc"
from fastapi import HTTPException

@app.get("/models/{model_id}")
def get_model(model_id: int):
    if model_id not in models:
        raise HTTPException(
            status_code=404,
            detail="Model not found"
        )

    return models[model_id]
```

The client receives an HTTP `404` response.

---

## 12. Async Endpoints

FastAPI supports both regular and asynchronous endpoints.

```python id="n9w3kb"
@app.get("/data")
async def get_data():
    result = await fetch_data()
    return result
```

`async`/`await` is particularly useful for **I/O-bound operations**, such as:

* database queries
* HTTP requests
* network operations
* file operations

It does not automatically make CPU-heavy ML inference faster.

---

## 13. FastAPI vs. Uvicorn

These are different components:

```text id="r4m7xp"
FastAPI
   │
   │ defines the API
   ▼
Uvicorn
   │
   │ runs the application
   ▼
HTTP Server
```

**FastAPI** is the web framework.

**Uvicorn** is an **ASGI server** that runs the FastAPI application.

For example:

```bash id="c8q2vn"
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 14. FastAPI in Kubernetes

A FastAPI application can be packaged into a Docker container and deployed to Kubernetes.

```text id="m3x7qa"
FastAPI Application
        │
        ▼
    Docker Image
        │
        ▼
 Kubernetes Deployment
        │
        ▼
       Pod
        │
        ▼
     Service
        │
        ▼
   Ingress / Route
```

This makes FastAPI suitable for building custom model-serving services when a framework such as KServe is not required.

---

## 15. FastAPI vs. KServe

FastAPI and KServe solve related but different problems.

|                          | FastAPI              | KServe                        |
| ------------------------ | -------------------- | ----------------------------- |
| Main purpose             | Build web APIs       | Model serving on Kubernetes   |
| Abstraction              | Web framework        | ML serving platform           |
| Model server             | You implement it     | Provided/configured by KServe |
| API endpoint             | You define it        | KServe manages it             |
| Kubernetes integration   | Manual               | Native                        |
| Autoscaling              | Configure separately | Built-in serving features     |
| Custom application logic | Very flexible        | More opinionated              |

For a simple custom ML service:

```text id="v5k8rm"
FastAPI
   │
   └── Your inference code
```

For Kubernetes-native model serving:

```text id="x3n7qa"
KServe
   │
   └── InferenceService
          │
          └── Model Server
```

FastAPI can also be used **inside a custom KServe model server or transformer** when custom Python logic is required.

---

## Key Takeaways

1. **FastAPI** is a Python framework for building HTTP APIs.
2. It uses **Python type hints and Pydantic** for validation.
3. It automatically generates an **OpenAPI specification**.
4. **Swagger UI** is available automatically through `/docs`.
5. FastAPI is well suited for exposing **ML models through API endpoints**.
6. **Uvicorn** is commonly used to run FastAPI applications.
7. FastAPI can be containerized and deployed on **Kubernetes/OpenShift**.
8. FastAPI is a web framework, while **KServe is an ML serving platform**.
