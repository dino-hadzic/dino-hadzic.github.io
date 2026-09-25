// UCup 1, Stage 19 (NAC 2023), B. A Tree and Two Edges
// Izaberemo razapinjuće stablo T (DFS); preostala dva brida su e1, e2. Svaki jednostavan put
// u -> v koristi svaki dodatni brid najviše jednom, a između dodatnih bridova ide jedinstvenim
// putem u stablu. Kandidata je 1 + 4 + 8 = 13 (bez dodatnih bridova; jedan brid u dva smjera;
// oba brida u dva redoslijeda i dva smjera). Kandidat je jednostavan put točno kad su njegovi
// segmenti u stablu u parovima vršno disjunktni. Dva puta u stablu se sijeku točno kad dublji
// od njihova dva LCA-a leži na drugom putu (provjera u O(1) Eulerovim vremenima nakon LCA).
#include <bits/stdc++.h>
using namespace std;

int n, q;
vector<vector<int>> adj;
vector<int> tin, tout, dubina, roditelj;
vector<array<int, 17>> gore;
const int LOG = 17;

void dfs(int root) {
    // iterativni DFS (n do 5*10^4, izbjegavamo duboku rekurziju)
    int timer = 0;
    vector<int> st, it(n + 1, 0);
    st.push_back(root);
    roditelj[root] = root;
    dubina[root] = 0;
    tin[root] = timer++;
    vector<char> posjecen(n + 1, 0);
    posjecen[root] = 1;
    while (!st.empty()) {
        int u = st.back();
        if (it[u] < (int)adj[u].size()) {
            int v = adj[u][it[u]++];
            if (posjecen[v]) continue;
            posjecen[v] = 1;
            roditelj[v] = u;
            dubina[v] = dubina[u] + 1;
            tin[v] = timer++;
            st.push_back(v);
        } else {
            tout[u] = timer++;
            st.pop_back();
        }
    }
}

bool predak(int a, int b) {           // je li a predak od b (ili a == b)
    return tin[a] <= tin[b] && tout[b] <= tout[a];
}

int lca(int a, int b) {
    if (predak(a, b)) return a;
    if (predak(b, a)) return b;
    for (int k = LOG - 1; k >= 0; --k)
        if (!predak(gore[a][k], b)) a = gore[a][k];
    return gore[a][0];
}

// leži li vrh w na putu x - y u stablu
bool naPutu(int w, int x, int y) {
    int l = lca(x, y);
    return predak(l, w) && (predak(w, x) || predak(w, y));
}

// sijeku li se putovi x1-y1 i x2-y2 u stablu
bool sijeku(int x1, int y1, int x2, int y2) {
    int l1 = lca(x1, y1), l2 = lca(x2, y2);
    if (dubina[l1] < dubina[l2]) { swap(x1, x2); swap(y1, y2); swap(l1, l2); }
    // l1 je dublji: putovi se sijeku točno kad je l1 na putu x2-y2
    return predak(l2, l1) && (predak(l1, x2) || predak(l1, y2));
}

int main() {
    if (scanf("%d %d", &n, &q) != 2) return 0;
    adj.assign(n + 1, {});
    vector<pair<int, int>> bridovi(n + 1);
    for (auto &e : bridovi) {
        if (scanf("%d %d", &e.first, &e.second) != 2) return 0;
    }
    // razapinjuće stablo unijom-pronađi; dodatni bridovi idu u `extra`
    vector<int> dsu(n + 1);
    iota(dsu.begin(), dsu.end(), 0);
    function<int(int)> nadji = [&](int x) { return dsu[x] == x ? x : dsu[x] = nadji(dsu[x]); };
    vector<pair<int, int>> extra;
    for (auto &e : bridovi) {
        int a = nadji(e.first), b = nadji(e.second);
        if (a == b) { extra.push_back(e); continue; }
        dsu[a] = b;
        adj[e.first].push_back(e.second);
        adj[e.second].push_back(e.first);
    }
    tin.assign(n + 1, 0); tout.assign(n + 1, 0); dubina.assign(n + 1, 0); roditelj.assign(n + 1, 0);
    dfs(1);
    gore.assign(n + 1, {});
    for (int v = 1; v <= n; ++v) gore[v][0] = roditelj[v];
    for (int k = 1; k < LOG; ++k)
        for (int v = 1; v <= n; ++v) gore[v][k] = gore[gore[v][k - 1]][k - 1];

    while (q--) {
        int u, v;
        if (scanf("%d %d", &u, &v) != 2) return 0;
        int odgovor = 1;                                   // put u stablu
        // jedan dodatni brid (p, r): u -> p, brid, r -> v
        for (int i = 0; i < 2; ++i) {
            for (int smjer = 0; smjer < 2; ++smjer) {
                int p = smjer ? extra[i].second : extra[i].first;
                int r = smjer ? extra[i].first : extra[i].second;
                if (!sijeku(u, p, r, v)) ++odgovor;
            }
        }
        // oba brida: u -> p, brid, r -> s, brid, t -> v
        for (int prvi = 0; prvi < 2; ++prvi) {
            int drugi = 1 - prvi;
            for (int s1 = 0; s1 < 2; ++s1) for (int s2 = 0; s2 < 2; ++s2) {
                int p = s1 ? extra[prvi].second : extra[prvi].first;
                int r = s1 ? extra[prvi].first : extra[prvi].second;
                int s = s2 ? extra[drugi].second : extra[drugi].first;
                int t = s2 ? extra[drugi].first : extra[drugi].second;
                if (!sijeku(u, p, r, s) && !sijeku(u, p, t, v) && !sijeku(r, s, t, v)) ++odgovor;
            }
        }
        printf("%d\n", odgovor);
    }
    return 0;
}
