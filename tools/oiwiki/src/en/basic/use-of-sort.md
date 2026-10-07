---
title: Uses of sorting
---

This page briefly introduces the uses of sorting.

## Understanding the characteristics of data

Processing data by sorting helps us understand its characteristics and makes later analysis and visualisation easier. Take everyday examples such as a dictionary or a menu: if they were not arranged in some order, the time people need to find what they are looking for would increase dramatically.

Computers have to process large amounts of data; after sorting, people can design the subsequent processing steps according to the characteristics of the data and their needs.

## Reducing time complexity

Sorting as a preprocessing step can reduce the time complexity needed to solve a problem; usually this is a trade-off of space for time. If a sorted list needs to be analysed many times, spending the resources for a single sort is well worth it, since every subsequent analysis saves a lot of time.

???+ note "Example: check whether a given sequence contains equal elements"
    Consider a sequence of numbers; you need to check whether it contains two equal elements.
    
    A naive approach checks every pair of numbers and tests whether they are equal. The time complexity is $O(n^2)$.
    
    Instead, let us sort the sequence first; then it is easy to see that if there are two equal numbers, they must be adjacent in the new sequence. Now a single $O(n)$ scan of the new sequence suffices.
    
    The total time complexity is that of sorting, $O(n\log n)$.

## Preprocessing for searching

Sorting is the preprocessing required by [binary search](./binary.md). Using binary search after sorting, a given element can be found in the sequence in $O(\log n)$ time.
