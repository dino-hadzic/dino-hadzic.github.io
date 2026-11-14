// A - Engineers, RMI 2025 Day 1
#include <bits/stdc++.h>
using namespace std;

#define REP(i, a, b) for (int i = (a); i <= (int)(b); ++i)
#define PER(i, a, b) for (int i = (a); i >= (int)(b); --i)
using VI = vector<int>;
using IP = array<int, 2>;

int solve(int N, int D, VI C, VI P, VI Q) {
  vector<VI> G(N);
  REP(i, 0, N - 2) G[P[i]].push_back(Q[i]), G[Q[i]].push_back(P[i]);
  int h = 1;
  while ((1 << h) <= N) ++h;
  vector<VI> up(N, VI(h));
  VI fa(N, -1), dep(N), tin(N), at(N), st = {0};
  int tm = 0;
  fa[0] = 0;
  while (!st.empty()) {
    int u = st.back();
    st.pop_back(), tin[u] = tm, at[tm++] = u;
    up[u][0] = fa[u];
    REP(j, 1, h - 1) up[u][j] = up[up[u][j - 1]][j - 1];
    for (int v : G[u]) if (v != fa[u])
      fa[v] = u, dep[v] = dep[u] + 1, st.push_back(v);
  }
  auto lca = [&](int u, int v) {
    if (dep[u] < dep[v]) swap(u, v);
    PER(j, h - 1, 0) if ((dep[u] - dep[v]) >> j & 1) u = up[u][j];
    if (u == v) return u;
    PER(j, h - 1, 0) if (up[u][j] != up[v][j]) u = up[u][j], v = up[v][j];
    return fa[u];
  };
  auto on_path = [&](int u, int a, int b) {
    int d = dep[a] + dep[b] - 2 * dep[lca(a, b)];
    return dep[a] + dep[b] + 2 * dep[u] - 2 * dep[lca(a, u)] - 2 * dep[lca(b, u)] == d;
  };
  set<int> s;
  int leaves = 0;
  auto leaf = [&](int t) {
    auto it = s.find(t), p = it, q = it;
    if (p == begin(s)) p = end(s);
    --p;
    if (++q == end(s)) q = begin(s);
    return !on_path(at[t], at[*p], at[*q]); // DFS 循环相邻点识别必要子树的叶子
  };
  auto neigh = [&](int t) {
    auto q = s.lower_bound(t);
    if (q == end(s)) q = begin(s);
    auto p = q;
    if (p == begin(s)) p = end(s);
    --p;
    return IP{*p, *q};
  };
  auto insert = [&](int u) {
    int t = tin[u];
    if ((int)s.size() < 3) {
      s.insert(t), leaves = 0;
      if (s.size() >= 2) for (int x : s) leaves += leaf(x);
      return;
    }
    auto [p, q] = neigh(t);
    leaves -= leaf(p) + leaf(q);
    s.insert(t), leaves += leaf(p) + leaf(q) + leaf(t);
  };
  auto erase = [&](int u) {
    int t = tin[u];
    if (s.size() <= 3) {
      s.erase(t), leaves = 0;
      if (s.size() >= 2) for (int x : s) leaves += leaf(x);
      return;
    }
    auto it = s.find(t), p = it, q = it;
    if (p == begin(s)) p = end(s);
    --p;
    if (++q == end(s)) q = begin(s);
    int a = *p, b = *q;
    leaves -= leaf(a) + leaf(b) + leaf(t);
    s.erase(t), leaves += leaf(a) + leaf(b);
  };
  VI ord(N);
  iota(begin(ord), end(ord), 0);
  sort(begin(ord), end(ord), [&](int u, int v) { return C[u] < C[v]; });
  REP(u, 0, N - 1) insert(u);
  int ans = N, r = 0;
  REP(l, 0, N - 1) {
    while (r < N and (long long)C[ord[r]] <= (long long)C[ord[l]] + D) erase(ord[r++]);
    int cur = s.empty() ? 0 : s.size() == 1 ? 1 : (leaves + 1) / 2;
    ans = min(ans, cur);
    insert(ord[l]);
  }
  return ans;
}

// https://qoj.ac/problem/16207
