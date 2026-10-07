---
title: Tree diameter
---

The longest simple path between any two nodes of a tree is called the "diameter" of the tree.

Prerequisites: [Tree basics](./tree-basic.md).

## Introduction

Obviously, a tree may have several diameters, and they all have the same length.

The diameter of a tree can be found in $O(n)$ time with two DFS runs or with tree DP.

## Two DFS runs

First start a DFS from an arbitrary node $y$ and reach the node farthest from it, denoted $z$; then start a second DFS from $z$ and reach the node farthest from $z$, denoted $z'$. Then $\delta(z,z')$ is the diameter of the tree.

Obviously, if the node $z$ reached by the first DFS is an endpoint of a diameter, then the node $z'$ reached by the second DFS must be an endpoint of a diameter. We only need to prove that in every case $z$ is an endpoint of a diameter.

Theorem: in a tree, if a DFS is started from an arbitrary node $y$, the farthest node $z$ reached must be an endpoint of a diameter.

???+ note "Proof"
    By contradiction. Let the start node be $y$. Let the true diameter be $\delta(s,t)$, and suppose the node $z$ reached by the first DFS from $y$ as the farthest one is neither $t$ nor $s$. There are three cases:
    
    -   If $y$ lies on $\delta(s,t)$:
    
    ![y lies on s-t](./images/tree-diameter1.svg)
    
    We have $\delta(y,z) > \delta(y,t) \Longrightarrow \delta(x,z) > \delta(x,t) \Longrightarrow \delta(s,z) > \delta(s,t)$, contradicting the fact that $\delta(s,t)$ is the longest simple path between any two nodes of the tree.
    
    -   If $y$ does not lie on $\delta(s,t)$, and $\delta(y,z)$ and $\delta(s,t)$ share a common part:
    
    ![y not on s-t, y-z and s-t share a common part](./images/tree-diameter2.svg)
    
    We have $\delta(y,z) > \delta(y,t) \Longrightarrow \delta(x,z) > \delta(x,t) \Longrightarrow \delta(s,z) > \delta(s,t)$, contradicting the fact that $\delta(s,t)$ is the longest simple path between any two nodes of the tree.
    
    -   If $y$ does not lie on $\delta(s,t)$, and $\delta(y,z)$ and $\delta(s,t)$ do not share a common part:
    
    ![y not on s-t, y-z and s-t do not share a common part](./images/tree-diameter3.svg)
    
    We have $\delta(y,z) > \delta(y,t) \Longrightarrow \delta(x',z) > \delta(x',t) \Longrightarrow \delta(x,z) > \delta(x,t) \Longrightarrow \delta(s,z) > \delta(s,t)$, contradicting the fact that $\delta(s,t)$ is the longest simple path between any two nodes of the tree.
    
    In summary, the assumption leads to a contradiction in all three cases, so the theorem is proved.

???+ warning "Negative edge weights"
    The above proof relies on the premise that no path has negative length. If the tree contains edges with negative weights, the proof does not hold. Hence, if there are negative edges, the diameter cannot be found with the two-DFS method.

If all nodes on a diameter are needed, during the second DFS we can record the predecessor of every node; then we walk back from one endpoint of the diameter and visit all nodes on it.

## Tree DP

### Method 1

Taking $1$ as the root of the tree, for every node, as the root of its subtree, we record the length $d_1$ of the longest downward path and the length $d_2$ of the second longest downward path (sharing no edge with the longest one). The diameter is then the maximum value of $d_1 + d_2$ over all nodes.

Tree DP can find the diameter of a tree even when negative edge weights exist.

If all nodes on a diameter are needed, during the DP we can record, for every node, the child corresponding to the longest and to the second longest downward path (defined as above); while computing $d$, remember the node $u$ with $d = d_1[u] + d_2[u]$. Then, starting from $u$, follow the children corresponding to the longest and the second longest path in one direction (for an unrooted tree, although $1$ was chosen as the root here, the direction of each jump still has to be recorded; for a rooted tree it suffices to go upward), visiting all nodes on the diameter.

### Method 2

Here we give a tree DP method that uses only one array.

Define $dp[u]$ as the longest path starting from $u$ within the subtree rooted at $u$. The transition follows easily: $dp[u] = \max(dp[u], dp[v] + w(u, v))$, where $v$ is a child of $u$ and $w(u, v)$ is the weight of the traversed edge.

The diameter of the tree can actually be obtained by enumerating the maximum sum of two different paths starting from some node. Therefore, during the DP, before updating $dp[u]$ we just compute $d = \max(d, dp[u] + dp[v] + w(u, v))$, which yields the diameter $d$.

## Example problem

???+ example "[Luogu B4016 Tree diameter](https://www.luogu.com.cn/problem/B4016)"
    Given a tree with $n$ nodes, find the length of its diameter. $1\leq n\leq 10^5$.

??? note "Reference implementation with two DFS runs"
    ```cpp
    --8<-- "docs/graph/code/tree-diameter/tree-diameter_1.cpp"
    ```

??? note "Reference implementation with tree DP using two arrays"
    ```cpp
    --8<-- "docs/graph/code/tree-diameter/tree-diameter_2.cpp"
    ```

??? note "Reference implementation with tree DP using one array"
    ```cpp
    --8<-- "docs/graph/code/tree-diameter/tree-diameter_3.cpp"
    ```

## Properties

The diameter of a tree has the following property: if all edge weights in the tree are positive, the midpoints of all diameters of the tree coincide.

???+ note "Proof"
    Proof: by contradiction. Let two diameters with different midpoints be $\delta(s,t)$ and $\delta(s',t')$, with midpoints $x$ and $x'$ respectively. Obviously $\delta(s,x) = \delta(x,t) = \delta(s',x') = \delta(x',t')$.
    
    ![the midpoints of all diameters of a tree without negative edges coincide](./images/tree-diameter4.svg)
    
    We have $\delta(s,t') = \delta(s,x) + \delta(x,x') + \delta(x',t') > \delta(s,x) + \delta(x,t) = \delta(s,t)$, contradicting the fact that $\delta(s,t)$ is the longest simple path between any two nodes of the tree, so the property is proved.

## Exercises

-   [CodeChef, Diameter of Tree](https://www.codechef.com/problems/DTREE)
-   [Educational Codeforces Round 35, Problem F, Tree Destruction](https://codeforces.com/contest/911/problem/F)
-   [ZOJ 3820 Building Fire Stations](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?problemSetProblemId=91827369872&page=28)
-   [CEOI2019/CodeForces 1192B. Dynamic Diameter](https://codeforces.com/contest/1192/problem/B)
-   [ICPC 2019 Shanghai online contest, Lightning Routing I](https://vjudge.net/problem/%E8%AE%A1%E8%92%9C%E5%AE%A2-A2290)
-   [NOIP2007 senior, Core of a Tree Network](https://www.luogu.com.cn/problem/P1099)
-   [SDOI2011 Fire Brigade](https://www.luogu.com.cn/problem/P2491)
-   [APIO2010 Patrol](https://www.luogu.com.cn/problem/P3629)
