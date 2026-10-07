---
title: Directed acyclic graph
---

## Definition

Edges are directed, and there are no cycles.

The English name is Directed Acyclic Graph, abbreviated DAG.

## Properties

-   A graph that can be [topologically sorted](./topo.md) is necessarily a directed acyclic graph;

    If there is a cycle, any two vertices on the cycle fail the condition in every ordering.

-   A directed acyclic graph can always be topologically sorted;

    (By induction.) Suppose every directed acyclic graph with fewer than $k$ vertices can be topologically sorted; for a graph with exactly $k$ vertices, just consider the situation after the first step of topological sorting.

## Testing

How do we test whether a graph is a directed acyclic graph?

Just check whether it can be [topologically sorted](./topo.md).

Of course there is another way: run a [DFS](../search/dfs.md) on the graph and look in the resulting DFS tree for a non-tree edge pointing to an ancestor (a back edge). If there is one, the graph has a cycle.

## Applications

### Longest (shortest) path by DP

On a general graph, the best time complexity for the single-source longest (shortest) path is $O(nm)$ ([Bellman–Ford algorithm](./shortest-path.md#bellmanford-algorithm), works with negative weights) or $O(m \log m)$ ([Dijkstra's algorithm](./shortest-path.md#dijkstras-algorithm), for graphs without negative weights).

But on a DAG we can compute the longest (shortest) path by DP and improve the time complexity to $O(n+m)$. The transition is $dis_v = min(dis_v, dis_u + w_{u,v})$ or $dis_v = max(dis_v, dis_u + w_{u,v})$.

After topological sorting, traverse the vertices in topological order and use the current vertex to update the vertices after it.

```cpp
struct edge {
  int v, w;
};

int n, m;
vector<edge> e[MAXN];
vector<int> L;                               // stores the result of the topological sort
int max_dis[MAXN], min_dis[MAXN], in[MAXN];  // in stores the in-degree of every vertex

void toposort() {  // topological sort
  queue<int> S;
  memset(in, 0, sizeof(in));
  for (int i = 1; i <= n; i++) {
    for (int j = 0; j < e[i].size(); j++) {
      in[e[i][j].v]++;
    }
  }
  for (int i = 1; i <= n; i++)
    if (in[i] == 0) S.push(i);
  while (!S.empty()) {
    int u = S.front();
    S.pop();
    L.push_back(u);
    for (int i = 0; i < e[u].size(); i++) {
      if (--in[e[u][i].v] == 0) {
        S.push(e[u][i].v);
      }
    }
  }
}

void dp(int s) {  // single-source longest (shortest) path from s
  toposort();     // topological sort first
  memset(min_dis, 0x3f, sizeof(min_dis));
  memset(max_dis, 0, sizeof(max_dis));
  min_dis[s] = 0;
  for (int i = 0; i < L.size(); i++) {
    int u = L[i];
    for (int j = 0; j < e[u].size(); j++) {
      min_dis[e[u][j].v] = min(min_dis[e[u][j].v], min_dis[u] + e[u][j].w);
      max_dis[e[u][j].v] = max(max_dis[e[u][j].v], max_dis[u] + e[u][j].w);
    }
  }
}
```

See also: [DP on a DAG](../dp/dag.md).
