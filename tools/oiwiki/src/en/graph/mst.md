---
title: Minimum spanning tree
---

## Definition

Before reading the following, make sure you have read [Graph theory concepts](./concept.md) and [Tree basics](./tree-basic.md), and know the following definitions:

1.  spanning subgraph
2.  spanning tree

We define the **minimum spanning tree** (MST) of an undirected connected graph as the spanning tree with the minimum sum of edge weights.

Note: only connected graphs have spanning trees; a disconnected graph only has a spanning forest.

## Kruskal's algorithm

Kruskal's algorithm is a common and easy-to-write minimum spanning tree algorithm invented by Kruskal. Its basic idea is to add edges from the smallest to the largest; it is a greedy algorithm.

### Prerequisites

[DSU](../ds/dsu.md), [greedy](../basic/greedy.md), [graph storage](./save.md).

### Implementation

Illustration:

![](./images/mst-2.apng)

Pseudocode:

<!--
```pseudo
\begin{algorithm}
\caption{Kruskal}
\begin{algorithmic}
\INPUT{ The edges of the graph $e$ where each element in $e$ is $(u, v, w)$ denoting that there is an edge between $u$ and $v$ weighted $w$. }
\OUTPUT The edges of the MST of the input graph
\STATE $result \gets \varnothing$
\STATE sort $e$ into nondecreasing order by weight $w$
\FOR{each $(u, v, w)$ in the sorted $e$}
    \IF{$u$ \AND $v$ are not connected in the union-find set}
        \STATE connect $u$ \AND $v$ in the union-find set
        \STATE $result \gets result \bigcup (u, v, w)$
    \ENDIF
\ENDFOR
\RETURN $result$
\end{algorithmic}
\end{algorithm}
```
-->

$$
\begin{array}{ll}
1 &  \textbf{Input. } \text{The edges of the graph } e , \text{ where each element in } e \text{ is } (u, v, w) \\
  &  \text{ denoting that there is an edge between } u \text{ and } v \text{ weighted } w . \\
2 &  \textbf{Output. } \text{The edges of the MST of the input graph}.\\
3 &  \textbf{Method. } \\ 
4 &  result \gets \varnothing \\
5 &  \text{sort } e \text{ into nondecreasing order by weight } w \\ 
6 &  \textbf{for} \text{ each } (u, v, w) \text{ in the sorted } e \\ 
7 &  \qquad \textbf{if } u \text{ and } v \text{ are not connected in the union-find set } \\
8 &  \qquad\qquad \text{connect } u \text{ and } v \text{ in the union-find set} \\
9 &  \qquad\qquad  result \gets result\;\bigcup\ \{(u, v, w)\} \\
10 &  \textbf{return }  result
\end{array}
$$

The algorithm is simple, but it needs an appropriate data structure to support it... Concretely, we maintain a forest, query whether two vertices are in the same tree, and connect two trees.

More abstractly, we maintain a bunch of **sets**, query whether two elements belong to the same set, and merge two sets.

Querying whether two vertices are connected and connecting two vertices can be maintained with a DSU.

If we use an $O(m\log m)$ sorting algorithm and an $O(m\alpha(m, n))$ or $O(m\log n)$ DSU, we get Kruskal's algorithm with time complexity $O(m\log m)$.

### Proof

The idea is simple: to build a minimum spanning tree, we start from the edge with the smallest weight and add edges in increasing order of weight; if adding an edge creates a cycle, we discard that edge, until $n-1$ edges have been added, i.e. a tree is formed.

Proof: by induction, we prove that at any time the edge set chosen by the K algorithm is contained in some MST.

Base: at the very beginning of the algorithm this obviously holds (a minimum spanning tree exists).

Step: suppose it holds at some moment, the current edge set is $F$, let $T$ be that MST, and consider the next edge $e$ to be added.

If $e$ belongs to $T$, it holds.

Otherwise, $T+e$ must contain a cycle; consider another edge $f$ on this cycle that does not belong to $F$ (at least one exists).

First, the weight of $f$ cannot be smaller than that of $e$, otherwise $f$ would have been chosen before $e$.

Then, the weight of $f$ cannot be larger than that of $e$, otherwise $T+e-f$ would be a spanning tree better than $T$.

Therefore $T+e-f$ contains $F$ and is also a minimum spanning tree, so the induction holds.

### Example

???+ note "[Luogu P1195 Sky in the Pocket](https://www.luogu.com.cn/problem/P1195)"
    There are $n$ clouds that you must connect into $k$ pieces of cotton candy; connecting clouds $X_i$ and $Y_i$ costs $L_i$. Find the minimum cost.

??? note "Example code"
    === "C++"
        ```cpp
        --8<-- "docs/graph/code/mst/mst_3.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/graph/code/mst/mst_3.py"
        ```
    
    === "Java"
        ```java
        --8<-- "docs/graph/code/mst/mst_3.java"
        ```

## Prim's algorithm

Prim's algorithm is another common and easy-to-write minimum spanning tree algorithm. Its basic idea is to start from one vertex and keep adding vertices (rather than adding edges as in Kruskal's algorithm).

### Implementation

Illustration:

![](./images/mst-3.apng)

Concretely, each time we choose the vertex with the minimum distance and use the new edges to update the distances of the other vertices.

In fact, just like Dijkstra's algorithm, each time we find the vertex with the minimum distance, which can be done by brute force or maintained with a heap.

The heap optimization is similar to the heap optimization of Dijkstra, but if a binary heap or another heap not supporting $O(1)$ decrease-key is used, the complexity is not better than Kruskal's, and the constant factor is larger than Kruskal's. Therefore Kruskal's algorithm is used in general; on dense graphs, especially complete graphs, brute-force Prim has better complexity than Kruskal, but it is **not necessarily** faster in practice.

Brute force: $O(n^2+m)$.

Binary heap: $O((n+m) \log n)$.

Fibonacci heap: $O(n \log n + m)$.

Pseudocode:

$$
\begin{array}{ll}
1 &  \textbf{Input. } \text{The nodes of the graph }V\text{ ; the function }g(u, v)\text{ which}\\
  &  \text{means the weight of the edge }(u, v)\text{; the function }adj(v)\text{ which}\\
  &  \text{means the nodes adjacent to }v.\\
2 &  \textbf{Output. } \text{The sum of weights of the MST of the input graph.} \\
3 &  \textbf{Method.} \\
4 &  result \gets 0 \\
5 & \text{choose an arbitrary node in }V\text{ to be the }root \\
6 &  dis(root)\gets 0 \\
7 &  \textbf{for } \text{each node }v\in(V-\{root\}) \\
8 &  \qquad  dis(v)\gets\infty \\
9 &  rest\gets V \\
10 &  \textbf{while }  rest\ne\varnothing \\
11 &  \qquad cur\gets \text{the node with the minimum }dis\text{ in }rest \\
12 &  \qquad  result\gets result+dis(cur) \\
13 &  \qquad  rest\gets rest-\{cur\} \\
14 &  \qquad  \textbf{for}\text{ each node }v\in adj(cur) \\
15 &  \qquad\qquad  dis(v)\gets\min(dis(v), g(cur, v)) \\
16 &  \textbf{return }  result 
\end{array}
$$

Note: the code above only computes the weight of the minimum spanning tree; to output the tree itself, you also need to record which edge each vertex's $dis$ represents.

??? note "Implementation"
    ```cpp
    // Prim's algorithm optimized with a binary heap.
    #include <cstring>
    #include <iostream>
    #include <queue>
    using namespace std;
    constexpr int N = 5050, M = 2e5 + 10;
    
    struct E {
      int v, w, x;
    } e[M * 2];
    
    int n, m, h[N], cnte;
    
    void adde(int u, int v, int w) { e[++cnte] = E{v, w, h[u]}, h[u] = cnte; }
    
    struct S {
      int u, d;
    };
    
    bool operator<(const S &x, const S &y) { return x.d > y.d; }
    
    priority_queue<S> q;
    int dis[N];
    bool vis[N];
    
    int res = 0, cnt = 0;
    
    void Prim() {
      memset(dis, 0x3f, sizeof(dis));
      dis[1] = 0;
      q.push({1, 0});
      while (!q.empty()) {
        if (cnt >= n) break;
        int u = q.top().u, d = q.top().d;
        q.pop();
        if (vis[u]) continue;
        vis[u] = true;
        ++cnt;
        res += d;
        for (int i = h[u]; i; i = e[i].x) {
          int v = e[i].v, w = e[i].w;
          if (w < dis[v]) {
            dis[v] = w, q.push({v, w});
          }
        }
      }
    }
    
    int main() {
      cin >> n >> m;
      for (int i = 1, u, v, w; i <= m; ++i) {
        cin >> u >> v >> w, adde(u, v, w), adde(v, u, w);
      }
      Prim();
      if (cnt == n)
        cout << res;
      else
        cout << "No MST.";
      return 0;
    }
    ```

### Proof

Start from an arbitrary vertex and divide the vertices into two classes: added and not added.

Each time, among the not-added vertices, find the one whose minimum edge weight to the added vertices is smallest.

Then add this vertex and connect it with that minimum-weight edge.

Repeat $n-1$ times.

Proof: again we show that at every step there is a minimum spanning tree containing the chosen edge set.

Base: with only one vertex it obviously holds.

Step: if it holds at some step, the current edge set $F$ belongs to the MST $T$, and the next edge to add is $e$.

If $e$ belongs to $T$, it holds.

Otherwise, consider another edge $f$ on the cycle in $T+e$ that could have been added to the current edge set.

First, the weight of $f$ cannot be smaller than that of $e$, otherwise $f$ would have been chosen instead of $e$.

Then, the weight of $f$ cannot be larger than that of $e$, otherwise $T+e-f$ would be a smaller spanning tree.

Therefore $e$ and $f$ have equal weight, and $T+e-f$ is also a minimum spanning tree containing $F$.

## Borůvka's algorithm

Next we introduce another algorithm for the minimum spanning tree — Borůvka's algorithm. Its idea is a combination of the two previous algorithms. It can be used to find the minimum spanning forest of an undirected graph (for an undirected connected graph this is the minimum spanning tree).

Borůvka's algorithm has an advantage in problems where the edges have many special properties, for example the complete graph problem [CF888G](https://codeforces.com/problemset/problem/888/G).

To describe the algorithm, we need to introduce some definitions:

1.  Let $E'$ be the edges of the minimum spanning forest found so far. During the algorithm we gradually add edges to $E'$; a **connected component** is a vertex set $V'\subseteq V$ such that any two vertices $u$, $v$ of this set are connected (mutually reachable) in the subgraph formed by the edges of $E'$.
2.  The **minimum edge** of a connected component is the edge with the smallest weight among the edges connecting it to other connected components.

Initially $E'=\varnothing$ and every vertex is its own connected component:

1.  Compute which connected component each vertex belongs to. Set every connected component to "no minimum edge".
2.  Iterate over every edge $(u, v)$; if $u$ and $v$ are not in the same connected component, use the weight of this edge to update the minimum edge of the components containing $u$ and $v$ respectively.
3.  If no connected component has a minimum edge, stop; the current $E'$ is the edge set of the minimum spanning forest of the original graph. Otherwise add the minimum edge of every connected component that has one to $E'$ and go back to the first step.

Here is an example shown with an animation (image from [Wikipedia](https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm)):

![eg](./images/mst-1.apng)

When the original graph is connected, the number of connected components at least halves in every iteration, so the algorithm iterates at most $O(\log V)$ times; when the original graph is disconnected, it is equivalent to several subproblems, so the complexity of the algorithm is $O(E\log V)$. Pseudocode of the algorithm (adapted from [Wikipedia](https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm)):

$$
\begin{array}{ll}
1 &  \textbf{Input. } \text{A graph }G\text{ whose edges have distinct weights. } \\
2 &  \textbf{Output. } \text{The minimum spanning forest of }G .  \\
3 &  \textbf{Method. }  \\
4 & \text{Initialize a forest }F\text{ to be a set of one-vertex trees} \\
5 &  \textbf{while } \text{True} \\
6 &  \qquad \text{Find the components of }F\text{ and label each vertex of }G\text{ by its component } \\
7 &  \qquad \text{Initialize the cheapest edge for each component to "None"} \\
8 &  \qquad  \textbf{for } \text{each edge }(u, v)\text{ of }G  \\
9 &  \qquad\qquad  \textbf{if }  u\text{ and }v\text{ have different component labels} \\
10 &  \qquad\qquad\qquad  \textbf{if }  (u, v)\text{ is cheaper than the cheapest edge for the component of }u  \\
11 &  \qquad\qquad\qquad\qquad\text{ Set }(u, v)\text{ as the cheapest edge for the component of }u \\
12 &  \qquad\qquad\qquad  \textbf{if }  (u, v)\text{ is cheaper than the cheapest edge for the component of }v  \\
13 &  \qquad\qquad\qquad\qquad\text{ Set }(u, v)\text{ as the cheapest edge for the component of }v  \\
14 &  \qquad  \textbf{if }\text{ all components'cheapest edges are "None"} \\
15 &  \qquad\qquad  \textbf{return }  F \\
16 &  \qquad  \textbf{for }\text{ each component whose cheapest edge is not "None"} \\
17 &  \qquad\qquad\text{ Add its cheapest edge to }F \\
\end{array}
$$

Note that comparing edges usually requires a secondary key (for example sorting by index) so that edges with equal weights can be ordered.

## Exercises

-   [「HAOI2006」Clever Monkeys](https://www.luogu.com.cn/problem/P2504)
-   [「SCOI2005」Busy City](https://loj.ac/problem/2149)

## Uniqueness of the minimum spanning tree

Consider the uniqueness of the minimum spanning tree. If an edge is **not in the edge set of the minimum spanning tree** and can replace another edge **with the same weight that is in the edge set of the minimum spanning tree**, then the minimum spanning tree is not unique.

For Kruskal's algorithm, we just compute how many edges of the current weight can be added and how many were actually added; if these two values differ, these edges form a cycle with the previous edges (this cycle contains at least two edges of the current weight, otherwise by the DSU this edge could not be added), i.e. the minimum spanning tree is not unique.

To find the edges with the same weight as the current edge, we only need to record head and tail pointers; with a monotonic queue this problem can be solved nicely in $O(\alpha(m))$ time (m is the number of edges), essentially the same as the original algorithm.

??? note "Example: [POJ 1679](http://poj.org/problem?id=1679)"
    ```cpp
    --8<-- "docs/graph/code/mst/mst_1.cpp"
    ```

## Second-best minimum spanning tree

### Non-strict second-best minimum spanning tree

#### Definition

In an undirected graph, the spanning tree with the minimum sum of edge weights among those whose sum of edge weights is **greater than or equal to** that of the minimum spanning tree.

#### Solution method

-   Find the minimum spanning tree $T$ of the undirected graph and let its weight sum be $M$.
-   Iterate over every unselected edge $e = (u,v,w)$, find the edge with the largest weight $e' = (s,t,w')$ on the path from $u$ to $v$ in $T$; replacing $e'$ with $e$ in $T$ gives a spanning tree $T'$ with weight sum $M' = M + w - w'$.
-   Take the minimum over all answers $M'$ obtained by replacement.

How do we find the maximum edge weight on the path between $u,v$?

We can maintain it with binary lifting: precompute the $2^i$-th ancestor of every vertex and the maximum edge weight on the path to its $2^i$-th ancestor, so that it can be obtained directly while computing the LCA with binary lifting.

### Strict second-best minimum spanning tree

#### Definition

In an undirected graph, the spanning tree with the minimum sum of edge weights among those whose sum of edge weights is **strictly greater than** that of the minimum spanning tree.

#### Solution method

Consider the solution process for the non-strict second-best minimum spanning tree just described: why is the solution obtained non-strict?

Because the minimum spanning tree guarantees that the maximum edge weight on the path from $u$ to $v$ in the tree is **not greater than** the maximum edge weight on any other path from $u$ to $v$. In other words, when the weight of the replacing edge equals the weight of the replaced edge in the original spanning tree, the second-best spanning tree obtained is non-strict.

The solution is natural: while maintaining the maximum edge weight on the path to the $2^i$-th ancestor, we also maintain the **strictly second-largest edge weight**; when the weight of the replacing edge equals the maximum edge weight on the path in the original spanning tree, we replace with the strictly second-largest value.

This process can be solved with binary lifting, complexity $O(m \log m)$.

??? note "Implementation"
    ```cpp
    #include <algorithm>
    #include <iostream>
    
    constexpr int INF = 0x3fffffff;
    constexpr long long INF64 = 0x3fffffffffffffffLL;
    
    struct Edge {
      int u, v, val;
    
      bool operator<(const Edge &other) const { return val < other.val; }
    };
    
    Edge e[300010];
    bool used[300010];
    
    int n, m;
    long long sum;
    
    class Tr {
     private:
      struct Edge {
        int to, nxt, val;
      } e[600010];
    
      int cnt, head[100010];
    
      int pnt[100010][22];
      int dpth[100010];
      // edge with the maximum weight on the path to the ancestor
      int maxx[100010][22];
      // edge with the second-largest weight on the path to the ancestor, -INF if it does not exist
      int minn[100010][22];
    
     public:
      void addedge(int u, int v, int val) {
        e[++cnt] = Edge{v, head[u], val};
        head[u] = cnt;
      }
    
      void insedge(int u, int v, int val) {
        addedge(u, v, val);
        addedge(v, u, val);
      }
    
      void dfs(int now, int fa) {
        dpth[now] = dpth[fa] + 1;
        pnt[now][0] = fa;
        minn[now][0] = -INF;
        for (int i = 1; (1 << i) <= dpth[now]; i++) {
          pnt[now][i] = pnt[pnt[now][i - 1]][i - 1];
          int kk[4] = {maxx[now][i - 1], maxx[pnt[now][i - 1]][i - 1],
                       minn[now][i - 1], minn[pnt[now][i - 1]][i - 1]};
          // take the maximum of the four values
          std::sort(kk, kk + 4);
          maxx[now][i] = kk[3];
          // take the strictly second-largest value
          int ptr = 2;
          while (ptr >= 0 && kk[ptr] == kk[3]) ptr--;
          minn[now][i] = (ptr == -1 ? -INF : kk[ptr]);
        }
    
        for (int i = head[now]; i; i = e[i].nxt) {
          if (e[i].to != fa) {
            maxx[e[i].to][0] = e[i].val;
            dfs(e[i].to, now);
          }
        }
      }
    
      int lca(int a, int b) {
        if (dpth[a] < dpth[b]) std::swap(a, b);
    
        for (int i = 21; i >= 0; i--)
          if (dpth[pnt[a][i]] >= dpth[b]) a = pnt[a][i];
    
        if (a == b) return a;
    
        for (int i = 21; i >= 0; i--) {
          if (pnt[a][i] != pnt[b][i]) {
            a = pnt[a][i];
            b = pnt[b][i];
          }
        }
        return pnt[a][0];
      }
    
      int query(int a, int b, int val) {
        int res = -INF;
        for (int i = 21; i >= 0; i--) {
          if (dpth[pnt[a][i]] >= dpth[b]) {
            if (val != maxx[a][i])
              res = std::max(res, maxx[a][i]);
            else
              res = std::max(res, minn[a][i]);
            a = pnt[a][i];
          }
        }
        return res;
      }
    } tr;
    
    int fa[100010];
    
    int find(int x) { return fa[x] == x ? x : fa[x] = find(fa[x]); }
    
    void Kruskal() {
      int tot = 0;
      std::sort(e + 1, e + m + 1);
      for (int i = 1; i <= n; i++) fa[i] = i;
    
      for (int i = 1; i <= m; i++) {
        int a = find(e[i].u);
        int b = find(e[i].v);
        if (a != b) {
          fa[a] = b;
          tot++;
          tr.insedge(e[i].u, e[i].v, e[i].val);
          sum += e[i].val;
          used[i] = true;
        }
        if (tot == n - 1) break;
      }
    }
    
    int main() {
      std::ios::sync_with_stdio(false);
      std::cin.tie(nullptr);
    
      std::cin >> n >> m;
      for (int i = 1; i <= m; i++) {
        int u, v, val;
        std::cin >> u >> v >> val;
        e[i] = Edge{u, v, val};
      }
    
      Kruskal();
      long long ans = INF64;
      tr.dfs(1, 0);
    
      for (int i = 1; i <= m; i++) {
        if (!used[i]) {
          int _lca = tr.lca(e[i].u, e[i].v);
          // find the maximum edge weight on the path that is not equal to e[i].val
          long long tmpa = tr.query(e[i].u, _lca, e[i].val);
          long long tmpb = tr.query(e[i].v, _lca, e[i].val);
          // such an edge may not exist; update the answer only when it exists
          if (std::max(tmpa, tmpb) > -INF)
            ans = std::min(ans, sum - std::max(tmpa, tmpb) + e[i].val);
        }
      }
      // output -1 when the second-best spanning tree does not exist
      std::cout << (ans == INF64 ? -1 : ans) << '\n';
      return 0;
    }
    ```

## Bottleneck spanning tree

### Definition

A bottleneck spanning tree of an undirected graph $G$ is a spanning tree whose maximum edge weight is minimal among all spanning trees of $G$.

### Properties

**Being a minimum spanning tree is a sufficient but not necessary condition for being a bottleneck spanning tree.** That is, a minimum spanning tree is always a bottleneck spanning tree, but a bottleneck spanning tree is not necessarily a minimum spanning tree.

The statement that a minimum spanning tree is always a bottleneck spanning tree can be proven by contradiction: let the maximum edge weight in the minimum spanning tree be $w$. If the minimum spanning tree were not a bottleneck spanning tree, then all edge weights of the bottleneck spanning tree would be smaller than $w$; we just delete the longest edge of the original minimum spanning tree and use an edge of the bottleneck spanning tree to connect the two trees formed after the deletion; the new spanning tree obtained must have a smaller weight sum than the original minimum spanning tree, which is a contradiction.

### Example

???+ note "POJ 2395 Out of Hay"
    Given n farms and m roads, with farms numbered 1 to n, a person starts from farm 1 and travels to the other farms; find the maximum weight of water he needs to carry along the way, noting that he can refill water at every farm he reaches, and the total path length should be minimal.
    What the problem asks for is the maximum edge of the bottleneck tree, which can be solved by finding the minimum spanning tree.

## Minimum bottleneck path

### Definition

A minimum bottleneck path from x to y in an undirected graph $G$ is a simple path whose maximum edge weight is minimal among all simple paths from x to y.

### Properties

By the definition of the minimum spanning tree, the maximum edge weight on the minimum bottleneck path from x to y equals the maximum edge weight on the path from x to y in the minimum spanning tree. Although the minimum spanning tree is not unique, the maximum edge weight on the path from x to y is the same in every minimum spanning tree and is the minimum. That is, the path from x to y in every minimum spanning tree is a minimum bottleneck path.

However, not every minimum bottleneck path has a minimum spanning tree in which it is the simple path from x to y in the tree.

For example, in the following picture:

![](./images/mst5.png)

the minimum bottleneck paths from 1 to 4 are clearly the following two: 1-2-3-4 and 1-3-4.

But 1-2 does not appear in any minimum spanning tree.

### Application

Since the minimum bottleneck path is not unique, usually the maximum edge weight on the minimum bottleneck path is asked.

That is, we need the max on a path in the minimum spanning tree.

Binary lifting and heavy-light decomposition can both solve it; we do not go into details here.

## Kruskal reconstruction tree

### Definition

While running Kruskal we add a number of edges from smallest to largest. Now we keep this order.

First create $n$ sets, each with exactly one vertex of weight $0$.

Every edge addition merges two sets; we can create a new vertex whose weight is the weight of the added edge, and set the roots of the two sets as the left and right children of the new vertex. Then we merge the two sets and the new vertex into one set and make the new vertex the root.

It is easy to see that after $n-1$ rounds we obtain a binary tree with exactly $n$ leaves, in which every internal vertex has exactly two children. This tree is called the Kruskal reconstruction tree.

An example:

![](./images/mst5.png)

The Kruskal reconstruction tree of this graph is as follows:

![](./images/mst6.png)

### Properties

It is easy to see: the minimum over all simple paths between two vertices of the original graph of the maximum edge weight = the maximum on the simple path between the two vertices in the minimum spanning tree = the weight of the LCA of the two vertices in the Kruskal reconstruction tree.

That is, all vertices $y$ for which the minimum of the maximum edge weight on a simple path to vertex $x$ is $\leq val$ lie in some subtree of the Kruskal reconstruction tree, and they are exactly all leaves of that subtree.

In the Kruskal reconstruction tree we find the shallowest vertex with weight $\leq val$ on the path from $x$ to the root. Clearly this is the root of the subtree containing all vertices satisfying the condition.

If we need the maximum over all simple paths between two vertices of the original graph of the minimum edge weight, we add edges in decreasing order of weight while running Kruskal.

??? note "[「LOJ 137」Minimum Bottleneck Path, Enhanced Version](https://loj.ac/problem/137)"
    ```cpp
    --8<-- "docs/graph/code/mst/mst_2.cpp"
    ```

??? note "[NOI 2018 Return](https://uoj.ac/problem/393)"
    First precompute the shortest path from every vertex to the root.
    
    We construct the maximum spanning tree according to altitude. Clearly the vertices reachable in each query are those whose minimum edge weight on the path to the query vertex in the maximum spanning tree is $> p$.
    
    By the properties of the Kruskal reconstruction tree, these vertices all lie in one subtree and are exactly all its leaves.
    
    That is, we only need to compute the min of the leaf weights of every subtree of the Kruskal reconstruction tree to support subtree queries.
    
    The root of the query can be found by binary lifting on the Kruskal reconstruction tree.
    
    Time complexity $O((n+m+Q) \log n)$.
