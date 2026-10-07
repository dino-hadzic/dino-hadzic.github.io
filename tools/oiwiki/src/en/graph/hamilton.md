---
title: Hamiltonian graphs
---

## Definition

A path that passes through every vertex of the graph exactly once is called a Hamiltonian path.

A cycle that passes through every vertex of the graph exactly once is called a Hamiltonian cycle.

A graph that has a Hamiltonian cycle is called a Hamiltonian graph.

A graph that has a Hamiltonian path but no Hamiltonian cycle is called a semi-Hamiltonian graph.

## Properties

Let $G=\langle V, E\rangle$ be a Hamiltonian graph. Then for every nonempty proper subset $V_1$ of $V$ we have $p(G-V_1) \leq |V_1|$, where $p(x)$ is the number of connected components of $x$.

Corollary: let $G=\langle V, E\rangle$ be a semi-Hamiltonian graph. Then for every nonempty proper subset $V_1$ of $V$ we have $p(G-V_1) \leq |V_1|+1$, where $p(x)$ is the number of connected components of $x$.

The complete graph $K_{2k+1} (k \geq 1)$ contains $k$ edge-disjoint Hamiltonian cycles, and these $k$ edge-disjoint Hamiltonian cycles contain all edges of $K_{2k+1}$.

The complete graph $K_{2k} (k \geq 2)$ contains $k-1$ edge-disjoint Hamiltonian cycles; the graph obtained from $K_{2k}$ by removing these $k-1$ edge-disjoint Hamiltonian cycles contains $k$ pairwise non-adjacent edges.

## Sufficient conditions

Let $G$ be a simple undirected graph with $n(n \geq 2)$ vertices. If for every pair of non-adjacent vertices $v_i, v_j$ of $G$ we have $d(v_i)+ d(v_j) \geq n - 1$, then $G$ has a Hamiltonian path.

Corollary 1: let $G$ be a simple undirected graph with $n(n \geq 3)$ vertices. If for every pair of non-adjacent vertices $v_i, v_j$ of $G$ we have $d(v_i)+ d(v_j) \geq n$, then $G$ has a Hamiltonian cycle, so $G$ is a Hamiltonian graph.

Corollary 2: let $G$ be a simple undirected graph with $n(n \geq 3)$ vertices. If for every vertex $v_i$ of $G$ we have $d(v_i) \geq \frac{n}{2}$, then $G$ has a Hamiltonian cycle, so $G$ is a Hamiltonian graph.

Let $D$ be a tournament of order $n(n \geq 2)$. Then $D$ has a Hamiltonian path.

If $D$ contains a tournament of order $n(n \geq 2)$ as a subgraph, then $D$ has a Hamiltonian path.

A strongly connected tournament is a Hamiltonian graph.

If $D$ contains a strongly connected tournament of order $n(n \geq 2)$ as a subgraph, then $D$ has a Hamiltonian cycle.
