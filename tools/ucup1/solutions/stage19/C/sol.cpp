// UCup 1, Stage 19 (NAC 2023), C. Broken Minimum Spanning Tree
// 1) Kruskalom nađemo MST T* koji među bridovima jednake težine preferira bridove početnog
//    stabla T -> T* ima najveći mogući presjek s T među svim MST-ovima (pohlepnost po matroidu).
// 2) Donja granica: svaka zamjena izbaci jedan brid, pa treba barem |T \ T*| zamjena.
// 3) Konstrukcija s točno toliko zamjena: dodaj brid f iz T* \ T_tren; na ciklusu koji nastaje
//    (f + put u stablu) postoji brid koji nije u T* (jer je T* acikličan) – izbaci ga.
//    Put u stablu nalazimo DFS-om, O(n) po zamjeni, ukupno O(n^2 + m log m).
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> U, V;
vector<long long> W;
vector<char> uStablu, uMst;
vector<vector<int>> adj;           // bridovi trenutnog stabla po vrhovima (indeksi bridova)

struct DSU {
    vector<int> p;
    DSU(int n) : p(n + 1) { iota(p.begin(), p.end(), 0); }
    int nadji(int x) { return p[x] == x ? x : p[x] = nadji(p[x]); }
    bool spoji(int a, int b) { a = nadji(a); b = nadji(b); if (a == b) return false; p[a] = b; return true; }
};

// nađi put a -> b u trenutnom stablu i vrati neki brid na putu koji nije u T*
int bridZaIzbaciti(int a, int b) {
    vector<int> roditeljBrid(n + 1, -1), st;
    vector<char> vidjen(n + 1, 0);
    st.push_back(a); vidjen[a] = 1;
    while (!st.empty()) {
        int x = st.back(); st.pop_back();
        if (x == b) break;
        for (int e : adj[x]) {
            int y = U[e] ^ V[e] ^ x;
            if (vidjen[y]) continue;
            vidjen[y] = 1;
            roditeljBrid[y] = e;
            st.push_back(y);
        }
    }
    for (int x = b; x != a; x = U[roditeljBrid[x]] ^ V[roditeljBrid[x]] ^ x) {
        int e = roditeljBrid[x];
        if (!uMst[e]) return e;
    }
    return -1;   // ne može se dogoditi: ciklus ne može biti cijeli u T*
}

int main() {
    if (scanf("%d %d", &n, &m) != 2) return 0;
    U.resize(m); V.resize(m); W.resize(m);
    uStablu.assign(m, 0); uMst.assign(m, 0);
    for (int i = 0; i < m; ++i) {
        if (scanf("%d %d %lld", &U[i], &V[i], &W[i]) != 3) return 0;
        uStablu[i] = (i < n - 1);
    }
    // Kruskal: po težini, a kod jednake težine prvo bridovi početnog stabla
    vector<int> red(m);
    iota(red.begin(), red.end(), 0);
    sort(red.begin(), red.end(), [&](int a, int b) {
        if (W[a] != W[b]) return W[a] < W[b];
        return uStablu[a] > uStablu[b];
    });
    DSU d(n);
    for (int e : red)
        if (d.spoji(U[e], V[e])) uMst[e] = 1;

    adj.assign(n + 1, {});
    for (int e = 0; e < n - 1; ++e) { adj[U[e]].push_back(e); adj[V[e]].push_back(e); }

    vector<pair<int, int>> zamjene;
    for (int f = 0; f < m; ++f) {
        if (!uMst[f] || uStablu[f]) continue;      // f je u T*, a nije u trenutnom stablu
        int e = bridZaIzbaciti(U[f], V[f]);
        // izbaci e iz stabla, dodaj f
        for (int x : {U[e], V[e]}) adj[x].erase(find(adj[x].begin(), adj[x].end(), e));
        adj[U[f]].push_back(f); adj[V[f]].push_back(f);
        uStablu[e] = 0; uStablu[f] = 1;
        zamjene.push_back({e + 1, f + 1});
    }
    printf("%d\n", (int)zamjene.size());
    for (auto &z : zamjene) printf("%d %d\n", z.first, z.second);
    return 0;
}
