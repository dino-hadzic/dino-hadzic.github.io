---
title: Introduction to sorting
---

This page briefly introduces sorting algorithms.

## Definition

A **sorting algorithm** is an algorithm that arranges a given collection of data in a certain order. There are many sorting algorithms, and their properties differ widely.

## Properties

### Stability

Stability refers to whether the relative order of equal elements changes after sorting.

A stable algorithm keeps the relative order of records with equal keys: if a sorting algorithm is stable and there are two records $R$ and $S$ with equal keys such that $R$ appears before $S$ in the original list, then $R$ will also appear before $S$ in the sorted list.

Radix sort, counting sort, insertion sort, bubble sort and merge sort are stable sorts.

Selection sort, heap sort, quick sort and shell sort are not stable.

### Time complexity

Main page: [Complexity](./complexity.md)

Time complexity measures the relationship between an algorithm's running time and the input size, and is usually written using $O$ notation.

A simple way to estimate complexity is to count the number of "elementary operations" performed; sometimes one can also approximate it by counting the levels of nested loops.

Time complexity is divided into best-case, average-case and worst-case. In OI contests one usually considers the worst case, because it is the lower bound on how well the algorithm runs – nothing worse can happen during judging.

Any comparison-based algorithm that sorts $n$ distinct elements needs $\Omega(n\log n)$ comparisons in the worst case.

Of course, there are also algorithms that are not $O(n\log n)$. For example, the time complexity of [counting sort](./counting-sort.md) is $O(n+w)$, where $w$ is the size of the range of the input values.

Below is a comparison of several sorting algorithms.

![Comparison of several sorting algorithms](images/sort-intro-1.apng)

### Space complexity

Similarly to time complexity, space complexity describes how much memory an algorithm uses. In general, the smaller the space complexity, the better the algorithm.

## External links

-   [Sorting algorithm – Wikipedia](https://en.wikipedia.org/wiki/Sorting_algorithm)
