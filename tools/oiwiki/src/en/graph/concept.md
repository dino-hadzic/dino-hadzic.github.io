---
title: Graph theory concepts
---

This page gives an overview of some concepts from graph theory. Not all of them are common in competitive programming; contestants only need to master the basic part of this page, and if they meet an unfamiliar concept while studying, they can come back here and look it up.

??? warning "Warning"
    Definitions in graph theory often differ between textbooks; when you meet them, judge them by context.

## Graph

A **graph** is an ordered pair $G=(V(G), E(G))$. Here $V(G)$ is a non-empty set called the **vertex set**; every element of $V$ is called a **vertex** or **node**, or simply a **vertex**. $E(G)$ is the set of edges between the vertices of $V(G)$, called the **edge set**.

A graph is usually denoted $G=(V,E)$.

When both $V$ and $E$ are finite sets, $G$ is called a **finite graph**.

When $V$ or $E$ is an infinite set, $G$ is called an **infinite graph**.

There are several kinds of graphs, including **undirected graphs**, **directed graphs**, **mixed graphs**, etc.

If $G$ is an undirected graph, every element of $E$ is an unordered pair $(u, v)$ called an **undirected edge**, or simply an **edge**, where $u, v \in V$. If $e = (u, v)$, then $u$ and $v$ are called the **endpoints** of $e$.

If $G$ is a directed graph, every element of $E$ is an ordered pair $(u, v)$, sometimes also written $u \to v$, called a **directed edge** or **arc**; when there is no risk of confusion it may also be called an **edge**. If $e = u \to v$, then $u$ is called the **tail** of $e$ and $v$ the **head** of $e$; the tail and the head are also called the **endpoints** of $e$. We also say that $u$ is a direct predecessor of $v$ and $v$ is a direct successor of $u$.

???+ note "Why is the start called the tail and the end the head?"
    Edges are usually drawn as arrows, and an arrow points from its "tail" to its "head".

If $G$ is a mixed graph, $E$ contains both **directed edges** and **undirected edges**.

If every edge $e_k=(u_k,v_k)$ of $G$ is assigned a number as its **weight**, $G$ is called a **weighted graph**. If all these weights are positive real numbers, $G$ is called a **positively weighted graph**.

The number of vertices $\left| V(G) \right|$ of a graph $G$ is also called the **order** of $G$.

Informally, a graph consists of a number of vertices and edges connecting pairs of vertices.

## Adjacency

In an undirected graph $G = (V, E)$, if vertex $v$ is an endpoint of edge $e$, we say that $v$ and $e$ are **incident** or **adjacent**. For two vertices $u$ and $v$, if the edge $(u, v)$ exists, we say that $u$ and $v$ are **adjacent**.

The **neighborhood** of a vertex $v \in V$ is the set of all vertices adjacent to it, denoted $N(v)$.

The neighborhood of a vertex set $S$ is the set of all vertices adjacent to at least one vertex of $S$, denoted $N(S)$, i.e.:

$$
N(S) = \bigcup_{v \in S} N(v)
$$

## Simple graph

**Loop**: for an edge $e = (u, v)$ in $E$, if $u = v$, then $e$ is called a loop.

**Multiple edges**: if $E$ contains two completely identical elements (edges) $e_1, e_2$, they are called (a pair of) multiple edges.

**Simple graph**: a graph with no loops and no multiple edges is called a simple graph. A simple undirected graph with at least two vertices always has vertices of the same degree. ([Pigeonhole principle](../math/combinatorics/drawer-principle.md))

If a graph has loops or multiple edges, it is called a **multigraph**.

??? warning "Warning"
    In an undirected graph $(u, v)$ and $(v, u)$ count as a pair of multiple edges, while in a directed graph $u \to v$ and $v \to u$ are not multiple edges.

??? warning "Warning"
    In problems, unless stated otherwise, loops and multiple edges may exist, which needs special consideration when solving them.

## Degree

The number of edges incident to a vertex $v$ is called the **degree** of that vertex, denoted $d(v)$. In particular, every edge of the form $(v, v)$ contributes $2$ to $d(v)$.

For a simple undirected graph, $d(v) = \left| N(v) \right|$.

Handshaking lemma (also called the fundamental theorem of graph theory): for any undirected graph $G = (V, E)$, $\sum_{v \in V} d(v) = 2 \left| E \right|$.

Corollary: in any graph, the number of vertices of odd degree is even.

If $d(v) = 0$, $v$ is called an **isolated vertex**.

If $d(v) = 1$, $v$ is called a **leaf vertex**/**pendant vertex**.

If $2 \mid d(v)$, $v$ is called an **even vertex**.

If $2 \nmid d(v)$, $v$ is called an **odd vertex**. The number of odd vertices in a graph is even.

If $d(v) = \left| V \right| - 1$, $v$ is called a **universal vertex**.

For a graph, the minimum degree over all vertices is called the **minimum degree** of $G$, denoted $\delta (G)$; the maximum is called the **maximum degree**, denoted $\Delta (G)$. That is: $\delta (G) = \min_{v \in G} d(v)$, $\Delta (G) = \max_{v \in G} d(v)$.

In a directed graph $G = (V, E)$, the number of edges whose tail is vertex $v$ is called the **out-degree** of that vertex, denoted $d^+(v)$. The number of edges whose head is vertex $v$ is called the **in-degree** of that vertex, denoted $d^-(v)$. Obviously $d^+(v)+d^-(v)=d(v)$.

For any directed graph $G = (V, E)$:

$$
\sum_{v \in V} d^+(v) = \sum_{v \in V} d^-(v) = \left| E \right|
$$

If in an undirected graph $G = (V, E)$ every vertex has degree equal to a fixed constant $k$, $G$ is called a **$k$-regular graph**.

If for a given sequence a there is a graph G whose degree sequence is a, then a is called **graphic**.

If for a given sequence a there is a simple graph G whose degree sequence is a, then a is called **simple graphic**.

## Paths

**Walk**: a walk is a sequence of edges connecting a sequence of vertices; it may be of finite or infinite length. Formally, a finite walk $w$ is a sequence of edges $e_1, e_2, \ldots, e_k$ such that there is a sequence of vertices $v_0, v_1, \ldots, v_k$ with $e_i = (v_{i-1}, v_i)$ for $i \in [1, k]$. Such a walk is abbreviated $v_0 \to v_1 \to v_2 \to \cdots \to v_k$. Usually the number of edges $k$ is called the **length** of the walk (if the edges are weighted, the length usually means the sum of the edge weights along the walk, though problems may define it differently).

**Trail**: a walk $w$ in which $e_1, e_2, \ldots, e_k$ are pairwise distinct is called a trail.

**Path** (also called **simple path**): a trail $w$ in which the vertices of the vertex sequence are pairwise distinct is called a path.

**Circuit**: a trail $w$ with $v_0 = v_k$ is called a circuit.

**Cycle** (also called **simple circuit**): a circuit $w$ in which $v_0 = v_k$ is the only repeated pair of vertices in the vertex sequence is called a cycle.

??? warning "Warning"
    Definitions of paths may vary between sources; e.g. "path" may mean what is called a "walk" here, and "cycle" may mean what is called a "circuit" here. If you see such words in a problem without a special note such as "simple path"/"not necessarily simple path" (i.e. a "walk" here), it is best to ask what exactly is meant.

## Subgraph

For a graph $G = (V, E)$, if there is another graph $H = (V', E')$ with $V' \subseteq V$ and $E' \subseteq E$, then $H$ is called a **subgraph** of $G$, written $H \subseteq G$.

If $H \subseteq G$ satisfies: for all $u, v \in V'$, whenever $(u, v) \in E$ we also have $(u, v) \in E'$, then $H$ is called an **induced subgraph** of $G$.

It is easy to see that an induced subgraph is determined solely by the vertex set of the subgraph, so the induced subgraph with vertex set $V'$ ($V' \subseteq V$) is called the subgraph induced by $V'$, denoted $G \left[ V' \right]$.

If $H \subseteq G$ satisfies $V' = V$, then $H$ is called a **spanning subgraph** of $G$.

Obviously, $G$ is a subgraph, a spanning subgraph and an induced subgraph of itself; the [edgeless graph](#special-graphs) is a spanning subgraph of $G$. The original graph $G$ and the edgeless graph are the trivial subgraphs of $G$.

If some spanning subgraph $F$ of an undirected graph $G$ is a $k$-regular graph, then $F$ is called a **$k$-factor** of $G$.

If an induced subgraph $H = G \left[ V^\ast \right]$ of a directed graph $G = (V, E)$ satisfies: for all $v \in V^\ast$, $(v, u) \in E$ implies $u \in V^\ast$, then $H$ is called a **closed subgraph** of $G$.

## Connectivity

### Undirected graphs

In an undirected graph $G = (V, E)$, for $u, v \in V$, if there is a walk with $v_0 = u, v_k = v$, we say $u$ and $v$ are **connected**. By definition, every vertex is connected to itself, and the two endpoints of any edge are connected.

If in an undirected graph $G = (V, E)$ any two vertices are connected, $G$ is called a **connected graph**, and this property of $G$ is called **connectivity**.

If $H$ is a connected subgraph of $G$ and there is no $F$ with $H\subsetneq F \subseteq G$ such that $F$ is a connected graph, then $H$ is a **connected component** of $G$ (a maximal connected subgraph).

### Directed graphs

In a directed graph $G = (V, E)$, for $u, v \in V$, if there is a walk with $v_0 = u, v_k = v$, we say $v$ is **reachable** from $u$. By definition, every vertex is reachable from itself, and the head of any edge is reachable from its tail. (Connectivity in an undirected graph can be seen as reachability in both directions.)

If in a directed graph every two vertices are mutually reachable, the graph is called **strongly connected**.

If replacing the edges of a directed graph with undirected edges yields a connected graph, the original directed graph is called **weakly connected**.

Analogously to connected components, there are also **weakly connected components** (maximal weakly connected subgraphs) and **strongly connected components** (maximal strongly connected subgraphs).

For the related algorithms see [Strongly connected components](./scc.md).

### Cuts

For the related algorithms see [Cut vertices and bridges](./cut.md) and [Biconnected components](./bcc.md).

In this part, "connected" for a directed graph usually means "strongly connected".

For a connected graph $G = (V, E)$, if $V'\subseteq V$ and $G\left[V\setminus V'\right]$ (i.e. $G$ with the vertices of $V'$ removed) is not a connected graph, then $V'$ is a **vertex cut/separating set** of $G$. A vertex cut of size one is also called a **cut vertex**.

For a connected graph $G = (V, E)$ and an integer $k$, if $|V|\ge k+1$ and $G$ has no vertex cut of size $k-1$, then $G$ is called **$k$-vertex-connected**, and the largest $k$ for which this holds is called the **vertex connectivity** of $G$, denoted $\kappa(G)$. (For non-complete graphs, the vertex connectivity equals the size of the minimum vertex cut, while the vertex connectivity of the complete graph $K_n$ is $n-1$.)

For a graph $G = (V, E)$ and $u, v\in V$ with $u\ne v$, $u$ and $v$ not adjacent, and $v$ reachable from $u$, if $V'\subseteq V$, $u, v\notin V'$, and $u$ and $v$ are not connected in $G\left[V\setminus V'\right]$, then $V'$ is called a vertex cut between $u$ and $v$. The size of the minimum vertex cut between $u$ and $v$ is called the **local connectivity** between $u$ and $v$, denoted $\kappa(u, v)$.

Similar definitions can be made for edges:

For a connected graph $G = (V, E)$, if $E'\subseteq E$ and $G' = (V, E\setminus E')$ (i.e. $G$ with the edges of $E'$ removed) is not a connected graph, then $E'$ is an **edge cut** of $G$. An edge cut of size one is also called a **bridge**.

For a connected graph $G = (V, E)$ and an integer $k$, if $G$ has no edge cut of size $k-1$, then $G$ is called **$k$-edge-connected**, and the largest $k$ for which this holds is called the **edge connectivity** of $G$, denoted $\lambda(G)$. (For any graph, the edge connectivity equals the size of the minimum edge cut.)

For a graph $G = (V, E)$ and $u, v\in V$ with $u\ne v$ and $v$ reachable from $u$, if $E'\subseteq E$ and $u$ and $v$ are not connected in $G'=(V, E\setminus E')$, then $E'$ is called an edge cut between $u$ and $v$. The size of the minimum edge cut between $u$ and $v$ is called the **local edge-connectivity** between $u$ and $v$, denoted $\lambda(u, v)$.

**Biconnected** coincides almost completely with $2$-vertex-connected, except for the graph consisting of a single edge joining two vertices: it is biconnected but not $2$-vertex-connected. In other words, a connected graph without cut vertices is biconnected.

**$2$-edge-connected** (edge-biconnected) coincides completely with $2$-edge-connectivity. In other words, a connected graph without bridges is $2$-edge-connected.

Analogously to connected components, there are also **biconnected components** (maximal biconnected subgraphs) and **$2$-edge-connected components** (maximal $2$-edge-connected subgraphs).

**Whitney's theorem**: for any graph $G$, $\kappa(G)\le \lambda(G)\le \delta(G)$. (The three terms of the inequality are the vertex connectivity, the edge connectivity and the minimum degree, respectively.)

## Sparse/dense graphs

If the number of edges of a graph is much smaller than the square of its number of vertices, it is a **sparse graph**.

If the number of edges of a graph is close to the square of its number of vertices, it is a **dense graph**.

These two concepts have no strict definition; they are usually used when discussing the efficiency difference between algorithms with [time complexity](../basic/complexity.md) $O(|V|^2)$ and algorithms with complexity $O(|E|)$ (on dense graphs the two are about equally efficient, while on sparse graphs the $O(|E|)$ algorithm is clearly more efficient).

## Complement graph

For a simple undirected graph $G = (V, E)$, its **complement graph** is the graph, denoted $\bar G$, satisfying $V \left( \bar G \right) = V \left( G \right)$ and, for any pair of vertices $(u, v)$, $(u, v) \in E \left( \bar G \right)$ if and only if $(u, v) \notin E \left( G \right)$.

## Transpose graph

For a directed graph $G = (V, E)$, its **transpose graph** is the graph with the same vertex set in which every edge is reversed, i.e.: if the transpose graph of $G$ is $G'=(V, E')$, then $E'=\{(v, u)|(u, v)\in E\}$.

## Special graphs

If a simple undirected graph $G$ has an edge between any two distinct vertices, $G$ is called a **complete graph**; the complete graph of order $n$ is denoted $K_n$. If a directed graph $G$ has two edges of opposite directions between any two distinct vertices, $G$ is called a **complete digraph**.

A graph with an empty edge set is called an **edgeless graph**, **empty graph** or **null graph**; the edgeless graph of order $n$ is denoted $\overline{K}_n$ or $N_n$. $N_n$ and $K_n$ are complements of each other.

??? warning "Warning"
    **Null graph** may also refer to the **order-zero graph** $K_0$, i.e. the graph whose vertex set and edge set are both empty.

If a simple directed graph $G$ has exactly one edge (in one direction) between any two distinct vertices, $G$ is called a **tournament graph**.

If all edges of a simple undirected graph $G = \left( V, E \right)$ form exactly one cycle, $G$ is called a **cycle graph**; the cycle graph of order $n$ ($n \geq 3$) is denoted $C_n$. It is easy to see that a graph is a cycle graph if and only if it is a $2$-regular connected graph.

If a simple undirected graph $G = \left( V, E \right)$ has a universal vertex $v$ and no edges between the remaining vertices, $G$ is called a **star graph**; the star graph of order $n + 1$ ($n \geq 1$) is denoted $S_n$.

If a simple undirected graph $G = \left( V, E \right)$ has a universal vertex $v$ and the other vertices form a cycle, $G$ is called a **wheel graph**; the wheel graph of order $n + 1$ ($n \geq 3$) is denoted $W_n$.

If all edges of a simple undirected graph $G = \left( V, E \right)$ form exactly one simple path, $G$ is called a **chain/path graph**; the chain of order $n$ is denoted $P_n$. It is easy to see that a chain is obtained from a cycle graph by deleting one edge.

If an undirected connected graph contains no cycle, it is called a **tree**. For details see [Tree basics](./tree-basic.md).

If an undirected connected graph contains exactly one cycle, it is called a **pseudotree**.

If every vertex of a weakly connected directed graph has in-degree $1$, it is called an **outward pseudotree**.

If every vertex of a weakly connected directed graph has out-degree $1$, it is called an **inward pseudotree**.

Several trees form a **forest**, several pseudotrees form a **pseudoforest**, several outward pseudotrees form an **outward pseudoforest**, and several inward pseudotrees form an **inward pseudoforest (functional graph)**.

If every edge of an undirected connected graph lies on at most one cycle, it is called a **cactus**. Several cacti form a **desert**.

If the vertex set of a graph can be split into two parts with no edges inside either part, the graph is a **bipartite graph**. If in a bipartite graph there is an edge between any two vertices from different parts, the graph is a **complete bipartite graph/biclique**; the complete bipartite graph whose parts have $n$ and $m$ vertices is denoted $K_{n, m}$. For details see [Bipartite graphs](./bi-graph.md).

If a graph can be drawn in the plane so that no two edges cross except at endpoints, the graph is a **planar graph**. For a simple connected planar graph $G=(V, E)$ with $V\ge 3$, $|E|\le 3|V|-6$.  
**Kuratowski's theorem**: a graph is planar if and only if it has no subgraph **homeomorphic** to $K_5$ or $K_{3, 3}$. Here graphs $G$ and $G'$ are homeomorphic if both can be turned into the same graph by adding some vertices of degree $2$ on edges[^ref1].

## Isomorphism

For two graphs $G$ and $H$, if there is a bijection $f : V(G) \to V(H)$ such that $(u,v)\in E(G)$ if and only if $(f(u),f(v))\in E(H)$, then $f$ is called an **isomorphism** from $G$ to $H$, and the graphs $G$ and $H$ are **isomorphic**, written $G \cong H$.

From the definition, if $G \cong H$, then necessarily:

-   $|V(G)|=|V(H)|,|E(G)|=|E(H)|$
-   $G$ and $H$ have the same non-increasing sequence of vertex degrees
-   $G$ and $H$ have isomorphic induced subgraphs

## Binary operations on simple undirected graphs

For simple undirected graphs we can define the following binary operations:

**Intersection**: the intersection of graphs $G = \left( V_1, E_1 \right), H = \left( V_2, E_2 \right)$ is defined as the graph $G \cap H = \left( V_1 \cap V_2, E_1 \cap E_2 \right)$.

It is easy to prove that the intersection of two simple undirected graphs is again a simple undirected graph.

**Union**: the union of graphs $G = \left( V_1, E_1 \right), H = \left( V_2, E_2 \right)$ is defined as the graph $G \cup H = \left( V_1 \cup V_2, E_1 \cup E_2 \right)$.

**Sum/direct sum**: for $G = \left( V_1, E_1 \right), H = \left( V_2, E_2 \right)$, construct an arbitrary $H' \cong H$ such that $V \left( H' \right) \cap V_1 = \varnothing$ ($H'$ may equal $H$). Then any graph isomorphic to $G \cup H'$ is called the sum/direct sum/disjoint union of $G$ and $H$, denoted $G + H$ or $G \oplus H$.

If the vertex sets of $G$ and $H$ are themselves disjoint, then $G \cup H = G + H$.

For example, a forest can be defined as the sum of several trees.

???+ note "Difference between union and sum"
    One can think of it as: the "union" merges the vertices and edges "with the same name" in the two graphs, while the "sum" does not.

## Special vertex/edge sets

### Dominating set

For an undirected graph $G=(V, E)$, if $V'\subseteq V$ and for every $v\in(V\setminus V')$ there is an edge $(u, v)\in E$ with $u\in V'$, then $V'$ is a **dominating set** of $G$.

The size of the minimum dominating set of an undirected graph $G$ is denoted $\gamma(G)$. Finding the minimum dominating set of a graph is [NP-hard](../misc/cc-basic.md#np-hard).

For a directed graph $G=(V, E)$, if $V'\subseteq V$ and for every $v\in(V\setminus V')$ there is an edge $(u, v)\in E$ with $u\in V'$, then $V'$ is an **out-dominating set** of $G$. Similarly one can define the **in-dominating set** of a directed graph.

The size of the minimum out-dominating set of a directed graph $G$ is denoted $\gamma^+(G)$, and that of the minimum in-dominating set $\gamma^-(G)$.

### Edge dominating set

For a graph $G=(V, E)$, if $E'\subseteq E$ and for every $e\in(E\setminus E')$ there is an edge in $E'$ sharing a vertex with it, then $E'$ is called an **edge dominating set** of $G$.

Finding the minimum edge dominating set of a graph is [NP-hard](../misc/cc-basic.md#np-hard).

### Independent set

For a graph $G=(V, E)$, if $V'\subseteq V$ and no two vertices of $V'$ are adjacent, then $V'$ is an **independent set** of $G$.

The size of the maximum independent set of a graph $G$ is denoted $\alpha(G)$. Finding the maximum independent set of a graph is [NP-hard](../misc/cc-basic.md#np-hard).

### Matching

For a graph $G=(V, E)$, if $E'\subseteq E$, no two distinct edges of $E'$ share an endpoint, and no edge of $E'$ is a loop, then $E'$ is a **matching** of $G$, also called an **independent edge set**. If a vertex is an endpoint of some edge of the matching, the vertex is called **matched/saturated**; otherwise it is called **unmatched**.

The matching with the most edges is called a **maximum-cardinality matching** of the graph. The size of the maximum matching of $G$ is denoted $\nu(G)$.

If the edges are weighted, the matching with the largest total weight is called a **maximum-weight matching** of the graph.

If a matching stops being a matching after adding any edge, it is a **maximal matching**. The largest maximal matching is a maximum matching, and any maximum matching is maximal. A maximal matching is always an edge dominating set, but an edge dominating set is not necessarily a matching. The minimum maximal matching and the minimum edge dominating set have the same size, but the minimum edge dominating set is not necessarily a matching. Finding the minimum maximal matching is NP-hard.

If all vertices are matched in a matching, it is a **perfect matching**. If exactly one vertex is unmatched in a matching, it is a **near-perfect matching**.

Counting the matchings or perfect matchings of a general or bipartite graph is [#P-complete](../misc/cc-basic.md#p_1).

For a matching $M$, if a path starts at an unmatched vertex and, of every two consecutive edges, one is in the matching and the other is not, the path is called an **alternating path**; an alternating path that ends at an unmatched vertex is called an **augmenting path**.

**Tutte's theorem**: an undirected graph $G$ of order $n$ has a perfect matching if and only if for every $V' \subset V(G)$, $p_{\text{odd}}(G-V')\leq |V'|$, where $p_{\text{odd}}$ denotes the number of connected components of odd order.

**Tutte's theorem (corollary)**: every bridgeless 3-regular graph has a perfect matching.

### Vertex cover

For a graph $G=(V, E)$, if $V'\subseteq V$ and every $e\in E$ has at least one endpoint in $V'$, then $V'$ is called a **vertex cover** of $G$.

A vertex cover is necessarily a dominating set, but a minimal vertex cover is not necessarily a minimal dominating set.

A vertex set is a vertex cover if and only if its complement is an independent set, so the complement of a minimum vertex cover is a maximum independent set. Finding the minimum vertex cover of a graph is [NP-hard](../misc/cc-basic.md#np-hard).

The size of any matching of a graph does not exceed the size of any of its vertex covers. In the complete bipartite graph $K_{n, m}$ the sizes of the maximum matching and the minimum vertex cover are both $\min(n, m)$.

### Edge cover

For a graph $G=(V, E)$, if $E'\subseteq E$ and every $v\in V$ is adjacent to at least one edge of $E'$, then $E'$ is called an **edge cover** of $G$.

The size of the minimum edge cover is denoted $\rho(G)$ and can be obtained by greedily extending a maximum matching: for every unmatched vertex, add one of its incident edges to the maximum matching, which yields a minimum edge cover.

A maximum matching can also be obtained from a minimum edge cover: for every pair of edges of the minimum edge cover sharing a vertex, delete one of them.

The size of the minimum edge cover of a graph plus the size of the maximum matching equals the number of vertices of the graph, i.e. $\rho(G)+\nu(G)=|V(G)|$.

The size of the maximum matching of a graph does not exceed the size of the minimum edge cover, i.e. $\nu(G)\le\rho(G)$. In particular, a perfect matching is always a minimum edge cover, and this is the only case in which the inequality above becomes an equality.

The size of any independent set of a graph does not exceed the size of any of its edge covers. In the complete bipartite graph $K_{n, m}$ the sizes of the maximum independent set and the minimum edge cover are both $\max(n, m)$.

### Clique

For a graph $G=(V, E)$, if $V'\subseteq V$ and any two distinct vertices of $V'$ are adjacent, then $V'$ is a **clique** of $G$. The subgraph induced by a clique is a complete graph.

If a clique stops being a clique after adding any vertex, it is a **maximal clique**.

The size of the maximum clique of a graph is denoted $\omega(G)$; the size of the maximum clique equals the size of the maximum independent set of the complement, i.e. $\omega(G)=\alpha(\bar{G})$. Finding the maximum clique of a graph is [NP-hard](../misc/cc-basic.md#np-hard).

## References

[OI 中转站 - 图论概念梳理](https://yhx-12243.github.io/OI-transit/memos/14.html)

[Wikipedia](https://en.wikipedia.org/wiki/Glossary_of_graph_theory_terms) (and the entries for the related concepts)

离散数学（修订版）, 田文成 周禄新 编著, 天津文学出版社, pp. 184-187

戴一奇, 胡冠章, 陈卫. 图论与代数结构 \[M]. 北京: 清华大学出版社, 1995.

[^ref1]: This operation is also called subdivision.
