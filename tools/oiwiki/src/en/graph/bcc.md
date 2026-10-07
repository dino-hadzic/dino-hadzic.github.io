---
title: Biconnected components
---

## Introduction

Before reading the following, make sure you are familiar with [graph theory concepts](./concept.md).

Related reading: [Cut vertices and bridges](./cut.md)

## Definition

For more rigorous definitions of cut vertices and bridges see [Graph theory concepts](./concept.md).

In a connected undirected graph, for two vertices $u$ and $v$, if deleting any single edge (only one may be deleted) cannot disconnect them, we say $u$ and $v$ are **edge-biconnected**.

In a connected undirected graph, for two vertices $u$ and $v$, if deleting any single vertex (only one may be deleted, and not $u$ or $v$ themselves) cannot disconnect them, we say $u$ and $v$ are **vertex-biconnected**.

Edge-biconnectivity is transitive: if $x,y$ are edge-biconnected and $y,z$ are edge-biconnected, then $x,z$ are edge-biconnected.

Vertex-biconnectivity is **not** transitive; a counterexample is shown below: $A,B$ are vertex-biconnected, $B,C$ are vertex-biconnected, but $A,C$ are **not** vertex-biconnected.

![bcc-counterexample.png](./images/bcc-0.svg)

A **maximal** edge-biconnected subgraph of an undirected graph is called an **edge-biconnected component**.

A **maximal** vertex-biconnected subgraph of an undirected graph is called a **vertex-biconnected component**.

## DFS spanning tree

For a connected undirected graph we can start a DFS from any vertex and obtain a DFS spanning tree of the original graph (rooted at the vertex where the DFS started). The edges of this spanning tree are called **tree edges**, and the edges not in the spanning tree are called **non-tree edges**.

Because of the properties of DFS, we can guarantee that for every non-tree edge, one of its two endpoints is an ancestor of the other in the spanning tree.

The DFS code is as follows:

???+ note "Implementation"
    === "C++"
        ```cpp
        void DFS(int p) {
          visited[p] = true;
          for (int to : edge[p])
            if (!visited[to]) DFS(to);
        }
        ```
    
    === "Python"
        ```python
        def DFS(p):
            visited[p] = True
            for to in edge[p]:
                if visited[to] == False:
                    DFS(to)
        ```

## Edge-biconnected components

???+ note "[Example: Luogu P8436 \[Template\] Edge-Biconnected Components](https://www.luogu.com.cn/problem/P8436)"
    For a graph with $n$ vertices and $m$ undirected edges, output the number of its edge-biconnected components and each edge-biconnected component.

### Tarjan's algorithm 1

Finding biconnected components with Tarjan's algorithm is similar to finding strongly connected components; you may first read Tarjan's algorithm in [Strongly connected components](./scc.md).

We first find all bridges, then find the edge-biconnected components with a DFS.

For finding bridges see the bridge part of [Cut vertices and bridges](./cut.md).

Time complexity $O(n+m)$.

??? note "Sample code"
    ```cpp
    --8<-- "docs/graph/code/bcc/bcc_1.cpp"
    ```

### Tarjan's algorithm 2

Let us first summarize an important property: in an undirected graph, with respect to the DFS spanning tree an edge is either a tree edge or a non-tree edge.

Relating this to the method for strongly connected components: in an undirected graph, as soon as a component has no bridges, all its vertices are in the same strongly connected component in the DFS spanning tree.

Conversely, a strongly connected component in the DFS spanning tree is an edge-biconnected component in the original undirected graph.

We see that the process of finding edge-biconnected components is in fact the process of finding strongly connected components.

Time complexity $O(n+m)$.

??? note "Sample code"
    ```cpp
    --8<-- "docs/graph/code/bcc/bcc_2.cpp"
    ```

### Difference-array algorithm

Similar to Tarjan's algorithm 1, we first find all bridges, then find the edge-biconnected components with a difference array.

First, run a DFS on the original graph.

![bcc-1.png](./images/bcc-1.svg)

As shown above, the black and green edges are tree edges, the red edges are non-tree edges. The two endpoints of every non-tree edge uniquely correspond to a simple path in the tree made of tree edges; we say that this non-tree edge **covers** all edges on that simple path.

In the picture, each green tree edge is covered by **at least** one non-tree edge, while the black tree edges are not covered by **any** non-tree edge.

Clearly, **non-tree edges** and **green tree edges** are never bridges, and **black tree edges** are always bridges.

Consider a brute-force approach first: for every non-tree edge, color every tree edge it covers green one by one; the time complexity is $O(nm)$.

Optimize with a difference array. For every non-tree edge, put a `-1` mark at its endpoint of smaller depth in the tree and a `+1` mark at its endpoint of larger depth, then compute the sum of marks inside the subtree of every vertex in $O(n)$.

For a vertex $u$, the sum of marks inside its subtree equals the number of non-tree edges covering the tree edge between $u$ and $fa_u$. If this value is $0$, the tree edge between $u$ and $fa_u$ is a **bridge**.

Then find the edge-biconnected components with a DFS.

Time complexity $O(n+m)$.

??? note "Sample code"
    ```cpp
    --8<-- "docs/graph/code/bcc/bcc_4.cpp"
    ```

???+ note "[#2788. 「CEOI2015 Day1」Pipes](https://loj.ac/p/2788)"
    Given an undirected graph with $N$ vertices and $M$ edges, not guaranteed to be connected. Treat each connected component as a subgraph and find the bridges in every subgraph. **You only have 16 MB of memory.**

??? note "Solution"
    The main feature of this problem is that you cannot store all the edges.
    
    Optimize edge storage: if a non-tree edge is completely covered by another non-tree edge, this edge is useless.
    
    Maintain this with a DSU.

## Vertex-biconnected components

???+ note "[Example: Luogu P8435 \[Template\] Vertex-Biconnected Components](https://www.luogu.com.cn/problem/P8435)"
    For a graph with $n$ vertices and $m$ undirected edges, output the number of its vertex-biconnected components and each vertex-biconnected component.

### Tarjan's algorithm

Cut vertices must be learned first; see the cut vertex part of [Cut vertices and bridges](./cut.md).

First, two properties:

1.  Two vertex-biconnected components share at most one vertex, and it must be a cut vertex.
2.  For a vertex-biconnected component, its vertex with the smallest dfn in the DFS search tree must be a cut vertex or the root of the tree.

Based on the second property, we distinguish cases:

1.  When this vertex is a cut vertex, it must be the root of the vertex-biconnected component, because as soon as its parent were included it would still be a cut vertex.
2.  When this vertex is the root of the tree:
    1.  it has two or more subtrees: it is a cut vertex;
    2.  it has only one subtree: it is the root of a vertex-biconnected component;
    3.  it has no subtree: it is regarded as a vertex-biconnected component by itself.

??? note "Sample code"
    ```cpp
    --8<-- "docs/graph/code/bcc/bcc_3.cpp"
    ```

### Difference-array algorithm

![bcc-2.png](./images/bcc-2.svg)

As shown above, the black edges are tree edges and the red edges are non-tree edges; the two endpoints of every non-tree edge uniquely correspond to a simple path in the tree made of tree edges.

Consider a new graph in which every vertex corresponds to a tree edge of the original graph (shown as blue vertices in the picture). For every non-tree edge of the original graph, connect the blue vertices corresponding to all edges on the tree path of that non-tree edge into one connected component (shown with blue edges in the picture).

Then a vertex is **not** a cut vertex if and only if the blue vertices corresponding to all edges incident to it **belong** to the same connected component in the new graph.

Two vertices **are** vertex-biconnected if and only if the blue vertices corresponding to all edges on their tree path in the original graph **belong** to the same connected component; that is, every connected component of blue vertices in the picture is a vertex-biconnected component.

The connectivity between blue vertices can be maintained with a method similar to the difference array used for edge-biconnected components; time complexity $O(n+m)$.
