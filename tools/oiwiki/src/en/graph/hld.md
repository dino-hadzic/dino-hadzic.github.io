---
title: Heavy-light decomposition (tree chain decomposition)
---

## Introduction

Tree chain decomposition is used to split a tree into a number of chains in order to maintain information about paths in the tree.

Concretely, the whole tree is decomposed into a number of chains so that it forms a linear structure, and then the information is maintained with other data structures.

**Tree chain decomposition** comes in several forms, such as **heavy-light decomposition** (heavy path decomposition), **long-path decomposition**, and the decomposition used in Link/cut Trees (sometimes called "preferred path decomposition"). In most cases (unless specified otherwise), "tree chain decomposition" refers to "heavy-light decomposition".

Heavy-light decomposition can split any path in a tree into at most $O(\log n)$ contiguous chains, where the depths of the nodes on each chain are pairwise distinct (i.e. each chain goes bottom-up, and the LCA of all nodes on the chain is one of its endpoints).

Heavy-light decomposition also guarantees that the DFS order of the nodes on every resulting chain is contiguous, so data structures for maintaining sequences (such as segment trees) can be conveniently used to maintain information about paths in the tree. For example:

1.  Modify the values of all nodes **on the path between two nodes of the tree**.
2.  Query the **sum/extremum/other information (that can be maintained with a data structure on a sequence and merged easily)** of the node weights **on the path between two nodes of the tree**.

Besides maintaining path information together with data structures, tree chain decomposition can also be used to compute the LCA in $O(\log n)$ (with a small constant factor). In some problems its properties can also be exploited in flexible ways.

## Heavy-light decomposition

We give some definitions:

The **heavy child** of a node is the child whose subtree is the largest among its children. If there are several children with the largest subtree, pick any one. If there are no children, there is no heavy child.

The **light children** are all the remaining children.

The edge from a node to its heavy child is a **heavy edge**.

The edges to the other, light children are **light edges**.

A number of heavy edges joined end to end form a **heavy chain**.

Treating isolated nodes as heavy chains as well, the whole tree is decomposed into a number of heavy chains.

As in the figure:

![HLD](./images/hld.png)

## Implementation

The implementation of the decomposition consists of two DFS passes. The pseudocode is as follows:

The first DFS records, for every node, its parent ($\textit{father}$), depth ($\textit{depth}$), subtree size ($\textit{size}$) and heavy child ($\textit{hson}$).

$$
\begin{array}{l}
\text{TREE-BUILD }(u,\textit{dep}) \\
\begin{array}{ll}
1 & u.\textit{hson}\gets 0 \\
2 & u.\textit{hson}.\textit{size}\gets 0 \\
3 & u.\textit{depth}\gets \textit{dep} \\
4 & u.\textit{size}\gets 1 \\
5 & \textbf{for }\text{each son }v\text{ of }u \\
6 & \qquad u.\textit{size}\gets u.\textit{size} + \text{TREE-BUILD }(v,\textit{dep}+1) \\
7 & \qquad v.\textit{father}\gets u \\
8 & \qquad \textbf{if }v.\textit{size}> u.\textit{hson}.\textit{size} \\
9 & \qquad \qquad u.\textit{hson}\gets v \\
10 & \textbf{return } u.\textit{size}
\end{array}
\end{array}
$$

The second DFS records the top of the chain the node belongs to ($\textit{top}$, which should be initialized to the node itself), the DFS order when traversing heavy edges first ($\textit{dfn}$), and the node index corresponding to each DFS index ($\textit{rank}$).

$$
\begin{array}{l}
\text{TREE-DECOMPOSITION }(u,\textit{top}) \\
\begin{array}{ll}
1 & u.\textit{top}\gets \textit{top} \\
2 & \textit{tot}\gets \textit{tot}+1\\
3 & u.\textit{dfn}\gets \textit{tot} \\
4 & \textit{rank}(\textit{tot})\gets u \\
5 & \textbf{if }u.\textit{hson}\text{ is not }0 \\
6 & \qquad \text{TREE-DECOMPOSITION }(u.\textit{hson},\textit{top}) \\
7 & \qquad \textbf{for }\text{each son }v\text{ of }u \\
8 & \qquad \qquad \textbf{if }v\text{ is not }u.\textit{hson} \\
9 & \qquad \qquad \qquad \text{TREE-DECOMPOSITION }(v,v) 
\end{array}
\end{array}
$$

The code implementation follows.

First some definitions:

-   $\operatorname{fa}(x)$ denotes the parent of node $x$ in the tree.
-   $\operatorname{dep}(x)$ denotes the depth of node $x$ in the tree.
-   $\operatorname{siz}(x)$ denotes the number of nodes in the subtree of node $x$.
-   $\operatorname{son}(x)$ denotes the **heavy child** of node $x$.
-   $\operatorname{top}(x)$ denotes the top node (of minimum depth) of the **heavy chain** containing node $x$.
-   $\operatorname{dfn}(x)$ denotes the **DFS index** of node $x$, which is also its index in the segment tree.
-   $\operatorname{rnk}(x)$ denotes the node index corresponding to a DFS index; we have $\operatorname{rnk}(\operatorname{dfn}(x))=x$.

We preprocess these values with two DFS passes: the first DFS computes $\operatorname{fa}(x)$, $\operatorname{dep}(x)$, $\operatorname{siz}(x)$, $\operatorname{son}(x)$, and the second DFS computes $\operatorname{top}(x)$, $\operatorname{dfn}(x)$, $\operatorname{rnk}(x)$.

```cpp
void dfs1(int u, int f) {
  fa[u] = f, dep[u] = dep[f] + 1, siz[u] = 1;
  for (auto v : G[u]) {
    if (v == f) continue;
    dfs1(v, u);
    siz[u] += siz[v];
    if (siz[v] > siz[son[u]]) son[u] = v;
  }
}

void dfs2(int u, int ftop) {
  top[u] = ftop, dfn[u] = ++idx, rnk[idx] = u;
  if (son[u]) dfs2(son[u], ftop);
  for (auto v : G[u])
    if (v != son[u] && v != fa[u]) dfs2(v, v);
}
```

## Properties of heavy-light decomposition

**Every node of the tree belongs to exactly one heavy chain**.

The first node of a heavy chain is certainly not a heavy child (because the first node of a heavy chain is either the root or a light child of its parent).

All heavy chains together **completely decompose** the whole tree.

During the decomposition we **traverse heavy edges first**, so in the final DFS order of the tree, the DFS indices within a heavy chain are contiguous. The sequence sorted by DFN is exactly the chains after decomposition.

The DFS indices within a subtree are contiguous.

One can see that whenever we go down through a **light edge**, the size of the subtree we are in is at least halved.

Therefore, for any path in the tree, splitting it into two descents from the [LCA](./lca.md) toward both sides, each descent takes at most $O(\log n)$ steps, so every path in the tree can be split into at most $O(\log n)$ heavy chains.

??? info "How to break HLD with good reason"
    In general, the $O(\log n)$ of HLD with a non-tight constant is hard to break; if one wants to, one can only build a binary tree of low depth.
    
    So we may consider a compromise.
    
    We build a binary tree with $\sqrt{n}$ nodes. For every edge from a node to its child, we replace it with a chain of length $\sqrt{n}$.
    
    This way we can push the number of light/heavy chain switches for random queries to $\frac{\log n}{2}$ on average, while having depth $O(\sqrt{n} \log n)$.
    
    Adding some random leaves seems able to break HLD. But since the constant factor of HLD is small, it may still not be broken.

## Common applications

### Path maintenance

Computing the sum of weights on the path between two nodes of a tree with heavy-light decomposition; the pseudocode is as follows:

$$
\begin{array}{l}
\text{TREE-PATH-SUM }(u,v) \\
\begin{array}{ll}
1 & \textit{tot}\gets 0 \\
2 & \textbf{while }u.\textit{top}\text{ is not }v.\textit{top} \\
3 & \qquad \textbf{if }u.\textit{top}.\textit{depth}< v.\textit{top}.\textit{depth} \\
4 & \qquad \qquad \text{SWAP}(u, v) \\
5 & \qquad \textit{tot}\gets \textit{tot} + \text{sum of values between }u\text{ and }u.\textit{top} \\
6 & \qquad u\gets u.\textit{top}.\textit{father} \\
7 & \textit{tot}\gets \textit{tot} + \text{sum of values between }u\text{ and }v \\
8 & \textbf{return } \textit{tot} 
\end{array}
\end{array}
$$

The DFS indices on a chain are contiguous, so they can be maintained with a segment tree or a Fenwick tree.

Each time, pick the chain of larger depth and jump upward, until both nodes are on the same chain.

The same chain-jumping structure applies to maintaining and counting other information on paths.

### Subtree maintenance

Sometimes it is required to maintain information on a subtree, for example increasing the weights of all nodes in the subtree rooted at $x$ by $v$.

During the DFS, the DFS indices of the nodes in a subtree are contiguous.

For every node record bottom, the node at the end of the contiguous interval of its subtree.

This turns subtree information into information on a contiguous interval.

### Computing the LCA

Keep jumping upward along heavy chains; when both reach the same heavy chain, the node of smaller depth is the LCA.

When jumping upward along heavy chains, first jump with the node whose heavy chain top has the larger depth.

Reference code:

```cpp
int lca(int u, int v) {
  while (top[u] != top[v]) {
    if (dep[top[u]] > dep[top[v]])
      u = fa[top[u]];
    else
      v = fa[top[v]];
  }
  return dep[u] > dep[v] ? v : u;
}
```

### Rerooting

Consider a new class of problems: in addition to the basic operations supported by heavy-light decomposition, a rerooting operation is added.

Since the information maintained by heavy-light decomposition is static, dynamic modifications are not supported. At the same time, it is impossible to redo the preprocessing after every rerooting; the complexity would be too high. Therefore, the previously obtained information needs to be fully exploited to handle the rerooting operation.

For path modifications and queries, since the simple path between two nodes of a tree is unique, nothing changes, and the handling is the same as usual.

For subtree modifications and queries, the general idea is to map the subtree after rerooting onto the original subtrees. This requires a case analysis of the relative positions of the root of the operated subtree, the root of the whole tree after rerooting, and the root of the original tree. For details, see the [example problem "LOJ 139. Tree chain decomposition" below](#example-problems).

## Example problems

This article shows how to apply heavy-light decomposition through examples. First, a template problem.

???+ example "["ZJOI2008" Tree statistics](https://loj.ac/problem/10138)"
    On a static tree with $n$ weighted nodes, perform $q$ operations of three kinds in total:
    
    1.  modify the weight of a single node;
    2.  query the maximum weight on the path from $u$ to $v$;
    3.  query the sum of weights on the path from $u$ to $v$.
    
    It is guaranteed that $1\le n\le 30000$, $0\le q\le 200000$.

??? note "Solution"
    According to the statement and the properties described above, the segment tree needs to maintain three operations:
    
    1.  point modification;
    2.  range maximum query;
    3.  range sum query.
    
    Point modification is easy to implement.
    
    Since the DFS indices of a subtree are contiguous (regardless of whether the tree is decomposed), modifying the subtree of a node only requires modifying this contiguous interval of DFS indices.
    
    The question is how to modify/query the path between two nodes.
    
    Recall how we **compute the LCA by binary lifting**. First we **lift the two nodes to the same height, then move both nodes upward together**. The same idea can be used for heavy-light decomposition.
    
    While jumping upward, if the current node is on a heavy chain, jump to the top of the heavy chain; if the current node is not on a heavy chain, jump up one node. Continue until the two nodes coincide. Update/query the interval information along the way.
    
    Each query passes through at most $O(\log n)$ heavy chains, and the segment tree complexity on each heavy chain is $O(\log n)$, so the total time complexity is $O(n\log n+q\log^2 n)$. In practice the number of heavy chains hardly reaches $O(\log n)$ (it can be saturated with a complete binary tree), so the decomposition generally has a small constant factor.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/hld/hld_1.cpp"
    ```

Next, a heavy-light decomposition template problem with a rerooting operation.

???+ example "[LOJ 139. Tree chain decomposition](https://loj.ac/p/139)"
    Given a tree with $n$ nodes (the initial root is $1$), support the following $m$ operations:
    
    -   reroot: make node $u$ the new root of the tree;
    -   modify node weights on a path: increase the weights of all nodes on the path between nodes $u$ and $v$ (including these two nodes) by $w$;
    -   modify node weights in a subtree: increase the weights of all nodes in the subtree rooted at node $u$ by $w$;
    -   query a path: the sum of weights of all nodes on the path between nodes $u$ and $v$ (including these two nodes);
    -   query a subtree: the sum of weights of all nodes in the subtree rooted at node $u$.
    
    $1 \le n,m \le 10^5$.

??? note "Solution"
    First run a DFS with $1$ as the root and preprocess the information needed for heavy-light decomposition. For convenience, we call the tree rooted at $1$ the "original tree" and the tree after a number of rerooting operations the "current tree". During the operations we maintain $\textit{root}$, the root of the current tree. Since the segment tree stores information in the DFS order of the original tree, every query and modification on the current tree has to be converted into one on the original tree.
    
    For the rerooting operation we simply set $\textit{root}\gets u$. For path operations, since rerooting does not affect paths, we just perform the corresponding operation on the original tree.
    
    The main issue is the subtree operations. We do a case analysis based on the relative positions of $u$ and $\textit{root}$:
    
    -   $u = \textit{root}$: the most special case, equivalent to operating on the whole tree. For this, just put a tag on the root of the segment tree or query the answer there.
    -   $u$ is an ancestor of $\textit{root}$ in the original tree, i.e. $u$ lies on the simple path from $1$ to $\textit{root}$.
    
        This is the case that deserves the most attention. Define $v$ as the node of minimum depth, other than $u$, on the simple path from $u$ to $\textit{root}$ in the original tree; one can see that the part of the original tree outside $v$ and its subtree is exactly $u$ and its subtree in the current tree.
    
        Consider how to find $v$ efficiently. First set $v\gets\textit{root}$, then jump upward along heavy chains until $\operatorname{dep}(\operatorname{top}(v))\le\operatorname{dep}(u)+1$.
    
        -   If $\operatorname{dep}(\operatorname{top}(v))=\operatorname{dep}(u)+1$, set $v\gets\operatorname{top}(v)$. In this case $v$ is a light child of $u$.
        -   If $\operatorname{dep}(\operatorname{top}(v))<\operatorname{dep}(u)+1$, i.e. $\operatorname{dep}(\operatorname{top}(v))\le \operatorname{dep}(u)$, this means $u,v$ are on the same heavy chain. By the property that the DFS indices on the same heavy chain are contiguous, the desired $v$ must satisfy $\operatorname{dfn}(v)=\operatorname{dfn}(u)+1$. So we can set $v\gets\operatorname{rnk}(\operatorname{dfn}(u)+1)$.
    
        Note that these two cases can be merged: after jumping we can directly set
    
        $$
        v\gets\operatorname{rnk}(\operatorname{dfn}(\operatorname{top}(v))+\operatorname{dep}(u)+1-\operatorname{dep}(\operatorname{top}(v))).
        $$
    
        It is easy to verify that the $v$ found with this expression is equivalent to the $v$ found by the case analysis. The reference implementation uses this expression.
    
        Since the subtree of $v$ covers the interval $[\operatorname{dfn}(v),\operatorname{dfn}(v)+\operatorname{siz}(v))$, it suffices to operate on $[1,\operatorname{dfn}(v))\cup[\operatorname{dfn}(v)+\operatorname{siz}(v),n]$.
    -   Other cases. One can see that rerooting does not affect the subtree of $u$, so maintain it in the normal way.
    
    The complexity of this approach is the same as without rerooting, $O(n\log^2 n)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/hld/hld_4.cpp"
    ```

Finally, an interactive problem, which is also a non-traditional application of the decomposition.

???+ example "[Nauuo and Binary Tree](https://loj.ac/problem/6669)"
    There is a binary tree rooted at $1$; you may query the distance between any two nodes, and you have to find the parent of every node.
    
    The number of nodes does not exceed $3000$, and you may make at most $30000$ queries.

??? note "Solution"
    First, the depth of every node can be determined with $n-1$ queries.
    
    Then consider determining the parent of every node in increasing order of depth, so that when determining the parent of a node, all its ancestors are already known.
    
    Before determining the parent of a node, perform heavy-light decomposition on the known part of the tree.
    
    Suppose we need to find the position of node $k$ in the subtree of $u$; we can query the distance between $k$ and the bottom end of the heavy chain containing $u$, which further determines the position of $k$; see the figure:
    
    ![](./images/hld2.png)
    
    The red dashed line is a heavy chain, $d$ is the query result, i.e. $\textit{dis}(k, \textit{bot}(u))$, and the depth of $v$ is $(\textit{dep}(k)+\textit{dep}(\textit{bot}(u))-d)/2$.
    
    Then, if $v$ has only one child, the parent of $k$ is $v$; otherwise, recursively find the parent of $k$ in the subtree of $w$.
    
    Time complexity $O(n^2)$, query complexity $O(n\log n)$.
    
    Concretely, let $T(n)$ be the number of queries needed in the worst case to find the position of a new node in a tree of size $n$; we obtain:
    
    $$
    T(n)\le
    \begin{cases}
    0&n=1\\
    T\left(\left\lfloor\frac{n-1}2\right\rfloor\right)+1&n\ge2
    \end{cases}
    $$
    
    $2999+\sum_{i=1}^{2999}T(i)\le 29940$; in fact this upper bound can be reached by constructed data, but with a bit of random perturbation (e.g. using an unstable sorting algorithm when sorting by depth), the number of queries hardly exceeds $21000$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/hld/hld_2.cpp"
    ```

## Long-path decomposition

Long-path decomposition is essentially just another way of decomposing a tree into chains.

The **heavy child** of a node is the child whose subtree has the greatest depth among its children. If there are several children with the deepest subtree, pick any one. If there are no children, there is no heavy child.

The **light children** are the remaining children.

The edge from a node to its heavy child is a **heavy edge**.

The edges to the other, light children are **light edges**.

A number of heavy edges joined end to end form a **heavy chain**.

Treating isolated nodes as heavy chains as well, the whole tree is decomposed into a number of heavy chains.

As in the figure (this decomposition can be viewed both as a heavy-light decomposition and as a long-path decomposition):

![HLD](./images/hld.png)

The implementation of long-path decomposition is similar to that of heavy-light decomposition and is not expanded on here.

### Common applications

First, we notice that with long-path decomposition, the number of light-edge switches on the path from a node to the root is of order $\sqrt{n}$.

??? info "How to construct data that maximizes the number of light/heavy edge switches"
    We can construct the following binary tree T:
    
    Suppose the parameter of the constructed binary tree is $D$.
    
    If $D \neq 0$, construct a binary tree with parameter $D-1$ in the left child, and a chain of length $2D-1$ in the right child.
    
    If $D = 0$, we can directly construct a single leaf node and end the call.
    
    This construction guarantees that the path from the single leaf to the root consists entirely of light edges, and it needs a number of nodes of order $D^2$.
    
    Just take $D=\sqrt{n}$.

#### Optimizing DP with long-path decomposition

In general, a DP that can be optimized with long-path decomposition has one state dimension that is the depth dimension.

We can consider optimizing tree DP with long-path decomposition.

Concretely, the state of every node directly inherits the state of its heavy child, while the DP states of the light children are merged by brute force.

???+ example "[Codeforces 1009 F. Dominant Indices](http://codeforces.com/contest/1009/problem/F)"
    Given a rooted tree with $n$ vertices, rooted at vertex $1$.
    
    The depth array of vertex $x$ is defined as an infinite sequence $[d_{x, 0}, d_{x, 1}, d_{x, 2}, \dots]$, where $d_{x, i}$ denotes the number of vertices $y$ satisfying the following two conditions:
    
    -   $x$ is an ancestor of $y$;
    -   the simple path from $x$ to $y$ passes through exactly $i$ edges.
    
    The dominant index of the depth array of vertex $x$ (the dominant index of vertex $x$ for short) is defined as an index $j$ such that:
    
    -   for all $k < j$, $d_{x, k} < d_{x, j}$;
    -   for all $k > j$, $d_{x, k} \le d_{x, j}$.
    
    Compute the dominant index of every vertex in the tree.

??? note "Solution"
    Let $f_{i,j}$ denote the number of nodes in the subtree of i at distance j from i.
    
    A direct brute-force transition has time complexity $O(n^2)$
    
    We consider, at every transition, directly inheriting the DP array and the answer of the heavy child, and then updating on that basis.
    
    First we need to insert an element 1 at the front of the heavy child's DP array, representing the current node.
    
    Then we merge the DP arrays of all light children into the DP array of the current node by brute force.
    
    Note that the length of a light child's DP array equals the length of the heavy chain the light child belongs to, and the sum of the lengths of all heavy chains is $n$.
    
    In other words, the total time complexity of merging the light children by brute force is $O(n)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/hld/hld_3.cpp"
    ```

Note that, in general, the memory of the DP array is allocated for a whole heavy chain at once, and different nodes on the chain have different start pointers.

The length of the DP array can be computed from the deepest node of the subtree.

Of course, there are many tricks for optimizing DP with long-path decomposition, including but not limited to lazy tags and so on. They are not expanded on here.

See [the blog of 租酥雨](https://www.cnblogs.com/zhoushuyu/p/9468669.html).

#### Finding the k-th ancestor with long-path decomposition

That is, querying the node reached by jumping from a node to its parent $k$ times.

First, suppose we have already preprocessed the $2^i$-th ancestors of every node.

Now suppose we have found the $2^i$-th ancestor of the queried node such that $2^i \le k < 2^{i+1}$.

We consider finding the nodes of the heavy chain it belongs to and listing them in a table by depth. Suppose the length of the heavy chain is $d$.

At the same time, during preprocessing, for the top node of every heavy chain we find its $1$st to $d$-th ancestors and put them in the table as well.

By the property of long-path decomposition, $k-2^i \le 2^i \leq d$, which means we can find the $k$-th ancestor of this node in $O(1)$ from the table of this heavy chain.

The preprocessing requires binary lifting for the $2^i$-th ancestors, as well as preprocessing the table for every heavy chain.

Preprocessing complexity $O(n\log n)$, query complexity $O(1)$.

## Exercises

-   ["Luogu P3379" 【模板】Lowest common ancestor (LCA)](https://www.luogu.com.cn/problem/P3379) (computing the LCA with the decomposition needs no data structure, good for practice)
-   ["JLOI2014" Squirrel's new home](https://loj.ac/problem/2236) (can of course also be done with tree difference arrays)
-   ["HAOI2015" Tree operations](https://loj.ac/problem/2125)
-   ["Luogu P3384" 【模板】Heavy-light decomposition / tree chain decomposition](https://www.luogu.com.cn/problem/P3384)
-   ["Luogu P1505" \[National training team\] Travel](https://www.luogu.com.cn/problem/P1505)
-   ["NOI2015" Package manager](https://uoj.ac/problem/128)
-   ["SDOI2011" Coloring](https://www.luogu.com.cn/problem/P2486)
-   ["SDOI2014" Travel](https://hydro.ac/p/bzoj-P3531)
-   ["Luogu P3979" Distant land](https://www.luogu.com.cn/problem/P3979)
-   ["POI2014" Hotel, hard version](https://hydro.ac/p/bzoj-P4543) (DP optimized with long-path decomposition)
-   [Strategy](https://hydro.ac/p/bzoj-P3252) (greedy optimized with long-path decomposition)
