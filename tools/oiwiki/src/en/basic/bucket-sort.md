---
title: Bucket sort
---

This page briefly introduces bucket sort.

## Definition

**Bucket sort** is a sorting algorithm suitable for data whose range of values is large but fairly uniformly distributed.

## Procedure

Bucket sort proceeds in the following steps:

1.  set up an array of a fixed number of empty buckets;
2.  go through the sequence and put each element into its corresponding bucket;
3.  sort every non-empty bucket;
4.  put the elements from the non-empty buckets back into the original sequence.

## Properties

### Stability

If a stable sort is used inside the buckets, and inserting elements into the buckets does not change their relative order, then bucket sort is a stable sorting algorithm.

Since each bucket holds only a few elements, insertion sort is usually used inside the buckets. In that case bucket sort is stable.

### Time complexity

Let $n$ be the number of elements and $k$ the number of buckets. If the elements fall into the buckets independently and uniformly, the average time complexity of bucket sort is $O(n + n^2/k + k)$ (splitting the value range into $k$ equal parts + sorting + merging the elements back), which is $O(n)$ when $k\approx n$.[^ref1]

The worst-case time complexity of bucket sort is $O(n^2+k)$.

## Implementation

Below, the indices of `a[]` start from $1$, and we require $0\le a_i\le w$ and $0\le n<N$, where $w$ is an upper bound on the largest key.

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/bucket-sort/bucket-sort_1.cpp:sort"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/bucket-sort/bucket-sort_1.py:sort"
    ```

## References and notes

[^ref1]: [Bucket sort - Wikipedia](https://en.wikipedia.org/wiki/Bucket_sort#Average-case_analysis)
