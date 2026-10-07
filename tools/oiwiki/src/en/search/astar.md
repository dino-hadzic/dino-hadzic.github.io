---
title: A*
---

This page introduces the A\* search algorithm.

The A\* search algorithm (A\* is read "A-star"), A\* algorithm for short, is an algorithm for finding the shortest path between a given start and target in a weighted directed graph. It belongs to graph traversal and best-first search algorithms, and it is also an improvement of [BFS](./bfs.md).

## Procedure

The goal of the A\* algorithm is to find the shortest path from the start $s$ to the target $t$ in a directed graph. Let $d(x,y)$ be the distance between nodes $x$ and $y$, i.e. the length of the shortest path between them. Denote by $g(x)=d(s,x)$ the distance function from the start $s$ to node $x$, by $h^*(x)$ the distance function from node $x$ to the target $t$, and by $h(x)$ an estimate of $h^*(x)$[^note1]. Finally, denote the estimate of the length of the shortest path from $s$ through $x$ to $t$ by

$$
f(x) = g(x) + h(x).
$$

During the search, the A\* algorithm each time pops the node with the smallest $f$ from a priority queue. Then it pushes all its successors $x$ into the priority queue and updates $f(x)$ using the actually recorded $g(x)$ and the estimated $h(x)$.

## Properties

Since the actual value of $h^*(x)$ is unknown during the search, an easily computable $h(x)$ is used as its estimate. The actual complexity of A\* search depends on the properties of this estimate function $h(x)$. It is easy to imagine that if $h\equiv h^*$, i.e. the estimate is exact, the search proceeds strictly along the shortest path. If instead $h\equiv 0$, the A\* algorithm degenerates into [Dijkstra's algorithm](./../graph/shortest-path.md#dijkstra-算法); when $h\equiv 0$ and all edge weights are $1$, it is exactly [BFS](./bfs.md).

Suppose the graph has no negative-weight edges. If the estimate $h(x)$ never exceeds the actual distance $h^*(x)$, i.e. $0\le h\le h^*$, then the A\* algorithm is guaranteed to find the optimal solution. An estimate function $h(x)$ satisfying this condition is called **admissible**. By the discussion above, the closer $h$ is to $h^*$, the more efficient the corresponding A\* algorithm is. In general, in the worst case the algorithm visits all nodes satisfying

$$
f(x) = g(x) + h(x) \le C^*
$$

where $C^*$ is the shortest distance between the start $s$ and the target $t$. Intuitively, the closer $h$ is to $h^*$, the fewer successors satisfy this condition at each expansion, and therefore the fewer branches the algorithm explores. So the A\* algorithm can be seen as a "pruning" optimization of search.

If $h$ is not only admissible but also **consistent**, i.e.

$$
h(x) \le h(y) + d(x, y),
$$

then the A\* algorithm never re-inserts into the queue a node that has already been popped. The consistency condition can be understood as the triangle inequality among the nodes $x,y,t$.

## Worked example

A classic application of the A\* algorithm is the k shortest paths problem. For the description of that problem, the A\* approach, and the approach with better complexity using persistent mergeable heaps, see the page [k-th shortest path](./../graph/kth-path.md).

This section introduces a classic problem that can be solved with the A\* algorithm.

???+ example "[Eight Puzzle](https://www.luogu.com.cn/problem/P1379)"
    On a $3\times 3$ board there are eight tiles, each labeled with one of the numbers $1$ to $8$. One cell of the board is empty, and the empty cell is denoted by $0$. A tile adjacent to the empty cell can be moved into it, and its original position then becomes empty. Given an initial layout and a target layout (to keep the problem simple, let the target state be as below), find a sequence of moves with the minimum number of steps from the initial layout to the target layout.
    
    $$
    \begin{aligned}
    123\\
    804\\
    765
    \end{aligned}
    $$

??? note "Solution idea"
    The function $h$ can be defined as the number of tiles that are not in their correct position. It is easy to see that $h$ is both admissible and consistent, so the problem can be solved with the A\* algorithm.

??? note "Sample code"
    ```cpp
    --8<-- "docs/search/code/astar/astar_1.cpp"
    ```

## References and notes

-   [A\* search algorithm - Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)

[^note1]: Here $h$ stands for "heuristic". See [Heuristic (computer science) - Wikipedia](https://en.wikipedia.org/wiki/Heuristic_(computer_science)) and the "Bounded relaxation" section of [A\* search algorithm - Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm#Bounded_relaxation).
