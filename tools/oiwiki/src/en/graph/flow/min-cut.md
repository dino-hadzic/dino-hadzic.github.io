---
title: Minimum cut
---

## Concepts

### Cut

For a flow network $G=(V,E)$, a cut is defined as a **partition of the vertices**: all vertices are divided into two sets $S$ and $T=V-S$, where the source $s\in S$ and the sink $t\in T$.

### Capacity of a cut

We define the capacity $c(S,T)$ of a cut $(S,T)$ as the sum of the capacities of all edges going from $S$ to $T$, i.e. $c(S,T)=\sum_{u\in S,v\in T}c(u,v)$. Of course, we may also write $c(s,t)$ for $c(S,T)$.

### Minimum cut

The minimum cut problem asks for a cut $(S,T)$ whose capacity $c(S,T)$ is minimum.

## Proof

### Max-flow min-cut theorem

See the section on the max-flow min-cut theorem on the [Maximum flow](max-flow.md) page.

## Code

### Minimum cut

By the **max-flow min-cut theorem** we directly obtain the following code:

??? note "Sample code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <queue>
    
    constexpr int N = 1e4 + 5, M = 2e5 + 5;
    int n, m, s, t, tot = 1, lnk[N], ter[M], nxt[M], val[M], dep[N], cur[N];
    
    void add(int u, int v, int w) {
      ter[++tot] = v, nxt[tot] = lnk[u], lnk[u] = tot, val[tot] = w;
    }
    
    void addedge(int u, int v, int w) { add(u, v, w), add(v, u, 0); }
    
    int bfs(int s, int t) {
      memset(dep, 0, sizeof(dep));
      memcpy(cur, lnk, sizeof(lnk));
      std::queue<int> q;
      q.push(s), dep[s] = 1;
      while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int i = lnk[u]; i; i = nxt[i]) {
          int v = ter[i];
          if (val[i] && !dep[v]) q.push(v), dep[v] = dep[u] + 1;
        }
      }
      return dep[t];
    }
    
    int dfs(int u, int t, int flow) {
      if (u == t) return flow;
      int ans = 0;
      for (int &i = cur[u]; i && ans < flow; i = nxt[i]) {
        int v = ter[i];
        if (val[i] && dep[v] == dep[u] + 1) {
          int x = dfs(v, t, std::min(val[i], flow - ans));
          if (x) val[i] -= x, val[i ^ 1] += x, ans += x;
        }
      }
      if (ans < flow) dep[u] = -1;
      return ans;
    }
    
    int dinic(int s, int t) {
      int ans = 0;
      while (bfs(s, t)) {
        int x;
        while ((x = dfs(s, t, 1 << 30))) ans += x;
      }
      return ans;
    }
    
    int main() {
      scanf("%d%d%d%d", &n, &m, &s, &t);
      while (m--) {
        int u, v, w;
        scanf("%d%d%d", &u, &v, &w);
        addedge(u, v, w);
      }
      printf("%d\n", dinic(s, t));
      return 0;
    }
    ```

### Recovering the cut

We can find all vertices of the set $S$ by running a DFS from the source $s$, each time walking only along edges with residual capacity greater than $0$.

```cpp
void dfs(int u) {
  vis[u] = 1;
  for (int i = lnk[u]; i; i = nxt[i]) {
    int v = ter[i];
    if (!vis[v] && val[i]) dfs(v);
  }
}
```

### Number of cut edges

If we want the cut with the fewest edges, simply set all edge capacities to $1$ and compute a minimum cut once. If we want the minimum cut with the fewest edges, there are two approaches:

1.  Replace the capacity $c(u,v)$ of every edge with $c(u,v)(|E| + 1) + 1$ and compute a minimum cut on the new graph; this is the minimum cut of the original graph with the fewest cut edges. The capacity of the new graph's minimum cut divided by $|E| + 1$ and rounded down is the original minimum cut, and the remainder is the number of cut edges.

    This amounts to finding the lexicographically smallest cut with the cut size as the first key and the number of cut edges as the second key. Because the coefficient $|E| + 1$ is strictly larger than the total number of edges, while the number of cut edges never exceeds the total number of edges, the number of cut edges can never, whatever it is, cancel out the effect of the cut size, so the cut found is certainly a minimum cut of the original graph; among the minimum cuts of the original graph, the one with the fewest cut edges becomes the minimum cut of the new graph.

    Note that the correctness of this approach relies on all edge capacities being integers: only then is it guaranteed that the number of cut edges $k\le|E|<|E|+1$ does not carry over into the higher digit. If the capacities are rational, first multiply by a common denominator to make them integers; if the capacities are arbitrary reals, or an integer type would overflow, simply take the capacity to be the pair $(c(u,v),1)$, add component-wise and compare lexicographically. Then every augmenting-path algorithm that relies only on adding, subtracting and comparing capacities (such as Dinic's algorithm) runs unchanged.

2.  First compute the maximum flow of the graph, then build a new graph: for every arc of the **residual graph** (i.e. the forward arc of every unsaturated edge and the backward arc of every edge carrying flow) add an edge of capacity $\infty$, and for every saturated edge add an edge of capacity $1$; running a minimum cut again gives the minimum number of cut edges.

    The cut edges of the new graph's minimum cut certainly contain no edge of capacity $\infty$, i.e. no residual arc points from $S$ to $T$. Hence, in the new graph's minimum cut, all forward edges of the original graph are saturated and all backward edges carry no flow, which shows that its capacity equals the maximum flow, so it is certainly a minimum cut of the original graph. Conversely, the forward edges of any minimum cut of the original graph are all saturated, so its capacity in the new graph is exactly its number of cut edges. Therefore the minimum cut of the new graph is the minimum cut of the original graph with the fewest cut edges.

    ??? warning "Common mistake: \"only set the capacities of unsaturated edges to $\infty$\""
        This approach has a common incorrect version: after computing the maximum flow, set the capacities of saturated edges to $1$ and of unsaturated edges to $\infty$, and directly run a minimum cut. This seems intuitive but is actually wrong. A counterexample is shown in the figure below.
        
        ![](images/min-cut-1.svg)
        
        As shown, the maximum flow is $16$ (i.e. all out-edges of $s$ are saturated), the maximum flow is unique, and only the edge $A\to B$ is unsaturated. Every minimum cut of the original graph has $3$ cut edges, but after resetting the capacities as in the incorrect version, the minimum cut of the new graph is $2$, attained at $S = \{s,x,y,B\}$. The capacity of this cut is $20$, so it is not a minimum cut of the original graph: although its forward edges $s\to A$ and $B\to t$ are saturated, the edge $A\to B$, which carries flow, points from the $T$ side back to the $S$ side, and the incorrect version does not rule out this case. In the correct approach, $A\to B$ carries flow, so a backward edge $B\to A$ of capacity $\infty$ is added, which prevents this incorrect minimum cut from appearing.

## Problem model 1

There are $n$ items and two sets $A,B$. If an item is not put into set $A$ it costs $a_i$, and if it is not put into set $B$ it costs $b_i$; there are also several constraints of the form $u_i,v_i,w_i$, meaning that it costs $w_i$ if $u_i$ and $v_i$ are not in the same set. Every item must belong to exactly one set; find the minimum cost.

This is a classic **choose one of two** minimum cut problem. For the two sets we set up a source $s$ and a sink $t$; from $s$ to the $i$-th vertex we add an edge of capacity $a_i$, and from the $i$-th vertex to $t$ an edge of capacity $b_i$. For a constraint $u,v,w$ we add a bidirectional edge of capacity $w$ between $u$ and $v$.

Note that when the source and the sink are disconnected, every vertex has chosen one of the sets. Cutting an edge to $s$ or $t$ means not putting the item into $A$ or $B$ respectively, and cutting an edge between two items means that the two items are not in the same set.

The minimum cut is the minimum cost.

## Problem model 2

Maximum weight closure: given a directed graph in which every vertex has a weight (positive, negative or $0$), choose a subgraph of maximum total weight such that every successor of every vertex in the subgraph is also in the subgraph.

Approach: create a super source $s$ and a super sink $t$. If a vertex $u$ has positive weight, add a directed edge from $s$ to $u$ whose weight equals the vertex weight; if a vertex $u$ has negative weight, add a directed edge from $u$ to $t$ whose weight is the negative of the vertex weight. Set the weights of all edges of the original graph to $\infty$. Run a maximum flow; the answer is the sum of all positive weights minus the maximum flow.

A few short claims for the proof:

1.  Every valid subgraph corresponds to a cut in the flow network. Each cut divides the network into two parts, and the part connected to $s$ has no edge pointing into the other part, so the condition above holds. This statement is both necessary and sufficient.
2.  The edges removed by a minimum cut must be incident to either $s$ or $t$, since otherwise their weight is $\infty$ and they could not be part of a minimum cut.
3.  For the chosen subgraph, total weight $=$ sum of all positive weights $-$ sum of the weights of the unchosen positive-weight vertices $+$ sum of the weights of the chosen negative-weight vertices. When we do not choose a positive-weight vertex, its edge to $s$ is cut; when we choose a negative-weight vertex, its edge to $t$ is cut. The sum of the weights of the cut edges is the capacity of the cut. Thus the formula above becomes: total weight $=$ sum of all positive weights $-$ capacity of the cut.
4.  Hence we conclude: maximum total weight $=$ sum of all positive weights $-$ minimum cut $=$ sum of all positive weights $-$ maximum flow.

## Exercises

-   ["USACO 4.4" Pollutant Control](https://www.luogu.com.cn/problem/P1344)
-   ["USACO 5.4" Telecowmunication](https://www.luogu.com.cn/problem/P1345)
-   ["Luogu 1361" Little M's Crops](https://www.luogu.com.cn/problem/P1361)
-   ["SHOI 2007" Well-Intentioned Voting](https://www.luogu.com.cn/problem/P2057)
-   [Space Flight Program](https://www.luogu.com.cn/problem/P2762)
