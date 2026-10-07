---
title: Chordal graphs
---

Chordal graphs are a special class of graphs: many problems that are NP-hard on general graphs have nice linear-time algorithms on chordal graphs.

## Some definitions and properties

**Subgraph**: a graph whose vertex set and edge set are subsets of the vertex set and edge set of the original graph.

**Induced subgraph**: a graph whose vertex set is a subset of the vertex set of the original graph, and whose edge set consists of all edges **with both endpoints in the chosen vertex set**.

**Clique**: a complete subgraph.

**Maximal clique**: a clique that is not a subgraph of any other clique.

**Maximum clique**: a clique with the largest number of vertices.

**Clique number**: the number of vertices of a maximum clique, denoted $\omega(G)$.

**Minimum coloring**: coloring the vertices with the fewest colors so that the two endpoints of every edge have different colors.

**Chromatic number**: the number of colors in a minimum coloring, denoted $\chi(G)$.

**Maximum independent set**: a largest vertex set in which no two vertices are directly connected by an edge. Its size is denoted $\alpha(G)$.

**Minimum clique cover**: covering all vertices with the fewest cliques. The number of cliques used is denoted $\kappa(G)$.

**Chord**: an edge connecting two non-adjacent vertices of a cycle.

**Chordal graph**: a graph in which every cycle of length greater than $3$ has a chord.

**Lemma 1**: clique number $\omega(G)\le \chi(G)$ chromatic number

Proof: consider coloring the induced subgraph of a maximum clique alone; it needs at least $\omega(G)$ colors.

**Lemma 2**: maximum independent set size $\alpha(G)\le \kappa(G)$ minimum clique cover size

Proof: at most one vertex can be chosen from each clique.

**Lemma 3**: every induced subgraph of a chordal graph is chordal.

Proof: if a chordal graph had an induced subgraph that is not chordal, that induced subgraph would contain a chordless cycle of length greater than $3$; then no matter what the original graph looks like (however edges are added), it cannot be chordal, a contradiction.

**Lemma 4**: no induced subgraph of a chordal graph can be a cycle with more than $3$ vertices.

Proof: a cycle with more than $3$ vertices is not chordal; apply the lemma above.

## Recognizing chordal graphs

### Problem statement

Given an undirected graph, decide whether it is chordal.

### Vertex separators

For two vertices $u,v$ of a graph $G$, a **vertex separator** of these two vertices is a set of vertices whose removal disconnects $u,v$. If no proper subset of a vertex separator for $u,v$ is a vertex separator, it is called a **minimal vertex separator**.

**Lemma 5**: a minimal vertex separator for $u,v$ splits the original graph into several connected components; let $V_1$ be the component containing $u$ and $V_2$ the component containing $v$. Then for every vertex $a$ of the minimal vertex separator, $N(a)$ contains vertices from both $V_1$ and $V_2$.

Proof: if $N(a)$ contains vertices from at most one of the components $V_1$ and $V_2$, then removing $a$ from the separator still leaves them disconnected, so the original separator is not minimal.

**Lemma 6**: the induced subgraph of a minimal vertex separator between any two vertices of a chordal graph is a clique.

Proof: if the minimal vertex separator has size $\le 1$, its induced subgraph is clearly a clique.

Otherwise let $x,y$ be two vertices of the minimal vertex separator; by **Lemma 5**, $N(x)$ contains vertices from $V_1,V_2$, call them $x_1,x_2$, and similarly take $y_1,y_2$; note that possibly $x_1=y_1,x_2=y_2$.

Since $V_1,V_2$ are connected components, shortest paths exist between the pairs $x_1,y_1$ and $x_2,y_2$. Let the shortest paths between $x,y$ inside $V_1,V_2$ be $x-x_1\sim y_1-y,x-x_2\sim y_2-y$; then the graph contains a cycle $x-x_1\sim y_1-y-y_2\sim x_2-x$ of length certainly $\ge 4$, so by the definition of a chordal graph this cycle must have a chord.

If this chord connects the two components $V_1,V_2$, the set is not a vertex separator. If it connects two vertices inside one component, or a vertex inside a component with a vertex of the separator, it violates the shortest path property. So the chord can only connect $x,y$.

Hence any two vertices of a minimal vertex separator in a chordal graph are directly connected by an edge, which proves the property.

### Simplicial vertices

Let $N(x)$ denote the set of vertices adjacent to $x$. If the induced subgraph of the vertex set $\{x\}+N(x)$ is a clique, the vertex $x$ is called simplicial.

**Lemma 7**: every chordal graph has at least one simplicial vertex, and a chordal graph that is not complete has at least two non-adjacent simplicial vertices.

Proof: by induction. Consider each connected component separately.

Base case: when the graph is isomorphic to a complete graph, every vertex is simplicial. When the graph has $\le 3$ vertices, the lemma holds.

If the graph has $\ge 4$ vertices and is not complete, there exist $u,v$ with $(u,v)\notin E$. Let $I$ be a minimal vertex separator for $u,v$. Let $A,B$ be the connected components of the induced subgraph after removing $I$ that contain $u,v$ respectively. By symmetry we only consider the side of $A$; let $L=A+I$. If $L$ is a complete graph, then $u$ is simplicial; if not, since $L$ is an induced subgraph of the original graph it is also chordal, so it has two non-adjacent simplicial vertices; since $I$ is a clique and any two of its vertices are adjacent, $A$ must contain a simplicial vertex. This vertex is simplicial in the whole graph as well.

Since at every step the graph is split into components whose size strictly decreases and which all satisfy the property, the induction goes through.

### Perfect elimination ordering

Let $n=|V|$; a perfect elimination ordering $v_1,v_2,\ldots ,v_n$ is a permutation of $1,2,\ldots ,n$ such that $v_i$ is a simplicial vertex in the induced subgraph of $\{v_i,v_{i+1},\ldots ,v_n\}$.

**Lemma 8**: an undirected graph is chordal if and only if it has a perfect elimination ordering.

Sufficiency: a chordal graph with $1$ vertex has a perfect elimination ordering. By **Lemma 3** and **Lemma 7**, a perfect elimination ordering of a chordal graph with $n$ vertices is obtained from a perfect elimination ordering of a chordal graph with $n-1$ vertices by adding a simplicial vertex.

Necessity: suppose an undirected graph has a cycle with $>3$ vertices and a perfect elimination ordering; let $v$ be the first vertex of the cycle appearing in the perfect elimination ordering, and let $v$ be connected on the cycle to $v_1,v_2$. By the property of the perfect elimination ordering, i.e. the definition of a simplicial vertex, $v_1,v_2$ are directly connected by an edge, a contradiction.

### Naive algorithm

Each time, find a **simplicial vertex** $v$ and append it to the perfect elimination ordering.

Delete the vertex $v$ and its incident edges from the graph.

Repeat the process; if all vertices get deleted, the graph is chordal and a perfect elimination ordering has been found; if the graph has no simplicial vertex, the graph is not chordal.

Time complexity $O(n^4)$.

### MCS algorithm

**Maximum Cardinality Search** is a method that finds a perfect elimination ordering of an undirected graph in $O(n+m)$ time.

Number the vertices in reverse order, i.e. assign labels in the order from $n$ down to $1$.

Let $label_x$ denote how many already labeled vertices the vertex $x$ is adjacent to; each time, label the unlabeled vertex with the largest $label$ value.

Use linked lists to maintain, for each $i$, the vertices $x$ with $label_x=i$.

Since every edge contributes at most $2$ to $\sum_{i=1}^n label_i$, the time complexity is $O(n+m)$.

**Proof of correctness**:

Let $\alpha(x)$ be the position of $x$ in this ordering.
We need to prove that for every chordal graph the ordering found by the algorithm is a perfect elimination ordering, i.e. all vertices that come after a given vertex in the ordering and are adjacent to it are pairwise adjacent.

**Lemma 9**: consider three vertices $u,v,w$ with $\alpha(u)<\alpha(v)<\alpha(w)$; if $uw$ is an edge but $vw$ is not, then $w$ contributes only to the $label$ of $u$, not of $v$. For $v$ to enter the ordering before $u$, there must be an $x$ with $\alpha(v)<\alpha(x)$ such that $vx$ is an edge but $ux$ is not, i.e. $x$ contributes only to $v$ and not to $u$.

**Lemma 10**: a chordal graph cannot contain a sequence $v_0,v_1,\dots,v_k(k\ge 2)$ with the following properties:

1.  $v_iv_j$ is an edge if and only if $|i-j|=1$.
2.  $\alpha(v_0)>\alpha(v_i)(i\in[1,k])$.
3.  There exists $i\in[1,k-1]$ such that $\alpha(v_i)<\alpha(v_{i+1})<\dots<\alpha(v_k)$ and $\alpha(v_i)<\alpha(v_{i-1})<\dots<\alpha(v_1)<\alpha(v_k)<\alpha(v_0)$.

Proof:

Since $\alpha(v_1)<\alpha(v_k)<\alpha(v_0)$, $v_1v_0$ is an edge and $v_kv_0$ is not, by property one there exists $x$ with $\alpha(v_k)<\alpha(x)$ such that $v_kx$ is an edge but $v_1x$ is not.

Consider the smallest $j\in(1,k]$ such that $v_jx$ is an edge; we can deduce that $v_0x$ is not an edge, since otherwise $v_0v_1\cdots v_jx$ would form a chordless cycle of length $\ge 4$.

If $x<v_0$, then $v_0,v_1,\dots,v_j,x$ is also a sequence with these properties; if $v_0<x$, then $x,v_j,\dots,v_1,v_0$ is also a sequence with these properties.

In the derivation above we increased $\min(v_0,v_k)$, so continuing this way must eventually lead to a contradiction.

**Theorem 1**: for every chordal graph, the ordering found by maximum cardinality search is a perfect elimination ordering.

Proof: consider any three vertices $u,v,w$ with $\alpha(u)<\alpha(v)<\alpha(w)$; we need to prove that if $uv$ is an edge and $uw$ is an edge, then $vw$ must be an edge.

By contradiction, suppose they are not adjacent; then $w,u,v$ is a sequence with the properties of **Lemma 10**, and we proved that such a sequence does not exist, a contradiction; so $vw$ is an edge.

???+ note "Reference implementation"
    ```cpp
    --8<-- "docs/graph/code/chord/chord_1.cpp:var"
    --8<-- "docs/graph/code/chord/chord_1.cpp:mcs"
    ```

If the original graph is chordal, the ordering obtained is a perfect elimination ordering; but since the original graph may not be chordal, in which case the ordering obtained is certainly not a perfect elimination ordering, the problem becomes **checking whether the obtained ordering is a perfect elimination ordering of the original graph**.

### Checking whether an ordering is a perfect elimination ordering

#### Naive algorithm

By definition, check in turn whether the vertices of $\{v_i,v_{i+1},\ldots ,v_n\}$ adjacent to $v_i$ in the ordering $v$ form a clique. Time complexity $O(nm)$.

#### Improved algorithm

Let $N^+(u)$ be the set of vertices after $u$ in the ordering that are adjacent to $u$, and $f(u)$ the earliest of them in the ordering. For every vertex $u$ with non-empty $N^+(u)$, it suffices to check whether every vertex of $N^+(u)\setminus\{f(u)\}$ is adjacent to $f(u)$.

This condition is clearly necessary. Sufficiency follows by induction from the back of the ordering: if all later vertices satisfy the requirement of a perfect elimination ordering, then $N^+(f(u))$ is a clique. When the check passes, $N^+(u)\setminus\{f(u)\}\subseteq N^+(f(u))$ and all its vertices are adjacent to $f(u)$, so $N^+(u)$ is also a clique. When $N^+(u)$ is empty, no check is needed.

First scan the adjacency lists to find $f(u)$ for every vertex, and group the vertices with the same $f(u)$. When processing the group with $f(u)=v$, first mark all neighbors of $v$, then scan the adjacency list of every vertex $u$ in the group and check whether all neighbors after $v$ in the ordering are marked. Using the vertex number $v$ as the mark value avoids clearing the mark array after each group. Every vertex belongs to at most one group, and the adjacency list of every vertex is scanned at most once when computing $f(u)$, when setting marks and when checking, so the total time complexity is $O(n+m)$.

???+ note "Reference implementation"
    ```cpp
    --8<-- "docs/graph/code/chord/chord_1.cpp:var"
    --8<-- "docs/graph/code/chord/chord_1.cpp:core"
    ```

Thus the **chordal graph recognition problem** can be solved in $O(n+m)$ time.

## Maximal cliques of a chordal graph

Let $N(x)$ be the set of vertices directly connected to $x$ by an edge that come after $x$ in the perfect elimination ordering. Then every maximal clique of a chordal graph has the form $\{x\}+N(x)$.

Proof: consider a maximal clique $V$ of the chordal graph and its vertex $x$ that appears first in the perfect elimination ordering; certainly $V\subseteq \{x\}+N(x)$, and since $V$ is a maximal clique, $V=\{x\}+N(x)$.

A chordal graph has at most $n$ maximal cliques. To find all maximal cliques of a chordal graph, we can check for each $\{x\}+N(x)$ whether it is a maximal clique.

Let $A=\{x\}+N(x),B=\{y\}+N(y)$; if $A\subsetneqq B$, then $A$ is not a maximal clique. In this case $y$ obviously comes before $x$ in the perfect elimination ordering.

Let $nxt_x$ denote the vertex of $N(x)$ that comes earliest in the perfect elimination ordering, and $y*$ the latest among all $y$ with $A\subseteq B$. Then necessarily $nxt_{y*}=x$, since otherwise $y*$ would not be the latest: $y*=nxt_{y*}$ would still satisfy the condition.

$A\subsetneqq B$ if and only if $|A|+1\le |B|$.

The problem becomes checking whether there exists $y$ with $nxt_y=x$ and $|N(x)|+1\le |N(y)|$. Time complexity $O(n+m)$.

```cpp
for (int i = 1; i <= n; i++) {
  cur = 0;
  for (vector<int>::iterator it = G[p[i]].begin(); it != G[p[i]].end(); it++)
    if (rnk[p[i]] < rnk[*it]) {
      s[++cur] = *it;
      if (rnk[s[cur]] < rnk[s[1]]) swap(s[1], s[cur]);
    }
  fst[p[i]] = s[1];
  N[p[i]] = cur;
}
for (int i = 1; i <= n; i++) {
  if (!vis[p[i]]) ans++;
  if (N[p[i]] >= N[fst[p[i]]] + 1) vis[fst[p[i]]] = true;
}
```

## Chromatic number / clique number of a chordal graph

A construction: color the vertices one by one along the perfect elimination ordering from back to front, giving each vertex the smallest color it may receive. Time complexity $O(m+n)$.

Proof of correctness: suppose the method above uses $t$ colors; then $t\ge \chi(G)$. Since all vertices of a clique get different colors, $t=\omega(G)$, and by **Lemma 1** $t=\omega(G)\le \chi(G)$. Hence $t=\chi(G)=\omega(G)$.

When no coloring is needed and only the chromatic/clique number of the chordal graph is required, it can be obtained as the maximum of $|\{x\}+N(x)|$.

```cpp
for (int i = 1; i <= n; i++) ans = max(ans, deg[i] + 1);
```

## Maximum independent set / minimum clique cover of a chordal graph

Maximum independent set: go through the perfect elimination ordering from front to back and choose every vertex that is not directly connected by an edge to any already chosen vertex.

Minimum clique cover: let the maximum independent set be $\{v_1,v_2,\ldots ,v_t\}$; then the set of cliques $\{\{v_1+N(v_1)\},\{v_2+N(v_2)\},\ldots ,\{v_t+N(v_t)\} \}$ is a minimum clique cover of the graph. The time complexity of both is $O(n+m)$.

Proof of correctness: let the independent set size and the clique cover size of the scheme above be $t$; by definition $t\le \alpha(G),t\ge \kappa(G)$, and by **Lemma 2** $\alpha(G)\le \kappa(G)$, so $t=\alpha(G)=\kappa(G)$.

```cpp
for (int i = 1; i <= n; i++)
  if (!vis[p[i]]) {
    ans++;
    for (vector<int>::iterator it = G[p[i]].begin(); it != G[p[i]].end(); it++)
      vis[*it] = true;
  }
```

## Exercises

[Library Checker - Chordal Graph Recognition](https://judge.yosupo.jp/problem/chordal_graph_recognition)

[SPOJ FISHNET - Fishing Net](https://www.spoj.com/problems/FISHNET)

[P3196 \[HNOI2008\] Magical Kingdom](https://www.luogu.com.cn/problem/P3196)

[P3852 \[TJOI2007\] Children](https://www.luogu.com.cn/problem/P3852)

## References

[On chordal graphs (Chinese)](https://yhx-12243.github.io/OI-transit/memos/15.html)

[WC 2009 lecture slides (Chinese)](https://github.com/hzwer/shareOI/blob/master/%E5%9B%BE%E8%AE%BA/%E5%BC%A6%E5%9B%BE%E4%B8%8E%E5%8C%BA%E9%97%B4%E5%9B%BE_%E9%99%88%E4%B8%B9%E7%90%A6.pptx)

[Summary of chordal graphs - zhoushuyu (Chinese)](https://www.cnblogs.com/zhoushuyu/p/8716935.html)

[R. E. Tarjan and M. Yannakakis, Simple linear-time algorithms to test chordality of graphs,test acyclicity of hypergraphs,and selectively reduce acyclic hypergraphs, SIAM J. Comput., 13 (1984), pp. 566–579.](https://dl.acm.org/doi/abs/10.1137/0213035)
