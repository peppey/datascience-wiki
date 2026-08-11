# Set Theory

**Set theory** is the mathematical study of **sets**, collections of objects considered as mathematical entities.

Sets provide a foundation for many areas of mathematics, including:

* logic
* analysis
* algebra
* topology
* probability
* discrete mathematics
* computer science

---

# Power Set

The **power set** of $A$, denoted by $\mathcal\{P\}(A)$ or $2^A$, is the set of all subsets of $A$.

For:

$$
A=\{1,2\},
$$

we have:

$$
\mathcal\{P\}(A)
=

\{\varnothing,\{1\},\{2\},\{1,2\}\}.
$$

If $A$ is finite:

$$
|A|=n,
$$

then:

$$
|\mathcal\{P\}(A)|=2^n.
$$

The power set is important in logic, combinatorics, topology, and the foundations of mathematics.

---

# Laws of Set Algebra

Set operations satisfy many algebraic identities.

## Commutative Laws

$$
A\cup B=B\cup A
$$

$$
A\cap B=B\cap A
$$

## Associative Laws

$$
(A\cup B)\cup C
=

A\cup(B\cup C)
$$

$$
(A\cap B)\cap C
=

A\cap(B\cap C)
$$

## Distributive Laws

$$
A\cap(B\cup C)
=

(A\cap B)\cup(A\cap C)
$$

$$
A\cup(B\cap C)
=

(A\cup B)\cap(A\cup C)
$$

## Identity Laws

$$
A\cup\varnothing=A
$$

$$
A\cap U=A
$$

## Complement Laws

$$
A\cup A^c=U
$$

$$
A\cap A^c=\varnothing
$$

---

# De Morgan's Laws

De Morgan's laws describe how complements interact with unions and intersections:

$$
(A\cup B)^c
=

A^c\cap B^c
$$

and:

$$
(A\cap B)^c
=

A^c\cup B^c.
$$

For arbitrary collections of sets:

$$
\left(\bigcup_\{i\in I\}A_i\right)^c
=

\bigcap_\{i\in I\}A_i^c
$$

and:

$$
\left(\bigcap_\{i\in I\}A_i\right)^c
=

\bigcup_\{i\in I\}A_i^c.
$$

---

# Partitions

A **partition** of a set $A$ is a collection of non-empty subsets such that:

1. every element of $A$ belongs to exactly one subset
2. the subsets are pairwise disjoint
3. their union is $A$

For example:

$$
\{\{1,2\},\{3,4\},\{5\}\}
$$

is a partition of:

$$
\{1,2,3,4,5\}.
$$

Partitions are closely related to **equivalence relations**.

---

# Cartesian Product

The **Cartesian product** of $A$ and $B$ is:

$$
A\times B
=

\{(a,b):a\in A,\ b\in B\}.
$$

Its elements are **ordered pairs**.

For example:

$$
\{1,2\}\times\{a,b\}
=

\{(1,a),(1,b),(2,a),(2,b)\}.
$$

For finite sets:

$$
|A\times B|
=

|A||B|.
$$

Cartesian products form the basis for coordinate spaces such as:

$$
\mathbb\{R\}^2
=

\mathbb\{R\}\times\mathbb\{R\}.
$$

---

# Relations


A **binary relation** from $A$ to $B$ is a subset of the Cartesian product:

$$
R\subseteq A\times B.
$$

If:

$$
(a,b)\in R,
$$

we can write:

$$
aRb.
$$

Relations can have properties such as:

* reflexivity
* symmetry
* antisymmetry
* transitivity

---

## Equivalence Relations

A relation $\sim$ on $A$ is an **equivalence relation** if it is:

### Reflexive

$$
a\sim a.
$$

### Symmetric

$$
a\sim b
\Rightarrow
b\sim a.
$$

### Transitive

$$
a\sim b
\land
b\sim c
\Rightarrow
a\sim c.
$$

Every equivalence relation induces a partition of the set into **equivalence classes**.

---

## Equivalence Classes

The equivalence class of $a$ is:

$$
[a]
=

\{x\in A:x\sim a\}.
$$

The set of all equivalence classes is called the **quotient set**:

$$
A/\{\sim\}.
$$

---

# Functions

A function from $A$ to $B$ is a relation that assigns **exactly one** element of $B$ to every element of $A$:

$$
f:A\to B.
$$

Here:

* $A$ is the **domain**
* $B$ is the **codomain**
* $f(A)$ is the **image** or **range**

The graph of a function is a subset of:

$$
A\times B.
$$

---

## Injective Functions

A function is **injective** if different inputs have different outputs:

$$
f(a)=f(b)
\Rightarrow
a=b.
$$

---

## Surjective Functions

A function is **surjective** if every element of the codomain is reached:

$$
\forall b\in B,\ \exists a\in A:
f(a)=b.
$$

---

## Bijective Functions

A function is **bijective** if it is both injective and surjective.

A bijection establishes a one-to-one correspondence between two sets.

This concept is fundamental to **cardinality**.

---

# Finite and Infinite Sets

A set is **finite** if it contains exactly $n$ elements for some:

$$
n\in\mathbb\{N\}.
$$

Otherwise, it is infinite.

An infinite set can have the same cardinality as a proper subset of itself.

For example:

$$
\mathbb\{N\}
$$

and:

$$
2\mathbb\{N\}
=

\{2,4,6,\ldots\}
$$

have the same cardinality because:

$$
f(n)=2n
$$

is a bijection.

---

# Countable Sets

A set is **countably infinite** if there exists a bijection:

$$
f:\mathbb\{N\}\to A.
$$

The natural numbers, integers, and rational numbers are countably infinite:

$$
|\mathbb\{N\}|
=

 |\mathbb\{Z\}|

|\mathbb\{Q\}|.
$$

Although $\mathbb\{Q\}$ is dense in $\mathbb\{R\}$, it is still countable.

---

# Uncountable Sets

A set is **uncountable** if no bijection with $\mathbb\{N\}$ exists.

The real numbers are uncountable:

$$
|\mathbb\{R\}|>|\mathbb\{N\}|.
$$

Cantor's **diagonal argument** proves that the real numbers cannot be enumerated by the natural numbers.

---

# Cardinal Numbers

Infinite cardinalities are represented using **cardinal numbers**.

The cardinality of the natural numbers is:

$$
\aleph_0.
$$

The cardinality of the real numbers is:

$$
|\mathbb\{R\}|=2^\{\aleph_0\}.
$$

Cantor's theorem states that for every set $A$:

$$
|A|<|\mathcal\{P\}(A)|.
$$

Therefore, there is no largest cardinality.

---

# Ordinal Numbers

**Ordinal numbers** describe the order type of well-ordered sets.

Finite ordinals correspond to:

$$
0,1,2,3,\ldots
$$

The first infinite ordinal is:

$$
\omega.
$$

Cardinals describe **how many** elements a set has, while ordinals describe **the position or order type**.

---

# Well-Ordering

A set is **well-ordered** if every non-empty subset has a least element.

The natural numbers are well-ordered under the usual ordering.

The **well-ordering theorem** states:

> Every set can be well-ordered.

This theorem is equivalent to the **axiom of choice** in standard set theory.

---

# Axiom of Choice

The **axiom of choice (AC)** states that for every collection of non-empty sets, it is possible to choose one element from each set.

Informally:

$$
\{A_i\}_\{i\in I\},
\quad
A_i\neq\varnothing
$$

implies the existence of a choice function:

$$
f:I\to\bigcup_\{i\in I\}A_i
$$

such that:

$$
f(i)\in A_i.
$$

The axiom of choice has many important consequences, including:

* well-ordering theorem
* Zorn's lemma
* every vector space has a basis
* every set can be well-ordered

---

# Zorn's Lemma

**Zorn's lemma** states that if a partially ordered set has the property that every chain has an upper bound, then the set contains a maximal element.

It is equivalent to the axiom of choice.

Zorn's lemma is frequently used to prove existence results in abstract mathematics.

For example, it can be used to prove that every vector space has a basis.

---

# Axioms of Set Theory

Modern mathematics commonly uses the **Zermelo-Fraenkel axioms** (ZF).

The most common axioms include:

* Extensionality
* Empty Set
* Pairing
* Union
* Power Set
* Infinity
* Separation
* Replacement
* Foundation

Adding the **Axiom of Choice** gives:

$$
\text\{ZFC\}=\text\{ZF\}+\text\{AC\}.
$$

ZFC is the standard foundational system for much of modern mathematics.

---

# Extensionality

The **axiom of extensionality** states that sets are determined entirely by their elements:

$$
\forall A,B:
\left[
\forall x(x\in A\iff x\in B)
\Rightarrow
A=B
\right].
$$

This formalizes the idea that two sets with exactly the same elements are the same set.

---

# Foundation

The **axiom of foundation** prevents infinite descending membership chains.

Informally, it prevents sets from containing themselves, such as:

$$
A\in A.
$$

It also rules out structures such as:

$$
A_1\ni A_2\ni A_3\ni\cdots
$$

in the standard foundations of mathematics.

---

# Russell's Paradox

Naive set theory allows definitions such as:

$$
R=\{x:x\notin x\}.
$$

Now ask whether:

$$
R\in R.
$$

If:

$$
R\in R,
$$

then by definition:

$$
R\notin R.
$$

If:

$$
R\notin R,
$$

then by definition:

$$
R\in R.
$$

This contradiction is **Russell's paradox**.

It showed that unrestricted set formation cannot be used safely as a foundation for mathematics.

Modern axiomatic set theory restricts how sets can be constructed.

---

# Classes

In some formulations of set theory, it is useful to distinguish between **sets** and **proper classes**.

A **set** can itself be an element of another set.

A **proper class** is too large to be a set within the theory.

For example, in standard set theory, the collection of all sets is not itself a set.

Similarly, the collection of all ordinals forms a proper class.

---

# Transfinite Mathematics

Set theory extends familiar finite concepts to infinite structures.

Important concepts include:

* infinite cardinal numbers
* ordinal numbers
* transfinite induction
* transfinite recursion
* well-orderings

These provide mathematical tools for reasoning about arbitrary infinite structures.

---

# Transfinite Induction

**Transfinite induction** generalizes ordinary mathematical induction to well-ordered sets.

For a property $P(\alpha)$, one proves that:

$$
P(\beta)
$$

holds assuming:

$$
P(\alpha)
$$

for all:

$$
\alpha<\beta.
$$

Then:

$$
P(\alpha)
$$

holds for all ordinals $\alpha$.

---

# Set-Theoretic Constructions

Set theory provides standard constructions used throughout mathematics.

Important examples include:

* ordered pairs
* Cartesian products
* relations
* functions
* equivalence classes
* quotient sets
* power sets
* sequences
* indexed families

Many mathematical objects can ultimately be represented in terms of sets.

---

# Indexed Families

An **indexed family of sets** is written:

$$
\{A_i\}_\{i\in I\}.
$$

The index set $I$ identifies the members of the family.

The union is:

$$
\bigcup_\{i\in I\}A_i
$$

and the intersection is:

$$
\bigcap_\{i\in I\}A_i.
$$

Indexed families are fundamental in topology, measure theory, probability, and analysis.

---

# Sequences

A sequence can be viewed as a function:

$$
a:\mathbb\{N\}\to A.
$$

We usually write:

$$
(a_n)_\{n\in\mathbb\{N\}\}.
$$

This connects set theory directly with analysis, where sequences are used to define convergence, limits, and series.

---

# Set Systems

A **set system** or **family of sets** is a collection of subsets of a common universe:

$$
\mathcal\{F\}\subseteq\mathcal\{P\}(X).
$$

Important examples include:

* sigma-algebras
* topologies
* filters
* ideals
* simplicial complexes

Set systems are particularly important in probability, topology, and combinatorics.

---

# Sigma-Algebras

A **sigma-algebra** $\mathcal\{F\}$ on a set $X$ is a collection of subsets of $X$ satisfying:

$$
X\in\mathcal\{F\},
$$

if:

$$
A\in\mathcal\{F\}
\Rightarrow
A^c\in\mathcal\{F\},
$$

and if:

$$
A_1,A_2,\ldots\in\mathcal\{F\},
$$

then:

$$
\bigcup_\{i=1\}^\{\infty\}A_i\in\mathcal\{F\}.
$$

Sigma-algebras form the foundation of **measure theory and probability theory**.

---

# Topologies

A **topology** on $X$ is a collection $\mathcal\{T\}\subseteq\mathcal\{P\}(X)$ satisfying:

$$
\varnothing,X\in\mathcal\{T\},
$$

arbitrary unions of sets in $\mathcal\{T\}$ are in $\mathcal\{T\}$, and finite intersections of sets in $\mathcal\{T\}$ are in $\mathcal\{T\}$.

The elements of $\mathcal\{T\}$ are called **open sets**.

Topology therefore builds geometric and analytical structures directly from sets.

---

# Important Distinctions

### Element vs. Subset

If:

$$
A=\{1,2,3\},
$$

then:

$$
1\in A
$$

but:

$$
\{1\}\subseteq A.
$$

These are different statements.

### Set vs. Power Set

If:

$$
A=\{1,2\},
$$

then:

$$
1\in A
$$

while:

$$
\{1\}\in\mathcal\{P\}(A).
$$

### Cardinal vs. Ordinal

* **Cardinality** describes size.
* **Ordinality** describes order type.

---

# Why Set Theory Matters

Set theory provides a common language for mathematics.

Concepts such as:

$$
\text\{numbers\}
\rightarrow
\text\{functions\}
\rightarrow
\text\{spaces\}
\rightarrow
\text\{structures\}
$$

can all be formulated using sets.

It is therefore closely connected to:

* **logic** — formal mathematical reasoning
* **analysis** — sequences, functions, spaces
* **algebra** — groups, rings, fields
* **topology** — open sets and topological spaces
* **probability** — sample spaces and sigma-algebras
* **computer science** — relations, functions, semantics, and formal methods
