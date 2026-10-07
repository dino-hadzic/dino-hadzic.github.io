---
title: Backtracking
---

This page briefly introduces the concept of backtracking and its applications.

## Introduction

Backtracking is a technique frequently used in [depth-first search (DFS)](./dfs.md) and [breadth-first search (BFS)](./bfs.md).

Its essence is: if you cannot go on, turn back.

## Procedure

1.  Build the state-space tree;

2.  traverse it;

3.  when a boundary condition is met, stop searching downward and switch to another branch;

4.  when the target condition is reached, output the result.

## Examples

???+ example "[USACO 1.5.4 Checker Challenge](https://www.luogu.com.cn/problem/P1219)"
    Consider the following $6 \times 6$ checkerboard, on which six checkers are placed so that each row, each column, and each diagonal (including all diagonals parallel to the two main diagonals) contains at most one checker.
    
    ```plain
    0   1   2   3   4   5   6
      -------------------------
    1 |   | O |   |   |   |   |
      -------------------------
    2 |   |   |   | O |   |   |
      -------------------------
    3 |   |   |   |   |   | O |
      -------------------------
    4 | O |   |   |   |   |   |
      -------------------------
    5 |   |   | O |   |   |   |
      -------------------------
    6 |   |   |   |   | O |   |
      -------------------------
    ```
    
    The layout above can be described by the sequence $\{2,4,6,1,3,5\}$: the $i$-th number means that in row $i$ there is a checker in column $a_i$, as shown below.
    
    Row $i$: $\{1,2,3,4,5,6\}$
    
    Column $a_i$: $\{2,4,6,1,3,5\}$
    
    This is just one way of placing the checkers. Write a program that finds all placements and outputs them with the sequence notation above, in lexicographic order. You only need to output the first $3$ solutions and, on the last line, the total number of solutions. Pay special attention: you need to optimize your program so that it stays efficient for larger board sizes.

??? note "Sample code"
    ```cpp
    --8<-- "docs/search/code/backtracking/backtracking_1.cpp"
    ```

???+ example "[Maze](https://www.luogu.com.cn/problem/P1605)"
    There is a maze of size $N \times M$ with $T$ obstacles; obstacle cells cannot be passed. Given the coordinates of the start and of the target, and given that each cell may be visited at most once, how many ways are there to get from the start to the target? In the maze one moves in four ways: up, down, left, and right, one cell at a time. It is guaranteed that there is no obstacle on the start cell.

??? note "Sample code"
    ```cpp
    --8<-- "docs/search/code/backtracking/backtracking_2.cpp"
    ```
