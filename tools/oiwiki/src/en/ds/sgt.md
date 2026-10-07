---
title: Scapegoat tree
---

## Introduction

A **scapegoat tree** is a weight-balanced tree that maintains balance by rebuilding. After insertions and deletions, a scapegoat tree checks whether the tree has become unbalanced; if so, it rebuilds a targeted part of the tree to restore balance.

In general, scapegoat trees do not support range operations and cannot be made fully persistent, but they have the advantages of a simple implementation and a small constant factor.

## Basic structure and operations

The core operations of a scapegoat tree are rebuilding, insertion and deletion.

### Node information

A scapegoat tree needs to store the following information for self-balancing:

-   tree structure information:
    -   `id`: the number of nodes used;
    -   `rt`: the root;
    -   `lc[x]`, `rc[x]`: the left and right children;
    -   `tot[x]`: the size of the subtree rooted at $x$ (every node counts as $1$)[^tot-cnt];
    -   `tot_active`: the number of non-deleted nodes (i.e. those with `cnt[x] != 0`) in the whole tree.

When using a scapegoat tree to implement a balanced tree, the following information is also needed:

-   balanced-tree node information:
    -   `val[x]`: the value stored in the node;
    -   `cnt[x]`: the multiplicity of the value stored in the node (may be $0$);
    -   `sz[x]`: the sum of the multiplicities of the values stored in the subtree rooted at $x$.

To maintain the node information we can implement a `push_up` operation:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:push-up"
    ```

Note the difference between how `tot[x]` and `sz[x]` are updated.

### Rebuilding

When the tree becomes unbalanced, some subtree must be rebuilt to make it as balanced as possible. Rebuilding has two steps:

-   do an in-order traversal of the subtree to be rebuilt and store all non-deleted nodes in a sequence;
-   build the tree by bisection, i.e. take the middle element as the root, recursively build the subtrees on the left and right, and update the node information.

A reference implementation follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:rebuild"
    ```

When building the tree, take care to maintain the node information, including that of the leaves.

The complexity of a single rebuild is $\Theta(|T_x|)$, so rebuilding on every insertion and deletion would be unacceptable. The core idea of the scapegoat tree lies precisely in the choice of when to rebuild, which achieves an amortized complexity of $O(\log n)$.

### Insertion

An insertion may unbalance the tree. To detect imbalance, we introduce a parameter $\alpha\in(0.5,1)$, usually chosen between $0.7$ and $0.8$.

If the depth of the newly inserted node exceeds $\lfloor\log_{1/\alpha}|T|\rfloor$, where $|T|$ is the size of the tree after the update, then while backtracking we must find the node where the imbalance occurred and rebuild it. The subtree rooted at $x$ is considered unbalanced if

$$
\max\{|T_{\mathrm{left}(x)}|,|T_{\mathrm{right}(x)}|\} > \alpha\cdot |T_x|,
$$

where $\mathrm{left}(x)$ and $\mathrm{right}(x)$ are the left and right children of $x$, and $|T_x|$ is the size of the subtree rooted at $x$.

The concrete steps of insertion are as follows:

-   first, use the binary search tree property to descend to the position of the inserted value, recording the depth on the way down;
-   if a node already exists, simply update its information; otherwise create a new node;
-   backtrack from the bottom up to the root, updating the node information; if the new node is too deep, also record the first (or any) node on the way back whose subtree is unbalanced;
-   if an unbalanced node exists, rebuild its subtree.

A reference implementation follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:insert"
    ```

Note that a single insertion triggers at most one rebuild. If no new node was created, or the new node is not too deep, or a rebuild has already been performed during this backtracking, there is no need to keep checking for imbalance. Redundant rebuilds may cause a loss of efficiency[^insert-complexity]. The first unbalanced node on the way back is the so-called "scapegoat".

### Deletion

Deletion is handled very simply. The deletion strategy of a scapegoat tree is "lazy deletion": when a node becomes empty, it is not removed but left for later processing.

Of course, if there are too many empty nodes in the tree, access efficiency drops considerably. Therefore a scapegoat tree maintains two counters: the number of non-deleted nodes in the whole tree and the number of nodes actually used in the whole tree. For a chosen threshold[^threshold] $\alpha\in(0,1)$, when the ratio of the former to the latter drops below $\alpha$, the whole tree is rebuilt once, and all empty nodes are removed during the rebuild.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:remove"
    ```

### Time complexity

In a scapegoat tree of size $n$, the time complexity of a single node access is $O(\log n)$; the time complexity of $\Theta(n)$ insertions and deletions is also amortized $O(\log n)$ per operation.

This section gives only a brief justification of the time complexity of scapegoat trees; for a detailed proof see the original paper.

??? note "Justification of the time complexity of scapegoat trees"
    Because of lazy deletion, a scapegoat tree with $n$ non-deleted nodes may occupy $\alpha^{-1}n$ nodes. Since they differ only by a constant factor, this text does not distinguish between the number of non-deleted nodes and the number of occupied nodes of a scapegoat tree, and calls both "the size of the tree".
    
    1.  **Access**: the complexity of access is guaranteed because the height of a scapegoat tree of size $n$ is always $O(\log n)$.
    
        First, distinguish two concepts:
    
        -   $\alpha$‑weight-balance: at every node, the sizes of the subtrees of the left and right children do not exceed $\alpha$ times the size of the subtree at that node;
        -   $\alpha$‑height-balance: the height of the tree does not exceed $\lfloor\log_{1/\alpha}|T|\rfloor$, where $|T|$ is the size of the tree.
    
        $\alpha$‑weight-balance implies $\alpha$‑height-balance, because each time the depth increases by one, the subtree size shrinks to at most $\alpha$ times the previous size; the converse need not hold. More precisely, after every operation finishes, the scapegoat tree is always $\alpha$‑height-balanced[^hei-bal], which guarantees the complexity of access.
    
        Only insertion changes the structure of the tree, so it suffices to show that after every insertion the scapegoat tree is still $\alpha$‑height-balanced. If the newly inserted node is too deep, so that the whole tree is no longer $\alpha$‑height-balanced, then when backtracking from that node to the root we must meet at least one node, the "scapegoat", whose subtree is no longer $\alpha$‑weight-balanced. After rebuilding it, the height of the subtree decreases by at least one, so the newly inserted node is no longer too deep.
    2.  **Insertion**: the complexity of insertion is amortized $O(\log n)$.
    
        Suppose that after some insertion a subtree rebuild happens at node $x$, with time cost $\Theta(|T_x|)$. When node $x$ was just inserted, or just after it went through the previous rebuild (of itself or of an ancestor), its left and right subtrees differ by at most one node. And right before this rebuild, at node $x$ we must have
    
        $$
        \max\{|T_{\mathrm{left}(x)}|,|T_{\mathrm{right}(x)}|\} > \alpha\cdot |T_x|.
        $$
    
        This condition guarantees that the difference between the sizes of the left and right subtrees is at least $(2\alpha-1)|T_x|$. Hence, between these two rebuilds, $\Omega(|T_x|)$ nodes were inserted into the subtree $T_x$.
    
        By amortized analysis[^alternative-analysis], if on every insertion we add $\Theta(1)$ potential at every node on the path from the root to the inserted node (before any rebuild), then before the subtree rebuild at node $x$, a potential of $\Omega(|T_x|)$ must have accumulated at node $x$, enough to pay for the cost $\Theta(|T_x|)$ of rebuilding the subtree at $x$. Since the depth of the tree is always $O(\log n)$, the potential added by a single insertion is $O(\log n)$; this means that the total increase of potential over $\Theta(n)$ insertions is $O(n\log n)$. Hence the total cost of subtree rebuilds is also $O(n\log n)$, and the amortized time complexity of a single insertion (including rebuilding) is $O(\log n)$.
    
        Note that the analysis does not assume that no other rebuilds happen inside the subtree $T_x$ between two rebuilds at node $x$. Therefore, as long as we only rebuild subtrees at nodes satisfying the imbalance condition, the complexity is guaranteed to be correct.
    3.  **Deletion**: the complexity of deletion is also amortized $O(\log n)$.
    
        A rebuild triggered by deletion results in a whole tree without empty nodes. Before some deletion triggers a rebuild, the whole tree already contains $\Theta(n)$ empty nodes, which means at least $\Theta(n)$ deletions have been performed. Since the complexity of locating the node in each deletion is $O(\log n)$ and the complexity of a single rebuild is $\Theta(n)$, the actual time cost of these $\Theta(n)$ deletions is
    
        $$
        \Theta(n)O(\log n)+\Theta(n)
        $$
    
        . Hence the amortized complexity of a single deletion is $O(\log n)$.

## Balanced tree operations

This section describes how to maintain a multiset with a scapegoat tree.

Apart from the operations introduced in the previous section, the remaining operations are the usual balanced tree operations. However, since a scapegoat tree may contain empty nodes, these operations also need to be adjusted accordingly.

### Querying the rank

Use the binary search tree property to descend to the position of the node, counting along the way the values stored to the left of the path.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:find-rank"
    ```

### Querying the value by rank

Descend using the counts of values stored in the subtrees that the nodes record. Note that nodes with count zero may exist.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:find-kth"
    ```

### Querying the predecessor and successor

Simply combine the two functions above.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:pred-succ"
    ```

If you want to implement them directly, take care to handle nodes with count zero.

### Reference implementation

At the end of this section, we give a reference implementation of the template problem [Ordinary balanced tree](https://loj.ac/p/104).

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:full-text"
    ```

## References

-   Galperin, Igal, and Ronald L. Rivest. "Scapegoat trees." Proceedings of the fourth annual ACM-SIAM Symposium on Discrete algorithms. 1993.
-   [Scapegoat Tree - Wikipedia](https://en.wikipedia.org/wiki/Scapegoat_tree)
-   [Scapegoat tree – riteme's blog](https://riteme.site/blog/2016-4-6/scapegoat.html)

[^tot-cnt]: One may also count only the non-deleted nodes; then `tot_active` is no longer needed, but the total number of occupied nodes `tot_max` must be counted instead, and the code adjusted accordingly.

[^insert-complexity]: From the complexity analysis below, these efficiency losses only mean a larger constant factor, and the complexity remains correct. Since checking the tree depth may involve many floating-point logarithm operations, code that does not check the depth and only checks for imbalance may be faster on some data.

[^threshold]: It need not be the same as the parameter chosen for insertion above. Although the original paper makes this assumption, choosing different parameters only changes the constant term in the complexity of a single operation, and the overall complexity remains correct.

[^hei-bal]: By the definition in the original paper, $n$ denotes the number of non-deleted nodes, so one can only guarantee that the tree height does not exceed $\lfloor\log_{1/\alpha}n\rfloor+1$, which is called weak $\alpha$‑height-balance. We do not dwell on this difference in the constant term here.

[^alternative-analysis]: Some articles simply argue that $\Omega(|T_x|)$ insertions correspond to one rebuild, so the amortized complexity is $\dfrac{\Omega(|T_x|)O(\log n)+\Theta(|T_x|)}{\Omega(|T_x|)} = O(\log n)$. This line of thought helps understand why the amortized complexity is correct, but it is not rigorous. This is because a single insertion may correspond to rebuilds at several ancestor nodes, so when a rebuild happens at node $x$, it is not obvious that the number of nodes in the subtree that did not trigger a rebuild is $\Omega(|T_x|)$.
