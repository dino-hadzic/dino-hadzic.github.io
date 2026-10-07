---
title: Planar graphs
---

This article introduces planar graphs, plane graphs and related concepts.

## Planar graphs

If a graph $G$ can be drawn in a plane $S$ so that edges intersect only at vertices, we say that $G$ can be embedded in the plane $S$ and that $G$ is a **planar graph**. The drawing without edge crossings is called a plane representation or **planar embedding** of $G$. Such a planar embedding of a planar graph is also called a **plane graph**.

???+ info "\"Planar graph\" and \"plane graph\""
    In different texts the meaning of the term "planar graph" may differ. In the definitions of this article, a planar graph is a graph-theoretic object that may be embedded in the plane in different ways; a plane graph is a geometric object that, besides the graph structure, also specifies how the graph is drawn. One planar graph usually corresponds to several plane graphs. Therefore, for results in this article that depend only on the graph structure we use the term "planar graph"; for results that also depend on the planar embedding we use the term "plane graph".

Here are simple examples of planar graphs:

![](images/planar-1.svg)

(left: the butterfly graph; right: the complete graph $K_4$ of order $4$)

Here are simple examples of non-planar graphs:

![](images/planar-2.svg)

(left: the complete graph $K_5$ of order $5$; right: the complete bipartite graph $K_{3,3}$ with $3$ vertices on each side)

## Properties

This section presents properties of plane graphs.

### Faces and their degrees

Let $G$ be a plane graph; the edges of $G$ divide the plane containing $G$ into several regions, and each region is called a **face** of $G$. The unbounded face is called the **unbounded face** or **external face**, and the bounded ones are called finite or internal faces. Every plane graph has exactly one external face.

The closed walk formed by all edges surrounding a face is called the **boundary** of that face, and the edges of the boundary are said to be **incident** with the face. The length of the boundary is called the **degree** of the face. When computing the degree of a face, every cut edge is counted twice. The sum of the degrees of all faces of a plane graph equals $2$ times the number of edges $|E|$.

In a plane graph, the boundary of a face of degree $1$ corresponds to a self-loop, and the boundary of a face of degree $2$ usually corresponds to a pair of multiple edges[^face-2]. In a simple connected plane graph with $|V|\ge 3$ vertices, all faces have degree at least $3$.

### Euler's formula

An important property of plane graphs is **Euler's formula**. It gives the relation between the number of vertices $|V|$, the number of edges $|E|$ and the number of faces $|F|$ of a graph.

???+ note "Euler's formula"
    For a connected plane graph $G$,
    
    $$
    |V| - |E| + |F| = 2.
    $$

??? note "Proof"
    We use induction on the number of faces $|F|$. The base case is $|F|=1$. Then the plane graph has only the external face and all edges are cut edges. Hence the graph $G$ is a tree, so necessarily $|E|=|V|-1$; substituting into Euler's formula shows that it holds. Assume Euler's formula holds for plane graphs with $|F| = k$ faces. In a plane graph $G$ with $|F|=k + 1$ faces there must exist a non-cut edge $e$, which is a common edge of two different faces. Deleting the edge $e$ from the graph gives the graph $G-e$ with $|V|$ vertices, $|E|-1$ edges and $|F|-1$ faces. By the induction hypothesis Euler's formula holds for $G-e$, i.e. $|V|-(|E|-1)+(|F|-1)=2$, and rearranging gives Euler's formula for $G$. Hence, by induction, Euler's formula holds for all plane graphs.

???+ note "Corollary"
    For a plane graph $G$ with $k$ connected components,
    
    $$
    |V| - |E| + |F| = k + 1.
    $$

??? note "Proof"
    Every connected component of $G$ is a plane graph, but these components share the same external face. So if we apply Euler's formula to each component directly and add them up, the total numbers of vertices and edges are correct, but the total number of faces is too large by $(k-1)$, because the unique external face has been counted $k$ times in total. Taking this correction into account gives $|V|-|E|+|F| = 2k - (k-1) = k+1$.

From this one can derive a relation between the numbers of edges and vertices of a plane graph.

???+ note "Theorem"
    For a plane graph $G$ with $k$ connected components, if every face of $G$ has degree at least $l \ge 3$, then
    
    $$
    |E| \le \dfrac{l}{l-2}(|V|-k-1).
    $$

??? note "Proof"
    Since every face of $G$ has degree at least $l$, the sum of the degrees of all faces is at least $l|F|$, i.e. $2|E| \ge l|F|$. Substituting the corollary of Euler's formula $|V| - |E| + |F| = k + 1$ gives
    
    $$
    2|E| \ge l(k + 1 - |V| + |E|).
    $$
    
    Using $l \ge 2$ and solving for $|E|$ gives
    
    $$
    |E| \le \dfrac{l}{l-2}(|V|-k-1).
    $$

???+ note "Corollary"
    Let $G$ be a simple planar graph with $|V|\ge 3$. Then
    
    $$
    |E| \le 3|V|-6.
    $$

??? note "Proof"
    When $G$ is connected, all faces have degree at least $3$. Taking $k=1$ and $l=3$ in the theorem above gives $|E|\le 3|V|-6$.
    
    When $G$ is not connected, there are two cases:
    
    -   If some connected component has at least $3$ vertices, then for each component with at least $3$ vertices we can set up the inequality $|E_i|\le 3|V_i|-6$ separately. The components with fewer than $3$ vertices certainly satisfy $|E_i|\le |V_i| \le 3|V_i|$. Adding the inequalities for all components gives $|E|\le 3|V|-6$.
    -   If all connected components have fewer than $3$ vertices, then overall $|E|\le |V|$. Since $|V|\le 3|V|-6$ for $|V|\ge 3$, $|E|\le 3|V|-6$ still holds.
    
    This proves the claim.

This corollary shows that simple planar graphs are sparse graphs.

### Dual graph

Every plane graph has a corresponding (geometric) dual graph.

![](images/planar-dual-1.svg)

Let $G$ be a plane graph; the graph $G^*$ is drawn as follows:

1.  Inside every face $f_i$ of $G$, draw a vertex $v_i^*$.
2.  For every edge $e$ of $G$, if $e$ lies on the common boundary of faces $f_i$ and $f_j$, draw an edge $e^*$ connecting $v_i^*$ and $v_j^*$ so that it crosses $e$ exactly once and does not cross any other edge of $G$ or $G^*$. In particular, when $e$ appears only on the boundary of a single face $f_i$, draw a self-loop at $v_i^*$ that crosses $e$.

The graph $G^*$ obtained this way is called the **dual graph** of $G$.

???+ note "Theorem"
    Let $G^*$ be the dual graph of a plane graph $G$. Then $G^*$ is a connected plane graph. Moreover, $G^{**}$ is isomorphic to $G$ if and only if $G$ is connected.

??? note "Proof"
    That $G^*$ is a plane graph is guaranteed by its construction. It remains to prove that $G^*$ is connected. For any two vertices $v^*_i,v^*_j$ of $G^*$, let the line segment in the plane connecting $v^*_i$ and $v^*_j$ pass through the faces and edges of $G$ $f_i,e_{s_1},f_{s_1},\cdots,f_{s_{r-1}},e_{s_r},f_j$ in order; they correspond to the vertices and edges $v_i^*,e_{s_1}^*,v^*_{s_1},\cdots,v^*_{s_{r-1}},e^*_{s_r},v^*_j$ of the dual graph. By the construction of $G^*$, adjacent vertices and edges in this sequence are incident, so the sequence describes a walk in $G^*$. Hence $G^*$ is connected.
    
    The graph $G^{**}$ is the dual of $G^*$, so it is necessarily connected. Therefore a necessary condition for $G$ and $G^{**}$ to be isomorphic is that $G$ is connected. Next we prove that this condition is also sufficient. For this it suffices to show that, when $G$ is connected, $G$ satisfies the construction requirements of the dual graph of $G^*$. Since the edges of $G^*$ and the edges of $G$ naturally correspond, it suffices to prove that every face of $G^*$ contains exactly one vertex of $G$. For any face $f^*$ of $G^*$, let $e^*$ be an edge on its boundary; then one endpoint of the corresponding edge $e$ of $G$ must lie inside the face $f^*$, so the face $f^*$ contains at least one vertex of $G$. Since both $G^*$ and $G$ are connected, Euler's formula holds; and since $G$ and $G^*$ have the same number of edges and the number of faces of $G$ equals the number of vertices of $G^*$, the number of vertices of $G$ equals the number of faces of $G^*$. Hence every face of $G^*$ contains exactly one vertex of $G$. This proves the claim.

There are many correspondences between the structure of a plane graph and that of its dual:

-   Faces of $G$ correspond to vertices of $G^*$, edges of $G$ correspond to edges of $G^*$, and vertices of $G$ correspond to faces of $G^*$.
-   Self-loops of $G$ correspond to cut edges of $G^*$, and self-loops of $G^*$ correspond to cut edges of $G$.
-   Edge cuts of $G$ correspond to closed walks of $G^*$, and closed walks of $G^*$ correspond to edge cuts of $G$.

Note that the concept of the dual graph is defined only for a concrete plane graph and cannot be defined for an arbitrary planar graph. In fact, the duals of two isomorphic plane graphs need not be isomorphic. In other words, the duals of different planar embeddings of the same graph may differ.

???+ example "Example"
    The figure below shows two isomorphic plane graphs whose dual graphs are not isomorphic.
    
    ![](images/planar-dual-2.svg)
    
    The dual graphs are not isomorphic because the right graph has a face of degree 1, so its dual has a vertex of degree 1, while the left one does not.

Transferring a problem on a planar graph to the dual graph sometimes makes it easier to solve. A typical example is that the [minimum cut](./flow/min-cut.md) problem on a planar graph can be transformed into a [shortest path](./shortest-path.md) problem on the dual graph. Let $G$ be a planar graph with edge weights and $s,t$ two of its vertices; we want the minimum $s$-$t$ cut.

![](images/planar-dual-3.svg)

As shown in the figure, by choosing a suitable planar embedding we make $s,t$ lie on the boundary of the external face of $G$. In addition, add rays extending from $s$ and $t$ that split the external face into two parts $f_{+}$ and $f_{-}$. Based on this graph, build the dual graph and assign the edge weights to the corresponding edges of the dual. Then the paths between the vertices of the dual graph $G^*$ corresponding to the faces $f_{+}$ and $f_{-}$ (thick red line) are in one-to-one correspondence with the $s$-$t$ edge cuts of $G$ (thick black line), and both have the same weight. Thus, solving the shortest path problem in the dual graph gives the minimum $s$-$t$ cut in $G$.

A common misconception is to claim, based on the transformation above, that the minimum cut of a plane graph equals the shortest path of its dual. In fact, this applies only when there is a planar embedding of $G$ in which $s,t$ lie on a common face; it is just that in contest problems testing this topic the given graph usually has, and comes with, such a planar embedding. Here is a theorem that can be used to decide its existence.

???+ note "Theorem"
    For two vertices $s,t$ of a planar graph $G=(V,E)$, there exists a planar embedding of $G$ in which $s,t$ lie on the same face if and only if $(V,E \cup \{(s,t)\}$ is a planar graph.

??? note "Proof"
    If there is a planar embedding of $G$ in which $s,t$ lie on the same face, then an edge $(s,t)$ can be added inside that face while preserving planarity.
    
    If $(V, E \cup \{(s,t)\})$ is a planar graph, then in any of its planar embeddings $s,t$ both lie on the face containing the edge $(s,t)$. After deleting $(s,t)$, $s,t$ still lie on a common face. This proves the claim.

For example, adding the edge $(s,t)$ to the graph below yields the non-planar graph $K_5$, so no such planar embedding exists and the transformation above does not apply.

![](images/planar-st.svg)

### Further results

Of course, there are many more famous results about plane graphs. This section simply lists them without discussion.

???+ note "Four color theorem"
    Every plane graph (without self-loops) is $4$‑colorable.

???+ note "Fáry's theorem"
    A simple planar graph always has a planar embedding in which all edges are straight line segments.

???+ note "Theorem (Wood)"
    A planar graph has at most $8|V|-16$ maximal cliques.

???+ note "Theorem (Tutte)"
    Every $4$‑vertex-connected planar graph is Hamiltonian.

## Recognition

This section discusses how to decide whether a given graph is planar.

### Forbidden graphs

The most classical characterization of planar graphs is given in terms of **forbidden graphs**.

First, $K_5$ and $K_{3,3}$ are not planar.

???+ note "Theorem"
    $K_5$ and $K_{3,3}$ are not planar graphs.

??? note "Proof"
    It was shown above that a simple connected plane graph with $|V|\ge 3$ must satisfy
    
    $$
    |E| \le \dfrac{l}{l-2}(|V|-2).
    $$
    
    where $l$ is the minimum face degree. For $K_5$ we have $l=3,~|V|=5,~|E|=10$, so $K_5$ cannot be drawn as a plane graph. For $K_{3,3}$ we have $l=4,~|V|=6,~|E|=9$, so $K_{3,3}$ cannot be drawn as a plane graph.

In fact, these are exactly the minimal structures that make a graph non-planar. That is, as long as a graph does not (in a certain sense) contain these two graphs as substructures, it is certainly planar.

The first planarity criterion is Kuratowski's theorem. It uses the notion of homeomorphic graphs: if two graphs $G_1$ and $G_2$ are isomorphic, or become isomorphic after repeatedly inserting or removing vertices of degree $2$, they are called **homeomorphic**. With this, the following result can be stated:

???+ note "Kuratowski's theorem"
    A graph $G$ is planar if and only if $G$ contains no subgraph homeomorphic to $K_5$ or $K_{3,3}$.

Another related theorem is Wagner's theorem. It characterizes planar graphs using the contraction operation. Contraction means repeatedly contracting an edge of the graph into a single vertex. With this, the following result can be stated:

???+ note "Wagner's theorem"
    A graph $G$ is planar if and only if $G$ has no subgraph that can be contracted to $K_5$ or $K_{3,3}$.

That planar graphs contain no subgraphs of these kinds is relatively obvious, so the key part of both theorems is the sufficiency of the respective forbidden-graph condition. Since a subgraph homeomorphic to $K_5$ or $K_{3,3}$ can always be contracted to them, while the converse need not hold, Kuratowski's theorem provides a weaker and easier-to-check criterion for planarity.

### Planarity testing algorithms

Although it does not look easy, the planarity testing problem actually has many linear-time algorithms. However, since the implementations of these algorithms are usually rather complicated, they almost never appear in algorithm contests.

The earliest linear algorithm is the Hopcroft–Tarjan algorithm[^ht74], but its implementation is quite complex. The de Fraysseix–Ossona de Mendez–Rosenstiehl algorithm (also known as the LR planarity algorithm)[^dor06][^df08][^bra09] further improves the procedure of the Hopcroft–Tarjan algorithm and is one of the best planarity testing algorithms available. Python's NetworkX library [implements](https://github.com/networkx/networkx/blob/main/networkx/algorithms/planarity.py) this algorithm.

Another equally good algorithm is the Boyer–Myrvold algorithm[^bm99][^bm04]. It decides in linear time whether a given graph is planar. Moreover, if the graph is planar, the algorithm outputs a planar embedding; otherwise it outputs a Kuratowski subgraph (i.e. a subgraph homeomorphic to $K_5$ or $K_{3,3}$). The C++ Boost library [implements](https://www.boost.org/doc/libs/1_67_0/boost/graph/planar_detail/boyer_myrvold_impl.hpp) this algorithm.

More related algorithms can be found in the references at the end of the article.

## Special plane graphs

This section introduces several special classes of planar graphs.

### Maximal plane graphs

For a simple planar graph $G$, if adding an edge between any two non-adjacent vertices yields a graph that is no longer planar, $G$ is called a **maximal planar graph**. A planar embedding of a maximal planar graph is called a **maximal plane graph**.

???+ note "Theorem"
    A maximal planar graph $G$ is necessarily connected. Moreover, when the number of vertices is $|V|\ge 3$, $G$ has no cut edges.

??? note "Proof"
    If a planar graph $G$ is not connected, then in any of its planar embeddings we can choose two vertices from different connected components and connect them inside the external face; the resulting graph is obviously still a plane graph, which shows that $G$ is not a maximal planar graph. Hence, if $G$ is a maximal planar graph, it must be connected.
    
    If a planar graph $G$ has $|V|\ge 3$ vertices and $G$ has a cut edge $e=(u,v)$, then the graph $G - e$ obtained by deleting $e$ has exactly two connected components, and $u,v$ belong to different components. Suppose the component containing $v$ has at least two vertices. Then we can first draw the component $G_1$ containing $u$ in the plane, choose any face $f$ of $G_1$ whose boundary contains $u$, and draw the other component $G_2$ inside the face $f$. Since $G_2$ is a simple graph, the boundary of its external face is certainly not a self-loop, so there is at least one more vertex $w\neq u,v$. Connecting $v,w$ to $u$ yields a plane graph containing $G$ as a subgraph. Hence $G$ is not a maximal planar graph. Therefore a maximal planar graph with $|V|\ge 3$ vertices has no cut edges.

The structure of maximal plane graphs can be described more precisely.

???+ note "Theorem"
    A plane graph $G$ with $|V|\ge 3$ vertices is a maximal plane graph if and only if it is simple and every face has degree $3$.

??? note "Proof"
    Sufficiency of the condition is obvious. We only need to show necessity, i.e. to prove: in a maximal plane graph $G$ with $|V|\ge 3$ vertices, every face has degree $3$. Since $G$ is a connected simple plane graph with $|V|\ge 3$, all faces have degree at least $3$. So, if the claim fails, there must be a face $f$ whose boundary has length at least $4$. Since $G$ has no cut edges, this boundary can only be a cycle. Let this cycle be $v_1v_2v_3v_4\cdots v_1$. Then, if $v_1$ and $v_3$ are not adjacent, connecting $v_1$ and $v_3$ inside the face $f$ does not break planarity, contradicting the maximality of $G$; so $v_1$ and $v_3$ are adjacent; similarly, $v_2$ and $v_4$ are adjacent. But neither of the edges $(v_1,v_3)$ and $(v_2,v_4)$ appears inside the face $f$. This means both edges must lie outside the face $f$. But that is impossible: however they are drawn, these two edges must cross. Hence $G$ has no face of degree greater than $3$. This proves the claim.

???+ note "Corollary"
    For a graph $G$ with $|V|\ge 3$ vertices, the number of edges is always $|E|=3|V|-6$ and the number of faces $|F|=2|V|-4$.

Since every face of a maximal plane graph is bounded by three edges, a maximal plane graph is also called a **plane triangulation**.

### Outerplanar graphs

Let $G$ be a planar graph; if $G$ has a planar embedding $\tilde{G}$ such that all vertices of $G$ lie on the boundary of one face of $\tilde{G}$, then $G$ is called an **outerplanar graph**. This embedding is also called an outerplanar embedding or **outerplane graph**. Usually the face whose boundary passes through all vertices is drawn as the external face.

![](images/planar-outer.svg)

Every outerplanar graph is planar, but the converse need not hold. Outerplanar graphs can likewise be characterized by forbidden graphs.

???+ note "Theorem"
    A graph $G$ is outerplanar if and only if $G$ contains no subgraph homeomorphic to $K_4$ or $K_{2,3}$.

For outerplanar graphs one can likewise discuss the notion of maximal outerplanar graphs. For a simple outerplanar graph $G$, if adding an edge between any two non-adjacent vertices yields a graph that is no longer outerplanar, $G$ is called a **maximal outerplanar graph**. An outerplanar embedding of a maximal outerplanar graph is called a **maximal outerplane graph**. A maximal outerplane graph is in fact a triangulation of a polygon in the plane.

???+ note "Theorem"
    A maximal outerplane graph $G$ with $|V|\ge 3$ vertices, all of which lie on the boundary of the external face, then $G$ has exactly $|V|-2$ internal faces.

??? note "Proof"
    We use induction on $|V|$. The base case is $|V|=3$. Then $G$ is a triangle with only $1$ internal face, so the claim holds. Assume the claim holds for $|V| = k$. We now prove that it still holds for $|V| = k+1$.
    
    First, $G$ must have a vertex of degree $2$. Otherwise, every vertex would have to be connected to some third vertex besides its neighbors on the boundary of the external face. Number the vertices on the boundary of the external face in order and, for each $i = 1,2,\cdots,k+1$, define $f(i)$ as the smallest number of a vertex connected to vertex $i$ whose number is not adjacent to it. Consider the possible values of $f(i)$. First, $1 < f(1)$. Since vertex $1$ is already connected to $f(1)$, the connection between $2$ and $f(2)$ cannot cross the edge $(1,f(1))$, so necessarily $1 < 2 < f(2) < f(1)$. Similarly, $2 < 3 < f(3) < f(2)$. Since there are only finitely many vertices, this shrinking process must stop after finitely many steps. Let $i^*$ be the largest number $i$ satisfying $1 < \cdots < i-1 < i < f(i) < f(i-1) < \cdots < f(1)$. Then, since the vertices $i^*$ and $f(i^*)$ are not adjacent, necessarily $i^* < i^* + 1 < f(i^*)$. Repeating the previous argument, we should still have $i^* < i^*+1 < f(i^*+1) < f(i^*)$, contradicting the maximality of $i^*$. This contradiction shows that $G$ must have a vertex of degree $2$.
    
    Let $v$ be such a vertex of degree $2$. Deleting this vertex from $G$ gives an outerplane graph $G-v$ with $k$ vertices. It must be a maximal outerplane graph, since otherwise any legal way of adding an edge to it would also apply to $G$. By the induction hypothesis $G-v$ has exactly $k-2$ internal faces, and deleting the vertex $v$ removed exactly one internal face of $G$. Hence $G$ has $k-1$ internal faces. This proves the claim.

???+ note "Theorem"
    An outerplane graph $G$ with $|V|\ge 3$ vertices, all of which lie on the boundary of the external face, then $G$ is a maximal outerplane graph if and only if the boundary of the external face of $G$ is a cycle of length $|V|$ and the boundaries of all internal faces are cycles of length $3$.

??? note "Proof"
    Sufficiency is obvious. Indeed, consider connecting two non-adjacent vertices on the boundary of the external face. If the connection is made inside the external face, then not all vertices can lie on the boundary of a single face; otherwise, the connection must cross the boundary of some internal face.
    
    Next we prove necessity. Suppose the boundary of the external face $v_1v_2v_3\cdots v_nv_1~(n = |V|)$ of $G$ is not a cycle. Then it passes through some vertex more than once, i.e. there exist $i\neq j$ with $i-j\neq\pm 1\pmod{n}$ such that $v_i=v_j$. Without loss of generality let $1 < i < j < n$. Then the edges incident to $v_{i-1}$ can only lie inside the bounded region enclosed by the closed walk $v_jv_{j+1}\cdots v_nv_1\cdots v_{i-1}v_i$, and the edges incident to $v_{i+1}$ can only lie inside the bounded region enclosed by the closed walk $v_iv_{i+1}\cdots v_{j-1}v_{j}$, so $v_{i-1}$ and $v_{i+1}$ cannot be adjacent. We can add an edge $e$ connecting $v_{i-1}$ and $v_{i+1}$ inside the external face, obtaining the graph $G+e$. This is obviously still a plane graph, and the boundary of its external face contains all vertices. This contradicts the maximal outerplanarity of $G$. Hence the external face of $G$ must be a cycle of length $|V|$. The reason why the boundaries of the internal faces of $G$ are cycles of length $3$ is the same as for maximal plane graphs and is not repeated here.

???+ note "Corollary"
    For a maximal outerplane graph $G$ with $|V|\ge 3$ vertices:
    
    1.  $|E|=2|V|-3$.
    2.  $G$ has at least $3$ vertices of degree at most $3$, and at least $2$ vertices of degree $2$.
    3.  The vertex connectivity of $G$ is $2$.

## Exercises

-   [Luogu P3209 \[HNOI2010\] Planarity testing](https://www.luogu.com.cn/problem/P3209)
-   [Luogu P3249 \[HNOI2016\] Mining area](https://www.luogu.com.cn/problem/P3249)
-   [Luogu P4001 \[ICPC-Beijing 2006\] Wolf catches rabbits](https://www.luogu.com.cn/problem/P4001)
-   [Luogu P4073 \[WC2013\] Planar graph](https://www.luogu.com.cn/problem/P4073)
-   [Luogu P7295 \[USACO21JAN\] Paint by Letters P](https://www.luogu.com.cn/problem/P7295)

## References and notes

-   [Planar graph - Wikipedia](https://en.wikipedia.org/wiki/Planar_graph)
-   [Planarity testing - Wikipedia](https://en.wikipedia.org/wiki/Planarity_testing)
-   Bondy, John Adrian, and Uppaluri Siva Ramachandra Murty. Graph theory with applications. Vol. 290. London: Macmillan, 1976.
-   Diestel, Reinhard. Graph theory. Vol. 173. Springer Nature, 2025.
-   Patrignani, Maurizio. "Planarity Testing and Embedding." (2013): 1-42.

[^face-2]: But this is not the only possibility. Two nested self-loops also form a face of degree 2. Moreover, having a face of degree 2 does not necessarily mean the graph is not simple; for example, in a graph with a single edge, the only face (the external face) also has degree 2.

[^ht74]: Hopcroft, John, and Robert Tarjan. "Efficient planarity testing." Journal of the ACM (JACM) 21, no. 4 (1974): 549-568.

[^dor06]: De Fraysseix, Hubert, Patrice Ossona De Mendez, and Pierre Rosenstiehl. "Trémaux trees and planarity." International Journal of Foundations of Computer Science 17, no. 05 (2006): 1017-1029.

[^df08]: De Fraysseix, Hubert. "Trémaux trees and planarity." Electronic Notes in Discrete Mathematics 31 (2008): 169-180.

[^bra09]: Brandes, Ulrik. "The left-right planarity test." Manuscript submitted for publication 3 (2009).

[^bm99]: Boyer, John M., and Wendy J. Myrvold. "Stop Minding Your p's and q's: A Simplified O (n) Planar Embedding Algorithm." In SODA, vol. 99, pp. 140-146. 1999.

[^bm04]: Boyer, John M., and Wendy J. Myrvold. "Simplified o (n) planarity by edge addition." Graph Algorithms and Applications 5 (2006): 241.
