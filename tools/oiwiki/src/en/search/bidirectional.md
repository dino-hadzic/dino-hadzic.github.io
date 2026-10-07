---
title: Bidirectional search
---

This page briefly introduces two bidirectional search algorithms: "simultaneous bidirectional search" and "meet in the middle".

## Simultaneous bidirectional search

### Definition

The basic idea of simultaneous bidirectional search is to run [BFS](./bfs.md) or [DFS](./dfs.md) from both the start and the target of the state graph at the same time.

If the two ends of the search meet, we can consider that a feasible solution has been found.

### Procedure

Steps of bidirectional BFS:

```text
push the start node and the target node into the queue q
mark the start node with 1
mark the target node with 2
while (queue q is not empty)
{
  expand s new nodes from q.front()
  
  if a newly expanded node has already been marked with the other number
    then the two ends of the search have collided
    then the loop ends
  
  if the s new nodes were expanded from the start node
    then mark these s nodes with 1 and push them into q 
  
  if the s new nodes were expanded from the target node
    then mark these s nodes with 2 and push them into q
}
```

### Worked example

???+ note "Example [Eight Puzzle](https://www.luogu.com.cn/problem/P1379)"
    On a $3\times 3$ board there are eight tiles, each labeled with one of the numbers $1$ to $8$. One cell of the board is empty, and the empty cell is denoted by $0$. A tile adjacent to the empty cell can be moved into it. The task is: given an initial layout (initial state) and a target layout (to keep the problem simple, let the target state be $123804765$), find a sequence of moves with the minimum number of steps that transforms the initial layout into the target layout.

??? note "Solution idea"
    A brute-force BFS is easy to come up with, and in this problem it does not even exceed the time limit. Here, however, we use it as an example of simultaneous bidirectional search. We can run two BFSs, one forward from the initial state and one backward from the target state, alternating between them; the size of the search tree shrinks considerably. When one BFS reaches a state already found by the other BFS, we have the answer.

??? note "Sample code"
    ```cpp
    --8<-- "docs/search/code/bidirectional/bidirectional_1.cpp"
    ```

## Meet in the middle

???+ warning "Warning"
    This section is not about [**binary search**](../basic/binary.md) (in Chinese, binary search is sometimes also called "halving search").

### Introduction

The meet in the middle algorithm has no official Chinese name; common translations are "halving search", "bidirectional search" or "meeting halfway".

It is suitable when the input is small, but not small enough to apply brute-force search directly.

### Procedure

The main idea of meet in the middle is to split the whole search into two halves, search each half separately, and finally merge the results of the two halves.

### Properties

The complexity of brute-force search is often exponential, and switching to meet in the middle can halve the exponent, i.e. reduce the complexity from $O(a^b)$ to $O(a^{b/2})$.

### Worked example

???+ note "Example ["USACO09NOV" Lights](https://www.luogu.com.cn/problem/P2962)"
    There are $n$ lights, each connected to several other lights, and each light has a switch. Pressing the switch of a light toggles that light and all lights connected to it. Initially all lights are off, and you need to turn all of them on. Find the minimum number of switch presses.
    
    $1\le n\le 35$.

??? note "Solution idea"
    If we searched the on/off states with brute-force DFS, the time complexity would be $O(2^{n})$, which clearly exceeds the time limit. With meet in the middle, however, the time complexity can be reduced to $O(n2^{n/2})$. Meet in the middle means we first search half of the states, i.e. find the states reachable using only switches numbered $1$ to $\mathrm{mid}$, and then find the states reachable using only the other half of the switches. If the lights turned on in the first half and in the second half are complementary, merging the two halves gives a way to turn on all the lights. In the implementation, the states of the first half and the minimum number of presses for each of them are stored in a map; while searching the second half, each way found is merged with the complementary way from the first half to update the answer.

??? note "Sample code"
    ```cpp
    --8<-- "docs/search/code/bidirectional/bidirectional_2.cpp"
    ```

## External links

-   [What is meet in the middle algorithm w.r.t. competitive programming? - Quora](https://www.quora.com/What-is-meet-in-the-middle-algorithm-w-r-t-competitive-programming)
-   [Meet in the Middle Algorithm - YouTube](https://www.youtube.com/watch?v=57SUNQL4JFA)
