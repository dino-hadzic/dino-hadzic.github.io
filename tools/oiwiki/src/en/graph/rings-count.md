---
title: Counting cycles
---

## Counting general cycles

???+ note "[Example 1: Codeforces Beta Round 11 D. A Simple Task](https://codeforces.com/problemset/problem/11/D)"
    Given a simple graph, find the number of simple cycles in it. A simple cycle is a cycle with no repeated vertices or edges.
    
    Number of vertices $1\leq n\leq 19$.

??? note "Solution idea"
    Use bitmask DP (state-compression DP). Let $f(s,i)$ be the number of paths whose set of visited vertices is $s$, which are currently at vertex $i$, and whose first vertex is **the vertex with the smallest index** in the set $s$.
    
    For a state $f(s,i)$, enumerate the next vertex $u$. If $u$ is in the set $s$ and is the one with the smallest index (i.e. the starting vertex), add $f(s,i)$ to the answer $A$. If $u$ is not in $s$, add $f(s,i)$ to $f(s\cup\{u\},u)$.
    
    This also counts cycles of length two (i.e. edges), and every cycle of length greater than two is counted twice (because from a fixed starting vertex one can go in two directions), so the answer is $\dfrac{A-m}2$, where $m$ is the number of edges. The time complexity is $O(2^nm)$.

??? note "Sample code"
    ```cpp
    --8<-- "docs/graph/code/rings-count/rings-count_1.cpp"
    ```

## Counting triangles

A **triangle** (cycle of length three) in a simple graph $G$ is an unordered triple $(u,\ v,\ w)$ such that there are three edges connecting $(u,\ v)$, $(v,\ w)$ and $(w,\ u)$. The **triangle counting problem** asks for the number of all triangles in the graph.

First orient all edges. We direct each edge from the vertex of smaller degree to the vertex of larger degree, and for equal degrees from the vertex of smaller index to the vertex of larger index. The graph then becomes a directed acyclic graph (DAG).

??? note "Proof that the graph has no cycles"
    Suppose, for contradiction, that there is a cycle. Then the degrees of the vertices along the cycle keep increasing, so to close the cycle all degrees would have to be equal; but the indices are necessarily different – a contradiction.
    
    Hence after orientation the graph certainly has no cycles.
    
    In fact, the orientation rule above defines a [partial order](../math/order-theory.md#二元关系), so the graph built by this rule (i.e. the [Hasse diagram](../math/order-theory.md#偏序集的可视化表示hasse-图) of that partial order) is necessarily a DAG.

Enumerate $u$ and the vertices $v$ that $u$ points to, then enumerate $w$ among the vertices $v$ points to, and check whether $u$ is connected to $w$.

The time complexity of this algorithm is $O(m\sqrt m)$.

???+ note "Proof of the time complexity"
    The orientation step visits all edges, with complexity $O(n+m)$.
    
    For each pair $(v,\ w)$, the number of possible $u$ does not exceed the in-degree $d^-(v)$ of $v$.
    
    If $d^-(v)\leq\sqrt m$, since there are at most $n$ vertices $w$, this part has complexity $O(n\sqrt m)$.
    
    If $d^-(v) > \sqrt m$, since $v$ points to $w$ we have $d(v) \leq d(w)$, hence $d(w) > \sqrt m$; but there are only $m$ edges in total, so there are at most $\sqrt m$ such $w$ and the complexity is $O(m\sqrt m)$.
    
    The total time complexity is $O(n+m+n\sqrt m+m\sqrt m)=O(m\sqrt m)$.
    
    In fact, if during orientation the edges are directed from the vertex of larger degree to the vertex of smaller degree, the complexity is still correct: just swap the roles of $u,\ w$ and the proof above still holds.

???+ note "Sample code ([Luogu P1989 Counting triangles in an undirected graph](https://www.luogu.com.cn/problem/P1989))"
    ```cpp
    --8<-- "docs/graph/code/rings-count/rings-count_2.cpp"
    ```

### Example 2

???+ note "[HDU 6184 Counting Stars](https://acm.hdu.edu.cn/showproblem.php?pid=6184)"
    Given an undirected graph with $n$ vertices and $m$ edges, find the number of occurrences of the following shape.
    
    ![](./images/rings-count1.svg)
    
    $2\leq n\leq 10^5$, $1\leq m\leq\min\left\{2\times 10^5,\ \dfrac{n(n-1)}2\right\}$.

??? note "Solution idea"
    This shape is formed by two triangles sharing one edge. So we first run triangle counting and, for every edge, count the triangles containing it; then enumerate the shared edge – if $x$ triangles contain this edge, its contribution to the answer is $\dbinom x2$.
    
    The time complexity is $O(m\sqrt m)$.

??? note "Sample code"
    ```cpp
    --8<-- "docs/graph/code/rings-count/rings-count_3.cpp"
    ```

## Counting 4-cycles

Similarly, a **4-cycle** consists of four vertices $a,\ b,\ c,\ d$ such that $(a,\ b)$, $(b,\ c)$, $(c,\ d)$ and $(d,\ a)$ are all connected by edges.

First sort the vertices: vertices of smaller degree come first, vertices of larger degree come last.

Enumerate the vertex $a$ that is last in the order; then for every vertex $c$ ranked before $a$ we need the number of vertices $b$ ranked before $a$ such that both $(a,\ b)$ and $(b,\ c)$ are edges. Then any two of these $b$ form a 4-cycle. To count the $b$'s it suffices to iterate over $b$ and $c$ once.

Note that the complexity of our enumeration is essentially equivalent to enumerating triangles, so the time complexity is also $O(m\sqrt m)$ (assuming $n,\ m$ are of the same order).

It is worth noting that $(a,\ b,\ c,\ d)$ and $(a,\ c,\ b,\ d)$ can be two different 4-cycles.

Also, vertices with equal degree will have different ranks, and one must remember to check $a\neq c$.

???+ note "Sample code ([LibreOJ P191 Counting 4-cycles in an undirected graph](https://loj.ac/p/191))"
    ```cpp
    --8<-- "docs/graph/code/rings-count/rings-count_4.cpp"
    ```

### Example 3

???+ note "[Gym 102028L Connected Subgraphs](https://codeforces.com/gym/102028/problem/L)"
    Given an undirected graph with $n$ vertices and $m$ edges, find the number of ways to choose four edges whose induced subgraph is connected.
    
    $4\leq n\leq 10^5$, $4\leq m\leq 2\times 10^5$.

??? note "Solution idea"
    It is easy to split the cases into five kinds: a star, a 4-cycle, a triangle with one extra edge hanging off a vertex, a chain of four vertices with an extra edge hanging off a middle vertex, and a chain of five vertices.
    
    Stars are counted directly from the vertex degrees using binomial coefficients. 4-cycles are obtained directly by the algorithm above. For the triangle part, just enumerate the triangles $(u,\ v,\ w)$; the contribution to the answer is $[d(u)-2]+[d(v)-2]+[d(w)-2]$.
    
    Now consider the fourth case. Enumerate a vertex $x$ of degree $2$, then enumerate a neighbor $y$ of it as the vertex of degree $3$. The contribution to the answer is $[d(x)-1]\cdot\dbinom{d(y)-1}2$. However, note that a neighbor of $y$ may coincide with a neighbor of $x$, in which case the shape is equivalent to the third case. Each such over-counted third case is counted twice (because there are two vertices of degree $3$), so twice the number of third cases should be subtracted.
    
    For the last case, first enumerate the middle vertex $x$; it is easy to see that the contribution to the answer is
    
    $$
    \sum_{y\in son_x}\sum_{z\in son_x}[d(y)-1]\cdot[d(z)-1].
    $$
    
    Again there is over-counting here. Let $s$ be a neighbor of $y$ and $t$ a neighbor of $z$; after some thought, the over-counted configurations are:
    
    1.  $y$ coincides with $t$ but $s$ does not coincide with $z$ – equivalent to the third case;
    2.  $s$ coincides with $z$ but $y$ does not coincide with $t$ – also equivalent to the third case;
    3.  both $y$ with $t$ and $s$ with $z$ coincide – equivalent to a triangle;
    4.  $s$ coincides with $t$ – equivalent to a 4-cycle (the second case).
    
    Since the two vertices of degree $2$ in the third case, taken as $x$, correspond exactly to over-counts 1 and 2, twice the number of third cases must additionally be subtracted. For a triangle, all three vertices can serve as $x$, so it is over-counted $3$ times. Likewise, a 4-cycle is over-counted $4$ times.
    
    Thus we obtain an algorithm for all cases, with time complexity $O(n+m\sqrt m)$.

??? note "Sample code"
    ```cpp
    --8<-- "docs/graph/code/rings-count/rings-count_5.cpp"
    ```

## Exercises

[Luogu P3547 \[POI2013\] CEN-Price List](https://www.luogu.com.cn/problem/P3547)

[CodeForces 985G Team Players](https://codeforces.com/contest/985/problem/G) (inclusion–exclusion principle)
