# SOLID Principles

## TL;DR

The **SOLID principles** are five principles for designing maintainable and extensible object-oriented software.

```text
S — Single Responsibility Principle
O — Open/Closed Principle
L — Liskov Substitution Principle
I — Interface Segregation Principle
D — Dependency Inversion Principle
```

They help reduce coupling and make software easier to change.

---

## Single Responsibility Principle

**A class should have one responsibility and one reason to change.**

Instead of:

```text
UserService
├── Authentication
├── Database Access
├── Email Sending
└── PDF Generation
```

separate the responsibilities:

```text
AuthenticationService
UserRepository
EmailService
PdfGenerator
```

This makes individual components easier to understand, test, and modify.

---

## Open/Closed Principle

**Software entities should be open for extension but closed for modification.**

Instead of repeatedly modifying existing code when adding new behavior, use abstractions that allow new implementations.

```text
PaymentProcessor
      │
      ├── CreditCardPayment
      ├── PayPalPayment
      └── BankTransfer
```

Adding a new payment method should ideally require adding a new implementation rather than changing existing payment logic.

---

## Liskov Substitution Principle

**Objects of a subclass should be usable wherever objects of the base class are expected.**

For example:

```text
        Bird
       /    \
   Sparrow  Penguin
```

If `Bird` requires every subclass to implement `fly()`, `Penguin` would violate the principle because penguins cannot fly.

A better abstraction might be:

```text
Bird
 │
 ├── Sparrow
 │      └── Flyable
 │
 └── Penguin
```

The principle is about preserving the expected behavior of an abstraction when it is replaced by one of its subtypes.

---

## Interface Segregation Principle

**Clients should not be forced to depend on methods they do not use.**

Instead of one large interface:

```text
Animal
├── eat()
├── sleep()
├── fly()
└── swim()
```

use smaller, focused interfaces:

```text
Animal
├── Eater
├── Flyer
└── Swimmer
```

A class only implements the capabilities it actually needs.

---

## Dependency Inversion Principle

**High-level components should depend on abstractions rather than concrete implementations.**

Instead of:

```text
Application
    │
    ▼
PostgreSQLDatabase
```

use an abstraction:

```text
Application
    │
    ▼
Database Interface
    ▲
    │
PostgreSQLDatabase
```

This makes implementations easier to replace and test.

For example, a test environment could use:

```text
Database Interface
├── PostgreSQLDatabase
└── MockDatabase
```

---

## SOLID Together

The principles work together to create loosely coupled systems:

```text
             SOLID
               │
       ┌───────┼────────┐
       ▼       ▼        ▼
   Low Coupling       High
                   Cohesion
       │
       ▼
Maintainable Software
```

They encourage:

* Small, focused components
* Clear abstractions
* Low coupling
* High cohesion
* Easier testing
* Easier extension

---

## Key Idea

The five SOLID principles provide guidelines for structuring object-oriented software:

| Principle | Core Idea                      |
| --------- | ------------------------------ |
| **S**     | One responsibility             |
| **O**     | Extend without modifying       |
| **L**     | Subtypes must be substitutable |
| **I**     | Prefer small interfaces        |
| **D**     | Depend on abstractions         |

SOLID is not a set of strict rules. The principles are **design guidelines** that help prevent tightly coupled and difficult-to-maintain code.
