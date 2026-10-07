---
title: Maximum weight bipartite matching
---

A maximum weight matching of a bipartite graph is a matching with the largest total edge weight.

## Hungarian algorithm (Kuhn–Munkres algorithm)

The Hungarian algorithm, also known as the **KM** algorithm, finds a **maximum weight perfect matching** of a bipartite graph in $O(n^3)$ time.

Since the two parts of a bipartite graph do not always have the same number of vertices, to apply the KM algorithm to maximum weight matching we first do the following: add vertices to the smaller part so that both sides have the same number of vertices, and set the weights of non-existent edges to $0$. The problem then becomes the **maximum weight perfect matching problem**, which the KM algorithm can solve.

???+ note "Feasible vertex labeling"
    Assign to every vertex $i$ a weight $l(i)$ such that for all edges $(u,v)$ we have $w(u,v) \leq l(u) + l(v)$.

???+ note "Equality subgraph"
    The spanning subgraph of the original graph, under a given feasible labeling, that contains all vertices but only those edges $(u,v)$ satisfying $w(u,v) = l(u) + l(v)$.

???+ note "Theorem 1: For some feasible labeling, if the equality subgraph has a perfect matching, then that matching is a maximum weight perfect matching of the original bipartite graph."
    Proof 1.
    
    Consider an arbitrary perfect matching $M$ of the original bipartite graph; its total edge weight is
    
    $val(M) = \sum_{(u,v)\in M} {w(u,v)} \leq \sum_{(u,v)\in M} {l(u) + l(v)} \leq \sum_{i=1}^{n} l(i)$
    
    The total edge weight of a perfect matching $M'$ of the equality subgraph of an arbitrary feasible labeling is
    
    $val(M') = \sum_{(u,v)\in M} {l(u) + l(v)} = \sum_{i=1}^{n} l(i)$
    
    That is, the total edge weight of any perfect matching is no larger than $val(M')$, so $M'$ is a maximum weight matching.

With Theorem 1, our goal is to keep adjusting the feasible labeling until the equality subgraph has a perfect matching.

Since both sides have the same number of vertices, let that number be $n$; $lx(i)$ denotes the label of the $i$-th left vertex, $ly(i)$ the label of the $i$-th right vertex, and $w(u,v)$ the weight between the $u$-th left vertex and the $v$-th right vertex.

First initialize a feasible labeling, for example

$lx(i) = \max_{1\leq j\leq n} \{ w(i, j)\},\, ly(i) = 0$

Then pick an unmatched vertex and look for an augmenting path, as in maximum matching. If an augmenting path is found, augment; otherwise, we get an alternating tree.

Let $S$ and $T$ denote the left and right vertices of the bipartite graph that are in the alternating tree, and $S'$ and $T'$ those that are not.

![bigraph-weight-match-1](./images/bigraph-weight-match-1.png)

In the equality subgraph:

-   $S-T'$ edges do not exist, otherwise the alternating tree would grow.
-   $S'-T$ edges must be non-matching edges, otherwise the vertex would belong to $S$.

Suppose we add $-a$ to the labels in $S$ and $+a$ to the labels in $T$. Then:

-   $S-T$ edges still remain in the equality subgraph.
-   $S'-T'$ is unchanged.
-   For $S-T'$ edges, $lx + ly$ decreases, so they may enter the equality subgraph.
-   For $S'-T$ edges, $lx + ly$ increases, so they cannot enter the equality subgraph.

So the value of $a$ must obviously be the minimum over the $S-T'$ edges:

$a = \min \{ lx(u) + ly(v) - w(u,v) | u\in{S} , v\in{T'} \}$.

When a new edge $(u,v)$ enters the equality subgraph there are two cases:

-   $v$ is unmatched, so an augmenting path is found;
-   $v$ is already matched to a vertex in $S'$.

Thus after at most $n$ label adjustments an augmenting path is found.

Each time the labels are adjusted, the edges of the alternating tree do not leave the equality subgraph, so we can maintain the tree directly.

For every vertex $v$ in $T$ we maintain

$slack(v) = \min \{ lx(u) + ly(v) - w(u,v) | u\in{S} \}$.

So the label adjustment $a$ can be computed in $O(n)$:

$a = \min \{ slack(v) | v\in{T'} \}$

When a new vertex enters $S$ in the alternating tree, $O(n)$ is needed to update $slack(v)$. Adjusting the labels takes $O(n)$ to subtract $a$ from every $slack(v)$. As soon as the alternating tree reaches an unmatched vertex, an augmenting path is found.

Initially we enumerate $n$ vertices to find augmenting paths; finding each requires extending the alternating tree $n$ times, and each extension requires $n$ maintenance steps, for a total of $O(n^3)$.

??? note "Reference code"
    ```cpp
    template <typename T>
    struct hungarian {  // km
      int n;
      vector<int> matchx;  // matched vertices of the left set
      vector<int> matchy;  // matched vertices of the right set
      vector<int> pre;     // left vertex connected to the right set
      vector<bool> visx;   // visited array, left
      vector<bool> visy;   // visited array, right
      vector<T> lx;
      vector<T> ly;
      vector<vector<T>> g;
      vector<T> slack;
      T inf;
      T res;
      queue<int> q;
      int org_n;
      int org_m;
    
      hungarian(int _n, int _m) {
        org_n = _n;
        org_m = _m;
        n = max(_n, _m);
        inf = numeric_limits<T>::max();
        res = 0;
        g = vector<vector<T>>(n, vector<T>(n));
        matchx = vector<int>(n, -1);
        matchy = vector<int>(n, -1);
        pre = vector<int>(n);
        visx = vector<bool>(n);
        visy = vector<bool>(n);
        lx = vector<T>(n, -inf);
        ly = vector<T>(n);
        slack = vector<T>(n);
      }
    
      void addEdge(int u, int v, int w) {
        g[u][v] = max(w, 0);  // a negative value is worse than not matching, so setting it to 0 changes nothing
      }
    
      bool check(int v) {
        visy[v] = true;
        if (matchy[v] != -1) {
          q.push(matchy[v]);
          visx[matchy[v]] = true;  // in S
          return false;
        }
        // found a new unmatched vertex; update the matching, pre stores the vertex connected by a "non-matching edge"
        while (v != -1) {
          matchy[v] = pre[v];
          swap(v, matchx[pre[v]]);
        }
        return true;
      }
    
      void bfs(int i) {
        while (!q.empty()) {
          q.pop();
        }
        q.push(i);
        visx[i] = true;
        while (true) {
          while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v = 0; v < n; v++) {
              if (!visy[v]) {
                T delta = lx[u] + ly[v] - g[u][v];
                if (slack[v] >= delta) {
                  pre[v] = u;
                  if (delta) {
                    slack[v] = delta;
                  } else if (check(v)) {  // delta=0 means the edge can enter the equality subgraph; look for an augmenting path
                                          // if found, return and rebuild the alternating tree
                    return;
                  }
                }
              }
            }
          }
          // no augmenting path, adjust the vertex labels
          T a = inf;
          for (int j = 0; j < n; j++) {
            if (!visy[j]) {
              a = min(a, slack[j]);
            }
          }
          for (int j = 0; j < n; j++) {
            if (visx[j]) {  // S
              lx[j] -= a;
            }
            if (visy[j]) {  // T
              ly[j] += a;
            } else {  // T'
              slack[j] -= a;
            }
          }
          for (int j = 0; j < n; j++) {
            if (!visy[j] && slack[j] == 0 && check(j)) {
              return;
            }
          }
        }
      }
    
      void solve() {
        // initial vertex labels
        for (int i = 0; i < n; i++) {
          for (int j = 0; j < n; j++) {
            lx[i] = max(lx[i], g[i][j]);
          }
        }
    
        for (int i = 0; i < n; i++) {
          fill(slack.begin(), slack.end(), inf);
          fill(visx.begin(), visx.end(), false);
          fill(visy.begin(), visy.end(), false);
          bfs(i);
        }
    
        // custom
        for (int i = 0; i < n; i++) {
          if (g[i][matchx[i]] > 0) {
            res += g[i][matchx[i]];
          } else {
            matchx[i] = -1;
          }
        }
        cout << res << "\n";
        for (int i = 0; i < org_n; i++) {
          cout << matchx[i] + 1 << " ";
        }
        cout << "\n";
      }
    };
    ```

## Dynamic Hungarian algorithm

Original paper: [The Dynamic Hungarian Algorithm for the Assignment Problem with Changing Costs](https://www.ri.cmu.edu/publications/the-dynamic-hungarian-algorithm-for-the-assignment-problem-with-changing-costs/)

A paper with clearer pseudocode: [A Fast Dynamic Assignment Algorithm for Solving Resource Allocation Problems](https://www.researchgate.net/publication/352490780_A_Fast_Dynamic_Assignment_Algorithm_for_Solving_Resource_Allocation_Problems)

Related OJ problem: [DAP](https://www.spoj.com/problems/DAP/)

???+ note "Idea of the algorithm"
    1.  Changing the weights between a single vertex $u_i$ and all $v_j$, i.e. one row of the weight matrix
        -   update the label $lx(u_i) = max(w_{ij} - v_{j}), \forall j$
        -   remove the matching involving $u_i$
    2.  Changing the weights between all $u_i$ and a single vertex $v_j$, i.e. one column of the weight matrix
        -   update the label $ly(v_j) = max(w_{ij} - u_{i}), \forall i$
        -   remove the matching involving $v_j$
    3.  Changing the weight between a single vertex $u_i$ and a single vertex $v_j$, i.e. a single element of the weight matrix
        -   perform either operation 1 or operation 2
    4.  Adding a single vertex $u_i$ or a single vertex $v_j$, i.e. adding or removing a row or a column of the weight matrix
        -   perform 1 or 2 accordingly; note that adding a vertex here only adds the vertex without setting any weights – the weights between the new vertex and the others are 0.

???+ note "Proof of the algorithm"
    -   Let the original graph be G, the labels of the left and right vertices $\alpha^{i}$ and $\beta^{j}$, and the feasible labeling l; then $G_l$ is the subgraph of G containing the vertices and edges of G satisfying $w_{ij} = alpha_{i}+beta_{j}$.
    -   In the Hungarian algorithm section above, Theorem 1 proved: for some feasible labeling, if the equality subgraph has a perfect matching, then that matching is a maximum weight perfect matching of the original bipartite graph.
    -   Suppose the original optimal matching is $M^*$. When a change occurs, we update the feasible labeling according to the rules; denote the updated labels $\alpha^{i^*}$ or $\beta^{j^*}$. The following cases arise:
        1.  An entire row of the weight matrix is changed; let it be row $i^*$, i.e. all edges of $v_{i^*}$ are changed, so the old label of $v_{i^*}$ may no longer satisfy the condition, since we need $w_{i^{*}j} \leq alpha_{i^*}+beta_{j}$. For the other $u_j$, the weights of their edges, apart from those related to $i^*$, are unchanged, so their labels are still valid. Hence the algorithm updates the label of $v_{i^*}$ so that the labeling is feasible again.
        2.  An entire column of the weight matrix is changed; similarly, the algorithm updates the labels so that the labeling is feasible.
        3.  A single element of the weight matrix is changed; updating either of the two labels suffices to satisfy the labeling condition.
    -   Every change of the weight matrix concerns one particular vertex, which may be on the left or on the right, so we simply denote it $x$; this vertex was matched to some vertex $y$ in the original optimal matching. Each change at most unpairs this pair of vertices, so it suffices to run one round of the search of the Hungarian algorithm to obtain a new match, and by Theorem 1 the new match is optimal.

The following code should be the code submitted by the author of paper 2 (this version maximizes the weight; the original paper minimizes the cost).

??? note "Reference code for the dynamic Hungarian algorithm"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-weight-match/bigraph-weight-match_1.cpp"
    ```

## Conversion to a min-cost flow model

Similarly to [maximum bipartite matching](./bigraph-match.md), maximum weight bipartite matching can also be converted to a network flow problem.

First, add a source and a sink to the graph.

From the source, add an edge of capacity $1$ and cost $0$ to every left vertex of the bipartite graph; from every right vertex of the bipartite graph, add an edge of capacity $1$ and cost $0$ to the sink.

Next, for every edge of the bipartite graph joining a left vertex $u$ and a right vertex $v$ with weight $w$, add an edge from $u$ to $v$ of capacity $1$ and cost $w$.

In addition, since the number of edges in a maximum weight matching need not equal the number of edges in a maximum matching, from every left vertex we also add an edge of capacity $1$ and cost $0$ to the sink.

The answer is obtained by computing the [maximum-cost maximum flow](../flow/min-cost.md) of this network. The maximum flow of the network is then necessarily the number of left vertices, and the maximum cost under maximum flow corresponds to a maximum weight matching.

## Exercises

??? note "[UOJ #80. 二分图最大权匹配](https://uoj.ac/problem/80)"
    Template problem
    
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-weight-match/bigraph-weight-match_2.cpp"
    ```
