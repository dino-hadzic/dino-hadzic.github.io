---
title: Shortest paths
---

## Definition

(Do you still remember these definitions? Before reading on, make sure you know the basics from [Graph theory concepts](./concept.md).)

-   path
-   shortest path
-   shortest paths in directed graphs, shortest paths in undirected graphs
-   single-source shortest path, all-pairs shortest paths

## Notation

For convenience, we first give the meaning of some notation used below.

-   $n$ is the number of vertices of the graph, $m$ the number of edges;
-   $s$ is the source of the shortest paths;
-   $D(u)$ is the **actual** shortest distance from $s$ to $u$;
-   $dis(u)$ is the **estimated** shortest distance from $s$ to $u$. At any time $dis(u) \geq D(u)$. In particular, when a shortest path algorithm terminates, $dis(u)=D(u)$ should hold.
-   $w(u,v)$ is the weight of the edge $(u,v)$.

## Properties

In a graph with positive edge weights, a shortest path between any two vertices does not pass through a vertex twice.

In a graph with positive edge weights, a shortest path between any two vertices does not pass through an edge twice.

In a graph with positive edge weights, any shortest path between any two vertices has at most $n$ vertices and at most $n-1$ edges.

## Floyd's algorithm

It finds the shortest paths between all pairs of vertices.

The complexity is rather high, but the constant is small and it is easy to implement (only three `for` loops).

It applies to any graph, directed or undirected, with positive or negative weights, but the shortest paths must exist. (There must be no negative cycle.)

### Implementation

We define an array `f[k][x][y]`, the shortest distance from vertex $x$ to vertex $y$ when only vertices $1$ to $k$ may be passed through (that is, paths within the subgraph $V'={1, 2, \ldots, k}$; note that $x$ and $y$ need not be in this subgraph).

Obviously `f[n][x][y]` is the shortest distance from vertex $x$ to vertex $y$ (because $V'={1, 2, \ldots, n}$ is $V$ itself, so the shortest path it represents is the one we want).

Next we consider how to compute the values of `f`.

`f[0][x][y]`: the weight of the edge between $x$ and $y$, or $0$, or $+\infty$ (when should `f[0][x][y]` be $+\infty$? When $x$ and $y$ are directly connected by an edge, it is the weight of that edge; when $x = y$ it is zero, because the distance to itself is zero; when there is no edge directly connecting $x$ and $y$, it is $+\infty$).

`f[k][x][y] = min(f[k-1][x][y], f[k-1][x][k]+f[k-1][k][y])` (`f[k-1][x][y]` is the shortest path not passing through vertex $k$, while `f[k-1][x][k]+f[k-1][k][y]` is the shortest path passing through vertex $k$).

Both lines above are obviously correct, so this approach uses $O(N^3)$ space; we increase the problem size step by step ($k$ from $1$ to $n$) and determine the shortest path between any two vertices for the current problem size.

=== "C++"
    ```cpp
    for (k = 1; k <= n; k++) {
      for (x = 1; x <= n; x++) {
        for (y = 1; y <= n; y++) {
          f[k][x][y] = min(f[k - 1][x][y], f[k - 1][x][k] + f[k - 1][k][y]);
        }
      }
    }
    ```

=== "Python"
    ```python
    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                f[k][x][y] = min(f[k - 1][x][y], f[k - 1][x][k] + f[k - 1][k][y])
    ```

Since the first dimension does not affect the result, we notice that the first dimension of the array can be dropped, so we can simply write `f[x][y] = min(f[x][y], f[x][k]+f[k][y])`.

???+ note "Proof that the first dimension does not affect the result"
    For a given `k`, when updating `f[k][x][y]`, the elements involved always come from row `k` and column `k` of the array `f[k-1]`. Then we notice that for a given `k`, when updating `f[k][k][y]` or `f[k][x][k]`, the value never changes, because by the formula `f[k][k][y] = min(f[k-1][k][y], f[k-1][k][k]+f[k-1][k][y])`, `f[k-1][k][k]` is 0, so this value is always `f[k-1][k][y]`; the proof for `f[k][x][k]` is similar.
    
    Therefore, if the first dimension is dropped, for a given `k` none of the elements used in the update of any element has been updated in this iteration, so dropping the first dimension does not affect the result.

=== "C++"
    ```cpp
    for (k = 1; k <= n; k++) {
      for (x = 1; x <= n; x++) {
        for (y = 1; y <= n; y++) {
          f[x][y] = min(f[x][y], f[x][k] + f[k][y]);
        }
      }
    }
    ```

=== "Python"
    ```python
    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                f[x][y] = min(f[x][y], f[x][k] + f[k][y])
    ```

In total, the time complexity is $O(N^3)$ and the space complexity is $O(N^2)$.

### Applications

???+ question "Given an undirected graph with positive weights, find a cycle with the minimum total weight."
    First, this must be a simple cycle.
    
    Think about how this cycle is formed.
    
    Consider the vertex $u$ with the largest index on the cycle.
    
    `f[u-1][x][y]` together with $(u,x)$, $(u,y)$ forms the cycle.
    
    Enumerate $u$ during Floyd's algorithm and compute the minimum of this sum.
    
    The time complexity is $O(n^3)$.
    
    See the [Minimum cycle](./min-cycle.md) section for more.

???+ question "Given, for a directed graph, whether there is an edge between any two vertices, decide whether any two vertices are connected."
    This problem is computing the **transitive closure of the graph**.
    
    We just follow Floyd's procedure, adding the vertices one by one.
    
    Only now the edge weights become $1/0$, and taking $\min$ becomes the **or** operation.
    
    With a further bitset optimization, the complexity becomes $O(\frac{n^3}{w})$.
    
    ```cpp
    // std::bitset<SIZE> f[SIZE];
    for (k = 1; k <= n; k++)
      for (i = 1; i <= n; i++)
        if (f[i][k]) f[i] = f[i] | f[k];
    ```

## Bellman–Ford algorithm

The Bellman–Ford algorithm is a shortest path algorithm based on the relaxation operation; it can find shortest paths in graphs with negative weights and detect the case where no shortest path exists.

The "SPFA" you may have heard of in the Chinese OI community is one implementation of the Bellman–Ford algorithm.

### Procedure

We first introduce the relaxation operation used by the Bellman–Ford algorithm (Dijkstra's algorithm uses relaxation too).

For an edge $(u,v)$, relaxation corresponds to the formula $dis(v) = \min(dis(v), dis(u) + w(u, v))$.

The meaning is obvious: we try to use the path $S \to u \to v$ (where the shortest path is taken for $S \to u$) to update the shortest distance of vertex $v$; if this path is better, we update.

What the Bellman–Ford algorithm does is keep trying to relax every edge of the graph. In every round of the loop we try to relax all edges of the graph once; when a round has no successful relaxation, the algorithm stops.

Each round is $O(m)$; how many rounds can there be at most?

If the shortest paths exist, since one relaxation increases the number of edges of a shortest path by at least $1$, and a shortest path has at most $n-1$ edges, the whole algorithm performs at most $n-1$ rounds of relaxation. Hence the total time complexity is $O(nm)$.

There is one more case: if starting from $S$ we reach a negative cycle, the relaxations go on forever. Note that the argument above already showed that for a graph where the shortest paths exist, relaxation runs at most $n-1$ rounds; so if in the $n$-th round there is still an edge that can be relaxed, a negative cycle is reachable from $S$.

???+ warning "A common misconception in negative cycle detection"
    Note that when running Bellman–Ford with $S$ as the source, if it does not report a negative cycle, this only means that no negative cycle is reachable from $S$, not that the graph has no negative cycle.
    
    Therefore, to decide whether the whole graph contains a negative cycle, the most rigorous approach is to create a super source, connect it to every vertex of the graph with an edge of weight 0, and run Bellman–Ford from the super source.

### Implementation

??? note "Reference implementation"
    === "C++"
        ```cpp
        struct Edge {
          int u, v, w;
        };
        
        vector<Edge> edge;
        
        int dis[MAXN], u, v, w;
        constexpr int INF = 0x3f3f3f3f;
        
        bool bellmanford(int n, int s) {
          memset(dis, 0x3f, (n + 1) * sizeof(int));
          dis[s] = 0;
          bool flag = false;  // whether a relaxation happened during this round
          for (int i = 1; i <= n; i++) {
            flag = false;
            for (int j = 0; j < edge.size(); j++) {
              u = edge[j].u, v = edge[j].v, w = edge[j].w;
              if (dis[u] == INF) continue;
              // infinity plus or minus a constant is still infinity
              // so edges leaving a vertex with shortest distance INF cannot relax
              if (dis[v] > dis[u] + w) {
                dis[v] = dis[u] + w;
                flag = true;
              }
            }
            // stop the algorithm when no edge can be relaxed
            if (!flag) {
              break;
            }
          }
          // if relaxation is still possible in round n, a negative cycle is reachable from s
          return flag;
        }
        ```
    
    === "Python"
        ```python
        class Edge:
            def __init__(self, u=0, v=0, w=0):
                self.u = u
                self.v = v
                self.w = w
        
        
        INF = 0x3F3F3F3F
        edge = []
        
        
        def bellmanford(n, s):
            dis = [INF] * (n + 1)
            dis[s] = 0
            for i in range(1, n + 1):
                flag = False
                for e in edge:
                    u, v, w = e.u, e.v, e.w
                    if dis[u] == INF:
                        continue
                    # infinity plus or minus a constant is still infinity
                    # so edges leaving a vertex with shortest distance INF cannot relax
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        flag = True
                # stop the algorithm when no edge can be relaxed
                if not flag:
                    break
            # if relaxation is still possible in round n, a negative cycle is reachable from s
            return flag
        ```

### Queue optimization: SPFA

That is, the Shortest Path Faster Algorithm.

Often we do not need that many useless relaxations.

Obviously, only the edges leaving vertices relaxed in the previous step can cause the next relaxation.

So if we maintain with a queue "which vertices may cause a relaxation", we only visit the necessary edges.

SPFA can also decide whether a negative cycle is reachable from $s$: just record how many edges the shortest path passes through; when it passes through at least $n$ edges, a negative cycle is reachable from $s$.

??? note "Implementation"
    === "C++"
        ```cpp
        struct edge {
          int v, w;
        };
        
        vector<edge> e[MAXN];
        int dis[MAXN], cnt[MAXN], vis[MAXN];
        queue<int> q;
        
        bool spfa(int n, int s) {
          memset(dis, 0x3f, (n + 1) * sizeof(int));
          dis[s] = 0, vis[s] = 1;
          q.push(s);
          while (!q.empty()) {
            int u = q.front();
            q.pop(), vis[u] = 0;
            for (auto ed : e[u]) {
              int v = ed.v, w = ed.w;
              if (dis[v] > dis[u] + w) {
                dis[v] = dis[u] + w;
                cnt[v] = cnt[u] + 1;  // number of edges on the shortest path
                if (cnt[v] >= n) return false;
                // without a negative cycle a shortest path has at most n - 1 edges
                // so if it has more than n edges it must pass through a negative cycle
                if (!vis[v]) q.push(v), vis[v] = 1;
              }
            }
          }
          return true;
        }
        ```
    
    === "Python"
        ```python
        from collections import deque
        
        
        class Edge:
            def __init__(self, v=0, w=0):
                self.v = v
                self.w = w
        
        
        e = [[Edge() for i in range(MAXN)] for j in range(MAXN)]
        INF = 0x3F3F3F3F
        
        
        def spfa(n, s):
            dis = [INF] * (n + 1)
            cnt = [0] * (n + 1)
            vis = [False] * (n + 1)
            q = deque()
        
            dis[s] = 0
            vis[s] = True
            q.append(s)
            while q:
                u = q.popleft()
                vis[u] = False
                for ed in e[u]:
                    v, w = ed.v, ed.w
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        cnt[v] = cnt[u] + 1  # number of edges on the shortest path
                        if cnt[v] >= n:
                            return False
                        # without a negative cycle a shortest path has at most n - 1 edges
                        # so if it has more than n edges it must pass through a negative cycle
                        if not vis[v]:
                            q.append(v)
                            vis[v] = True
        ```

Although SPFA runs fast in most cases, its worst-case time complexity is $O(nm)$, and it is not hard to construct tests that force this complexity, so use it with care in contests (without negative edges it is best to use Dijkstra's algorithm; with negative edges and no special properties of the graph, if SPFA is part of the intended solution, the problem should not have constraints that the Bellman–Ford algorithm cannot pass).

???+ note "Other optimizations of Bellman–Ford"
    Besides the queue optimization (SPFA), Bellman–Ford has other optimizations; they are effective on some graphs, but on certain special graphs the worst-case complexity may become exponential.
    
    -   Heap optimization: replace the queue with a heap; the difference from Dijkstra is that a vertex may enter the queue several times. On graphs with negative edges it can be forced to exponential complexity.
    -   Stack optimization: replace the queue with a stack (i.e. turn the BFS into a DFS); it may be more efficient when looking for a negative cycle, but the worst-case time complexity is still exponential.
    -   LLL optimization: replace the plain queue with a deque; each time a vertex is pushed, compare its distance with the average distance in the queue: if it is larger, insert it at the back, otherwise at the front.
    -   SLF optimization: replace the plain queue with a deque; each time a vertex is pushed, compare its distance with the front of the queue: if it is larger, insert it at the back, otherwise at the front.
    -   D´Esopo–Pape algorithm: replace the plain queue with a deque; if a vertex has never been in the queue before, insert it at the back, otherwise at the front.
    
    For more optimizations and ways of hacking them, see [fstqwq's answer on Zhihu](https://www.zhihu.com/question/292283275/answer/484871888).

## Dijkstra's algorithm

Dijkstra's (/ˈdikstrɑ/ or /ˈdɛikstrɑ/) algorithm was discovered by the Dutch computer scientist E. W. Dijkstra in 1956 and published in 1959. It is an algorithm for single-source shortest paths in **graphs with non-negative weights**.

### Procedure

Split the vertices into two sets: the vertices whose shortest distance has been determined (set $S$) and the vertices whose shortest distance has not yet been determined (set $T$). Initially all vertices belong to $T$.

Initialize $dis(s)=0$ and $dis$ of all other vertices to $+\infty$.

Then repeat the following:

1.  From the set $T$, pick the vertex with the smallest shortest distance and move it to the set $S$.
2.  Relax all outgoing edges of the vertex just added to $S$.

The algorithm ends when the set $T$ is empty.

### Time complexity

The naive implementation, after each operation 2, searches the set $T$ by brute force for the vertex with the smallest shortest distance. The total time complexity of operation 2 is $O(m)$, that of operation 1 is $O(n^2)$, and the whole process takes $O(n^2 + m) = O(n^2)$.

The process can be optimized with a heap: every time an edge $(u,v)$ is successfully relaxed, insert $v$ into the heap (if $v$ is already in the heap, perform Decrease-key directly), and operation 1 simply takes the top of the heap. There are $O(m)$ Decrease-key operations and $O(n)$ pops in total; different heaps give different complexities, see the [Heap](../ds/heap.md) page. The best complexity achievable by heap optimization is $O(n\log n+m)$, achieved for instance by Fibonacci heaps.

In particular, a priority queue can be used; then Decrease-key cannot be performed, but the vertex can be re-inserted at every relaxation, and when popping we check whether the vertex has already been processed and skip it if so; the complexity is $O(m\log n)$, and the advantage is a simpler implementation.

The heap here can also be implemented with a segment tree, with complexity $O(m\log n)$; with some special non-recursive segment tree implementations the constant is smaller than with a heap. Moreover, a segment tree supports more operations, and some special graph problems can only be maintained with a segment tree.

On sparse graphs, $m = O(n)$, heap-optimized Dijkstra has a considerable efficiency advantage; on dense graphs, $m = O(n^2)$, the naive implementation is better.

### Proof of correctness

We prove the correctness of Dijkstra's algorithm by mathematical induction under the assumption that **all edge weights are non-negative**[^1].

Simply put, we need to prove that when operation 1 is performed, the shortest distance of the extracted vertex $u$ has already been determined, i.e. $D(u) = dis(u)$ holds.

Initially $S = \varnothing$ and the claim holds.

We proceed by contradiction.

Let $u$ be the first vertex in the algorithm for which $D(u) = dis(u)$ does not hold when it is added to $S$. Since $s$ certainly satisfies $D(u)=dis(u)=0$ and it is certainly the first vertex added to $S$, we have $S \neq \varnothing$ before adding $u$ to $S$; if there is no path from $s$ to $u$, then $D(u) = dis(u) = +\infty$, contradicting the assumption.

So there must be a path $s \to x \to y \to u$, where $y$ is the first vertex on the path $s \to u$ that belongs to $T$ and $x$ is the predecessor of $y$ (obviously $x \in S$). Note that $s = x$ or $y = u$ is possible, i.e. $s \to x$ or $y \to u$ may be an empty path.

Since all vertices added before $u$ satisfy $D(u) = dis(u)$, when $x$ was added to $S$ we had $D(x) = dis(x)$, and at that time the edge $(x,y)$ was relaxed; hence we can prove that when $u$ is added to $S$, $D(y)=dis(y)$ must hold.

Now we prove that $D(u) = dis(u)$ holds. On the path $s \to x \to y \to u$, since all edge weights are non-negative, $D(y) \leq D(u)$. Thus $dis(y) = D(y) \leq D(u)\leq dis(u)$. But when $u$ was taken out of $T$ in operation 1, $y$ had not yet been taken out of $T$, so at that moment $dis(u)\leq dis(y)$; hence $dis(y) = D(y) = D(u) = dis(u)$, contradicting the assumption $D(u)\neq dis(u)$, so the assumption is false.

Thus we have proved that the shortest distance of every vertex extracted in operation 1 has already been determined. The claim is proved.

Note that the key inequality $D(y) \leq D(u)$ in the proof was derived under the condition that all edge weights are non-negative. When the graph contains negative edges, this inequality no longer holds, the correctness of Dijkstra's algorithm is not guaranteed, and the algorithm may give wrong results.

### Implementation

Here we give both the $O(n^2)$ brute-force implementation and the $O(m \log m)$ priority queue implementation.

???+ note "Naive implementation"
    === "C++"
        ```cpp
        struct edge {
          int v, w;
        };
        
        vector<edge> e[MAXN];
        int dis[MAXN], vis[MAXN];
        
        void dijkstra(int n, int s) {
          memset(dis, 0x3f, (n + 1) * sizeof(int));
          dis[s] = 0;
          for (int i = 1; i <= n; i++) {
            int u = 0, mind = 0x3f3f3f3f;
            for (int j = 1; j <= n; j++)
              if (!vis[j] && dis[j] < mind) u = j, mind = dis[j];
            vis[u] = true;
            for (auto ed : e[u]) {
              int v = ed.v, w = ed.w;
              if (dis[v] > dis[u] + w) dis[v] = dis[u] + w;
            }
          }
        }
        ```
    
    === "Python"
        ```python
        class Edge:
            def __init__(self, v=0, w=0):
                self.v = v
                self.w = w
        
        
        e = [[Edge() for i in range(MAXN)] for j in range(MAXN)]
        INF = 0x3F3F3F3F
        
        
        def dijkstra(n, s):
            dis = [INF] * (n + 1)
            vis = [0] * (n + 1)
        
            dis[s] = 0
            for i in range(1, n + 1):
                u = 0
                mind = INF
                for j in range(1, n + 1):
                    if not vis[j] and dis[j] < mind:
                        u = j
                        mind = dis[j]
                vis[u] = True
                for ed in e[u]:
                    v, w = ed.v, ed.w
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
        ```

???+ note "Priority queue implementation"
    === "C++"
        ```cpp
        struct edge {
          int v, w;
        };
        
        struct node {
          int dis, u;
        
          bool operator>(const node& a) const { return dis > a.dis; }
        };
        
        vector<edge> e[MAXN];
        int dis[MAXN], vis[MAXN];
        priority_queue<node, vector<node>, greater<node>> q;
        
        void dijkstra(int n, int s) {
          memset(dis, 0x3f, (n + 1) * sizeof(int));
          memset(vis, 0, (n + 1) * sizeof(int));
          dis[s] = 0;
          q.push({0, s});
          while (!q.empty()) {
            int u = q.top().u;
            q.pop();
            if (vis[u]) continue;
            vis[u] = 1;
            for (auto ed : e[u]) {
              int v = ed.v, w = ed.w;
              if (dis[v] > dis[u] + w) {
                dis[v] = dis[u] + w;
                q.push({dis[v], v});
              }
            }
          }
        }
        ```
    
    === "Python"
        ```python
        def dijkstra(e, s):
            """
            Input:
            e: adjacency list
            s: source vertex
            Returns:
            dis: shortest distances from s to every vertex
            """
            dis = defaultdict(lambda: float("inf"))
            dis[s] = 0
            q = [(0, s)]
            vis = set()
            while q:
                _, u = heapq.heappop(q)
                if u in vis:
                    continue
                vis.add(u)
                for v, w in e[u]:
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        heapq.heappush(q, (dis[v], v))
            return dis
        ```

## Johnson's all-pairs shortest path algorithm

Johnson's algorithm, like Floyd's, finds the shortest paths between any two vertices of a graph without negative cycles. It was proposed by Donald B. Johnson in 1977.

All-pairs shortest paths can be found by enumerating the source and running the Bellman–Ford algorithm $n$ times, with time complexity $O(n^2m)$, or directly with Floyd's algorithm, with time complexity $O(n^3)$.

Note that heap-optimized Dijkstra has a better time complexity for single-source shortest paths than Bellman–Ford; if we enumerate the source and run Dijkstra's algorithm $n$ times, the problem is solved in $O(nm\log m)$ time (depending on the implementation of Dijkstra's algorithm), which is better than running Bellman–Ford $n$ times, and on sparse graphs also better than Floyd's algorithm.

But Dijkstra's algorithm cannot correctly compute shortest paths with negative edges, so we need to preprocess the edges of the original graph to make sure all edge weights are non-negative.

An idea that comes to mind easily is to add the same positive number $x$ to all edge weights, making them all non-negative. If the shortest path from the start to the end in the new graph passes through $k$ edges, subtracting $kx$ from it gives the actual shortest path.

But this method is wrong. Consider the following graph:

![](./images/shortest-path1.svg)

The shortest path $1 \to 2$ is $1 \to 5 \to 3 \to 2$, of length $−2$.

But what if we add $5$ to every edge weight?

![](./images/shortest-path2.svg)

The shortest path $1 \to 2$ in the new graph is $1 \to 4 \to 2$, which is no longer the actual shortest path.

Johnson's algorithm relabels the edge weights in a different way.

We create a virtual vertex (here we give it the index $0$). From this vertex we add an edge of weight $0$ to every other vertex.

Next we use the Bellman–Ford algorithm to compute the shortest distances from vertex $0$ to all other vertices, denoted $h_i$.

If there is an edge from $u$ to $v$ with weight $w$, we reset its weight to $w+h_u-h_v$.

Then we run $n$ rounds of Dijkstra's algorithm with every vertex as the source, obtaining the shortest paths between all pairs of vertices.

The initial Bellman–Ford run is not the time bottleneck; if Dijkstra's algorithm is implemented with a `priority_queue`, the time complexity of the algorithm is $O(nm\log m)$.

### Proof of correctness

Why is this way of relabeling the edge weights correct?

Before discussing this, let us first discuss a concept from physics — potential energy.

Potential energies such as gravitational potential energy and electric potential energy share a property: the change in potential energy depends only on the relative positions of the start and end points, not on the path taken between them.

Potential energy has another property: its absolute value usually depends on the chosen zero point, but no matter where the zero point is set, the difference in potential energy between two points is fixed.

Back to the topic.

In the relabeled graph, the length of a path $s \to p_1 \to p_2 \to \dots \to p_k \to t$ from $s$ to $t$ is:

$(w(s,p_1)+h_s-h_{p_1})+(w(p_1,p_2)+h_{p_1}-h_{p_2})+ \dots +(w(p_k,t)+h_{p_k}-h_t)$

Simplifying gives:

$w(s,p_1)+w(p_1,p_2)+ \dots +w(p_k,t)+h_s-h_t$

Whichever path we take from $s$ to $t$, the value of $h_s-h_t$ does not change, which matches exactly the property of potential energy!

For convenience, we will call $h_i$ the potential of vertex $i$.

The expression for the length of the shortest path $s \to t$ in the new graph consists of two parts: the first, the sum of edge weights, is the shortest path $s \to t$ in the original graph, and the second is the potential difference between the two vertices. Since the potential difference between two vertices is fixed, the shortest path $s \to t$ in the original graph corresponds to the shortest path $s \to t$ in the new graph.

At this point half of the correctness proof is done — we have shown that the shortest path in the graph with relabeled weights is still the original shortest path. Next we need to show that all edge weights in the new graph are non-negative, because on a graph with non-negative weights Dijkstra's algorithm is guaranteed to give the correct result.

By the triangle inequality, for any edge $(u,v)$ of the graph, its endpoints satisfy $h_v \leq h_u + w(u,v)$. The relabeled weight of this edge is $w'(u,v)=w(u,v)+h_u-h_v \geq 0$. Thus we have shown that all edge weights in the new graph are non-negative.

This proves the correctness of Johnson's algorithm.

## Comparison of the methods

| Shortest path algorithm | Floyd | Bellman–Ford | Dijkstra | Johnson |
| ------- | ---------- | ------------ | ------------ | ------------- |
| Type of shortest path | all pairs | single source | single source | all pairs |
| Applies to | any graph | any graph | non-negative weights | any graph |
| Detects negative cycles? | yes | yes | no | yes |
| Time complexity | $O(N^3)$ | $O(NM)$ | $O(M\log M)$ | $O(NM\log M)$ |

Note: the complexity of Dijkstra's algorithm in the table assumes a `priority_queue` implementation.

## Printing the solution

Keep a `pre` array and, when updating a distance, record where the next vertex was reached from; before the algorithm ends, print the path recursively.

For example, Floyd records `pre[i][j] = k;`, while Bellman–Ford and Dijkstra usually record `pre[v] = u`.

## Some special cases

-   Shortest paths in graphs whose edge weights are only $0$ and $1$: [0-1 BFS](./bfs.md#double-ended-queue-bfs);
-   Shortest path problems that allow changing the path cost at most $k$ times and the like: [Shortest paths in layered graphs](./node.md#shortest-path-in-a-layered-graph).

## References and notes

[^1]: Introduction to Algorithms (3rd edition, Chinese translation), China Machine Press, 2013, pp. 384–385.
