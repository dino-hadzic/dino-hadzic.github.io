// Brute force: izgradi cijeli graf (kaktus + ciklus listova DFS-stabla + stablo treće faze)
// i iscrpno prođi sve podskupove vrhova (N <= 20).
#include <bits/stdc++.h>
using namespace std;
int n, m;
vector<vector<int>> g; vector<int> par, dep, pre, chc; vector<char> vis;
void dfs(int v) {
    vis[v] = 1; pre.push_back(v);
    for (int w : g[v]) if (!vis[w]) { par[w] = v; dep[w] = dep[v] + 1; chc[v]++; dfs(w); }
}
int main() {
    scanf("%d %d", &n, &m);
    vector<long long> T(n); for (auto &t : T) scanf("%lld", &t);
    g.assign(n, {}); vector<unsigned> adj(n, 0);
    for (int i = 0; i < m; i++) { int u, v; scanf("%d %d", &u, &v); g[u].push_back(v); g[v].push_back(u); adj[u] |= 1u << v; adj[v] |= 1u << u; }
    int k; scanf("%d", &k);
    for (int i = 0; i < k; i++) { int x, y; scanf("%d %d", &x, &y); adj[x] |= 1u << y; adj[y] |= 1u << x; }
    par.assign(n, -1); dep.assign(n, 0); chc.assign(n, 0); vis.assign(n, 0);
    dfs(0);
    vector<int> leaves;
    for (int v : pre) if ((v == 0 && chc[v] == 1) || (v != 0 && chc[v] == 0)) leaves.push_back(v);
    for (size_t i = 0; i < leaves.size(); i++) {
        int a = leaves[i], b = leaves[(i + 1) % leaves.size()];
        adj[a] |= 1u << b; adj[b] |= 1u << a;
    }
    long long best = -1; unsigned bestMask = 0;
    for (unsigned mask = 0; mask < (1u << n); mask++) {
        bool ok = true; long long w = 0;
        for (int v = 0; v < n && ok; v++) if (mask >> v & 1) { if (adj[v] & mask) ok = false; w += T[v]; }
        if (ok && w > best) { best = w; bestMask = mask; }
    }
    vector<int> res; for (int v = 0; v < n; v++) if (bestMask >> v & 1) res.push_back(v);
    printf("%lld %d\n", best, (int)res.size());
    for (size_t i = 0; i < res.size(); i++) printf("%d%c", res[i], i + 1 == res.size() ? '\n' : ' ');
    if (res.empty()) printf("\n");
}
