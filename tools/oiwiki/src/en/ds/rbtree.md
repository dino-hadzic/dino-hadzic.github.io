---
title: Red-black tree
---

author: 0x03A6, abc1763613206, auuuu4, CCXXXI, Conless, Enter-tainer, fanenr, happyZYM, hsfzLZH1, iamtwz, LeverImmy, leverimmy, Lhcfl, Marcythm, RIvance, Tiphereth-A, trudbot, Xeniume, Xeonacid, YBYCS, yuhuoji

A red-black tree is a self-balancing binary search tree. Each node stores an additional color field ("RED" or "BLACK") to keep the tree balanced during insertion and deletion.

A red-black tree is a variant of a B-tree of order 4 (a [2-3-4 tree](https://en.wikipedia.org/wiki/2%E2%80%933%E2%80%934_tree)).[^gilbas1978]

## Properties

A valid red-black tree must satisfy the following four properties:

1.  A node is red or black.
2.  NIL nodes (empty leaf nodes) are black.
3.  The children of a red node are black.
4.  Every path from the root to a NIL node contains the same number of black nodes.

The figure below shows a valid red-black tree:

![rbtree-example](images/rbtree-example.svg)

???+ note "Note"
    Some sources add a fifth property: the root must be black. This requires coloring the root black after insertion if it is red. However, coloring the root black can be delayed until deletion, so this property is not essential (the implementation in this article does satisfy it). For precision, we also quote the [original Wikipedia text](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree#Properties):
    
    > Some authors, e.g. Cormen & al.,[^cite_note-cormen2009-18]claim "the root is black" as fifth requirement; but not Mehlhorn & Sanders[^cite_note-mehlhorn2008-17]or Sedgewick & Wayne.[^cite_note-algs4-16]Since the root can always be changed from red to black, this rule has little effect on analysis. This article also omits it, because it slightly disturbs the recursive algorithms and proofs.

## Red-black tree class definition

```cpp
--8<-- "docs/ds/code/rbtree/rbtree.hpp:class-node1"
  // ...
--8<-- "docs/ds/code/rbtree/rbtree.hpp:class-node2"
```

???+ note "Note"
    Storing child pointers in an array within red-black tree nodes improves code reuse.

## Operations

???+ note "Note"
    There are several ways to implement insertion/deletion in a red-black tree. This article follows *Introduction to Algorithms*, dividing balance maintenance after insertion into 3 cases and after deletion into 4 cases.

Traversal, finding the minimum/maximum, searching for an element, finding an element's rank, selecting an element by rank, and finding predecessors/successors are the same as in a [binary search tree](./bst.md), so they are not repeated here.

In the code comments for balance maintenance after insertion/deletion, we use the following notation:

-   `p` means node `p` is black;
-   `[p]` means node `p` is red;
-   `{p}` means node `p` is red or black;
-   `|p|` means node `p` is a NIL node or is black.

### Rotations

Rotations are the key to maintaining balance in most balanced trees. They change the depth of local nodes without changing the inorder traversal of a valid BST.

![rbtree-rotations](images/rbtree-rotate.svg)

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:rotate"
    ```

### Insertion

Insertion into a red-black tree is similar to insertion into an ordinary BST. In a red-black tree, the new node is initially red. After insertion, corrections based on the inserted node and related nodes are needed to satisfy the four properties above.

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert"
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-leaf"
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-fixup1"
        // ...
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-fixup2"
    ```

### Maintaining balance after insertion

???+ note "Note"
    To deepen your understanding, verify for yourself that property 4 holds after balance maintenance.

Since an inserted node must be red unless it is the root, insertion may violate property 3, requiring balance maintenance.

Let the inserted node be $n$, its parent $p$, its grandparent $g$, and its uncle $u$. Property 3 implies that $g$ must be black.

We maintain balance recursively upward from the insertion position. If $p$ is black, we can stop; otherwise, there are 3 cases.

```cpp
--8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-aux1"
      // ...
--8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-aux2"
```

#### Insert case 1

Both $p$ and $u$ are red. Recoloring alone is sufficient.

![](images/rbtree-insert-case1.svg)

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-case1"
    ```

#### Insert case 2

$p$ is red, $u$ is black, and the directions of $p$ and $n$ differ.

We rotate at $p$ to convert this into the third case.

![](images/rbtree-insert-case2.svg)

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-case2"
    ```

#### Insert case 3

$p$ is red, $u$ is black, and the directions of $p$ and $n$ are the same.

We rotate at $g$ to make $p$ the subtree root, then swap the colors of $p$ and $g$.

![](images/rbtree-insert-case3.svg)

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-case3"
    ```

### Deletion

Deletion in a red-black tree involves a few more steps than in an ordinary BST. Specifically:

-   If the node $n$ to be deleted has two children, swap the data of $n$ and the smallest node $s$ in the right subtree, then set $n$ to $s$. Now $n$ cannot have two children.
-   If the node $n$ to be deleted has one child $s$, property 4 implies that $s$ is red, and property 3 then implies that $n$ is black. We only need to replace the pointer to $n$ in its parent $p$ with the address of $s$, replace the parent pointer of $s$ with the address of $p$, and then color $s$ black.
-   If the node $n$ to be deleted has no children and $n$ is the root or $n$ is red, we can delete it directly. Otherwise, direct deletion would violate property 4, requiring balance maintenance.

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete"
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-leaf"
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-fixup1"
        // ...
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-fixup2"
    ```

### Maintaining balance after deletion

???+ note "Note"
    To deepen your understanding, verify for yourself that property 4 holds after balance maintenance.

From the discussion above, $n$ is a black leaf that is not the root. Let $n$ have parent $p$, sibling $s$, and nephews $c$ and $d$.

Balance maintenance after deletion also proceeds recursively upward from $n$. If $n$ is the root or $n$ is red, we can stop; otherwise, there are 4 cases.

```cpp
--8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-aux1"
      // Delete case 1
      // ...
      // Other cases
--8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-aux2"
      // ...
--8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-aux3"
```

#### Delete case 1

$s$ is red.

We rotate at $p$ to make $s$ the subtree root, then swap the colors of $s$ and $p$ to convert this into one of the other three cases.

![](images/rbtree-remove-case1.svg)

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-case1"
    ```

#### Delete case 2

The color of $p$ is unspecified, and $s$, $c$, and $d$ are black.

We only need to color $s$ red.

![](images/rbtree-remove-case2.svg)

Note that if $p$ is red, this violates property 3. However, a red $p$ causes the loop to exit immediately, so we color it black at the end.

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-case2"
    ```

#### Delete case 3

The color of $p$ is unspecified, $s$ and $d$ are black, and $c$ is red.

We rotate at $s$ to make $c$ the root of the subtree previously rooted at $s$, then swap the colors of $s$ and $c$ to convert this into the fourth case.

![](images/rbtree-remove-case3.svg)

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-case3"
    ```

#### Delete case 4

The colors of $p$ and $c$ are unspecified, $s$ is black, and $d$ is red.

We rotate at $p$ to make $s$ the subtree root, swap the colors of $s$ and $p$, and color $d$ black. Balance maintenance can then stop.

![](images/rbtree-remove-case4.svg)

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-case4"
    ```

## Reference code

The following code implements a set using a red-black tree:

??? note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:full"
    ```

??? note "Example problems: [Luogu P3369 [Template] Ordinary Balanced Tree](https://www.luogu.com.cn/problem/P3369) and [Luogu P6136 [Template] Ordinary Balanced Tree (Stronger Test Data)](https://www.luogu.com.cn/problem/P6136)"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:class"
    --8<-- "docs/ds/code/rbtree/rbtree_1.cpp:main"
    ```

## Relationship with 2-3-4 trees

A 2-3-4 tree is a B-tree of order 4. Like a general B-tree, it supports search, insertion, and deletion in $O(\log n)$ time. There are three types of nodes: 2-nodes, 3-nodes, and 4-nodes, containing one, two, or three data elements, respectively. All leaves are at the same depth (the bottom level), and all data is stored in order.

2-3-4 trees and red-black trees are isomorphic: every red-black tree corresponds to a unique 2-3-4 tree. Node expansion, splitting, and merging caused by insertion and deletion in a 2-3-4 tree correspond to recoloring and rotations in a red-black tree. The figure below shows the red-black tree nodes corresponding to 2-nodes, 3-nodes, and 4-nodes. Notice that a 3-node in a 2-3-4 tree corresponds to two red-black tree cases, with a left-leaning or right-leaning red node, so a red-black tree may correspond to multiple 2-3-4 trees.

![2-3-4-tree-rbt-1](images/2-3-4-tree-rbt-1.svg)

The figure below shows a red-black tree and its corresponding 2-3-4 tree. Moving the red nodes up to the left and right sides of their parents forms B-tree nodes and gives the corresponding 2-3-4 tree. We can observe that the number of nodes in the red-black tree equals the number of nodes in the 2-3-4 tree.

![2-3-4-tree-rbt](images/2-3-4-tree-rbt-2.svg)

Insertion and deletion in a red-black tree can be understood by comparison with a 2-3-4 tree.[^234-vs-rbt]

## Use in real-world projects

Red-black trees have the best overall efficiency among mainstream in-memory balanced trees in industry today, so they are widely used in real-world projects. Here are some practical examples with source links for comparison and study.

### Linux

Source code:

-   [`linux/lib/rbtree.c`](https://elixir.bootlin.com/linux/latest/source/lib/rbtree.c)

All red-black tree operations in Linux are implemented iteratively using loops. Extensive comments preserve readability while maintaining efficiency, and studying this code is highly recommended. Red-black trees are widely used in the Linux kernel; only a few classic examples are listed here.

-   [CFS scheduling of non-real-time tasks](https://www.kernel.org/doc/html/latest/scheduler/sched-design-CFS.html)

    Starting with stable kernel versions after 2.6.24, Linux uses the new CFS scheduler. All runnable non-real-time processes are maintained in a red-black tree keyed by virtual runtime, enabling fairer and more efficient task scheduling. CFS abandons the active/expired arrays and dynamically computed priorities, no longer tracks task sleep time or distinguishes interactive tasks, and instead selects the next task using a red-black tree with time-based keys. Scheduling priorities are determined from the CPU time used by all tasks.

-   [epoll](https://man7.org/linux/man-pages/man7/epoll.7.html)

    epoll, short for event poll, is an implementation of IO multiplexing in the Linux kernel and an improvement over the original poll/select mechanisms. Linux's epoll implementation stores file descriptors in a red-black tree.

### Nginx

Source code:

-   [`nginx/src/core/ngx_rbtree.h`](https://github.com/nginx/nginx/blob/master/src/core/ngx_rbtree.h)
-   [`nginx/src/core/ngx_rbtree.c`](https://github.com/nginx/nginx/blob/master/src/core/ngx_rbtree.c)

User-space timers in nginx are implemented with a red-black tree. All timer nodes in nginx are maintained in one red-black tree. Each iteration of a worker process calls `ngx_process_events_and_timers`, which calls `ngx_event_expire_timers` to process timers. This function repeatedly takes the node with the smallest time value from the tree, checks whether it has expired, and executes its function, until it reaches a node whose time has not yet expired.

Many public resources analyze nginx's red-black tree source code; readers can look them up for further study.

### C++

Source code:

-   GNU libstdc++

    -   [`libstdc++-v3/include/bits/stl_tree.h`](https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/include/bits/stl_tree.h)
    -   [`libstdc++-v3/src/c++98/tree.cc`](https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/src/c%2B%2B98/tree.cc)

    In addition, `libstdc++` provides [`__gnu_cxx::rb_tree`](https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/include/ext/rb_tree) in `<ext/rb_tree>`. It inherits from `std::_Rb_tree` and can be viewed as a type alias intended for external use. Note that this header is **not** part of the C++ standard, so using it is not recommended unless necessary.

    The [`pb_ds`](../lang/pb-ds/tree.md) library in `libstdc++` also provides a red-black tree.

-   LLVM libcxx
    -   [`libcxx/include/__tree`](https://github.com/llvm/llvm-project/blob/main/libcxx/include/__tree)

-   Microsoft STL
    -   [`stl/inc/xtree`](https://github.com/microsoft/STL/blob/main/stl/inc/xtree)

In most STL implementations, `std::set` and `std::map` use a red-black tree internally (including those listed above). However, the C++ standard does not require `std::set` and `std::map` to use red-black trees, so their internal data structures should not be used directly in projects.

### OpenJDK

Source code:

-   [`java.util.TreeMap<K, V>`](https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/util/TreeMap.java)
-   [`java.util.TreeSet<K, V>`](https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/util/TreeSet.java)
-   [`java.util.HashMap<K, V>`](https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/util/HashMap.java)

Both `TreeMap` and `TreeSet` in the JDK use a red-black tree as their underlying data structure. Since JDK 1.8, when a linked list for an entry in `HashMap`'s internal hash table exceeds length 8, it also automatically becomes a red-black tree to improve lookup efficiency.

## References

-   Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022).*Introduction to algorithms*. MIT press.
-   [Red-Black Tree - Wikipedia](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)
-   [Red-Black Tree Visualization](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html)

[^gilbas1978]: L. J. Guibas and R. Sedgewick, "A dichromatic framework for balanced trees,"*19th Annual Symposium on Foundations of Computer Science (sfcs 1978)*, Ann Arbor, MI, USA, 1978, pp. 8-21, doi:[10.1109/SFCS.1978.3](https://doi.org/10.1109%2FSFCS.1978.3).

[^cite_note-cormen2009-18]: <https://en.wikipedia.org/wiki/Red–black_tree#cite_note-Cormen2009-18>

[^cite_note-mehlhorn2008-17]: <https://en.wikipedia.org/wiki/Red–black_tree#cite_note-Mehlhorn2008-17>

[^cite_note-algs4-16]: <https://en.wikipedia.org/wiki/Red–black_tree#cite_note-Algs4-16>: 432–447

[^234-vs-rbt]: [This blog post](https://www.cnblogs.com/zhenbianshu/p/8185345.html) provides a detailed description.
