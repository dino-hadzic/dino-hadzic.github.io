---
title: Selection sort
---

This page briefly introduces selection sort.

## Definition

**Selection sort** is a simple and intuitive sorting algorithm. It works by finding the $i$-th smallest element in each step (that is, the smallest element among $A_{i..n}$) and swapping it with the element at position $i$ of the array.

![selection sort animate example](images/selection-sort-animate.svg)

## Properties

### Stability

The stability of selection sort depends on the implementation.

If it is implemented with a linked list, then, since insertion and deletion at any position of a linked list are $O(1)$, no swap operation (exchanging two elements) is needed: in each step select the smallest element of the unsorted part (if there are several, take the first one) and insert it before the first element of the unsorted part; this guarantees stability.

Array implementations usually use `swap` to move the smallest element into the sorted part in order to reduce the number of moves, so they are unstable.

All implementations given below are based on swapping array elements and are therefore **unstable**.

### Time complexity

The best, average and worst-case time complexity of selection sort are all $O(n^2)$.

## Implementation

### Pseudocode

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{An array } A \text{ consisting of }n\text{ elements.} \\
2 & \textbf{Output. } A\text{ will be sorted in nondecreasing order.} \\
3 & \textbf{Method. }  \\
4 & \textbf{for } i\gets 1\textbf{ to }n-1\\
5 & \qquad \textit{ith}\gets i\\
6 & \qquad \textbf{for }j\gets i+1\textbf{ to }n\\
7 & \qquad\qquad\textbf{if }A[j]<A[\textit{ith}]\\
8 & \qquad\qquad\qquad \textit{ith}\gets j\\
9 & \qquad \text{swap }A[i]\text{ and }A[\textit{ith}]\\
\end{array}
$$

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/selection-sort/selection-sort_1.cpp"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/selection-sort/selection-sort_1.py:core"
    ```

=== "Java"
    ```java
    // the indices of arr start from 1
    static void selection_sort(int[] arr, int n) {
        for (int i = 1; i < n; i++) {
            int ith = i;
            for (int j = i + 1; j <= n; j++) {
                if (arr[j] < arr[ith]) {
                    ith = j;
                }
            }
            // swap
            int temp = arr[i];
            arr[i] = arr[ith];
            arr[ith] = temp;
        }
    }
    ```
