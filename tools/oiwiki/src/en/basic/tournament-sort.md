---
title: Tournament sort
---

This page briefly introduces tournament sort.

## Definition

**Tournament sort**, also known as tree selection sort, is an optimised version of [selection sort](./selection-sort.md) and a variant of [heap sort](./heap-sort.md) (both use a complete binary tree). It builds on selection sort by using a priority queue to find the next element to select.

## Introduction

Tournament sort takes its name from single-elimination tournaments. In such a format many players take part; they are compared in pairs and the winner advances to the next round. This kind of elimination determines the best player, but the player eliminated in the final round is not necessarily the second best – they may be worse than a player eliminated earlier.

## Procedure

Take a **minimum tournament tree** as an example:

![tournament-sort1](./images/tournament-sort1.svg)

The elements to be sorted are shown in the leaves. The red edges show the winning path of the smaller element in each round of comparisons. Clearly, one "tournament" selects the smallest element of a set.

After each round of comparisons among $n$ elements we get $\left\lceil\dfrac{n}{2}\right\rceil$ "winners"; the smaller element of each pair enters the next round. If an element cannot be paired, it goes straight into the next round.

![tournament-sort2](./images/tournament-sort2.svg)

After a "tournament" is completed, the selected element must be removed. Simply set it to $\infty$ (an operation similar to the one in [heap sort](./heap-sort.md)), then hold the "tournament" again to select the second smallest element.

Repeat this until all elements are sorted.

## Properties

### Stability

Tournament sort is an unstable sorting algorithm.

### Time complexity

The best, average and worst-case time complexity of tournament sort are all $O(n\log n)$. It takes $O(n)$ time to initialise the "tournament" and then $O(\log n)$ time to select one element out of $n$.

### Space complexity

The space complexity of tournament sort is $O(n)$.

## Implementation

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/tournament-sort/tournament-sort_1.cpp:sort"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/tournament-sort/tournament-sort_1.py:sort"
    ```

## External links

-   [Tournament sort - Wikipedia](https://en.wikipedia.org/wiki/Tournament_sort)
