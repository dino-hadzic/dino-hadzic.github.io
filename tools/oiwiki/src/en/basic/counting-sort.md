---
title: Counting sort
---

Prerequisites: [Prefix sums](./prefix-sum.md)

???+ warning "Reminder"
    This page is not about [**radix sort**](./radix-sort.md).

This page briefly introduces counting sort.

## Definition

**Counting sort** is a linear-time sorting algorithm.

## Procedure

Counting sort works by using an extra array $C$, whose $i$-th element is the number of elements in the array $A$ to be sorted whose value equals $i$; then it uses the array $C$ to place the elements of $A$ into their correct positions.[^ref1]

The process consists of three steps:

1.  count how many times each number occurs;
2.  compute the [prefix sums](./prefix-sum.md) of the counts;
3.  using the prefix sums of the counts, from right to left, compute the rank of each number.

### Why prefix sums are computed

Rebuilding from the frequencies can sort pure keys and handle duplicates; but to stably rearrange the original records, the output positions are determined from the prefix sums of the frequencies.

By computing the prefix sum of each entry of the extra array $C$ and combining it with the entry's value, we can assign a unique rank to each of the duplicate elements:

the value of an entry of $C$ is the number of duplicates with that key, and its prefix sum is the rank of the last of those duplicates.

If we place the elements in reverse order of $A$, the sorted array clearly keeps the original order of $A$ (for equal keys), i.e. we obtain a stable sorting algorithm.

![counting sort animate example](images/counting-sort-animate.svg)

## Properties

### Stability

Counting sort is a stable sorting algorithm.

### Time complexity

The time complexity of counting sort is $O(n+w)$, where $w$ is the size of the range of the values to be sorted.

## Implementation

### Pseudocode

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{An array } A \text{ consisting of }n\text{ positive integers no greater than } w. \\
2 & \textbf{Output. } \text{Array }A\text{ after sorting in nondecreasing order stably.} \\
3 & \textbf{Method. }  \\
4 & \textbf{for }i\gets0\textbf{ to }w\\
5 & \qquad \textit{cnt}[i]\gets0\\
6 & \textbf{for }i\gets1\textbf{ to }n\\
7 & \qquad \textit{cnt}[A[i]]\gets\textit{cnt}[A[i]]+1\\
8 & \textbf{for }i\gets1\textbf{ to }w\\
9 & \qquad \textit{cnt}[i]\gets \textit{cnt}[i]+\textit{cnt}[i-1]\\
10 & \textbf{for }i\gets n\textbf{ downto }1\\
11 & \qquad B[\textit{cnt}[A[i]]]\gets A[i]\\
12 & \qquad \textit{cnt}[A[i]]\gets \textit{cnt}[A[i]]-1\\
13 & \textbf{return } B
\end{array}
$$

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/counting-sort/counting-sort_1.cpp"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/counting-sort/counting-sort_1.py:core"
    ```

## References and notes

[^ref1]: [Counting sort – Wikipedia](https://en.wikipedia.org/wiki/Counting_sort)
