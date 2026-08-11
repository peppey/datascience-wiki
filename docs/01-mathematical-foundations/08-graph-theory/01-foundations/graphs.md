# Graphs

## TL;DR

A **graph** is a mathematical structure used to represent **objects and relationships** between them.

A graph consists of:

* **Vertices (nodes)** — the objects
* **Edges** — the relationships between objects

A graph is commonly written as:

$$
G=(V,E)
$$

where $V$ is the set of vertices and $E$ is the set of edges.

## Basic Concepts

Consider a graph:

$$
G=(V,E)
$$

with

$$
V={A,B,C,D}
$$

and

$$
E={(A,B),(B,C),(C,D)}.
$$

The edges describe which vertices are connected.

### Degree

The **degree** of a vertex is the number of edges connected to it.

For example, if

$$
E={(A,B),(A,C),(A,D)},
$$

then vertex $A$ has degree:

$$
\deg(A)=3.
$$

## Types of Graphs

### Undirected Graph

In an **undirected graph**, edges have no direction:

$$
(A,B)=(B,A)
$$

They represent a symmetric relationship.

### Directed Graph

In a **directed graph**, edges have a direction:

$$
A\rightarrow B
$$

Here, $A\rightarrow B$ does not necessarily imply $B\rightarrow A$.

### Weighted Graph

Edges can have associated values called **weights**:

$$
w(A,B)=5
$$

Weights can represent distance, cost, similarity, probability, or other quantities.

### Unweighted Graph

In an **unweighted graph**, edges simply indicate whether a relationship exists.

## Paths and Connectivity

A **path** is a sequence of connected vertices:

$$
A\rightarrow B\rightarrow C\rightarrow D.
$$

The **length** of an unweighted path is usually the number of edges it contains.

A graph is **connected** if every pair of vertices can be connected by a path.

## Cycles

A **cycle** is a path that starts and ends at the same vertex without repeating intermediate vertices.

For example:

$$
A\rightarrow B\rightarrow C\rightarrow A.
$$

A graph without cycles is called **acyclic**.

A connected undirected acyclic graph is a **tree**.

## Graph Representation

Graphs can be represented in several ways.

### Adjacency Matrix

An adjacency matrix stores connections in a matrix:

$$
A_{ij}=
\begin{cases}
1 & \text{if } i \text{ and } j \text{ are connected}\
0 & \text{otherwise}
\end{cases}
$$

For weighted graphs, the entries can contain edge weights instead.

### Adjacency List

An adjacency list stores the neighbors of each vertex:

```text
A → B, C
B → A, C
C → A, B
```

Adjacency lists are often more memory-efficient for **sparse graphs**.

## Common Graph Algorithms

Important graph algorithms include:

* **Breadth-First Search (BFS)** — explores vertices level by level
* **Depth-First Search (DFS)** — explores paths deeply before backtracking
* **Dijkstra's algorithm** — finds shortest paths with non-negative edge weights
* **Minimum Spanning Tree (MST)** — connects all vertices with minimum total edge weight
* **Topological sorting** — orders vertices of a directed acyclic graph

## Graphs in Data Science

Graphs are useful whenever data contains relationships between entities.

Examples include:

* Social networks
* Road and transportation networks
* Knowledge graphs
* Recommendation systems
* Molecular structures
* Computer networks
* Dependencies between software packages

Graph-based machine learning methods include **Graph Neural Networks (GNNs)**, which learn representations from both node features and graph structure.

## Summary

Graphs provide a mathematical framework for modeling **entities and their relationships**.

The fundamental concepts are:

* **Vertices** — entities
* **Edges** — relationships
* **Paths** — sequences of connections
* **Cycles** — closed paths
* **Weights** — values associated with edges
* **Connectivity** — how vertices are related

Graphs form the foundation of **graph theory** and are widely used in computer science, mathematics, and data science.
