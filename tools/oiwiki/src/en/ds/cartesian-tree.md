---
title: Cartesian tree
---

## Introduction

A Cartesian tree is a binary tree in which every node consists of a pair of keys $(k,w)$. The key $k$ must satisfy the binary search tree (BST) property, and $w$ must satisfy the heap property. If the keys $k,w$ of a Cartesian tree are fixed, all $k$ are pairwise distinct and all $w$ are pairwise distinct, then the structure of the Cartesian tree is unique. See the figure below:

![eg](./images/cartesian-tree1.png)

(Figure taken from Wikipedia.)

The Cartesian tree above corresponds to taking the array values as the key $w$ and the array indices as the key $k$. One can see that the keys $k$ of this tree satisfy the BST property, while the keys $w$ satisfy the min-heap property. Moreover, by the property of binary search trees, in this special kind of Cartesian tree the indices inside any subtree form a contiguous interval.

When Cartesian trees are used in contests, the array index is usually taken as the key $k$ of the pair; the indices $k$ satisfy the BST property.

Below, whenever we use $k,w$, we assume by default that $k$ satisfies the BST property and $w$ satisfies the heap property.

## Building a Cartesian tree with a monotonic stack

### Procedure

Consider inserting the elements into the current Cartesian tree one by one in increasing order of $k$.

For a Cartesian tree, define the "right chain" as the chain obtained by starting at the root and repeatedly going to the right child until reaching a node without a right child. After a node is inserted, it must lie on the right chain. Because we insert in increasing order of $k$, which satisfies the BST property, the newly inserted node is necessarily at the **rightmost** end of the tree. This node cannot be a left child, and it has no right child.

So we perform the following process: compare, from bottom to top, the $w$ of the nodes on the right chain with the $w$ of the current node $u$; once we find a node $x$ on the right chain with $w_x<w_u$, we attach $u$ as the right child of $x$, and the former right subtree of $x$ becomes the left subtree of $u$.

The red frame in the figure marks the right chain that we maintain throughout:

![build](./images/cartesian-tree2.png)

Clearly every number enters and leaves the right chain at most once (in other words, every node stays on the right chain for one contiguous period of time). This process can be maintained with a monotonic stack: the stack holds the nodes currently on the right chain of the Cartesian tree. Once a node is no longer on the right chain, it is popped. Thus every node is pushed and popped at most once, and the complexity is $O(n)$.

???+ note "Cartesian trees and Treaps"
    In fact, a Treap is a kind of Cartesian tree, except that in a Treap the values $w$ are completely random. Treaps have a linear-time construction algorithm: if the keys $k$ are sorted in advance, the construction can be done with the monotonic stack algorithm above, although this is rarely done in practice.

### C++ implementation

```cpp
// stk holds the array indices corresponding to the nodes of the Cartesian tree
for (int i = 1; i <= n; i++) {
  int k = top;  // top is the stack top before the operation, k is the current stack top
  while (k > 0 && w[stk[k]] > w[i]) k--;  // maintain the nodes on the right chain
  if (k) rs[stk[k]] = i;  // stack top.right child := current element
  if (k < top) ls[i] = stk[k + 1];  // current element.left child := last popped element
  stk[++k] = i;                     // push the current element
  top = k;
}
```

## Example problem

???+ note "[HDU 1506. Largest Rectangle in a Histogram](https://acm.hdu.edu.cn/showproblem.php?pid=1506)"
    There are $n$ positions, and the height at each position is $h_i$; find the largest sub-rectangle. See the figure:
    
    ![eg](./images/cartesian-tree3.png)
    
    The shaded part is the largest sub-rectangle in the figure.

??? note "Solution idea"
    Specifically, we take the index as the key $k$ and $h_i$ as the key $w$ satisfying the min-heap property, and build the Cartesian tree of the pairs $(i,h_i)$.
    
    Then we enumerate every node $u$ and take $w_u$ (that is, the height $h$ of node $u$) as the height of the largest sub-rectangle. Since the Cartesian tree we built satisfies the min-heap property, the heights of all nodes in the subtree of $u$ are greater than or equal to that of $u$. We also know that the indices in the subtree of $u$ form a contiguous interval. So we only need to know the size of the subtree, and then we can compute the area of the largest sub-rectangle on that interval. We update the answer with the value computed at every node. Clearly this can be done with a single DFS, so the complexity is $O(n)$.

??? note "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/cartesian-tree/cartesian-tree_1.cpp"
    ```

## References

[Cartesian tree – Wikipedia](https://en.wikipedia.org/wiki/Cartesian_tree)
