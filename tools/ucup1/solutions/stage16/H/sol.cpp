// UCup 1, Stage 16, zadatak H: Classical Maximization Problem
// Bipartitni graf: vrhovi su razlicite x-koordinate i razlicite y-koordinate,
// svaka tocka je brid (x_i, y_i). Prijateljski par = dva brida sa zajednickim vrhom.
// U komponenti s m bridova moze se sloziti tocno floor(m/2) takvih parova:
// DFS stablo nema poprecnih bridova, pa obradom vrhova od dna prema vrhu svaki vrh v
// upari bridove koji su "ostali" njemu (nespareni bridovi do djece + povratni bridovi
// prema potomcima); ako ih je neparno mnogo, zadnji uparimo s bridom do roditelja.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    if (scanf("%d", &t) != 1) return 0;
    while (t--) {
        int n;
        scanf("%d", &n);
        int E = 2 * n;  // broj tocaka = bridova
        vector<long long> xs(E), ys(E);
        for (int i = 0; i < E; ++i) scanf("%lld %lld", &xs[i], &ys[i]);

        // kompresija koordinata: x-vrhovi 0..X-1, y-vrhovi X..X+Y-1
        vector<long long> sx(xs), sy(ys);
        sort(sx.begin(), sx.end()); sx.erase(unique(sx.begin(), sx.end()), sx.end());
        sort(sy.begin(), sy.end()); sy.erase(unique(sy.begin(), sy.end()), sy.end());
        int X = sx.size(), V = X + (int)sy.size();
        vector<int> eu(E), ev(E);
        vector<vector<int>> adj(V);  // indeksi bridova
        for (int i = 0; i < E; ++i) {
            eu[i] = lower_bound(sx.begin(), sx.end(), xs[i]) - sx.begin();
            ev[i] = X + (lower_bound(sy.begin(), sy.end(), ys[i]) - sy.begin());
            adj[eu[i]].push_back(i);
            adj[ev[i]].push_back(i);
        }

        // iterativni DFS: tin, roditeljski brid, redoslijed posjeta
        vector<int> tin(V, -1), parEdge(V, -1), order;
        vector<char> treeEdge(E, 0);
        vector<size_t> it(V, 0);
        int timer = 0;
        for (int s = 0; s < V; ++s) {
            if (tin[s] != -1) continue;
            vector<int> st = {s};
            tin[s] = timer++; order.push_back(s);
            while (!st.empty()) {
                int v = st.back();
                if (it[v] == adj[v].size()) { st.pop_back(); continue; }
                int e = adj[v][it[v]++];
                int u = eu[e] ^ ev[e] ^ v;
                if (tin[u] == -1) {
                    tin[u] = timer++; order.push_back(u);
                    parEdge[u] = e; treeEdge[e] = 1;
                    st.push_back(u);
                }
            }
        }

        // povratni bridovi pripadaju krajnjem vrhu koji je predak (manji tin)
        vector<vector<int>> dostupni(V);
        for (int e = 0; e < E; ++e)
            if (!treeEdge[e]) dostupni[tin[eu[e]] < tin[ev[e]] ? eu[e] : ev[e]].push_back(e);

        vector<pair<int, int>> parovi;
        vector<int> ostatak;  // po jedan nespareni brid iz svake neparne komponente
        for (int idx = V - 1; idx >= 0; --idx) {  // od potomaka prema precima
            int v = order[idx];
            vector<int>& S = dostupni[v];
            for (size_t i = 0; i + 1 < S.size(); i += 2) parovi.push_back({S[i], S[i + 1]});
            int pe = parEdge[v];
            if (S.size() % 2 == 1) {
                if (pe != -1) parovi.push_back({S.back(), pe});  // trosi brid do roditelja
                else ostatak.push_back(S.back());
            } else if (pe != -1) {
                int p = eu[pe] ^ ev[pe] ^ v;
                dostupni[p].push_back(pe);  // brid do roditelja ostaje roditelju
            }
        }
        int k = parovi.size();
        for (size_t i = 0; i + 1 < ostatak.size(); i += 2) parovi.push_back({ostatak[i], ostatak[i + 1]});

        printf("%d\n", k);
        for (auto [a, b] : parovi) printf("%d %d\n", a + 1, b + 1);
    }
    return 0;
}
