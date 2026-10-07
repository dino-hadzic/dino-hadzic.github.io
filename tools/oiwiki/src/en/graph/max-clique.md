---
title: Maximum clique search algorithms
---

Prerequisites: [clique](./concept.md)

## Introduction

In computer science, the clique problem refers to the computational problem of finding a clique (a subset of vertices that are all pairwise adjacent, also called a complete subgraph) in a given graph.

The clique problem also appears in real life. For example, consider a social network where the vertices of the graph represent users and an edge means that the two connected users know each other. Then once we find a clique, we have found a group of people who all know each other.

If we want to find the largest group of mutually acquainted people in this social network, we need a maximum clique search algorithm.

We have already introduced the concept of a [maximal clique](./concept.md); a maximum clique is a maximal clique with the largest number of vertices.

## Explanation

The idea is to use recursion and backtracking: store the vertices in a list, and every time a vertex is added, check whether the chosen vertices still form a clique. If adding the vertex breaks the clique, backtrack to a position that satisfies the condition and try adding a different vertex.

The reason for backtracking is that we do not know whether some vertex $v$ is **ultimately** a member of the maximum clique. If the recursive algorithm picks $v$ as a member of the maximum clique and fails to find the maximum clique, it should backtrack and look for a solution without $v$.

## Procedure

The **Bron–Kerbosch** algorithm is an optimized implementation of this idea. Its basic form searches recursively using three given sets $R$, $P$, $X$. The steps are as follows:

1.  Initialize the sets $R,X$ to be empty and the set $P$ to be the set of all vertices of the graph.
2.  Each time, take a vertex $v$ from the set $P$; when the set has no vertices left, there are two cases:
    1.  the set $R$ is a maximal clique, and the set $X$ is empty,
    2.  there is no maximal clique, so we backtrack.
3.  For every vertex $v$ taken from the set $P$, do the following:
    1.  add the vertex $v$ to the set $R$, then recurse on the sets $R,P,X$,
    2.  delete the vertex $v$ from the set $P$ and add the vertex $v$ to the set $X$,
    3.  if the sets $P,X$ are both empty, the set $R$ is a maximal clique.

This method can be optimized further. To save time and let the algorithm backtrack faster, the search can be guided by a pivot vertex. Another optimization is to sort all vertices at the beginning and enumerate them in index order to avoid repetition.

## Implementation

### Pseudocode

```text
R := {}
P := node set of G 
X := {}

BronKerbosch1(R, P, X):
    if P and X are both empty:
        report R as a maximal clique
    for each vertex v in P:
        BronKerbosch1(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
        P := P \ {v}
        X := X ⋃ {v}
```

### C++ implementation

??? note "Implementation code"
    ```cpp
    --8<-- "docs/graph/code/max-clique/max-clique_1.cpp"
    ```

## Example problem

???+ note "[POJ 2989: All Friends](http://poj.org/problem?id=2989)"
    Problem summary: given $n$ people among whom there are $m$ pairs of friends, find the number of maximal cliques.

Idea: a template problem for the Bron–Kerbosch algorithm.

Pseudocode:

```text
 BronKerbosch(All, Some, None):  
     if Some and None are both empty:  
         report All as a maximal clique // all vertices chosen and no forbidden vertices left, increase the answer  
     for each vertex v in Some: // enumerate every element of Some  
         BronKerbosch1(All ⋃ {v}, Some ⋂ N(v), None ⋂ N(v))   
         // add v to All; clearly only friends of v can be candidates, and only friends of v in None affect what follows  
         Some := Some - {v} // already searched, remove from Some and add to None  
         None := None ⋃ {v} 
```

To save time and let the algorithm backtrack faster, we can optimize by choosing a pivot vertex $v$.

We know that the algorithm above necessarily recomputes many previously found maximal cliques before backtracking.

Take the sets $R$, $P$, $X$ mentioned above as an example:

Consider the following: if we take a vertex $u$ from the set $P\cup X$, then to form a maximal clique together with $R$, the chosen vertex must be a vertex of $P\cap N(u)$ ($N(u)$ denotes the set of vertices adjacent to $u$).

If after taking $u$ we can also add its neighbor $v$ to the maximal clique, then it suffices to take only $u$. This reduces the repeated computation for $v$ later. Afterwards we only need to take vertices not adjacent to $u$.

C++ implementation with this optimization:

??? note "Implementation code"
    ```cpp
    --8<-- "docs/graph/code/max-clique/max-clique_2.cpp"
    ```

## Exercises

-   [ZOJ 1492 Maximum Clique](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?page=4&problemSetProblemId=91827364991)
-   [POJ 1419 Maximum clique of an undirected graph](http://poj.org/problem?id=1419)
-   [POJ 1129 Channel Allocation](http://poj.org/problem?id=1129)

## References

-   [Clique problem – Wikipedia](https://en.wikipedia.org/wiki/Clique_problem)
-   [Maximal and maximum cliques of an undirected graph (Bron–Kerbosch algorithm)](https://blog.csdn.net/yo_bc/article/details/77453478)
-   [The maximum clique problem – Bron–Kerbosch algorithm](https://hallelujahjeff.github.io/2018/04/12/34/)
-   [The maximum clique problem](https://www.cnblogs.com/zhj5chengfeng/archive/2013/07/29/3224092.html)
