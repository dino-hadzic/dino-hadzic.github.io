---
title: Hanging line method
---

## Introduction

The scope of the hanging line method (also "hoverline") is a subset of that of the monotonic stack. Specifically, the hanging line method can be applied to problems that satisfy the following conditions:

-   monotonic information needs to be maintained while scanning a sequence;
-   they can be solved with a monotonic stack;
-   no binary search on the monotonic stack is needed.

It seems the hanging line method can be replaced and is not very useful, but its concept is simpler than that of the monotonic stack, so it is more suitable for beginners in OI to understand and solve problems such as the largest submatrix.

## Example problems

???+ note "[SPOJ HISTOGRA - Largest Rectangle in a Histogram](https://www.spoj.com/problems/HISTOGRA)"
    In short: there are $n$ rectangles of width $1$ on a horizontal line; find the area of the largest sub-rectangle contained in these rectangles.

A hanging line is a vertical segment with two properties, an initial position and a height, and it can move left and right as long as its upper endpoint does not exceed the height of the rectangle at its current position.

For a hanging line, under the condition that its upper endpoint does not exceed the height of the rectangle at the current position and it does not move out of bounds, we move it left and right and find how far it can extend to the left and to the right at most; the area swept by this hanging line is then the largest possible rectangle containing this hanging line. It is easy to see that the largest sub-rectangle must contain a hanging line with initial position $i$ and height $h_i$. Implementing this process by enumeration has time complexity $O(n ^ 2)$, but with the hanging line method we can optimize it to $O(n)$.

Let us consider how to quickly find the leftmost position a hanging line can reach.

### Process

Define $l_i$ as the leftmost position found so far to which the hanging line at position $i$ can extend; clearly $l_i$ is initially $i$, and we need to further check whether it can extend further to the left.

-   If currently $l_i = 1$, we have reached the boundary and cannot.
-   If currently $a_i > a_{l_i - 1}$, the position the current hanging line has extended to cannot extend further to the left.
-   If currently $a_i \le a_{l_i - 1}$, the current hanging line can extend further to the left, and wherever the hanging line at position $l_i - 1$ can extend to the left, the hanging line at position $i$ can certainly extend as well, so we update $l_i$ to $l_{l_i - 1}$ and continue checking.

By amortized analysis, it can be proved that each $l_i$ is visited at most once by other $l_j$, so the time complexity is $O(n)$.

### Implementation

??? note "Reference code"
    ```cpp
    --8<-- "docs/misc/code/hoverline/hoverline_1.cpp"
    ```

???+ note "[UVa1619 Feel Good](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=4494)"
    For a sequence of length $n$, find a subarray such that the product of the minimum value in the subarray and the sum of its elements is maximized; among those with the maximum comfort value minimize the length, and among those with the minimum length minimize the index of the left endpoint.

In this problem we can enumerate the minimum value: treat the number $a_i$ at each position as the minimum, and consider extending from $i$ to the left and right to find the widest possible range $[l, r]$ satisfying $\min\limits _ {j = l} ^ r a_j = a_i$. Thus the problem is transformed into the hanging line model.

??? note "Reference code"
    ```cpp
    --8<-- "docs/misc/code/hoverline/hoverline_2.cpp"
    ```

## Largest submatrix

???+ note "[P4147 玉蟾宫 (Jade Toad Palace)](https://www.luogu.com.cn/problem/P4147)"
    Given an $n \times m$ matrix containing `'F'` and `'R'`, find the area of its largest submatrix $\times 3$ such that every cell of this submatrix is `'F'`.

We notice that the model of this problem is very similar to the model of the first problem. On closer analysis, if we consider only all elements of one row at a time, and take the distance an element at position $(x, y)$ can extend upward as the hanging line length at that position, then the largest submatrix must be one of the largest rectangles obtained by extending these hanging lines to the left and right.

??? note "Reference code"
    ```cpp
    --8<-- "docs/misc/code/hoverline/hoverline_3.cpp"
    ```

## Exercises

-   [P1169「ZJOI2007」棋盘制作 (Chessboard Making)](https://www.luogu.com.cn/problem/P1169)
