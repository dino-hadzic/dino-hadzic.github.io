// E. Susjedstvo
// Centroidna dekompozicija. Za centroid c pamtimo udaljenosti dist(c, y) svih
// vrhova njegove komponente u DFS poretku (iz c). Promjena težine brida
// mijenja dist(c, y) za sve y u podstablu ispod tog brida -> dodavanje na
// interval. Upit (x, d) za svaki centroidni predak c od x broji vrhove y s
// dist(c, y) <= d - dist(c, x) u cijeloj komponenti, umanjeno za one iz
// pod-komponente koja sadrži x (oni se broje na dubljim razinama).
// Niz s "dodaj na interval" i "prebroji <= T na intervalu" održavamo
// sqrt-dekompozicijom (blokovi sa sortiranom kopijom i lijenom oznakom);
// djelomični blok se popravlja spajanjem (merge) u O(S). Veličine komponenti
// se po razinama polove, pa je ukupno O((n + q) sqrt(n) log n).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct Blocked {
    int m, S, nb;
    vector<ll> a, sv, lazy;     // vrijednosti, sortirane vrijednosti po blokovima, lijeni pomaci
    vector<int> sidx;           // indeks elementa uz sortiranu vrijednost
    void build(const vector<ll>& vals) {
        m = vals.size(); a = vals;
        S = max(1, (int)sqrt((double)m) + 1); nb = (m + S - 1) / S;
        lazy.assign(nb, 0); sv.resize(m); sidx.resize(m);
        for (int b = 0; b < nb; ++b) {
            int l = b * S, r = min(m, l + S);
            vector<pair<ll,int>> t;
            for (int i = l; i < r; ++i) t.push_back({a[i], i});
            sort(t.begin(), t.end());
            for (int i = l; i < r; ++i) { sv[i] = t[i - l].first; sidx[i] = t[i - l].second; }
        }
    }
    void partial_add(int b, int l, int r, ll delta) {   // [l, r] unutar bloka b
        int bl = b * S, br = min(m, bl + S);
        for (int i = l; i <= r; ++i) a[i] += delta;
        static vector<ll> v1, v2; static vector<int> i1, i2;
        v1.clear(); v2.clear(); i1.clear(); i2.clear();
        for (int i = bl; i < br; ++i) {
            if (l <= sidx[i] && sidx[i] <= r) { v1.push_back(sv[i] + delta); i1.push_back(sidx[i]); }
            else { v2.push_back(sv[i]); i2.push_back(sidx[i]); }
        }
        size_t p = 0, q = 0;
        for (int i = bl; i < br; ++i) {
            if (q == v2.size() || (p < v1.size() && v1[p] <= v2[q])) { sv[i] = v1[p]; sidx[i] = i1[p]; ++p; }
            else { sv[i] = v2[q]; sidx[i] = i2[q]; ++q; }
        }
    }
    void range_add(int l, int r, ll delta) {
        int bl = l / S, br = r / S;
        if (bl == br) { partial_add(bl, l, r, delta); return; }
        partial_add(bl, l, (bl + 1) * S - 1, delta);
        partial_add(br, br * S, r, delta);
        for (int b = bl + 1; b < br; ++b) lazy[b] += delta;
    }
    ll get(int i) const { return a[i] + lazy[i / S]; }
    int count_le(int l, int r, ll T) const {           // broj i u [l, r] s a[i] + lazy <= T
        if (l > r) return 0;
        int bl = l / S, br = r / S, res = 0;
        if (bl == br) { for (int i = l; i <= r; ++i) res += (a[i] + lazy[bl] <= T); return res; }
        for (int i = l; i < (bl + 1) * S; ++i) res += (a[i] + lazy[bl] <= T);
        for (int i = br * S; i <= r; ++i) res += (a[i] + lazy[br] <= T);
        for (int b = bl + 1; b < br; ++b) {
            ll t = T - lazy[b];
            res += upper_bound(sv.begin() + b * S, sv.begin() + min(m, (b + 1) * S), t) - (sv.begin() + b * S);
        }
        return res;
    }
};

struct AncInfo { int sid, pos, subL, subR; };   // struktura, pozicija x, interval pod-komponente koja sadrži x
struct RangeInfo { int sid, l, r; };

int n, q;
vector<vector<pair<int,int>>> adj;
vector<ll> ew;
vector<char> removed_;
vector<Blocked> structs;
vector<vector<AncInfo>> anc;
vector<vector<RangeInfo>> edgeRanges;

int main() {
    scanf("%d %d", &n, &q);
    adj.assign(n + 1, {}); ew.assign(n, 0);
    for (int i = 1; i < n; ++i) { int x, y; scanf("%d %d %lld", &x, &y, &ew[i]); adj[x].push_back({y, i}); adj[y].push_back({x, i}); }
    removed_.assign(n + 1, 0); anc.assign(n + 1, {}); edgeRanges.assign(n, {});
    vector<int> sz(n + 1, 0), par(n + 1, 0), parE(n + 1, 0), tin(n + 1, 0), tout(n + 1, 0), topc(n + 1, 0);
    vector<ll> dist(n + 1, 0);
    vector<int> comp, stk, order;
    // centroidna dekompozicija (eksplicitni stog)
    vector<int> todo = {1};
    while (!todo.empty()) {
        int root = todo.back(); todo.pop_back();
        // skupi komponentu i veličine podstabala (DFS iz root)
        comp.clear(); stk = {root}; par[root] = 0;
        while (!stk.empty()) {
            int v = stk.back(); stk.pop_back(); comp.push_back(v);
            for (auto [u, id] : adj[v]) if (!removed_[u] && u != par[v]) { par[u] = v; stk.push_back(u); }
        }
        for (int i = (int)comp.size() - 1; i >= 0; --i) { int v = comp[i]; sz[v] = 1; }
        for (int i = (int)comp.size() - 1; i >= 0; --i) { int v = comp[i]; if (par[v]) sz[par[v]] += sz[v]; }
        int total = comp.size(), c = root;
        while (true) {
            int nxt = 0;
            for (auto [u, id] : adj[c]) if (!removed_[u] && u != par[c] && sz[u] * 2 > total) { nxt = u; break; }
            if (!nxt) break;
            c = nxt;
        }
        // DFS iz centroida: poredak, intervali, udaljenosti, vršno dijete
        order.clear(); stk = {c}; par[c] = 0; parE[c] = 0; dist[c] = 0; topc[c] = 0;
        vector<int> it; // iterativni DFS s ulaznim/izlaznim vremenima
        {
            vector<pair<int,int>> st2 = {{c, 0}}; int timer = 0;
            while (!st2.empty()) {
                auto& [v, i] = st2.back();
                if (i == 0) { tin[v] = timer++; order.push_back(v); }
                if (i < (int)adj[v].size()) {
                    auto [u, id] = adj[v][i]; ++i;
                    if (removed_[u] || u == par[v]) continue;
                    par[u] = v; parE[u] = id; dist[u] = dist[v] + ew[id]; topc[u] = (v == c) ? u : topc[v];
                    st2.push_back({u, 0});
                } else { tout[v] = timer - 1; st2.pop_back(); }
            }
        }
        int sid = structs.size();
        vector<ll> vals(order.size());
        for (int v : order) vals[tin[v]] = dist[v];
        structs.emplace_back(); structs.back().build(vals);
        for (int v : order) {
            if (v != c) edgeRanges[parE[v]].push_back({sid, tin[v], tout[v]});
            int t = topc[v];
            anc[v].push_back({sid, tin[v], t ? tin[t] : -1, t ? tout[t] : -1});
        }
        removed_[c] = 1;
        for (auto [u, id] : adj[c]) if (!removed_[u]) todo.push_back(u);
    }
    string out;
    while (q--) {
        int t; scanf("%d", &t);
        if (t == 1) {
            int i; ll w; scanf("%d %lld", &i, &w);
            ll delta = w - ew[i]; ew[i] = w;
            if (delta) for (auto& r : edgeRanges[i]) structs[r.sid].range_add(r.l, r.r, delta);
        } else {
            int x; ll d; scanf("%d %lld", &x, &d);
            ll cnt = 0;
            for (auto& a : anc[x]) {
                const Blocked& B = structs[a.sid];
                ll dx = B.get(a.pos);
                if (dx > d) continue;
                ll T = d - dx;
                cnt += B.count_le(0, B.m - 1, T);
                if (a.subL >= 0) cnt -= B.count_le(a.subL, a.subR, T);
            }
            out += to_string(cnt); out += '\n';
        }
    }
    fputs(out.c_str(), stdout);
    return 0;
}
