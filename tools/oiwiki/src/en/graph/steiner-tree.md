---
title: Steiner tree
---

The Steiner tree problem is a combinatorial optimization problem, similar to the minimum spanning tree, and one of the shortest network problems. The minimum spanning tree looks, within a given set of vertices and edges, for the shortest network connecting all vertices. The minimum Steiner tree allows adding extra vertices beyond the given ones so that the resulting shortest network has minimum cost.

## Motivation

In the early 19th century Steiner, a famous geometer at the University of Berlin, studied a very simple but instructive problem: connect three villages by roads of minimum total length. Mathematically, given three points $A$, $B$, $C$ in the plane, find a fourth point $P$ in the plane such that the sum $a+b+c$ is minimal, where $a$, $b$, $c$ denote the distances from $P$ to $A$, $B$, $C$.

The answer is: if every interior angle of triangle $\textit{ABC}$ is less than $120^{\circ}$, then $P$ is the point at which the sides $\textit{AB}$, $\textit{BC}$, $\textit{AC}$ each subtend an angle of $120^{\circ}$. If triangle $\textit{ABC}$ has an angle, say angle $C$, greater than or equal to $120^{\circ}$, then point $P$ coincides with vertex $C$.

### Generalizations

1.  In Steiner's problem three fixed points $A,B,C$ are given. It is natural to generalize to $n$ given points $A_1,A_2,\dots,A_n$: we look for a point $P$ in the plane such that the sum of distances $a_1+a_2+\dots+a_n$ is minimal, where $a_i$ is the distance $PA_i$.

2.  Taking other factors related to the points into account, weights are introduced. The other factors of the $n$ points can be converted into weights; we look for a point $P$ in the plane such that the sum of products of distances and weights $a_1\cdot w_1+a_2\cdot w_2+\dots+a_n\cdot w_n$ is minimal, where $w_i$ is the weight of each point.

3.  Courant (R. Courant) and Robbins (H. Robbins) pointed out that the first generalization is superficial. To obtain a truly valuable generalization of Steiner's problem, one must give up looking for a single point $P$ and instead look for a "road network" of minimum total length. Mathematically: given $n$ points $A_1,A_2,\cdots,A_n$, find a system of straight segments of minimum total length connecting these $n$ points such that any two points are connected by a polyline made of segments of the system. They called this new problem the **Steiner tree problem**. For $n$ given points there are at most $n-2$ additional junction points (Steiner points). At most three edges pass through each Steiner point. If there are three, they pairwise meet at angles of $120^{\circ}$; if there are two, then the Steiner point must be one of the given points, and the angle between the two edges is greater than or equal to $120^{\circ}$.

Shortest network connecting more than three points

![steiner-tree1](./images/steiner-tree-1.svg)

In the first case the solution consists of five segments with two Steiner points (red $s_1,s_2$), where three segments meet at mutual angles of $120^{\circ}$. The solution in the second case contains three Steiner points. In the third case one or more Steiner points may degenerate, i.e. be replaced by one or more of the given points.

We present the Steiner tree problem model in graph-theoretic form.

![steiner-tree2](./images/steiner-tree-2.svg)

In the first form, if the key vertices are $\{1,2,3,4\}$, we see that the minimum edge weight sum when connecting these four key vertices directly is 12, which is clearly not optimal. If we consider using vertex 5, the minimum edge weight sum becomes 9, a better answer.

In the second form, if the key vertices are $\{1,2,3,4\}$, we see that some of these key vertices do not even have a direct edge between them, so junction points (Steiner points) must be used. Including vertex 5 gives the minimum edge weight sum 9.

We also notice that in both pictures the Steiner points at vertices 1 and 4 are degenerate, replaced by vertices 1 and 4.

## Examples

First, a template problem to get familiar with the minimum Steiner tree problem. See [\[Template\] Minimum Steiner Tree](https://www.luogu.com.cn/problem/P6192).

The statement is clear: in a connected graph $G$ with $n$ vertices, $k$ key vertices are given; connect the $k$ key vertices so that the sum of weights of all edges of the resulting tree is minimal.

From the above we know that the weight sum when connecting these $k$ key vertices directly is not necessarily minimal, or that the $k$ key vertices are not directly (adjacently) connected at all. So the remaining $n-k$ vertices should be used.

We solve it with bitmask dynamic programming. Let $f(i,S)$ denote the minimum edge weight sum of a tree rooted at $i$ that contains all vertices of the set $S$.

State transitions:

-   First transition over connected subsets: $f(i,S)\leftarrow \min(f(i,S),f(i,T)+f(i,S-T))$.

-   Then, for the current connectivity state of the subset, relax along edges: $f(i,S)\leftarrow \min(f(i,S),f(j,S)+w(j,i))$. In the code below, `tree[tot]` records the information about two adjacent vertices $i,j$.

??? note "Reference implementation"
    ```cpp
    --8<-- "docs/graph/code/steiner-tree/steiner-tree_1.cpp"
    ```

Another classic example: [\[WC2008\] Sightseeing Plan](https://www.luogu.com.cn/problem/P4294).

This problem asks for the Steiner tree with minimum vertex weight sum; $f(i,S)$ denotes the minimum vertex weight sum of a tree rooted at $i$ that contains all vertices of the set $S$, and $a_i$ is the vertex weight.

State transitions:

-   $f(i,S)\leftarrow \min(f(i,S),f(i,T)+f(i,S-T)-a_i)$. When merging, the weight $a_i$ of the same vertex would be added twice, so we subtract it.

-   $f(i,S)\leftarrow \min(f(i,S),f(j,S)+w(j,i))$.

The transitions are similar to those of the template problem above; the troublesome part is printing the answer, since the path has to be recorded during the DP.

`pre[i][s]` records the vertex and set from which the state with root $i$ and connectivity set $s$ was reached. After the DP, starting from `pre[root][S]`, we look for the vertices connected to those in the set and gradually decompose the set $S$; the ans array records the vertices used, and the search ends when the set has been fully decomposed.

??? note "Reference implementation"
    ```cpp
    --8<-- "docs/graph/code/steiner-tree/steiner-tree_2.cpp"
    ```

## Exercises

-   [\[Template\] Minimum Steiner Tree](https://www.luogu.com.cn/problem/P6192)
-   [\[WC2008\] Sightseeing Plan](https://www.luogu.com.cn/problem/P4294)
-   [\[JLOI2015\] Pipeline Connection](https://loj.ac/problem/2110)
-   [\[APIO2013\] Robots](https://www.luogu.com.cn/problem/P3638)
