---
title: Maximum bipartite matching
---

Prerequisites: [bipartite graph](../bi-graph.md), [graph matching](./graph-match.md)

## Introduction

This article discusses the maximum matching problem in a bipartite graph $G=(X,Y,E)$.

A typical real-life example of bipartite matching is pairing men and women. Suppose there are some men ($X$) and women ($Y$); every person can be paired at most once, and the allowed pairs are restricted by some list ($E$). The task of a maximum bipartite matching algorithm is to find, under these restrictions, the largest number of pairs, so that as many people as possible are successfully paired.

???+ info "Note"
    This article assumes that a partition (coloring) of the vertex set $V$ of the bipartite graph is known: $V=X\cup Y$. If the partition of the vertex set $V$ is not known in advance, it can be found by the [bipartite graph coloring algorithm](../bi-graph.md#判定) in $O(|V|+|E|)$ time.

## Kuhn's algorithm

Kuhn's algorithm is a direct application of [Berge's lemma](./graph-match.md#berge-引理). It is also a part of the [Hungarian algorithm](./bigraph-weight-match.md#hungarian-algorithm-kuhnmunkres-algorithm).

### Procedure

To find a maximum matching, the algorithm enumerates all vertices in turn, tries to find an augmenting path starting at each of them, and augments along it. Since the length of an augmenting path is always odd, in a bipartite graph its endpoints must lie in different parts. This means that it suffices to consider augmenting paths starting in the left part.

To look for an augmenting path, we can orient the bipartite graph according to the current matching $M$. An augmenting path (or any alternating path) starting at an unmatched left vertex can only go from a left vertex to a right vertex along a non-matching edge, and from a right vertex to a left vertex along a matching edge. Therefore we can let all non-matching edges point to right vertices and all matching edges point to left vertices. Finding an augmenting path then becomes finding a simple path in the directed graph from some unmatched left vertex to some unmatched right vertex. This problem is easily solved by [DFS](../dfs.md) or [BFS](../bfs.md) in $O(|E|)$ time.

![](images/bigraph-match-1.svg)

(In the figure, dark vertices are matched, light vertices are unmatched, red edges are matching edges, black edges are non-matching edges, and arrows show the orientation corresponding to the current matching. One can see that the path $1\rightarrow 8\rightarrow 3\rightarrow 11\rightarrow 6\rightarrow 12$ is an augmenting path with respect to the current matching.)

At the start of the algorithm all edges point to right vertices. Each time an augmenting path is found, all edges along it have to be reversed, to indicate that their matching status has flipped. When the algorithm finishes, all edges pointing to left vertices are matching edges.

Since at most $O(|V|)$ left vertices have to be enumerated, [each once](./graph-match.md#berge-引理), the total time complexity of the algorithm is $O(|V||E|)$.

### Optimizations

There are some simple tricks that improve the constant factor of Kuhn's algorithm:

1.  Kuhn's algorithm is based on Berge's lemma, which does not require the left and right parts of the bipartite graph to be given in advance. Hence Kuhn's algorithm also runs correctly when the two parts are not explicitly separated, as long as the graph itself is bipartite. However, it is usually more efficient to color the bipartite graph first and determine its left and right parts.
2.  Since the time complexity of Kuhn's algorithm as described above is actually $O(|X||E|)$, we can choose the smaller of the two parts as the left part $X$.
3.  When looking for augmenting paths, the marks used to avoid repeated visits need not be cleared before every DFS. Before clearing the marks, we can try to find an augmenting path for every unmatched left vertex. In one such round every edge is visited at most once, so the complexity is still $O(|E|)$; but one round may find several augmenting paths, so the total number of rounds $k$ does not exceed $|M|+1$, where $M$ is a maximum matching. Accordingly, the overall complexity drops to $O(k|E|)$.
4.  When looking for an augmenting path, prefer unmatched right vertices, since that means a shorter augmenting path.
5.  Since Berge's lemma does not require the initial matching to be empty, at the start of Kuhn's algorithm we can randomly pick some pairwise disjoint edges as the initial matching, to reduce the number of later searches. If optimization 3 is applied, this optimization can be ignored.

Although the worst-case complexity is still $O(|V||E|)$, a well-optimized Kuhn's algorithm is not inefficient. Nevertheless, to prevent particular test data from forcing the worst case, the order of edges or vertices should be shuffled randomly before matching.

### Reference implementation

In the implementation there is no need to actually maintain the orientation; it suffices to store, for each vertex, the vertex it is matched to.

??? example "Template problem [Library Checker - Matching on Bipartite Graph](https://judge.yosupo.jp/problem/bipartitematching)"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_1.cpp"
    ```

## Hopcroft–Karp algorithm

The Hopcroft–Karp algorithm further optimizes the way Kuhn's algorithm searches for augmenting paths, reducing the total number of rounds to $O(|V|^{1/2})$ and thereby achieving a time complexity of $O(|V|^{1/2}|E|)$. This algorithm is in fact a special case of [Dinic's algorithm](../flow/max-flow.md#dinic-算法).

### Procedure

The algorithm still searches for augmenting paths, but to finish the matching in fewer rounds, it applies the following strategy in every round:

1.  Orient matching edges toward left vertices and non-matching edges toward right vertices.
2.  Run a BFS on the directed graph from all unmatched left vertices, recording for every visited vertex the layer $d(v)$ it lies in, until an unmatched right vertex appears in some layer. If the BFS finishes without finding an unmatched right vertex, the current matching is already maximum.
3.  Run a DFS from each unmatched left vertex in turn, find an augmenting path and augment along it. The DFS only extends along edges whose layers are consecutive and strictly increasing (i.e. $d(v') = d(v) + 1$), and only visits vertices not yet visited in this round's DFS. In particular, the DFS never visits vertices that the preceding BFS did not reach.

In the terminology of network flows, step 2 builds a level graph, and step 3 finds a blocking flow in the level graph. A level graph is one in which every edge necessarily goes from one layer to the next; a blocking flow, in the present context, is a maximal set of augmenting paths that pairwise share no vertices. The set of augmenting paths obtained in step 3 is necessarily maximal: otherwise there would be a new augmenting path, which should already have been found when its starting vertex was enumerated.

Compared with Kuhn's algorithm above, the key change in the Hopcroft–Karp algorithm is the added step of building the level graph before finding the blocking flow. Running the DFS on the level graph amounts to forcing the algorithm to always reach every vertex along a shortest path. The benefit is that the lengths of the augmenting paths found in different rounds of the algorithm are strictly increasing. Moreover, it can be proved that until a maximum matching is found, the length of the augmenting paths increases at most $3|M|^{1/2}$ times, where $|M|$ is the size of a maximum matching. This bounds the total number of augmentation rounds by $O(|M|^{1/2})$, giving a time complexity of $O(|M|^{1/2}|E|)$. Since $2|M|\le |V|$, the time complexity can also be written with the looser upper bound $O(|V|^{1/2}|E|)$.

??? note "Proof"
    First we show that the lengths of the augmenting paths found in different rounds of the algorithm are strictly increasing.
    
    Suppose the BFS in the current round extends $\ell$ layers forward. Since the unmatched right vertices found by the BFS all lie in the same layer, every augmenting path the DFS of this round can find has length $\ell$. We need to prove that after augmenting along the set of augmenting paths $\{P_i\}$ found in this round, the reoriented directed graph no longer contains an augmenting path of length at most $\ell$.
    
    In fact, if $P$ is a shortest augmenting path with respect to $M$ and $P'$ is an augmenting path with respect to $M\oplus P$, then $|P'|\ge |P| + 2|P\cap P'|$. This is because $N=(M\oplus P)\oplus P'$ is augmented twice relative to $M$, so, as in the [proof of Berge's lemma](./graph-match.md#berge-引理), one can show that the symmetric difference $M\oplus N=P\oplus P'$ contains at least two disjoint augmenting paths $P_1$ and $P_2$ with respect to $M$. By the minimality of $P$,
    
    $$
    2|P|\le |P_1|+|P_2|\le |P\oplus P'| = |P| + |P'| - 2|P\cap P'|.
    $$
    
    This shows $|P'|\ge |P| + 2|P\cap P'|$. Therefore, if after adding the augmenting paths $\{P_i\}$ a new augmenting path $P'$ is still as long as they are, it must be disjoint from each of them, contradicting the maximality of $\{P_i\}$. This contradiction shows that after augmenting along the blocking flow, a new augmenting path must be strictly longer.
    
    Finally, we need to show that the length of the augmenting paths increases at most $3|M|^{1/2}$ times.
    
    Let $p=\lfloor|M|^{1/2}\rfloor$. After the first $p$ rounds, the remaining augmenting paths have length at least $|M|^{1/2}$. Let the current matching be $M_p$; then, similarly to the above, one can show that the graph $(V,M\oplus M_p)$ contains $|M|-|M_p|$ vertex-disjoint augmenting paths with respect to $M_p$. Each of them uses at least $|M|^{1/2}/2$ matching edges of $M$, so there are at most $2|M|^{1/2}$ of them, i.e. $|M|-|M_p|\le 2|M|^{1/2}$. This means that starting from $M_p$ at most $2|M|^{1/2}$ more augmentations are possible, which likewise means the algorithm performs at most $2|M|^{1/2}$ more augmentation rounds. Hence the length of the augmenting paths increases at most $3|M|^{1/2}$ times in total.

This is only an estimate of the worst-case complexity of the Hopcroft–Karp algorithm. In fact, on random graphs the time complexity of the Hopcroft–Karp algorithm is $O(|E|\log |V|)$ with high probability[^hk-comp-ref].

### Optimization

When building the level graph, the Hopcroft–Karp algorithm, like the usual Dinic's algorithm, stops as soon as it reaches an unmatched right vertex. For the bipartite matching problem alone, however, this is unnecessary. Moreover, because the BFS stops too early, it limits the range of the subsequent DFS, so only a limited number of augmenting paths is found per round, which slows down the whole matching. On some graphs it is even less efficient than an optimized Kuhn's algorithm. A simple improvement, therefore, is not to stop the BFS early but to build the level graph for all reachable vertices.

??? note "Proof of correctness"
    In the optimized algorithm, the augmenting paths in the blocking flow no longer have the same length, so the complexity proof above no longer holds. It can be shown, however, that by constructing an auxiliary graph for each round of the algorithm, the conclusion that the length of the shortest augmenting path strictly increases can still be established, which guarantees that the worst-case complexity remains correct.
    
    Let the bipartite graph be $G=(X,Y,E)$ and the current matching $M$. Let $W\subseteq Y$ be the set of unmatched right vertices reachable by the BFS, and let $d(y)$ be the length of the shortest augmenting path reaching $y\in W$. Let $d_\text{max} = \max_{y\in W}d(y)$. For every $y\in W$ we can attach a new chain starting at $y$ of length $d_\text{max} - d(y)$, marking the new vertices alternately as left and right vertices and the new edges alternately as matching and non-matching edges. Let the resulting graph be $G'=(X',Y',E')$ with matching $M'$; its shortest augmenting path has length $d_\text{max}$. Then there is a bijection between the augmenting paths with respect to $M$ that can be found in $G$ along the level graph – that is, the shortest augmenting paths to the corresponding vertices – and the globally shortest augmenting paths with respect to $M'$ in $G'$. Hence finding a blocking flow in the level graph of $G$ and augmenting along it is equivalent to finding a blocking flow in the level graph of $G'$ and augmenting along it. By the proof above, after augmenting, $G'$ no longer contains an augmenting path of length $d_\text{max}$. Therefore $G$ no longer contains an augmenting path of length $d_\text{min}=\min_{y\in W} d(y)$ either: such a path, extended by the newly attached alternating path, would necessarily correspond to an augmenting path of length $d_\text{max}$ in $G'$. This again yields the conclusion that the length of the shortest augmenting path strictly increases between rounds of the algorithm. Hence the overall complexity is still $O(|M|^{1/2}|E|)$.

### Reference implementation

??? example "Template problem [Library Checker - Matching on Bipartite Graph](https://judge.yosupo.jp/problem/bipartitematching)"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_2.cpp"
    ```

## Reduction to maximum flow

The maximum bipartite matching problem can be reduced to the maximum flow problem.

![](images/bigraph-match-2.svg)

As shown in the figure, add two vertices serving as the source and the sink. From the source, add an edge to every left vertex; from every right vertex, add an edge to the sink; and for every undirected edge of the bipartite graph, add an edge directed from the left vertex to the right vertex. All edges have capacity $1$. Every integral flow in the resulting directed graph corresponds one-to-one to a matching in the bipartite graph, and the value of the flow equals the size of the corresponding matching. Therefore finding a maximum bipartite matching is equivalent to finding a maximum flow in the corresponding directed graph.

Any algorithm that solves the maximum flow problem can be used to solve the maximum bipartite matching problem. It is easy to see that Kuhn's algorithm and the Hopcroft–Karp algorithm are special cases of the corresponding maximum flow algorithms. Likewise, the [push-relabel algorithm](../flow/max-flow.md#push-relabel-预流推进算法) and others can also be used for maximum bipartite matching. Note, however, that any maximum flow algorithm, when applied to maximum bipartite matching, needs targeted optimizations to avoid an excessive constant factor.

### Linear programming formulation

As with other maximum flow problems, the maximum matching problem in a bipartite graph $G=(X,Y,E)$ (write $V=X\cup Y$) can be written as a linear program. If $x_e\in\{0,1\}$ indicates whether edge $e$ belongs to the matching, we obtain the following linear program:

$$
\begin{aligned}
\max_{\{x_e\}}\;& \sum_{e\in E}x_e \\
\text{subject to } & \sum_{e\sim v} x_{e} \le 1,~\forall v\in V,\\
& x_e\ge 0,~\forall e\in E.
\end{aligned}
$$

Here $e\sim v$ denotes incidence, i.e. vertex $v$ is one of the endpoints of edge $e$. Apart from non-negativity, the constraints require that every vertex $v\in V$ is incident to at most one chosen edge, which is exactly the definition of a matching. Hence all matchings correspond to certain integer points of the feasible region of this linear program.

The converse does not hold. In a feasible solution $x_e$ may be fractional, which does not represent any actual matching. Nevertheless, for a bipartite graph $G$ all extreme points of the above linear program are integral. This means the optimal value of the objective is always attained at an integer point, so non-integer cases need not be considered. This property does not hold for general graphs, so for general graphs the above linear program is not equivalent to the maximum matching problem.

The dual of this linear program can be written as follows:

$$
\begin{aligned}
\min_{\{y_v\}}\;& \sum_{v\in V}y_v \\
\text{subject to } & y_u+y_v \ge 1,~\forall (u,v)\in E,\\
& y_v\ge 0,~\forall v\in V.
\end{aligned}
$$

As we will see shortly, this is exactly the minimum vertex cover problem in bipartite graphs.

## Dulmage–Mendelsohn decomposition

Using a maximum matching of a bipartite graph, the vertices can be partitioned into several pairwise disjoint subsets that completely characterize the distribution and structure of all maximum matchings of the graph. This is the Dulmage–Mendelsohn decomposition. In competitive programming, this decomposition can be used to identify the essential vertices and essential edges of maximum matchings, and thereby to decide whether the maximum matching is unique or to solve games on bipartite graphs and similar problems.

### Construction

Let $M$ be a maximum matching of the bipartite graph $G=(X,Y,E)$.

![](images/bigraph-match-4.svg)

As shown in the figure, define the following three subsets of all vertices $V=X\cup Y$:

-   even-reachable vertices $\mathcal E$: all vertices reachable from some unmatched vertex along an alternating path of even length;
-   odd-reachable vertices $\mathcal O$: all vertices reachable from some unmatched vertex along an alternating path of odd length;
-   unreachable vertices $\mathcal U$: all vertices not reachable from any unmatched vertex along an alternating path.

It can be proved that the three vertex sets $\mathcal E,\mathcal O,\mathcal U$ obtained this way have the following properties:

???+ note "Properties"
    1.  The sets $\mathcal E,\mathcal O,\mathcal U$ form a partition of the vertex set, and this partition does not depend on the choice of the maximum matching $M$.
    2.  Every maximum matching of $G$ contains a perfect matching among the vertices of $\mathcal U$ and matches every vertex of $\mathcal O$ to a vertex of $\mathcal E$. In other words, the size of a maximum matching of $G$ equals $|\mathcal O|+|\mathcal U|/2$.
    3.  $G$ contains no edge joining a vertex of $\mathcal E$ to a vertex of $\mathcal E\cup\mathcal U$.

??? note "Proof"
    1.  By definition, $\mathcal U$ and $\mathcal E\cup\mathcal O$ are disjoint. It remains to prove that $\mathcal E$ and $\mathcal O$ are disjoint. Suppose not: for a vertex $v\in\mathcal E\cap\mathcal O$ there is an alternating path of even length from an unmatched vertex $a$ to $v$ and an alternating path of odd length from an unmatched vertex $b$ to $v$. Since $G$ is bipartite, $a\neq b$, and the edges by which the two paths reach $v$ are a matching edge and a non-matching edge, respectively. Joining the two paths therefore yields an alternating path from $a$ through $v$ to $b$. This is an augmenting path, contradicting that $M$ is a maximum matching. Hence $\mathcal E\cap\mathcal O=\varnothing$.
    
        Let $M'$ be a maximum matching different from $M$. Repeating the [proof of Berge's lemma](./graph-match.md#berge-引理) shows that $M'\oplus M$ consists only of paths of even length and even cycles. Starting from the maximum matching $M$, we can flip the edges in these components (paths and cycles) one by one (swapping matching and non-matching edges) to obtain the maximum matching $M'$. When flipping an even cycle, unmatched vertices remain unmatched and the parity of the lengths of alternating paths from them does not change; when flipping a path of even length, the two endpoints of the path swap their matching status, but the parity of the length of the path from either of them to any vertex on the path is the same. Hence the sets $\mathcal E,\mathcal O,\mathcal U$ remain unchanged throughout the flipping. This shows that the decomposition does not depend on the choice of the maximum matching $M$.
    2.  If a matching edge appears on some alternating path from an unmatched vertex $v$, the parities of the distances of its two endpoints from $v$ must differ, so they belong to $\mathcal E$ and $\mathcal O$ respectively; otherwise both of its endpoints must be in $\mathcal U$. This shows that the matching edges of a maximum matching must be $\mathcal E\mathcal O$ edges or $\mathcal U\mathcal U$ edges. Conversely, an unmatched vertex is reachable from itself by an alternating path of length zero, so it appears only in $\mathcal E$; this shows that all vertices in $\mathcal O$ and $\mathcal U$ are matched. A simple count shows that the size of a maximum matching is $|\mathcal O|+|\mathcal U|/2$.
    3.  By definition, any vertex $a\in\mathcal E$ is reachable from an unmatched vertex $v$ along an alternating path of even length; in other words, a vertex in $\mathcal E$ is either unmatched or the alternating path $P$ reaching it ends with a matching edge. If $G$ contained an edge joining $a$ to some vertex $b\in\mathcal E\cup\mathcal U$, then by the previous discussion this edge would have to be a non-matching edge, and the alternating path $P$ could be extended along it. This would mean that vertex $b$ also belongs to $\mathcal O$, contradicting the first property. Hence $G$ contains no edge joining a vertex of $\mathcal E$ to a vertex of $\mathcal E\cup\mathcal U$.

The resulting decomposition of the vertex set $V=\mathcal E\cup\mathcal O\cup\mathcal U$ is called the **Dulmage–Mendelsohn decomposition**. After a maximum matching has been found by the algorithms described above, the Dulmage–Mendelsohn decomposition can be computed by BFS in $O(|V|+|E|)$ time.

### Essential vertices of maximum matchings

If a vertex $v$ is matched in every maximum matching of the bipartite graph $G$, it is called an essential vertex of maximum matchings. The following result shows: a vertex is essential if and only if, in some maximum matching, there is no alternating path of even length from an unmatched vertex to that vertex.

???+ note "Theorem"
    Let $V=\mathcal E\cup\mathcal O\cup\mathcal U$ be the Dulmage–Mendelsohn decomposition of the bipartite graph $G=(X,Y,E)$. Then a vertex $v\in V$ is essential if and only if $v\in\mathcal O\cup \mathcal U$.

??? note "Proof"
    By the properties of the Dulmage–Mendelsohn decomposition, in every maximum matching of $G$ the vertices of $\mathcal O$ and $\mathcal U$ are necessarily matched. Hence the vertices of $\mathcal O\cup \mathcal U$ are necessarily essential. It remains to show that $\mathcal E$ contains no essential vertex. If in a maximum matching $M$ a vertex $a\in\mathcal E$ were essential, there would be an alternating path $P$ of even length joining $a$ to some unmatched vertex $b\in\mathcal E$. Flipping all edges on this path yields the maximum matching $M\oplus P$, in which $a$ is unmatched. Hence $\mathcal E$ contains no essential vertex.

Therefore, to find the essential vertices of maximum matchings, it suffices to compute the Dulmage–Mendelsohn decomposition.

### Essential edges of maximum matchings

Similarly, if an edge $e$ is a matching edge in every maximum matching of the bipartite graph $G$, it is called an essential edge of maximum matchings. The maximum matching of a bipartite graph is unique if and only if, in one of its maximum matchings, all matching edges are essential.

???+ note "Theorem"
    Let $V=\mathcal E\cup\mathcal O\cup\mathcal U$ be the Dulmage–Mendelsohn decomposition of the bipartite graph $G=(X,Y,E)$ and let $M$ be one of its maximum matchings. Then an edge $e\in E$ is essential if and only if both endpoints of $e$ are in $\mathcal U$, $e$ is a matching edge of $M$, and there is no alternating cycle with respect to $M$ containing $e$.

??? note "Proof"
    The endpoints of an essential edge must be essential vertices. By the properties of the Dulmage–Mendelsohn decomposition, the edges of a maximum matching can only be $\mathcal E\mathcal O$ edges or $\mathcal U\mathcal U$ edges. But $\mathcal E$ contains no essential vertex, so an essential edge can only be a $\mathcal U\mathcal U$ edge. Of course, an essential edge must also be a matching edge of $M$. Let $e\in M$ be a $\mathcal U\mathcal U$ edge. It is not essential if and only if there is another maximum matching $M'\neq M$ with $e\in M\oplus M'$. Repeating the [proof of Berge's lemma](./graph-match.md#berge-引理) shows that $M'\oplus M$ consists only of paths of even length and even cycles. One endpoint of each such path is a vertex unmatched in $M$, so no vertex on such a path is in $\mathcal U$, contradicting the choice of $e$. Hence $e$ can only appear in an even cycle. Therefore a $\mathcal U\mathcal U$ edge $e\in M$ is not essential if and only if there is an alternating cycle with respect to $M$ containing $e$. This is what we wanted to prove.

Hence, to find the essential edges of maximum matchings, proceed as follows:

1.  find a maximum matching $M$ of $G$;
2.  orient the edges of $G$ according to $M$, obtaining the directed graph $G_M$;
3.  run a BFS to find the set $\mathcal U$ of the Dulmage–Mendelsohn decomposition, i.e. the set of vertices not reachable from unmatched vertices along alternating paths;
4.  use [Tarjan's algorithm](../scc.md#tarjan-算法) to find all strongly connected components of the directed graph $G_M$;
5.  go through the edges of the matching $M$: if both endpoints of an edge are in $\mathcal U$ but not in the same strongly connected component, it is an essential edge.

Once a maximum matching is available, the time complexity of the remaining steps is $O(|V|+|E|)$.

## Related problems

Maximum bipartite matching algorithms can be used to solve other combinatorial optimization problems.

### Minimum vertex cover in bipartite graphs

The minimum vertex cover problem asks to choose the fewest vertices in an undirected graph such that every edge has at least one chosen endpoint.

The minimum vertex cover problem for general graphs is NP-hard, but for bipartite graphs Kőnig's theorem shows that it reduces to the maximum matching problem and can therefore be solved efficiently. The proof of the theorem also gives a construction of the minimum vertex cover.

???+ note "Kőnig's theorem"
    In a bipartite graph, the number of vertices in a minimum vertex cover equals the number of edges in a maximum matching.

??? note "Proof"
    Let $M$ be a maximum matching of the bipartite graph $G=(X,Y,E)$. Let $U$ be the set of unmatched left vertices, and let $Z$ be the set of vertices of $G$ reachable from vertices of $U$ along some alternating path. Then the vertex set $C=(X\setminus Z)\cup(Y\cap Z)$ is the desired minimum vertex cover.
    
    ![](images/bigraph-match-3.svg)
    
    First, $C$ is a vertex cover. Suppose not: there is an edge $(u,v)\in E$ with $u\in X\cap Z$ and $v\in Y\setminus Z$. Let $P_u$ be an alternating path reaching $u$. If $(u,v)$ is a matching edge, then the last edge of $P_u$ is $(v,u)$, contradicting $v\notin Z$; if $(u,v)$ is not a matching edge, then $P_u$ can be extended along $(u,v)$ to an alternating path reaching $v$, again contradicting $v\notin Z$. These contradictions show that every edge has at least one endpoint in $C$, so $C$ is a vertex cover.
    
    Next, we need to show that $C$ is a minimum vertex cover. To cover all edges of the maximum matching $M$, any vertex cover needs at least $|M|$ vertices. Hence it suffices to prove $|C|=|M|$, from which it follows that $C$ is a minimum vertex cover. This is equivalent to proving that, apart from one endpoint of each matching edge, $C$ contains no other vertices; that is, $C$ contains no unmatched vertex. Suppose not: there is an unmatched vertex $v\in C$. If $v\in X$, then necessarily $v\in U\subseteq Z$, contradicting the construction of $C$; if $v\in Y$, then an alternating path reaching $v$ is an augmenting path with respect to $M$, which by Berge's lemma contradicts that $M$ is a maximum matching. These contradictions show that no such unmatched vertex exists, and hence $C$ is a minimum vertex cover.

From the network flow point of view, the minimum vertex cover problem is the minimum cut problem: choosing a left vertex corresponds to cutting the edge between it and the source, and choosing a right vertex corresponds to cutting the edge between it and the sink. From the linear programming point of view, the minimum vertex cover problem is the dual of the maximum matching problem. Hence Kőnig's theorem can be seen as a special case of the [max-flow min-cut theorem](../flow/max-flow.md#最大流最小割定理), or more generally, a special case of the strong duality theorem of linear programming.

### Maximum independent set in bipartite graphs

The maximum independent set problem asks to choose the most vertices in an undirected graph such that no two of them are adjacent.

For general graphs the following theorem holds:

???+ note "Theorem"
    In a graph $G=(V,E)$, a vertex set $C\subseteq V$ is a vertex cover if and only if its complement $V\setminus C$ is an independent set.

??? note "Proof"
    The set $C$ is a vertex cover iff for every edge $e$ in $E$ at least one of its two endpoints lies in $C$, iff no edge in $E$ has both endpoints in $V\setminus C$, iff $V\setminus C$ is an independent set.

???+ note "Corollary"
    In a graph $G=(V,E)$, the sizes of a minimum vertex cover and a maximum independent set sum to the number of vertices.

Hence, like the minimum vertex cover problem, the maximum independent set problem is NP-hard for general graphs, but for bipartite graphs it reduces to the maximum matching problem and can be solved efficiently.

### Minimum path cover in directed acyclic graphs

The minimum path cover problem asks to choose the fewest simple paths in a directed graph such that every vertex appears in exactly one path.

The minimum path cover problem on general directed graphs is NP-hard, but for directed acyclic graphs it reduces to maximum bipartite matching. For a directed acyclic graph $G=(V,E)$, construct the bipartite graph $G'=(V^\text{in},V^\text{out},E')$ as follows:

-   For every vertex $v\in V$, create an in-vertex $v^\text{in}$ and an out-vertex $v^\text{out}$. Let the sets of all in-vertices and all out-vertices be $V^\text{in}$ and $V^\text{out}$. They become the left and right parts of the new graph, respectively.
-   For every directed edge $(u,v)\in E$, create the undirected edge $(u^\text{out},v^\text{in})$. The set of all these undirected edges is $E'$.

Then we have the following:

???+ note "Theorem"
    The size of a minimum path cover of the directed acyclic graph $G=(V,E)$ and the size of a maximum matching of the corresponding bipartite graph $G'=(V^\text{in},V^\text{out},E')$ sum to the number of vertices.

??? note "Proof"
    Every matching $M'$ of the bipartite graph $G'$ corresponds to a subgraph $F$ of $G$ in which every vertex has in-degree and out-degree at most one; that is, $F$ is a collection of pairwise disjoint paths or cycles in the directed graph $G$. But we assumed $G$ has no cycles, so $F$ contains only disjoint paths. Conversely, for every such subgraph $F$ a corresponding matching can be constructed. Since the size of the matching $M'$ equals the number of vertices minus the number of paths in $F$, the minimum path cover problem of $G$ corresponds to the maximum matching problem of $G'$.

The proof is constructive, so a corresponding minimum path cover is easily built from the maximum matching obtained. Moreover, the construction shows that for general directed graphs this reduction no longer holds, precisely because a matching in the bipartite graph may correspond to a cycle in the directed graph.

In particular, for a set $X$ with a partial order $P$ on it, we can build the directed acyclic graph $G=(X,P)$. By [Dilworth's theorem](../../math/order-theory.md#dilworth-定理与-mirsky-定理), the size of a minimum path cover of $G$ then equals the length of its longest antichain, i.e. the width of the poset $(X,P)$. Hence this section actually gives an efficient way to compute the width of an arbitrary poset.

## Example problems

The hard part of applying bipartite matching is building the graph; this section shows graph-building techniques through some example problems.

???+ example "[Luogu P1129 矩阵游戏](https://www.luogu.com.cn/problem/P1129)"
    Given a square 01-matrix, each move swaps two rows or two columns. Can the swaps make the main diagonal (top-left to bottom-right) consist entirely of ones?

??? note "Solution"
    Observe that if there are $n$ ones no two of which share a row or a column, then a solution must exist; otherwise none exists. The problem becomes whether these $n$ ones can be found.
    
    For a single $1$, choosing it in the final solution means its row and column are occupied. So we build a bipartite graph with $n$ left vertices and $n$ right vertices, where for each element equal to $1$ we add an edge joining the left vertex of its row and the right vertex of its column. Then we run bipartite matching.

??? note "Code"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_3.cpp"
    ```

???+ example "[Gym 104427B Lawyers](https://codeforces.com/gym/104427/problem/B)"
    There are $n$ lawyers, all accused of fraud. They need to defend each other so that every lawyer is acquitted. Among these $n$ lawyers there are $m$ trust relations; a trust relation $(a, b)$ means $a$ can defend $b$. Any lawyer who is defended will be acquitted, with one exception: if $a$ and $b$ defend each other, both will be found guilty.
    
    Determine whether every lawyer can be acquitted.

??? note "Solution"
    For every **unordered pair** $(a, b)$, when $a$ can defend $b$, add an edge from this unordered pair to $b$, and vice versa.
    
    Keeping only the pairs $(a, b)$ that are joined by an edge, the problem becomes a maximum bipartite matching with $m$ left vertices and $n$ right vertices.

??? note "Code"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_4.cpp"
    ```

???+ example "[Codeforces 1404E Bricks](https://codeforces.com/problemset/problem/1404/E)"
    Exactly cover an $n \times m$ grid with bricks of size $1 \times x$; bricks may be rotated, and some cells must not be covered.

??? note "Solution"
    Consider how the final arrangement is formed:
    
    First cover every coverable cell with a $1 \times 1$ brick. A $1 \times x$ brick can be formed by successively "row-merging" $x$ consecutive $1 \times 1$ bricks in the same row. Likewise, an $x \times 1$ brick can be formed by successively "column-merging" $x$ consecutive $1 \times 1$ bricks in the same column.
    
    Clearly a row merge and a column merge cannot involve the same brick, and the more merges there are, the fewer bricks. So we take row merges as left vertices, column merges as right vertices, and the conflicts above as edges, and build a bipartite graph. The original problem thus becomes a maximum independent set problem in a bipartite graph.

??? note "Code"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_5.cpp"
    ```

???+ example "[Codeforces 1139E - Maximize Mex](https://codeforces.com/problemset/problem/1139/E)"
    There are $m$ multisets with $n$ elements in total. Each time, one element is deleted from some multiset, and then we are asked: "choosing at most one element from each multiset, what is the maximum achievable $\operatorname{mex}$?"

??? note "Solution"
    First consider how to solve it without deletions.
    
    Create a new vertex for every multiset, and a new vertex for every possible answer. Then, for an element $a$ of the multiset corresponding to vertex $l_i$, add an edge from $l_i$ to $r_a$. This weakened version is now a maximum bipartite matching.
    
    Now add the deletions back, and we find it cannot be handled at all: deleting an edge may change the matching drastically, and the complexity is unacceptable. So instead we go backwards: each time we add an edge and then re-augment. Hence only Kuhn's algorithm can be used for this problem.

??? note "Code"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_6.cpp"
    ```

???+ example "[Luogu P3355 - 骑士共存问题](https://www.luogu.com.cn/problem/P3355)"
    Given an $n \times n$ chessboard where some squares cannot hold pieces, what is the maximum number of knights that can be placed so that no two attack each other?

??? note "Solution"
    Observe that if the whole board is colored so that no two black squares and no two white squares are adjacent, a knight can only attack squares of the opposite color.
    
    Then we can directly apply maximum independent set in a bipartite graph.

??? note "Code"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_7.cpp"
    ```

## Exercises

-   [Codeforces 1765A - Access Levels](https://codeforces.com/problemset/problem/1765/A)
-   [AtCoder abc274G - Security Camera 3](https://atcoder.jp/contests/abc274/tasks/abc274_g)
-   [Codeforces 1773D - Dominoes](https://codeforces.com/problemset/problem/1773/D)
-   [Luogu P5030 - 长脖子鹿放置](https://www.luogu.com.cn/problem/P5030)
-   [Luogu P2071 - 座位安排](https://www.luogu.com.cn/problem/P2071)
-   [LibreOJ 6002 - 最小路径覆盖](https://loj.ac/p/6002)

## References

-   [Kuhn's Algorithm - Maximum Bipartite Matching](https://cp-algorithms.com/graph/kuhn_maximum_bipartite_matching.html)
-   [二分图最大匹配的 König 定理及其证明 (Kőnig's theorem on maximum bipartite matching and its proof)](https://matrix67.com/blog/archives/116)
-   [Implementing Dinitz on bipartite graphs by adamant - Codeforces blogs](https://codeforces.com/blog/entry/118098)
-   Bondy, John Adrian, and Uppaluri Siva Ramachandra Murty. Graph theory with applications. Vol. 290. London: Macmillan, 1976.
-   陈胤伯 (Chen Yinbo). 浅谈图的匹配算法及其应用 (On graph matching algorithms and their applications). Collected papers of the candidates for the Chinese national team at the Olympiad in Informatics, 2015.
-   [Dulmage–Mendelsohn decomposition - Wikipedia](https://en.wikipedia.org/wiki/Dulmage%E2%80%93Mendelsohn_decomposition)
-   [Notes on Dulmage–Mendelsohn decomposition](https://www.cse.iitm.ac.in/~meghana/matchings/bip-decomp.pdf)

[^hk-comp-ref]: Bast, Holger; Mehlhorn, Kurt; Schäfer, Guido; Tamaki, Hisao (2006), "Matching algorithms are fast in sparse random graphs", Theory of Computing Systems, 39 (1): 3–14.
