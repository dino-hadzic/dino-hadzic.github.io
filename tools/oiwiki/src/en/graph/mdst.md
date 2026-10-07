---
title: Minimum diameter spanning tree
---

Before learning about the minimum diameter spanning tree, we recommend reading [Tree diameter](./tree-diameter.md) first.

## Definition

Among all spanning trees of an undirected graph, the one with the smallest diameter is the minimum diameter spanning tree.

## Absolute center of a graph

To find the minimum diameter spanning tree, we first need to find the **absolute center of the graph**. The **absolute center of the graph** may lie on an edge or at a vertex; it is the point for which the maximum of the shortest distances to all vertices is minimal.

From the definition of the **absolute center of the graph** it follows that there are at least two vertices farthest from the absolute center.

Let $d(i,j)$ be the length of the shortest path between vertices $i,j$; compute the shortest paths between all vertices with a multi-source shortest path algorithm.

$\textit{rk}(i,j)$ records the $j$-th closest vertex to vertex $i$ among all other vertices.

The absolute center of the graph may lie on an edge: enumerate every edge $w=(u,v)$ and assume the absolute center $c$ lies on that edge. Then the distance to $u$ is $x$ ($x \leq w$) and the distance to $v$ is $w - x$.

For any vertex $i$ of the graph, the distance from the absolute center $c$ to $i$ is $d(c,i)=\min(d(u,i) + x, d(v,i) + (w - x))$.

Take a vertex $i$ as an example; the positional relationship between this vertex and the absolute center of the graph is shown below.

![mdst1](./images/mdst-graph.svg)

As the absolute center $c$ moves along the edge, we get the graph of the distance as a function of the position of $c$. Clearly, the graph of the function $d(c,i)$ is a polyline made of two segments with the same slope.

![mdst2](./images/mdst-plot1.svg)

For any vertex of the graph, the function giving the distance from the absolute center to the farthest vertex is written as $f = \max\{ d(c,i)\},i \in[1,n]$, and its graph looks like this.

![mdst3](./images/mdst-plot2.svg)

The abscissa of the lowest point among the intersections of these polylines is the position of the absolute center of the graph.

The absolute center of the graph may also be at a vertex; then we update using the vertex farthest from the candidate vertex, i.e. $\textit{ans}\leftarrow \min(\textit{ans},d(i,\textit{rk}(i,n))\times 2)$.

### Procedure

1.  Use a multi-source shortest path algorithm ([Floyd](./shortest-path.md#floyd-算法), [Johnson](./shortest-path.md#johnson-全源最短路径算法), etc.) to compute the array $d$;

2.  Compute $\textit{rk}(i,j)$ and sort it in ascending order;

3.  The absolute center of the graph may be at a vertex: update using the vertex farthest from the candidate vertex; iterate over all vertices and update the minimum with $\textit{ans}\leftarrow \min(\textit{ans},d(i,\textit{rk}(i,n)) \times 2)$.

4.  The absolute center of the graph may lie on an edge: enumerate all edges. For an edge $w(u,v)$, start updating from the vertex farthest from $u$. When $d(v,\textit{rk}(u,i)) > \max_{j=i+1}^n d(v,\textit{rk}(u,j))$ occurs, update with $\textit{ans}\leftarrow  \min(\textit{ans}, d(u,\textit{rk}(u,i))+\max_{j=i+1}^n d(v,\textit{rk}(u,j))+w(u,v))$, because in this case the absolute center of the graph changes.

??? note "Implementation"
    ```cpp
    bool cmp(int a, int b) { return val[a] < val[b]; }
    
    void Floyd() {
      for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
          for (int j = 1; j <= n; j++) d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
    }
    
    void solve() {
      Floyd();
      for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
          rk[i][j] = j;
          val[j] = d[i][j];
        }
        sort(rk[i] + 1, rk[i] + 1 + n, cmp);
      }
      int ans = INF;
      // the absolute center of the graph may be at a vertex
      for (int i = 1; i <= n; i++) ans = min(ans, d[i][rk[i][n]] * 2);
      // the absolute center of the graph may be on an edge
      for (int i = 1; i <= m; i++) {
        int u = a[i].u, v = a[i].v, w = a[i].w;
        for (int p = n, i = n - 1; i >= 1; i--) {
          if (d[v][rk[u][i]] > d[v][rk[u][p]]) {
            ans = min(ans, d[u][rk[u][i]] + d[v][rk[u][p]] + w);
            p = i;
          }
        }
      }
    }
    ```

### Example

-   [CodeForce 266D BerDonalds](https://codeforces.com/contest/266/problem/D)

## Minimum diameter spanning tree

From the definition of the absolute center of the graph, it is easy to see that the absolute center is the midpoint of the diameter of the minimum diameter spanning tree.

To find the minimum diameter spanning tree, first find the absolute center of the graph. Starting from the absolute center, build a shortest path tree, and we obtain the minimum diameter spanning tree.

??? note "Implementation"
    ```cpp
    #include <algorithm>
    #include <climits>
    #include <iostream>
    #include <vector>
    using namespace std;
    constexpr int MAXN = 502;
    using ll = long long;
    using pii = pair<int, int>;
    ll d[MAXN][MAXN], dd[MAXN][MAXN], rk[MAXN][MAXN], val[MAXN];
    constexpr ll INF = 1e17;
    int n, m;
    
    bool cmp(int a, int b) { return val[a] < val[b]; }
    
    void floyd() {
      for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
          for (int j = 1; j <= n; j++) d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
    }
    
    struct node {
      ll u, v, w;
    } a[MAXN * (MAXN - 1) / 2];
    
    void solve() {
      // find the absolute center of the graph
      floyd();
      for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
          rk[i][j] = j;
          val[j] = d[i][j];
        }
        sort(rk[i] + 1, rk[i] + 1 + n, cmp);
      }
      ll P = 0, ansP = INF;
      // at a vertex
      for (int i = 1; i <= n; i++) {
        if (d[i][rk[i][n]] * 2 < ansP) {
          ansP = d[i][rk[i][n]] * 2;
          P = i;
        }
      }
      // on an edge
      int f1 = 0, f2 = 0;
      ll disu = INT_MIN, disv = INT_MIN, ansL = INF;
      for (int i = 1; i <= m; i++) {
        ll u = a[i].u, v = a[i].v, w = a[i].w;
        for (int p = n, i = n - 1; i >= 1; i--) {
          if (d[v][rk[u][i]] > d[v][rk[u][p]]) {
            if (d[u][rk[u][i]] + d[v][rk[u][p]] + w < ansL) {
              ansL = d[u][rk[u][i]] + d[v][rk[u][p]] + w;
              f1 = u, f2 = v;
              disu = (d[u][rk[u][i]] + d[v][rk[u][p]] + w) / 2 - d[u][rk[u][i]];
              disv = w - disu;
            }
            p = i;
          }
        }
      }
      cout << min(ansP, ansL) / 2 << '\n';
      // shortest path tree
      vector<pii> pp;
      for (int i = 1; i <= 501; ++i)
        for (int j = 1; j <= 501; ++j) dd[i][j] = INF;
      for (int i = 1; i <= 501; ++i) dd[i][i] = 0;
      if (ansP <= ansL) {
        for (int j = 1; j <= n; j++) {
          for (int i = 1; i <= m; ++i) {
            ll u = a[i].u, v = a[i].v, w = a[i].w;
            if (dd[P][u] + w == d[P][v] && dd[P][u] + w < dd[P][v]) {
              dd[P][v] = dd[P][u] + w;
              pp.push_back({u, v});
            }
            u = a[i].v, v = a[i].u, w = a[i].w;
            if (dd[P][u] + w == d[P][v] && dd[P][u] + w < dd[P][v]) {
              dd[P][v] = dd[P][u] + w;
              pp.push_back({u, v});
            }
          }
        }
        for (auto [x, y] : pp) cout << x << ' ' << y << '\n';
      } else {
        d[n + 1][f1] = disu;
        d[f1][n + 1] = disu;
        d[n + 1][f2] = disv;
        d[f2][n + 1] = disv;
        a[m + 1].u = n + 1, a[m + 1].v = f1, a[m + 1].w = disu;
        a[m + 2].u = n + 1, a[m + 2].v = f2, a[m + 2].w = disv;
        n += 1;
        m += 2;
        floyd();
        P = n;
        for (int j = 1; j <= n; j++) {
          for (int i = 1; i <= m; ++i) {
            ll u = a[i].u, v = a[i].v, w = a[i].w;
            if (dd[P][u] + w == d[P][v] && dd[P][u] + w < dd[P][v]) {
              dd[P][v] = dd[P][u] + w;
              pp.push_back({u, v});
            }
            u = a[i].v, v = a[i].u, w = a[i].w;
            if (dd[P][u] + w == d[P][v] && dd[P][u] + w < dd[P][v]) {
              dd[P][v] = dd[P][u] + w;
              pp.push_back({u, v});
            }
          }
        }
        cout << f1 << ' ' << f2 << '\n';
        for (auto [x, y] : pp)
          if (x != n && y != n) cout << x << ' ' << y << '\n';
      }
    }
    
    void init() {
      for (int i = 1; i <= 501; ++i)
        for (int j = 1; j <= 501; ++j) d[i][j] = INF;
      for (int i = 1; i <= 501; ++i) d[i][i] = 0;
    }
    
    int main() {
      init();
      cin >> n >> m;
      for (int i = 1; i <= m; ++i) {
        ll u, v, w;
        cin >> u >> v >> w;
        w *= 2;
        d[u][v] = w, d[v][u] = w;
        a[i].u = u, a[i].v = v, a[i].w = w;
      }
      solve();
      return 0;
    }
    ```

### Examples

[SPOJ MDST](https://www.spoj.com/problems/MDST/)

[timus 1569. Networking the "Iset"](https://acm.timus.ru/problem.aspx?space=1&num=1569)

[SPOJ PT07C - The GbAaY Kingdom](https://www.spoj.com/problems/PT07C)

## References

[Play with Trees Solutions The GbAaY Kingdom](https://adn.botao.hu/adn-backup/blog/attachments/month_0705/32007531153238.pdf)
