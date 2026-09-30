// H. Not Another Path Query Problem – O(60 * (m + q) * alpha)
// Vrijednost puta je AND težina; ona je >= V ako je jednaka V ili se od V prvi put
// razlikuje na nekom bitu i tako da je taj bit u vrijednosti 1, a u V 0 (viši bitovi jednaki).
// Za svaki takav i maska M_i = (V s bitom i postavljenim, niži bitovi 0); dovoljno je da
// SVE težine na putu sadrže M_i. Za svaku od <= 61 maski gradimo DSU nad bridovima
// koji sadrže masku; upit je "Yes" ako su u i v spojeni za bar jednu masku.
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;

struct DSU {
    vector<int> p;
    DSU(int n) : p(n + 1) { iota(p.begin(), p.end(), 0); }
    int find(int x) { while (p[x] != x) x = p[x] = p[p[x]]; return x; }
    void unite(int a, int b) { a = find(a); b = find(b); if (a != b) p[a] = b; }
};

int main() {
    int n, m, q; ull V;
    scanf("%d %d %d %llu", &n, &m, &q, &V);
    vector<int> eu(m), ev(m); vector<ull> ew(m);
    for (int i = 0; i < m; i++) scanf("%d %d %llu", &eu[i], &ev[i], &ew[i]);
    vector<ull> masks = {V};                       // slučaj AND == V
    for (int i = 0; i < 60; i++)
        if (!(V >> i & 1)) masks.push_back(((V >> i) | 1ULL) << i);   // prvi različit bit je i
    int K = masks.size();
    // comp[k][v] = predstavnik komponente vrha v u grafu maske k
    vector<vector<int>> comp(K, vector<int>(n + 1));
    for (int k = 0; k < K; k++) {
        DSU d(n);
        for (int i = 0; i < m; i++)
            if ((ew[i] & masks[k]) == masks[k]) d.unite(eu[i], ev[i]);
        for (int v = 1; v <= n; v++) comp[k][v] = d.find(v);
    }
    string out;
    while (q--) {
        int u, v; scanf("%d %d", &u, &v);
        bool ok = false;
        for (int k = 0; k < K && !ok; k++) ok = comp[k][u] == comp[k][v];
        out += ok ? "Yes\n" : "No\n";
    }
    fputs(out.c_str(), stdout);
    return 0;
}
