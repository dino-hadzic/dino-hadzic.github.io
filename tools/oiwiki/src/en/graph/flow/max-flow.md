---
title: Maximum flow
---

This page mainly introduces the algorithms related to the maximum flow problem.

## Overview

For the basic concepts of network flow, see [Introduction to network flow](../flow.md).

Let $G=(V,E)$ be a network with a source and a sink; we want to assign a suitable flow $f$ on $G$ that maximizes the total flow of the network $|f|$ (i.e. $\sum_{x \in V} f(s, x) - \sum_{x \in V} f(x, s)$). This problem is called the maximum flow problem.

## Ford–Fulkerson augmentation

Ford–Fulkerson augmentation is the collective name for a class of algorithms that compute a maximum flow. The method uses a greedy idea: it updates and solves the maximum flow by finding augmenting paths.

### Overview

Given a network $G$ and a flow $f$ on $G$, we make the following definitions.

For an edge $(u, v)$, we call the difference between its capacity and its flow the residual capacity $c_f(u,v)$, i.e. $c_f(u,v)=c(u,v)-f(u,v)$.

We call the subgraph of $G$ consisting of all vertices and the edges with residual capacity greater than $0$ the residual network $G_f$, i.e. $G_f=(V,E_f)$, where $E_f=\left\{(u,v) \mid c_f(u,v)>0\right\}$.

???+ warning "Warning"
    As we are about to mention, flow may be negative, so the edges of $E_f$ may not be in $E$. After introducing the notion of augmentation, this will be explained concretely below.

We call a path from the source $s$ to the sink $t$ in $G_f$ an augmenting path. For an augmenting path, we add the same amount of flow to every edge $(u, v)$ so that the total flow of the network increases; this process is called augmentation. Thus the computation of a maximum flow can be viewed as the superposition of the flows obtained by a sequence of augmentations.

In addition, during Ford–Fulkerson augmentation, for every edge $(u, v)$ we also create a reverse edge $(v, u)$. We stipulate $f(u, v) = -f(v, u)$; this property can be guaranteed by introducing a flow-canceling operation at every augmentation, i.e. when $f(u, v)$ increases, $f(v, u)$ should decrease by the same amount.

???+ tip "Tip"
    In code implementations of maximum flow algorithms, we usually need to support fast access to the reverse edge. In an adjacency matrix this operation is trivial ($g_{u, v} \leftrightarrow g_{v, u}$). But the mainstream implementation is the superior linked adjacency list (chained forward star). A common trick is to number the edges starting from an even number (usually $0$) and, when adding an edge, to always add its reverse edge immediately afterwards so that their indices are adjacent. Thus the edge with index $i$ and the edge with index $i \oplus 1$ are always reverse edges of each other.

Readers encountering this method for the first time may notice a counterintuitive situation: the flow $f(v, u)$ of a reverse edge may be negative. In fact, we can observe that during Ford–Fulkerson augmentation what really matters is the residual capacity $c_f$, while the absolute value of $f(v, u)$ is irrelevant; we can regard the decrease of the reverse edge's flow as an increase of the reverse edge's residual capacity $c_f(v, u)$ — which agrees with the meaning of flow canceling — an increase in the reverse edge's residual capacity means that later we may traverse the reverse edge to cancel the earlier forward augmentation, representing a kind of "regret" operation.

The following example may help you understand the process. Suppose $G$ is a unit-capacity network and consider the following process:

-   There are several augmenting paths on $G$; among them, we choose to perform an augmentation passing through $u, v$ in turn (as in the left figure), and the flow increases by $1$.
-   We notice that if we performed the augmentation in the middle figure, the local maximum flow would be $2$ rather than $1$. But since the edge into $u$ and the edge out of $v$ exhausted their capacity in the first augmentation, we cannot now perform the augmentation of the middle figure. This means our current flow is not good enough, but locally there may be no other augmenting path (using only edges of the original graph and no reverse edges).
-   Now introduce the flow-canceling operation. After the first augmentation, canceling means $c_f(v, u)$ gained $1$ unit of residual capacity, which is equivalent to adding the edge $(v, u)$, so we can perform another augmentation passing through $p, v, u, q$ in turn (the orange path in the right figure). The flows on the undirected edge $(u, v)$ cancel out between the two augmentations, and we are surprised to find that the superposition of the two augmentations is actually equivalent to the middle figure.

![](./images/flow2.png)

The example above tells us that the "canceling" effect brought by the flow-canceling operation means we need not worry about having chosen augmenting paths in the "wrong" order.

It is easy to see that as long as an augmenting path exists on $G_f$, augmenting along it increases the total flow; otherwise the total flow has reached its maximum possible value and the computation is complete. This is the process of Ford–Fulkerson augmentation.

### Max-flow min-cut theorem

We have roughly understood the idea of Ford–Fulkerson augmentation, but how do we prove the correctness of this method? Why is the flow $f$ after augmentation finishes a maximum flow?

In fact, the correctness of Ford–Fulkerson augmentation is equivalent to the max-flow min-cut theorem. This theorem states that for any network $G = (V, E)$, its maximum flow $f$ and minimum cut $\{S, T\}$ always satisfy $|f| = ||S, T||$.

To prove the max-flow min-cut theorem, we start from a lemma: for a network $G = (V, E)$, take any flow $f$ and any cut $\{S, T\}$; then always $|f| \leq ||S, T||$, where equality holds if and only if all edges of $\{(u, v) | u \in S, v \in T\}$ are saturated and all edges of $\{(u, v) | u \in T, v \in S\}$ are empty.

???+ note "Proof"
    $$
    \begin{aligned}
    |f| & = f(s) \\
        & = \sum_{u \in S} f(u) \\
        & = \sum_{u \in S} \left( \sum_{v \in V} f(u, v) - \sum_{v \in V} f(v, u) \right) \\
        & = \sum_{u \in S} \left( \sum_{v \in T} f(u, v) + \sum_{v \in S} f(u, v) - \sum_{v \in T} f(v, u) - \sum_{v \in S} f(v, u) \right) \\
        & = \sum_{u \in S} \left( \sum_{v \in T} f(u, v) - \sum_{v \in T} f(v, u) \right) + \sum_{u \in S} \sum_{v \in S} f(u, v) - \sum_{u \in S} \sum_{v \in S} f(v, u) \\
        & = \sum_{u \in S} \left( \sum_{v \in T} f(u, v) - \sum_{v \in T} f(v, u) \right) \\
        & \leq \sum_{u \in S} \sum_{v \in T} f(u, v) \\
        & \leq \sum_{u \in S} \sum_{v \in T} c(u, v) \\
        & = ||S, T|| \\
    \end{aligned}
    $$
    
    For equality, the first inequality requires all edges of $\{(u, v) \mid u \in T, v \in S\}$ to be empty, and the second requires all edges of $\{(u, v) \mid u \in S, v \in T\}$ to be saturated. This proves the lemma.

So, for an arbitrary network, can the equality condition above always be satisfied? If the answer is yes, the max-flow min-cut theorem is proved. We attempt a proof below.

???+ note "Proof"
    Suppose that after some round of augmentation we obtain a flow $f$ such that no augmenting path exists on $G_f$, i.e. there is no path from $s$ to $t$ on $G_f$. Let $S$ be the set of vertices reachable from $s$, and let $T = V \setminus S$.
    
    Clearly $\{S, T\}$ is a cut of $G_f$, and $||S, T|| = \sum_{u \in S} \sum_{v \in T} c_f(u, v) = 0$. Since residual capacities are non-negative, this also means that for all $u \in S, v \in T, (u, v) \in E_f$, we have $c_f(u, v) = 0$. We split these edges into two cases: edges that exist in the original graph and reverse edges:
    
    -   $(u, v) \in E$: then $c_f(u, v) = c(u, v) - f(u, v) = 0$, hence $c(u, v) = f(u, v)$, i.e. all edges of $\{(u, v) \mid u \in S, v \in T\}$ are saturated;
    -   $(v, u) \in E$: then $c_f(u, v) = c(u, v) - f(u, v) = 0 - f(u, v) = f(v, u) = 0$, i.e. all edges of $\{(v, u) \mid u \in S, v \in T\}$ are empty.
    
    Therefore, after augmentation stops, the flow $f$ above satisfies the equality condition. By the size relation stated in the lemma, naturally $f$ is a maximum flow of $G$ and $\{S, T\}$ is a minimum cut of $G$.

It is easy to see that Kőnig's theorem is a special case of the max-flow min-cut theorem. In fact, both are related to duality in linear programming.

### Time complexity analysis

On a network $G = (V, E)$ with integer flows, trivially assuming that the flow of every augmentation is an integer, an upper bound on the time complexity of Ford–Fulkerson augmentation is $O(|E||f|)$, where $f$ is the maximum flow on $G$. This is because a single round of augmentation takes $O(|E|)$, and augmentation increases the total flow, so the number of rounds cannot exceed $|f|$.

Different implementations of Ford–Fulkerson augmentation have different time complexities. The more mainstream implementations include the Edmonds–Karp, Dinic, SAP, ISAP and other algorithms, which we introduce one by one below.

### Edmonds–Karp algorithm

#### Idea

How do we find an augmenting path in $G_f$? When considering a concrete implementation of Ford–Fulkerson augmentation, the most natural choice is BFS. Then Ford–Fulkerson augmentation becomes the Edmonds–Karp algorithm. Its concrete procedure is as follows:

-   If on $G_f$ we can reach $t$ from $s$ by BFS, we have found a new augmenting path.

-   For the augmenting path $p$, we compute the minimum residual capacity of the edges on $p$, $\Delta = \min_{(u, v) \in p} c_f(u, v)$. We add $\Delta$ flow to every edge on $p$ and cancel $\Delta$ flow on their reverse edges, increasing the maximum flow by $\Delta$.

-   Since we modified the flow, we get a new $G_f$; we repeat the process above on the new $G_f$ until no augmenting path exists, at which point the flow no longer increases.

The algorithm above is the Edmonds–Karp algorithm.

#### Time complexity analysis

Next let us try to analyze the time complexity of the Edmonds–Karp algorithm.

Clearly, a single round of BFS augmentation takes $O(|E|)$.

The upper bound on the total number of augmentation rounds is $O(|V||E|)$. This claim is often falsely proved (or vaguely skipped) in online materials. Below we attempt to give a more formal proof[^ref_ek].

???+ note "Proof of the upper bound on the total number of augmentation rounds"
    First, we introduce a lemma — the shortest-path non-decreasing lemma. Specifically, let $d_f(u)$ denote the distance (i.e. shortest path length, likewise below) from vertex $u$ to the source $s$ on $G_f$. For some round of augmentation, let $f$ and $f'$ denote the flow before and after the augmentation respectively; we claim that for any vertex $u$, augmentation always yields $d_{f'}(u) \geq d_f(u)$. We will prove this lemma shortly.
    
    Call the edge with the minimum residual capacity on an augmenting path the saturated edge (if several edges attain the minimum, take any one). If a directed edge $(u, v)$ is chosen as the saturated edge, augmentation clears its residual capacity so the saturated edge disappears, and flow canceling adds a new reverse edge (if the reverse edge did not exist before), i.e. $(u, v) \not \in E_{f'}$ and $(v, u) \in E_{f'}$. The analysis above tells us that for an undirected edge $(u, v)$, the two directions in which it is augmented always alternate.
    
    When augmenting along $(u, v)$ on $G_f$, $d_f(u) + 1 = d_f(v)$, after which the residual network becomes $G_{f'}$. When augmenting along $(v, u)$ on $G_{f'}$, $d_{f'}(v) + 1 = d_{f'}(u)$. By the shortest-path non-decreasing lemma we also have $d_{f'}(v) \geq d_f(v)$; chaining all the relations, we get $d_{f'}(u) \geq d_{f}(u) + 2$. In other words, if the directed edge $(u, v)$ is chosen as the saturated edge, then compared with the last time it was chosen as the saturated edge, the distance from $u$ to $s$ has increased by at least $2$.
    
    The distance from $s$ to any vertex cannot exceed $|V|$; combined with the property above, we find that the number of times each edge is chosen as the saturated edge is $O(|V|)$, and multiplying by the number of edges gives the upper bound $O(|V||E|)$ on the total number of augmentation rounds.
    
    Next we prove the shortest-path non-decreasing lemma, i.e. $d_{f'}(u) \geq d_f(u)$. This proof is not hard, but may be slightly convoluted; readers may pause and think carefully for a moment.
    
    ???+ note "Proof of the shortest-path non-decreasing lemma"
        We argue by contradiction. For some round of augmentation, suppose there are several vertices whose distance to $s$ decreases after this round compared with before. Let $v$ be the one among them with the smallest distance to $s$ (i.e. $v = \arg \min_{x \in V, d_{f'}(x) < d_f(x)} d_{f'}(x)$). Note that by the contradiction hypothesis, $d_{f'}(v) < d_f(v)$ is a known condition.
        
        On the shortest path from $s$ to $v$ in $G_{f'}$, let $u$ be the vertex preceding $v$, i.e. $d_{f'}(u) + 1 = d_{f'}(v)$.
        
        For $u$ not to break the "smallest distance" property of $v$, $u$ must satisfy $d_{f'}(u) \geq d_f(u)$.
        
        Adding the same amount to both sides of this inequality, we get $d_{f'}(v) \geq d_f(u) + 1$. Relaxing according to the contradiction hypothesis, we get $d_f(v) > d_f(u) + 1$.
        
        Below we discuss the direction of augmentation on $(u, v)$.
        
        -   Suppose the directed edge $(u, v) \in E_f$. By the "breadth-first" property of BFS, we have $d_f(u) + 1 \geq d_f(v)$. This conflicts with the relaxed result, yielding a contradiction.
        -   Suppose the directed edge $(u, v) \not \in E_f$. By the definition of $u$ we already know $(u, v) \in E_{f'}$, so the existence of this edge must be the result of the current round's augmentation passing through $(v, u)$ and canceling flow to produce the reverse edge, i.e. $d_f(v) + 1 = d_f(u)$. This conflicts with the relaxed result, yielding a contradiction.
        
        Since augmenting $(u, v)$ in either direction leads to a contradiction, we know the contradiction hypothesis does not hold, and the shortest-path non-decreasing lemma is proved.

Multiplying the complexity of a single round of BFS augmentation by the upper bound on the number of rounds, we get that the time complexity of the Edmonds–Karp algorithm is $O(|V||E|^2)$.

#### Implementation

A possible implementation of the Edmonds–Karp algorithm is as follows.

??? note "Reference code"
    ```cpp
    constexpr int MAXN = 250;
    constexpr int INF = 0x3f3f3f3f;
    
    struct Edge {
      int from, to, cap, flow;
    
      Edge(int u, int v, int c, int f) : from(u), to(v), cap(c), flow(f) {}
    };
    
    struct EK {
      int n, m;             // n: number of vertices, m: number of edges
      vector<Edge> edges;   // edges: the set of all edges
      vector<int> G[MAXN];  // G: vertex x -> indices in edges of all edges out of x
      int a[MAXN], p[MAXN];  // a: vertex x -> the maximum flow given to x by the edge that most recently reached x during BFS
                             // p: vertex x -> the edge that most recently reached x during BFS
    
      void init(int n) {
        for (int i = 0; i < n; i++) G[i].clear();
        edges.clear();
      }
    
      void AddEdge(int from, int to, int cap) {
        edges.push_back(Edge(from, to, cap, 0));
        edges.push_back(Edge(to, from, 0, 0));
        m = edges.size();
        G[from].push_back(m - 2);
        G[to].push_back(m - 1);
      }
    
      int Maxflow(int s, int t) {
        int flow = 0;
        for (;;) {
          memset(a, 0, sizeof(a));
          queue<int> Q;
          Q.push(s);
          a[s] = INF;
          while (!Q.empty()) {
            int x = Q.front();
            Q.pop();
            for (int i = 0; i < G[x].size(); i++) {  // iterate over edges starting at x
              Edge& e = edges[G[x][i]];
              if (!a[e.to] && e.cap > e.flow) {
                p[e.to] = G[x][i];  // G[x][i] is the edge that most recently reached e.to
                a[e.to] =
                    min(a[x], e.cap - e.flow);  // the flow given to e.to by the edge that most recently reached it
                Q.push(e.to);
              }
            }
            if (a[t]) break;  // if the sink received flow, exit the BFS
          }
          if (!a[t])
            break;  // if the sink received no flow, the source and sink are not in the same connected component
          for (int u = t; u != s;
               u = edges[p[u]].from) {  // trace the s -> t path from the BFS via u
            edges[p[u]].flow += a[t];      // increase the flow of the edges on the path
            edges[p[u] ^ 1].flow -= a[t];  // decrease the flow of the reverse edges
          }
          flow += a[t];
        }
        return flow;
      }
    };
    ```

### Dinic's algorithm

#### Idea

Consider performing a BFS layering of $G_f$ before augmenting, i.e. dividing the vertices into layers according to the distance $d(u)$ from vertex $u$ to the source $s$. We require that flow passing through $u$ may only go to vertices $v$ in the next layer, i.e. we delete the out-edges of $u$ leading to vertices with equal or smaller layer labels; we call the remaining part of $G_f$ the level graph. Formally, $G_L = (V, E_L)$ is the level graph of $G_f = (V, E_f)$, where $E_L = \left\{ (u, v) \mid (u, v) \in E_f, d(u) + 1 = d(v) \right\}$.

If on the level graph $G_L$ we find a maximal augmenting flow $f_b$ such that it is impossible to further enlarge $f_b$ using only $G_L$, we call $f_b$ a blocking flow of $G_L$.

??? warning "Warning"
    Although above we defined augmentation/augmenting flow only on a single augmenting path, in a broader sense the word "augmentation" refers not only to the augmenting flow on a single path but also to the union of several augmenting flows — it is the latter sense we use when defining the blocking flow.

Having defined the level graph and the blocking flow, the procedure of Dinic's algorithm is as follows.

1.  Build the level graph $G_L$ on $G_f$ by BFS.
2.  Find a blocking flow $f_b$ on $G_L$ by DFS.
3.  Merge $f_b$ into the existing flow $f$, i.e. $f \leftarrow f + f_b$.
4.  Repeat the above until no path from $s$ to $t$ exists.

The $f$ at that point is the maximum flow.

Before analyzing the complexity of this algorithm, we need to specifically explain the step "find a blocking flow $f_b$ on $G_L$ by DFS". Although the BFS for the level graph should be trivial for readers of this page, the DFS for the blocking flow needs a bit of technique — we need to introduce the current-arc optimization.

Note that during the DFS on $G_L$, if a vertex $u$ has a large number of in-edges and out-edges, and every time $u$ receives flow from an in-edge it scans the out-edge list to decide which out-edge to pass the flow to, then the local time complexity at $u$ can reach $O(|E|^2)$ in the worst case. To avoid this defect, if at some moment we already know that the edge $(u, v)$ has been augmented to its limit (the edge $(u, v)$ has no residual capacity left, or the part beyond $v$ has been augmented to blocking), there is no need for the flow at $u$ to try flowing to the out-edge $(u, v)$ again. Accordingly, for every vertex $u$ we maintain the first out-edge in $u$'s out-edge list that is still worth trying. Conventionally, we call this maintained pointer the current arc, and this technique the current-arc optimization.

??? note "Multi-path augmentation"
    Multi-path augmentation is a constant-factor optimization of Dinic's algorithm — if we have found an augmenting path $p$ from $s$ to $t$ on the level graph, then we do not necessarily need to start from $s$ again to find the next augmenting path; instead we may start from the last position on $p$ that still has residual capacity and look for a branch to augment. Considering its consistency with the form of backtracking, this optimization is also natural in a DFS implementation.
    
    ??? failure "Common misconception"
        Possibly due to wrong statements in many online materials being passed along, a considerable number of contestants like to list the current-arc optimization and multi-path augmentation side by side as the two optimizations of Dinic's algorithm. In fact, the current-arc optimization is part of what guarantees the correctness of Dinic's time complexity, while multi-path augmentation is merely a constant-factor optimization that does not affect the complexity.

#### Time complexity analysis

With the current-arc optimization applied, the time complexity analysis of Dinic's algorithm is as follows.

First, we try to prove that the time complexity of the DFS for the blocking flow in a single round of augmentation is $O(|V||E|)$.

???+ note "Proof of the time complexity of a single augmentation round"
    Consider each augmenting path in the blocking flow $f_b$; each is obtained by jumping along the current arc on $G_L$, and the number of jumps of each augmenting path cannot exceed $|V|$.
    
    Every time an augmenting path is found, a saturated edge disappears (its residual capacity is cleared). Consider each augmenting path in the blocking flow $f_b$; denote by $E_1$ the set of saturated edges they clear. Considering the layered nature of $G_L$, after a saturated edge disappears its reverse edge cannot be traversed by another augmenting path within the same augmentation round, so $E_1$ is a subset of $E_L$.
    
    In addition, for the cases where we jump along the current arc but fail to obtain an augmenting path because of blocking at some position, denote by $E_2$ the set of last edges on these incomplete paths. Members of $E_2$ are not saturated, so $E_1$ and $E_2$ are disjoint, and $E_1 \cup E_2$ is still a subset of $E_L$.
    
    Since each member of $E_1 \cup E_2$ costs no more than $|V|$ jumps (and with the multi-path augmentation optimization some jumps are counted multiple times), in summary, the total number of jumps during the DFS cannot exceed $|V||E_L|$.
    
    ??? failure "A common false proof"
        For every vertex, we maintain the next edge along which augmentation is possible, and the current arc changes at most $|E|$ times, so the worst-case time complexity of a single augmentation round is $O(|V||E|)$.
    
    ??? bug "Bug"
        "The current arc changes at most $|E|$ times" does not imply "each vertex visits its out-edges at most $|E|$ times". This is because visiting the current arc does not necessarily exhaust its residual capacity, so vertex $u$ may visit the same current arc multiple times.

Note that the number of layers of the level graph obviously cannot exceed $|V|$; if we can prove that the number of layers of the level graph strictly increases during augmentation, then the number of augmentation rounds of Dinic's algorithm is $O(|V|)$. Next we try to prove this conclusion[^ref_dinic].

???+ note "Proof of the monotonicity of the number of layers of the level graph"
    We need to introduce a concept from push-relabel algorithms (another class of maximum flow algorithms) — the height label. To state our proof more conveniently with height labels, in the proof we let $d_f(u)$ be the distance from vertex $u$ to the **sink** $t$ on $G_f$, and layer starting from the **sink** rather than the source (there is no essential difference). For some round of augmentation, we use $f$ and $f'$ to denote the flow before and after augmentation respectively. After computing and adding the blocking flow in this round, let the level graph change from $G_L = (V, E_L)$ to $G'_{L} = (V, E'_L)$.
    
    We give height labels a loose temporary definition — on a network $G = (V, E)$, let $h$ be a function from the vertex set $V$ to the set of integers $N$; $h$ is a valid height label on $G$ if and only if $h(u) \leq h(v) + 1$ holds for all $(u, v) \in E$.
    
    Examining all members $(u, v)$ of $E_{f'}$, we find that the reason for $(u, v) \in E_{f'}$ is one of the following two.
    
    -   $(u, v) \in E_f$ and its residual capacity was not exhausted during this round of augmentation — by the definition of shortest paths, in this case $d_f(u) \leq d_f(v) + 1$;
    -   $(u, v) \not \in E_f$, but during this round the blocking flow passed through $(v, u)$ and canceled flow to produce the reverse edge — by the definitions of the level graph and the blocking flow, in this case $d_f(u) + 1 = d_f(v)$.
    
    The observation above leads us to a conclusion — $d_f$ is a valid height label on $G_{f'}$. Of course, also on $G'_L$, a subgraph of $G_{f'}$.
    
    Now, for an augmenting path $p = (s, \dots, u, v, \dots, t)$ on $G'_L$, consider the process of starting from an empty path and adding one vertex at a time in the reverse order of the vertices on $p$ (from $t$ to $s$). Suppose vertex $v$ has been added and vertex $u$ is being added; we find that after adding $u$, by the definition of the level graph, the value of $d_{f'}(u)$ increases by $1$ relative to $d_{f'}(v)$; meanwhile, since $d_f$ is a height label on $G'_L$, the value of $d_f(u)$ may increase by $1$ relative to $d_f(v)$, or stay the same or decrease. Therefore, after the whole path has been added, we get $d_{f'}(s) \geq d_f(s)$, where equality holds if and only if $d_f(u) = d_f(v) + 1$ holds for all $(u, v) \in p$. If this inequality cannot be tight, then $d_{f'}(s) > d_f(s)$ — which is the conclusion we want, "the number of layers of the level graph strictly increases during augmentation". Below we try to prove that the inequality cannot be tight.
    
    Arguing by contradiction, we assume $d_{f'}(s) = d_f(s)$ holds and try to derive a contradiction. We now claim that on $G'_L$, $p$ contains at least one edge $(u, v)$ such that $(u, v)$ does not exist on $G_L$. If there were no such edge, considering $d_f(s) = d_{f'}(s)$ and combining the definitions of the level graph and the blocking flow, the augmentation on $G_L$ would not yet have been completed. To avoid this contradiction, our claim must be correct.
    
    Let $(u, v)$ be the edge satisfying the claim; the reason it satisfies the claim can only be one of the following two.
    
    -   $(u, v) \in E_f$ but $d_f(u) \leq d_f(v) + 1$ is not tight, so by the definition of the level graph $(u, v) \not \in E_L$, and it was added to $E'_L$ in the new round of re-layering after augmentation;
    -   $(u, v) \not \in E_f$, which means the edge $(u, v)$ was produced by the blocking flow of the current round passing through $(v, u)$ and canceling flow to create the reverse edge, i.e. $d_f(u) = d_f(v) - 1$.
    
    Since in whichever way the claim is satisfied we get $d_f(u) \neq d_f(v) + 1$, i.e. the necessary and sufficient condition for equality in $d_{f'}(s) \geq d_f(s)$ cannot be satisfied, this conflicts with the contradiction hypothesis $d_{f'}(s) = d_f(s)$, and the original proposition is proved.
    
    ??? failure "Another common false proof"
        Argue by contradiction. Suppose the number of layers of the level graph after a round of augmentation equals the previous one; then there should still be at least one augmenting path from $s$ to $t$ on the level graph in which the layer difference between adjacent vertices is $1$. That this augmenting path was not augmented shows the round of augmentation had not yet finished. To avoid the contradiction above, the original proposition holds.
    
    ??? bug "Bug"
        "The $s$-$t$ shortest path on the new level graph after a round of augmentation equals the previous one" does not imply "the round of augmentation on the old level graph had not yet finished". This is because there is no reason the edge sets of the two level graphs are the same; the $s$-$t$ shortest path on the new level graph may pass through edges that did not exist on the old level graph.

Multiplying the time complexity of a single augmentation round $O(|V||E|)$ by the number of augmentation rounds $O(|V|)$, the time complexity of Dinic's algorithm is $O(|V|^2|E|)$.

To make the actual running time of Dinic's algorithm approach its theoretical upper bound, we need to construct networks with special properties as input. Since in algorithm competition practice, the examination of network flow knowledge often focuses on the technique of modeling the original problem as a network flow problem, our models usually do not contain the special properties that make Dinic's algorithm slow; on the contrary, Dinic's algorithm is very efficient on most graphs. Therefore, the constraints of network flow problems are usually large, and the approach "plug the values of $|V|, |E|$ into $|V|^2|E|$ to estimate the running time" is not applicable. In fact, an accurate estimate requires the contestant to have some experience with the practical efficiency of Dinic's algorithm; readers can practice more.

#### Time complexity analysis in special cases

On some graphs with nice properties, Dinic's algorithm has better time complexity.

For a network $G = (V, E)$, if all edge capacities are $1$, i.e. $c(u, v) \in \{0, 1\}$ holds for all $(u, v) \in E$, we say $G$ is a unit-capacity network.

In a unit-capacity network, the time complexity of a single augmentation round of Dinic's algorithm is $O(|E|)$.

???+ note "Proof"
    This is because every augmentation causes all edges on the augmenting path to become saturated and disappear, so within a single augmentation round each edge can be augmented only once.

In a unit-capacity network, the number of augmentation rounds of Dinic's algorithm is $O(|E|^{\frac{1}{2}})$.

???+ note "Proof"
    Layer with the source $s$ as the center, and let $d_f(u)$ be the distance from vertex $u$ to the source $s$ on $G_f$. In addition, we define the vertex set $\left\{u \mid u \in V, d_f(u) = k \right\}$ as the layer $D_k$ with index $k$, and let $S_k = \cup_{i \leq k} D_i$.
    
    Suppose we have already performed $|E|^{\frac{1}{2}}$ augmentation rounds. By the pigeonhole principle, there is at least one $k$ such that the size of the edge set $\left\{ (u, v) \mid u \in D_k, v \in D_{k+1}, (u, v) \in E_f \right\}$ does not exceed $\frac {|E|} {|E|^{\frac{1}{2}}} \approx |E|^{\frac{1}{2}}$. Clearly, $\{S_k, V - S_k\}$ is an $s$-$t$ cut on $G_f$, and its cut capacity does not exceed $|E|^{\frac{1}{2}}$. By the max-flow min-cut theorem, the maximum flow on $G_f$ does not exceed $|E|^{\frac{1}{2}}$, i.e. at most $|E|^{\frac{1}{2}}$ more augmentation rounds can be performed on $G_f$. Therefore the total number of augmentation rounds is $O(|E|^{\frac{1}{2}})$.

In a unit-capacity network, the number of augmentation rounds of Dinic's algorithm is $O(|V|^{\frac{2}{3}})$.

???+ note "Proof"
    Suppose we have already performed $2 |V|^{\frac{2}{3}}$ augmentation rounds. Since at most half of the layers ($|V|^{\frac{2}{3}}$ of them) contain more than $|V|^{\frac{1}{3}}$ vertices, no matter how we distribute the sizes of all layers, there is at least one $k$ such that two adjacent layers both contain no more than $|V|^{\frac{1}{3}}$ vertices, i.e. $|D_k| \leq |V|^{\frac{1}{3}}$ and $|D_{k+1}| \leq |V|^{\frac{1}{3}}$.
    
    To maximize the number of edges between $D_k$ and $D_{k+1}$, we assume they form a complete bipartite graph; then the size of the edge set $\left\{ (u, v) \mid u \in D_k, v \in D_{k+1}, (u, v) \in E_f \right\}$ does not exceed $|V|^{\frac{2}{3}}$. Clearly, $\{S_k, V - S_k\}$ is an $s$-$t$ cut on $G_f$, and its cut capacity does not exceed $|V|^{\frac{2}{3}}$. By the max-flow min-cut theorem, the maximum flow on $G_f$ does not exceed $|V|^{\frac{2}{3}}$, i.e. at most $|V|^{\frac{2}{3}}$ more augmentation rounds can be performed on $G_f$. Therefore the total number of augmentation rounds is $O(|V|^{\frac{2}{3}})$.

In a unit-capacity network, if every vertex $u$ other than the source and sink satisfies $\mathit{deg}_{\mathit{in}}(u) = 1$ or $\mathit{deg}_{\mathit{out}}(u) = 1$, then the number of augmentation rounds of Dinic's algorithm is $O(|V|^{\frac{1}{2}})$. Here $\mathit{deg}_{\mathit{in}}(u)$ and $\mathit{deg}_{\mathit{out}}(u)$ denote the in-degree and out-degree of vertex $u$ respectively.

???+ note "Proof"
    We introduce the following lemma — for a network of this form, any flow on it can always be decomposed into several **vertex-disjoint** augmenting paths of unit flow.
    
    Suppose we have already performed $|V|^{\frac{1}{2}}$ augmentation rounds. By the definition of the level graph, the length of any new augmenting path is now at least $|V|^{\frac{1}{2}}$.
    
    Consider the augmenting-path decomposition of the maximum flow on $G_f$; the number of augmenting paths we obtain cannot exceed $\frac {|V|} {|V|^{\frac{1}{2}}} \approx |V|^{\frac{1}{2}}$, which means at most $|V|^{\frac{1}{2}}$ more augmentation rounds can be performed on $G_f$. Therefore the total number of augmentation rounds is $O(|V|^{\frac{1}{2}})$.

In summary, we obtain some corollaries.

-   On a unit-capacity network, the total time complexity of Dinic's algorithm is $O(|E| \min(|E|^\frac{1}{2}, |V|^{\frac{2}{3}}))$.
-   On a unit-capacity network, if every vertex $u$ other than the source and sink satisfies $\mathit{deg}_{\mathit{in}}(u) = 1$ or $\mathit{deg}_{\mathit{out}}(u) = 1$, the total time complexity of Dinic's algorithm is $O(|E||V|^{\frac{1}{2}})$. For the maximum bipartite matching problem we often use the Hopcroft–Karp algorithm, which is in fact a special case of Dinic's algorithm on a unit-capacity network satisfying the degree constraint above.

#### Implementation

??? note "Reference code"
    ```cpp
    struct MF {
      struct edge {
        int v, nxt, cap, flow;
      } e[N];
    
      int fir[N], cnt = 0;
    
      int n, S, T;
      ll maxflow = 0;
      int dep[N], cur[N];
    
      void init() {
        memset(fir, -1, sizeof fir);
        cnt = 0;
      }
    
      void addedge(int u, int v, int w) {
        e[cnt] = {v, fir[u], w, 0};
        fir[u] = cnt++;
        e[cnt] = {u, fir[v], 0, 0};
        fir[v] = cnt++;
      }
    
      bool bfs() {
        queue<int> q;
        memset(dep, 0, sizeof(int) * (n + 1));
    
        dep[S] = 1;
        q.push(S);
        while (q.size()) {
          int u = q.front();
          q.pop();
          for (int i = fir[u]; ~i; i = e[i].nxt) {
            int v = e[i].v;
            if ((!dep[v]) && (e[i].cap > e[i].flow)) {
              dep[v] = dep[u] + 1;
              q.push(v);
            }
          }
        }
        return dep[T];
      }
    
      int dfs(int u, int flow) {
        if ((u == T) || (!flow)) return flow;
    
        int ret = 0;
        for (int& i = cur[u]; ~i; i = e[i].nxt) {
          int v = e[i].v, d;
          if ((dep[v] == dep[u] + 1) &&
              (d = dfs(v, min(flow - ret, e[i].cap - e[i].flow)))) {
            ret += d;
            e[i].flow += d;
            e[i ^ 1].flow -= d;
            if (ret == flow) return ret;
          }
        }
        return ret;
      }
    
      void dinic() {
        while (bfs()) {
          memcpy(cur, fir, sizeof(int) * (n + 1));
          maxflow += dfs(S, INF);
        }
      }
    } mf;
    ```

### MPM algorithm

The **MPM** (Malhotra, Pramodh-Kumar and Maheshwari) algorithm obtains the maximum flow in one of two ways: using a heap-based priority queue, with time complexity $O(n^3\log n)$, or the commonly used BFS approach, with time complexity $O(n^3)$. Note that this section focuses only on analyzing the better and simpler $O(n^3)$ algorithm.

The overall structure of the MPM algorithm is similar to Dinic's algorithm; it also runs in phases. In each phase, it finds augmenting paths in the layered network of the residual network of $G$. Its main difference from Dinic's algorithm is the way augmenting paths are found: the part of the MPM algorithm that finds augmenting paths takes only $O(n^2)$, a time complexity better than Dinic's.

The MPM algorithm considers the capacities of vertices rather than edges. In the layered network $L$, if we define the capacity $p(v)$ of a vertex $v$ as the minimum of its incoming and outgoing residual capacities, we have:

$$
\begin{aligned}
p_{in}(v) &= \sum\limits_{(u,v) \in L} (c(u, v) - f(u, v)) \\
p_{out}(v) &= \sum\limits_{(v,u) \in L} (c(v, u) - f(v, u)) \\
p(v) &= \min (p_{in}(v), p_{out}(v))
\end{aligned}
$$

We call a node $r$ a reference node if and only if $p(r) = \min {p(v)}$. For a reference node $r$, we can always increase the flow through $r$ by $p(r)$ so that its capacity becomes $0$. This is because $L$ is a directed acyclic graph and the node capacities in $L$ are at least $p(r)$, so we can always find a directed path from $s$ through $r$ to $t$. Then we simply increase the flow of the edges on this path by $p(r)$. This path is the augmenting path of this phase. Finding the augmenting path can be done with BFS. After augmenting, all saturated edges can be deleted from $L$, since they will not be used after this phase. Likewise, all nodes other than $s$ and $t$ with no out-edges or no in-edges can be deleted.

#### Time complexity analysis

Each phase of the MPM algorithm takes $O(V^2)$, because there are at most $V$ iterations (since at least the chosen reference node is deleted), and in each iteration we delete all traversed edges except at most $V$. Summing up, we get $O(V^2+E)=O(V^2)$. Since the total number of phases is less than $V$, the total running time of the MPM algorithm is $O(V^3)$.

???+ note "Proof that the total number of phases is less than V"
    The MPM algorithm finishes in fewer than $V$ phases. To prove this, we must first prove two lemmas.
    
    **Lemma 1**: after each iteration, the distance from $s$ to every vertex does not decrease, that is, $level_{i+1}[v] \ge level_{i}[v]$.
    
    **Proof**: fix a phase $i$ and a vertex $v$. Consider any shortest path $P$ from $s$ to $v$ in $G_{i}^R$. The length of $P$ equals $level_{i}[v]$. Note that $G_{i}^R$ can only contain backward edges and forward edges of $G_{i}^R$. If $P$ has no backward edge of $G_{i}^R$, then $level_{i+1}[v] \ge level_{i}[v]$, because $P$ is also a path in $G_{i}^R$. Now suppose $P$ has at least one backward edge and the first such edge is $(u,w)$; then $level_{i+1}[u] \ge level_{i}[u]$ (because of the first case). The edge $(u,w)$ does not belong to $G_{i}^R$, so $(u,w)$ was affected by the augmenting path of the previous iteration. This means $level_{i}[u] = level_{i}[w]+1$. Moreover, $level_{i+1}[w] = level_{i+1}[u]+1$. From these two equations and $level_{i+1}[u] \ge level_{i}[u]$ we get $level_{i+1}[w] \ge level_{i}[w]+2$. The same idea can be used for the rest of the path.
    
    **Lemma 2**: $level_{i+1}[t] > level_{i}[t]$.
    
    **Proof**: from Lemma 1 we get $level_{i+1}[t] \ge level_{i}[t]$. Suppose $level_{i+1}[t] = level_{i}[t]$; note that $G_{i}^R$ can only contain backward edges and forward edges of $G_{i}^R$. This means there is a shortest path in $G_{i}^R$ not blocked by the augmenting paths. This is a contradiction.

#### Implementation

??? note "Reference code"
    ```cpp
    struct MPM {
      struct FlowEdge {
        int v, u;
        long long cap, flow;
    
        FlowEdge() {}
    
        FlowEdge(int _v, int _u, long long _cap, long long _flow)
            : v(_v), u(_u), cap(_cap), flow(_flow) {}
    
        FlowEdge(int _v, int _u, long long _cap)
            : v(_v), u(_u), cap(_cap), flow(0ll) {}
      };
    
      constexpr static long long flow_inf = 1e18;
      vector<FlowEdge> edges;
      vector<char> alive;
      vector<long long> pin, pout;
      vector<list<int>> in, out;
      vector<vector<int>> adj;
      vector<long long> ex;
      int n, m = 0;
      int s, t;
      vector<int> level;
      vector<int> q;
      int qh, qt;
    
      void resize(int _n) {
        n = _n;
        ex.resize(n);
        q.resize(n);
        pin.resize(n);
        pout.resize(n);
        adj.resize(n);
        level.resize(n);
        in.resize(n);
        out.resize(n);
      }
    
      MPM() {}
    
      MPM(int _n, int _s, int _t) {
        resize(_n);
        s = _s;
        t = _t;
      }
    
      void add_edge(int v, int u, long long cap) {
        edges.push_back(FlowEdge(v, u, cap));
        edges.push_back(FlowEdge(u, v, 0));
        adj[v].push_back(m);
        adj[u].push_back(m + 1);
        m += 2;
      }
    
      bool bfs() {
        while (qh < qt) {
          int v = q[qh++];
          for (int id : adj[v]) {
            if (edges[id].cap - edges[id].flow < 1) continue;
            if (level[edges[id].u] != -1) continue;
            level[edges[id].u] = level[v] + 1;
            q[qt++] = edges[id].u;
          }
        }
        return level[t] != -1;
      }
    
      long long pot(int v) { return min(pin[v], pout[v]); }
    
      void remove_node(int v) {
        for (int i : in[v]) {
          int u = edges[i].v;
          auto it = find(out[u].begin(), out[u].end(), i);
          out[u].erase(it);
          pout[u] -= edges[i].cap - edges[i].flow;
        }
        for (int i : out[v]) {
          int u = edges[i].u;
          auto it = find(in[u].begin(), in[u].end(), i);
          in[u].erase(it);
          pin[u] -= edges[i].cap - edges[i].flow;
        }
      }
    
      void push(int from, int to, long long f, bool forw) {
        qh = qt = 0;
        ex.assign(n, 0);
        ex[from] = f;
        q[qt++] = from;
        while (qh < qt) {
          int v = q[qh++];
          if (v == to) break;
          long long must = ex[v];
          auto it = forw ? out[v].begin() : in[v].begin();
          while (true) {
            int u = forw ? edges[*it].u : edges[*it].v;
            long long pushed = min(must, edges[*it].cap - edges[*it].flow);
            if (pushed == 0) break;
            if (forw) {
              pout[v] -= pushed;
              pin[u] -= pushed;
            } else {
              pin[v] -= pushed;
              pout[u] -= pushed;
            }
            if (ex[u] == 0) q[qt++] = u;
            ex[u] += pushed;
            edges[*it].flow += pushed;
            edges[(*it) ^ 1].flow -= pushed;
            must -= pushed;
            if (edges[*it].cap - edges[*it].flow == 0) {
              auto jt = it;
              ++jt;
              if (forw) {
                in[u].erase(find(in[u].begin(), in[u].end(), *it));
                out[v].erase(it);
              } else {
                out[u].erase(find(out[u].begin(), out[u].end(), *it));
                in[v].erase(it);
              }
              it = jt;
            } else
              break;
            if (!must) break;
          }
        }
      }
    
      long long flow() {
        long long ans = 0;
        while (true) {
          pin.assign(n, 0);
          pout.assign(n, 0);
          level.assign(n, -1);
          alive.assign(n, true);
          level[s] = 0;
          qh = 0;
          qt = 1;
          q[0] = s;
          if (!bfs()) break;
          for (int i = 0; i < n; i++) {
            out[i].clear();
            in[i].clear();
          }
          for (int i = 0; i < m; i++) {
            if (edges[i].cap - edges[i].flow == 0) continue;
            int v = edges[i].v, u = edges[i].u;
            if (level[v] + 1 == level[u] && (level[u] < level[t] || u == t)) {
              in[u].push_back(i);
              out[v].push_back(i);
              pin[u] += edges[i].cap - edges[i].flow;
              pout[v] += edges[i].cap - edges[i].flow;
            }
          }
          pin[s] = pout[t] = flow_inf;
          while (true) {
            int v = -1;
            for (int i = 0; i < n; i++) {
              if (!alive[i]) continue;
              if (v == -1 || pot(i) < pot(v)) v = i;
            }
            if (v == -1) break;
            if (pot(v) == 0) {
              alive[v] = false;
              remove_node(v);
              continue;
            }
            long long f = pot(v);
            ans += f;
            push(v, s, f, false);
            push(v, t, f, true);
            alive[v] = false;
            remove_node(v);
          }
        }
        return ans;
      }
    };
    ```

### ISAP

In Dinic's algorithm, after finding augmenting paths each time we have to run BFS to re-layer; is there a more efficient method?

The answer is the ISAP algorithm introduced below.

#### Procedure

As in Dinic's algorithm, we first run BFS to layer the vertices of the graph, but slightly differently from Dinic, we choose to run the BFS on the reverse graph, from vertex $t$ toward vertex $s$.

After the layering, we use DFS to find augmenting paths.

The augmentation process is similar to Dinic's: we only augment toward vertices whose layer is $1$ less than the current vertex's.

Unlike Dinic, we do not rerun BFS to re-layer the vertices; instead, the re-layering is done during the augmentation process.

Specifically, let $d_i$ be the layer of vertex $i$; when we finish augmenting at vertex $i$, we iterate over all out-edges of $i$ in the residual network, find the target vertex $j$ with the smallest layer, and then set $d_i \gets d_j+1$. In particular, if $i$ has no out-edges in the residual network, set $d_i \gets n$.

It is easy to see that when $d_s \geq n$, there is no augmenting path in the graph, and the algorithm can terminate.

Similar to Dinic, ISAP also has the **current-arc optimization**.

ISAP has another optimization: we record the number $num_i$ of vertices with layer $i$; whenever a vertex's layer is updated from $x$ to $y$, we update the $num$ array accordingly, and if $num_x=0$ after the update, a gap has appeared in the graph and no augmenting path can be found anymore, so the algorithm can terminate immediately (in the implementation, simply set $d_s$ to $n$). This optimization is called the **GAP optimization**.

#### Implementation

??? note "Reference code"
    ```cpp
    struct Edge {
      int from, to, cap, flow;
    
      Edge(int u, int v, int c, int f) : from(u), to(v), cap(c), flow(f) {}
    };
    
    bool operator<(const Edge& a, const Edge& b) {
      return a.from < b.from || (a.from == b.from && a.to < b.to);
    }
    
    struct ISAP {
      int n, m, s, t;
      vector<Edge> edges;
      vector<int> G[MAXN];
      bool vis[MAXN];
      int d[MAXN];
      int cur[MAXN];
      int p[MAXN];
      int num[MAXN];
    
      void AddEdge(int from, int to, int cap) {
        edges.push_back(Edge(from, to, cap, 0));
        edges.push_back(Edge(to, from, 0, 0));
        m = edges.size();
        G[from].push_back(m - 2);
        G[to].push_back(m - 1);
      }
    
      bool BFS() {
        memset(vis, 0, sizeof(vis));
        queue<int> Q;
        Q.push(t);
        vis[t] = true;
        d[t] = 0;
        while (!Q.empty()) {
          int x = Q.front();
          Q.pop();
          for (int i = 0; i < G[x].size(); i++) {
            Edge& e = edges[G[x][i] ^ 1];
            if (!vis[e.from] && e.cap > e.flow) {
              vis[e.from] = true;
              d[e.from] = d[x] + 1;
              Q.push(e.from);
            }
          }
        }
        return vis[s];
      }
    
      void init(int n) {
        this->n = n;
        for (int i = 0; i < n; i++) G[i].clear();
        edges.clear();
      }
    
      int Augment() {
        int x = t, a = INF;
        while (x != s) {
          Edge& e = edges[p[x]];
          a = min(a, e.cap - e.flow);
          x = edges[p[x]].from;
        }
        x = t;
        while (x != s) {
          edges[p[x]].flow += a;
          edges[p[x] ^ 1].flow -= a;
          x = edges[p[x]].from;
        }
        return a;
      }
    
      int Maxflow(int s, int t) {
        this->s = s;
        this->t = t;
        int flow = 0;
        BFS();
        memset(num, 0, sizeof(num));
        for (int i = 0; i < n; i++) num[d[i]]++;
        int x = s;
        memset(cur, 0, sizeof(cur));
        while (d[s] < n) {
          if (x == t) {
            flow += Augment();
            x = s;
          }
          int ok = 0;
          for (int i = cur[x]; i < G[x].size(); i++) {
            Edge& e = edges[G[x][i]];
            if (e.cap > e.flow && d[x] == d[e.to] + 1) {
              ok = 1;
              p[e.to] = G[x][i];
              cur[x] = i;
              x = e.to;
              break;
            }
          }
          if (!ok) {
            int m = n - 1;
            for (int i = 0; i < G[x].size(); i++) {
              Edge& e = edges[G[x][i]];
              if (e.cap > e.flow) m = min(m, d[e.to]);
            }
            if (--num[d[x]] == 0) break;
            num[d[x] = m + 1]++;
            cur[x] = 0;
            if (x != s) x = edges[p[x]].from;
          }
        }
        return flow;
      }
    };
    ```

## Push-relabel (preflow) algorithms

This method ignores flow conservation during the computation and updates the information of one vertex at a time in order to compute the maximum flow.

### Generic push-relabel algorithm

First we introduce the main idea of the push-relabel algorithm and a feasible brute-force implementation.

The push-relabel algorithm computes the maximum flow by updating single vertices until no vertex needs updating.

The flow function maintained during the algorithm does not necessarily preserve flow conservation: for a vertex, we allow the flow entering the vertex to exceed the flow leaving it; the excess is called the **excess flow** $e(u)$ of the vertex $u(u\in V-\{s,t\})$:

$$
e(u)=\sum_{(x,u)\in E}f(x,u)-\sum_{(u,y)\in E}f(u,y)
$$

If $e(u)>0$, we say the vertex $u$ is **overflowing**[^note1]; note that when we mention overflowing vertices, $s$ and $t$ are not included.

The push-relabel algorithm maintains the height $h(u)$ of every vertex and stipulates that an overflowing vertex $u$, if it wants to push excess flow, may only push it to vertices with height less than that of $u$; if $u$ has no adjacent vertex with height less than $u$'s, we modify the height of $u$ (relabel).

#### Height function[^note2]

Precisely, push-relabel maintains the following mapping $h:V\to \mathbf{N}$:

-   $h(s)=|V|,h(t)=0$
-   $\forall (u,v)\in E_f,h(u)\leq h(v)+1$

$h$ is called the height function of the residual network $G_f=(V_f,E_f)$.

Lemma 1: let $h$ be the height function on $G_f$; for any two vertices $u,v\in V$, if $h(u)>h(v)+1$, then $(u,v)$ is not an edge in $G_f$.

The algorithm only performs pushes on edges with $h(u)=h(v)+1$.

#### Push

Applicability condition: vertex $u$ is overflowing, and there is a vertex $v((u,v)\in E_f,c(u,v)-f(u,v)>0,h(u)=h(v)+1)$; then the push operation applies to $(u,v)$.

Then we push as much excess flow as possible from $u$ to $v$; during the push we only care about the minimum of the excess flow and $c(u,v)-f(u,v)$, and do not care whether $v$ overflows.

If $(u,v)$ is saturated after the push, remove it from the residual network.

#### Relabel

Applicability condition: if vertex $u$ is overflowing and $\forall (u,v)\in E_f,h(u)\leq h(v)$, then the relabel operation applies to $u$.

Then simply update $h(u)$ to $\min_{(u,v)\in E_f}h(v)+1$.

#### Initialization

$$
\forall (u,v)\in E,~~f(u,v)=\begin{cases}
c(u,v),&u=s\\
0,&u\neq s
\end{cases}
$$

$$
\forall u\in V,~~h(u)=\begin{cases}
|V|,&u=s\\
0,&u\neq s
\end{cases}
$$

$$
e(u)=\sum_{(x,u)\in E}f(x,u)-\sum_{(u,y)\in E}f(u,y)
$$

The above fills the edges $(s,v)\in E$ with flow and raises $h(s)$ so that $(s,v)\notin E_f$, because $h(s)>h(v)$, and $(s,v)$ is saturated anyway, so there is no need to keep it in the residual network; the above also initializes $e(s)$ to the negative of $\sum_{(s,v)\in E}f(s,v)$.

#### Procedure

Each time we scan the whole graph, and as long as there is a vertex $u$ satisfying the condition for push or relabel, we perform the corresponding operation.

In the figure, the middle of each vertex shows its index, the lower left shows the height $h(u)$, and the lower right shows the excess flow $e(u)$; the darkness of a vertex's color also indicates its height; the edge weight denotes $c(u,v)-f(u,v)$, and green edges are the edges $(u,v)$ satisfying $h(u)=h(v)+1$ (i.e. the edges $E_f$ of the residual network):

![p1](./images/2148.png)

Let us roughly go through the whole algorithm; here the author uses a brute-force algorithm, i.e. brute-force scanning for overflowing vertices and updating them if any exist.

![p2](./images/2149.gif)

The final result

![p3](./images/2150.png)

We can see that part of the excess flow eventually returns to $s$, and apart from the source and sink no vertex overflows; the flow function $f$ at this point satisfies flow conservation, is a maximum flow, and its value is $e(t)$.

However, the paper[^ref1] actually points out that processing only overflowing nodes with height less than $n$ also yields the correct maximum flow value, but then at the end of the algorithm the preflow does not yet satisfy the properties of a flow function, so the real flow on each edge is unknown.

#### Implementation

???+ note "Core code"
    ```cpp
    constexpr int N = 1e4 + 4, M = 1e5 + 5, INF = 0x3f3f3f3f;
    int n, m, s, t, maxflow, tot;
    int ht[N], ex[N];
    
    void init() {  // initialization
      for (int i = h[s]; i; i = e[i].nex) {
        const int &v = e[i].t;
        ex[v] = e[i].v, ex[s] -= ex[v], e[i ^ 1].v = e[i].v, e[i].v = 0;
      }
      ht[s] = n;
    }
    
    bool push(int ed) {
      const int &u = e[ed ^ 1].t, &v = e[ed].t;
      int flow = min(ex[u], e[ed].v);
      ex[u] -= flow, ex[v] += flow, e[ed].v -= flow, e[ed ^ 1].v += flow;
      return ex[u];  // if u is still overflowing, return 1
    }
    
    void relabel(int u) {
      ht[u] = INF;
      for (int i = h[u]; i; i = e[i].nex)
        if (e[i].v) ht[u] = min(ht[u], ht[e[i].t]);
      ++ht[u];
    }
    ```

### HLPP algorithm

The Highest Label Preflow Push algorithm, within the generic push-relabel algorithm above, always prefers the overflowing vertex with the greatest height when selecting a vertex; its complexity is $O(n^2\sqrt m)$.

#### Procedure

Specifically, the HLPP algorithm proceeds as follows:

1.  initialize (based on the push-relabel algorithm);
2.  among the overflowing vertices, choose the vertex $u$ with the greatest height and push along all of its pushable edges;
3.  if $u$ is still overflowing, relabel it and go back to step 2;
4.  if there is no overflowing vertex, the algorithm ends.

A paper[^ref2] testing the practical performance of maximum flow algorithms shows that preflow-based algorithms actually spend a considerable portion of their time on the relabel step. Below we introduce two optimizations from the paper[^ref3] that significantly reduce the number of relabels.

#### BFS optimization

The upper bound of HLPP is $O(n^2\sqrt m)$, but in practice it is fairly tight; we can optimize when initializing the heights. Specifically, we initialize $h(u)$ to the shortest distance from $u$ to $t$; in particular, $h(s)=n$.

During the BFS we also check the connectivity of the graph and rule out the case with no solution.

#### GAP optimization

The push condition of HLPP is $h(u)=h(v)+1$; if at some moment of the algorithm there is some $k$ such that the number of vertices with $h(u)=k$ is $0$, then vertices with $h(u)>k$ can never push excess flow to $t$ again and can only send it back to $s$, so at that moment we directly make their heights at least $n+1$ to push back to $s$ as soon as possible and reduce relabel operations.

The implementation below adopts the method from the paper[^ref2], using $N*2-1$ buckets `B`, where `B[i]` records all overflowing nodes whose current height is $i$. It includes the two optimizations mentioned above and only processes overflowing nodes with height less than $n$.

It is worth noting that the buckets used in the paper[^ref2] are linked-list-based stacks, while the default container of STL's `stack` is `deque`. Simple tests show that `vector`, `deque` and `list` do not differ much in efficiency in the actual run of this problem.

#### Implementation

??? note "Luogu P4722 [Template] Maximum flow, enhanced version / push-relabel"
    ```cpp
    #include <cstdio>
    #include <cstring>
    #include <queue>
    #include <stack>
    using namespace std;
    constexpr int N = 1200, M = 120000, INF = 0x3f3f3f3f;
    int n, m, s, t;
    
    struct qxx {
      int nex, t;
      long long v;
    };
    
    qxx e[M * 2 + 1];
    int h[N + 1], cnt = 1;
    
    void add_path(int f, int t, long long v) {
      e[++cnt] = qxx{h[f], t, v}, h[f] = cnt;
    }
    
    void add_flow(int f, int t, long long v) {
      add_path(f, t, v);
      add_path(t, f, 0);
    }
    
    int ht[N + 1];        // height;
    long long ex[N + 1];  // excess flow;
    int gap[N];           // gap optimization. gap[i] is the number of nodes with height i
    stack<int> B[N];      // bucket B[i] records all v with ht[v]==i
    int level = 0;        // greatest height among overflowing nodes
    
    int push(int u) {      // push excess flow as much as possible through pushable edges
      bool init = u == s;  // whether we are initializing
      for (int i = h[u]; i; i = e[i].nex) {
        const int &v = e[i].t;
        const long long &w = e[i].v;
        // during initialization, ignore the height difference of 1
        if (!w || (init == false && ht[u] != ht[v] + 1) || ht[v] == INF) continue;
        long long k = init ? w : min(w, ex[u]);
        // take the minimum of the residual capacity and the excess flow; during initialization the source's excess may become negative.
        if (v != s && v != t && !ex[v]) B[ht[v]].push(v), level = max(level, ht[v]);
        ex[u] -= k, ex[v] += k, e[i].v -= k, e[i ^ 1].v += k;  // push
        if (!ex[u]) return 0;  // return once everything has been pushed
      }
      return 1;
    }
    
    void relabel(int u) {  // relabel (height)
      ht[u] = INF;
      for (int i = h[u]; i; i = e[i].nex)
        if (e[i].v) ht[u] = min(ht[u], ht[e[i].t]);
      if (++ht[u] < n) {  // only process nodes with height less than n
        B[ht[u]].push(u);
        level = max(level, ht[u]);
        ++gap[ht[u]];  // new height, update gap
      }
    }
    
    bool bfs_init() {
      memset(ht, 0x3f, sizeof(ht));
      queue<int> q;
      q.push(t), ht[t] = 0;
      while (q.size()) {  // reverse BFS, enqueue unvisited vertices
        int u = q.front();
        q.pop();
        for (int i = h[u]; i; i = e[i].nex) {
          const int &v = e[i].t;
          if (e[i ^ 1].v && ht[v] > ht[u] + 1) ht[v] = ht[u] + 1, q.push(v);
        }
      }
      return ht[s] != INF;  // if the graph is disconnected, return 0
    }
    
    // select one of the nodes with the current greatest height; return 0 if there are no overflowing nodes left
    int select() {
      while (level > -1 && B[level].size() == 0) level--;
      return level == -1 ? 0 : B[level].top();
    }
    
    long long hlpp() {            // returns the maximum flow
      if (!bfs_init()) return 0;  // graph is disconnected
      memset(gap, 0, sizeof(gap));
      for (int i = 1; i <= n; i++)
        if (ht[i] != INF) gap[ht[i]]++;  // initialize gap
      ht[s] = n;
      push(s);  // initialize the preflow
      int u;
      while ((u = select())) {
        B[level].pop();
        if (push(u)) {  // still overflowing
          if (!--gap[ht[u]])
            for (int i = 1; i <= n; i++)
              if (i != s && ht[i] > ht[u] && ht[i] < n + 1)
                ht[i] = n + 1;  // the nodes relabeled to n+1 here are not overflowing nodes
          relabel(u);
        }
      }
      return ex[t];
    }
    
    int main() {
      scanf("%d%d%d%d", &n, &m, &s, &t);
      for (int i = 1, u, v, w; i <= m; i++) {
        scanf("%d%d%d", &u, &v, &w);
        add_flow(u, v, w);
      }
      printf("%lld", hlpp());
      return 0;
    }
    ```

Get a feel for the running process

![HLPP](./images/1152.png)

Between pic13 and pic14, Relabel(4) was executed and the GAP optimization was applied.

## Footnotes

[^ref_ek]: <http://pisces.ck.tp.edu.tw/~peng/index.php?action=showfile&file=f6cdf7ef750d7dc79c7d599b942acbaaee86a2e3e>

[^ref_dinic]: <https://people.orie.cornell.edu/dpw/orie633/LectureNotes/lecture9.pdf>

[^ref1]: Cherkassky B V, Goldberg A V. On implementing push-relabel method for the maximum flow problem\[C]//International Conference on Integer Programming and Combinatorial Optimization. Springer, Berlin, Heidelberg, 1995: 157-171.

[^ref2]: Ahuja R K, Kodialam M, Mishra A K, et al. Computational investigations of maximum flow algorithms\[J]. European Journal of Operational Research, 1997, 97(3): 509-542.

[^ref3]: Derigs U, Meier W. Implementing Goldberg's max-flow-algorithm—A computational investigation\[J]. Zeitschrift für Operations Research, 1989, 33(6): 383-403.

[^note1]: In English literature this is usually called "active".

[^note2]: In English literature, the height of a vertex is usually called a "distance label". The term "height" used here comes from the corresponding chapter of Introduction to Algorithms. You can find the reasoning for this in the footnote on p. 432 of the Chinese edition (original 3rd edition, China Machine Press).
