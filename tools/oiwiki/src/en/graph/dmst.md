---
title: Minimum arborescence
---

## Definition

A minimum spanning tree on a directed graph (Directed Minimum Spanning Tree) is called a minimum arborescence.

The commonly used algorithm is the Chu–Liu algorithm (also called Edmonds' algorithm), which solves the minimum arborescence problem in $O(nm)$ time.

## Procedure

1.  For every vertex, choose the incoming edge of minimum weight.
2.  If there is no cycle, the algorithm terminates; otherwise contract the cycle and update the distances from the other vertices to the cycle.

## Implementation

```cpp
bool solve() {
  ans = 0;
  int u, v, root = 0;
  for (;;) {
    f(i, 0, n) in[i] = 1e100;
    f(i, 0, m) {
      u = e[i].s;
      v = e[i].t;
      if (u != v && e[i].w < in[v]) {
        in[v] = e[i].w;
        pre[v] = u;
      }
    }
    f(i, 0, m) if (i != root && in[i] > 1e50) return 0;
    int tn = 0;
    memset(id, -1, sizeof id);
    memset(vis, -1, sizeof vis);
    in[root] = 0;
    f(i, 0, n) {
      ans += in[i];
      v = i;
      while (vis[v] != i && id[v] == -1 && v != root) {
        vis[v] = i;
        v = pre[v];
      }
      if (v != root && id[v] == -1) {
        for (int u = pre[v]; u != v; u = pre[u]) id[u] = tn;
        id[v] = tn++;
      }
    }
    if (tn == 0) break;
    f(i, 0, n) if (id[i] == -1) id[i] = tn++;
    f(i, 0, m) {
      u = e[i].s;
      v = e[i].t;
      e[i].s = id[u];
      e[i].t = id[v];
      if (e[i].s != e[i].t) e[i].w -= in[v];
    }
    n = tn;
    root = id[root];
  }
  return ans;
}
```

## Tarjan's DMST algorithm

Tarjan proposed an algorithm that solves the minimum arborescence problem in $O(m+n\log n)$ time.

The algorithm description and reference code here are based on Professor Uri Zwick's lecture notes; see the original for more details.

### Procedure

Tarjan's algorithm consists of two phases: **contraction** and **expansion**. We first describe the **contraction** phase.

We assume the input graph is strongly connected; if it is not, we add $O(n)$ edges of infinite weight to make it so.

We need a heap storing, for each vertex, the incoming edge indices, incoming edge weights, the total cost of the vertex and related information; since heaps will be merged later, it is implemented with a [leftist tree](../ds/leftist-tree.md) and a [DSU](../ds/dsu.md). In each step the algorithm picks an arbitrary vertex $v$ that is not the root and has no incoming edge in the heap yet, and adds the minimum incoming edge of $v$ to the heap. If the newly added edge forms a cycle with the edges in the heap, the vertices forming the cycle are contracted; we call these contracted vertices **supervertices** and continue the process. Once all vertices have been contracted into a single supervertex, the contraction phase ends. After the whole contraction phase we obtain a contraction tree, on which the expansion is then performed.

The edges in the heap always form a path $v_0\leftarrow v_1\leftarrow \dots\leftarrow v_k$; since the graph is strongly connected this path necessarily exists, and each $v_i$ may be an original single vertex or a contracted supervertex.

Initially $v_o=a$, where $a$ is an arbitrary vertex of the graph. Each time we pick a minimum incoming edge $v_k\leftarrow u$; if $u$ is not one of the vertices $v_0,v_1,\dots,v_k$, we extend the path with $v_{k+1}=u$. If $u$ is one of them, say $v_i$, we have found a cycle $v_i\leftarrow\dots\leftarrow v_k\leftarrow v_i$ and contract it into a single supervertex $c$.

Put all vertices or supervertices into a queue $P$ and initially choose an arbitrary vertex $a$; as long as the queue is not empty, perform the following steps:

1.  Choose the minimum incoming edge of $a$, making sure it is not a self-loop, and find the vertex $b$ at the other end. If vertex $b$ has not been recorded, no cycle has formed; set $a\leftarrow b$ and continue looking for a cycle.

2.  If $b$ has already been recorded, a cycle has appeared. Increase the total number of vertices by one, renumber all vertices on the cycle, merge the heaps, and update the total weights of the vertices/supervertices. Updating the weights means collecting all incoming edges of the vertices on the cycle and subtracting the weight of the incoming edge on the cycle.

![dmst1](./images/dmst1.png)

Taking the picture as an example, the strongly connected graph on the left becomes after contraction the contraction tree on the right, where $a$ is the supervertex obtained by contracting vertices 1 and 2, $b$ is the supervertex obtained by contracting vertices 3, 4 and 5, and $A$ is formed by contracting the two supervertices $a$ and $b$.

The expansion phase is relatively simple: starting from the originally required root $r$, expand every cycle on the path from $r$ to the root of the contraction tree. Then start from the ancestor $f_r$ of $r$ and expand the cycles on its path to the root, and so on until all vertices have been visited.

### Implementation

```cpp
#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
using namespace std;

using ll = long long;
constexpr int MAXN = 102;
constexpr int INF = 0x3f3f3f3f;

struct UnionFind {
  int fa[MAXN << 1];

  UnionFind() { memset(fa, 0, sizeof(fa)); }

  void clear(int n) { memset(fa + 1, 0, sizeof(int) * n); }

  int find(int x) { return fa[x] ? fa[x] = find(fa[x]) : x; }

  int operator[](int x) { return find(x); }
};

struct Edge {
  int u, v, w, w0;
};

struct Heap {
  Edge *e;
  int rk, constant;
  Heap *lch, *rch;

  Heap(Edge *_e) : e(_e), rk(1), constant(0), lch(NULL), rch(NULL) {}

  void push() {
    if (lch) lch->constant += constant;
    if (rch) rch->constant += constant;
    e->w += constant;
    constant = 0;
  }
};

Heap *merge(Heap *x, Heap *y) {
  if (!x) return y;
  if (!y) return x;
  if (x->e->w + x->constant > y->e->w + y->constant) swap(x, y);
  x->push();
  x->rch = merge(x->rch, y);
  if (!x->lch || x->lch->rk < x->rch->rk) swap(x->lch, x->rch);
  if (x->rch)
    x->rk = x->rch->rk + 1;
  else
    x->rk = 1;
  return x;
}

Edge *extract(Heap *&x) {
  Edge *r = x->e;
  x->push();
  x = merge(x->lch, x->rch);
  return r;
}

vector<Edge> in[MAXN];
int n, m, fa[MAXN << 1], nxt[MAXN << 1];
Edge *ed[MAXN << 1];
Heap *Q[MAXN << 1];
UnionFind id;

void contract() {
  bool mark[MAXN << 1];
  // For every vertex of the graph, record the vertices connected to it.
  for (int i = 1; i <= n; i++) {
    queue<Heap *> q;
    for (int j = 0; j < in[i].size(); j++) q.push(new Heap(&in[i][j]));
    while (q.size() > 1) {
      Heap *u = q.front();
      q.pop();
      Heap *v = q.front();
      q.pop();
      q.push(merge(u, v));
    }
    Q[i] = q.front();
  }
  mark[1] = true;
  for (int a = 1, b = 1, p; Q[a]; b = a, mark[b] = true) {
    // Find the minimum incoming edge and its endpoint, making sure there is no self-loop.
    do {
      ed[a] = extract(Q[a]);
      a = id[ed[a]->u];
    } while (a == b && Q[a]);
    if (a == b) break;
    if (!mark[a]) continue;
    // Contract the cycle found, renumber the vertices in the cycle and update the total weights.
    for (a = b, n++; a != n; a = p) {
      id.fa[a] = fa[a] = n;
      if (Q[a]) Q[a]->constant -= ed[a]->w;
      Q[n] = merge(Q[n], Q[a]);
      p = id[ed[a]->u];
      nxt[p == n ? b : p] = a;
    }
  }
}

ll expand(int x, int r);

ll expand_iter(int x) {
  ll r = 0;
  for (int u = nxt[x]; u != x; u = nxt[u]) {
    if (ed[u]->w0 >= INF)
      return INF;
    else
      r += expand(ed[u]->v, u) + ed[u]->w0;
  }
  return r;
}

ll expand(int x, int t) {
  ll r = 0;
  for (; x != t; x = fa[x]) {
    r += expand_iter(x);
    if (r >= INF) return INF;
  }
  return r;
}

void link(int u, int v, int w) { in[v].push_back({u, v, w, w}); }

int main() {
  int rt;
  scanf("%d %d %d", &n, &m, &rt);
  for (int i = 0; i < m; i++) {
    int u, v, w;
    scanf("%d %d %d", &u, &v, &w);
    link(u, v, w);
  }
  // guarantee strong connectivity
  for (int i = 1; i <= n; i++) link(i > 1 ? i - 1 : n, i, INF);
  contract();
  ll ans = expand(rt, n);
  if (ans >= INF)
    puts("-1");
  else
    printf("%lld\n", ans);
  return 0;
}
```

## References

Uri Zwick. (2013),[Directed Minimum Spanning Trees](http://www.cs.tau.ac.il/~zwick/grad-algo-13/directed-mst.pdf), Lecture notes on "Analysis of Algorithms"

<https://riteme.site/blog/2018-6-18/mdst.html#_3>
