---
title: Lowest common ancestor
---

## Definition

The lowest common ancestor is abbreviated LCA. The lowest common ancestor of two nodes is the one among their common ancestors that is farthest from the root.
For convenience, we denote the lowest common ancestor of a set of nodes $S=\{v_1,v_2,\ldots,v_n\}$ by $\text{LCA}(v_1,v_2,\ldots,v_n)$ or $\text{LCA}(S)$.

## Properties

> The content of the **Properties** section is translated, with modifications, from [wcipeg](http://wcipeg.com/wiki/Lowest_common_ancestor).

1.  $\text{LCA}(\{u\})=u$;
2.  $u$ is an ancestor of $v$ if and only if $\text{LCA}(u,v)=u$;
3.  if $u$ is not an ancestor of $v$ and $v$ is not an ancestor of $u$, then $u$ and $v$ lie in two different subtrees of $\text{LCA}(u,v)$;
4.  in a preorder traversal, $\text{LCA}(S)$ appears before all elements of $S$, and in a postorder traversal $\text{LCA}(S)$ appears after all elements of $S$;
5.  the lowest common ancestor of the union of two sets of nodes is the lowest common ancestor of their respective lowest common ancestors, i.e. $\text{LCA}(A\cup B)=\text{LCA}(\text{LCA}(A), \text{LCA}(B))$;
6.  the lowest common ancestor of two nodes necessarily lies on the shortest path between the two nodes in the tree;
7.  $d(u,v)=h(u)+h(v)-2h(\text{LCA}(u,v))$, where $d$ is the distance between two nodes in the tree and $h$ denotes the distance from a node to the root.

## Methods

### Naive algorithm

#### Process

In every step we can take the deeper of the two nodes and move it upward. Obviously, in a tree these two nodes must eventually meet, and the meeting point is the desired LCA.
Alternatively, first move the deeper node upward until both have the same depth, then move both upward together; they will also eventually meet.

#### Properties

The naive algorithm needs a dfs of the whole tree in preprocessing, with time complexity $O(n)$, and a single query has time complexity $\Theta(n)$. If the tree is random, the time complexity is related to the expected height of such a random tree.

### Binary lifting

#### Process

Binary lifting is the most classical method of computing LCA and is an improvement of the naive algorithm. By preprocessing the array $\text{fa}_{x,i}$, the cursor can move quickly, greatly reducing the number of cursor jumps. $\text{fa}_{x,i}$ denotes the $2^i$-th ancestor of node $x$. The array $\text{fa}_{x,i}$ can be preprocessed by dfs.

Now let us see how to optimize these jumps:
In the first phase of adjusting the cursors, we need to bring the two nodes $u,v$ to the same depth. We can compute the depth difference of $u,v$, call it $y$. By decomposing $y$ in binary, we optimize $y$ cursor jumps into "the number of `1`s in the binary representation of $y$" cursor jumps.
In the second phase, we loop from the largest $i$ down to $0$ (inclusive); if $\text{fa}_{u,i}\not=\text{fa}_{v,i}$, then $u\gets\text{fa}_{u,i},v\gets\text{fa}_{v,i}$, and the final LCA is $\text{fa}_{u,0}$.

#### Properties

The preprocessing time complexity of binary lifting is $O(n \log n)$, and a single query has time complexity $O(\log n)$.
In addition, binary lifting can swap the two dimensions of the `fa` array so that the smaller dimension comes first. This reduces the number of cache misses and improves the efficiency of the program.

??? note "Example problem"
    [HDU 2586 How far away?](https://acm.hdu.edu.cn/showproblem.php?pid=2586) Shortest path queries on a tree.

We can first compute the LCA and then answer using property $7$. The result can also be computed directly while computing the LCA.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/lca/lca_1.cpp"
    ```

### Tarjan's algorithm

#### Process

Tarjan's algorithm is an **offline algorithm** that uses a [union-find](../ds/dsu.md) to record the ancestor of a node. The procedure is as follows:

1.  First read the input edges (adjacency list) and the query edges (stored in another adjacency list). The query edges are actually virtually added edges; for convenience, whenever a query edge is read, both the edge and its reverse are added to the `queryEdge` array.
2.  Then perform a DFS traversal, using the `visited` array to record whether a node has been visited and `parent` to record the parent of the current node.
3.  This involves the idea of **backtracking**: whenever we reach a node, we regard the root of that node as itself. Only after the DFS rooted at that node has completely finished do we set the root of that node to its parent.
4.  When backtracking, if for a query edge in `queryEdge` starting at this node the other node has also already been visited, directly update the LCA result of that query edge.
5.  Finally output the results.

#### Properties

Tarjan's algorithm needs to initialize the union-find, so the preprocessing time complexity is $O(n)$.

The naive Tarjan algorithm processes all $m$ queries in $O(m \alpha(m+n, n) + n)$ time, but the constant factor of Tarjan's algorithm is larger than that of binary lifting. An $O(m + n)$ implementation exists.

???+ warning "Note"
    The claim that "the union-find used in the naive Tarjan LCA algorithm has special properties, so a single call to `find()` has amortized time complexity $O(1)$" is not true.
    
    The complexity of the naive Tarjan implementation below is $O(m \alpha(m+n, n) + n)$. If strictly linear complexity is required, refer to [the 1983 paper by Gabow and Tarjan](https://dl.acm.org/doi/pdf/10.1145/800061.808753), which gives an $O(m + n)$ approach.

#### Implementation

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/lca/lca_tarjan.cpp"
    ```

### Reduction to RMQ via the Euler tour

#### Definition

Perform a DFS on the tree, and every time a node is reached, whether on the first visit or when backtracking, record its index; we obtain a sequence of length $2n-1$, which is called the Euler tour of the tree.

In the following, the position of the first occurrence of node $u$ in the Euler tour is denoted $pos(u)$ (also called the Euler index of node $u$), and the Euler tour itself is denoted $E[1..2n-1]$.

#### Process

With the Euler tour, the LCA problem can be transformed into an RMQ problem in linear time, namely $pos(LCA(u, v))=\min\{pos(k)|k\in E[pos(u)..pos(v)]\}$.

This equality is not hard to understand: on the way from $u$ to $v$ we must pass through $LCA(u,v)$, but not through the ancestors of $LCA(u,v)$. Therefore, the node with the smallest Euler index passed on the way from $u$ to $v$ is exactly $LCA(u, v)$.

Computing the Euler tour by DFS has time complexity $O(n)$, and the length of the Euler tour is also $O(n)$, so the LCA problem can be transformed in $O(n)$ time into an RMQ problem of the same size.

#### Implementation

???+ note "Reference code"
    ```cpp
    int dfn[N << 1], pos[N], tot, st[30][(N << 1) + 2],
        rev[30][(N << 1) + 2];  // rev is the index of the node corresponding to the minimum depth
    
    void dfs(int cur, int dep) {
      dfn[++tot] = cur;
      depth[tot] = dep;
      pos[cur] = tot;
      for (int i = head[t]; i; i = side[i].next) {
        int v = side[i].to;
        if (!pos[v]) {
          dfs(v, dep + 1);
          dfn[++tot] = cur, depth[tot] = dep;
        }
      }
    }
    
    void init() {
      for (int i = 2; i <= tot + 1; ++i)
        lg[i] = lg[i >> 1] + 1;  // precompute lg instead of the library function log2 to reduce the constant factor
      for (int i = 1; i <= tot; i++) st[0][i] = depth[i], rev[0][i] = dfn[i];
      for (int i = 1; i <= lg[tot]; i++)
        for (int j = 1; j + (1 << i) - 1 <= tot; j++)
          if (st[i - 1][j] < st[i - 1][j + (1 << i - 1)])
            st[i][j] = st[i - 1][j], rev[i][j] = rev[i - 1][j];
          else
            st[i][j] = st[i - 1][j + (1 << i - 1)],
            rev[i][j] = rev[i - 1][j + (1 << i - 1)];
    }
    
    int query(int l, int r) {
      int k = lg[r - l + 1];
      return st[k][l] < st[k][r + 1 - (1 << k)] ? rev[k][l]
                                                : rev[k][r + 1 - (1 << k)];
    }
    ```

When we need the LCA of a pair $(u, v)$, we just query the node represented by the minimum on the interval $[\min\{pos[u], pos[v]\}, \max\{pos[u], pos[v]\}]$.

If a sparse table is used to solve the RMQ problem, the algorithm does not support online modifications, the preprocessing time complexity is $O(n\log n)$, and each LCA query has time complexity $O(1)$.

### Reduction to RMQ via the DFS order

The length of the Euler tour is $2n-1$, so the time and space constant factors are slightly larger. In fact, the LCA can be computed directly using the DFS timestamps $\operatorname{dfn}$.

Consider the LCA of a pair $(u,v)$ and let $d=\operatorname{LCA}(u,v)$. If $u=v$, then $d=u$, which needs special handling. Otherwise, without loss of generality let $\operatorname{dfn}(u) < \operatorname{dfn}(v)$; then $v$ is certainly not an ancestor of $u$. Unlike the Euler tour, in the DFS order $d$ does not appear in the interval $(\operatorname{dfn}(u), \operatorname{dfn}(v)]$. However, it must contain the child of $d$ lying on the path from $d$ to $v$. This always holds, regardless of whether $u$ is an ancestor of $v$. Therefore, as soon as we find the node of minimum depth (not necessarily unique) in the interval $[\operatorname{dfn}(u) + 1, \operatorname{dfn}(v)]$, its parent must be the LCA. The reason the interval starts at $\operatorname{dfn}(u) + 1$ is: if $u$ is an ancestor of $v$ and the interval contained $u$, the node of minimum depth would be $u$ itself, and its parent is not the LCA.

Thus, computing the LCA again becomes an RMQ problem.

If we do not want to store extra depth and parent information, we can directly store $\operatorname{fa}(u)$ at position $\operatorname{dfn}(u)$ of the DFS order. Then, on this sequence, compare two values by their timestamps. Then the element of this sequence with the smallest timestamp in the interval $[\operatorname{dfn}(u) + 1, \operatorname{dfn}(v)]$ is exactly $\operatorname{LCA}(u,v)$. This is because the nodes in the interval $[\operatorname{dfn}(u) + 1, \operatorname{dfn}(v)]$ must be proper descendants of $d$, so the DFS timestamps of their parents are not smaller than $\operatorname{dfn}(d)$; and within the interval the minimum $\operatorname{dfn}(d)$ is attained exactly at a child of $d$, and by the discussion above such a child must exist.

Transforming LCA into RMQ via the DFS order takes $O(n)$, and the total complexity depends on the RMQ method used. A reference implementation using a sparse table with $O(n\log n)$ preprocessing and $O(1)$ queries is as follows:

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/graph/code/lca/lca-dfs.cpp:lca"
    ```

### Heavy-light decomposition

The LCA is the node pointed to by the shallower of the two cursors at the moment both have jumped onto the same heavy chain.

The preprocessing time complexity of heavy-light decomposition is $O(n)$, a single query has time complexity $O(\log n)$, and the constant factor is small.

### Link Cut Tree

In a [Link Cut Tree](../ds/lct.md), if the nodes of two consecutive [access](../ds/lct.md#access) operations are `u` and `v` respectively, then the node returned by the second [access](../ds/lct.md#access) operation is the LCA of `u` and `v`.

Without link and cut operations, a single query using a Link Cut Tree has time complexity $O(\log n)$.

### Standard RMQ

Earlier we described transforming the LCA problem into an RMQ problem using the Euler tour; the bottleneck is the RMQ. If RMQ can be solved in $O(n) \sim O(1)$, then LCA can also be solved in $O(n) \sim O(1)$.

Note that in the Euler tour the difference between two adjacent numbers is 1 or -1, so the $O(n) \sim O(1)$ [±1 RMQ](../topic/rmq.md#加减-1rmq) can be used.

Time complexity $O(n) \sim O(1)$, space complexity $O(n)$, supports online queries, large constant factor.

#### Example problem [Luogu P3379【模板】Lowest common ancestor (LCA)](https://www.luogu.com.cn/problem/P3379)

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/lca/lca_2.cpp"
    ```

## Exercises

-   [Ancestor-descendant queries](https://loj.ac/problem/10135)
-   [Truck transportation](https://loj.ac/problem/2610)
-   [Distance between nodes](https://loj.ac/problem/10130)

## References

-   [A little-known technique – LCA via DFS order, by Alex\_Wei – Luogu](https://www.luogu.com.cn/article/pu52m9ue)
