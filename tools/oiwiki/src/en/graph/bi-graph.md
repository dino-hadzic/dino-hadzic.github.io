---
title: Bipartite graphs
---

## Introduction

A bipartite graph, also called a two-part graph, is a class of graphs with a special structure. Its vertex set can be partitioned into two disjoint subsets such that every edge of the graph connects a pair of vertices from different sets and never two vertices inside the same set.

Thanks to this simple structure, bipartite graphs not only exhibit many elegant properties but are also widely used to model real-world situations such as task assignment, recommendation systems, and matching markets. Many optimization problems that are hard on general graphs can be solved efficiently and exactly on bipartite graphs.

## Definition

If the vertex set $V$ of a graph $G=(V,E)$ can be split into two disjoint subsets $X$ and $Y$ such that the two endpoints of every edge $e\in E$ belong to $X$ and $Y$ respectively, the graph $G$ is called a **bipartite graph**. The sets $X$ and $Y$ are often called its two **parts**, or the left and right part of the bipartite graph. When the two parts $X$ and $Y$ are known, the bipartite graph $G$ can also be written as the triple $(X, Y, E)$.

A typical bipartite graph is shown below.

![](./images/bi-graph-1.svg)

Trees, even cycles, grid graphs, etc. are common examples of bipartite graphs.

## Characterization

Bipartite graphs can equivalently be defined by the following properties:

-   The graph $G$ is 2-colorable. That is, all vertices of the graph can be colored with at most two colors so that adjacent vertices have different colors.
-   The graph $G$ contains no cycle of odd length.

Clearly the first property is equivalent to the definition of a bipartite graph: just color each of the two parts with one color.

The second property is slightly more involved. Try to color the graph $G$ with two colors. Since the colorings of different connected components do not interfere with each other, it suffices to consider the components one by one. Pick any vertex $s$ in a component, run a DFS, and record for every vertex $v$ of the component its distance (i.e. depth) from $s$ in the DFS tree. By induction on the DFS tree starting from $s$, if a valid coloring exists, it must color each vertex $v$ with one of the two colors according to the parity of its distance to the starting vertex $s$.

![](./images/bi-graph-2.svg)

Next consider the edges that are not in the spanning tree. If the two endpoints of every such non-tree edge have different colors, the current coloring is valid; otherwise no valid coloring exists. Furthermore, two vertices have different colors if and only if their distances to the root $s$ have different parity, which is equivalent to the cycle formed by adding that non-tree edge being even rather than odd. Hence, as long as there is no odd cycle, the non-tree edges necessarily connect vertices of different colors, so the whole graph can be colored with two colors and the graph is certainly bipartite.

## Testing

To test whether a graph is bipartite, simply use the equivalent characterization above and try to color the graph. To do so, traverse the graph with [DFS](./dfs.md) or [BFS](./bfs.md). If an odd cycle is found, i.e. a situation where coloring is impossible, the graph is not bipartite; otherwise it is.

The concrete procedure is as follows:

-   Iterate over the vertices; when an uncolored vertex is found, a new connected component has been discovered.
-   Color that vertex with any color and run [DFS](./dfs.md) or [BFS](./bfs.md) from it, trying to color that connected component.
-   When visiting adjacent vertices, if an already colored vertex is found, check whether its color equals the color of the current vertex. If it does, the graph is not bipartite and we return immediately; otherwise continue the traversal.
-   If an uncolored vertex is found, color it with the color opposite to that of the current vertex.

Reference code:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/graph/code/bi-graph/check-bipartite.cpp:core"
    ```

The time complexity is $O(|V|+|E|)$.

## Applications

Because of their simple structure, many graph optimization problems can be solved efficiently on bipartite graphs. See the corresponding main articles for details.

-   maximum clique (trivial)
-   minimum vertex coloring (trivial)
-   [minimum edge coloring](./color.md#constructive-proof-of-vizings-theorem-for-bipartite-graphs)
-   [maximum matching](./graph-matching/bigraph-match.md)
-   [minimum edge cover](./graph-matching/graph-match.md#最小权边覆盖)
-   [minimum vertex cover](./graph-matching/bigraph-match.md#二分图最小点覆盖)
-   [maximum independent set](./graph-matching/bigraph-match.md#二分图最大独立集)
-   [maximum weight matching](./graph-matching/bigraph-weight-match.md)
-   [bipartite graph games](../math/game-theory/impartial-game.md#二分图博弈)
