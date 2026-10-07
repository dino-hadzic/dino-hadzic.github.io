---
title: Interval DP
---

## Definition

Interval DP is an extension of linear dynamic programming: when the problem is split into stages, the order in which the elements appear within a stage, and which elements of the previous stage the current state was merged from, matter a great deal.

Let the state $f(i,j)$ denote the maximum value obtainable by merging all elements at positions $i$ through $j$. Then $f(i,j)=\max\{f(i,k)+f(k+1,j)+cost\}$, where $cost$ is the value of merging these two groups of elements.

## Properties

Interval DP has the following characteristics:

**Merging**: two or more parts are combined into a whole (or, of course, the reverse);

**Feature**: the problem can be decomposed into a form in which parts are merged pairwise;

**Solving**: define the optimal value for the whole problem, enumerate the merge point, split the problem into a left and a right part, and finally merge the optimal values of the two parts to obtain the optimal value of the original problem.

## Explanation

### Example

???+ note "[\"NOI1995\" Merging Stones](https://loj.ac/problem/10147)"
    Problem summary: there are $n$ numbers $a_1,a_2,\dots,a_n$ on a circle. Perform $n-1$ merge operations; each operation merges two adjacent piles into one and scores the number of stones in the new pile. Maximize your total score.

First consider the case where the piles are not on a circle but in a line.

Let $f(i,j)$ denote the maximum score obtainable by merging all stones in the interval $[i,j]$ into one pile.

Write the **state transition equation**: $f(i,j)=\max\{f(i,k)+f(k+1,j)+\sum_{t=i}^{j} a_t \}~(i\le k<j)$

Let $sum_i$ denote the prefix sum of the array $a$; the transition becomes $f(i,j)=\max\{f(i,k)+f(k+1,j)+sum_j-sum_{i-1} \}$.

### How to perform the state transitions

Since computing $f(i,j)$ requires all the values $f(i,k)$ and $f(k+1,j)$, and both of these contain fewer elements than $f(i,j)$, we use $len=j-i+1$ as the stage of the DP. First enumerate $len$ from small to large, then enumerate $i$, compute $j$ from $len$ and $i$ by the formula, and finally enumerate $k$. The time complexity is $O(n^3)$.

### How to handle the circle

In the problem the stones form a circle rather than a line. What do we do?

**Method 1**: since the stones form a circle, we can enumerate the position where we cut it, turning the circle into a line. As this must be done $n$ times, the final time complexity is $O(n^4)$.

**Method 2**: extend the line to twice its length, i.e. $2\times n$ piles, where pile $i$ is identical to pile $n+i$. After solving with dynamic programming, take the best of $f(1,n),f(2,n+1),\dots,f(n,2n-1)$; that is the final answer. Time complexity $O(n^3)$.

## Implementation

=== "C++"
    ```cpp
    for (len = 2; len <= n; len++)
      for (i = 1; i <= 2 * n - len; i++) {
        int j = len + i - 1;
        for (k = i; k < j; k++)
          f[i][j] = max(f[i][j], f[i][k] + f[k + 1][j] + sum[j] - sum[i - 1]);
      }
    ```

=== "Python"
    ```python
    for len in range(2, n + 1):
        for i in range(1, 2 * n - len + 1):
            j = len + i - 1
            for k in range(i, j):
                f[i][j] = max(f[i][j], f[i][k] + f[k + 1][j] + sum[j] - sum[i - 1])
    ```

## A few exercises

[NOIP 2006 Energy Necklace](https://www.luogu.com.cn/problem/P1063)

[NOIP 2007 Matrix Number Game](https://www.luogu.com.cn/problem/P1005)

[\"IOI2000\" Post Office](https://www.luogu.com.cn/problem/P4767)
