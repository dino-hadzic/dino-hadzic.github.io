---
title: Minimal representation
---

## Definition

The minimal representation algorithm solves the problem of finding the minimal representation of a string.

## Minimal representation of a string

### Cyclic equivalence

If we can choose, in string $S$, a position $i$ such that

$$
S[i\cdots n]+S[1\cdots i-1]=T
$$

then $S$ and $T$ are called cyclically equivalent.

### Minimal representation

The minimal representation of a string $S$ is the lexicographically smallest of all strings cyclically equivalent to $S$.

## Simple brute force

Each time, compare the cyclic shifts starting at $i$ and $j$, and denote the current comparison offset by $k$. Whenever different characters are encountered, skip the larger candidate. The one left at the end is the optimal solution.

### Implementation

=== "C++"
    ```cpp
    int k = 0, i = 0, j = 1;
    while (k < n && i < n && j < n) {
      if (sec[(i + k) % n] == sec[(j + k) % n]) {
        ++k;
      } else {
        if (sec[(i + k) % n] > sec[(j + k) % n])
          ++i;
        else
          ++j;
        k = 0;
        if (i == j) i++;
      }
    }
    i = min(i, j);
    ```

=== "Python"
    ```python
    k, i, j = 0, 0, 1
    while k < n and i < n and j < n:
        if sec[(i + k) % n] == sec[(j + k) % n]:
            k += 1
        else:
            if sec[(i + k) % n] > sec[(j + k) % n]:
                i += 1
            else:
                j += 1
            k = 0
            if i == j:
                i += 1
    i = min(i, j)
    ```

### Explanation

This implementation performs well on random data, but specially constructed inputs can make it too slow.

For example, for $\texttt{aaa}\cdots\texttt{aab}$, it is easy to see that the complexity degrades to $O(n^2)$.

The algorithm becomes less efficient when the string contains several consecutive repeated substrings. Let us optimize this process.

## Minimal representation algorithm

### Core idea

Consider two strings $A,B$ starting in the original string $S$ at positions $i,j$, with the same first $k$ characters, that is,

$$
S[i \cdots i+k-1]=S[j \cdots j+k-1]
$$

First consider the case $S[i+k]>S[j+k]$. No string whose starting index $l$ satisfies $i\le l\le i+k$ can be the answer. For any string $S_{i+p}$ (the string starting at $i+p$, where $p \in [0, k]$), there is always a better string $S_{j+p}$.

Thus, during comparison we can skip the indices $l\in [i,i+k]$ and compare $S_{i+k+1}$ directly.

This completes the optimization of the brute-force method above.

### Time complexity

$O(n)$

### Procedure

1.  Initialize pointer $i$ to $0$ and $j$ to $1$, and initialize the matched length $k$ to $0$.
2.  Compare the characters at offset $k$ and advance the corresponding pointer according to the result. If the two pointers become equal, increment either one to ensure that the strings being compared are different.
3.  Repeat until the comparison is complete.
4.  The answer is the smaller of $i,j$.

### Implementation

=== "C++"
    ```cpp
    int k = 0, i = 0, j = 1;
    while (k < n && i < n && j < n) {
      if (sec[(i + k) % n] == sec[(j + k) % n]) {
        k++;
      } else {
        sec[(i + k) % n] > sec[(j + k) % n] ? i = i + k + 1 : j = j + k + 1;
        if (i == j) i++;
        k = 0;
      }
    }
    i = min(i, j);
    ```

=== "Python"
    ```python
    k, i, j = 0, 0, 1
    while k < n and i < n and j < n:
        if sec[(i + k) % n] == sec[(j + k) % n]:
            k += 1
        else:
            if sec[(i + k) % n] > sec[(j + k) % n]:
                i = i + k + 1
            else:
                j = j + k + 1
            if i == j:
                i += 1
            k = 0
    i = min(i, j)
    ```
