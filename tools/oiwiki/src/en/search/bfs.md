---
title: BFS (search)
---

## Introduction

BFS (breadth-first search) is a basic algorithm of graph theory; see the page [BFS (graph theory)](../graph/bfs.md). In **search algorithms** the term usually refers to a search that uses a queue to expand states level by level; the idea is the same as the graph-theoretic BFS, and it is particularly suited to **shortest path** or **minimum number of steps** problems.

## Explanation

The core idea of BFS is **expansion by levels**: starting from the source, the reachable positions are scanned level by level. The path length at the first encounter with the target is exactly the shortest path length. This guarantees the layered structure and the optimality of the search.

In practice, BFS starts from the source and first visits all nodes directly reachable from it; these nodes form the first level of the search. Then these nodes become the new starting points and their neighbors are visited in turn, forming the second level; and so on, expanding outward until the target node is found or all reachable nodes have been visited. During this process the algorithm uses a queue and a visited array: the newly discovered nodes of each level (those not yet recorded in the visited array) are enqueued in order, which ensures that the nodes of the same level are processed in visiting order, strictly following the logic of "expansion by levels".

BFS is very good at quickly finding a **shortest path** or the **minimum number of steps**. When the algorithm meets the target for the first time at some level, the path length (number of steps) traveled is necessarily the shortest. This is because the "expansion by levels" mechanism of BFS guarantees that every node is reached with the fewest steps: it is like searching along the most direct path from the source until the target is reached, without detours or extra steps. On this kind of problem BFS is usually also more efficient than DFS.

However, compared with DFS, BFS also has drawbacks. It usually needs more memory, lacks a natural backtracking process, and depth pruning is less flexible than in DFS.

## Worked example

???+ example "Example [Luogu B3625 Maze Path](https://www.luogu.com.cn/problem/B3625)"
    In an $n \times m$ maze matrix, `.` denotes a passable cell and `#` an obstacle. Starting from $(1,1)$, each move goes up, down, left or right. Can the target $(n,m)$ be reached?

??? note "Solution"
    The implementation maintains a queue of coordinates waiting to be processed, together with a visited-flag array to avoid repeated computation. When a node expands its reachable nodes, it expands up, down, left and right; these four directions are $(x, y + 1)$, $(x, y - 1)$, $(x + 1, y)$ and $(x - 1, y)$, and the code uses direction arrays. Be careful not to expand into a cell containing an obstacle.

??? note "Sample code"
    ```cpp
    --8<-- "docs/search/code/bfs/bfs-1.cpp"
    ```

???+ example "Example [Luogu P1135 Strange Elevator](https://www.luogu.com.cn/problem/P1135)"
    There are $n$ floors and one elevator. When the elevator is on floor $i$, it moves up or down by exactly $k_i$ floors. If the destination floor is invalid, i.e. not between $1$ and $n$, that operation cannot be performed. Question: how many elevator operations are needed at least to get from floor $a$ to floor $b$? If it is impossible, print $-1$.

??? note "Solution"
    This problem asks for a shortest path, which is exactly what BFS is good at. In the implementation, the queue stores both the floor to be processed and the shortest distance from the start $a$ to that floor, together with a visited-flag array to avoid inserting the same element twice. When a node $i$ expands its reachable nodes, it expands to $i + k_i$ and $i - k_i$, taking care not to reach an invalid floor. When we expand to a valid floor not yet reached, we enqueue it and record its shortest distance as the shortest distance to the current floor plus one. When node $b$ is reached for the first time, the recorded shortest distance is the final answer.
    
    The code stores the distance array directly and uses whether the distance is still the default value (i.e. $-1$) to tell whether a node has not been visited yet.

??? note "Sample code"
    ```cpp
    --8<-- "docs/search/code/bfs/bfs-2.cpp"
    ```

## Exercises

-   [Luogu P1443 Knight's Tour](https://www.luogu.com.cn/problem/P1443)
-   [Luogu P3956 \[NOIP 2017 Junior\] Chessboard](https://www.luogu.com.cn/problem/P3956)
-   [Luogu P1126 Robot Moving Heavy Objects](https://www.luogu.com.cn/problem/P1126)
