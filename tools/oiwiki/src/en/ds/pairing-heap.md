---
title: Pairing heap
---

## Introduction

A pairing heap is a data structure supporting insertion, find-min/delete-min, merging, modifying elements and other operations; it is a mergeable heap. It has the advantages of speed and structural simplicity, but since its complexity is amortized and based on potential analysis, it cannot be made persistent.

## Definition

A pairing heap is a weighted multiway tree satisfying the heap property (see the figure below), i.e. the weight of every node is less than or equal to that of all its children (taking a min-heap as the example, likewise below).  
![](./images/pairingheap1.jpg)

We usually store a pairing heap in the child-sibling representation (see the figure below): all children of a node form a singly linked list. Each node stores a pointer to its first child, i.e. the head of that list, and a pointer to its right sibling.

This representation makes the pairing heap easy to implement and also convenient for complexity analysis.

![](./images/pairingheap2.jpg)

```cpp
struct Node {
  T v;  // T is the weight type
  Node *child, *sibling;
  // child points to the first child of this node, sibling to its next sibling.
  // If the node has no children / no next sibling, the pointer is nullptr.
};
```

From the definition we can see that, compared with other common heap structures, a pairing heap does not maintain any extra information such as tree size, depth or rank (a binary heap does not maintain extra information either, but it guarantees the complexity of its operations by maintaining a strict complete-binary-tree structure), and any tree satisfying the heap property is a valid pairing heap. This simple yet highly flexible data structure is the foundation of the pairing heap's excellent efficiency in practice; by contrast, the poor constant factor of the Fibonacci heap is due to the large amount of extra information it has to maintain.

The pairing heap guarantees its total complexity through a carefully designed order of operations; the original paper[^ref1] calls it a "Self Adjusting Heap". In this respect it is quite similar to the Splay tree (called a "Self Adjusting Binary Tree" in the original paper).

## Procedures

### Find-min

From the definition of the pairing heap, the root must have the minimum weight, so we simply return the root.

### Merge

Merging two pairing heaps is very simple: first let the smaller of the two roots be the new root, then insert the larger root as its child. (See the figure below.)

![](./images/pairingheap3.jpg)

Note that the child list of a node is ordered by insertion time: the rightmost node became a child of the parent earliest, and the leftmost node most recently.

???+ note "Implementation"
    ```cpp
    Node* meld(Node* x, Node* y) {
      // if one is empty, return the other
      if (x == nullptr) return y;
      if (y == nullptr) return x;
      if (x->v > y->v) std::swap(x, y);  // after the swap x is the heap with the smaller weight, y the larger
      // make y a child of x
      y->sibling = x->child;
      x->child = y;
      return x;  // the new root is x
    }
    ```

### Insert

With merge available, insertion simply treats the new element as a new pairing heap and merges it with the original heap.

### Delete-min

First of all, the operations above are all very lazy and do no maintenance of the data structure at all, so we have to design the delete-min operation carefully to make sure the total complexity does not suffer.

The root is the minimum, so the root is what we delete. Consider what happens after removing the root: all former children of the root form a forest, while a pairing heap should be a tree, so we need to merge all these children in some order.

A very natural idea is to use the `meld` function to merge the children one by one from left to right; this is obviously correct, but it makes the complexity of a single operation degrade to $O(n)$.

To guarantee the total amortized complexity, a "two-pass" merging method is needed:

1.  pair the children up two by two and use `meld` to merge the two children of each pair (see figure 1 below),
2.  merge the newly created heaps one by one **from right to left** (i.e. from the older children toward the newer ones) (see figure 2 below).

![](./images/pairingheap4.jpg)

![](./images/pairingheap5.jpg)

First implement a helper function `merges` that merges all siblings of a node.

???+ note "Implementation"
    ```cpp
    Node* merges(Node* x) {
      if (x == nullptr || x->sibling == nullptr)
        return x;  // if the tree is empty or it has no next sibling, nothing to merge, return.
      Node* y = x->sibling;                // y is the next sibling of x
      Node* c = y->sibling;                // c is the sibling after that
      x->sibling = y->sibling = nullptr;   // detach
      return meld(merges(c), meld(x, y));  // the core part
    }
    ```

The last statement is the core of this function and consists of three parts:

1.  `meld(x,y)` "pairs" x and y.
2.  `merges(c)` recursively merges c and its siblings.
3.  The two new trees produced by the above two operations are merged.

Note that, as mentioned above, the merging direction in the second step is prescribed (merge from right to left); this recursive implementation already guarantees that order. If readers want to implement an iterative version themselves, be sure to preserve this order, otherwise the complexity guarantee is lost.

With the `merges` function, the `delete-min` operation is obvious.

???+ note "Implementation"
    ```cpp
    Node* delete_min(Node* x) {
      Node* t = merges(x->child);
      delete x;  // if memory reclamation is needed
      return t;
    }
    ```

### Decrease-key

To implement this operation, nodes need an additional "father" pointer: when a node has a left sibling, it points to the left sibling instead of the actual parent; otherwise it points to its parent.

First the node definition is changed to:

???+ note "Implementation"
    ```cpp
    struct Node {
      LL v;
      int id;
      Node *child, *sibling;
      Node *father;  // new: father pointer; if this node is the root it points to nullptr
    };
    ```

The `meld` operation is changed to:

???+ note "Implementation"
    ```cpp
    Node* meld(Node* x, Node* y) {
      if (x == nullptr) return y;
      if (y == nullptr) return x;
      if (x->v > y->v) std::swap(x, y);
      if (x->child != nullptr) {  // new: maintain the father pointer
        x->child->father = y;
      }
      y->sibling = x->child;
      y->father = x;  // new: maintain the father pointer
      x->child = y;
      return x;
    }
    ```

The `merges` operation is changed to:

???+ note "Implementation"
    ```cpp
    Node *merges(Node *x) {
      if (x == nullptr) return nullptr;
      x->father = nullptr;  // new: maintain the father pointer
      if (x->sibling == nullptr) return x;
      Node *y = x->sibling, *c = y->sibling;
      y->father = nullptr;  // new: maintain the father pointer
      x->sibling = y->sibling = nullptr;
      return meld(merges(c), meld(x, y));
    }
    ```

Now let us consider how to implement the `decrease-key` operation.  
First we notice that after decreasing the weight of node `x`, the subtree rooted at `x` still satisfies the pairing heap property, but the heap property between the parent of `x` and `x` may no longer hold.  
So we cut out the whole subtree rooted at `x`; now both trees satisfy the pairing heap property, and merging them completes the whole operation.

???+ note "Implementation"
    ```cpp
    // root is the root of the heap, x the node to operate on, v the new weight; the caller must ensure v <= x->v
    // the return value is the new root
    Node *decrease_key(Node *root, Node *x, LL v) {
      x->v = v;                 // update the weight
      if (x == root) return x;  // if x is the root, return directly
      // cut x out of the children of fa; the position of x has to be distinguished here.
      if (x->father->child == x) {
        x->father->child = x->sibling;
      } else {
        x->father->sibling = x->sibling;
      }
      if (x->sibling != nullptr) {
        x->sibling->father = x->father;
      }
      x->sibling = nullptr;
      x->father = nullptr;
      return meld(root, x);  // merge x and the root again
    }
    ```

## Complexity analysis

The structure and implementation of the pairing heap are simple, but the time complexity analysis is not easy.

The original paper[^ref1] only analyzed the complexity to the extent that `meld` and `delete-min` are both amortized $O(\log n)$, but conjectured that all its operations have the same complexity as the Fibonacci heap.

Unfortunately, it was later found that for a pairing heap that maintains no extra information, under certain sequences of operations the amortized complexity of `decrease-key` has a lower bound of at least $\Omega (\log \log n)$[^ref2].

Currently, the better estimates of the upper bounds are: Iacono's $O(1)$ `meld` and $O(\log n)$ `decrease-key`[^ref3]; Pettie's $O(2^{2 \sqrt{\log \log n}})$ `meld` and `decrease-key`[^ref4]. Note that all these complexities are amortized, so one cannot take the minimum of the results for each operation separately.

## References

[^ref1]: [The pairing heap: a new form of self-adjusting heap](http://www.cs.cmu.edu/~sleator/papers/pairing-heaps.pdf)

[^ref2]: [On the efficiency of pairing heaps and related data structures](https://dl.acm.org/doi/10.1145/320211.320214)

[^ref3]: [Improved upper bounds for pairing heaps](https://arxiv.org/abs/1110.4428)

[^ref4]: [Towards a Final Analysis of Pairing Heaps](http://web.eecs.umich.edu/~pettie/papers/focs05.pdf)

-   <https://en.wikipedia.org/wiki/Pairing_heap>
-   <https://brilliant.org/wiki/pairing-heap/>
