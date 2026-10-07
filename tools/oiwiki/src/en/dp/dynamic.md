---
title: Dynamic DP
---

Prerequisites: [Matrices](../math/linear-algebra/matrix.md), [Heavy-light decomposition](../graph/hld.md).

Dynamic DP is a technique presented by "猫锟" at WC2018; it is generally used to solve DP problems on trees with point-update operations on vertex (edge) weights.

## Example

We explain the process of dynamic DP using this template problem as an example.

???+ note "Example [Luogu P4719 [Template] Dynamic DP](https://www.luogu.com.cn/problem/P4719)"
    Given a tree with $n$ vertices, each vertex has a weight. There are $m$ operations; each operation gives $x,y$ and sets the weight of vertex $x$ to $y$. After each operation you must output the weight of the maximum weight independent set of the tree.

### Generalized matrix multiplication

Define the generalized matrix multiplication $A\times B=C$ as:

$$
C_{i,j}=\max_{k=1}^{n}(A_{i,k}+B_{k,j})
$$

This is ordinary matrix multiplication with multiplication replaced by addition and addition replaced by the $\max$ operation.

Generalized matrix multiplication is also associative, so fast matrix exponentiation can be used.

### Without update operations

Let $f_{i,0}$ denote the best answer when $i$ is not chosen and $f_{i,1}$ the best answer when $i$ is chosen.

The DP equation is:

$$
\begin{cases}f_{i,0}=\sum_{son}\max(f_{son,0},f_{son,1})\\f_{i,1}=w_i+\sum_{son}f_{son,0}\end{cases}
$$

The answer is $\max(f_{root,0},f_{root,1})$.

### With update operations

First perform heavy-light decomposition on the tree; suppose we have a heavy chain like this:

![](./images/dynamic.png)

Let $g_{i,0}$ denote the best answer when $i$ is not chosen and only vertices in the subtrees of the light children of $i$ may be chosen, and $g_{i,1}$ the best answer when $i$ is chosen, ignoring $son_i$; $son_i$ denotes the heavy child of $i$.

Assuming $g_{i,0/1}$ are known, the DP equation is:

$$
\begin{cases}f_{i,0}=g_{i,0}+\max(f_{son_i,0},f_{son_i,1})\\f_{i,1}=g_{i,1}+f_{son_i,0}\end{cases}
$$

The answer is $\max(f_{root,0},f_{root,1})$.

We can construct the matrix:

$$
\begin{bmatrix}
g_{i,0} & g_{i,0}\\
g_{i,1} & -\infty
\end{bmatrix}\times 
\begin{bmatrix}
f_{son_i,0}\\f_{son_i,1}
\end{bmatrix}=
\begin{bmatrix}
f_{i,0}\\f_{i,1}
\end{bmatrix}
$$

Note that we use the generalized multiplication rule here.

Observe that an update only requires modifying $g_{i,1}$ and every heavy chain on the way up.

### Concrete approach

1.  Preprocess $f_{i,0/1}$ and $g_{i,0/1}$ with a DFS.

2.  Perform heavy-light decomposition on the tree (note: since a query on a vertex requires the interval matrix product from that vertex to the end of its heavy chain, record $End_i$ for every vertex, the index of the last vertex of the heavy chain containing $i$); build a segment tree for each heavy chain, maintaining the $g$ matrices and the interval products of $g$ matrices.

3.  For an update, first modify $g_{i,1}$ and the matrix of node $i$ in the segment tree, compute the change of the matrix of $top_i$, and apply it to the matrix of $fa_{top_i}$.

4.  A query is the interval product from vertex 1 to the end of its heavy chain; finally take the $\max$.

??? note "Implementation"
    ```cpp
    --8<-- "docs/dp/code/dynamic/dynamic_1.cpp"
    ```

## Exercises

-   [SPOJ GSS3 - Can you answer these queries III](https://www.spoj.com/problems/GSS3/)
-   ["NOIP2018" Defending the Kingdom](https://loj.ac/p/2955)
-   ["SDOI2017" Tree Cutting Game](https://loj.ac/p/2269)
