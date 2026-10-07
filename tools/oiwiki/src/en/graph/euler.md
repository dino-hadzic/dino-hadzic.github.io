---
title: Eulerian graphs
---

This page briefly introduces the concept of Eulerian graphs, their implementation and applications.

## Definition

Only finite graphs are discussed in this article.

In graph theory, an **Eulerian path** is a path that traverses every edge of the graph exactly once, and an **Eulerian circuit** is a closed path that traverses every edge of the graph exactly once.
If a graph has an Eulerian circuit, it is called an **Eulerian graph**; if a graph has no Eulerian circuit but has an Eulerian path, it is called a **semi-Eulerian graph**.

??? warning "Warning"
    Although the word "path" is used in this definition, strictly speaking the concept used here is a "trail". An Eulerian path or circuit may use every edge exactly once, but places no restriction on how often vertices are visited.

## Properties

Below we assume that the graph $G$ under discussion has no isolated vertices. This assumption loses no generality, because for a graph $G$ with isolated vertices the following properties still hold for the graph $G'$ obtained from $G$ by deleting the isolated vertices.

For a connected graph $G$, the following three properties are equivalent:

1.  $G$ is an Eulerian graph;
2.  every vertex of $G$ has even degree (for directed graphs, the in-degree of every vertex equals its out-degree);
3.  $G$ can be decomposed into a union of several edge-disjoint circuits.

We now prove the equivalence.

If a graph $G$ is Eulerian, then every vertex of $G$ has even degree: start at any vertex and walk once around the Eulerian circuit; the degree of every vertex $v$ equals the number of departures from $v$ plus the number of arrivals at $v$. Since the trajectory is a closed walk, for every vertex $v$ the number of departures equals the number of arrivals. That is, every vertex has degree of the form $2k$, i.e. even.
In particular, for directed graphs the same argument shows that the in-degree of every vertex equals its out-degree.

If every vertex of a graph $G$ has even degree (or equal in- and out-degree), then it can be decomposed into a disjoint union of several edge-disjoint circuits: start at any vertex $u$, choose any outgoing edge $(u, v)$, move to the adjacent vertex $v$ and delete $(u, v)$, and continue until returning to the starting vertex $u$. One can prove that this process must eventually return to $u$: whenever we arrive at a new vertex $v \neq u$, by the previous property its remaining degree is odd, so there must be an outgoing edge and the process does not stop at $v$. (In other words, the process stops if and only if we return to $u$.) Since the number of edges in $G$ is finite, the process must stop after finitely many steps, so we must eventually return to $u$ and obtain a circuit. Note that in this argument we only used the fact that all degrees are even, and after finding and deleting one circuit the remaining graph still has this property, so we can repeat the process until the remaining graph is empty, thereby splitting $G$ into several edge-disjoint circuits.
Furthermore, every circuit can be split, at the vertices it passes through more than once, into a disjoint union of simple cycles, so the circuits in the property above may be replaced by simple cycles.

If a connected graph $G$ can be decomposed into a disjoint union of several edge-disjoint circuits, then $G$ is Eulerian: from a set of edge-disjoint circuits, repeatedly pick two that share a vertex and merge them into one, until no two circuits share a vertex.
One can prove that exactly one circuit remains at the end of this process. For any two edge-disjoint circuits $P_1, P_2$: if $P_1$ and $P_2$ share a vertex, merge them directly there; otherwise take any vertex $v_1$ on $P_1$ and $v_2$ on $P_2$; by the connectivity of $G$ there is a path $e_1, e_2, \ldots, e_k$ joining $v_1$ and $v_2$, each of whose edges $e_i$ is contained in some circuit $C_i$, where $P_1$ and $C_1$, $C_i$ and $C_{i+1}$, and $C_k$ and $P_2$ all share vertices (or $C_i = C_{i+1}$, which does not affect the proof). In this case $P_1$ and $P_2$ can be merged through $C_1, \ldots, C_k$. That is, any two circuits can be merged, so the remaining circuit is unique, its edge set is the union of all the edge-disjoint circuits, namely $E(G)$, and this circuit is an Eulerian circuit of $G$, so $G$ is Eulerian.

The properties above also form the criterion for recognizing Eulerian graphs. Concretely, a graph is Eulerian if and only if its vertices of nonzero degree are mutually (strongly) connected and all vertices have even degree (or equal in- and out-degree).

Semi-Eulerian graphs have properties similar to Eulerian ones: a semi-Eulerian graph has exactly two vertices of odd degree, and these two vertices are the endpoints of the Eulerian path. Connecting these two vertices turns a semi-Eulerian graph into an Eulerian one. Deleting any edge of an Eulerian graph yields a semi-Eulerian graph.
From this we get the criterion for semi-Eulerian graphs: a graph is semi-Eulerian if and only if its vertices of nonzero degree are mutually (strongly) connected and there are exactly two vertices of odd degree. For directed graphs the second condition is: there are exactly two vertices $u, v$ with $\deg^+(u) - \deg^-(u) = 1, \deg^+(v) - \deg^-(v) = -1$, and all other vertices have equal in- and out-degree.

## Constructing an Eulerian circuit/path

Here we present the most commonly used Hierholzer algorithm, whose core idea is the third of the Eulerian graph properties above: an Eulerian graph can be decomposed into a union of several edge-disjoint circuits.
Note that the proof above already describes a complete and feasible procedure for merging edge-disjoint circuits into an Eulerian circuit, and with suitable data structures (e.g. storing cycles in a linked-list-like structure) the implementation is not hard.

Concretely, the algorithm first finds a circuit in the graph as the current circuit; then it repeatedly picks a vertex of the current circuit with nonzero remaining degree, finds a new simple circuit starting there and merges it into the current circuit, until no vertex of the current circuit has remaining degree; the current circuit is then an Eulerian circuit.

The algorithm also works for directed graphs. For a semi-Eulerian graph, take a path joining the two odd-degree vertices as the current path, then repeatedly pick a vertex of nonzero degree, find a simple circuit and merge it into the current path; in the end we obtain an Eulerian path.

### Implementation

The pseudocode of Hierholzer's algorithm is as follows:

$$
\begin{array}{ll}
1 &  \textbf{Input. } \text{The edges of the graph } e , \text{ where each element in } e \text{ is } (u, v) \\
2 &  \textbf{Output. } \text{The vertex of the Euler Road of the input graph}.\\
3 &  \textbf{Method. } \\
4 &  \textbf{Function } \text{Hierholzer } (v) \\
5 &  \qquad circle \gets \text{Find a Circle in } e \text{ Begin with } v \\
6 &  \qquad \textbf{if } circle=\varnothing \\
7 &  \qquad\qquad \textbf{return } v \\
8 &  \qquad e \gets e-circle \\
9 &  \qquad \textbf{for} \text{ each } v \in circle \\
10&  \qquad\qquad v \gets \text{Hierholzer}(v) \\
11&  \qquad \textbf{return } circle \\
12&  \textbf{Endfunction}\\
13&  \textbf{return } \text{Hierholzer}(\text{any vertex})
\end{array}
$$

### Time complexity analysis

The time complexity of Hierholzer's algorithm is $O(|E| + |V|)$.

Note that in the correctness argument above, finding a simple circuit in an Eulerian or semi-Eulerian graph (or the initial path of a semi-Eulerian graph) **requires no backtracking**: simply keep walking along the remaining edges and the desired circuit or path will be found, and **every edge is visited only once**.
To exploit this, the edges should be stored in a linked-list-like way, such as adjacency lists or a linked forward star, so that every edge can be deleted right after it is visited. If a plain adjacency matrix is used, each edge lookup costs $O(|V|)$ and the total complexity becomes $O(|V||E|)$.

???+ note "Note"
    In fact the exact complexity of this algorithm should be $O(|E|)$ rather than $O(|V| + |E|)$, because the algorithm can be implemented in a way that depends only on the edges and not on the vertices, by maintaining a global linked list of remaining edges from which the next circuit is sought.

If the lexicographically smallest Eulerian path or circuit is required, the edges must be sorted, giving time complexity $\Theta(|E|\log |E|)$ or $\Theta(|E|)$ (using counting sort or radix sort).

### Applications

Directed Eulerian graphs can be used for computer decoding.

Suppose there are $m$ letters and we want to build a disk with $m^n$ sectors, each holding one letter, such that every $n$ consecutive positions on the disk correspond to a string of length $n$. After one full rotation ($m^n$ steps) we obtain $m^n$ pairwise distinct strings of length $n$ over the $m$ letters.

![](images/euler1.svg)

Construct the following directed Eulerian graph:

Let $S = \{a_1, a_2, \cdots, a_m\}$ and construct $D=\langle V, E\rangle$ as follows:

$V = \{a_{i_1}a_{i_2}\cdots a_{i_{n-1}} |a_i \in S, 1 \leq i \leq n - 1 \}$

$E = \{a_{j_1}a_{j_2}\cdots a_{j_{n-1}}|a_j \in S, 1 \leq j \leq n\}$

The incidence between vertices and edges of $D$ is defined as follows:

the vertex $a_{i_1}a_{i_2}\cdots a_{i_{n-1}}$ has $m$ outgoing edges: $a_{i_1}a_{i_2}\cdots a_{i_{n-1}}a_r, r=1, 2, \cdots, m$;

the edge $a_{j_1}a_{j_2}\cdots a_{j_{n-1}}$ enters the vertex $a_{j_2}a_{j_3}\cdots a_{j_{n}}$.

![](images/euler2.svg)

Such a $D$ is connected and every vertex has in-degree equal to out-degree (both equal to $m$), so $D$ is a directed Eulerian graph.

Take any Eulerian circuit $C$ of $D$, take the last letter of each edge in $C$, and arrange these letters in a circle on the disk in the order in which the edges appear in $C$.

## Example problem

???+ note "[Luogu P2731 Riding the Fences](https://www.luogu.com.cn/problem/P2731)"
    Given an undirected graph with 500 vertices, find an Eulerian path or Eulerian circuit of the graph. If there are several solutions, output the smallest one.
    
    In this problem the Eulerian path or circuit does not need to pass through all vertices.
    
    The number of edges m satisfies $1\leq m \leq 1024$.

??? note "Solution idea"
    This problem is a direct application of Hierholzer's algorithm.
    
    The answer can be stored in a `std::stack<int>`, because if what we find is not a circuit, that part must go at the end.
    
    Note that the graph must not be stored as an adjacency matrix, otherwise the time complexity degrades to $\Theta(nm)$. Since the edges need to be sorted, a forward star or `std::vector` is recommended for storing the graph. The sample code uses `std::vector`.

??? note "Sample code"
    ```cpp
    --8<-- "docs/graph/code/euler/euler_1.cpp"
    ```

## Exercises

-   [SGU 101 Domino](https://codeforces.com/problemsets/acmsguru/problem/99999/101)

-   [POJ 1780 Code](http://poj.org/problem?id=1780)

-   [Luogu P1127 Word Chain](https://www.luogu.com.cn/problem/P1127)

-   [Luogu P1333 Ruirui's Sticks](https://www.luogu.com.cn/problem/P1333)

-   [Luogu P1341 Unordered Letter Pairs](https://www.luogu.com.cn/problem/P1341)

-   [Luogu P6066 \[USACO05JAN\]Watchcow S](https://www.luogu.com.cn/problem/P6066)

-   [Luogu P6628 \[Provincial Selection 2020, Paper B\] Lilac Road](https://www.luogu.com.cn/problem/P6628)

-   [Luogu P3520 \[POI 2011\] SMI-Garbage](https://www.luogu.com.cn/problem/P3520)
