---
title: Garsia–Wachs algorithm
---

## Introduction

The **Garsia–Wachs algorithm** is an efficient algorithm used by computers to build an **optimal binary search tree** and an **alphabetic Huffman code** in **linear time**. It is named after Adriano Garsia and Michelle L. Wachs, who published the corresponding paper in 1977.

## Problem description

Given an integer $n$ and $n+1$ non-negative weights $w_{0},w_{1},\dots ,w_{n}$, construct a rooted binary tree in which each of the $n$ internal nodes has two children, which means that the binary tree has $n+1$ leaves. We map the input sequence of length $n+1$ one-to-one onto the nodes of the binary tree in order, and the goal is to find, among all possible tree structures with $n$ internal nodes, a tree that minimizes the weighted sum of the external path lengths from the root to every leaf.

### Optimal binary search tree

This problem can be understood as the problem of constructing a binary search tree over $n$ ordered keys, assuming that the tree will only be used to search for values that are not present in the tree. In this case the $n$ keys partition the space of search values into $n+1$ intervals, and the weight of one of these intervals can be taken as the probability that the search value falls into that interval. The weighted sum of the external path lengths controls the expected search time.

### Alphabetic Huffman code

This problem can also be used to construct a Huffman code. This is a method of unambiguously encoding $n+1$ given values using variable-length sequences of binary values. In this interpretation, the code of a value is given by the sequence of left and right steps from parent to child on the path from the root of the tree to the leaf (for example, $0$ for left and $1$ for right). Unlike the standard Huffman code, a Huffman code constructed in this way is alphabetic, i.e. the sorted order of these binary codes is the same as the input order of the values. If the weight of a value is its frequency in the encoded message, then the output of the Garsia–Wachs algorithm is the alphabetic Huffman code that compresses the message to the shortest length.

## Procedure

The Garsia–Wachs algorithm generally consists of three phases:

1.  Build a binary tree whose values are in the leaves, noting that the order may be wrong.
2.  Compute the distance from the root to each leaf in the tree.
3.  Build another binary tree with the same leaf distances but the correct order.

![](./images/garsia-wachs.png)

As shown in the figure above, in the first phase of the algorithm a binary tree (left) is built by finding and merging unordered triples of the input sequence, and the output of the algorithm is a correctly ordered binary tree whose leaf heights are the same as in the other tree.

The first phase of the algorithm is easier to describe if two sentinel values $\infty$ (or any sufficiently large finite value) are added at the beginning and the end of the input sequence. Therefore, when using the Garsia–Wachs algorithm in contest solutions, for an array $\mathit{num}$ of length $n$ we usually define $\mathit{num}[0] = \mathit{num}[n+1] = \infty$.

The first phase maintains a forest consisting initially of single-node trees created for each non-sentinel input weight. Each tree is associated with a value, the sum of the weights of its leaves; one tree node is created for each non-sentinel input weight. To maintain the sequence of these values, there are two sentinel values at each end. The initial sequence is just the leaf weights in input order. Then the following steps are repeated, each of which reduces the length of the input sequence, until only one tree containing all leaves remains:

-   Find the first three consecutive weights $x$, $y$, $z$ in the sequence such that $x \leq z$. Because the sentinel value at the end of the sequence is greater than any two finite values before it, such a triple always exists.
-   Remove $x$ and $y$ from the sequence and create a new tree node as the parent of the nodes $x$ and $y$, with value $x+y$.
-   Re-insert the new node to the right of the value closest to $x$ among those before the original position of $x$ that are greater than or equal to $x+y$. Because of the left sentinel value, such a position always exists.

To implement this phase efficiently, the algorithm can maintain the current sequence of values in any balanced binary search tree structure. Such a structure lets us remove $x$ and $y$ and re-insert their new parent in logarithmic time. In each step, the weights at even indices of the array up to the value $y$ form a decreasing sequence, and the weights at odd indices form another decreasing sequence. Therefore, the position for re-inserting $x+y$ can be found in logarithmic time by performing two binary searches on these two decreasing sequences using the balanced tree. By a linear sequential search starting from the value $z$ of the previous triple, we can perform the search for the first position satisfying $x \leq z$ in linear total time.

The proof of the third phase of the Garsia–Wachs algorithm, namely that another tree with the same distances exists and that this tree gives the optimal solution of the problem, is very important. However, since there are several ways to prove it and they are too complicated, it is omitted here. Assuming that the third phase is correct, the second and third phases are easy to implement in linear time. Therefore, on an input sequence of length $n$, the total time complexity of the Garsia–Wachs algorithm is $O(n\log n)$.

## Applications

The [garsia-wachs package](https://hackage.haskell.org/package/garsia-wachs) of the functional programming language Haskell provides a functional implementation of the Garsia–Wachs algorithm. It is mainly used to build optimal search tables or to balance the [rope](https://hackage.haskell.org/package/rope) data structure with optimal complexity.

???+ note "Note"
    **rope** is a tool in the Haskell language for manipulating [finger trees](../ds/finger-tree.md) of bytestrings with optional annotations.

## Example problems

???+ note "[POJ 1738 An old Stone Game](http://poj.org/problem?id=1738)"
    There is an old stone game. At the beginning of the game, the player lines up $n$ ($1 \leq n \leq 50000$) piles of stones in a row. The goal is to merge the stones into one pile according to the following rules: in each step of the game, the player may merge two adjacent piles into a new pile. The score is the total number of stones in the new pile. Compute the minimum possible total score.

??? note "Solution idea"
    The stone merging problem is a classic one; we can usually solve it with interval DP, but when the amount of data is large, e.g. $n$ ($1 \leq n \leq 50000$) as in this problem, solving it with the Garsia–Wachs algorithm is more efficient. Step one: initialize an array $\mathit{num}[n]$ of size $n$, where $\mathit{num}[0] = \mathit{num}[n+1] = \infty$. Step two: each time, find the smallest $i$ such that $\mathit{num}[i-1] \leq \mathit{num}[i+1]$ and merge $\mathit{num}[i-1], \mathit{num}[i]$ into $\mathit{temp}$; then find the largest $j$ before it such that $\mathit{num}[j] > \mathit{temp}$ and move $\mathit{temp}$ right after $j$. Repeat this step until $1$ pile remains.
    As for the requirement that only adjacent piles of stones may be merged: since $\mathit{num}[j]\geq \mathit{num}[i-1] + \mathit{num}[i]$, we can regard $\mathit{num}[j+1]$ through $\mathit{num}[i-2]$ as a single whole $\mathit{num}[mid]$, so $\mathit{sum}$ is certainly merged first. Therefore the requirement of the problem is not violated.

???+ note "[ATCODER N-Slimes](https://atcoder.jp/contests/dp/tasks/dp_n)"
    There are $N$ slimes lined up in a row. Initially, the size of the $i$-th slime from the left is $a_{i}$. Taro is trying to combine all the slimes into one larger slime. He repeatedly performs the following operation until there is only one slime:
    choose two adjacent slimes and combine them into a new slime. The new slime has size $x+y$, where $x$ and $y$ are the sizes of the slimes before combining. This step has a cost of $x+y$. The positions of the slimes do not change when they are combined. Find the minimum possible total cost incurred.

## References and further reading

1.  [Garsia–Wachs algorithm - Wikipedia](https://en.wikipedia.org/wiki/Garsia%E2%80%93Wachs_algorithm)
2.  [Data.Algorithm.GarsiaWachs - Hackage Haskell](https://hackage.haskell.org/package/garsia-wachs-1.2/docs/Data-Algorithm-GarsiaWachs.html)
3.  [garsia-wachs: A Functional Implementation of the Garsia-Wachs Algorithm](https://hackage.haskell.org/package/garsia-wachs)
4.  [Sentinel value - Wikipedia](https://en.wikipedia.org/wiki/Sentinel_value)
5.  [A new proof of the Garsia-Wachs algorithm](https://www.sciencedirect.com/science/article/abs/pii/0196677488900090)
