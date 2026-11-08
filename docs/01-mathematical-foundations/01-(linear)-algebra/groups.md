# GROUPS

## Introduction

Groups are fundamental algebraic structures in abstract algebra and play an important role in linear algebra, geometry, number theory and many other areas of mathematics.

A group is a set equipped with a binary operation that combines any two elements of the set and satisfies four fundamental properties: closure, associativity, the existence of an identity element and the existence of inverse elements.

Groups provide a mathematical framework for describing symmetry, transformations and algebraic operations.

In linear algebra, groups frequently appear when studying invertible matrices, linear transformations, vector spaces and symmetry operations.

Understanding groups is particularly useful for more advanced topics such as group representations, eigenvalue theory, matrix decompositions and Lie groups.

## Definition of a Group

A group is defined as a pair $(G, *)$, where:

- $G$ is a non-empty set.
- $*$ is a binary operation defined on $G$.

The binary operation maps two elements of the set to another element of the same set:

$$
*:G\times G\rightarrow G
$$

For $(G,*)$ to be a group, the following four axioms must hold.

### Closure

For any two elements $a,b\in G$, their combination must also belong to $G$:

$$
a*b\in G
$$

This means that applying the group operation never produces an element outside the group.

### Associativity

The group operation must be associative:

$$
(a*b)*c=a*(b*c)
$$

for all $a,b,c\in G$.

Associativity means that the grouping of operations does not affect the result.

Importantly, associativity does not imply commutativity.

### Identity Element

There must exist an element $e\in G$ such that:

$$
e*a=a*e=a
$$

for every $a\in G$.

The element $e$ is called the identity element.

For example, the identity element of addition is $0$, whereas the identity element of multiplication is $1$.

### Inverse Element

For every element $a\in G$, there must exist an inverse element $a^{-1}\in G$ such that:

$$
a*a^{-1}=a^{-1}*a=e
$$

The inverse element reverses the effect of the group operation.

For additive groups, the inverse of an element $a$ is usually written as $-a$.

For multiplicative groups, it is written as $a^{-1}$.

## Abelian Groups

A group is called an Abelian group if its operation is commutative.

This means that:

$$
a*b=b*a
$$

for all $a,b\in G$.

Every Abelian group is a group, but not every group is Abelian.

**Example: Integers under Addition**

Consider the set of integers:

$$
(\mathbb{Z},+)
$$

This is an Abelian group because:

- The sum of two integers is always an integer.
- Addition is associative.
- The identity element is $0$.
- Every integer $a$ has an additive inverse $-a$.
- Addition is commutative.

Therefore:

$$
a+b=b+a
$$

**Example: Invertible Matrices**

The set of all invertible $n\times n$ matrices with real entries forms a group under matrix multiplication.

However, matrix multiplication is generally not commutative:

$$
AB\neq BA
$$

Therefore, this group is generally non-Abelian.

## Examples of Groups

### Integers Under Addition

The integers form a group under addition:

$$
(\mathbb{Z},+)
$$

The relevant properties are:

| Property | Description |
|---|---|
| Closure | $a+b\in\mathbb{Z}$ |
| Associativity | $(a+b)+c=a+(b+c)$ |
| Identity | $0$ |
| Inverse | $-a$ |
| Commutativity | $a+b=b+a$ |

This is one of the simplest examples of an infinite Abelian group.

### Non-Zero Real Numbers Under Multiplication

Consider the set:

$$
(\mathbb{R}\setminus\{0\},\cdot)
$$

This set forms an Abelian group under multiplication.

The identity element is:

$$
e=1
$$

The inverse of an element $a$ is:

$$
a^{-1}=\frac{1}{a}
$$

The element $0$ must be excluded because it does not possess a multiplicative inverse.

### Invertible Matrices

The set of all invertible $n\times n$ matrices over a field $F$ is called the general linear group:

$$
GL(n,F)
$$

It is defined as:

$$
GL(n,F)
=
\{A\in F^{n\times n}:\det(A)\neq 0\}
$$

The group operation is matrix multiplication.

Its identity element is the identity matrix:

$$
I_n=
\begin{pmatrix}
1&0&\cdots&0\\
0&1&\cdots&0\\
\vdots&\vdots&\ddots&\vdots\\
0&0&\cdots&1
\end{pmatrix}
$$

Every matrix $A\in GL(n,F)$ has an inverse:

$$
AA^{-1}=A^{-1}A=I_n
$$

This group is particularly important in linear algebra because invertible matrices represent reversible linear transformations.

## Subgroups

A subgroup is a subset of a group that is itself a group under the same operation.

Let $(G,*)$ be a group and let $H\subseteq G$.

Then $H$ is a subgroup of $G$ if $(H,*)$ also satisfies the group axioms.

This relationship is denoted by:

$$
H\leq G
$$

A useful subgroup criterion states that a non-empty subset $H$ of a group $G$ is a subgroup if:

$$
a*b^{-1}\in H
$$

for all $a,b\in H$.

For additive groups, this criterion becomes:

$$
a-b\in H
$$

for all $a,b\in H$.

### Example: Even Integers

Consider the set of even integers:

$$
2\mathbb{Z}
=
\{\dots,-4,-2,0,2,4,\dots\}
$$

This set is a subgroup of $(\mathbb{Z},+)$.

For any two even integers $a,b\in 2\mathbb{Z}$:

$$
a-b\in 2\mathbb{Z}
$$

Therefore:

$$
2\mathbb{Z}\leq\mathbb{Z}
$$

### Example: Special Linear Group

An important subgroup of the general linear group is the special linear group:

$$
SL(n,F)
=
\{A\in GL(n,F):\det(A)=1\}
$$

The determinant condition is preserved under matrix multiplication because:

$$
\det(AB)=\det(A)\det(B)
$$

If $\det(A)=\det(B)=1$, then:

$$
\det(AB)=1
$$

Furthermore:

$$
\det(I_n)=1
$$

and:

$$
\det(A^{-1})=\frac{1}{\det(A)}=1
$$

Consequently:

$$
SL(n,F)\leq GL(n,F)
$$

The special linear group consists of invertible matrices that preserve oriented volume.

## Cyclic Groups

A group is called cyclic if all its elements can be generated by repeatedly applying the group operation to a single element.

An element $g\in G$ is called a generator if:

$$
G=\langle g\rangle
$$

For a multiplicative group, the generated subgroup is:

$$
\langle g\rangle
=
\{g^k:k\in\mathbb{Z}\}
$$

For an additive group, it is:

$$
\langle g\rangle
=
\{kg:k\in\mathbb{Z}\}
$$

### Example: Integers Under Addition

The group of integers is cyclic because every integer can be generated by adding or subtracting $1$:

$$
\mathbb{Z}=\langle 1\rangle
$$

It is also possible to use $-1$ as a generator:

$$
\mathbb{Z}=\langle -1\rangle
$$

### Finite Cyclic Groups

Consider the integers modulo $n$:

$$
\mathbb{Z}_n
=
\{0,1,\dots,n-1\}
$$

with addition modulo $n$.

For example:

$$
\mathbb{Z}_5=\{0,1,2,3,4\}
$$

The operation is defined as:

$$
a\oplus b=(a+b)\mod 5
$$

The element $1$ generates the entire group:

$$
\mathbb{Z}_5=\langle 1\rangle
$$

because repeated addition produces:

$$
1,\ 2,\ 3,\ 4,\ 0
$$

Every cyclic group is Abelian.

## Permutation Groups

A permutation is a rearrangement of the elements of a set.

The set of all permutations of $n$ elements forms a group under composition, called the symmetric group:

$$
S_n
$$

The group operation is the composition of permutations.

The symmetric group contains exactly:

$$
|S_n|=n!
$$

elements.

For example, the symmetric group on three elements contains:

$$
|S_3|=3!=6
$$

permutations.

Permutation groups are generally non-Abelian for $n\geq 3$ because the order of composition can change the result.

They are important in algebra, combinatorics and the mathematical description of symmetry.

## Matrix Groups and Linear Transformations

Groups are closely connected to linear algebra because invertible linear transformations can be represented by invertible matrices.

A linear transformation:

$$
T:V\rightarrow V
$$

is invertible if there exists an inverse transformation:

$$
T^{-1}:V\rightarrow V
$$

such that:

$$
T\circ T^{-1}=T^{-1}\circ T=I
$$

The set of all invertible linear transformations on a vector space $V$ forms a group under composition.

This group is called the general linear group of the vector space:

$$
GL(V)
$$

When a basis is chosen, these transformations can be represented by invertible matrices.

Therefore, the abstract group of invertible linear transformations corresponds to the matrix group $GL(n,F)$.

### Orthogonal Groups

An important example of a matrix group is the orthogonal group:

$$
O(n)
=
\{Q\in\mathbb{R}^{n\times n}:Q^TQ=I_n\}
$$

An orthogonal matrix satisfies:

$$
Q^{-1}=Q^T
$$

Orthogonal matrices preserve Euclidean lengths and angles.

For any vector $x\in\mathbb{R}^n$:

$$
\|Qx\|^2
=
(Qx)^T(Qx)
$$

$$
=x^TQ^TQx
$$

$$
=x^Tx
$$

Therefore:

$$
\|Qx\|=\|x\|
$$

Orthogonal matrices describe transformations such as rotations and reflections.

### Special Orthogonal Group

The special orthogonal group is defined as:

$$
SO(n)
=
\{Q\in O(n):\det(Q)=1\}
$$

It consists of rotations without reflections.

In two dimensions, a rotation matrix is given by:

$$
R(\theta)
=
\begin{pmatrix}
\cos(\theta)&-\sin(\theta)\\
\sin(\theta)&\cos(\theta)
\end{pmatrix}
$$

It satisfies:

$$
R(\theta)^TR(\theta)=I
$$

and:

$$
\det(R(\theta))=1
$$

Consequently:

$$
R(\theta)\in SO(2)
$$

The special orthogonal group is important in geometry, physics, computer graphics and robotics.

## Order of a Group

The order of a finite group is the number of elements it contains.

It is denoted by:

$$
|G|
$$

For example, the group $\mathbb{Z}_5$ has order:

$$
|\mathbb{Z}_5|=5
$$

The order of an individual element $g\in G$ is the smallest positive integer $k$ such that:

$$
g^k=e
$$

if such an integer exists.

For additive groups, this condition becomes:

$$
kg=0
$$

For example, in $\mathbb{Z}_6$, the element $2$ has order $3$ because:

$$
2+2+2=6\equiv 0\pmod 6
$$

## Lagrange's Theorem

Lagrange's theorem is a fundamental result concerning finite groups and their subgroups.

It states that the order of every subgroup divides the order of the group.

For a finite group $G$ and a subgroup $H\leq G$:

$$
|H|\mid |G|
$$

Equivalently:

$$
|G|=[G:H]\cdot |H|
$$

where $[G:H]$ denotes the index of $H$ in $G$, meaning the number of distinct left cosets of $H$ in $G$.

For example, consider:

$$
G=\mathbb{Z}_6
$$

The subset:

$$
H=\{0,2,4\}
$$

is a subgroup of $G$.

Their orders are:

$$
|G|=6
$$

$$
|H|=3
$$

Therefore:

$$
6=2\cdot 3
$$

This illustrates Lagrange's theorem.

An important consequence is that the order of every element in a finite group divides the order of the group.

## Group Homomorphisms

A group homomorphism is a mapping between two groups that preserves their group operations.

Let $(G,*)$ and $(H,\circ)$ be groups.

A function:

$$
\varphi:G\rightarrow H
$$

is a group homomorphism if:

$$
\varphi(a*b)
=
\varphi(a)\circ\varphi(b)
$$

for all $a,b\in G$.

This means that applying the group operation before or after the mapping produces the same result.

### Example: Determinant

The determinant provides an important example of a group homomorphism.

Consider:

$$
\det:GL(n,F)\rightarrow F^\times
$$

where $F^\times$ denotes the non-zero elements of the field $F$ under multiplication.

For any invertible matrices $A$ and $B$:

$$
\det(AB)=\det(A)\det(B)
$$

Therefore, the determinant preserves the group operation and is a group homomorphism.

Its kernel is:

$$
\ker(\det)
=
\{A\in GL(n,F):\det(A)=1\}
$$

Consequently:

$$
\ker(\det)=SL(n,F)
$$

This illustrates how group theory can be used to identify important matrix subgroups.

## Isomorphisms

An isomorphism is a bijective group homomorphism.

If two groups are isomorphic, they have the same algebraic structure, even if their elements are represented differently.

This is denoted by:

$$
G\cong H
$$

An isomorphism preserves the group operation, identity element, inverses and element orders.

For example, the additive group of real numbers and the multiplicative group of positive real numbers are isomorphic.

Consider the mapping:

$$
\varphi:\mathbb{R}\rightarrow\mathbb{R}_{>0}
$$

defined by:

$$
\varphi(x)=e^x
$$

It preserves the group operations because:

$$
\varphi(x+y)
=
e^{x+y}
=
e^xe^y
$$

Therefore:

$$
\varphi(x+y)=\varphi(x)\varphi(y)
$$

Since the exponential function is bijective from $\mathbb{R}$ to $\mathbb{R}_{>0}$, the groups are isomorphic:

$$
(\mathbb{R},+)
\cong
(\mathbb{R}_{>0},\cdot)
$$

## Applications in Linear Algebra and Beyond

Groups are used in many mathematical and applied fields.

**Linear Algebra**

Invertible matrices form groups under matrix multiplication. Special matrix groups describe transformations that preserve properties such as lengths, angles and volumes.

**Geometry**

Groups describe geometric symmetries, including rotations, reflections and translations.

**Physics**

Symmetry groups are fundamental in classical mechanics, quantum mechanics and particle physics.

**Computer Graphics**

Rotational groups are used to describe the orientation of objects in two-dimensional and three-dimensional space.

**Cryptography**

Finite groups and their algebraic properties are used in cryptographic systems, including discrete logarithm-based methods.

**Machine Learning**

Group theory provides the mathematical foundation for symmetry-aware architectures and equivariant neural networks.

## Summary

Groups are algebraic structures consisting of a set and a binary operation satisfying closure, associativity, identity and inverse properties.

They provide a general mathematical framework for studying operations, symmetries and transformations.

Important examples include the integers under addition, invertible matrices under multiplication, cyclic groups, permutation groups and orthogonal matrix groups.

In linear algebra, groups are particularly relevant because invertible linear transformations form groups, while special matrix groups describe transformations that preserve geometric properties.

Concepts such as subgroups, homomorphisms, isomorphisms and Lagrange's theorem provide additional tools for understanding the structure and relationships between groups.

Overall, group theory establishes a fundamental connection between algebraic operations, linear transformations and symmetry.