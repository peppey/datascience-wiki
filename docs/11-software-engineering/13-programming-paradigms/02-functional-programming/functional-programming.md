# Functional Programming

## TL;DR

**Functional programming** is a programming paradigm that treats computation as the evaluation of **functions** and emphasizes **immutability**, **pure functions**, and **declarative code**.

Instead of describing *how* to change program state step by step, functional programming focuses on **what should be computed**.

---

## Pure Functions

A **pure function** always produces the same output for the same input and has no side effects.

```python
def add(x, y):
    return x + y
```

The function:

* depends only on its inputs
* does not modify external state
* does not perform side effects

This makes pure functions easier to test, reason about, and reuse.

---

## Immutability

Functional programming prefers **immutable data**.

Instead of modifying an existing object, a new value is created.

```python
numbers = [1, 2, 3]

new_numbers = numbers + [4]
```

The original `numbers` remains unchanged.

Immutability reduces unexpected interactions between different parts of a program.

---

## First-Class Functions

Functions can be treated like any other value.

They can be:

* assigned to variables
* passed as arguments
* returned from other functions
* stored in data structures

```python
def square(x):
    return x ** 2

f = square

print(f(3))
```

---

## Higher-Order Functions

A **higher-order function** takes a function as an argument or returns a function.

For example:

```python
numbers = [1, 2, 3, 4]

squared = list(map(lambda x: x ** 2, numbers))
```

Here, `map` applies a function to every element.

Common higher-order functions include:

* `map`
* `filter`
* `reduce`

---

## Declarative Programming

Functional programming is often **declarative**.

Imperative code describes *how* to perform an operation:

```python
result = []

for x in numbers:
    if x > 2:
        result.append(x)
```

A more functional approach describes *what* is wanted:

```python
result = list(filter(lambda x: x > 2, numbers))
```

The second version focuses on the desired transformation rather than the individual steps.

---

## Recursion

Functional programming often uses **recursion** instead of mutable loops.

For example:

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

Functional languages often provide mechanisms such as **tail-call optimization** to make recursive programs more efficient.

---

## Benefits

Functional programming can provide:

* easier testing
* fewer side effects
* more predictable code
* easier reasoning about program behavior
* better composability
* safer concurrent programming

These properties are particularly useful for data processing and large software systems.

---

## Functional Programming in Python

Python is not a purely functional language, but it supports many functional programming concepts:

```python
numbers = [1, 2, 3, 4, 5]

result = list(
    map(
        lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)
```

Python also provides tools such as:

* `lambda`
* `map`
* `filter`
* `functools.reduce`
* comprehensions
* generators

In practice, Python programs often combine **functional**, **object-oriented**, and **imperative** programming styles.

---

## Functional vs. Imperative Programming

| Functional                       | Imperative                                   |
| -------------------------------- | -------------------------------------------- |
| Focuses on transformations       | Focuses on instructions                      |
| Prefers immutable data           | Often uses mutable state                     |
| Uses pure functions              | Frequently uses side effects                 |
| Declarative                      | Procedural                                   |
| Functions are first-class values | Functions may primarily represent procedures |

Most modern programming languages support a mixture of these approaches.

---

## Key Concepts

The main ideas of functional programming are:

1. **Pure functions**
2. **Immutability**
3. **First-class functions**
4. **Higher-order functions**
5. **Function composition**
6. **Declarative programming**
7. **Recursion**
8. **Minimizing side effects**

Functional programming is therefore less about using a specific language and more about **structuring programs around predictable transformations of data**.
