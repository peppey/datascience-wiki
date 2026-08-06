# Factory Pattern

## TL;DR (30 seconds)

The **Factory Pattern** is a **creational design pattern** that separates object creation from object usage.

Instead of creating objects directly:

```python
model = RandomForestModel()
```

the client asks a factory to create the object:

```python
model = ModelFactory.create("random_forest")
```

The factory decides which concrete implementation should be created.

Main benefits:

- reduces coupling
- centralizes object creation
- makes systems easier to extend
- hides implementation details

---

## Problem

Without a factory, code directly depends on concrete classes:

```python
model = RandomForestModel()
```

The client needs to know:

- which class to instantiate
- how the object is configured
- which implementation is currently used

If the implementation changes:

```python
model = XGBoostModel()
```

every place creating the object must be updated.

---

## Idea of the Factory Pattern

The factory introduces an abstraction layer:

```
        Client
          |
          ▼
       Factory
          |
 ┌────────┼────────┐
 ▼        ▼        ▼
Class A  Class B  Class C
```

The client only interacts with the factory.

The factory handles:

- object selection
- initialization
- configuration
- creation logic

---

## Example: Machine Learning Model Factory

Imagine an application supporting multiple ML models:

```
              ModelFactory
                   |
     ┌─────────────┼─────────────┐
     ▼             ▼             ▼
RandomForest    XGBoost     NeuralNetwork
```

The client does not need to know the concrete classes.

---

## Implementation Example (Python)

### Base Interface

```python
from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def train(self, data):
        pass
```

---

### Concrete Implementations

```python
class RandomForestModel(Model):

    def train(self, data):
        print("Training Random Forest")


class NeuralNetworkModel(Model):

    def train(self, data):
        print("Training Neural Network")
```

---

### Factory

```python
class ModelFactory:

    @staticmethod
    def create(model_type):

        if model_type == "random_forest":
            return RandomForestModel()

        elif model_type == "neural_network":
            return NeuralNetworkModel()

        else:
            raise ValueError("Unknown model type")
```

---

### Usage

```python
model = ModelFactory.create("random_forest")

model.train(data)
```

Output:

```
Training Random Forest
```

The client never directly creates:

```python
RandomForestModel()
```

---

## Advantages

### Loose Coupling

Without a factory:

```
Client
  |
  ▼
RandomForestModel
```

The client depends on a specific implementation.

With a factory:

```
Client
  |
  ▼
Model Interface
  |
  ▼
Factory
  |
  ▼
Concrete Model
```

The implementation can change without modifying the client.

---

### Easier Extension

Adding a new model:

```python
class XGBoostModel(Model):

    def train(self, data):
        print("Training XGBoost")
```

Only the factory needs to change:

```python
elif model_type == "xgboost":
    return XGBoostModel()
```

Existing client code stays unchanged.

---

### Centralized Creation Logic

Complex initialization can be hidden:

```python
class ModelFactory:

    @staticmethod
    def create(model_type):

        if model_type == "production":
            return NeuralNetworkModel(
                layers=20,
                dropout=0.2
            )
```

The client does not need to know configuration details.

---

## Applications in Machine Learning

Factories are common when many interchangeable components exist.

---

## Model Factory

```
ModelFactory
      |
      ├── LogisticRegression
      ├── RandomForest
      ├── XGBoost
      └── NeuralNetwork
```

Example:

```python
model = ModelFactory.create("xgboost")
```

---

### Data Loader Factory

```
DataLoaderFactory
        |
 ┌──────┼────────┐
 ▼      ▼        ▼
 CSV   SQL    Parquet
```

Example:

```python
loader = DataLoaderFactory.create("sql")

data = loader.load()
```

---

### Database Factory

```
DatabaseFactory
        |
 ┌──────┼────────┐
 ▼      ▼        ▼
Postgres MySQL MongoDB
```

---

## Factory Pattern Variants

### Simple Factory

The **Simple Factory** is the simplest form of the Factory Pattern.

A single factory class or function is responsible for deciding which object should be created.

The client does not directly instantiate concrete classes.

---

#### Structure

```
        Client
          |
          ▼
   Simple Factory
          |
   ┌──────┼──────┐
   ▼      ▼      ▼
Class A Class B Class C
```

The factory contains the creation logic.

---

#### Example

Without a factory:

```python
model = RandomForestModel()
```

The client is directly coupled to the implementation.

With a simple factory:

```python
model = ModelFactory.create("random_forest")
```

The factory decides which class is needed.

---

#### Base Interface

```python
from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def train(self, data):
        pass
```

---

#### Concrete Classes

```python
class RandomForestModel(Model):

    def train(self, data):
        print("Training Random Forest")


class NeuralNetworkModel(Model):

    def train(self, data):
        print("Training Neural Network")
```

---

#### Simple Factory

```python
class ModelFactory:

    @staticmethod
    def create(model_type):

        if model_type == "random_forest":
            return RandomForestModel()

        elif model_type == "neural_network":
            return NeuralNetworkModel()

        else:
            raise ValueError(
                "Unknown model type"
            )
```

---

#### Usage

```python
model = ModelFactory.create("neural_network")

model.train(data)
```

Output:

```
Training Neural Network
```

The client does not need to know:

- which class is instantiated
- how the object is configured
- how the object is initialized

---

## Factory Method

The **Factory Method** is a more flexible version of the Factory Pattern.

Instead of one factory deciding everything, subclasses decide which object should be created.

The creation process is delegated to subclasses.

---

### Structure

```
              Creator
                 |
          create_object()
                 |
       ┌─────────┴─────────┐
       ▼                   ▼
RandomForestCreator   NeuralNetworkCreator
       |                   |
       ▼                   ▼
RandomForestModel    NeuralNetworkModel
```

---

### Example

#### Abstract Creator

```python
from abc import ABC, abstractmethod


class ModelCreator(ABC):

    @abstractmethod
    def create_model(self):
        pass
```

---

#### Concrete Creators

```python
class RandomForestCreator(ModelCreator):

    def create_model(self):
        return RandomForestModel()


class NeuralNetworkCreator(ModelCreator):

    def create_model(self):
        return NeuralNetworkModel()
```

---

#### Usage

```python
creator = NeuralNetworkCreator()

model = creator.create_model()

model.train(data)
```

The creator controls the object creation.

---

## Simple Factory vs Factory Method

| | Simple Factory | Factory Method |
|---|---|---|
| Creation logic | One factory class | Distributed across subclasses |
| Flexibility | Lower | Higher |
| Complexity | Simple | More complex |
| Extension | Modify factory | Add new creator subclass |
| Pattern type | Common programming technique | Official GoF design pattern |

---

## Factory Pattern vs Dependency Injection

Both reduce coupling, but they solve different problems.

---

### Factory

The client asks for an object:

```python
model = ModelFactory.create("xgboost")
```

The factory creates the object.

```
Client
  |
  ▼
Factory
  |
  ▼
Object
```

---

### Dependency Injection

The object is provided from outside:

```python
def train(model):

    model.fit(data)
```

The client does not create anything.

```
External Container
        |
        ▼
      Client
        |
        ▼
      Object
```

---

## When to Use the Factory Pattern

Use a factory when:

- many related object types exist
- object creation is complex
- implementations may change
- configuration determines the object type
- you want to avoid repeated creation logic

Examples:

- machine learning models
- database connections
- API clients
- data loaders
- serializers

---

## When Not to Use It

Avoid factories for very simple objects.

Example:

```python
user = User()
```

Replacing it with:

```python
user = UserFactory.create()
```

does not provide meaningful benefits.

A factory should solve a real design problem, not just add another abstraction layer.

---

## Summary

| Concept | Purpose |
|---|---|
| Simple Factory | Centralize object creation |
| Factory Method | Delegate creation to subclasses |
| Category | Creational design pattern |
| Main benefit | Reduce coupling |
| Client knows | Interface |
| Client does not know | Concrete implementation |

The Factory Pattern separates **how an object is created** from **how it is used**, making software systems easier to maintain, test, and extend.