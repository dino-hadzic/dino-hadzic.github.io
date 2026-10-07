---
title: Splay tree
---

This page briefly introduces how to maintain a binary search tree with a Splay tree.

## Definition

A **Splay tree** is a self-balancing binary search tree that repeatedly rotates some node to the root by the **splay operation**, so that the whole tree still satisfies the binary search tree property and insertion, lookup and deletion can be done in amortized $O(\log n)$ time.[^degen]

Splay trees were invented by Daniel Sleator and Robert Tarjan in 1985.

## Basic structure and operations

This section discusses the basic structure of a Splay tree and its core operations, the most important of which is the splay operation.

A Splay tree is a binary search tree, i.e. every node in the tree satisfies the property: the value of any node in the left subtree $<$ the value of this node $<$ the value of any node in the right subtree.

### Maintained information

This article implements the Splay tree with arrays simulating pointers, and needs to maintain the following information:

|   rt  |    id   | fa\[i] | ch\[i]\[0/1] | val\[i] | cnt\[i] | sz\[i] |
| :---: | :-----: | :----: | :----------: | :-----: | :-----: | :----: |
| index of the root | number of nodes used |   parent   |    indices of the left and right children    |   value of the node  |  multiplicity of the value |  subtree size  |

At initialization, all information is simply set to zero.

### Auxiliary operations

First, some simple auxiliary operations:

-   `dir(x)`: determines whether node $x$ is the left or the right child of its parent;
-   `push_up(x)`: after the position of a node changes, updates the information of node $x$ from the information of its children.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:aux"
    ```

### Rotations

To keep the Splay tree balanced, rotations are needed. A rotation moves some node one position upward.

A rotation must guarantee:

-   the in-order traversal of the whole Splay tree is unchanged (the binary search tree property must not be broken);
-   the information maintained by the affected nodes remains correct and valid;
-   `rt` must point to the root after the rotation.

There are two kinds of rotations in a Splay tree: left rotation and right rotation.

![](./images/splay-rotate.svg)

From the figure one sees that if we want to move node $x$ ($1$ in the left rotation and $2$ in the right rotation) upward by a rotation, then the direction of the rotation is uniquely determined by whether this node is the left or the right child of its parent. Therefore, when implementing the rotation, it suffices to pass in only the node $x$ to be moved up.

The concrete steps of a rotation are as follows (let the node to be moved up be $x$, taking the right rotation as an example):

1.  First, record the parent $y$ of node $x$ and the parent $z$ of $y$ (possibly empty), and record whether $x$ is the left or the right child of $y$;
2.  In bottom-up order of the tree after the rotation, set the left child of $y$ to the right child of $x$, the right child of $x$ to $y$, and, if $z$ is non-empty, the child of $z$ to $x$;
3.  In the same order, set the parent of the current left child of $y$ (if it exists) to $y$, the parent of $y$ to $x$, and the parent of $x$ to $z$;
4.  Maintain the node information from the bottom up.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:rotate"
    ```

When implementing all functions, take care not to modify the information of node $0$.

### Splay operation

A Splay tree requires that after every access to a node $x$, that node is forcibly rotated to the root. This operation is also called the splay operation.

Let the node just accessed be $x$. Splaying consists of performing a sequence of **splay steps** on $x$. After each splay step on $x$, $x$ gets closer to the root. Define $p$ as the parent of $x$. There are three kinds of splay steps:

1.  **zig**: performed when $p$ is the root. The Splay tree rotates on the edge between $x$ and $p$. **zig** handles the parity of the depth, and is performed only as the last step of a splay operation, and only when $x$ had odd depth at the beginning of the splay operation.

    ![splay-zig](./images/splay-zig.svg)

    That is, directly rotate $x$ right or left (figures 1, 2).

    ![Figure 1](./images/splay-rotate1.svg)![Figure 2](./images/splay-rotate2.svg)

2.  **zig-zig**: performed when $p$ is not the root and $x$ and $p$ are both right children or both left children. The example figure below shows the case where $x$ and $p$ are both left children. The Splay tree first rotates on the edge joining $p$ with its parent $g$, and then rotates on the edge joining $x$ and $p$.

    ![splay-zig-zig](./images/splay-zig-zig.svg)

    That is, first rotate $p$ right or left, then rotate $x$ right or left (figures 3, 4).

    ![Figure 3](./images/splay-rotate3.svg)![Figure 4](./images/splay-rotate4.svg)

3.  **zig-zag**: performed when $p$ is not the root and one of $x$ and $p$ is a right child while the other is a left child. The Splay tree first rotates on the edge between $p$ and $x$, and then rotates on the newly created edge between $x$ and $g$ after the rotation.

    ![splay-zig-zag](./images/splay-zig-zag.svg)

    That is, rotate $x$ first left then right, or first right then left (figures 5, 6).

    ![Figure 5](./images/splay-rotate5.svg)![Figure 6](./images/splay-rotate6.svg)

???+ tip "Tip"
    Readers are encouraged to simulate the $6$ rotation cases themselves to understand the basic idea of the splay operation.

Comparing the three kinds of splay steps, the key to deciding which operation to use is to check whether $x$ is a child of the root, and whether $x$ and its parent are on the same side of their respective parents.

The implementation provided here allows specifying an arbitrary root $z$ and moves any node $x$ in its subtree up to the position of $z$:

1.  First record the parent $w$ of the root $z$, so that `fa[x] == w` can be used to check whether $x$ is already at the root;
2.  Record the current parent $y$ of $x$; if $y$ and $w$ are the same, $x$ has already reached the root;
3.  Otherwise, use `fa[y] == w` to check whether $y$ is the root. If so, directly perform a zig step to rotate $x$; if not, use `dir(x) == dir(y)` to decide between zig-zig and zig-zag: the former first rotates $y$ then $x$, the latter rotates $x$ twice.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:splay"
    ```

The splay operation is the core operation of the Splay tree and the key step that guarantees its time complexity. Make sure to perform a splay operation after every downward access to a node.

Moreover, the splay operation updates, from the bottom up, the information of all nodes on the path from the current node $x$ to the root $z$. Precisely because of this, one can modify a non-root node and then move it up to the root by splaying to complete the information update of the whole tree.

### Time complexity

The complexity of $m$ splay operations on a Splay tree of size $n$ is $O((m+n)\log n)$, and the amortized complexity of a single operation is $O(\log n)$.

??? note "Complexity proof based on the potential method"
    For this it suffices to analyze the complexity of the three operations **zig**, **zig-zig** and **zig-zag**. To do so, we use the **potential method**, deriving the amortized complexity of the operations by studying the change of potential. Suppose $m$ splay operations are performed on a Splay tree containing $n$ nodes; the analysis goes as follows:
    
    **Definitions**:
    
    1.  **Potential of a single node**: $w(x) = \log(\text{size}(x))$, where $\text{size}(x)$ denotes the size of the subtree rooted at node $x$.
    2.  **Potential of the whole tree**: $\varphi = \sum w(x)$, i.e. the sum of the potentials of all nodes in the tree; the initial potential satisfies $\varphi_0 \leq n \log n$.
    3.  **Amortized cost of the $i$-th operation**: $c_i = t_i + \varphi_i - \varphi_{i-1}$, where $t_i$ is the actual cost of the operation, and $\varphi_i$ and $\varphi_{i-1}$ are the potentials after and before the operation respectively.
    
    **Properties**:
    
    1.  If $p$ is the parent of $x$, then $w(p) \geq w(x)$, i.e. the potential of a parent is no less than that of its child.
    
    2.  Since the subtree size of the root does not change before and after the operation, the potential of the root stays unchanged during the operation.
    
    3.  If $\text{size}(p)\ge\text{size}(x)+\text{size}(y)$, then $2w(p) - w(x) - w(y) \geq 2$.
    
    ??? note "Proof of property 3"
        By the AM–GM inequality,
        
        $$
        \begin{aligned}
        2w(p) - w(x) - w(y) 
        &= \log\dfrac{\text{size}(p)^2}{\text{size}(x)\cdot\text{size}(y)} \\
        &\ge \log\dfrac{\left(\text{size}(x)+\text{size}(y)\right)^2}{\text{size}(x)\cdot\text{size}(y)} \\
        &\ge \log 4 \\
        &= 2.
        \end{aligned}
        $$
    
    Next, we carry out the potential analysis for the **zig**, **zig-zig** and **zig-zag** operations respectively. Let the potentials of node $x$ before and after the operation be $w(x)$ and $w'(x)$. The notation for the nodes is the same as [above](#splay-operation).
    
    **zig**: by properties 1 and 2, $w(p) = w'(x)$ and $w'(x) \geq w'(p)$. Hence the amortized cost is
    
    $$
    \begin{aligned}
    c_i &= 1 + w'(x) + w'(p) - w(x) - w(p)\\
    &= 1 + w'(p) - w(x)\\
    &\leq 1 + w'(x) - w(x).
    \end{aligned}
    $$
    
    **zig-zig**: by properties 1 and 2, $w(g) = w'(x)$, $w'(x) \geq w'(p)$ and $w(x) \leq w(p)$. Since
    
    $$
    \begin{aligned}
    \text{size}'(x) 
    &= 3 + \text{size}(A) + \text{size}(B) + \text{size}(C) + \text{size}(D) \\
    &> (1 + \text{size}(A) + \text{size}(B)) + (1 + \text{size}(C) + \text{size}(D)) \\
    &= \text{size}(x) + \text{size}'(g),
    \end{aligned}
    $$
    
    by property 3 we get
    
    $$
    2 w'(x) - w(x) - w'(g) \geq 2.
    $$
    
    Hence the amortized cost is
    
    $$
    \begin{aligned}
    c_i &= 2 + w'(x) + w'(p) + w'(g) - w(x) - w(p) - w(g) \\
    &= 2 + w'(p) + w'(g) - w(x) - w(p) \\
    &\le (2 w'(x) - w(x) - w'(g)) + w'(p) + w'(g) - w(x) - w(p) \\
    &= 2(w'(x)-w(x)) + w'(p) - w(p) \\
    &\le 3(w'(x)-w(x)).
    \end{aligned}
    $$
    
    **zig-zag**: by properties 1 and 2, $w(g) = w'(x)$ and $w(p) \geq w(x)$. Since $\text{size}'(x)>\text{size}'(p)+\text{size}'(g)$, by property 3 we get
    
    $$
    2 \cdot w'(x) - w'(g) - w'(p) \geq 2.
    $$
    
    Hence the amortized cost is
    
    $$
    \begin{aligned}
    c_i &= 2 + w'(x) + w'(p) + w'(g) - w(x) - w(p) - w(g) \\
    &= 2 + w'(p) + w'(g) - w(x) - w(p) \\
    &\le (2w'(x) - w'(g) - w'(p)) + w'(p) + w'(g) - w(x) - w(p) \\
    &= 2w'(x) - w(x) - w(p) \\
    &\le 2(w'(x) - w(x)).
    \end{aligned}
    $$
    
    **A single splay operation**:
    
    Let $w^{(j)}(x)=(w^{(j-1)})'(x)$ and $w^{(0)}(x)=w(x)$. Suppose a splay operation consists of $k$ splay steps in total and finally moves node $x_{1}$ up to the root. This necessarily goes through several **zig-zig** and **zig-zag** operations and at most one **zig** operation; the amortized cost of the first two kinds does not exceed $3(w'(x)-w(x))$, while the amortized cost of the last one does not exceed $3(w'(x) - w(x))+1$, so the total amortized cost does not exceed
    
    $$
    3(w^{(k)}(x_1) - w^{(0)}(x_1)) + 1 \le 3\log n + 1.
    $$
    
    Therefore, the amortized complexity of one splay operation is $O(\log n)$. Consequently, the time complexity of insertion, query, deletion and other operations based on splaying is also amortized $O(\log n)$.
    
    **Conclusion**:
    
    After $m$ splay operations, the actual cost is
    
    $$
    \begin{aligned}
    \sum_{i=1}^m t_i &= \sum_{i=1}^m \left(c_i + \varphi_{i-1} - \varphi_i \right) \\
    &= \sum_{i=1}^m c_i + \varphi_0 - \varphi_m \\
    &\le m(3\log n+1) + n\log n.
    \end{aligned}
    $$
    
    Therefore, the actual time complexity of $m$ splay operations is $O((m+n)\log n)$.

??? info "Why does the rebalancing operation of the Splay tree achieve amortized $O(\log n)$ complexity?"
    The naive rebalancing idea is to repeatedly rotate a node upward until it becomes the root. The problem with this naive idea is that, for a chain-shaped tree in which all children are left (right) children, it amounts to repeatedly performing **zig** operations, so the constant term $1$ in the amortized complexity of **zig** keeps accumulating, and the final amortized complexity reaches the $O(n)$ level. The design of the rebalancing operation of the Splay tree avoids the accumulation of constants in the case of consecutive **zig** steps, so that in one complete splay operation at most one standalone **zig** operation is performed, which optimizes the time complexity.

## Balanced tree operations

This section discusses how to implement the common balanced tree operations based on a Splay tree. Among them, the more important ones are finding an element by value or by rank: they locate a specific element and move it up to the root for subsequent processing.

As an example, this section discusses the implementation of the template problem [Ordinary balanced tree](https://loj.ac/problem/104).

### Searching by value

As a binary search tree, the corresponding node can be found by its value $v$: simply compare the value $v$ being searched for with the value of the current node, and once found, move that element up to the root.

Note that it often happens that the corresponding node does not exist in the tree. In this case, record the last visited node (i.e. $y$ in the implementation) and move $y$ up to the root. Then the value stored at node $y$ must be either the largest among all elements smaller than $v$ (i.e. the predecessor of $v$) or the smallest among all elements larger than $v$ (i.e. the successor of $v$). This is because the search process guarantees that the left subtree always stores values smaller than $v$, and the right subtree always stores values larger than $v$.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:find"
    ```

This implementation allows specifying any node $z$ as the root and searches by value within its subtree.

### Accessing by rank

Because the subtree size information is recorded, a Splay tree can also access elements by rank, i.e. find the $k$-th smallest element in the tree.

Let $k$ be the remaining rank; the concrete steps are as follows:

-   if the left subtree is non-empty and the remaining rank $k$ is not greater than the size of the left subtree, search in the left subtree;
-   otherwise, if $k$ is not greater than the sum of the size of the left subtree and the multiplicity of the root's value, then the root is the one we are looking for;
-   otherwise, subtract from $k$ the sum of the size of the left subtree and the multiplicity of the root's value, and continue searching in the right subtree;
-   move the element finally found up to the root.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:loc"
    ```

This implementation requires that the rank $k$ does not exceed the size of the tree at the root $z$.

Operation $4$ of the template problem asks to return the value by rank; simply call this method and return the value.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:find-kth"
    ```

### Merging

Sometimes two Splay trees need to be merged.

Let the roots of the two trees be $x$ and $y$. To guarantee that the result is still a binary search tree, the maximum value in tree $x$ must be smaller than the minimum value in tree $y$. This condition can usually be satisfied, because the two trees are often split from a larger subtree.

The merge operation is as follows:

-   if one of $x$ and $y$, or both, is an empty tree, directly return the root of the non-empty tree or the empty tree;
-   otherwise, move the minimum value of tree $y$ up to the root $y$ via `loc(y, 1)`, then set its left child (which must be empty at this point) to $x$, update the node information, and return node $y$.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:merge"
    ```

Splitting is similar. Therefore, a Splay tree can imitate the approach of the [non-rotating Treap](./treap.md#non-rotating-treap) to perform various operations, including range operations. [Later](#sequence-operations) we will introduce a way of handling range operations that is more in the style of Splay trees.

### Insertion

Insertion is a relatively complex process. The concrete steps are as follows (suppose the inserted value is $v$):

-   similarly to searching by value, descend according to $v$ to the node storing $v$ or to an empty node, recording the parent $y$ along the way;
-   if a node $x$ storing $v$ exists, update its information directly; otherwise create a new node $x$;
-   perform a splay operation to move the last node $x$ up to the root.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:insert"
    ```

This implementation allows inserting a value directly into an empty tree. If you do not want to handle the empty tree, you can insert dummy nodes into the tree in advance.

### Deletion

Deletion is also a relatively complex operation. The concrete steps are as follows (suppose the deleted value is $v$):

-   first search by value $v$ for the node storing it, and move it up to the root;
-   if no node stores it, return directly (the previous step has already performed the splay operation);
-   otherwise, update the node information;
-   if the multiplicity of the root's value drops to zero, delete that node, i.e. merge the left and right subtrees as the new root; note that before merging, the parents of the roots of the two subtrees must be set to empty.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:remove"
    ```

### Querying the rank

Directly access the node by value $v$ (and move it up to the root), then return the corresponding rank.

Note that when $v$ does not exist, the order relation between the root returned by `find(rt, v)` and $v$ cannot be determined, and must be discussed separately.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:find-rank"
    ```

### Querying the predecessor

The predecessor is defined as the largest number smaller than $v$. The concrete steps are as follows:

-   access the node by value $v$ (and move it up to the root);
-   if the value at the root is smaller than $v$, it must be the largest such one, so return it directly;
-   otherwise, find the maximum value in the left subtree and move it up to the root.

The last step amounts to calling `loc(ch[rt][0], sz[ch[rt][0]])` directly, just without the unnecessary checks.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:find-prev"
    ```

This implementation allows the predecessor not to exist, in which case it returns $-1$.

### Querying the successor

The successor is defined as the smallest number larger than $v$. The query method is similar to that of the predecessor, except that the maximum of the left subtree is replaced by the minimum of the right subtree, i.e. call `loc(ch[rt][1], 1)`.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:find-next"
    ```

### Reference implementation

At the end of this section, we give a reference implementation of the template problem [Ordinary balanced tree](https://loj.ac/problem/104).

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:full-text"
    ```

## Sequence operations

Splay trees can also be applied to sequences, to maintain interval information. Compared with segment trees, Splay trees have a larger constant factor but support more complex sequence operations, such as interval reversal. It was mentioned above that Splay trees also support split and merge operations, so they can imitate the [non-rotating Treap](./treap.md#non-rotating-treap) to perform range operations; we will not discuss this further here. This section mainly discusses how to implement range operations based on the splay operation.

A Splay tree built from a sequence has the following properties:

-   the in-order traversal of the Splay tree corresponds to traversing the original sequence from left to right;
-   a node of the Splay tree represents an element of the original sequence;
-   a subtree of the Splay tree represents an interval of the original sequence.

Thanks to the splay operation, the Splay subtree representing a certain interval can be extracted quickly.

As an example, this section discusses the implementation of the template problem [Artistic balanced tree](https://loj.ac/problem/105).

### Building the tree from a sequence

Before the operations, the Splay tree must first be built from the given sequence. Due to the characteristics of Splay trees, it suffices to directly build a chain that has only left children. The time complexity is $O(n)$.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-2.cpp:build"
    ```

The final splay operation updates the node information from the bottom up. For the convenience of the range operations below, two sentinel nodes are added on the left and right sides of the sequence.

### Interval reversal

Taking interval reversal as an example, one can understand the method for range operations (let the interval be $[L,R]$):

-   first move node $L-1$ up to the root, then in its right subtree, move node $R+1$ up to the root of the right subtree;
-   now let $x$ be the left child of the right child of the root; then the subtree rooted at $x$ corresponds exactly to the interval $[L,R]$;
-   perform the operation on the interval $[L,R]$ at $x$ and apply a lazy tag;
-   push down the tag at $x$ once, then use the splay operation to move $x$ up to the root.

The operation needed in the first step is exactly the "accessing by rank" from the balanced tree operations above, since the index of an element is its rank. Because it involves the management of lazy tags, its implementation differs slightly from the one above.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-2.cpp:reverse"
    ```

The splay operation in the last step is not there to guarantee the correctness of the complexity, but to update the node information. Since the splay operation involves the left and right children of node $x$, the tag at node $x$ must be pushed down once beforehand. Of course, for the interval reversal operation alone, reversing a sub-interval has no effect on the ancestor nodes, so omitting this step is also correct. The implementation here keeps these two lines to illustrate the procedure in the general case.

### Lazy tag management

First, we need the auxiliary functions `lazy_reverse(x)` and `push_down(x)`. The former swaps the left and right children and updates the lazy tag; the latter pushes the tag down.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-2.cpp:push-down"
    ```

Then, it suffices to push down the tags when passing through nodes on the way down. The operations required by the template problem are relatively simple; only the search by rank (i.e. `loc`) involves accessing nodes downward. Note that the tag must be pushed down **before** the function accesses a new node each time.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-2.cpp:push-down-lazy"
    ```

Because all lazy tags on the traversed path have already been removed when accessing nodes downward, there is no longer any need to handle lazy tags when moving a node up by splaying. However, the node on which the range operation is performed must be handled with care: it also lies on the path of the splay operation, but it has just been operated on and may carry a tag not yet pushed down, so it must be pushed down first before splaying, exactly as done above.

### Reference implementation

At the end of this section, we give a reference implementation of the template problem [Artistic balanced tree](https://loj.ac/problem/105).

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-2.cpp:full-text"
    ```

## Exercises

These problems are plain maintenance of a binary search tree with a Splay tree:

-   ["Template" Ordinary balanced tree](https://loj.ac/problem/104)
-   ["Template" Artistic balanced tree](https://loj.ac/problem/105)
-   ["HNOI2002" Turnover statistics](https://loj.ac/problem/10143)
-   ["HNOI2004" Pet adoption center](https://loj.ac/problem/10144)

Splay trees also appear in more complex application scenarios:

-   ["Cerc2007" Robotic sort](https://www.luogu.com.cn/problem/P4402)
-   ["HNOI2011" Bracket repair / "JSOI2011" Bracket sequence](https://www.luogu.com.cn/problem/P3215)
-   [Double balanced tree (tree of trees)](https://loj.ac/problem/106)
-   [BZOJ 2827 Birds vanish over a thousand mountains](https://hydro.ac/p/bzoj-P2827)
-   ["Lydsy1706 monthly contest" K-th smallest value query](https://hydro.ac/p/bzoj-P4923)
-   [POJ3580 SuperMemo](http://poj.org/problem?id=3580)

## References and notes

Part of the content of this article is quoted from the algocode algorithm blog, with special thanks!

[^degen]: Splay trees only guarantee an amortized complexity of $O(\log n)$. They do not maintain balance conditions like AVL trees or red-black trees, and may even degenerate into a chain after a sequence of operations. Therefore, the worst-case complexity of a single operation is $O(n)$.
