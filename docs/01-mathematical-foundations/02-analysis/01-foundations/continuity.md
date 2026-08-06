# Continuity

## TL;DR

A function is **continuous** if small changes in the input lead to small changes in the output.

Informally:

> A continuous function can be drawn without lifting the pen.

---

## Definition

A function:
f: R → R

is continuous at a point `a` if:
lim x→a f(x) = f(a)

This means:

1. The limit exists
2. The function value exists
3. Both are equal

---

## Intuition

For a continuous function:
x changes slightly
↓
f(x) changes slightly

Example:
f(x) = x²

Small changes in `x` create small changes in the output.

---

## Discontinuous Functions

A function is discontinuous if there is a break, jump, or missing point.

Examples:

### Jump discontinuity

The function suddenly changes its value.

---

### Missing point

Example:

f(x) = (x² - 1) / (x - 1)

At x = 1, the function is not defined, even though the limit exists.

---

## Continuity in Machine Learning

Continuity is important because many ML methods assume that small input changes should not create unpredictable outputs.

Examples:

- neural networks use continuous activation functions
- optimization methods rely on smooth changes of the loss function
- gradient descent requires continuous and often differentiable functions

---

## Continuity vs Differentiability

Differentiability is a stronger condition:

differentiable ⇒ continuous

but:
continuous ⇏ differentiable

Example:
f(x) = |x|

is continuous but has a sharp corner at:
x = 0

---

## Key Idea

Continuity means that a function behaves smoothly: nearby inputs produce nearby outputs.
