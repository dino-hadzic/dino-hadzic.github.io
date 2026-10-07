---
title: Graph matching
---

## Introduction

A **matching** or **independent edge set** is a set of edges of a graph that share no common endpoints. Graph matching algorithms are commonly used in informatics competitions and can roughly be divided into two kinds: maximum matching and maximum weight matching. Since matching in [bipartite graphs](../bi-graph.md) is equivalent to a network flow problem, has nice properties and is relatively easy to handle, we first introduce both kinds of algorithms on bipartite graphs and then discuss algorithms for general graphs.

## Matchings in a graph

Let $G=(V,E)$ be an undirected graph, where $V$ is the vertex set and $E$ is the edge set. If a set of edges $M\subseteq E$ contains no self-loops and no two of its edges share a vertex, then the edge set $M$ is called a **matching** or **independent edge set** of the graph $G$. An edge $e\in E$ that appears in the matching $M$ is called a **matched edge**, otherwise an **unmatched edge**. Correspondingly, a vertex $v\in V$ that is an endpoint of a matched edge is called a **matched vertex**, otherwise an **unmatched vertex**.

The size of a matching $M$ is the number of edges it contains. For matchings in (weighted) undirected graphs, the following concepts are often considered:

-   **Maximal matching**: a matching to which no further matched edge can be added. A maximal matching is not necessarily a maximum matching.

    ![maximal matching](images/graph-match-1.svg)

-   **Maximum matching** (or maximum cardinality matching): a matching with the largest number of matched edges. There may be more than one maximum matching, but the number of edges of a maximum matching is fixed, and it cannot exceed half the number of vertices of the graph.

    ![maximum cardinality matching](images/graph-match-2.svg)

-   **Maximum weight matching**: in a weighted graph, the matching with the largest sum of edge weights.

    ![maximum weight matching](images/graph-match-3.svg)

-   **Maximum weight maximum cardinality matching**: subject to the number of matched edges being maximum, the matching with the largest sum of edge weights. That is, among all maximum matchings, the one with the largest edge weight sum.

    ![maximum weight maximum cardinality matching](images/graph-match-4.svg)

-   **Perfect matching**: a matching in which every vertex is matched. A perfect matching is always a maximum matching. A complete graph with an even number of vertices always has a perfect matching.

-   **Near-perfect matching**: a matching with exactly one unmatched vertex. This can only happen when the graph has an odd number of vertices. A near-perfect matching is also always a maximum matching. A complete graph with an odd number of vertices always has a near-perfect matching.

Graph matching problems in algorithm competitions mainly refer to the maximum matching or the maximum weight matching of a graph.

## Augmenting paths

In graph matching algorithms, the augmenting path is the core structure used to improve a matching.

### Definition

For a graph $G=(V,E)$ and a matching $M$ of it, we can define the following two kinds of (simple) paths:

-   an **alternating path** is a path in which matched and unmatched edges alternate;
-   an **augmenting path** is an alternating path that starts at an unmatched vertex and ends at an unmatched vertex.

Since an augmenting path has $1$ more unmatched edge than matched edges, the number of edges in an augmenting path is always odd. If we flip the matched and unmatched edges on an augmenting path, it remains an alternating path, and the number of matched edges increases by $1$. The process of finding an augmenting path and flipping it to increase the size of the matching is called **augmentation**. In mathematical terms, augmentation takes the symmetric difference of the matching $M$ and the augmenting path $P$, yielding the new matching $M\oplus P$.

The figure below shows how, after one augmentation, the number of matched edges grows from $2$ to $3$.

![augment-1](./images/augment-1.png)

### Berge's lemma

Berge's lemma states that improving a matching via augmenting paths is sufficient. In other words, when no augmenting path can be found, a maximum matching has been obtained.

???+ note "Berge's lemma"
    For a graph $G=(V,E)$ and a matching $M$ of it, $M$ is a maximum matching if and only if there is no augmenting path with respect to $M$.

??? note "Proof"
    We have already shown that when an augmenting path $P$ exists, the matching $M\oplus P$ is larger than $M$, so $M$ is certainly not a maximum matching.
    
    Conversely, we need to show that if there is a matching $M'$ larger than $M$, then there must be an augmenting path $P$ with respect to $M$. To this end, consider the symmetric difference $M\oplus M'$. The degrees of vertices in the graph $(V,M\oplus M')$ can only be $0$, $1$ or $2$; the connected components of such a graph must be paths, cycles or isolated vertices. Moreover, the two edges adjacent to a vertex of degree $2$ must come from different matchings, so in these cycles the number of edges from $M$ equals the number from $M'$. Since $M'$ is larger than $M$, there is at least one path with more edges from $M'$ than from $M$; call it $P$. Then both endpoints of $P$ are unmatched vertices of $M$, and $P$ is an alternating path with respect to $M$, so $P$ must be an augmenting path with respect to $M$. This completes the proof.

From this theorem we obtain the core idea for finding a maximum matching:

-   enumerate all unmatched vertices and look for augmenting paths until no augmenting path can be found.

In fact, after each augmentation there is no need to re-scan all unmatched vertices. Over the whole process of finding a maximum matching, each vertex needs to be processed only once.

??? note "Proof"
    It suffices to show that if, when the enumeration reaches vertex $v$, there is no augmenting path starting at $v$, then after any number of further augmentations there is still no augmenting path starting at $v$. This means that even though augmentation changes the matching, the previously enumerated unmatched vertices need not be checked again.
    
    Suppose otherwise. That is, suppose $v$ is an already enumerated unmatched vertex, and after augmenting along an augmenting path $P$ from $u$ to $w$ in some round, a new augmenting path $P'$ starting at $v$ appears that did not exist before. Then the path $P'$ must share an edge with $P$; otherwise augmenting along $P$ would not change the matching status of the edges in $P'$, and $P'$ would not be an augmenting path newly created by this augmentation.
    
    ![augment-2](./images/augment-2.svg)
    
    (In the figure, black denotes unmatched edges, and red and blue denote different matching states.)
    
    Let $x$ be the first vertex of $P$ reached when walking from $v$ along $P'$. Since an alternating path from $v$ to $x$ already existed before this augmentation, and at that time there was no augmenting path starting at $v$, $x$ must be a matched vertex, and hence cannot be $u$ or $w$. Therefore, on the augmenting path $P$ there are two edges adjacent to $x$, and their matching states are opposite. This means that regardless of the matching state of the edge by which the alternating path starting at $v$ reaches $x$, the alternating path can be extended along $P$ to either $u$ or $w$. Hence an augmenting path starting at $v$ already existed before the augmentation, contradicting the assumption.

### Alternating trees

Another concept closely related to augmenting paths is the alternating tree. It is the tree produced while searching for an augmenting path by DFS or BFS from an unmatched vertex $r$.

For a graph $G=(V,E)$ and a matching $M$ of it, if a subgraph $H\subseteq G$ is a tree rooted at an unmatched vertex $r$, and the path connecting $r$ to any $v\in V(H)$ is an alternating path, then $H$ is called an **alternating tree**. Vertices at even depth in the tree are called even vertices, and vertices at odd depth are called odd vertices.

The figure below shows an alternating tree that may be obtained by BFS from the unmatched vertex $1$. (In the figure, red edges are matched edges and black edges are unmatched; dark vertices are matched and light vertices are unmatched.)

![](images/alternating-tree.svg)

## Existence of perfect matchings

In matching theory there are two important existence theorems that can be used to decide whether a perfect matching exists in a bipartite or general graph.

### Hall's theorem

Suppose $G=(X,Y,E)$ is a bipartite graph with $|X|\le |Y|$. For a matching $M$ of $G$, if all vertices in $X$ are matched, $M$ is called an **$X$-perfect matching**, sometimes simply a perfect matching (of the bipartite graph $G$). This is the largest matching achievable in a bipartite graph. Hall's theorem provides a necessary and sufficient condition for the existence of such a matching.

Hall's theorem says that as long as, for every subset of $X$, there are enough vertices in $Y$ that can be matched to it, an $X$-perfect matching must exist.

???+ note "Hall's theorem"
    Suppose $G=(X,Y,E)$ is a bipartite graph with $|X|\le |Y|$. For any $W\subseteq X$, let $N_G(W)$ denote the set of all vertices of $G$ adjacent to a vertex in $W$. Then an $X$-perfect matching exists if and only if $|W|\le |N_G(W)|$ holds for all $W\subseteq X$.

??? note "Proof"
    The condition is clearly necessary. Suppose an $X$-perfect matching $M$ exists; then every vertex in $X$ is matched to a distinct vertex in $Y$. The set $N_G(W)$ includes at least the vertices matched to vertices in $W$, so its size is at least $|W|$.
    
    The condition is also sufficient. Suppose no $X$-perfect matching exists; then there is a maximum matching $M$ in which some vertex $v\in X$ is still unmatched. Let $Z$ be the set of all vertices reachable via alternating paths starting from $v$, and let $S=Z\cap X$, $T=Z\cap Y$. All vertices in $S\setminus\{v\}$ must be matched, because $G$ is bipartite, so an alternating path from $v$ to a vertex in $X$ has even length and its last edge must be a matched edge; all vertices in $T$ must also be matched, since otherwise an augmenting path would exist, which by Berge's lemma contradicts $M$ being maximum. Since they are all matched and matching can only happen between $X$ and $Y$, the vertices in $S\setminus\{v\}$ and in $T$ are in one-to-one correspondence, i.e. $|T|=|S|-1$. Meanwhile, since the vertices in $T$ are matched to vertices in $S$, at least $T\subseteq N_G(S)$; but for any $u\in N_G(S)$, say adjacent to $v'$ in $S$, we can extend the alternating path reaching $v'$ to an alternating path reaching $u$, hence $u\in T$: this shows $T=N_G(S)$. These arguments show $|N_G(S)|<|S|$, contradicting the hypothesis of Hall's theorem. Hence an $X$-perfect matching exists.

???+ note "Corollary"
    Every $k$-regular ($k\ge 1$) bipartite graph has a perfect matching.

??? note "Proof"
    In a regular bipartite graph all vertices have the same degree, say $k\ge 1$. First verify that Hall's condition holds, i.e. for any $W\subseteq X$, $|N_G(W)|\ge |W|$. The number of edges adjacent to vertices in $W$ is $k|W|$, and each vertex in $N_G(W)$ is adjacent to at most $k$ of them, so necessarily $k|W|\le k|N_G(W)|$, i.e. $|W|\le |N_G(W)|$. In particular, $|X|\le |Y|$; since $X$ and $Y$ are symmetric, $|X|=|Y|$. This shows that in a regular bipartite graph an $X$-perfect matching is also a perfect matching. Since Hall's theorem guarantees that an $X$-perfect matching exists, a perfect matching must exist as well.

### Tutte's theorem

Tutte's theorem provides a necessary and sufficient condition for the existence of a perfect matching in a general graph. The condition stems from a direct observation: a graph with an odd number of vertices cannot have a perfect matching.

???+ note "Tutte's theorem"
    A graph $G=(V,E)$ has a perfect matching if and only if for every $U\subseteq V$, $\operatorname{odd}(G-U)\le |U|$, where $G-U$ denotes the subgraph obtained from $G$ by deleting the vertices in $U$ and their incident edges, and $\operatorname{odd}(G-U)$ denotes the number of connected components of $G-U$ with an odd number of vertices.

??? note "Proof"
    It suffices to consider simple graphs, since multi-edges and self-loops affect neither Tutte's condition nor the existence of a perfect matching.
    
    Necessity is relatively easy. Suppose a perfect matching $M$ exists. For any $U\subseteq V$, after deleting the vertices in $U$ from $G$, every connected component with an odd number of vertices has at least one vertex that cannot be matched with a vertex of the same component, and such vertices can only be matched with vertices in $U$. For such a matching to exist, we need at least $\operatorname{odd}(G-U)\le |U|$. This is Tutte's condition.
    
    Sufficiency is more involved. Suppose $G$ satisfies Tutte's condition but has no perfect matching. Since adding any edge to $G$ keeps Tutte's condition satisfied, we may assume $G$ is a maximal such graph, i.e. $G$ has no perfect matching, but adding any edge $e$ not yet present makes $G+e$ have a perfect matching. Let $U\subseteq V$ be the set of all vertices of degree $|V|-1$. One can prove that every connected component of $G-U$ is a complete graph. From this, a perfect matching of $G$ can be constructed: first take a maximum matching of each connected component of $G-U$, so that an unmatched vertex appears only when the component has an odd number of vertices; match these unmatched vertices to vertices in $U$; since the number of vertices of $G$ is even (take $U=\varnothing$ in Tutte's condition), the number of remaining unmatched vertices in $U$ is also even, so pair them up. This contradiction shows that no $G$ satisfies Tutte's condition yet has no perfect matching.
    
    The key is to prove that every connected component of $G-U$ is a complete graph. Suppose not. Let vertices $x,y,z$ belong to such a component with $(x,y)\in E$, $(y,z)\in E$, $(x,z)\notin E$. Moreover, since $y\notin U$, there must be $w\in V\setminus U$ with $(y,w)\notin E$. By the maximality of $G$, the graphs $G+(x,z)$ and $G+(y,w)$ have perfect matchings $M_1$ and $M_2$ respectively. Consider their symmetric difference $M_1\oplus M_2$. Since all vertex degrees in the graph $(V,M_1\oplus M_2)$ are either $0$ or $2$, $M_1\oplus M_2$ is in fact a disjoint union of even cycles, each consisting of alternating matched edges from $M_1$ and $M_2$. We may assume $(x,z)\in M_1$ and $(y,w)\in M_2$, since otherwise $M_1$ or $M_2$ is already a perfect matching of $G$; hence both edges appear in $M_1\oplus M_2$.
    
    ![](images/tutte-proof.svg)
    
    As shown in the figure, there are two cases:
    
    -   $(x,z)$ and $(y,w)$ lie on different cycles (left): let $C$ be the cycle containing $(y,w)$; then the edge set $M_2\oplus C$ is a perfect matching of $G$;
    -   $(x,z)$ and $(y,w)$ lie on the same cycle (right): by symmetry, assume the cycle passes through $x,y,w,z$ in this order, so we can take the path $P$ on the cycle from $y$ via $w$ to $z$, denote $\{(y,z)\}\cup P$ as the cycle $C$, and then the edge set $M_2\oplus C$ is likewise a perfect matching of $G$.
    
    Either case contradicts the choice of $G$. This contradiction shows that every connected component of $G-U$ is a complete graph.

???+ note "Corollary"
    Every bridgeless 3-regular graph has a perfect matching.

??? note "Proof"
    To verify Tutte's condition, take any $U\subseteq V$; we need to prove $\operatorname{odd}(G-U)\le |U|$. Let $G_1,\cdots,G_n$ be all connected components of $G-U$ with an odd number of vertices. Let $m_i$ be the number of edges connecting vertices of $G_i$ to vertices of $U$. Simple counting gives
    
    $$
    3|V(G_i)| = \sum_{v\in V(G_i)} d(v) = 2|E(G_i)| + m_i.
    $$
    
    Hence $m_i$ must be odd. Since $G$ has no bridges (i.e. cut edges), $m_i\ge 3$. This shows
    
    $$
    \operatorname{odd}(G-U) = n \le \dfrac{1}{3}\sum_{i=1}^n m_i \le \dfrac{1}{3}\sum_{v\in U} d(v) = |U|.
    $$
    
    Therefore Tutte's condition holds and $G$ must have a perfect matching.

## Common algorithms

A basic problem in combinatorial optimization is finding the maximum matching and the maximum weight matching of a graph.

### Maximum bipartite matching

See the page [Maximum bipartite matching](./bigraph-match.md).

In an unweighted bipartite graph, the problem can be solved with Kuhn's algorithm in $O(|V||E|)$ time, or with the Hopcroft–Karp algorithm in $O(|V|^{1/2}|E|)$ time.

### Maximum weight bipartite matching

See the page [Maximum weight bipartite matching](./bigraph-weight-match.md).

In a weighted bipartite graph, the problem can be solved with the Hungarian algorithm. If the Bellman–Ford algorithm is used to find shortest paths, the time complexity is $O(|V|^2|E|)$; using Dijkstra's algorithm with a Fibonacci heap, it can be solved in $O(|V|^{2}\log {|V|}+|V||E|)$ time.

### Maximum matching in general graphs

See the page [Maximum matching in general graphs](./general-match.md).

In an unweighted general graph, the problem can be solved with Edmonds' blossom algorithm in $O(|V|^2|E|)$ time.

### Maximum weight matching in general graphs

See the page [Maximum weight matching in general graphs](./general-weight-match.md).

In a weighted general graph, the problem can be solved with Edmonds' blossom algorithm in $O(|V|^2|E|)$ time.

## Related problems

Maximum (weight) matching is closely connected to other graph-theoretic problems. This section only discusses general graphs; for results on bipartite graphs see the page [Maximum bipartite matching](./bigraph-match.md#相关问题).

### Maximum weight maximum cardinality matching

The maximum weight maximum cardinality matching problem and the maximum weight matching problem reduce to each other. A notable difference between them is that negative-weight edges may appear in a maximum weight maximum cardinality matching, but never in a maximum weight matching.

First, the maximum weight matching problem reduces to the maximum weight maximum cardinality matching problem. To do this, first set the weights of all negative edges of $G$ to $0$; then extend the graph to a complete graph $G'$ by adding edges of weight $0$. Note that in a complete graph with non-negative edge weights, the maximum weight maximum cardinality matching and the maximum weight matching coincide. So it suffices to compute the maximum weight maximum cardinality matching $M'$ of $G'$ and delete all zero-weight edges from $M'$; the resulting edge set $M$ is a maximum weight matching of $G$.[^other-approach]

![graph-match](images/graph-match-5.svg)

Conversely, the maximum weight maximum cardinality matching problem reduces to the maximum weight matching problem. It suffices to add a sufficiently large positive number $K$ to the weights of all edges of $G$; then the maximum weight matching of the resulting graph $G'$ is guaranteed to be a maximum matching, and hence necessarily a maximum weight maximum cardinality matching. This is because computing the maximum weight matching of $G'$ amounts to maximizing, over all matchings of $G$,

$$
K|M| + \sum_{e\in M}w(e).
$$

When $K$ is large enough, the gain $K$ from matching one more edge exceeds the change in the weight sum of the second term. Therefore the algorithm first matches as many edges as possible and only then maximizes the weight sum of the matched edges. The constant $K$ just needs to be strictly larger than the difference between the weight sums of any two matchings. An obvious choice is

$$
K = \sum_{e\in E}|w(e)| + 1.
$$

![graph-match](images/graph-match-6.svg)

### Minimum (weight) edge cover

Another problem closely related to maximum (weight) matching is the minimum (weight) edge cover. The relationship between edge covers and matchings (also called edge independent sets) is similar to that between vertex covers and independent sets.

A set of edges $C\subseteq E$ of a graph $G=(V,E)$ is called an **edge cover** of $G$ if every vertex $v\in V$ is an endpoint of some edge in $C$. When discussing edge covers, we always assume that $G$ has no isolated vertices.

For unweighted graphs, the minimum edge cover problem is almost the same as the maximum matching problem. For any maximum matching $M$ of $G$, adding one incident edge for every unmatched vertex yields a minimum edge cover $C$. Their sizes satisfy the simple relation $|M|+|C|=|V|$. The figure below shows some examples of minimum edge covers:

![graph-match](images/graph-match-7.svg)

For weighted graphs, the minimum weight edge cover problem reduces to a **minimum weight perfect matching** problem. First, make a copy of $G=(V,E)$ to obtain $\tilde G=(\tilde V,\tilde E)$ with the same edge weights; then connect every vertex $v\in V$ to its copy $\tilde v\in\tilde V$ with an edge whose weight is the minimum weight of the edges incident to $v$ in $G$. Denote the resulting graph by $G'=(V',E')$. If $G$ is bipartite or sparse, then $G'$ is likewise bipartite or sparse, respectively. Moreover, the minimum weight edge cover problem of $G$ reduces to the minimum weight perfect matching problem of $G'$[^edge-cover]: given a minimum weight perfect matching $M'$ of $G'$, keep the edges in $E$ and replace every matched $(v,\tilde v)$ with the minimum-weight edge incident to $v$ in $G$; this yields a minimum weight edge cover of $G$.

## References

1.  [Wikiwand - Matching (graph theory)](https://www.wikiwand.com/en/Matching_%28graph_theory%29)
2.  [Wikiwand - Blossom algorithm](https://www.wikiwand.com/en/Blossom_algorithm)
3.  Chen Yinbo, "A brief discussion of graph matching algorithms and their applications", 2015.
4.  [Algorithm Notes - Matching](http://web.ntnu.edu.tw/~algo/Matching.html)
5.  [the-tourist/algo](https://github.com/the-tourist/algo)
6.  [Bill Yang's Blog - Blossom algorithm notes](https://blog.bill.moe/blossom-algorithm-notes/)
7.  [Maximum matching, perfect matching and the Hungarian algorithm in bipartite graphs](https://www.renfei.org/blog/bipartite-matching.html)
8.  [Wikiwand - Hopcroft–Karp algorithm](https://www.wikiwand.com/en/Hopcroft%E2%80%93Karp_algorithm)
9.  Bondy, John Adrian, and Uppaluri Siva Ramachandra Murty. Graph theory with applications. Vol. 290. London: Macmillan, 1976.

[^other-approach]: Of course, this is not the only reduction. For a graph $G=(V,E)$, one can also attach a copy $\tilde G=(\tilde V,\tilde E)$ of it to the original graph vertex by vertex, and set the weights of all edges new relative to the original graph $G$ (including the edges in the copy) to $0$, obtaining a graph $G'=(V',E')$. In other words, the vertex set of the new graph $G'$ is $V\cup\tilde V$, and its edge set, besides the edges of $G$, connects every vertex $v\in V$ to its copy $\tilde v\in\tilde V$ by a zero-weight edge, and for every edge $(u,v)\in E$ connects $\tilde u$ and $\tilde v$ by a zero-weight edge. Every matching $M$ of $G$ corresponds to a perfect matching of $G'$ with the same weight sum: just match every unmatched vertex $v$ of $G$ with its copy $\tilde v$, and for every matched edge $(u,v)$ match $\tilde u$ with $\tilde v$. Therefore the maximum weight maximum cardinality matching of $G'$, i.e. its maximum weight perfect matching, restricted to $E$ gives a maximum weight matching of $G$. The advantage of this reduction is that if $G$ is bipartite or sparse, the extended graph $G'$ is likewise bipartite or sparse, respectively.

[^edge-cover]: For every perfect matching $M'$ of $G'$, the construction described here yields an edge cover $C$ of $G$ whose weight sum is half that of $M'$; reversing the construction, for every edge cover $C$ of $G$ one can construct a perfect matching $M'$ of $G'$ whose weight sum is at most twice that of $C$. This shows that the reduction is valid.
