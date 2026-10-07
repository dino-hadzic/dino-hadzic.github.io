---
title: Tree centroid
---

This article introduces the concept of the centroid of a tree and its basic properties.

## Definition

If, after deleting some node $v$ from a tree $T$, the size of every connected component of the resulting graph $T\setminus\{v\}$ does not exceed half of the number of nodes of the original tree, then node $v$ is called a **centroid** of the whole tree. The size of the largest connected component obtained by deleting a node is also called the **weight** of that node. Using this concept, the definition of a centroid can be stated as a node whose weight does not exceed half of the number of nodes of the tree.

???+ info "\"Subtree\""
    This article may deal simultaneously with unrooted trees, rooted trees, and trees obtained by rerooting a rooted tree at a non-root node. To avoid confusion, we denote an unrooted tree by $T$ and the rooted tree rooted at node $v$ by $T^{(v)}$. A "subtree" in this article always means the tree formed, in a **rooted tree**, by a node and all of its descendants. In the rooted tree $T^{(v)}$, the subtree corresponding to node $u$ is denoted $T^{(v)}_u$. A subtree defined this way of course includes the whole tree itself. When we want to explicitly exclude the whole tree, we will call it a "proper subtree".
    
    A "subtree" of an unrooted tree usually refers to one of its connected subgraphs. When discussing centroids, some authors use the word "subtree" specifically for a maximal connected subgraph not containing a certain node, or for one of the two connected components obtained by deleting an edge. It is easy to verify that the sets of "subtrees" obtained by these two definitions coincide, and they do not include the whole tree itself. Since this does not coincide with the set of subtrees of a rooted tree, this article avoids using the notion of "subtree" for unrooted trees.
    
    When actually computing the centroid or dealing with certain problems, there is usually a default root. Then, among the connected components obtained by deleting a non-root node $v$, besides the subtrees corresponding to the children of that node there is also an "upward" subtree. If the parent of node $v$ is $u$, this "upward" subtree is $T_u^{(v)}$. When this article refers to such a subgraph, it will explicitly call it the "upward" subtree. Unless otherwise stated, the subtrees mentioned in this article do not include such "upward" subtrees.

Note that the resulting connected components are again unrooted trees. By deleting the centroid, a tree becomes several trees of size at most half of the original. This property of the centroid makes it possible to apply the divide-and-conquer idea on trees. This is [centroid decomposition](./tree-divide.md#centroid-decomposition), also called centroid decomposition of a tree.

## Properties

This section discusses the properties of the centroid. First, the centroid of a tree has the following equivalent definitions:

???+ note "Equivalent definitions"
    A node $v$ of a tree $T$ is its centroid if and only if any of the following holds:
    
    === "Unrooted tree version"
        1.  After deleting node $v$ from the tree, the size of every connected component of the resulting graph $T\setminus\{v\}$ does not exceed half of the number of nodes of the original tree.
        2.  Among the sizes of the largest connected component obtained by deleting a node, the value obtained by deleting node $v$ is minimal.
        3.  Among the sums of distances from all nodes of the tree to a node, the sum of distances to node $v$ is minimal.
    
    === "Rooted tree version"
        1.  When the tree is rooted at node $v$, the size of every proper subtree does not exceed half of the number of nodes of the original tree.
        2.  Among the sizes of the largest proper subtree when the tree is rooted at a node, the value obtained when rooting at node $v$ is minimal.
        3.  Among the sums of depths of all nodes when the tree is rooted at a node, the sum of depths when rooting at node $v$ is minimal.

??? note "Proof"
    First, introduce some notation. The formulations of the rooted and unrooted versions are obviously equivalent. Define $W(x)=\max_{u\sim x}|T_u^{(x)}|$, where $u\sim x$ means that $u$ and $x$ are adjacent. Define $S(x)=\sum_{u\in T}d(u,x)$, where $d(u,x)$ is the distance between nodes $u$ and $x$. Then definition 1 amounts to requiring $W(v)\le |T|/2$, definition 2 amounts to requiring $v\in\arg\min_{x\in T}W(x)$, and definition 3 amounts to requiring $v\in\arg\min_{x\in T}S(x)$. What needs to be proved is that these three conditions are equivalent.
    
    Interpret $S(x)$ as the sum of node depths when the root is $x$, and consider how it changes when the root is moved from node $v$ to an adjacent node $u$. Note that after deleting the edge $(v,u)$ from the tree, the two resulting connected components are the subtrees $T_v^{(u)}$ and $T_u^{(v)}$. Before and after rerooting, the depth of every node in the subtree $T_v^{(u)}$ increases by $1$, and the depth of every node in the subtree $T_u^{(v)}$ decreases by $1$, so the change of the depth sum is
    
    $$
    \Delta S_{v\to u} = S(u) - S(v) = |T_v^{(u)}| - |T_u^{(v)}| = |T| - 2|T_u^{(v)}|.
    $$
    
    Therefore, the condition of definition 1 amounts to requiring $\Delta S_{v\to u}\ge 0$ for all neighbors $u$ of $v$, that is, $v$ is a local minimum of $S(\cdot)$.
    
    Now suppose instead that $v$ is a (global) minimum point of $S(\cdot)$ (i.e. definition 3); it necessarily exists and is certainly a local minimum. Consider the rooted tree $T^{(v)}$ rooted at $v$. Let $u\neq v$ be a non-root node, and on the directed path from $v$ to $u$, let the node after $v$ be $y$ (possibly $u$ itself), and the node before $u$ be $x$ (possibly $v$ itself). Then, since $T_u^{(x)}\subseteq T_y^{(v)}$, we have
    
    $$
    2|T_x^{(u)}| = 2|T| - 2|T_u^{(x)}| \ge 2|T| - 2|T_y^{(v)}| \ge |T|.
    $$
    
    Here the last step uses the fact that $v$ is a local minimum of $S(\cdot)$. Now there are two cases:
    
    -   There exists a node $u$ with $2|T_x^{(u)}|=|T|$. Then, by the inequality above, necessarily $(x,u)=(v,y)$ and $|T_v^{(u)}|=|T_{u}^{(v)}| = |T|/2$. In other words, the node $u$ for which equality holds must be adjacent to $v$; and since the sum of the sizes of the subtrees corresponding to all neighbors of $v$ is $|T|-1<|T|$, there can be only one such node $u$. Then, for all other nodes $u'\neq u,v$, there necessarily exists $x'\sim u'$ with $|T_{x'}^{(u')}| > |T|/2$. The set of nodes satisfying condition 1 is $\{v,u\}$.
    
        Note that when deleting any node, the sum of the sizes of the resulting connected components is always $|T|-1$, so as soon as one component has size at least $|T|/2$, it must be the largest component. Therefore, in this case, $W(v)=W(u)=|T|/2$, and for all $u'\neq u,v$ we have $W(u') > |T|/2$. Hence the set of nodes satisfying condition 2 is $\arg\min W(\cdot) = \{v,u\}$.
    
        Moreover, since $\Delta S_{v\to u} = 0$, we have $S(v)=S(u)$. Since $v$ is a global minimum point, $u$ must also be a global minimum point. And for $u'\neq u,v$ there exists $x'\sim u'$ with $|T_{x'}^{(u')}| > |T|/2$, which violates the condition a local minimum must satisfy, so $u'$ is certainly not a global minimum point either. Hence the set of nodes satisfying condition 3 is $\arg\min S(\cdot) = \{v,u\}$.
    -   There is no node $u$ with $2|T_x^{(u)}|=|T|$. Then, for all nodes $u\neq v$, there exists a node $x\sim u$ with $|T_x^{(u)}| > |T|/2$. Repeating the previous analysis shows that for all nodes $u\neq v$ we have $W(u) > |T|/2$ and $u$ is not a local minimum of $S(\cdot)$. Hence the only node satisfying condition 1 is $v$, and $\arg\min W(\cdot)=\arg\min S(\cdot) = \{v\}$.
    
    In either case, the sets satisfying the three conditions are the same. This proves that the three definitions are equivalent.

Besides these equivalent definitions, the centroid of a tree also has the following common properties:

???+ note "Properties"
    1.  If the centroid of a tree is not unique, then there are exactly two. These two centroids are adjacent. Moreover, after deleting the edge between them, the tree becomes two connected components of equal size.
    2.  When a leaf is added to or removed from a tree, its centroid moves by at most one edge.
    3.  When two trees are connected by an edge to form a new tree, the centroid of the new tree lies on the path connecting the centroids of the two original trees.
    4.  The centroid of a rooted tree always lies on the heavy chain containing the root. The centroid of a tree is always an ancestor of the centroid of the subtree corresponding to the heavy child of the root.

??? note "Proof"
    Property 1 follows from the proof of the equivalent definitions of the centroid.
    
    For property 2 it suffices to consider adding a leaf. This further splits into two cases:
    
    -   The tree $T$ has only one centroid $v$. Let $x$ be the newly added leaf, and in the graph $T\cup\{x\}\setminus\{v\}$ obtained by deleting node $v$ from the new tree, let the connected component containing $x$ be $B\cup\{x\}$. Since $v$ is the unique centroid of $T$, we have $2|B| < |T|$, i.e. $2|B|+1\le |T|$. Consequently,
    
        $$
        2|B\cup\{x\}| = 2(|B|+1) \le |T| + 1 = |T\cup\{x\}|.
        $$
    
        Therefore, $v$ is still a centroid of the new tree $T\cup\{x\}$. Even if the centroid of the new tree is not unique, it must be a neighbor of $v$. Hence the centroid moves by at most one edge.
    -   The tree $T$ has two centroids $u,v$. Then the two connected components $T_u^{(v)}$ and $T_v^{(u)}$ obtained by deleting $(u,v)$ have equal size, both $|T|/2$. Without loss of generality, let the newly added leaf $x$ be attached to the component $T_v^{(u)}$ containing $v$. Then, since
    
        $$
        |T_v^{(u)}\cup\{x\}| = |T|/2 + 1 > (|T|+1)/2 = |T\cup\{x\}|/2,
        $$
    
        $u$ is no longer a centroid of the new tree. Conversely, after deleting $v$ there is still the connected component $T_u^{(v)}$ of size $|T|/2$, while the sum of the sizes of the other components is
    
        $$
        |T\cup\{x\}| - 1 - |T_u^{(v)}| = |T|/2 \le |T_u^{(v)}|,
        $$
    
        so $v$ is still a centroid of the new tree. Since the number of nodes of the new tree is odd, the centroid must be unique. So again the centroid moves by at most one edge.
    
    Summarizing the analysis of the two cases, the centroid of the new tree always lies on the path between the centroid of the old tree and the newly added leaf.
    
    Property 3 can be shown by induction. Let the newly added edge when connecting $T$ and $T'$ be $(x,y)$, with $x\in T,y\in T'$. Without loss of generality, let a centroid of the new tree be in $T$. Consider the process of starting from the tree $T$ and adding the nodes of $T'$ one by one as leaves. Fix a centroid $c$ of the tree $T$. It can be proved by induction that a centroid of the tree always lies on the path connecting $c$ and node $x$. The base case is obvious. Suppose the statement holds up to some moment, and let the centroid at that moment be $v$. By the analysis of property 2, the centroid of the new tree must lie on the path connecting the newly added node and the current centroid $v$, and since it does not move outside the tree $T$, it suffices to consider the common part of this path and the tree $T$, namely the path connecting the current centroid $v$ and node $x$. By the induction hypothesis, $v$ lies on the path connecting $c$ and node $x$, so the centroid of the new tree must also lie on the path connecting $c$ and node $x$. By induction, the statement holds.
    
    Property 4 follows by combining with the [properties of heavy-light decomposition](./hld.md#properties-of-heavy-light-decomposition). Let a centroid of the tree $T$ be $v$. If $v$ is the root, the statement obviously holds. Now let $v$ be a non-root node and $u$ its parent. Since $|T_u^{(v)}| \le |T|/2$, the size of the subtree containing $v$ is at least $|T|/2$. But as soon as the path from it to the root passes through a light edge, the size of the subtree containing it would be strictly less than $|T|/2$, a contradiction. Hence it must lie on the heavy chain containing the root. Furthermore, by the definition of heavy chains, the heavy chain containing the root of the subtree corresponding to the heavy child of the root is part of the heavy chain containing the root of the original tree; and by property 3, after adding the root and the subtrees of all its light children to the subtree of the heavy child, the position of the centroid moves along the path between the current centroid and the root, so the new centroid must be an ancestor of the old centroid (including itself).

## Methods

According to the equivalent definitions of the centroid, there are two ways to find all centroids of a tree in $O(n)$ time, where $n$ is the size of the tree.

### DFS computing subtree sizes

Compute the size of every subtree by DFS. For every node, record the sizes of the subtrees corresponding to all its children, and obtain the size of the "upward" subtree by subtracting the current subtree size from the total number of nodes; then the centroid can be found according to the definition.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/graph/code/tree-centroid/tree-centroid-2.cpp:core"
    ```

### Rerooting DP computing depth sums

We can also use rerooting DP to compute, for each node as the root, the sum of depths of all nodes (i.e. the sum of distances to the current root). By definition, it suffices to find the node minimizing this depth sum.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/graph/code/tree-centroid/tree-centroid-3.cpp:core"
    ```

## Example problem

???+ example "[Codeforces Round 359 (Div. 1) B. Kay and Snowflake](https://codeforces.com/problemset/problem/685/B)"
    Given a rooted tree, find the centroid of every subtree.

??? note "Solution idea"
    By property 4, for the subtree rooted at node $u$, its centroid must lie on the path from the centroid of the subtree rooted at the heavy child of $u$ to node $u$.
    
    Similarly to the DFS method of finding the centroid mentioned above, for every subtree rooted at node $u$, first find the centroid of the subtree of its heavy child (the centroid of a leaf is itself), then go upward from that centroid and check whether the nodes on the path are centroids; if none of the nodes on the path is a centroid, then $u$ itself is the centroid.
    
    Since the centroids of the subtrees on the same heavy chain only move upward along the chain, the total number of upward checks on each heavy chain is of the same order as the length of the chain, so the centroids of all subtrees can be found in $O(n)$ time.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/tree-centroid/tree-centroid-1.cpp"
    ```

## Exercises

-   [Gym 101649G Godfather](https://codeforces.com/gym/101649/problem/G)
-   [POJ 1655 Balancing Act](http://poj.org/problem?id=1655)
-   [Luogu P1364 Hospital Placement](https://www.luogu.com.cn/problem/P1364)
-   [Codeforces 1406C Link Cut Centroids](https://codeforces.com/contest/1406/problem/C)
-   [Codeforces 708C Centroids](https://codeforces.com/problemset/problem/708/C)

## References

-   [Some properties of the "centroid" of a tree and its dynamic maintenance – fanhq666](https://web.archive.org/web/20181122041458/http://fanhq666.blog.163.com/blog/static/81943426201172472943638) ([repost on cnblogs](https://www.cnblogs.com/qlky/p/5781081.html))
-   [Tree diameter, tree centroid and centroid decomposition – cyendra](https://www.cnblogs.com/zinthos/p/3899075.html)
-   [Properties of the tree centroid and their proofs – suxxsfe](https://www.cnblogs.com/suxxsfe/p/13543253.html)
-   "Dictionary of the Olympiad in Informatics" (信息学奥林匹克辞典), section 2.4.7.11, 1. Tree centroid
