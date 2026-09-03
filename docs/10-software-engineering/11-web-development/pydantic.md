# Pydantic

## TL;DR (30 seconds)

**Pydantic** is a Python library for **data validation and serialization based on type hints**.

It allows you to define the expected structure of data using Python classes:

```python id="p7m3xk"
from pydantic import BaseModel

class PredictionRequest(BaseModel):
    temperature: float
    humidity: float
```

When data is passed to the model, Pydantic validates it and can convert compatible input types automatically.

Pydantic is widely used with **FastAPI** for validating API requests and responses.

---

## Pydantic Models

A Pydantic model is a Python class that inherits from `BaseModel`.

```python id="m8x2qa"
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

The model defines the expected schema:

```text id="k4v9sc"
User
├── name: str
└── age: int
```

Creating an instance:

```python id="a2n7fw"
user = User(name="Alice", age=30)
```

The resulting object is a regular Python object with validated data.

---

## Data Validation

Pydantic checks whether the provided data conforms to the declared types.

```python id="c6r1tp"
class User(BaseModel):
    name: str
    age: int

user = User(name="Alice", age="30")
```

Pydantic can convert the string `"30"` into the integer `30` when the input is compatible.

Invalid data raises a validation error:

```python id="x9d4me"
User(name="Alice", age="hello")
```

This results in a `ValidationError`.

---

## Required and Optional Fields

Fields without a default value are required:

```python id="j3p8vn"
class User(BaseModel):
    name: str
    age: int
```

Both fields must be provided.

Optional fields can have a default value:

```python id="q5w7lz"
class User(BaseModel):
    name: str
    age: int = 0
```

Now `age` defaults to `0` if it is not provided.

A field can also explicitly allow `None`:

```python id="h2k6rd"
from typing import Optional

class User(BaseModel):
    name: str
    nickname: Optional[str] = None
```

---

## Nested Models

Pydantic models can contain other Pydantic models.

```python id="r7c3ym"
class Address(BaseModel):
    city: str
    country: str

class User(BaseModel):
    name: str
    address: Address
```

This allows complex data structures to be represented:

```text id="f8w2qa"
User
├── name
└── address
    ├── city
    └── country
```

---

## Collections

Pydantic supports common collection types:

```python id="v3n9kp"
class Prediction(BaseModel):
    probabilities: list[float]
    labels: list[str]
```

For example:

```python id="z5r1bx"
prediction = Prediction(
    probabilities=[0.1, 0.7, 0.2],
    labels=["cat", "dog", "bird"]
)
```

The declared types are validated for the collection elements as well.

---

## Field Constraints

Fields can have additional constraints.

```python id="w6k2pt"
from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    temperature: float = Field(ge=-50, le=60)
    confidence: float = Field(ge=0, le=1)
```

Here:

* `temperature` must be between `-50` and `60`
* `confidence` must be between `0` and `1`

This is useful when type information alone is not sufficient.

---

## Custom Validators

Custom validation logic can be added when more complex rules are required.

```python id="n4y8sc"
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value
```

The validator is executed when the model is created.

---

## Serialization

Pydantic models can be converted back into dictionaries:

```python id="b7m2qa"
user = User(name="Alice", age=30)

data = user.model_dump()
```

Result:

```python id="c8v4nx"
{
    "name": "Alice",
    "age": 30
}
```

They can also be serialized to JSON:

```python id="p2r6wk"
json_data = user.model_dump_json()
```

This makes Pydantic useful for processing data received from or sent to APIs.

---

## Pydantic with FastAPI

Pydantic is particularly common in **FastAPI**.

A request body can be defined using a Pydantic model:

```python id="m5x8qd"
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictionRequest(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(request: PredictionRequest):
    return {"prediction": model.predict([request.features]).tolist()}
```

The resulting flow is:

```text id="v9c3ak"
HTTP Request
     │
     ▼
FastAPI
     │
     ▼
Pydantic validation
     │
     ▼
Python object
     │
     ▼
ML model
     │
     ▼
Response
```

FastAPI also uses Pydantic models to generate parts of the API's **OpenAPI schema** and interactive documentation.

---

## Pydantic in Machine Learning

Pydantic is useful around an ML model even though it does not perform the actual inference.

For example, a model API might accept:

```python id="k6w3tp"
class PredictionRequest(BaseModel):
    age: float
    income: float
    account_balance: float
```

The ML model then receives validated data:

```text id="q8n2vr"
HTTP Request
     │
     ▼
Pydantic
     │
     │ validated data
     ▼
Preprocessing
     │
     ▼
ML Model
     │
     ▼
Prediction
```

This separates **data validation** from **model inference**.

---

## Pydantic vs. Dataclasses

Both Pydantic models and Python `dataclasses` can represent structured data.

|                    | Pydantic  | Dataclass                       |
| ------------------ | --------- | ------------------------------- |
| Type hints         | ✓         | ✓                               |
| Runtime validation | ✓         | ✗                               |
| Type conversion    | ✓         | Limited                         |
| Serialization      | ✓         | Manual / additional tools       |
| API validation     | Excellent | Not primarily designed for this |
| Standard library   | ✗         | ✓                               |

Use a **dataclass** when you mainly need a lightweight structured Python object.

Use **Pydantic** when you need **validation, parsing, serialization, or API schemas**.

---

## Pydantic v2

Pydantic v2 introduced a new validation engine and changed several APIs compared with Pydantic v1.

For example, serialization commonly uses:

```python id="r4m7xc"
model.model_dump()
model.model_dump_json()
```

rather than the older:

```python id="s8k2qn"
model.dict()
model.json()
```

When starting a new project, use the current Pydantic v2 API.

---

## Key Takeaways

1. **Pydantic** provides data validation and serialization using Python type hints.
2. Models are defined by inheriting from `BaseModel`.
3. Pydantic validates types, nested structures, collections, and custom constraints.
4. **Pydantic models** are particularly useful for defining API request and response schemas.
5. **FastAPI** uses Pydantic extensively for request validation and OpenAPI schema generation.
6. In ML applications, Pydantic is useful for validating data **before it reaches the model**.
7. Pydantic is primarily concerned with **data structures and validation**, not ML itself.
