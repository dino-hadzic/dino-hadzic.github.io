---
title: Finger tree
---

???+ warning "Note"
    This chapter is optional reading; before reading it, make sure you are somewhat familiar with functional programming.

## Introduction

The **finger tree** is a **purely functional** data structure proposed by Ralf Hinze and Ross Paterson.

## Why we need finger trees

In functional programming, the list is a very common data type. Almost all functional languages support sequence operations such as adding and removing elements at both ends (double-ended queue operations), insertion, concatenation and deletion at arbitrary positions, finding an element that satisfies a condition, and splitting a sequence into subsequences. However, these languages find it hard to perform many operations efficiently; even when corresponding implementations exist, they are usually very complex and hard to use in practice.

The finger tree provides a purely functional sequence data structure that supports access to and insertion at the front and the back of the sequence in amortized constant time, and concatenation and random access in logarithmic time. Besides good asymptotic running-time bounds, the finger tree is also very flexible: combined with [monoidal tags](https://en.wikipedia.org/wiki/Monoidal_category) on the elements, the finger tree can be used to implement efficient random-access sequences, ordered sequences, interval trees and priority queues.

## Basic structure

A finger tree stores its data at the "fingers" (leaves) of the tree, with amortized constant access time. A finger is a point from which part of the data structure can be accessed. In an imperative language it would be called a pointer. In a finger tree, a "finger" is a structure pointing to the ends of the sequence or to the leaves. The finger tree also stores, in every internal node, the result of applying some associative operation to its descendants. The data stored in the internal nodes can provide functionality beyond that of tree data structures.

1.  The depth of a finger tree is counted from the bottom up.
2.  The first level of the finger tree, i.e. the leaves of the tree, contains only values and has depth $0$. The second level has depth $1$, the third level has depth $2$, and so on.
3.  The closer a node is to the root, the deeper the subtree of the original tree (the tree before it became a finger tree) that it points to. Thus, walking down the tree is actually a walk from the leaves to the root, which is the opposite of usual tree data structures. To obtain this structure we must make sure the original tree has uniform depth. When declaring a node object, it must be parameterized by the type of its children. Spine nodes of depth $1$ and more point to trees, and thanks to this parameterization they can be represented by nested nodes.

### Converting a tree into a finger tree

???+ note "Note"
    A **2-3 tree** is a tree data structure in which every node with children (internal node) has either two children ($2$-node) and one data element, or three children ($3$-node) and two data elements. A 2-3 tree is a B-tree of order $3$. The external nodes of the tree (leaves) have no children and contain one or two data elements.

We start the process with a balanced 2-3 tree. For a finger tree to work properly, all leaves must be on the same level, as in the figure below (the figures are taken from the finger tree paper):

![](./images/finger-tree-1.png)

A finger is "a structure that provides efficient access to tree nodes near a given position". To make a finger tree, we put fingers at the left and right ends of the tree: we take the leftmost and rightmost internal nodes and lift them up, so that the rest of the tree hangs between them. This gives amortized constant-time access to the ends of the sequence.

![](./images/finger-tree-2.png)

This new data structure is called a finger tree. A finger tree consists of several layers (the blue boxes below) arranged along the spine of the tree (the brown line):

![](./images/finger-tree-3.png)

```haskell
data FingerTree a = Empty
                  | Single a
                  | Deep (Digit a) (FingerTree (Node a)) (Digit a)

data Digit a = One a | Two a a | Three a a a | Four a a a a
data Node a = Node2 a a | Node3 a a a
```

The digits in the example are the nodes labeled with letters. Each list is split by the prefix or suffix of each spine node. In the converted 2-3 tree it seems that the list of digits at the top level can have length two or three, while lower levels only have length one or two. For some applications of finger trees to run so efficiently, the finger tree allows from $1$ to $4$ subtrees at each level. The digits of a finger tree can be converted into a list, e.g.:

```haskell
type Digit a = One a | Two a a | Three a a a | Four a a a a
```

The top level has elements of type $a$, the next level has elements of type Node $a$, because these are the nodes between the spine and the leaves; in general, this means the $n$-th level of the tree has elements of type $Node^{n}$ $a$, i.e. 2-3 trees of depth $n$. This means that a sequence of $n$ elements is represented by a tree of depth `Θ(log n)`. An element at distance $d$ from the nearer end is stored in the tree at depth `Θ(log d)`.

### Double-ended queue operations

The finger tree also provides an efficient double-ended queue (deque). Whether or not the structure is persistent, all operations take `Θ(1)`. It can be seen as an extension of the implicit deque[^okasaki1999purely]:

1.  Replacing pairs with 2-3 nodes gives enough flexibility for efficient concatenation. (To keep deque operations in constant time, Digit needs to be extended to four.)
2.  Labeling the internal nodes with a monoid enables efficient splitting.

```haskell
data ImplicitDeque a = Empty
                     | Single a
                     | Deep (Digit a) (ImplicitDeque (a, a)) (Digit a)

data Digit a = One a | Two a a | Three a a a
```

## Time complexity

The finger tree provides amortized constant-time access to the "fingers" (leaves) of the tree, where the data is stored, and concatenation and splitting in time logarithmic in the size of the smaller part. It also stores, in each internal node, the result of applying some associative operation to its descendants. This "summary" data stored in the internal nodes can provide the functionality of data structures other than trees.

| Operation                       | Finger tree              | Annotated 2-3 tree | List         | Vector |
| ----------------------------- | ---------------------- | ----------------------------- | -------------------- | ---------- |
| `cons`,`snoc`                 | $O(1)$                 | $O(\log n)$                   | $O(1)$/$O(n)$        | $O(n)$     |
| `viewl`,`viewr`               | $O(1)$                 | $O(\log n)$                   | $O(1)$/$O(n)$        | $O(1)$     |
| `measure`/`length`            | $O(1)$                 | $O(1)$                        | $O(n)$               | $O(1)$     |
| `append`                      | $O(\log \min(l1, l2))$ | $O(\log n)$                   | $O(n)$               | $O(m+n)$   |
| `split`                       | $O(\log \min(n, l-n))$ | $O(\log n)$                   | $O(n)$               | $O(1)$     |
| `replicate`                   | $O(\log n)$            | $O(\log n)$                   | $O(n)$               | $O(n)$     |
| `fromList`,`toList`,`reverse` | $O(l)$/$O(l)$/$O(l)$   | $O(l)$                        | $O(1)$/$O(1)$/$O(n)$ | $O(n)$     |
| `index`                       | $O(\log \min(n, l-n))$ | $O(\log n)$                   | $O(n)$               | $O(1)$     |

## Applications

Finger trees can be used to build other trees. For example, a priority queue can be obtained by labeling the internal nodes with the minimum priority among their children, and an indexed list/array by labeling the nodes with the number of leaves among their children. Other applications include random-access sequences (described below), ordered sequences and interval trees.

The finger tree offers $O(1)$ on average for push, reverse and pop, $O(\log n)$ for append and split, and can be adapted to indexed or sorted sequences. Like all functional data structures, it is inherently persistent; this means that old versions of the tree are always kept.

As for implementations, the finite sequences `Seq` in the Haskell core library are implemented with a 2-3 finger tree ([Data.Sequence](https://hackage.haskell.org/package/containers-0.6.5.1/docs/Data-Sequence.html)), and the [implementation](https://ocaml-batteries-team.github.io/batteries-included/hdoc2/BatFingerTree.html) of the `BatFingerTree` module in OCaml also uses a generic finger tree structure. Finger trees can be implemented with or without lazy evaluation, but laziness allows a simpler implementation.

## References and further reading

1.  Ralf Hinze and Ross Paterson, "[Finger trees: a simple general-purpose data structure](http://www.staff.city.ac.uk/~ross/papers/FingerTree.html)", Journal of Functional Programming 16:2 (2006) pp 197-217.
2.  [Finger Tree - Wikipedia](https://en.wikipedia.org/wiki/Finger_tree)

[^okasaki1999purely]: [Purely Functional Data Structures](https://www.cambridge.org/us/academic/subjects/computer-science/programming-languages-and-applied-logic/purely-functional-data-structures), Chris Okasaki (1999)
