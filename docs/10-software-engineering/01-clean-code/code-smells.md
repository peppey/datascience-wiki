# Code Smells

## TL;DR

A **code smell** is a pattern in source code that indicates a potential problem with **maintainability, readability, or design**.

A code smell is not necessarily a bug. It is a warning sign that the code may be unnecessarily complex or difficult to change.

---

## Common Code Smells

### Long Method

A method contains too much logic and performs many different tasks.

```python
def process_order(order):
    # validation
    # calculation
    # database access
    # email sending
    # logging
```

Large methods are often difficult to understand and test.

**Refactoring:** Split the method into smaller functions with clear responsibilities.

---

### Large Class

A class contains too many responsibilities.

```text
UserManager
├── Authentication
├── Database Access
├── Email Sending
├── Logging
└── Report Generation
```

This often violates the **Single Responsibility Principle**.

**Refactoring:** Split the class into smaller, focused classes.

---

### Duplicated Code

The same or very similar code appears in multiple places.

```python
if user.is_active:
    calculate_price()

# ...

if user.is_active:
    calculate_price()
```

Duplicated code makes maintenance harder because changes have to be made in multiple places.

**Refactoring:** Extract shared logic into a function or class.

---

### Long Parameter List

A function requires many parameters:

```python
create_user(
    name,
    email,
    age,
    address,
    city,
    country,
    phone,
    role
)
```

Long parameter lists make functions harder to understand and use.

**Refactoring:** Group related parameters into an object or data structure.

---

### Deeply Nested Code

Many nested conditions make control flow difficult to follow:

```python
if user:
    if user.is_active:
        if user.has_permission:
            if request.is_valid:
                process(request)
```

**Refactoring:** Use guard clauses or extract logic into separate functions.

---

### Magic Numbers

Unexplained numbers appear directly in the code:

```python
if age > 18:
    ...
```

The meaning of `18` may not be obvious.

Instead:

```python
MINIMUM_AGE = 18

if age > MINIMUM_AGE:
    ...
```

---

### God Object

A **God Object** knows or does almost everything in an application.

```text
ApplicationManager
├── Users
├── Orders
├── Payments
├── Database
├── Authentication
├── Logging
└── Reports
```

This creates strong coupling and makes the system difficult to maintain.

**Refactoring:** Divide responsibilities among smaller components.

---

### Dead Code

Code that is never executed or used remains in the codebase.

```python
def old_algorithm():
    ...
```

Dead code increases complexity and can confuse developers.

**Refactoring:** Remove unused code, preferably using version control to preserve its history.

---

### Excessive Comments

Comments are sometimes used to explain code that is unnecessarily complicated:

```python
# Check if x is greater than zero
if x > 0:
    ...
```

Good code should be understandable through meaningful names and simple structure.

Comments are most useful for explaining **why** something is done rather than **what** the code does.

---

### Inconsistent Naming

Different naming conventions make code harder to understand.

```python
user_name
UserName
username
usr
```

A consistent naming convention improves readability.

---

### Feature Envy

A method frequently accesses data from another class instead of its own data.

```text
Class A
   │
   └── constantly accesses → Class B
```

This can indicate that some behavior belongs in the other class.

---

### Shotgun Surgery

A small change requires modifications in many different parts of the codebase.

```text
One Change
    │
    ├── File A
    ├── File B
    ├── File C
    ├── File D
    └── File E
```

This often indicates that related responsibilities are spread across too many components.

---

## Code Smells vs. Bugs

A **bug** means that the software behaves incorrectly.

A **code smell** indicates that the code structure may cause problems or make future changes harder.

```text
Bug
└── Incorrect behavior

Code Smell
└── Potential design or maintainability problem
```

A code smell can exist even when the program currently works correctly.

---

## Code Smells and SonarQube

Tools such as **SonarQube** automatically detect many common code smells.

```text
Source Code
     │
     ▼
SonarQube
     │
     ├── Bugs
     ├── Vulnerabilities
     └── Code Smells
             │
             ▼
        Refactoring
```

This allows code quality problems to be detected automatically during CI/CD.

---

## Key Idea

Code smells are **warning signs in source code**, not necessarily errors.

Common examples include:

```text
Long Methods
Large Classes
Duplicated Code
Long Parameter Lists
Deep Nesting
Magic Numbers
God Objects
Dead Code
Inconsistent Naming
Feature Envy
Shotgun Surgery
```

The goal of identifying code smells is to recognize code that can be **simplified, refactored, and made easier to maintain**.
