---
title: Vertex/edge connectivity
---

## Definition

For the definitions of the following notions, see [basic concepts of graph theory](./concept.md):

-   edge connectivity, edge cut;
-   vertex connectivity, vertex cut;
-   clique.

## Properties

### Whitney's inequality

**Whitney's inequality** (1932) relates the vertex connectivity $\kappa$, the edge connectivity $\lambda$ and the minimum degree $\delta$:

$$
\kappa \le \lambda \le \delta
$$

???+ note "Proof"
    Intuitively, if there is an edge cut of size $\lambda$, picking one endpoint of each of its edges gives a vertex cut of size $\lambda$, so the first inequality holds.
    
    All edges incident to a vertex of minimum degree (any one of them, if there are several) form an edge cut of size $\delta$, so the second inequality holds as well.

This inequality cannot be improved; in other words, for every triple satisfying it there is a graph with exactly these parameters.

???+ note "Construction"
    Connect two cliques of size $\delta + 1$ by $\lambda$ edges so that in one clique these edges end at $\lambda$ distinct vertices and in the other at $\kappa$ distinct vertices.

### Menger's theorem

From the [max-flow min-cut theorem](./flow/min-cut.md) (also known as the Ford–Fulkerson theorem) it follows that the maximum number of disjoint (pairwise edge-disjoint) paths between two vertices equals the minimum size of a cut (this corollary is also called **Menger's theorem** – translator's note).

## Computation

Below, all edge weights are $1$.

### Edge connectivity via maximum flow

Enumerate the pairs of vertices $(s, t)$ and, for each one, run a maximum flow with source $s$, sink $t$ and edge weights $1$. This needs $O(n^2)$ maximum flows; with the Edmonds–Karp algorithm the complexity is $O(|V|^3 |E|^2)$. Dinic's algorithm does better: $O(|V|^2 |E| \min(|V|^{2/3}, |E|^{1/2}))$.

### Global minimum cut

With the [Stoer–Wagner algorithm](./stoer-wagner.md) a single minimum cut without source and sink suffices. The complexity is $O(|V||E| + |V|^{2}\log|V|)$, usually approximated as $O(|V|^3)$.

### Vertex connectivity

Again enumerate pairs of vertices, but this time split every vertex $x$ that is neither the source nor the sink into two vertices $x_1$ and $x_2$ joined by the edge $(x_1, x_2)$. Replace every edge $(u, v)$ of the original graph by the two edges $(u_2, v_1)$ and $(v_2, u_1)$. The maximum flow then equals the size of the minimum vertex cut between $s$ and $t$ (also called the local vertex connectivity). The complexity is the same as for computing the edge connectivity via maximum flow.

**This page is translated from the articles [Рёберная связность. Свойства и нахождение](http://e-maxx.ru/algo/rib_connectivity) and [Вершинная связность. Свойства и нахождение](http://e-maxx.ru/algo/vertex_connectivity) and their English translation [Edge connectivity/Vertex connectivity](https://cp-algorithms.com/graph/edge_vertex_connectivity.html). The Russian version is licensed under Public Domain + Leave a Link; the English version under CC-BY-SA 4.0.**

## Further reading

-   The paper [*Connectivity Algorithms*](https://www.cse.msu.edu/~cse835/Papers/Graph_connectivity_revised.pdf) surveys recent progress in algorithms for computing connectivity. Interested readers may browse it on their own.
