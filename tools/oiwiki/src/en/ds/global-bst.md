---
title: Global balanced binary tree
---

## Introduction

Prerequisite: [heavy-light decomposition](../graph/hld.md)

The time complexity of heavy-light decomposition is $O(n\log^2 n)$, while the well-known LCT, although $O(n\log n)$, has a large constant factor and may even be slower than heavy-light decomposition. So is there a method that is both $O(n\log n)$ and has a relatively small constant? This is where the global balanced binary tree comes in.

A global balanced binary tree is actually a forest of binary trees, each of which maintains one heavy chain. The binary trees in this forest are nevertheless connected to each other: the root of each binary tree is linked to the parent of the top of its heavy chain, just like in an LCT. However, the global balanced binary tree is a static tree: unlike an LCT, its shape does not change after it is built.

The global balanced binary tree is a data structure for path updates/queries on a tree, and it achieves:

-   updating a whole path in $O(\log n)$;
-   querying a whole path in $O(\log n)$;
-   finding the lowest common ancestor, subtree updates, subtree queries, etc. in $O(\log n)$; these complexities are the same as for heavy-light decomposition.

## Main properties

1.  A global balanced binary tree consists of many binary trees connected by light edges; each binary tree maintains one heavy chain of the original tree, and its in-order traversal corresponds to the order of increasing depth along that heavy chain. Every node appears in exactly one binary tree.
2.  Edges are divided into heavy and light edges. Heavy edges are the edges contained in the binary trees and are maintained like in an ordinary binary tree: we record the left and right children and the parent. A light edge goes from the root of a binary tree to the parent of the top node of its heavy chain. Light edges are maintained in the "child knows parent, parent does not know child" fashion, i.e., the parent can be reached from the child but not the other way around. Note that the edges of the global balanced binary tree do not correspond to the edges of the original tree.
3.  Counting both heavy and light edges, the height of a global balanced binary tree is $O(\log n)$. This property guarantees the time complexity.

Below is an example of building a global balanced binary tree. The first figure is the original tree, rooted at node 1. Solid lines are heavy edges.

![global-bst-1](images/global-bst-1.svg)

The second figure is the resulting global balanced binary tree, where dashed lines are light edges, solid lines are heavy edges, and each binary tree is marked with a red circle.

![global-bst-2](images/global-bst-2.svg)

## Building the tree

First, as in ordinary heavy-light decomposition, one DFS determines the heavy child of each node. Then, starting from the root, find the heavy chain containing the root, recursively build trees for the light children of these nodes, and attach light edges. Next we need to build a binary tree for the nodes of the heavy chain. We first store the nodes of the heavy chain in an array and compute, for each node, the sum of the subtree sizes of its light children plus one (i.e. the size contributed by the node itself). Based on this we find the weighted midpoint of the heavy chain, make it the root of the binary tree, build both sides recursively, and attach heavy edges.

The code is as follows:

???+ note "Implementation"
    ```cpp
    std::vector<int> G[N];
    int n, fa[N], son[N], sz[N];
    
    void dfsS(int u) {
      sz[u] = 1;
      for (int v : G[u]) {
        dfsS(v);
        sz[u] += sz[v];
        if (sz[v] > sz[son[u]]) son[u] = v;
      }
    }
    
    int b[N], bs[N], l[N], r[N], f[N], ss[N];
    
    // build a binary tree over the points b[bl,br) and return its root
    int cbuild(int bl, int br) {
      int x = bl, y = br;
      while (y - x > 1) {
        int mid = (x + y) >> 1;
        if (2 * (bs[mid] - bs[bl]) <= bs[br] - bs[bl])
          x = mid;
        else
          y = mid;
      }
      // binary search for the weighted midpoint according to bs
      y = b[x];
      ss[y] = br - bl;  // ss: size of the heavy subtree in the binary tree
      if (bl < x) {
        l[y] = cbuild(bl, x);
        f[l[y]] = y;
      }
      if (x + 1 < br) {
        r[y] = cbuild(x + 1, br);
        f[r[y]] = y;
      }
      return y;
    }
    
    int build(int x) {
      int y = x;
      do
        for (int v : G[y])
          if (v != son[y])
            f[build(v)] =
                y;  // build recursively and attach light edges; the edge goes from the root of the binary tree, not from the child
      while (y = son[y]);
      y = 0;
      do {
        b[y++] = x;                              // store the nodes of the heavy chain
        bs[y] = bs[y - 1] + sz[x] - sz[son[x]];  // bs: sum of light children sizes + 1, as prefix sums
      } while (x = son[x]);
      return cbuild(0, y);
    }
    ```

From the code one can see that the construction takes $O(n\log n)$ time. Next we prove that the height of the tree is $O(\log n)$: consider jumping to the parent repeatedly from an arbitrary node up to the root. Jumping over a light edge corresponds to moving to another heavy chain in the original tree, so by the properties of heavy-light decomposition there are at most $O(\log n)$ light edges. Since the root of each binary tree is chosen as the weighted midpoint that accounts for the light children, every jump over a heavy edge at least doubles the size (light children included), so there are also at most $O(\log n)$ heavy edges. The overall height is therefore $O(\log n)$.

## Queries

That covers the global balanced binary tree itself. The remaining path update and path query operations are relatively simple: start from the node being operated on and keep jumping until the root is reached. Operating on all nodes of a node's heavy chain that are shallower than it is essentially the same as operating on all nodes to the left of the target node in the binary tree of that heavy chain. These operations decompose into a series of subtree operations, similar to maintaining an ordinary binary tree, involving subtree sums and subtree tags. In this process, permanent tags (without pushing them down) are used. One could also use pushdown for the tags and pushup for the subtree sums, but this may be more complicated: a binary tree is usually processed top-down, whereas here one would first have to determine the jump path and only then push down from top to bottom, which may increase the constant factor.

The code is as follows:

???+ note "Implementation"
    ```cpp
    // a: subtree addition tag
    // s: subtree sum (excluding the addition tag)
    int a[N], s[N];
    
    void add(int x) {
      bool t = true;
      int z = 0;
      while (x) {
        s[x] += z;
        if (t) {
          a[x]++;
          if (r[x]) a[r[x]]--;
          z += 1 + ss[l[x]];
          s[x] -= ss[r[x]];
        }
        t = (x != l[f[x]]);
        if (t && x != r[f[x]]) z = 0;  // reset when crossing a light edge
        x = f[x];
      }
    }
    
    int query(int x) {
      int ret = 0;
      bool t = true;
      int z = 0;
      while (x) {
        if (t) {
          ret += s[x] - s[r[x]];
          ret -= 1ll * ss[r[x]] * a[r[x]];
          z += 1 + ss[l[x]];
        }
        ret += 1ll * z * a[x];
        t = (x != l[f[x]]);
        if (t && x != r[f[x]]) z = 0;  // reset when crossing a light edge
        x = f[x];
      }
      return ret;
    }
    ```

Furthermore, for subtree operations, where light children must be taken into account, one also has to maintain a subtree sum and a subtree tag that include the light children; you can practice on "[Luogu P3384 【模板】轻重链剖分](https://www.luogu.com.cn/problem/P3384)".

## Example problem

??? note "[Luogu P4751 【模板】动态 DP & 动态树分治（加强版）](https://www.luogu.com.cn/problem/P4751)"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    constexpr int MAXN = 1000000;
    constexpr int MAXM = 3000000;
    constexpr int INF = 0x3FFFFFFF;
    using namespace std;
    
    struct edge {
      int to;
      edge *nxt;
    } edges[MAXN * 2 + 5];
    
    edge *ncnt = &edges[0], *Adj[MAXN + 5];
    int n, m;
    
    struct Matrix {
      int M[2][2];
    
      Matrix operator*(const Matrix &B) const {
        static Matrix ret;
        for (int i = 0; i < 2; i++)
          for (int j = 0; j < 2; j++) {
            ret.M[i][j] = -INF;
            for (int k = 0; k < 2; k++)
              ret.M[i][j] = max(ret.M[i][j], M[i][k] + B.M[k][j]);
          }
        return ret;
      }
    } matr1[MAXN + 5], matr2[MAXN + 5];  // each node maintains two matrices
    
    int root;
    int w[MAXN + 5], dep[MAXN + 5], son[MAXN + 5], siz[MAXN + 5], lsiz[MAXN + 5];
    int g[MAXN + 5][2], f[MAXN + 5][2], trfa[MAXN + 5], bstch[MAXN + 5][2];
    int stk[MAXN + 5], tp;
    bool vis[MAXN + 5];
    
    void AddEdge(int u, int v) {
      edge *p = ++ncnt;
      p->to = v;
      p->nxt = Adj[u];
      Adj[u] = p;
    
      edge *q = ++ncnt;
      q->to = u;
      q->nxt = Adj[v];
      Adj[v] = q;
    }
    
    void DFS(int u, int fa) {
      siz[u] = 1;
      for (edge *p = Adj[u]; p != NULL; p = p->nxt) {
        int v = p->to;
        if (v == fa) continue;
        dep[v] = dep[u] + 1;
        DFS(v, u);
        siz[u] += siz[v];
        if (!son[u] || siz[son[u]] < siz[v]) son[u] = v;
      }
      lsiz[u] = siz[u] - siz[son[u]];  // sum of siz of light children + 1
    }
    
    void DFS2(int u, int fa) {
      f[u][1] = w[u], f[u][0] = 0;
      g[u][1] = w[u], g[u][0] = 0;
      if (son[u]) {
        DFS2(son[u], u);
        f[u][0] += max(f[son[u]][0], f[son[u]][1]);
        f[u][1] += f[son[u]][0];
      }
      for (edge *p = Adj[u]; p != NULL; p = p->nxt) {
        int v = p->to;
        if (v == fa || v == son[u]) continue;
        DFS2(v, u);
        f[u][0] += max(f[v][0], f[v][1]);  // f[][] is the ordinary DP array
        f[u][1] += f[v][0];
        g[u][0] += max(f[v][0], f[v][1]);  // the g[][] array only accounts for the node itself and its light children
        g[u][1] += f[v][0];
      }
    }
    
    void PushUp(int u) {
      matr2[u] = matr1[u];  // matr1 is the node plus light children info, matr2 is the interval info
      if (bstch[u][0]) matr2[u] = matr2[bstch[u][0]] * matr2[u];
      // mind the direction of the transition; with a different matrix product definition the direction may differ
      if (bstch[u][1]) matr2[u] = matr2[u] * matr2[bstch[u][1]];
    }
    
    int getmx2(int u) { return max(matr2[u].M[0][0], matr2[u].M[0][1]); }
    
    int getmx1(int u) { return max(getmx2(u), matr2[u].M[1][0]); }
    
    int SBuild(int l, int r) {
      if (l > r) return 0;
      int tot = 0;
      for (int i = l; i <= r; i++) tot += lsiz[stk[i]];
      for (int i = l, sumn = lsiz[stk[l]]; i <= r; i++, sumn += lsiz[stk[i]])
        if (sumn * 2 >= tot)  // this is the centroid
        {
          int lch = SBuild(l, i - 1), rch = SBuild(i + 1, r);
          bstch[stk[i]][0] = lch;
          bstch[stk[i]][1] = rch;
          trfa[lch] = trfa[rch] = stk[i];
          PushUp(stk[i]);  // gather the interval information
          return stk[i];
        }
      return 0;
    }
    
    int Build(int u) {
      for (int pos = u; pos; pos = son[pos]) vis[pos] = true;
      for (int pos = u; pos; pos = son[pos])
        for (edge *p = Adj[pos]; p != NULL; p = p->nxt)
          if (!vis[p->to])  // a light child
          {
            int v = p->to, ret = Build(v);
            trfa[ret] = pos;  // attach the light child via treefa[]
          }
      tp = 0;
      for (int pos = u; pos; pos = son[pos]) stk[++tp] = pos;  // extract the heavy chain
      int ret = SBuild(1, tp);  // a separate SBuild for the heavy chain (Special Build, I guess?)
      return ret;               // return the root of the binary tree of the current heavy chain
    }
    
    void Modify(int u, int val) {
      matr1[u].M[1][0] += val - w[u];
      w[u] = val;
      for (int pos = u; pos; pos = trfa[pos])
        if (trfa[pos] && bstch[trfa[pos]][0] != pos && bstch[trfa[pos]][1] != pos) {
          matr1[trfa[pos]].M[0][0] -= getmx1(pos);
          matr1[trfa[pos]].M[0][1] = matr1[trfa[pos]].M[0][0];
          matr1[trfa[pos]].M[1][0] -= getmx2(pos);
          PushUp(pos);
          matr1[trfa[pos]].M[0][0] += getmx1(pos);
          matr1[trfa[pos]].M[0][1] = matr1[trfa[pos]].M[0][0];
          matr1[trfa[pos]].M[1][0] += getmx2(pos);
        } else
          PushUp(pos);
    }
    
    int read() {
      int ret = 0, f = 1;
      char c = 0;
      while (c < '0' || c > '9') {
        c = getchar();
        if (c == '-') f = -f;
      }
      ret = 10 * ret + c - '0';
      while (true) {
        c = getchar();
        if (c < '0' || c > '9') break;
        ret = 10 * ret + c - '0';
      }
      return ret * f;
    }
    
    void print(int x) {
      if (x == 0) return;
      print(x / 10);
      putchar(x % 10 + '0');
    }
    
    int main() {
      scanf("%d %d", &n, &m);
      for (int i = 1; i <= n; i++) w[i] = read();
      int u, v;
      for (int i = 1; i < n; i++) {
        u = read(), v = read();
        AddEdge(u, v);
      }
      DFS(1, -1);
      // compute heavy children
      DFS2(1, -1);
      // initial DP values; could be done in Build(), but this way it matches the HLD style
      for (int i = 1; i <= n; i++) {
        matr1[i].M[0][0] = matr1[i].M[0][1] = g[i][0];
        matr1[i].M[1][0] = g[i][1], matr1[i].M[1][1] = -INF;  // initialize matrices
      }
      root = Build(1);  // root is the centroid of the heavy chain containing the root node
      int lastans = 0;
      for (int i = 1; i <= m; i++) {
        u = read(), v = read();
        u ^= lastans;  // forced online
        Modify(u, v);
        lastans = getmx1(root);  // read the value directly
        if (lastans == 0)
          putchar('0');
        else
          print(lastans);
        putchar('\n');
      }
      return 0;
    }
    ```

## References

[P4211 \[LNOI2014\] LCA | 全局平衡二叉树](https://www.luogu.com.cn/blog/nederland/globalbst)
