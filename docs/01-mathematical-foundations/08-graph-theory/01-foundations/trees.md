# Trees

## TL;DR

A **tree** is a special type of **graph** that is **connected** and **acyclic**.

A tree with $n$ vertices always has exactly:

$$
n-1
$$

edges.

## Basic Structure

A tree consists of **nodes (vertices)** connected by **edges**.

A tree can be represented hierarchically:

```text
        A
       / \
      B   C
     / \
    D   E
```

The top node is called the **root**.

Nodes connected below another node are its **children**, while the node above is its **parent**.

## Important Properties

For a tree:

* There is exactly **one path** between any two nodes.
* A tree is **connected**.
* A tree contains **no cycles**.
* A tree with $n$ nodes has $n-1$ edges.

A node with no children is called a **leaf**.

## Binary Trees

A **binary tree** is a tree in which each node has at most two children.

```text
        A
       / \
      B   C
     / \
    D   E
```

Binary trees are important for data structures and algorithms.

Examples include:

* **Binary Search Trees (BSTs)**
* **Heaps**
* **Decision Trees**

## Trees in Data Science

Trees are particularly important in machine learning.

A **Decision Tree** recursively splits data based on features:

```text
        Feature?
        /      \
      Yes       No
      /          \
   Class A      Class B
```

Tree-based models include:

* Decision Trees
* Random Forests
* Gradient Boosted Trees

Trees are also used to represent hierarchical data, such as file systems, taxonomies, and organizational structures.

## Summary

A **tree** is a connected, acyclic graph with a hierarchical structure.

Key concepts include:

* **Root** — top node
* **Parent / Child** — hierarchical relationships
* **Leaf** — node without children
* **Depth** — distance from the root
* **Height** — maximum depth of the tree
