// F. Pokrivanje
// Korijenimo stablo. F[v] = najbolji zbroj puteva s LCA u podstablu v.
// Za put s LCA v troši se 1 ili 2 bridova prema djeci, a "lanac" od djeteta do
// krajnje točke a prolazi vrhovima x na kojima je rezerviran po jedan brid prema
// dolje; njegova cijena je zbroj e[x] = max_{maska bez x} dp[p(x)][maska] - F[x]
// duž lanca (prefiksna suma po dubini, Fenwick s dodavanjem na podstablo).
// dp[v][maska] = g[maska] + sum_{c ∉ maska} F[c], gdje je g[maska] najbolje
// pokrivanje maske bridova disjunktnim putevima s LCA v (DP po podskupovima,
// O(2^deg * deg)).  Ukupno O(sum 2^deg * deg + m log n).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll NEG = LLONG_MIN / 4;

int n, m, k;
vector<vector<int>> adj, children;
vector<int> par, dep, tin, tout, order_, cidx;
vector<vector<int>> up;
int LOG;

struct Fenwick {                       // dodavanje na interval, upit u točki
    int n; vector<ll> t;
    Fenwick(int n) : n(n), t(n + 1, 0) {}
    void add(int i, ll v) { for (; i <= n; i += i & -i) t[i] += v; }
    void range_add(int l, int r, ll v) { add(l, v); if (r + 1 <= n) add(r + 1, -v); }
    ll query(int i) { ll s = 0; for (; i > 0; i -= i & -i) s += t[i]; return s; }
};

int lift(int v, int d) {               // predak vrha v udaljen d koraka
    for (int j = 0; d > 0; ++j, d >>= 1) if (d & 1) v = up[j][v];
    return v;
}
int lca(int a, int b) {
    if (dep[a] < dep[b]) swap(a, b);
    a = lift(a, dep[a] - dep[b]);
    if (a == b) return a;
    for (int j = LOG - 1; j >= 0; --j) if (up[j][a] != up[j][b]) { a = up[j][a]; b = up[j][b]; }
    return up[0][a];
}

struct Path { int sa, sb, a, b; ll w; };   // sa, sb = indeks djeteta prema a odn. b (-1 ako je a == v)

int main() {
    scanf("%d %d %d", &n, &m, &k);
    adj.assign(n + 1, {});
    for (int i = 0; i < n - 1; ++i) { int x, y; scanf("%d %d", &x, &y); adj[x].push_back(y); adj[y].push_back(x); }
    // iterativni DFS iz korijena 1: roditelj, dubina, euler-interval, poredak
    par.assign(n + 1, 0); dep.assign(n + 1, 0); tin.assign(n + 1, 0); tout.assign(n + 1, 0);
    children.assign(n + 1, {}); cidx.assign(n + 1, 0);
    {
        vector<int> st = {1}, it(n + 1, 0);
        int timer = 0; par[1] = 0; tin[1] = ++timer; order_.push_back(1);
        while (!st.empty()) {
            int v = st.back();
            if (it[v] < (int)adj[v].size()) {
                int w = adj[v][it[v]++];
                if (w == par[v]) continue;
                par[w] = v; dep[w] = dep[v] + 1; tin[w] = ++timer;
                cidx[w] = children[v].size(); children[v].push_back(w);
                order_.push_back(w); st.push_back(w);
            } else { tout[v] = timer; st.pop_back(); }
        }
    }
    LOG = 1; while ((1 << LOG) <= n) ++LOG;
    up.assign(LOG, vector<int>(n + 1, 0));
    for (int v = 1; v <= n; ++v) up[0][v] = par[v] ? par[v] : v;
    for (int j = 1; j < LOG; ++j) for (int v = 1; v <= n; ++v) up[j][v] = up[j - 1][up[j - 1][v]];

    vector<vector<Path>> at(n + 1);        // putevi grupirani po LCA
    for (int i = 0; i < m; ++i) {
        int a, b; ll w; scanf("%d %d %lld", &a, &b, &w);
        int l = lca(a, b);
        Path p{-1, -1, a, b, w};
        if (a != l) p.sa = cidx[lift(a, dep[a] - dep[l] - 1)];
        if (b != l) p.sb = cidx[lift(b, dep[b] - dep[l] - 1)];
        at[l].push_back(p);
    }

    vector<ll> F(n + 1, 0);
    Fenwick fen(n);
    vector<ll> P, g, dp, sub, bestExcl;
    for (int idx = n - 1; idx >= 0; --idx) {   // djeca prije roditelja
        int v = order_[idx];
        int d = children[v].size();
        int full = 1 << d;
        P.assign(full, NEG);
        for (const Path& p : at[v]) {          // vrijednost puta s rezerviranim lancima
            ll val = p.w;
            int mask = 0;
            if (p.sa >= 0) { val += F[p.a] + fen.query(tin[p.a]); mask |= 1 << p.sa; }
            if (p.sb >= 0) { val += F[p.b] + fen.query(tin[p.b]); mask |= 1 << p.sb; }
            P[mask] = max(P[mask], val);
        }
        g.assign(full, NEG); g[0] = 0;
        sub.assign(full, 0);
        for (int mask = 1; mask < full; ++mask) {
            int low = mask & -mask, li = __builtin_ctz(mask);
            sub[mask] = sub[mask ^ low] + F[children[v][li]];
            ll best = NEG;
            if (P[low] > NEG && g[mask ^ low] > NEG) best = g[mask ^ low] + P[low];
            for (int rest = mask ^ low; rest; rest &= rest - 1) {
                int j = rest & -rest;
                if (P[low | j] > NEG && g[mask ^ low ^ j] > NEG) best = max(best, g[mask ^ low ^ j] + P[low | j]);
            }
            g[mask] = best;
        }
        ll sumF = sub[full - 1];
        dp.assign(full, NEG);
        bestExcl.assign(d, NEG);
        ll Fv = NEG;
        for (int mask = 0; mask < full; ++mask) {
            if (g[mask] == NEG) continue;
            dp[mask] = g[mask] + (sumF - sub[mask]);
            Fv = max(Fv, dp[mask]);
            for (int i = 0; i < d; ++i) if (!(mask >> i & 1)) bestExcl[i] = max(bestExcl[i], dp[mask]);
        }
        F[v] = Fv;
        for (int i = 0; i < d; ++i) {          // e[c] za svako dijete c: rezerviran brid (v,c)
            int c = children[v][i];
            ll e = bestExcl[i] - F[c];
            fen.range_add(tin[c], tout[c], e);
        }
    }
    printf("%lld\n", F[1]);
    return 0;
}
