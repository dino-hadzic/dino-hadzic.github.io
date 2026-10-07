---
title: Graph coloring
---

## Vertex coloring

(We discuss undirected graphs without self-loops.)

Color the vertices of an undirected graph so that adjacent vertices do not share a color. If G is $k$-colorable but not $(k-1)$-colorable, k is called the chromatic number of G, denoted $\chi(G)$.

For any graph G, $\chi(G) \leq \Delta(G) + 1$, where $\Delta(G)$ is the maximum degree.

### Brooks' theorem

If a connected graph is neither a complete graph nor an odd cycle, then $\chi(G) \leq \Delta(G)$.

#### Proof

???+ note "Proof"
    Let $|V(G)|=n$; we proceed by induction.
    
    First, for $n\leq 3$ the claim obviously holds.
    
    Next, assume the claim holds for $n-1$; we will now strengthen the claim step by step.
    
    It suffices to consider $\Delta(G)$-regular graphs, since a non-regular graph can be viewed as a regular graph with some edges removed, and this process does not affect the conclusion.
    
    For any regular graph G that is neither complete nor an odd cycle, take any vertex v and consider the subgraph $H:=G-v$; by the induction hypothesis $\chi(H)\leq\Delta(H)=\Delta(G)$, so it remains to prove that inserting v into H does not affect the conclusion.
    
    Let $\Delta:=\Delta(G)$, let the $\Delta$ colors used on H be $c_1,c_2,\dots,c_{\Delta}$, and let the $\Delta$ neighbors of v be $v_1,v_1,\dots,v_{\Delta}$. We may assume that these neighbors of v have pairwise different colors; otherwise the claim is proved.
    
    Next, let all vertices of H colored $c_i$ or $c_j$, together with all edges between them, form the subgraph $H_{i,j}$. We may assume that any 2 distinct vertices $v_i$, $v_j$ lie in the same connected component of $H_{i,j}$; if they were in two components, we could swap the colors of all vertices in one of the components, making $v_i$, $v_j$ the same color.
    
    > Swapping colors here means: if the graph has only two colors a and b, recolor all vertices originally colored a with b, and all vertices originally colored b with a.
    
    Denote this connected component by $C_{i,j}$; then $C_{i,j}$ can only be a path from $v_i$ to $v_j$. Since the degree of $v_i$ in H is $\Delta-1$, the neighbors of $v_i$ in H must have pairwise different colors (otherwise $v_i$ could be recolored with another color and would then share a color with another neighbor of v), so $v_i$ has exactly 1 neighbor in $C_{i,j}$; likewise for $v_j$. Then take a path from $v_i$ to $v_j$ in $C_{i,j}$ and call it P; if $C_{i,j}\ne P$, we recolor the vertices along P in order and let u be the first vertex of degree greater than 2 we encounter; the neighbors of u use at most $\Delta-2$ colors, so u can be recolored, making $v_i$, $v_j$ disconnected.
    
    Then it is easy to see that for any 3 distinct vertices $v_i$, $v_j$, $v_k$, $V(C_{i,j})\cap V(C_{j,k})=\{v_j\}$.
    
    At this point the strengthening of the claim is complete.
    
    The rest is simple. First, if the neighbors of v are pairwise adjacent, the claim is proved. Without loss of generality let $v_1$, $v_2$ be non-adjacent; take the neighbor w of $v_1$ in $C_{1,2}$ and swap the colors in $C_{1,3}$. In the new graph, $w\in V(C_{1,2})\cap V(C_{2,3})$, a contradiction.
    
    This completes the proof.

### Welsh–Powell algorithm

The Welsh–Powell algorithm is a greedy algorithm for finding a coloring when **the number of colors is not limited**.

For an undirected graph G without self-loops, let $V(G):=\{v_1,v_2,\dots,v_n\}$ satisfy

$\deg(v_i)\geq\deg(v_{i+1}),~\forall 1\leq i\leq n-1$

The number of colors used by the Welsh–Powell algorithm is at most $\max_{i=1}^n\min\{\deg(v_i)+1,i\}$, and the time complexity of the algorithm is $O\left(n\max_{i=1}^n\min\{\deg(v_i)+1,i\}\right)=O(n^2)$.

#### Procedure

1.  Sort the currently uncolored vertices in descending order of degree.
2.  Color the first vertex with an unused color.
3.  Go through the following vertices in order; if the current vertex is **not adjacent** to any vertex with the **same** color as the first vertex, color it with the color of the first vertex.
4.  If there are still uncolored vertices, go back to step 1; otherwise stop.

An example:

![Original](images/color1.png)

(Generated with [Graph Editor](https://csacademy.com/app/graph_editor/).)

First sort the vertices in descending order of degree:

| Order                   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9  | 10 | 11 | 12 | 13 |
| ----------------------- | - | - | - | - | - | - | - | - | -- | -- | -- | -- | -- |
| Vertex label            | 4 | 5 | 0 | 2 | 9 | 1 | 3 | 6 | 10 | 12 | 7  | 8  | 11 |
| Degree                  | 5 | 5 | 4 | 4 | 4 | 3 | 3 | 3 | 3  | 3  | 2  | 2  | 1  |
| $\min\{\deg(v_i)+1,i\}$ | 1 | 2 | 3 | 4 | 5 | 4 | 4 | 4 | 4  | 4  | 3  | 3  | 2  |

So the Welsh–Powell algorithm uses at most 5 colors.

Moreover, since the graph has a subgraph $C_3$, the chromatic number is at least 3.

-   First coloring:

    ![Colored 1](images/color2.png)

    Color vertices `4 9 3 11`.
-   Second coloring:

    ![Colored 2](images/color3.png)

    Color vertices `5 2 6 7 8`.
-   Third coloring:

    ![Colored 3](images/color4.png)

    Color vertices `0 1 10 12`.

#### Proof

???+ note "Proof"
    For an undirected graph G without self-loops, let $V(G):=\{v_1,v_2,\dots,v_n\}$ satisfy
    
    $\deg(v_i)\geq\deg(v_{i+1}),~\forall 1\leq i\leq n-1$
    
    Let $V_0=\varnothing$; we take a subset $V_m$ of $V(G)\setminus\bigcup_{i=0}^{m-1} V_i$ whose elements satisfy
    
    1.  $v_{k_m}\in V_m$, where $k_m=\min\{k:v_k\notin\bigcup_{i=0}^{m-1} V_i\}$
    2.  If
    
        $\{v_{i_{m,1}},v_{i_{m,2}},\dots,v_{i_{m,l_m}}\}\subset V_m,~i_{m,1}<i_{m,2}<\dots<i_{m,l_m}$
    
        then $v_j\in V_m$ if and only if
    
        1.  $j>i_{m,l_m}$
        2.  $v_j$ is adjacent to none of $v_{i_{m,1}},v_{i_{m,2}},\dots,v_{i_{m,l_m}}$
    
    Clearly, if the vertices of $V_i$ are given the i-th color, this coloring is exactly the one produced by the Welsh–Powell algorithm, and clearly
    
    -   $V_1\neq\varnothing$
    -   $V_i\cap V_j=\varnothing\iff i\neq j$
    -   $\exists \alpha(G)\in\Bbb{N}^*,\forall i>\alpha(G),~s.t.~ V_i=\varnothing$
    
    We only need to prove:
    
    $\bigcup_{i=1}^{\alpha(G)} V_i=V(G)$
    
    where
    
    $\chi(G)\leq\alpha(G)\leq\max_{i=1}^n\min\{\deg(v_i)+1,i\}$
    
    The left inequality obviously holds; we consider the right one.
    
    First, it is easy to see:
    
    if $v\notin\bigcup_{i=1}^mV_i$, then v is adjacent to at least one vertex in each of $V_1,V_2,\dots,V_m$, hence $\deg(v)\geq m$
    
    and therefore
    
    $v_j\in\bigcup_{i=1}^{\deg(v_j)+1}V_i$
    
    On the other hand, from the construction of the sequence $\{V_i\}$ it is easy to see
    
    $v_j\in\bigcup_{i=1}^j V_i$
    
    Combining the two relations proves the claim.

## Edge coloring

Color the edges of an undirected graph so that adjacent edges get different colors. If G is k-edge-colorable but not $(k-1)$-edge-colorable, k is called the edge chromatic number of G, denoted $\chi'(G)$.

### Vizing's theorem

If G is a simple graph, then $\Delta(G) \leq \chi'(G) \leq \Delta(G) + 1$

If G is a bipartite graph, then $\chi'(G)=\Delta(G)$

When $n$ is odd ($n \neq 1$), $\chi'(K_n)=n$; when $n$ is even, $\chi'(K_n)=n-1$

### Constructive proof of Vizing's theorem for bipartite graphs

???+ note "Proof"
    Add the edges to the bipartite graph one by one.
    
    When trying to add the edge $(x,y)$, we look for the unused color with the smallest index at $x$ and at $y$; call them $l_x$ and $l_y$ respectively.
    
    If $l_x=l_y$, we can directly set the color of this edge to $l_x$.
    
    Otherwise, assume $l_x<l_y$; we try to change the color of the edge of color $l_x$ leaving vertex $y$ to $l_y$.
    
    The modification process can be viewed approximately as a finite, uniquely determined augmenting path starting from $y$ and passing through edges of colors $l_x,l_y,\cdots$ in turn.
    
    Since the augmenting path is finite, we can flip the colors of all edges on it, i.e. change those of color $l_x$ to $l_y$ and those of color $l_y$ to $l_x$.
    
    By the property of bipartite graphs, vertex $x$ cannot be on the augmenting path, since that would contradict $l_x$ being the smallest unused color.
    
    So after augmenting we can directly set the color of the edge connecting $x$ and $y$ to $l_x$.
    
    The total time complexity of the construction is $O(nm)$.

???+ note "Example code [UVa10615 Rooks](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=18&page=show_problem&problem=1556)"
    ```cpp
    --8<-- "docs/graph/code/color/color_1.cpp"
    ```

??? note "A rather non-trivial example [UOJ 444 Bipartite graph](https://uoj.ac/problem/444)"
    This problem was set by the author in 2018 as a first-round homework problem for the Chinese national training team.
    
    First, we observe that a lower bound on the answer is the number of vertices whose degree is not a multiple of k.
    
    The construction achieving the lower bound splits the vertices of the bipartite graph.
    
    If $degree \bmod k \neq 0$, split the vertex into $degree/k$ vertices of degree k and one vertex of degree $degree \bmod k$.
    
    If $degree \bmod k = 0$, split the vertex into $degree/k$ vertices of degree k.
    
    The split vertices have the same meaning in the original graph, i.e. subject to the degree constraints, an edge endpoint may connect to any of the split vertices.
    
    By Vizing's theorem we can obviously construct a k-coloring of this graph.
    
    The edge deletion part has little to do with Vizing's theorem and is not expanded on here.
    
    Interested readers can read the author's editorial from that time.

## Chromatic polynomial

$P(G,k)$ denotes the total number of different k-colorings of G.

$P(K_n, k) = k(k-1)\cdots(k-n+1)$

$P(N_n, k) = k^n$

In an undirected graph G without self-loops,

1.  if $e=(v_i, v_j) \notin E(G)$, then $P(G, k) = P(G \cup e, k)+P(G\setminus e, k)$
2.  if $e=(v_i, v_j) \in E(G)$, then $P(G,k)=P(G-e,k)-P(G\setminus e,k)$

Theorem: let $V_1$ be a vertex separator of G such that $G[V_1]$ is a complete subgraph of G of order $|V_1|$, and let $G-V_1$ have $p(p \geq 2)$ connected components; then:

$P(G,k)=\frac{\Pi_{i=1}^{p}{(P(H_i, k))}}{P(G[V_1], k)^{p-1}}$

where $H_i=G[V_1 \cup V(G_i)]$

## References

1.  [Graph coloring - Wikipedia](https://en.wikipedia.org/wiki/Graph_coloring)
2.  Welsh, D. J. A.; Powell, M. B. (1967), "[An upper bound for the chromatic number of a graph and its application to timetabling problems](https://doi.org/10.1093%2Fcomjnl%2F10.1.85)", The Computer Journal, 10 (1): 85–86
