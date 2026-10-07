---
title: Leftist tree
---

## What is a leftist tree?

A **leftist tree**, like the [**pairing heap**](./pairing-heap.md), is a **mergeable heap**: it has the heap property and can be merged quickly.

## Definition and properties of the leftist tree

For a binary tree, we define an **external node** as a node with fewer than two children, and the $\mathrm{dist}$ of a node as the number of edges on the path to the nearest external node in its subtree. The $\mathrm{dist}$ of an empty node is $0$.

???+ note "Note"
    Some sources define $\mathrm{dist}$ as the $\mathrm{dist}$ of this article minus $1$; this definition lets you omit some emptiness checks when writing code, but the $\mathrm{dist}$ of the empty node must then be preset to $-1$. All code in this article uses **the definition in which the $\mathrm{dist}$ of the empty node is $-1$**; mind the difference from the definition of $\mathrm{dist}$ used in the text.

A leftist tree is a binary tree that not only has the heap property but is also "leftist": for every node the $\mathrm{dist}$ of its left child is greater than or equal to the $\mathrm{dist}$ of its right child.

Therefore the $\mathrm{dist}$ of every node of a leftist tree equals the $\mathrm{dist}$ of its right child plus one.

Note that $\mathrm{dist}$ is not depth: **the depth of a leftist tree is not bounded**, and a chain going to the left also fits the definition of a leftist tree.

## Core operation: merge

When merging two heaps, to satisfy the heap property we first take the root with the smaller value (for convenience this article discusses min-heaps) as the root of the merged heap, then the left child of this root becomes the left child of the merged heap, and we recursively merge its right child with the other heap to obtain the right child of the merged heap. To satisfy the leftist property, if after merging the $\mathrm{dist}$ of the left child is less than the $\mathrm{dist}$ of the right child, swap the two children.

Reference code:

???+ note "Implementation"
    ```cpp
    int merge(int x, int y) {
      if (!x || !y) return x | y;  // if one heap is empty, return the other
      if (t[x].val > t[y].val) swap(x, y);  // the smaller value becomes the root
      t[x].rs = merge(t[x].rs, y);          // recursively merge the right child with the other heap
      if (t[t[x].rs].d > t[t[x].ls].d)
        swap(t[x].ls, t[x].rs);   // if the leftist property is violated, swap the children
      t[x].d = t[t[x].rs].d + 1;  // update dist
      return x;
    }
    ```

Because of the leftist property, each level of recursion decreases the $\mathrm{dist}$ of the root of one of the heaps by $1$, and in a binary tree with $n$ nodes the $\mathrm{dist}$ of the root is at most $\left\lceil\log (n+1)\right\rceil$, so merging two heaps of sizes $n$ and $m$ costs $O(\log n+\log m)$.

???+ note "Proof of the $\mathrm{dist}$ property"
    A binary tree whose root has $\mathrm{dist}$ $x$ has at least $x-1$ levels forming a full binary tree, and therefore at least $2^x-1$ nodes. Note that this property holds for all binary trees, not only leftist trees.

A leftist tree can also be written without swapping the left and right children: treat the child with the larger $\mathrm{dist}$ as the left child and the one with the smaller $\mathrm{dist}$ as the right child:

???+ note "Implementation"
    ```cpp
    int& rs(int x) { return t[x].ch[t[t[x].ch[1]].d < t[t[x].ch[0]].d]; }
    
    int merge(int x, int y) {
      if (!x || !y) return x | y;
      if (t[x].val < t[y].val) swap(x, y);
      int& rs_ref = rs(x);
      rs_ref = merge(rs_ref, y);
      t[x].d = t[rs(x)].d + 1;
      return x;
    }
    ```

## Other operations on leftist trees

### Inserting a node

A single node can also be regarded as a heap, so just merge.

### Deleting the root

Just merge the left and right children of the root.

### Deleting an arbitrary node

#### Method

First merge the left and right children, then going bottom-up update $\mathrm{dist}$ and swap the children whenever the leftist property is violated; the recursion stops when $\mathrm{dist}$ no longer needs updating:

???+ note "Implementation"
    ```cpp
    int& rs(int x) { return t[x].ch[t[t[x].ch[1]].d < t[t[x].ch[0]].d]; }
    
    // with pushup, deleting a node while keeping the leftist property is just merging its left and right children
    int merge(int x, int y) {
      if (!x || !y) return x | y;
      if (t[x].val < t[y].val) swap(x, y);
      int& rs_ref = rs(x);
      rs_ref = merge(rs_ref, y);
      t[rs_ref].fa = x;
      t[x].d = t[rs(x)].d + 1;
      return x;
    }
    
    void pushup(int x) {
      if (!x) return;
      if (t[x].d != t[rs(x)].d + 1) {
        t[x].d = t[rs(x)].d + 1;
        pushup(t[x].fa);
      }
    }
    
    void erase(int x) {
      int y = merge(t[x].ch[0], t[x].ch[1]);
      t[y].fa = t[x].fa;
      if (t[t[x].fa].ch[0] == x)
        t[t[x].fa].ch[0] = y;
      else if (t[t[x].fa].ch[1] == x)
        t[t[x].fa].ch[1] = y;
      pushup(t[y].fa);
    }
    ```

#### Complexity proof

First consider the `merge` process: every step moves $x$ or $y$ down one level, so the most extreme case is always choosing the right node of the leftist tree (the node with the smallest $\mathrm{dist}$) and going down one level, which decreases $\mathrm{dist}$ by $1$.

Now consider the `pushup` process. Let $x$ be the node currently being pushed up, $y$ its parent, and the "initial $\mathrm{dist}$" of a node its $\mathrm{dist}$ before the `pushup`. The recursion starts from the parent of the deleted node, and there are two cases:

1.  $x$ is the right child of $y$; then the initial $\mathrm{dist}$ of $y$ is the initial $\mathrm{dist}$ of $x$ plus one.
2.  $x$ is the left child of $y$; since the $\mathrm{dist}$ of a node decreases by at most one, the recursion continues only when the initial $\mathrm{dist}$ values of the left and right children of $y$ are equal (then decreasing the left child's $\mathrm{dist}$ by one causes the children to be swapped), so the initial $\mathrm{dist}$ of $y$ is still the initial $\mathrm{dist}$ of $x$ plus one.

Hence each level of recursion increases the initial $\mathrm{dist}$ of $x$ by one, so there are at most $O(\log n)$ levels of recursion.

### Adding/subtracting a value to the whole heap, multiplying by a positive number

In fact any operation that can be lazily tagged and does not change the relative order works.

Put the tag on the root, and push the tag down when deleting the root or merging heaps (i.e. when accessing the children):

???+ note "Implementation"
    ```cpp
    int merge(int x, int y) {
      if (!x || !y) return x | y;
      if (t[x].val > t[y].val) swap(x, y);
      pushdown(x);
      t[x].rs = merge(t[x].rs, y);
      if (t[t[x].rs].d > t[t[x].ls].d) swap(t[x].ls, t[x].rs);
      t[x].d = t[t[x].rs].d + 1;
      return x;
    }
    
    int pop(int x) {
      pushdown(x);
      return merge(t[x].ls, t[x].rs);
    }
    ```

## Other mergeable heaps

### Randomized heap

???+ note "Implementation"
    ```cpp
    int merge(int x, int y) {
      if (!x || !y) return x | y;
      if (t[y].val < t[x].val) swap(x, y);
      if (rand() & 1)  // randomly decide whether to swap the left and right children
        swap(t[x].ls, t[x].rs);
      t[x].ls = merge(t[x].ls, y);
      return x;
    }
    ```

As you can see, the only difference in this implementation is that merging uses random numbers, which saves all the $\mathrm{dist}$ computations. Its average time complexity is also $O(\log n)$; for a detailed proof see [Randomized Heap](https://cp-algorithms.com/data_structures/randomized_heap.html).

### Skew heap

The skew heap is a self-adjusting form of the leftist tree. When merging two heaps, it unconditionally swaps the children of all nodes on the merge path in an attempt to maintain balance. By amortized analysis, insertion, merging and delete-min in a top-down skew heap take $O(\log n)$[^ref1].

## Example problems

### Template problems

[Luogu P3377 "Template" Leftist Tree (Mergeable Heap)](https://www.luogu.com.cn/problem/P3377)

[Monkey King](https://www.luogu.com.cn/problem/P1456)

[Roman Game](https://www.luogu.com.cn/problem/P2713)

Things to note:

1.  Before merging, check whether the elements are already in the same heap.

2.  The depth of a leftist tree can reach $O(n)$, so finding the top of the heap containing a node must be done with a disjoint set union, not by jumping up through parents by brute force. (Although many problems have weak test data and jumping through parents passes...) (When maintaining the roots with a DSU, make sure the old root points to the new root and the new root points to itself.)

??? note "Reference code for Roman Game"
    ```cpp
    --8<-- "docs/ds/code/leftist-tree/leftist-tree_1.cpp"
    ```

### Problems on trees

["APIO2012" Dispatching](https://www.luogu.com.cn/problem/P1552)

["JLOI2015" Castle Conquest](https://loj.ac/problem/2107)

In these problems each node typically maintains a heap, merges it with those of its children, and pops, modifies and computes the answer as the problem requires; they resemble problems on segment tree merging.

??? note "Reference code for Castle Conquest"
    ```cpp
    --8<-- "docs/ds/code/leftist-tree/leftist-tree_2.cpp"
    ```

### ["SCOI2011" Tricky Operations](https://loj.ac/problem/2441)

First, finding the top of the heap containing a node must use a DSU rather than jumping upward by brute force.

Next consider single-point queries. If tags are applied in the usual way, we would have to query the sum of tags on the path from the node to the root, which can cost $O(n)$ in the worst case. If only the heap top carried a tag, queries would be fast, but how can that be achieved?

We can use something like heuristic merging (merge the smaller into the larger): on every merge, push the tag of the smaller heap down to each of its nodes by brute force, and let the tag of the larger heap become the tag of the merged heap. Since the merged heap carries the other heap's tag, when pushing down the smaller heap must push down its tag minus the other heap's tag. Every time a node is merged, the size of its heap at least doubles, so each node has tags pushed down onto it at most $O(\log n)$ times, and the total cost of brute-force pushing is $O(n\log n)$.

Now single-point addition: just delete, update, and insert again.

Then the global maximum: use a balanced tree / a heap supporting deletion of arbitrary nodes (such as a leftist tree) / a multiset to maintain the tops of all heaps.

So the operations are, respectively:

1.  Push down the tag of the heap with fewer nodes by brute force, merge the two heaps, update size and tag, and remove from the multiset the old top that is no longer a top after merging.
2.  Delete the node, update its value, insert it back, update the multiset. Whether the deleted node is a root has to be handled separately.
3.  Tag the heap top, update the multiset.
4.  Apply a global tag.
5.  Query value + heap-top tag + global tag.
6.  Query the root's value + heap-top tag + global tag.
7.  Query the maximum of the multiset + global tag.

??? note "Reference code for Tricky Operations"
    ```cpp
    --8<-- "docs/ds/code/leftist-tree/leftist-tree_3.cpp"
    ```

### ["BOI2004" Sequence](https://www.luogu.com.cn/problem/P4331)

This is a problem from a paper; see ["Huang Yuanhe -- Characteristics of Leftist Trees and Their Applications"](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2005%E8%AE%BA%E6%96%87%E9%9B%86/%E9%BB%84%E6%BA%90%E6%B2%B3--%E5%B7%A6%E5%81%8F%E6%A0%91%E7%9A%84%E7%89%B9%E7%82%B9%E5%8F%8A%E5%85%B6%E5%BA%94%E7%94%A8/%E9%BB%84%E6%BA%90%E6%B2%B3.pdf).

## References

[^ref1]: [Self-Adjusting Heaps](https://epubs.siam.org/doi/10.1137/0215004)
