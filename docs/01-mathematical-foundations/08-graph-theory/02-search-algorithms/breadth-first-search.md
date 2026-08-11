# Breadth-First Search

## TL;DR

**Breadth-First Search (BFS)** is a graph traversal algorithm that explores a graph **level by level**.

It starts at a given node and visits all neighboring nodes before moving to the next level.

## Algorithm

Given a starting node:

```text
        A
       / \
      B   C
     / \   \
    D   E   F
```

BFS starting at $A$ visits:

```text
A → B → C → D → E → F
```

The algorithm typically uses a **queue**:

```text
1. Add the starting node to the queue.
2. Remove the first node from the queue.
3. Visit its unvisited neighbors.
4. Add those neighbors to the queue.
5. Repeat until the queue is empty.
```

## Example

```text
Queue: [A]

Visit A
Queue: [B, C]

Visit B
Queue: [C, D, E]

Visit C
Queue: [D, E, F]

Visit D
Queue: [E, F]

...
```

The resulting traversal is:

$$
A,B,C,D,E,F
$$

## Shortest Paths

For an **unweighted graph**, BFS finds the shortest path in terms of the number of edges.

For example:

```text
A ─ B ─ D
│
└─ C ─ E
```

Starting from $A$, BFS finds:

$$
A\rightarrow B\rightarrow D
$$

as a shortest path from $A$ to $D$.

## Complexity

For a graph with $V$ vertices and $E$ edges:

$$
O(|V|+|E|)
$$

The space complexity is also:

$$
O(|V|)
$$

because the queue and visited set can contain up to all vertices.

## Applications

BFS is commonly used for:

* Shortest paths in unweighted graphs
* Finding connected components
* Level-order traversal of trees
* Checking whether a graph is bipartite
* Finding nodes within a given distance
* Web crawling and network exploration

## BFS vs. DFS

|                            | BFS               | DFS                       |
| -------------------------- | ----------------- | ------------------------- |
| Strategy                   | Level by level    | Go as deep as possible    |
| Main structure             | Queue             | Stack / recursion         |
| Shortest path (unweighted) | Yes               | Not necessarily           |
| Typical use                | Distances, levels | Exploration, backtracking |

## Summary

**Breadth-First Search** explores a graph layer by layer using a **queue**.

Its main advantages are:

* Finds shortest paths in unweighted graphs
* Systematically explores all reachable nodes
* Runs in $O(|V|+|E|)$ time
