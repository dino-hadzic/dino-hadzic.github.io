---
title: Minimum-cost flow
---

Before reading this article, please read the definitions section of [Introduction to network flow](../flow.md).

## Flow with costs

Given a network $G=(V,E)$, every edge, besides the capacity constraint $c(u,v)$, also has a cost $w(u,v)$ per unit of flow.

When the flow on $(u,v)$ is $f(u,v)$, a cost of $f(u,v)\times w(u,v)$ must be paid.

$w$ also satisfies skew symmetry, i.e. $w(u,v)=-w(v,u)$.

The maximum flow with the smallest total cost in this network is called the **minimum-cost maximum flow**, i.e. subject to maximizing $\sum_{(s,v)\in E}f(s,v)$, minimize $\sum_{(u,v)\in E}f(u,v)\times w(u,v)$.

## SSP algorithm

The SSP (Successive Shortest Path) algorithm is a greedy algorithm. Its idea is to repeatedly find the augmenting path with the smallest unit cost and augment along it, until no augmenting path exists in the graph.

If the graph contains a cycle with negative unit cost, the SSP algorithm cannot correctly compute the minimum-cost maximum flow of the network. In that case the negative cycles must first be removed with a cycle-canceling algorithm.

### Proof

We prove the correctness of the SSP algorithm using mathematical induction and contradiction.

Let $f_i$ be the minimum cost when the flow is $i$. We assume the initial network **has no negative cycles**; in this case $f_0=0$.

Suppose $f_i$ obtained by the SSP algorithm is the minimum cost; starting from $f_i$, we find a shortest augmenting path and thereby obtain $f_{i+1}$. Then $f_{i+1}-f_i$ is the length of this shortest augmenting path.

Suppose a smaller $f_{i+1}$ exists; call it $f'_{i+1}$. Since $f_{i+1}-f_i$ is already a shortest augmenting path, $f'_{i+1}-f_i$ must correspond to an augmenting path passing through **at least one negative cycle**.

Now the contradiction appears: if there is an augmenting path passing through at least one negative cycle, then $f_i$ is not the minimum cost, because by simply adding flow to this negative cycle we can make the cost corresponding to $f_i$ smaller without increasing the flow leaving $s$.

In summary, the SSP algorithm correctly computes the minimum-cost maximum flow of a network without negative cycles.

### Time complexity

If the [Bellman–Ford algorithm](../shortest-path.md#bellmanford-algorithm) is used for shortest paths, each search for an augmenting path takes $O(nm)$. Let the maximum flow of the network be $f$; then the worst-case time complexity is $O(nmf)$. In fact, the SSP algorithm runs in [pseudo-polynomial time](../../misc/cc-basic.md#pseudo-polynomial-time-伪多项式时间).

???+ note "Why is the SSP algorithm pseudo-polynomial?"
    The time complexity of the SSP algorithm has an upper bound of $O(nmf)$, which is a polynomial in the value range, so it is pseudo-polynomial.
    
    One can construct a network with $m=n^2,f=2^{n/2}$[^note1] on which the SSP algorithm's time complexity reaches $O(n^3 2^{n/2})$, so the SSP algorithm is not polynomial.

### Implementation

Simply replace the augmenting-path search in the EK algorithm or Dinic's algorithm with a shortest-path algorithm that finds the augmenting path with the smallest unit cost.

??? note "Implementation based on the EK algorithm"
    ```cpp
    struct qxx {
      int nex, t, v, c;
    };
    
    qxx e[M];
    int h[N], cnt = 1;
    
    void add_path(int f, int t, int v, int c) {
      e[++cnt] = qxx{h[f], t, v, c}, h[f] = cnt;
    }
    
    void add_flow(int f, int t, int v, int c) {
      add_path(f, t, v, c);
      add_path(t, f, 0, -c);
    }
    
    int dis[N], pre[N], incf[N];
    bool vis[N];
    
    bool spfa() {
      memset(dis, 0x3f, sizeof(dis));
      queue<int> q;
      q.push(s), dis[s] = 0, incf[s] = INF, incf[t] = 0;
      while (q.size()) {
        int u = q.front();
        q.pop();
        vis[u] = false;
        for (int i = h[u]; i; i = e[i].nex) {
          const int &v = e[i].t, &w = e[i].v, &c = e[i].c;
          if (!w || dis[v] <= dis[u] + c) continue;
          dis[v] = dis[u] + c, incf[v] = min(w, incf[u]), pre[v] = i;
          if (!vis[v]) q.push(v), vis[v] = true;
        }
      }
      return incf[t];
    }
    
    int maxflow, mincost;
    
    void update() {
      maxflow += incf[t];
      for (int u = t; u != s; u = e[pre[u] ^ 1].t) {
        e[pre[u]].v -= incf[t], e[pre[u] ^ 1].v += incf[t];
        mincost += incf[t] * e[pre[u]].c;
      }
    }
    
    // Usage: while(spfa())update();
    ```

??? note "Implementation based on Dinic's algorithm"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <queue>
    
    constexpr int N = 5e3 + 5, M = 1e5 + 5;
    constexpr int INF = 0x3f3f3f3f;
    int n, m, tot = 1, lnk[N], cur[N], ter[M], nxt[M], cap[M], cost[M], dis[N], ret;
    bool vis[N];
    
    void add(int u, int v, int w, int c) {
      ter[++tot] = v, nxt[tot] = lnk[u], lnk[u] = tot, cap[tot] = w, cost[tot] = c;
    }
    
    void addedge(int u, int v, int w, int c) { add(u, v, w, c), add(v, u, 0, -c); }
    
    bool spfa(int s, int t) {
      memset(dis, 0x3f, sizeof(dis));
      memcpy(cur, lnk, sizeof(lnk));
      std::queue<int> q;
      q.push(s), dis[s] = 0, vis[s] = true;
      while (!q.empty()) {
        int u = q.front();
        q.pop(), vis[u] = false;
        for (int i = lnk[u]; i; i = nxt[i]) {
          int v = ter[i];
          if (cap[i] && dis[v] > dis[u] + cost[i]) {
            dis[v] = dis[u] + cost[i];
            if (!vis[v]) q.push(v), vis[v] = true;
          }
        }
      }
      return dis[t] != INF;
    }
    
    int dfs(int u, int t, int flow) {
      if (u == t) return flow;
      vis[u] = true;
      int ans = 0;
      for (int &i = cur[u]; i && ans < flow; i = nxt[i]) {
        int v = ter[i];
        if (!vis[v] && cap[i] && dis[v] == dis[u] + cost[i]) {
          int x = dfs(v, t, std::min(cap[i], flow - ans));
          if (x) ret += x * cost[i], cap[i] -= x, cap[i ^ 1] += x, ans += x;
        }
      }
      vis[u] = false;
      return ans;
    }
    
    int mcmf(int s, int t) {
      int ans = 0;
      while (spfa(s, t)) {
        int x;
        while ((x = dfs(s, t, INF))) ans += x;
      }
      return ans;
    }
    
    int main() {
      int s, t;
      scanf("%d%d%d%d", &n, &m, &s, &t);
      while (m--) {
        int u, v, w, c;
        scanf("%d%d%d%d", &u, &v, &w, &c);
        addedge(u, v, w, c);
      }
      int ans = mcmf(s, t);
      printf("%d %d\n", ans, ret);
      return 0;
    }
    ```

### Primal-dual algorithm

Finding shortest paths with Bellman–Ford takes $O(nm)$, which is worse than Dijkstra's algorithm on both sparse and dense graphs[^note2]. However, the network contains edges with negative unit cost, so Dijkstra's algorithm cannot be applied directly.

The idea of the primal-dual algorithm is similar to [Johnson's all-pairs shortest path algorithm](../shortest-path.md#johnsons-all-pairs-shortest-path-algorithm): by assigning a potential to each vertex, the costs of all edges in the network (hereafter simply edge weights) become non-negative, so Dijkstra's algorithm can be used to find the augmenting path with the smallest unit cost.

First run a shortest-path algorithm once to compute the shortest distance from the source to each vertex (which is also the vertex's initial potential) $h_i$. Then, as in Johnson's algorithm, for an edge from $u$ to $v$ with unit cost $w$, reset its weight to $w+h_u-h_v$.

One can see that after setting potentials this way, shortest paths in the new network necessarily correspond to shortest paths in the original network. The proof was already given when introducing Johnson's algorithm and is not repeated here.

Unlike an ordinary shortest-path problem, the shape of the graph changes after every augmentation, so the potentials of the vertices need to be updated.

How to update them? First the conclusion: let $d'_i$ be the shortest distance from the source to vertex $i$ after augmentation (the distance obtained after resetting the weight of every edge); it suffices to add $d'_i$ to $h_i$. Below we prove that after updating the weights this way, all edge weights in the graph are non-negative.

It is easy to see that after one round of augmentation, since some edges $(i,j)$ lie on the augmenting path, correspondingly some edges $(j,i)$ appear in the residual network, and they must satisfy $d'_i+(w(i,j)+h_i-h_j)=d'_j$ (otherwise the edge $(i,j)$ would not be on the augmenting path). A slight rearrangement gives $w(j,i)+(h_j+d'_j)-(h_i+d'_i)=0$. Hence the weights of the newly added edges are non-negative.

As for the existing edges, before augmentation $d'_i+(w(i,j)+h_i-h_j) - d'_j \geq 0$, hence $w(i,j)+(d'_i+h_i)-(d'_j+h_j) \geq 0$, i.e. using $h_i+d'_i$ as the new potential does not make the weight of $(i,j)$ negative.

In summary, after augmentation all edge weights are non-negative, and Dijkstra's algorithm correctly finds the shortest paths in the graph.

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <queue>
    constexpr int INF = 0x3f3f3f3f;
    using namespace std;
    
    struct edge {
      int v, f, c, next;
    } e[100005];
    
    struct node {
      int v, e;
    } p[10005];
    
    struct mypair {
      int dis, id;
    
      bool operator<(const mypair& a) const { return dis > a.dis; }
    
      mypair(int d, int x) { dis = d, id = x; }
    };
    
    int head[5005], dis[5005], vis[5005], h[5005];
    int n, m, s, t, cnt = 1, maxf, minc;
    
    void addedge(int u, int v, int f, int c) {
      e[++cnt].v = v;
      e[cnt].f = f;
      e[cnt].c = c;
      e[cnt].next = head[u];
      head[u] = cnt;
    }
    
    bool dijkstra() {
      priority_queue<mypair> q;
      for (int i = 1; i <= n; i++) dis[i] = INF;
      memset(vis, 0, sizeof(vis));
      dis[s] = 0;
      q.push(mypair(0, s));
      while (!q.empty()) {
        int u = q.top().id;
        q.pop();
        if (vis[u]) continue;
        vis[u] = 1;
        for (int i = head[u]; i; i = e[i].next) {
          int v = e[i].v, nc = e[i].c + h[u] - h[v];
          if (e[i].f && dis[v] > dis[u] + nc) {
            dis[v] = dis[u] + nc;
            p[v].v = u;
            p[v].e = i;
            if (!vis[v]) q.push(mypair(dis[v], v));
          }
        }
      }
      return dis[t] != INF;
    }
    
    void spfa() {
      queue<int> q;
      memset(h, 63, sizeof(h));
      h[s] = 0, vis[s] = 1;
      q.push(s);
      while (!q.empty()) {
        int u = q.front();
        q.pop();
        vis[u] = 0;
        for (int i = head[u]; i; i = e[i].next) {
          int v = e[i].v;
          if (e[i].f && h[v] > h[u] + e[i].c) {
            h[v] = h[u] + e[i].c;
            if (!vis[v]) {
              vis[v] = 1;
              q.push(v);
            }
          }
        }
      }
    }
    
    int main() {
      scanf("%d%d%d%d", &n, &m, &s, &t);
      for (int i = 1; i <= m; i++) {
        int u, v, f, c;
        scanf("%d%d%d%d", &u, &v, &f, &c);
        addedge(u, v, f, c);
        addedge(v, u, 0, -c);
      }
      spfa();  // compute the initial potentials first
      while (dijkstra()) {
        int minf = INF;
        for (int i = 1; i <= n; i++) h[i] += dis[i];
        for (int i = t; i != s; i = p[i].v) minf = min(minf, e[p[i].e].f);
        for (int i = t; i != s; i = p[i].v) {
          e[p[i].e].f -= minf;
          e[p[i].e ^ 1].f += minf;
        }
        maxf += minf;
        minc += minf * h[t];
      }
      printf("%d %d\n", maxf, minc);
      return 0;
    }
    ```

## Exercises

-   ["Luogu 3381" [Template] Minimum-cost maximum flow](https://www.luogu.com.cn/problem/P3381)
-   ["Luogu 4452" Flight scheduling](https://www.luogu.com.cn/problem/P4452)
-   ["SDOI 2009" Morning run](https://www.luogu.com.cn/problem/P2153)
-   ["SCOI 2007" Car repair](https://www.luogu.com.cn/problem/P2053)
-   ["HAOI 2010" Ordering](https://www.luogu.com.cn/problem/P2517)
-   ["NOI 2012" Food festival](https://loj.ac/problem/2674)

## References and notes

[^note1]: For the detailed construction see [min\_25's blog](https://web.archive.org/web/20211009144446/https://min-25.hatenablog.com/entry/2018/03/19/235802).

[^note2]: On sparse graphs, with a heap optimization, a time complexity of $O(m \log n)$ is achievable; on dense graphs, without the heap, $O(n^2)$ is achievable.
