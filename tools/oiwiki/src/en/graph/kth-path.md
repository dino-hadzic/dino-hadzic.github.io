---
title: k-th shortest path
---

Prerequisites: [Dijkstra's algorithm](./shortest-path.md#dijkstras-algorithm), [A\* algorithm](../search/astar.md), [persistent mergeable heap](../ds/persistent-heap.md)

## Problem statement

Given a directed graph with $n$ vertices and $m$ edges, find the length of the $k$-th shortest among all distinct paths from $s$ to $t$.

???+ info "“Path”"
    A "path" in this article may pass through the same edge or the same vertex several times, so strictly speaking the correct term is "[walk](./concept.md#paths)" rather than "path". Strictly speaking, the problem discussed here is the **$k$ shortest walk** problem. However, following convention, this article still uses the term "path", and calls a path that does not intersect itself a "simple path".

## A\* algorithm

A\* is a search algorithm. It assigns to every current state $x$ an evaluation function $f(x)=g(x)+h(x)$, where $g(x)$ is the actual cost of reaching the current state from the initial state and $h(x)$ is the estimated cost of the best path from the current state to the goal state. During the search, each time the state $x$ with the best $f(x)$ is taken out and all of its successor states are expanded. A **priority queue** can be used to maintain this value.

When solving the $k$-th shortest path problem, let $h(x)$ be the length of the shortest path from the current vertex to the target vertex $t$. This value can be precomputed for every vertex by running a single-source shortest path from vertex $t$ on the reversed graph. For every state we record two values: the current vertex $x$ and the distance $g(x)$ traveled so far; denote such a state by $(x,g(x))$. Initially, push the initial state $(s,0)$ into the priority queue. Each time, take out the state with the smallest evaluation $f(x)=g(x)+h(x)$, enumerate all outgoing edges of the vertex $x$ of that state, and push the corresponding successor states into the priority queue. When some vertex is popped for the $k$-th time, the $g(x)$ of the corresponding state is the length of the $k$-th shortest path from the starting vertex $s$ to that vertex.

This search process can be optimized. Since we only need the $k$-th shortest path from the starting vertex to the target vertex, once a vertex has been popped $k$ times, the states of that vertex popped later do not need to have their successor states expanded. These states do not affect the final answer, because the previous $k$ pops of that vertex have already produced $k$ valid paths to it, which suffice to construct the first $k$ shortest paths to the target vertex.

Since every vertex is expanded at most $k$ times, every edge is pushed into the priority queue at most $k$ times, so the time complexity of the algorithm is $O(km\log km)$ and the space complexity is $O(km)$. Compared with a direct search, A\* prunes with respect to the target vertex $t$, but this only improves the constant, not the asymptotic complexity. Although the complexity of the algorithm in this section is not great, within the same complexity it finds the first $k$ shortest paths from the starting vertex $s$ to every vertex (in the shortest path tree rooted at $t$).

### Implementation

??? example "Reference implementation for the template problem [Library Checker - K-Shortest Walk](https://judge.yosupo.jp/problem/k_shortest_walk)"
    ```cpp
    --8<-- "docs/graph/code/k-shortest-walk/k-shortest-walk-1.cpp"
    ```

## Persistent mergeable heap approach

The algorithm above actually finds the $k$ shortest paths to all vertices. If we only want the $k$ shortest paths to a given target vertex $t$, we can do better. This section gives an $O(m\log m+k\log k)$ approach based on a persistent mergeable heap.

### Shortest path tree and sidetracks

The bottleneck of the previous algorithm is that the answer is only updated when the target vertex $t$ is reached. However, different paths may differ very little. For instance, the second shortest path may differ from the shortest one only by detouring around one extra vertex at a single edge, while the rest of the path is identical; yet the previous algorithm may have to search these identical edges all over again to find the second shortest path. Since only the detouring part matters, to obtain the first $k$ shortest paths it suffices to consider the $k$ cheapest ways of detouring. This leads to the concept of the shortest path tree.

Run a single-source shortest path from the target vertex $t$ on the reversed graph, record the shortest distance $h(x)$ from every vertex $x$ to $t$, and record the first edge $f_x$ of the shortest path starting at vertex $x$; if there are several optimal choices, take the one recorded by Dijkstra's algorithm during relaxation. All these edges $f_x$ and their endpoints form a tree, and the simple path from every vertex $x$ of the tree to the root $t$ is a shortest path from $x$ to $t$. This is the **shortest path tree** $T$.

Once the shortest path tree $T$ is known, we can compute how much of a detour every edge not in $T$ causes. For an edge $e=(u,v)\notin T$ with weight $w$, define a new edge, still from $u$ to $v$, with cost $\Delta(e)=w + h(v) - h(u)$. This article vividly calls these edges with weights $\Delta(e)$ **sidetracks**, and the weight $\Delta(e)$ the sidetrack cost. Since $h(u)\le w+h(v)$, the sidetrack cost is always non-negative. If not both endpoints of an edge lie in the shortest path tree $T$, the edge does not affect the computation of the $k$-th shortest path to vertex $t$ and can simply be deleted.

In the figure below, the left side is the directed graph $G$, and the right side is its shortest path tree $T$ (thick edges) together with the corresponding sidetracks (thin edges):

![](./images/k-shortest-path-1.svg)

Let $P$ be the sequence of edges traversed by a path from $s$ to $t$, and let $P'$ be obtained by removing from $P$ the edges that belong to $T$. Then, listing the edges of $P'$ in order, any two adjacent edges $e_1=(u_1,v_1)$ and $e_2=(u_2,v_2)$ must satisfy

-   Condition $(*)$: the tail $u_2$ of the latter is an ancestor (including itself) of the head $v_1$ of the former in the shortest path tree $T$. For the first edge, by convention "the head of the former" is $s$.

This is because in the corresponding original path $P$, $v_1$ and $u_2$ are connected by some tree edges of $T$. Conversely, for an edge sequence $P'$ satisfying condition $(*)$, there is exactly one path $P$ in the graph $G$ corresponding to it, since the simple path between $v_1$ and $u_2$ in the shortest path tree $T$ is unique. This shows that the paths $P$ in the original graph are in one-to-one correspondence with the sidetrack sequences $P'$ satisfying condition $(*)$. Moreover, the length of the path $P$ equals the shortest path length $h(s)$ plus the sum of these sidetrack costs:

$$
h(s)+\sum_{e\in P'}\Delta(e).
$$

This discussion shows that the task of finding the $k$-th shortest path turns into the task of finding the sidetrack sequence $P'$ with the $k$-th smallest cost satisfying condition $(*)$.

To handle condition $(*)$, rather than searching for ancestors in the shortest path tree at every query, it is better to directly push down the sidetrack set of every vertex to its descendants in the shortest path tree. This amounts to building the following graph $G'$:

![](./images/k-shortest-path-2.svg)

In this graph, condition $(*)$ becomes the requirement that the edges of $P'$ be joined head to tail, i.e. that $P'$ is a path in the graph $G'$. The problem further turns into finding the path of $k$-th smallest length starting from $s$ **to any vertex** in this graph. Unlike the original $k$-th shortest path problem, the path is no longer required to end at the target vertex $t$.

The transformed problem is easy to solve. Start directly from the starting vertex $s$ and expand with a priority queue in increasing order of path length (the same vertex may be popped several times). Every time a vertex is popped from the priority queue, we have found a path in $G'$, which corresponds to a path to the target vertex $t$ in $G$.

### Persistent mergeable heap optimization

The idea of the algorithm is now clear. However, a naive implementation has too high a complexity. Since in the graph $G'$ the number of edges at a single vertex may be $\Theta(m)$, every time a vertex is expanded we may have to push an edge set of size $\Theta(m)$ into the priority queue. In fact, there is no need to push all edges into the priority queue: in many cases, among the pushed edges only the shortest ones may be popped later. In other words, the whole edge set at a vertex can be pushed into the priority queue as a single storage unit; all we need is fast access to the shortest edge in the set.

This suggests storing the edge set at a vertex in a min-heap. The priority queue then only stores these heaps, whose cost is the path cost corresponding to the edge at the top of the heap. Whenever the front of the queue is popped, the top edge of the heap at the front is popped from that heap as well. Then the heap with its top removed is pushed back into the priority queue, and the heap of the sidetrack set at the head of the popped edge is pushed into the priority queue too.

Storing the edge sets in heaps also solves the problem of pushing the edge sets down the shortest path tree. Pushing the edge set down amounts to merging the edge set of the current vertex into its child, so the heap must support merging; and merging into the child must not destroy the edge set at the current vertex, so the heap must also be persistent. This is exactly the persistent mergeable heap.

Thus we obtain the complete algorithm:

1.  Starting from the target vertex $t$, run a single-source shortest path and compute the shortest path tree.
2.  For every vertex of the shortest path tree, build the corresponding sidetrack set and store it in a persistent mergeable heap.
3.  Along the edges of the shortest path tree, from the target vertex $t$ top-down (e.g. in BFS order), merge the heap at every vertex into the heap of its child.
4.  Record the shortest path length $h(s)$ as the first answer, then starting from the starting vertex $s$ push the heap at $s$ into the priority queue.
5.  Pop the heap at the front of the queue, record the answer, push the heap with its top removed back into the priority queue, and push the heap at the head of the top edge into the priority queue.

The persistent mergeable heap is usually implemented with a leftist tree or a randomized heap. In that case the last step can be optimized further. The internal structure of these heaps is a binary tree. After popping the top of the heap, one would originally merge the left and right children and push the top of the merged heap into the priority queue; but in this algorithm the merge can be skipped and the heaps of the two children pushed into the priority queue separately. This saves the $O(\log m)$ cost of a single merge. Since after popping a heap from the front at most three new heaps are pushed into the priority queue, the size of the priority queue is $O(k)$. Thus the time complexity of a single query drops to $O(\log k)$, and the total query complexity is $O(k\log k)$.

Since building the shortest path tree and building the persistent mergeable heap both cost $O(m\log m)$, the total time complexity of the algorithm is $O(m\log m+k\log k)$.

### Implementation

??? example "Reference implementation for the template problem [Library Checker - K-Shortest Walk](https://judge.yosupo.jp/problem/k_shortest_walk)"
    ```cpp
    --8<-- "docs/graph/code/k-shortest-walk/k-shortest-walk-2.cpp"
    ```

## Exercises

-   ["SDOI2010" 魔法猪学院](https://www.luogu.com.cn/problem/P2483)

## References and notes

-   [\[Tutorial\] k shortest paths and Eppstein's algorithm by meooow - Codeforces](https://codeforces.com/blog/entry/102085)
