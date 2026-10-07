---
title: Segment tree basics
---

## Introduction

The segment tree is a data structure commonly used in competitive programming to maintain **interval information**.

A segment tree can perform point updates, point queries, range updates, range queries and similar operations in $O(\log N)$ time.

## Basic structure and operations

A segment tree is a binary tree. Each of its nodes stores the information of one interval:

-   a leaf stores the information of a single element $x$, which can also be viewed as the information of the interval $[x,x]$ of length $1$;
-   the leaves of the subtree rooted at an internal node form a contiguous interval $[l,r]$, and that node stores the information of the interval $[l,r]$.

An internal node always has two children, and its interval is exactly the disjoint union of the intervals of these two children. If an internal node stores the information of the interval $[l,r]~(l < r)$, its two children store the information of $[l,m]$ and $[m+1,r]$ respectively, where $l \le m < r$.

The root of the segment tree stores the information of the whole interval $[L,R]$. The size of the segment tree is expressed by the length $N = R - L + 1$ of this interval.

### Interval information

A segment tree maintains interval information. This section describes the common properties that interval information must satisfy and the corresponding implementation.

In general, **interval information** is a function $\varphi:\mathcal I\rightarrow M$ whose argument is an interval, where $\mathcal I$ denotes the set of all subintervals of $[L,R]$ (including the empty interval) and $M$ denotes the space of values the information can take, called the **information space** in this article. The interval information $\varphi$ stored by a segment tree must satisfy the following properties:

1.  If an interval is split into two subintervals, its information can be obtained by merging the information of the subintervals. That is, if $I$ is the disjoint union of $I_1$ and $I_2$ with $I_1$ to the left of $I_2$, then $\varphi(I)=\varphi(I_1)\circ\varphi(I_2)$, where the operation $\circ$ denotes **merging information**.
2.  If an interval is split into a disjoint union of several subintervals, the result of merging the information of these subintervals is independent of how the interval is split and how the merges are grouped; it always equals the information of the original interval. That is, the operation $\circ$ is associative.
3.  The empty interval $\varnothing$ also has well-defined information $e=\varphi(\varnothing)$. Moreover, since any interval $I$ can be viewed as the disjoint union of itself and the empty interval $\varnothing$, merging any interval information with the information of the empty interval leaves it unchanged. That is, $\varphi(I)\circ e = e\circ\varphi(I) = \varphi(I)$. This says that $e$ is the identity element of the operation $\circ$.

These properties guarantee that, to query the information of an interval $I$, it suffices to find a sequence of nodes whose intervals form a partition of $I$; the information of $I$ can then be merged from the information stored in these nodes.

Interval information can be merged, merging is associative, and an identity element exists. These properties mean that the information space $M$ together with the merge operation $\circ$ forms a [monoid](../math/algebra/basic.md#群).[^monoid]

???+ info "Convention"
    In the reference implementations of segment tree operations in this article, we assume that the elements of the information space $M$ are stored in a struct `Info`, whose default constructor yields the identity element and which overloads the addition operator to implement merging.

???+ example "Examples"
    Many kinds of interval information satisfy the monoid properties. Interval length, interval sum, interval product and interval maximum are simple examples. The corresponding monoids are $(\mathbf N,+),~(\mathbf R,+),~(\mathbf R,\times),~(\mathbf R\cup\{-\infty\},\max)$ respectively, with identity elements $0,0,1,-\infty$. These examples extend to other common operations with the monoid property, such as bitwise XOR, matrix multiplication, function composition and so on.
    
    There are also more complex examples. For instance, the maximum (non-empty) subarray sum of an interval can also be maintained as a monoid. Of course, if only the maximum subarray sum itself is maintained, merging is impossible. For a partition $I = I_1 \cup I_2$, the maximum subarray sum of $I$ may be attained on a subinterval of $I_1$, on a subinterval of $I_2$, or on a subinterval crossing from $I_1$ into $I_2$. To compute the maximum in the last case, one must additionally record the interval sum, the maximum (non-empty) prefix sum and the maximum (non-empty) suffix sum.
    
    === "Interval sum"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-2.cpp:info"
        ```
    
    === "Interval maximum (non-negative values)"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-bisect-recursive.cpp:info"
        ```
    
    === "Linear function"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-recursive.cpp:info"
        ```
    
    === "Maximum non-empty subarray sum"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-1.cpp:info"
        ```

Note that merging interval information is not necessarily commutative. When merging, the subintervals must be processed strictly in order from left to right.

### Recursive construction and storage layouts

To keep the tree height as small as possible, the interval $[l,r]$ of the current node should be split into two parts as evenly as possible. For this, one usually takes

$$
m = \left\lfloor\dfrac{l + r}{2}\right\rfloor.
$$

Then, if the interval of the current node has length $n > 1$, its two children $[l,m]$ and $[m+1,r]$ correspond to intervals of lengths $\lceil n/2\rceil$ and $\lfloor n/2\rfloor$ respectively. The height of the resulting segment tree is $\lceil\log_2N\rceil$. This guarantees that the segment tree is a balanced binary tree and that point operations always take $O(\log N)$.

![](images/seg-1.svg)

To store the information of an interval of length $N$, a segment tree with $N$ leaves must be built. As a full binary tree (every node has $0$ or $2$ children), the segment tree has exactly $2N-1$ nodes storing information. In other words, the space complexity of a segment tree built this way is $\Theta(N)$; during recursive construction each node is visited exactly once, so the time complexity is also $\Theta(N)$.

Although the structure of a segment tree is relatively fixed, its storage layout is not unique.

![](images/seg-2.svg)

The first common layout is heap-style storage (as shown above), i.e. embedding the segment tree into a perfect binary tree. The root then has index $1$; if the current node has index $i$, its left and right children have indices $2i$ and $2i+1$. Since the tree height is $\lceil\log_2N\rceil$, storing the segment tree this way requires an array of length $2^{\lceil\log_2N\rceil + 1}$. For simplicity one usually just allocates an array of length $4N$[^heap-size]; or pads $N$ up to a power of two $N'$ and allocates an array of length $2N'$. The advantage of this layout is that child indices need not be stored; the drawback is that some nodes are unused, so space utilization is not high.

![](images/seg-3.svg)

The second common layout uses a memory pool and assigns node indices dynamically. Since the shape of the segment tree is fixed, indices only need to be assigned once, at build time. This guarantees that there are no unused nodes, and an array of length $2N$ suffices. The node indices are then the preorder traversal numbers of the segment tree. However, since the index of the (right) child cannot be computed from the index of the current node alone[^child-id], one usually allocates additional arrays of total length $4N$ to store the indices of the left and right children. If the space needed for one index is $1$ and the space for one node is $K$, dynamic allocation uses no more space than heap-style storage as soon as $2NK + 4N \le 4NK$, i.e. $K \ge 2$.

These two ways of storing and building a segment tree are implemented as follows:

???+ example "Reference implementation"
    === "Heap-style storage"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-recursive.cpp:build"
        ```
    
    === "Dynamically allocated nodes"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-lazy-recursive.cpp:build"
        ```

???+ tip "Tips"
    1.  When computing the midpoint $m = \lfloor(l+r)/2\rfloor$ of the interval $[l,r]$, using `m = l + (r - l) / 2` instead of `m = (l + r) / 2` avoids integer overflow and problems with negative division rounding toward zero.
    2.  It is usually convenient to implement a `push_up` function that merges the information of the children into the current node.

Apart from the way children are accessed, the choice of storage layout does not affect the implementation of the operations after construction. However, in heap-style storage the index of a node is determined by its position in the perfect binary tree, which is poorly extensible and cannot support extensions such as dynamic node creation and persistence.

### Point update and point query

The simplest segment tree operations are point operations.

Consider the point query first. In a segment tree, the elements stored in the leaves are in order. Hence, when the recursion reaches an internal node, comparing the queried element with the midpoint of the current interval decides whether to continue into the left or the right child. When a leaf is reached, the information stored there is returned. This completes the point query.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-recursive.cpp:point-get"
    ```

The point update is similar. The leaf to be accessed is likewise located top-down. Then the leaf is modified. Finally, when backtracking, the information of all ancestors of that leaf must be updated accordingly. This is the point update. Since every point update can be viewed as replacing the value, only a reference implementation of setting a value is given here. More general updates are discussed in the section on [range updates](#range-updates-and-lazy-tags).

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-recursive.cpp:point-set"
    ```

Since the tree height is $\Theta(\log N)$, the point operations of a segment tree take $O(\log N)$.

### Range query

Next, consider the range query.

![](images/seg-5.svg)

As explained above, it suffices to split the queried interval into a disjoint union of intervals corresponding to segment tree nodes and then merge the information of these nodes in order. Naturally, the fewer nodes the better. This requires the nodes to correspond to **maximal intervals** contained in the query interval. In the figure above, the shaded area marks the operated interval and the nodes with thick borders correspond to maximal intervals. Finding these nodes is easy: starting from the root, search downward through all nodes whose intervals intersect the query interval; when a node completely contained in the query interval is found, a maximal-interval node has been found, so there is no need to search its descendants.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-recursive.cpp:range-get"
    ```

???+ tip "Tips"
    1.  Besides the implementation above, the search may also stop when a node whose interval is disjoint from the query interval is reached.
    2.  Since the result is initialized to the identity element of the information space $M$, the result returned by the left child can overwrite it directly without merging.

It can be shown that the total number of nodes visited during a range query – all maximal-interval nodes and their ancestors – is $O(\log N)$. Hence the complexity of a range query is also $O(\log N)$.

??? note "Proof"
    During a range query, for every visited non-root node, the interval of its parent must contain the left or the right endpoint of the query interval. Otherwise the parent's interval would be either completely contained in the query interval or disjoint from it, and in both cases its children (i.e. the current node) would not be visited. Moreover, intervals of nodes at the same depth are pairwise disjoint, so at most $1$ contains the left endpoint and at most $1$ the right endpoint, and each node has at most $2$ children. Therefore at most $4$ nodes of the same depth are visited during a range query. The height of the segment tree is $\Theta(\log N)$, so the number of nodes visited during a range query is also $O(\log N)$.

### Range updates and lazy tags

Finally, consider the range update.

Unlike the range query, the effect of a range update is not limited to the maximal-interval nodes and their ancestors; it also reaches their descendants. This is because a range update affects the subintervals of these maximal intervals, i.e. the descendants of the corresponding nodes. Modifying every affected node is obviously too expensive and impractical. Therefore, range updates are implemented with the idea of a **lazy tag**. Specifically, each range update actually modifies only the maximal-interval nodes and their ancestors, while the modification of the descendants of the maximal-interval nodes is postponed until necessary. To record the modifications that still have to be performed, a tag is left at the maximal-interval node. This tag records the operations that must be, but have not yet been, applied to its descendants (excluding itself). This is the lazy tag.

???+ info "Convention"
    This article assumes that the modification of a node carrying a lazy tag has itself already been completed. This is not mandatory and may vary between implementations.

In a segment tree supporting range updates, the implementation of the other operations must be adjusted accordingly. During any operation, whenever the children of a node are to be accessed, one must check whether the current node has a lazy tag that has not been cleared. If so, the lazy tag must first be pushed down before accessing the children or performing other operations. Pushing down a lazy tag means applying the corresponding modification to the children of the node, tagging the children with the lazy tag, and finally clearing the tag at the current node.

???+ example "Example"
    The figure below shows the segment tree built from the array $[4,1,3,2,5]$.
    
    ![](images/seg-lazy-1.svg)
    
    At each node, $s$ denotes the sum of the elements of the current interval and $t$ is the lazy tag used to implement range addition. Initially all interval sums are correct and all lazy tags are empty. Now add $2$ to every element of the interval $[2,5]$; the result is shown below.
    
    ![](images/seg-lazy-2.svg)
    
    In the figure, the shaded area marks the operated interval and the nodes with thick borders correspond to maximal intervals. At these maximal-interval nodes the sum $s$ increased by $2$ times the interval length, correctly reflecting the change caused by the range addition; at the same time the lazy tag increased by $2$, indicating that the descendants have not yet been updated. The ancestors of the maximal-interval nodes obtained the updated sums from their children. If we now query the sum of the interval $[4,4]$, the result is shown below.
    
    ![](images/seg-lazy-3.svg)
    
    While accessing the interval $[4,4]$, the interval $[4,5]$ is visited first and is found to carry the lazy tag $t=2$. Before visiting its children, the lazy tag must be pushed down: a range addition of $2$ is applied to each child, the lazy tags of the children also increase by $2$ (indicating that their descendants – although none exist in the figure – have not been updated), and finally the tag at $[4,5]$ is cleared. After pushing down, the child interval $[4,4]$ is visited and the correct sum $4$ is read.

When performing a range update or pushing down a lazy tag, the node to be tagged may already carry an uncleared lazy tag. In that case the tag must not simply be overwritten; it must be updated to the composition of the two operations. Since the composition of operations is not necessarily commutative, the order matters: the new operation is always composed after the existing tag. When pushing down, the parent's tag is always composed after the child's existing tag. This is because tags are always pushed down before a child is accessed, so when the child's existing tag was set, the parent certainly carried no tag; the parent's current tag can only come from later operations.

To record range updates correctly, one must understand the properties such operations must satisfy. Again let the interval information recorded by the segment tree be the function $\varphi:\mathcal I\rightarrow M$. Furthermore, let an update be $\pi:M\rightarrow M$, which transforms old information into new information by some rule. Then a range update $\pi$ must satisfy the following properties:

1.  It is well defined. That is, the result of the range update depends only on the information $m\in M$ and not on the interval $I\in\mathcal I$ it lives on. If the result of a range update involves characteristics of the interval, these characteristics (e.g. interval length, endpoints) can be made part of the interval information.
2.  The update must be compatible with merging. That is, if the information of an interval can be obtained by merging the information of its subintervals, then the result of updating that interval can still be obtained by merging the results of updating the subintervals; i.e. for $m_1,m_2\in M$ we always have $\pi(m_1\circ m_2) = \pi(m_1)\circ\pi(m_2)$.
3.  In particular, the information of the empty interval remains the information of the empty interval after an update, i.e. $\pi(e)=e$.[^endo]

This says that an update is an [endomorphism](../math/algebra/group-theory.md#群同态) of the monoid $M$. Moreover, consider the set $\Pi$ of such updates: as long as it is closed under composition, since composition is associative and the identity map is the identity element, $\Pi$ is also a monoid.

???+ info "Convention"
    In the reference implementations of segment tree operations in this article, we assume that updates are stored in a struct `Transform`, whose default constructor yields the identity operation, which overloads the addition operator to implement composition of operations, and which overloads the call operator (parentheses) to modify interval information. To make it easy to check whether a lazy tag is empty (i.e. modifies nothing), an explicit conversion to `bool` is also overloaded.

???+ example "Examples"
    Segment trees support many updates; range addition, range multiplication, range assignment and range affine transformation are common examples. The difficulty in the implementation often lies not in the operation itself but in how to apply it to the interval information, i.e. how to make it satisfy the three properties above. For example, when maintaining interval sums and supporting range addition, the contribution of the increment to the sum is the added number times the interval length, and the interval length is not part of the interval information. In this case, following the first property, simply include the interval length in the interval information.
    
    === "Interval minimum & range addition"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-perm-recursive.cpp:info"
        --8<-- "docs/ds/code/seg/seg-perm-recursive.cpp:transform"
        ```
    
    === "Interval sum & range addition"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-5.cpp:info"
        --8<-- "docs/ds/code/seg/seg-5.cpp:transform"
        ```
    
    === "Interval maximum & range assignment"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-bisect-recursive.cpp:info"
        --8<-- "docs/ds/code/seg/seg-bisect-recursive.cpp:transform"
        ```

Once the structure storing range updates is implemented, lazy updating and pushing down lazy tags can be implemented as follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-lazy-recursive.cpp:tag"
    ```

???+ tip "Tips"
    1.  Do not put lazy tags on empty nodes.
    2.  With a careful implementation, lazy tags need not be put on leaves either.

A single push-down usually takes $O(1)$.

The range update can then be implemented as follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-lazy-recursive.cpp:range-set"
    ```

Like the range query, the range update of a segment tree with lazy tags also takes $O(\log N)$. The other operations of a segment tree with lazy tags are implemented essentially the same way as without lazy tags; it suffices to add a push-down before accessing the children. Since a single operation pushes down at most $O(\log N)$ tags, the time complexity of these operations remains $O(\log N)$, only with a larger constant. If no range updates are involved, one usually implements a segment tree without lazy tags to reduce the constant factor.

### Reference implementation

Below are complete reference implementations of segment trees without and with lazy tags.

??? example "Reference implementation"
    === "Without lazy tags"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-recursive.cpp:seg-tree"
        ```
    
    === "With lazy tags"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-lazy-recursive.cpp:seg-tree"
        ```

In concrete applications it may be necessary to check whether the updates and queries are valid.

## Common techniques

This section describes several techniques commonly used when solving concrete problems with segment trees. They either improve the constant factor or extend the basic functionality.

### Non-recursive implementation

The recursive segment tree implementations described above can only be traversed recursively from the top down and pay the corresponding recursion overhead. Another approach is to maintain the segment tree bottom-up. In Chinese competitive programming materials this implementation became widespread through Zhang Kunwei, so it is often called the **zkw segment tree**.

![](images/seg-4.svg)

The figure above shows the storage layout of the non-recursive implementation. The segment tree is still embedded into a perfect binary tree, but it is built bottom-up. First, all leaves are stored on the same level at depth $\lceil\log_2N\rceil$; the surplus leaves store the identity element $e$, which can be viewed as the information of the empty interval. Then the internal nodes are traversed bottom-up and the information of the children is merged into the current node. Since all leaves are on the same level, the segment tree built this way differs slightly in structure from the two previous layouts, but it maintains interval information equally well. Space-wise it is the same as heap-style storage: an array of length $2^{\lceil\log_2N\rceil + 1}$ is needed.

The biggest advantage of this layout is that the leaf indices are consecutive and easy to locate, and the indices of parents and children can be computed directly. As shown above, if $n=2^{\lceil\log_2N\rceil}$, i.e. $N$ padded up to a power of $2$, the value of element $x\in[L,R]$ is stored at the node with index $n+x-L$; for a non-root node with index $i$, the parent has index $\lfloor i/2\rfloor$ and, more generally, the $d$-th ancestor has index $\lfloor i/2^d\rfloor$; for an internal node with index $i$, the left and right children have indices $2i$ and $2i+1$.

Thanks to these properties, building and point operations are very easy to implement. Building only requires copying the information of the elements into the corresponding leaves and then traversing the nodes $[1,n-1]$ in reverse order, merging the children's information. A point query directly returns the information stored in the corresponding leaf. A point update likewise directly modifies the corresponding leaf and then updates the information of its ancestors.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-nonrecursive.cpp:build"
    --8<-- "docs/ds/code/seg/seg-nonrecursive.cpp:point-get"
    --8<-- "docs/ds/code/seg/seg-nonrecursive.cpp:point-set"
    ```

![](images/seg-6.svg)

The range query is slightly more complex: all maximal-interval nodes of $[l,r]$ in the segment tree must be found. Ignore the right endpoint of the query for a moment and consider the maximal interval containing the left endpoint $l$. The nodes containing it are the leaf corresponding to $l$ and its ancestors. So, starting from the leaf of $l$, keep jumping up until the current node is the right child of its parent: at that point the parent also contains elements to the left of the current node, which do not belong to the not-yet-counted part, so the interval of the current node is exactly the maximal interval containing $l$. After accumulating its information, move one node to the right on the same level and then jump to the parent; this gives the node containing the leftmost not-yet-counted element, and the procedure repeats. The right endpoint is handled symmetrically. In practice both sides are processed simultaneously until they meet, at which point the query interval has been counted exactly. Note that the information must be accumulated separately on the left and on the right, and the two results merged only at the end, to keep the merge order correct.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-nonrecursive.cpp:range-get"
    ```

???+ tip "Tip"
    Different implementations of the range query differ in small details. The implementation here queries the closed interval $[l,r]$, the [AtCoder Library](https://github.com/atcoder/ac-library/blob/master/atcoder/segtree.hpp#L52-L65) queries $[l,r)$, and Zhang Kunwei's original material queries $(l,r)$. There is no essential difference between the three; only the handling of the boundaries differs.

Finally, consider the range update; the key is handling the lazy tags. Nodes can still be accessed bottom-up, but tags must be pushed down top-down, otherwise not all tags on the root-to-leaf path can be cleared. Hence it suffices to find all ancestors of the maximal-interval nodes and push down their tags in top-down order. For this, note that the parent of a maximal-interval node must contain one of the two endpoints, and all nodes containing an endpoint lie on the path from the root to the leaf of that endpoint. However, not every node on this path is an ancestor of a maximal-interval node: the segment from the maximal-interval node containing that endpoint down to the leaf is not, and should be skipped. So it suffices to push down tags once from the root toward the leaves along the two paths to the leaves of the left and right endpoints, skipping this segment. After the update, the information of the ancestors is updated bottom-up along the same two paths.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-lazy-nonrecursive.cpp:range-set"
    ```

???+ tip "Tips"
    1.  The implementation here still updates the closed interval $[l,r]$; for the half-open version $[l,r)$ see the [AtCoder Library](https://github.com/atcoder/ac-library/blob/master/atcoder/lazysegtree.hpp#L110-L138). Both versions use bit operations and share the same core idea: the segment of nodes to be skipped has its left (right) interval endpoint aligned with the left (right) endpoint of the updated interval.
    2.  For this segment of nodes, skipping during the push-down affects only efficiency, but skipping during the bottom-up pass is mandatory: calling `push_up` on a node that has just received a lazy tag would overwrite it with the not-yet-updated information of its children.

In the non-recursive implementation with lazy tags, the remaining operations likewise only need a root-to-leaf push-down added before the access.

The complete reference implementation of the non-recursive segment tree follows, again in two versions, without and with lazy tags:

??? example "Reference implementation"
    === "Without lazy tags"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-nonrecursive.cpp:seg-tree"
        ```
    
    === "With lazy tags"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-lazy-nonrecursive.cpp:seg-tree"
        ```

Apart from the point query of the segment tree without lazy tags dropping to $O(1)$, the complexities of the other operations are the same as in the recursive version, only with a smaller constant.

In summary, the non-recursive implementation also supports all basic segment tree operations, including range updates and lazy tags. But, like heap-style storage, node indices are determined by position, which requires the whole perfect binary tree to exist in advance; hence dynamic node creation is impossible and persistence is inconvenient.

### Dynamic node creation

All storage layouts described so far require allocating $\Theta(N)$ space at once when the tree is built. This is infeasible when the interval length $N$ is large (e.g. $\sim 10^9$). To save space, the tree does not have to be built all at once: initially only the root representing the whole interval is created, and a child representing a subinterval is created only when it needs to be accessed. Since the node indices are not fixed, a segment tree with dynamic node creation can only be implemented with dynamic allocation from a memory pool, with arrays storing the children's indices.

A prerequisite is that the information corresponding to not-yet-created nodes is known. The simplest case is when the interval information of a not-yet-created node is exactly the identity element $e$ of the information space $M$ (i.e. the information of the empty interval). Then a query on an empty node simply returns $e$, and merging needs no special treatment; nodes are created along the path only when an update needs to write information. The more general case is when the information of a not-yet-created node depends on its interval. In such problems the information must be computed from the endpoints of the current interval when querying an empty node, when creating a new node, and when merging the children's information. In any case, a segment tree with dynamic node creation usually cannot be built from an arbitrary initial array. Moreover, since the node index no longer carries interval information, the interval of the current node must be passed down level by level as a parameter when splitting intervals, as in the recursive implementation; in particular, children must be created before pushing down lazy tags.

![](images/seg-7.svg)

For reference, here are implementations of segment trees with dynamic node creation, without and with lazy tags. Corresponding to the two cases described above, the first assumes that the information of a not-yet-created node is exactly the identity element $e$, and the second assumes that it depends on the interval.

??? example "Reference implementation"
    === "Without lazy tags"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-dynamic.cpp:seg-tree"
        ```
    
    === "With lazy tags"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-lazy-dynamic.cpp:seg-tree"
        ```

???+ tip "Tip"
    Children must be created before pushing down tags, which increases the constant of the space complexity; allocate enough space.

Since each update creates nodes only along at most two root-to-leaf paths, a single operation creates at most $O(\log N)$ new nodes. Hence, after $q$ operations the total number of nodes is $O(q\log N)$, which is exactly why dynamic node creation can handle large intervals. The time complexity is unchanged: a single operation still takes $O(\log N)$. The bound $O(q\log N)$ is very loose. In practice, if the operated intervals overlap heavily, far fewer new nodes are created; conversely, if each operation touches pairwise disjoint intervals, the count approaches this bound. When initializing the segment tree, space should be allocated according to this upper bound.

Dynamic node creation is only one way to solve such problems. If all interval endpoints appearing in the operations are known in advance, they can first be [discretized](../misc/discrete.md) and an ordinary segment tree built over the discretized interval; the effect is the same and the implementation simpler. Dynamic node creation only needs to be considered when the operations are not known in advance (e.g. when the problem is forced online).

In addition, the [persistent segment tree](./persistent-seg.md) is also based on dynamic node creation: each update creates new nodes only along one root-to-leaf path and shares the rest with the old version, so each update needs only $O(\log N)$ extra space.

### Permanent tags

The lazy tags described so far must be pushed down. However, each push-down reads and writes the children, which is not a small constant; moreover, in some situations tags are hard to push down. To avoid pushing down, one can use the method of permanent tags (tag permanence): once a tag is placed it stays there forever and is never pushed down; during a query, the tags on the path from the root to the node are composed and applied to the information stored in the node.

![](images/seg-8.svg)

Following the earlier convention, the tag at node $x$ acts only on its descendants, and the information stored at $x$ already includes the effect of this tag. In other words, the information at $x$ is the information of the interval of $x$ without taking the tags of its ancestors into account. Taking the recursive implementation as an example, the range operations of the segment tree are implemented as follows:

-   Range update: recurse top-down. When a maximal-interval node is reached, place the tag there, update its information and return immediately without descending. When backtracking, merge the information of the children into the current node and then apply the tag of the current node to it.
-   Range query: recurse top-down. When a maximal-interval node is reached, directly return its stored information. When backtracking, merge the results of the children and then apply the tag of the current node to them; going up level by level, the tags of all nodes on the path are thus applied to the result.

The time complexity of both operations is still $O(\log N)$, but without any push-down, so the constant is smaller. The non-recursive implementation is similar, with recursion replaced by iteration. The reference implementations are:

??? example "Reference implementation"
    === "Recursive implementation"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-perm-recursive.cpp:seg-tree"
        ```
    
    === "Non-recursive implementation"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-perm-nonrecursive.cpp:seg-tree"
        ```

However, permanent tags are not always feasible; they impose an additional requirement on the updates. The composition of updates must be **commutative**. As explained above, the composition of lazy tags is not necessarily commutative, and pushing down guarantees the correct order because a tag is pushed down before every access to a child, so on a root-to-leaf path the tag closer to the root always corresponds to a later operation. Permanent tags give up exactly this property: a tag always stays where it is, its position is determined by the updated interval and does not depend on the order of operations. Hence the tag at an ancestor may be either earlier or later than the tag at a descendant. During a query the tags are composed in root-to-leaf order, which gives the correct result only if the composition is commutative.

???+ example "Examples"
    Range addition, range multiplication and similar operations are commutative, so permanent tags are possible. Range affine transformation (i.e. simultaneous addition and multiplication) and range assignment[^assign] are not commutative, so permanent tags are impossible.

Permanent tags are often applied in the [persistent segment tree](./persistent-seg.md) and in various nested trees (tree-in-tree). In both cases pushing down is expensive; permanent tags, even if not strictly necessary, are often the more convenient choice. In some problems tags cannot be pushed down at all (see the "union area of rectangles" example below), and then permanent tags are the only option.

### Binary search on the segment tree

Some problems require a binary search over the array. For instance, given $l$, find the largest $r$ such that the information of the interval $[l,r]$ satisfies some condition. The direct approach is to binary search $r$ and query the interval information with the segment tree each time, giving $O(\log^2 N)$. However, the segment tree is itself a binary structure; performing the binary search on the tree itself achieves $O(\log N)$.

Again let the information stored by the segment tree be $\varphi:\mathcal I\rightarrow M$. Let the condition be a predicate $g:M\rightarrow\{\text{True},\text{False}\}$ on the information space $M$. For the binary search to make sense, $g$ must be **monotone** (with respect to merging on the right): if $g(m)$ is false, then $g(m\circ m')$ is false for every $m'$. In other words, once the interval has been extended to the right so far that the condition fails, the condition never holds again. In addition, $g(e)$ must be true, i.e. the empty interval always satisfies the condition. The problem thus becomes: given $l$, find the largest $r$ such that $g(\varphi([l,r]))$ is true; if already $g(\varphi([l,l]))$ is false, the answer is by convention $l-1$.

![](images/seg-9.svg)

In the recursive implementation, the binary search is performed by recursing top-down while maintaining the accumulated information $m$, which represents the information of the part of the interval already known to belong to the answer. When the recursion reaches a node whose interval $I$ lies entirely within $[l,R]$, first try to include the whole node: compute $m\circ\varphi(I)$; if $g$ is still true, the whole node can be included, so update $m$ and return the right endpoint of the node; otherwise the boundary of the answer lies inside this node and the recursion must continue downward. If the condition fails even at a leaf, the boundary is exactly there.

The complexity is still $O(\log N)$. Indeed, only two kinds of nodes continue the recursion downward: those whose interval extends beyond $[l,R]$ – all of which lie on the path from the root to $l$ – and those whose inclusion would make $g$ false – among which only the nodes on the path containing the boundary actually descend, at most one per level. Both kinds have only $O(\log N)$ nodes, and all other nodes are either included whole or skipped whole.

![](images/seg-10.svg)

The non-recursive implementation divides the procedure into two phases. First bottom-up: starting from the leaf of $l$, jump upward while the current node is a left child, until it becomes a right child; then the left endpoint of its interval is aligned with the not-yet-included part, so try to include the whole node; if that succeeds, move one node to the right and continue jumping upward. As soon as including some node makes $g$ false, switch to the top-down descent: descend inside that node and at each level first try to include the left child; if that succeeds, move into the right child, otherwise enter the left child, down to a leaf – that is the boundary. Each phase walks a single path, so the complexity is also $O(\log N)$.

Symmetrically, one may be given $r$ and asked for the smallest $l$ such that $g(\varphi([l,r]))$ is true. Then the accumulated information must be merged from right to left, i.e. computing $\varphi(I)\circ m$, to keep the merge order correct; when there is no solution, the answer is by convention $r+1$. Here $g$ must be monotone with respect to merging on the left: if $g(m)$ is false, then $g(m'\circ m)$ is false for every $m'$.

??? example "Reference implementation"
    === "Recursive implementation"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-bisect-recursive.cpp:max-right"
        --8<-- "docs/ds/code/seg/seg-bisect-recursive.cpp:min-left"
        ```
    
    === "Non-recursive implementation"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-bisect-nonrecursive.cpp:max-right"
        --8<-- "docs/ds/code/seg/seg-bisect-nonrecursive.cpp:min-left"
        ```

???+ tip "Tips"
    1.  With lazy tags, tags must also be pushed down before descending into the children. In the non-recursive implementation, the tags along the path from the root to $l$ must be pushed down once before the upward phase.
    2.  If the condition depends only on the information of the current node itself (e.g. "does the interval contain an element greater than $x$"), the accumulated information need not be maintained and the implementation is simpler.
    3.  In the non-recursive implementation the surplus leaves store the identity element, on which $g$ is always true, so the upward phase may pass over them. In that case $R$ should be returned directly rather than computing the position from the node index.

### Segment tree on values

The segment trees so far were built over array indices. However, the segment tree does not care about the meaning of the indices. If it is built over the value domain, i.e. the leaf corresponding to the element $v$ records how many times the value $v$ occurs in a multiset, we obtain a **segment tree on values** (also called a weight segment tree; Chinese 权值线段树).

![](images/seg-11.svg)

Such a segment tree can be used as a set supporting the usual operations of a [balanced tree](./bst.md), and all of them follow directly from the operations described above:

-   Inserting an element $v$ is a point increment at position $v$.
-   Deleting an element $v$ is a point decrement at position $v$; one must check that the element exists.
-   Querying the rank of $v$ is the sum over the value interval $[L,v-1]$ plus one.
-   Querying the $k$-th smallest element: binary search on the segment tree for the largest $r$ such that the number of elements in the value interval $[L,r]$ is less than $k$; then $r+1$ is the answer. Since counts can be subtracted, during the descent it suffices to compare the count of the left child with $k$, without maintaining accumulated information.
-   Querying the predecessor and successor can be done via the rank and $k$-th smallest operations.

Compared to the usual balanced trees, the segment tree on values is much simpler to implement and has a smaller constant; the price is that it can only handle elements from the value domain and does not support operations such as interval reversal that depend on the tree structure itself.

Since the value domain is usually much larger than the number of elements, building directly is often infeasible. If all elements are known in advance, the value domain should be [discretized](../misc/discrete.md) and an ordinary segment tree built; otherwise dynamic node creation is needed. In the latter case the information of the nodes for values that do not occur is exactly the identity element – precisely the simplest case described above.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/seg/seg-as-bst.cpp:seg-tree"
    ```

The segment tree on values is the most common basis for extensions such as the [persistent segment tree](./persistent-seg.md) and segment tree merging. The former enables querying the $k$-th smallest element in a subarray, the latter efficiently merges two sets.

## Extensions

Segment trees have very wide applications; common extensions and variants include:

-   [persistent segment tree](./persistent-seg.md)
-   various nested trees:
    -   [segment tree in segment tree](./seg-in-seg.md)
    -   [segment tree in Fenwick tree](./seg-in-bit.md)
    -   [balanced tree in segment tree](./balanced-in-seg.md)
    -   [segment tree in balanced tree](./seg-in-balanced.md)
-   [Li Chao tree](./li-chao-tree.md)
-   [cat tree](./cat-tree.md)
-   [Segment Tree Beats](./seg-beats.md)

See the corresponding pages for details.

## Example problems

So far we have described the basic principles of the segment tree and given several templates. However, the implementation of a segment tree is very flexible. The reference implementations in this section do not strictly follow the templates.

???+ example "[Library Checker - Point Add Range Sum](https://judge.yosupo.jp/problem/point_add_range_sum)"
    Given an array, perform the following operations:
    
    -   add $x$ to the $p$-th number;
    -   compute the sum of the elements in the interval $[l,r)$.

??? note "Solution"
    It suffices to implement a segment tree with point updates and range queries.
    
    === "Implementation 1"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-2.cpp"
        ```
    
    === "Implementation 2"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-3.cpp"
        ```

???+ example "[Luogu P3372【模板】线段树 1](https://www.luogu.com.cn/problem/P3372)"
    Given an array, perform the following two operations:
    
    -   add $k$ to every number in some interval;
    -   compute the sum of the numbers in some interval.

??? note "Solution"
    It suffices to implement a segment tree with range updates and range queries. Note that range addition requires maintaining the length of the current interval as part of the information, or computing it from the interval endpoints during the update.
    
    === "Implementation 1"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-5.cpp"
        ```
    
    === "Implementation 2"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-4.cpp"
        ```

???+ example "[Luogu P3373【模板】线段树 2](https://www.luogu.com.cn/problem/P3373)"
    Given an array, perform the following three operations:
    
    -   multiply every number in some interval by $x$;
    -   add $x$ to every number in some interval;
    -   compute the sum of the numbers in some interval.

??? note "Solution"
    It suffices to implement a segment tree with range updates and range queries. One can directly implement a range affine transformation, which supports addition and multiplication simultaneously. If two lazy tags are used, one for addition and one for multiplication, care must be taken with the order in which they are pushed down.
    
    === "Implementation 1"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-7.cpp"
        ```
    
    === "Implementation 2"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-6.cpp"
        ```

???+ example "[SPOJ GSS3 - Can you answer these queries III](https://www.spoj.com/problems/GSS3/)"
    Given an array, perform the following operations:
    
    -   set the $x$-th number to $y$;
    -   compute the maximum non-empty subarray sum within the interval $[x,y]$.

??? note "Solution"
    It suffices to implement a segment tree with point updates and range queries. The way to maintain the maximum non-empty subarray sum was analyzed [above](#interval-information). In this problem merging is not commutative, so care must be taken with the merge order in the implementation.
    
    ```cpp
    --8<-- "docs/ds/code/seg/seg-1.cpp"
    ```

???+ example "[Luogu P13825【模板】线段树 1.5](https://www.luogu.com.cn/problem/P13825)"
    An array $\{a_i\}$ of length $n\le 10^9$ initially has $a_i = i$. Perform the following operations:
    
    -   add $k$ to every number in some interval;
    -   compute the sum of the numbers in some interval.

??? note "Solution"
    Since $n$ is too large, the tree cannot be built directly; dynamic node creation is needed. Moreover, the information of a not-yet-modified interval is not the identity element, so the information of an empty node must be computed from the endpoints of its interval, and a newly created node must be initialized accordingly. This means that the endpoints of the current interval must be passed down when pushing down tags and merging the children's information.
    
    In this problem the contribution of the initial values can actually be computed separately, and the segment tree only maintains the increment of each element. Then the increment sum of an empty node is $0$, exactly the identity element, so interval endpoints no longer matter when creating nodes and merging information; however, range addition still needs the interval length, which is then available only as a recursion parameter and cannot be made part of the information.
    
    Since the problem is not forced online, one can also store all operations first, discretize the endpoints and then use an ordinary segment tree. After discretization each leaf corresponds to a contiguous interval of the original array, so its information must be initialized according to the length and the element sum of that interval.
    
    === "Implementation 1"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-8.cpp"
        ```
    
    === "Implementation 2"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-9.cpp"
        ```
    
    === "Implementation 3"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-10.cpp"
        ```

???+ example "[Luogu P5490【模板】扫描线 & 矩形面积并](https://www.luogu.com.cn/problem/P5490)"
    Compute the area of the union of $n$ axis-parallel rectangles.

??? note "Solution"
    This is a template problem for the [sweep line](../geometry/scanning.md#area-of-the-union-of-rectangles-in-the-plane). See that page for the details of transforming the problem with a sweep line; here we only discuss the data structure after the transformation. We need a structure supporting range increments and decrements of a cover count: each operation increases or decreases the cover count of some interval by one, and each query asks for the total length of positions whose cover count is at least one.
    
    Consider implementing these range operations with a segment tree. The natural idea is to maintain at each node the cover count of the interval and the total length of the part covered at least once. However, when an interval is fully covered, the information about which subintervals were covered is lost from the total length, so it cannot be recovered after this layer of cover is removed. The solution is to record the two kinds of operations separately: the cover count only includes operations covering exactly the whole interval, and the total length only includes covers recorded in the descendants. Then the actually covered length of the interval is: the interval length if the cover count is positive, otherwise the recorded total length. When merging, the actually covered lengths of both children are added to form the total length of this node. Consequently the cover count can no longer be pushed down, because adding and removing the same cover land on the same set of nodes, and only if the count stays in place can they cancel each other out. This is exactly tag permanence.
    
    Of course, the problem can also be solved with the segment tree template above. It suffices to take as interval information the minimum cover count in the interval and the total length of the part where this minimum is attained. It is easy to verify that this information space is a monoid and that incrementing and decrementing the cover count is an endomorphism of it, so the range update and query can be taken from the template. The total covered length is obtained by subtracting the length of the part with cover count zero from the length of the whole interval; the latter is the recorded length if the minimum cover count is zero, and zero otherwise.
    
    === "Implementation 1"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-11.cpp"
        ```
    
    === "Implementation 2"
        ```cpp
        --8<-- "docs/ds/code/seg/seg-12.cpp"
        ```

???+ example "[Luogu P2894【USACO08FEB】Hotel G](https://www.luogu.com.cn/problem/P2894)"
    There are $n$ rooms, all initially empty. Perform the following operations:
    
    -   find $x$ consecutive empty rooms; if they exist, let guests move in;
    -   the rooms $[x,x+y-1]$ are vacated.
    
    For every operation of the first kind, output the smallest room number among the $x$ consecutive empty rooms; if they do not exist, return $0$.

??? note "Solution"
    Build a segment tree maintaining for every interval the maximum length of consecutive empty rooms. To merge this information one must also maintain the longest empty prefix, the longest empty suffix and the interval length: the consecutive empty rooms crossing the middle are exactly the longest suffix of the left subinterval joined with the longest prefix of the right one. The lazy tag only needs range assignment, i.e. setting the whole interval to empty or occupied; the case of no modification is recorded by a special value (e.g. $-1$). For the smallest available room number, it suffices to find the smallest $r$ such that the maximum length of consecutive empty rooms in $[1,r]$ is at least $x$; the room number is then $r-x+1$. This is done by binary search on the segment tree.
    
    ```cpp
    --8<-- "docs/ds/code/seg/seg-13.cpp"
    ```

???+ example "[Luogu P1168 中位数](https://www.luogu.com.cn/problem/P1168)"
    Given an array of length $n$, for every odd $i\le n$ output the median of the first $i$ numbers.

??? note "Solution"
    The median depends only on the relative order of the elements, not on their positions in the array, so it can be maintained with a segment tree on values. Insert the elements one by one and, after every odd number of inserted elements, query the $(i+1)/2$-th smallest element. It suffices to implement insertion and the $k$-th smallest query.
    
    ```cpp
    --8<-- "docs/ds/code/seg/seg-14.cpp"
    ```

## Exercises

Basic implementation and designing interval information:

-   [Luogu P2574 XOR 的艺术](https://www.luogu.com.cn/problem/P2574)
-   [Luogu P4588【TJOI2018】数学计算](https://www.luogu.com.cn/problem/P4588)
-   [Luogu P1253 扶苏的问题](https://www.luogu.com.cn/problem/P1253)
-   [Luogu P1471 方差](https://www.luogu.com.cn/problem/P1471)
-   [Luogu P4513 小白逛公园](https://www.luogu.com.cn/problem/P4513)
-   [Luogu P2572【SCOI2010】序列操作](https://www.luogu.com.cn/problem/P2572)

Dynamic node creation:

-   [Codeforces 915 E. Physical Education Lessons](https://codeforces.com/problemset/problem/915/E)
-   [Library Checker - Range Affine Range Sum (Large Array)](https://judge.yosupo.jp/problem/range_affine_range_sum_large_array)
-   [Codeforces 817 F. MEX Queries](https://codeforces.com/problemset/problem/817/F)

Permanent tags:

-   [Luogu P1502 窗口的星星](https://www.luogu.com.cn/problem/P1502)
-   [2018 Multi-University Training Contest 5 G. Glad You Came](https://acm.hdu.edu.cn/showproblem.php?pid=6356)

Binary search on the segment tree:

-   [AtCoder Library Practice Contest J - Segment Tree](https://atcoder.jp/contests/practice2/tasks/practice2_j)
-   [AtCoder Beginner Contest 292 Ex - Rating Estimator](https://atcoder.jp/contests/abc292/tasks/abc292_h)
-   [Luogu P4137 Rmq Problem/mex](https://www.luogu.com.cn/problem/P4137)
-   [Codeforces 773 E. Blog Post Rating](https://codeforces.com/problemset/problem/773/E)
-   [Codeforces 407 E. k-d-sequence](https://codeforces.com/problemset/problem/407/E)
-   [Codeforces 671 E. Organizing a Race](https://codeforces.com/problemset/problem/671/E)

Segment tree on values:

-   [Luogu P1908 逆序对](https://www.luogu.com.cn/problem/P1908)
-   [Luogu P1801 黑匣子](https://www.luogu.com.cn/problem/P1801)
-   [Luogu P1637 三元上升子序列](https://www.luogu.com.cn/problem/P1637)
-   [Luogu P2286【HNOI2004】宠物收养场](https://www.luogu.com.cn/problem/P2286)

## Application: optimizing graph construction with a segment tree

When building graphs, we sometimes encounter problems where one vertex must be connected by edges to every vertex of a contiguous interval, or a contiguous interval of vertices to one vertex. If the edges were actually added one by one, the complexity would explode as soon as there are many vertices; here the interval property of the segment tree optimizes the graph construction.

Below is a segment tree.

![](./images/segt5.svg)

Each node represents an interval; suppose we need to connect edges to the interval $[2, 4]$.

![](./images/segt6.svg)

Some problems also have the case where an interval must be connected to a single vertex; then all directed edges in the first figure are simply reversed. The tree above is called the in-tree, the one below the out-tree.

![](./images/segt7.svg)

???+ note "[Legacy](https://codeforces.com/problemset/problem/786/B)"
    Problem summary: given $n$ vertices and $q$ operations. Each operation is one of three types:
    
    -   type 1: add a directed edge $u \rightarrow v$ of weight $w$;
    -   type 2: for every $i \in [l,r]$, add a directed edge $u \rightarrow i$ of weight $w$;
    -   type 3: for every $i \in [l,r]$, add a directed edge $i \rightarrow u$ of weight $w$.
    
    Compute the shortest paths from vertex $s$ to the other vertices.
    
    $1 \le n,q \le 10^5, 1 \le w \le 10^9$.
    
    ??? note "Sample code"
        ```cpp
        --8<-- "docs/ds/code/seg/seg_8.cpp"
        ```

## References and notes

-   [统计的力量 – Zhang Kunwei (Chinese)](https://github.com/hzwer/shareOI/blob/master/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/%E7%BB%9F%E8%AE%A1%E7%9A%84%E5%8A%9B%E9%87%8F%E2%80%94%E2%80%94%E7%BA%BF%E6%AE%B5%E6%A0%91%E5%85%A8%E6%8E%A5%E8%A7%A6_%E5%BC%A0%E6%98%86%E7%8E%AE.pptx)
-   [Generalizing Segment Trees by Eklavya](https://sharmaeklavya2.github.io/blog/generalizing-segment-trees.html)
-   [线段树进阶 Part 1 by Alex\_Wei – Luogu (Chinese)](https://www.luogu.com.cn/article/r1mp3hga)

[^monoid]: Strictly speaking, the information maintained by a segment tree only needs to form a semigroup; the existence of an identity element is not necessary. The recursive implementation uses the identity element usually because the range query takes it as the initial value of the accumulated information; this can be avoided by distinguishing cases according to the intersection. However, the surplus leaves in the non-recursive implementation and the empty nodes in dynamic node creation cannot avoid the identity element. In the worst case, even when it is necessary, one can always add an element $e$ to the semigroup $S$ and stipulate that the result of operating $e$ with any element is that element, obtaining the monoid $S\cup\{e\}$. For simplicity of exposition, this article always assumes that the maintained information has a monoid structure.

[^endo]: Similarly to the discussion of interval information, in many implementations the identity element is never an input of an update, so this property is unnecessary; it suffices for the update to be a semigroup endomorphism. However, in the non-recursive implementation of permanent tags below, the initial value of the accumulated information is exactly the identity element, and the tags on the path are applied to it level by level, so this property cannot be ignored. For simplicity of exposition, this article always assumes that an update is a monoid endomorphism.

[^child-id]: In fact, when nodes are numbered in preorder as in the figure, the index of the right child can be computed from the index of the current node and the size of the left subtree, and the size of the left subtree can be computed from the interval length. Since the interval endpoints are usually maintained when accessing segment tree nodes recursively, the index of the right child can also be computed directly.

[^heap-size]: Consider the ratio of the space $2^{\lceil\log_2N\rceil+1}$ occupied by the binary tree to the size $N$ of the segment tree. The former depends only on the height of the binary tree. When the height of the segment tree is $k$, the smallest size of the segment tree is $N = 2^{k-1}+1$. The corresponding ratio is $(4N-4)/N = 4 - 4/N$, with supremum $4$. Therefore, to store a segment tree of size $N$, the corresponding perfect binary tree needs an array of size $4N$.

[^assign]: Range assignment by itself is not commutative. If a timestamp $t$ is recorded together with the assignment, and the composition of the tags $(v_1,t_1)$ and $(v_2,t_2)$ is defined to be the one with the larger timestamp, a commutative tag is obtained. With this method one can implement a segment tree with permanent tags supporting range assignment and point queries: during a query, take the tag with the largest timestamp along the path and apply it to the leaf. However, range queries are impossible, because $(v,t)$ is not an endomorphism of the information space: the interval information cannot tell which positions have already been overwritten by a later assignment.
