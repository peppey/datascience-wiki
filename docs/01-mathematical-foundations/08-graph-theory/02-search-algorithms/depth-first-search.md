# Depth-First Search

## TL;DR

**Depth-First Search (DFS)** is a graph traversal algorithm that explores a graph by going **as deep as possible** along a path before backtracking.

It can be implemented using **recursion** or an explicit **stack**.

## Algorithm

Given the graph:

```text
        A
       / \
      B   C
     / \
    D   E
```

Starting at $A$, one possible DFS traversal is:

```text
A → B → D → E → C
```

The exact order can depend on the order in which neighbors are visited.

The basic algorithm is:

```text
1. Start at a node.
2. Mark the node as visited.
3. Visit an unvisited neighbor.
4. Continue recursively until no unvisited neighbor remains.
5. Backtrack and continue with other neighbors.
```

## Recursive DFS

A recursive implementation follows the structure:

```text
DFS(node):
    mark node as visited

    for each neighbor:
        if neighbor is not visited:
            DFS(neighbor)
```

The **call stack** implicitly stores the path being explored.

## Iterative DFS

DFS can also use an explicit stack:

```text
Stack: [A]

Pop A
Push B, C

Pop C
...

Pop B
Push D, E
```

The stack follows **Last In, First Out (LIFO)** behavior.

## Complexity

For a graph with $V$ vertices and $E$ edges:

$$
O(|V|+|E|)
$$

The space complexity is:

$$
O(|V|)
$$

because the visited set and stack can contain up to all vertices.

## Applications

DFS is commonly used for:

* Finding connected components
* Detecting cycles
* Topological sorting
* Path finding
* Maze solving
* Backtracking algorithms
* Traversing trees and graphs

## DFS vs. BFS

|                            | DFS                    | BFS               |
| -------------------------- | ---------------------- | ----------------- |
| Strategy                   | Go as deep as possible | Level by level    |
| Main structure             | Stack / recursion      | Queue             |
| Shortest path (unweighted) | Not necessarily        | Yes               |
| Typical use                | Backtracking, cycles   | Distances, levels |

## Summary

**Depth-First Search** explores a graph by following a path as deeply as possible before **backtracking**.

Its main characteristics are:

* Uses a **stack** or recursion
* Explores deeply before exploring alternatives
* Runs in $O(|V|+|E|)$ time
* Useful for traversal, cycle detection, and backtracking
