---
title: Heap sort
---

This page briefly introduces heap sort.

## Definition

**Heap sort** (heapsort) is a sorting algorithm designed around the [binary heap](../ds/binary-heap.md) data structure. The data structure heap sort operates on is an array.

## Procedure

Heap sort is essentially selection sort built on top of a heap.

### Sorting

First build a max-heap, then take the element at the top of the heap as the maximum, swap it with the element at the end of the array, and restore the heap property on the remainder;

then take the element at the top of the heap as the second largest, swap it with the second-to-last element of the array, and restore the heap property on the remainder;

and so on – after the $(n-1)$-th operation the whole array is sorted.

### Building a binary heap on an array

Starting from the root, place the nodes of each level into the array in order.

Then for the node at index `i` in the array, the parent, left child and right child are as follows:

```cpp
iParent(i) = (i - 1) / 2;
iLeftChild(i) = 2 * i + 1;
iRightChild(i) = 2 * i + 2;
```

## Properties

### Stability

As with selection sort, the swaps in heap sort may change the relative order of equal elements, so it is an unstable sorting algorithm.

### Time complexity

The worst-case time complexity of heap sort is $O(n\log n)$.

### Space complexity

Since the heap can be built on the input array itself, this is an in-place algorithm.

## Implementation

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/heap-sort/heap-sort_1.cpp:sort"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/heap-sort/heap-sort_1.py:sort"
    ```

## External links

-   [Heapsort – Wikipedia](https://en.wikipedia.org/wiki/Heapsort)
