# Fields

## TL;DR

A **field** is an algebraic structure in which addition, subtraction, multiplication, and division (except by zero) are well-defined.

A field is a set $F$ equipped with two operations:

$$

* : F \times F \rightarrow F
  $$

and

$$
\cdot : F \times F \rightarrow F
$$

such that the field axioms hold.

## Field Axioms

For all $a,b,c \in F$:

### Addition

* **Associativity:**
  $$
  (a+b)+c=a+(b+c)
  $$

* **Commutativity:**
  $$
  a+b=b+a
  $$

* **Additive identity:**
  There exists $0\in F$ such that
  $$
  a+0=a
  $$

* **Additive inverse:**
  For every $a\in F$, there exists $-a\in F$ such that
  $$
  a+(-a)=0
  $$

### Multiplication

* **Associativity:**
  $$
  (ab)c=a(bc)
  $$

* **Commutativity:**
  $$
  ab=ba
  $$

* **Multiplicative identity:**
  There exists $1\in F$, with $1\neq0$, such that
  $$
  a\cdot1=a
  $$

* **Multiplicative inverse:**
  Every nonzero $a\in F$ has an inverse $a^{-1}$ such that
  $$
  aa^{-1}=1
  $$

### Distributivity

Multiplication distributes over addition:

$$
a(b+c)=ab+ac
$$

## Examples

Common examples of fields are:

* Rational numbers $\mathbb{Q}$
* Real numbers $\mathbb{R}$
* Complex numbers $\mathbb{C}$
* Finite fields $\mathbb{F}_p$, where $p$ is prime

For example, in $\mathbb{R}$:

$$
\frac{3}{4}\in\mathbb{R}
$$

and division is possible because every nonzero real number has a multiplicative inverse.

## Non-Examples

The integers $\mathbb{Z}$ are **not** a field.

For example,

$$
\frac{1}{2}\notin\mathbb{Z}
$$

so not every nonzero element has a multiplicative inverse within $\mathbb{Z}$.

The natural numbers $\mathbb{N}$ are also not a field because additive inverses and multiplicative inverses are generally missing.

## Field Extensions

A **field extension** is a field $K$ containing another field $F$:

$$
F\subseteq K
$$

For example:

$$
\mathbb{Q}\subseteq\mathbb{R}\subseteq\mathbb{C}
$$

Field extensions are important in algebra, number theory, and the study of polynomial equations.

## Relation to Other Algebraic Structures

A field can be viewed as a **commutative ring** in which every nonzero element has a multiplicative inverse.

The hierarchy is roughly:

$$
\text{Group}
\rightarrow
\text{Ring}
\rightarrow
\text{Field}
$$

Each structure adds additional operations and axioms.