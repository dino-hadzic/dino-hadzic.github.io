---
title: Iterative deepening
---

## Definition

Iterative deepening is a depth-first search that **limits the search depth each time**.

## Explanation

Iterative deepening search is still essentially depth-first search, except that it carries a depth $d$ along with the search: when $d$ reaches the set depth, it returns. It is generally used to find an optimal solution. If one search does not find a valid solution, the set depth is increased by one and the search restarts from the root.

Since the goal is to find an optimal solution, why not use BFS? We know that BFS is based on a queue, whose space complexity is large; when there are many states or a single state is large, BFS with a queue shows its disadvantage. In fact, iterative deepening is like a BFS implemented in the DFS manner, and its space complexity is relatively small.

When the search tree has many branches, the search complexity grows exponentially with each additional level, so the complexity of the repeated earlier parts is almost negligible; this is why iterative deepening can be regarded approximately as BFS.

## Procedure

First set a small depth as a global variable and run DFS. Each time we enter DFS, increase the current depth by one, and return when $d$ exceeds the set depth $\textit{limit}$. If the answer is found during the search, we can backtrack and record the path while backtracking. If the answer is not found, return to the function entry, increase the set depth, and continue searching.

???+ note "Implementation (pseudocode)"
    ```text
    IDDFS(u,d)
        if d>limit
            return
        else
            for each edge (u,v)
                IDDFS(v,d+1)
    return
    ```

## Notes

In most problems breadth-first search is still more convenient, and duplicates are easy to detect. When you find that breadth-first search is not good enough in terms of space and the problem asks for an optimal solution, you should consider iterative deepening.
