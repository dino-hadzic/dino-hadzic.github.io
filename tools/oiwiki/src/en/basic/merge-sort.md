---
title: Merge sort
---

This page introduces merge sort and its application to counting inversions.

## Definition

**Merge sort** ([merge sort](https://en.wikipedia.org/wiki/Merge_sort)) is an efficient, comparison-based, stable sorting algorithm.

## Properties

Merge sort is based on the divide-and-conquer idea: it splits the array into segments, sorts them and merges them. Its time complexity in the best, worst and average case is $\Theta (n \log n)$, and its space complexity is $\Theta (n)$.

Merge sort can be done with only $\Theta (1)$ auxiliary space, but for convenience an auxiliary array of the same length as the original is usually used.

## Procedure

### Merging

The core part of merge sort is the merge procedure: merging two sorted arrays `a` and `b` into one sorted array `c`.

Scan `a[i]` and `b[j]` from left to right, each time writing the smaller element into `c[k]`; when one array is exhausted, append the remaining elements of the other array to `c`.

To keep the sort stable, the first element of the front segment must be placed into `c[k]` as the minimum when it is less than **or equal to** the first element of the back segment (`a[i] <= b[j]`), not only when it is strictly less (`a[i] < b[j]`).

#### Implementation

=== "C/C++"
    === "Array version"
        ```cpp
        --8<-- "docs/basic/code/merge-sort/merge-sort_1.cpp:array"
        ```
    
    === "Pointer version"
        ```cpp
        --8<-- "docs/basic/code/merge-sort/merge-sort_1.cpp:pointer"
        ```
    
    You can also use the `std::merge` function from the `<algorithm>` library; its usage is the same as the pointer version above.

=== "Python"
    ```python
    --8<-- "docs/basic/code/merge-sort/merge-sort_1.py:merge"
    ```

### Merge sort by divide and conquer

1.  When the array has length $1$, it is already sorted and need not be split further.
2.  When the array has length greater than $1$, it is most likely not sorted. Split it into two segments and check each of them for sortedness (using rule 1). If they are sorted, merge them into one sorted array; otherwise repeat rule 2 on the unsorted segments and then merge.

By mathematical induction one can prove that this procedure turns an array into a sorted array.

To guarantee the complexity, the array is usually split into two segments of as equal length as possible ($\textit{mid} = \left\lfloor \dfrac{l + r}{2} \right\rfloor$).

#### Implementation

Note that the intervals represented in the code below are $[l, r)$, $[l, \textit{mid})$ and $[\textit{mid}, r)$ respectively.

=== "C/C++"
    ```cpp
    --8<-- "docs/basic/code/merge-sort/merge-sort_1.cpp:recursive"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/merge-sort/merge-sort_1.py:recursive"
    ```

### Merge sort by doubling (bottom-up)

We know that an array of length $1$ is already sorted.

Cut the whole array into segments of length $1$.

From left to right, merge pairs of sorted segments of length $1$, obtaining a series of sorted segments of length $\le 2$;

from left to right, merge pairs of sorted segments of length $\le 2$, obtaining a series of sorted segments of length $\le 4$;

from left to right, merge pairs of sorted segments of length $\le 4$, obtaining a series of sorted segments of length $\le 8$;

…

Repeat until only one sorted segment is left; that segment is the sorted original array.

???+ note "Why $\le$ rather than $=$"
    The length of the array is most likely not of the form $2^x$, so an incomplete segment may appear at the end, and the last segment may be left on its own.

#### Implementation

=== "C/C++"
    ```cpp
    --8<-- "docs/basic/code/merge-sort/merge-sort_1.cpp:iterative"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/merge-sort/merge-sort_1.py:iterative"
    ```

## Inversions

Further reading and reference implementation: [Inversions](../math/permutation.md#逆序数)

An inversion is an ordered pair $(i, j)$ with $i < j$ and $a_i > a_j$.

A sorted array has no inversions. In the merge step of merge sort, every time the first element of the back segment is taken as the current minimum, the number of remaining elements in the front segment is the number of inversions removed by that merge; hence merge sort counts inversions in $\Theta (n \log n)$ time. Inversions can also be counted with a Fenwick tree or a segment tree, also in $O(n \log n)$; a detailed explanation of that algorithm is in the corresponding part of the [Fenwick tree](../ds/fenwick.md#全局逆序对全局二维偏序) chapter. Reference implementations of both algorithms are in the [Inversions](../math/permutation.md#逆序数) chapter.

## External links

-   [Merge Sort - GeeksforGeeks](https://www.geeksforgeeks.org/merge-sort/)
-   [Merge sort – Wikipedia](https://en.wikipedia.org/wiki/Merge_sort)
-   [Inversion (discrete mathematics) – Wikipedia](https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics))
