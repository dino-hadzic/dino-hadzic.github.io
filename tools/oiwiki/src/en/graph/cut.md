---
title: Cut vertices and bridges
---

Related reading: [Biconnected components](./bcc.md)

For more rigorous definitions of cut vertices and bridges see [Graph theory concepts](./concept.md).

## Cut vertices

> In an undirected graph, if deleting a vertex increases the number of maximal connected components of the graph, then that vertex is a cut vertex (also called an articulation point) of the graph.

### Procedure

If we tried deleting every vertex and checking the connectivity of the graph, the complexity would be very high. So we introduce a commonly used algorithm: Tarjan's.

First, a graph:

![](./images/cut1.svg)

It is easy to see that the cut vertex is 2, and that this graph has only this one cut vertex.

First, we assign timestamps to the vertices in DFS order (the order of visiting).

![](./images/cut2.svg)

We store this information in an array called `dfn`.

We also need another array, `low`, which stores the smallest timestamp reachable without going through the parent.

For example, `low[2]` is 1, and `low[5]` and `low[6]` are 3.

Then we start the DFS. The criterion for deciding whether a vertex is a cut vertex is: for a vertex $u$, if there exists at least one vertex $v$ (a child of $u$) such that $low_v \geq dfn_u$, i.e. it cannot get back to an ancestor, then $u$ is a cut vertex.

This criterion does not apply only to the starting vertex of the search, which needs special consideration: if that vertex is not a cut vertex, then all vertices are reachable via other paths as well, so from the starting vertex we "search downwards only once", i.e. it has only one child in the search tree. If it has two or more children in the search tree, it must be a cut vertex (imagine starting the search from 2 in the picture above: there would be two children in the search tree, 3 or 4, and 5 or 6). If it has only one child, deleting it has no effect at all. For example, in the following graph a cycle is formed.

![](./images/cut3.svg)

When visiting the children of 1, suppose the DFS first reaches 2, marks it as visited, then recurses downwards to 4, and 4 goes on to 3; when the recursion backtracks, we find that 3 has already been visited, so 1 is not a cut vertex.

The pseudocode for updating `low` is as follows:

$$
\begin{array}{ll}
1 & \textbf{if } v \text{ is a son of } u \\
2 & \qquad \text{low}_u = \min(\text{low}_u, \text{low}_v) \\
3 & \textbf{else} \\
4 & \qquad \text{low}_u = \min(\text{low}_u, \text{dfn}_v) \\
\end{array}
$$

### Example

[Luogu P3388 \[Template\] Cut Vertices (Articulation Points)](https://www.luogu.com.cn/problem/P3388)

??? note "Example code"
    ```cpp
    --8<-- "docs/graph/code/cut/cut_1.cpp"
    ```

## Cut edges (without multi-edges)

Similar to cut vertices; they are called bridges.

> In an undirected graph, if deleting an edge increases the number of connected components of the graph, that edge is called a bridge or cut edge. Rigorously: let $G=\{V,E\}$ be a connected graph and $e$ one of its edges (i.e. $e \in E$); if $G-e$ is disconnected, then the edge $e$ is a cut edge (bridge) of the graph $G$.

For example, in the graph below,

![cut edge example](./images/bridge1.svg)

the red edge is a cut edge.

### Procedure

Almost the same as for cut vertices, with only one change: $low_v>dfn_u$ suffices, and the root case does not need to be considered.

Cut edges have nothing to do with whether a vertex is the root. When we computed cut vertices, the condition meant that vertex $v$ cannot get back to an ancestor (including the parent) without going through the parent $u$, so vertex $u$ is a cut vertex. If $low_v=dfn_u$, it means $v$ can still get back to the parent; if vertex $v$ cannot get back to an ancestor and there is no other way back to the parent either, then the edge $u-v$ is a cut edge.

### Implementation

The following code finds the cut edges of an undirected graph **without multi-edges**; when `isbridge[x]` is true, `(father[x],x)` is a cut edge.

=== "C++"
    ```cpp
    int low[MAXN], dfn[MAXN], idx;
    bool isbridge[MAXN];
    vector<int> G[MAXN];
    int cnt_bridge;
    int father[MAXN];
    
    void tarjan(int u, int fa) {
      father[u] = fa;
      low[u] = dfn[u] = ++idx;
      for (const auto &v : G[u]) {
        if (!dfn[v]) {
          tarjan(v, u);
          low[u] = min(low[u], low[v]);
          if (low[v] > dfn[u]) {
            isbridge[v] = true;
            ++cnt_bridge;
          }
        } else if (v != fa) {
          low[u] = min(low[u], dfn[v]);
        }
      }
    }
    ```

=== "Python"
    ```python
    low = [0] * MAXN
    dfn = [0] * MAXN
    idx = 0
    isbridge = [False] * MAXN
    G = [[0 for i in range(MAXN)] for j in range(MAXN)]
    cnt_bridge = 0
    father = [0] * MAXN
    
    
    def tarjan(u, fa):
        father[u] = fa
        idx = idx + 1
        low[u] = dfn[u] = idx
        for i in range(0, len(G[u])):
            v = G[u][i]
            if dfn[v] == False:
                tarjan(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > dfn[u]:
                    isbridge[v] = True
                    cnt_bridge = cnt_bridge + 1
            elif v != fa:
                low[u] = min(low[u], dfn[v])
    ```

## Cut edges (with multi-edges)

However, the approach above for graphs without multi-edges is wrong on undirected graphs with multi-edges.

There may be more than one edge between two vertices, in which case none of them is a bridge.

### Procedure

One idea is to replace the parameter `fa` with the index of the edge we just came through (both directions of an edge share the same index), i.e. to replace "do not update via the parent" with "do not update via the edge we came from".

Another, simpler idea is to set a flag indicating whether one edge to the parent has already been used; after the flag is set, the next time the parent is encountered we update normally.

The following code finds the cut edges of an undirected graph that **may have multi-edges**.

=== "C++"
    ```cpp
    int low[MAXN], dfn[MAXN], idx;
    bool isbridge[MAXN];
    vector<int> G[MAXN];
    int cnt_bridge;
    int father[MAXN];
    
    void tarjan(int u, int fa) {
      bool flag = false;
      father[u] = fa;
      low[u] = dfn[u] = ++idx;
      for (const auto &v : G[u]) {
        if (!dfn[v]) {
          tarjan(v, u);
          low[u] = min(low[u], low[v]);
          if (low[v] > dfn[u]) {
            isbridge[v] = true;
            ++cnt_bridge;
          }
        } else {
          if (v != fa || flag)
            low[u] = min(low[u], dfn[v]);
          else
            flag = true;
        }
      }
    }
    ```

## Exercises

-   [P3388 \[Template\] Cut Vertices (Articulation Points)](https://www.luogu.com.cn/problem/P3388)
-   [POJ2117 Electricity](http://poj.org/problem?id=2117)
-   [HDU4738 Caocao's Bridges](https://acm.hdu.edu.cn/showproblem.php?pid=4738)
-   [HDU2460 Network](https://acm.hdu.edu.cn/showproblem.php?pid=2460)
-   [POJ1523 SPF](http://poj.org/problem?id=1523)

Tarjan's algorithm has many other uses; it is commonly used to find strongly connected components, to contract components, to solve 2-SAT, and so on.
