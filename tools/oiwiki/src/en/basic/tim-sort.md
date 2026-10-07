---
title: Timsort
---

This page introduces Timsort, a hybrid, stable sorting algorithm.

## Introduction

Timsort was designed in 2002 by Tim Peters, a Python core developer, and used in the Python language. It cleverly combines the advantages of insertion sort and merge sort and is precisely optimized for the order already present in the data, which makes it especially suitable for data sets containing many partially sorted subsequences. CPython has used Timsort since version 2.3, and since version 3.11 its merge-order strategy has been replaced by Powersort[^powersort]. Timsort is also widely used in other programming environments; for example, in Java SE 7 it is used to sort arrays of non-primitive objects.

This page describes traditional Timsort, taking as reference the merge rules of CPython 3.6.5, in which the problem with maintaining the stack invariant was fixed[^merge-policy].

## Steps

The core idea of Timsort is to improve sorting efficiency by recognizing and exploiting the order already present in the data. Its main steps are:

1.  **Identify runs**: scan the array to be sorted and identify sorted contiguous subsequences (runs);
2.  **Extend runs**: if an identified run is shorter than `MIN_RUN`, extend it with insertion sort;
3.  **Merge runs**: Timsort maintains a special stack and uses a specific merge strategy to merge the runs on the stack into larger sorted sequences.

### Identifying runs

First, Timsort scans the array from left to right and identifies contiguous sorted sequences, which are called runs:

-   **Ascending run**: if the next element is greater than or equal to the previous one, keep extending the run.
-   **Descending run**: if the next element is smaller than the previous one, keep extending the run, then reverse the run into ascending order.

### Extending runs

To sort small amounts of data more efficiently, Timsort introduces a minimum run length `MIN_RUN`. Its value is usually computed dynamically from the length of the array to be sorted and is typically between $32$ and $64$.

-   If the identified run is at least `MIN_RUN` long, no extra work is needed and the run is pushed directly onto the stack.
-   If the identified run is shorter than `MIN_RUN`, binary insertion sort is used to insert the following elements into the run until its length reaches `MIN_RUN`, and then it is pushed onto the stack.

### Merging runs

In Timsort the merging is managed and controlled through a **stack**. The stack holds the sorted runs identified so far, and specific merge rules control how the runs on the stack are merged, with the goal of keeping the sequences balanced and the sort stable while merging.

#### Merge rules

Timsort is a stable sorting algorithm, i.e. equal elements keep their original relative order after sorting. To guarantee this, Timsort only merges adjacent, contiguous runs and never directly merges non-adjacent runs. Non-adjacent runs may contain equal elements, and merging them directly would very likely disturb their relative order.

At the same time, to control the balance of the merges and the number of runs waiting to be merged, Timsort requires every three adjacent runs on the stack to satisfy the following invariants. Denote the three runs from the top of the stack toward the bottom by X, Y and Z:

-   **Condition 1**: `len(Z) > len(Y) + len(X)`
-   **Condition 2**: `len(Y) > len(X)`

When there are only two runs on the stack, `len(Y) > len(X)` is also required. After each new run is pushed, `mergeCollapse` examines at most four runs at the top of the stack; denote them from the top downward by X, Y, Z, W. Merging is decided in the following order[^merge-policy]:

1.  if `len(Z) <= len(Y) + len(X)` or `len(W) <= len(Z) + len(Y)`, merge Y with the shorter of X and Z; if X and Z have equal length, choose X;
2.  otherwise, if `len(Y) <= len(X)`, merge Y and X;
3.  otherwise, stop this round of merging and continue identifying the next run.

Only the conditions whose required runs all exist are checked; after each merge, X, Y, Z, W are determined again and the process above is repeated. The figure below illustrates how the stack changes when X and Y are merged.

![Merge Rules](./images/tim-sort-1.svg)

???+ note "Why does the fourth run need to be checked?"
    Checking only the top three runs of the stack may, after a merge, miss a violated invariant deeper in the stack. For example, push runs of lengths $240,160,50,40,60$ in order (from bottom to top of the stack); the old rule would merge $50$ and $40$, giving $240,160,90,60$. The top of the stack now satisfies $160>90+60$ and $90>60$, but deeper down $240\le160+90$.
    
    This flaw invalidates the fixed stack capacity guarantee derived from the whole-stack invariant. CPython fixed the check conditions in 2015[^merge-fix].

#### Merge optimization

To merge runs of different lengths more efficiently and with less memory overhead, Timsort uses binary search before merging to pinpoint the range of elements that actually needs processing, and only merges the part that has to move. Specifically:

1.  **Determine the insertion points**: use binary search to find the position where the first element of the second run would be inserted into the first run, and the position where the last element of the first run would be inserted into the second run. This narrows the range to be merged so that only the elements that need to move are processed;

2.  **Temporary buffer**: traditional in-place merge algorithms are too inefficient and require many element moves. To reduce this overhead, Timsort uses a temporary buffer: it copies the shorter run into the buffer and then gradually copies elements from the buffer back into the original array.

For example, suppose there are two runs A and B:

-   Run A: $[1, 2, 3, 6, 10]$
-   Run B: $[4, 5, 7, 9, 12, 14, 17]$

Using binary search we determine:

-   element $4$ should be inserted at the fourth position of run A;
-   element $10$ should be inserted at the fifth position of run B.

Therefore the first $3$ elements of run A and the last $3$ elements of run B are already in the correct positions and need no processing. Only $[6, 10]$ from run A and $[4, 5, 7, 9]$ from run B need to be merged; the merge process is shown in the figure below:

![Timsort Merge](./images/tim-sort-2.apng)

#### Galloping mode

To further improve merge efficiency, Timsort introduces **galloping mode**. In a standard merge, the algorithm compares the elements of the two runs one by one and places the smaller one into the result array. However, if one run contains a long stretch of consecutive elements smaller than the current element of the other run, comparing one by one causes unnecessary overhead.

To solve this, Timsort sets a threshold `Min_Gallop` (default $7$). When the number of consecutive "wins" by elements of one run reaches `Min_Gallop`, the algorithm enters galloping mode and quickly locates the position of the element. The steps are:

1.  **Exponential search**: starting from the current position, the algorithm searches one run with exponentially growing steps $(1, 2, 4, 8, \dots)$ until it finds an interval containing the target element;
2.  **Binary search**: once the interval containing the target element is determined, the algorithm uses binary search within that interval to pinpoint the position of the target element.

In this way Timsort skips many unnecessary comparisons, quickly handles the consecutive smaller (or larger) elements of one run and moves them into the merge result in bulk.

Galloping mode is not more efficient in every case, however. For some data distributions it may lead to more comparisons. Therefore Timsort uses a dynamic adjustment strategy:

-   **Threshold adjustment**: a variable `Min_Gallop` parameter is maintained. When galloping mode performs well (i.e. elements are repeatedly taken from the same run), `Min_Gallop` is decreased by $1$ to encourage further galloping; when galloping mode performs poorly (frequent switching between the two runs), `Min_Gallop` is increased by $1$ to reduce how often galloping is used.

By dynamically adjusting the value of `Min_Gallop`, the algorithm strikes a balance between normal merging and galloping mode based on the actual data. For partially or highly ordered data, galloping mode can significantly improve efficiency and bring the performance of Timsort close to $O(n)$; for random data, the algorithm gradually leans toward normal merging, which guarantees the $O(n \log n)$ time complexity.

## Complexity

The time complexity of Timsort depends on how ordered the data is:

-   **Best case**: $O(n)$
    -   When the data is already sorted or nearly sorted, the runs identified by the algorithm have length close to $n$, the number of merges decreases and the complexity approaches $O(n)$.
-   **Worst case**: $O(n \log n)$
    -   If there are $r$ runs, $r-1$ two-way merges are needed in the end; the number of merges cannot be written as $O(\log n)$.

Identifying runs costs $O(n)$, and extending short runs with a bounded `MIN_RUN` also costs $O(n)$ in total. The merge cost is the sum of the lengths of the two runs merged each time, which equals the sum over all elements of the number of merges each element takes part in. The upper bound on this sum depends on the specific merge rules; for the Python 3.6.5 TimSort merge rules analyzed in the literature[^complexity], amortized analysis gives $O(n+n\log r)$, hence the worst case is $O(n\log n)$.

As for space complexity, since Timsort needs roughly $O(n)$ extra space for the stack and the temporary buffer, the total space complexity is $O(n)$.

## Implementation

???+ note "Pseudocode"
    $$
    \begin{array}{ll}
    1 & \textit{nRemaining} \gets \text{length of the array} \\
    2 & \textit{minRun} \gets \text{choose a suitable value of MinRun}(\textit{nRemaining}) \\
    3 & \textit{startIndex} \gets 0 \\
    4 & \textbf{while } \textit{nRemaining} > 0 \ \textbf{do} \\
    5 & \qquad \textit{runLength} \gets \text{identify run }(\textit{array}, \textit{startIndex}, \textit{nRemaining}) \\
    6 & \qquad \textbf{if } \textit{runLength} < \textit{minRun} \ \textbf{then} \\
    7 & \qquad \qquad \textit{extendLength} \gets \min(\textit{minRun}, \textit{nRemaining}) \\
    8 & \qquad \qquad \text{extend the interval } [\textit{startIndex}, \textit{startIndex} + \textit{extendLength} - 1] \text{ with insertion sort}\\
    9 & \qquad \qquad \textit{runLength} \gets \textit{extendLength} \\
    10 & \qquad \textbf{end if} \\
    11 & \qquad \text{push run } (\textit{startIndex}, \textit{runLength}) \text{ onto the stack} \\
    12 & \qquad \textbf{call } \text{mergeCollapse(stack)} \ \text{to check and merge the runs on the stack} \\
    13 & \qquad \textit{startIndex} \gets \textit{startIndex} + \textit{runLength} \ \text{update the start position} \\
    14 & \qquad \textit{nRemaining} \gets \textit{nRemaining} - \textit{runLength} \ \text{update the remaining length} \\
    15 & \textbf{end while} \\
    16 & \textbf{call } \text{mergeForceCollapse(stack)} \ \text{to finally merge all runs on the stack} \\
    \end{array}
    $$

## References and notes

1.  [Timsort](https://en.wikipedia.org/wiki/Timsort)
2.  [Tim Peters' design notes (CPython 3.6.5; merge conditions follow the code of that version)](https://github.com/python/cpython/blob/v3.6.5/Objects/listsort.txt)
3.  [Java implementation](https://cs.android.com/android/platform/superproject/main/+/main:libcore/ojluni/src/main/java/java/util/TimSort.java)
4.  [C implementation (CPython 3.6.5)](https://github.com/python/cpython/blob/v3.6.5/Objects/listobject.c)

[^complexity]: [On the Worst-Case Complexity of TimSort](https://drops.dagstuhl.de/opus/volltexte/2018/9467/pdf/LIPIcs-ESA-2018-4.pdf).

[^powersort]: [CPython: the commit adopting the Powersort merge-order strategy](https://github.com/python/cpython/commit/5cb4c672d855033592f0e05162f887def236c00a); [description of the merge strategy in CPython 3.11](https://github.com/python/cpython/blob/v3.11.0/Objects/listsort.txt#L329-L347).

[^merge-policy]: [CPython 3.6.5: `merge_collapse`](https://github.com/python/cpython/blob/v3.6.5/Objects/listobject.c#L1816-L1849).

[^merge-fix]: [CPython Issue 23515: Bad logic in timsort's merge\_collapse](https://bugs.python.org/issue23515).
