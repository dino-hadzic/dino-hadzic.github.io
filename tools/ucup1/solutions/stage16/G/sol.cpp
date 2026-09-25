// UCup 1, Stage 16, zadatak G: Classical Graph Theory Problem
// Algoritam "EAS for Endvertex Constrained Graphs" iz clanka Cheston, Hedetniemi,
// Liestman, Stehman: "The even adjacency split problem for graphs" (odjeljak 3).
// Vrhove postupno rasporedujemo u V1 i V2 i brisemo ih iz grafa, cuvajuci
// invarijante: (1) ||V1| - |V2|| <= 1, (2) svaki rasporedeni vrh ima susjeda
// u suprotnom skupu. U svakom koraku:
//  - ako postoji "trojka" (vrh s >= 3 susjednih listova) -> Recover Triple,
//  - inace ako postoji list -> Recover Endvertex,
//  - inace uzmemo proizvoljan brid x-y, x u V1, y u V2, i obrisemo oba.
// Listovi nose tip: 0 = list u izvornom grafu, 1/2 = nastao brisanjem brida do
// vrha iz V1/V2 (takav list vec ima susjeda u tom skupu). Slozenost O(n + m).
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> adj;
vector<int> deg, side, tip, brojListova;
vector<char> ziv;
vector<int> listovi, trojke;  // stogovi s lijenom provjerom valjanosti
int vel[3];                   // vel[1] = |V1|, vel[2] = |V2|

static inline bool jeList(int v) { return ziv[v] && deg[v] == 1; }
static inline bool jeTrojka(int v) { return ziv[v] && brojListova[v] >= 3; }
static inline int manji() { return vel[1] <= vel[2] ? 1 : 2; }
static inline int drugi(int s) { return 3 - s; }

static void stavi(int v, int s) {  // v ide u skup s
    side[v] = s;
    ++vel[s];
}

// jedini zivi susjed lista v
static int susjedLista(int v) {
    for (int u : adj[v])
        if (ziv[u]) return u;
    return -1;
}

// Obrisi x i sve njegove bridove; azuriraj stupnjeve, listove, trojke.
static void prune(int x) {
    bool xList = (deg[x] == 1);
    ziv[x] = 0;
    for (int u : adj[x]) {
        if (!ziv[u]) continue;
        if (xList) --brojListova[u];  // x vise nije list susjedan u-u
        --deg[u];
        if (deg[u] == 1) {
            // u je postao list; tip ovisi o skupu u koji je stavljen x
            tip[u] = side[x];
            listovi.push_back(u);
            int z = susjedLista(u);
            if (++brojListova[z] >= 3) trojke.push_back(z);
        } else if (deg[u] == 0) {
            // u je izoliran: ako jos nije rasporeden, ide u manji skup
            if (!side[u]) stavi(u, manji());
            ziv[u] = 0;
        }
    }
}

// x je list, Triples je prazan: njegov susjed w ima najvise jos jedan list z.
static void recoverEndvertex(int x) {
    int w = susjedLista(x);
    int s = manji();
    stavi(x, s);
    for (int z : adj[w])
        if (z != x && jeList(z)) stavi(z, s);
    stavi(w, drugi(s));
    prune(w);  // brise i x, z (postaju izolirani, vec rasporedeni)
}

// x ima >= 3 susjedna lista (najvise 2 tipa 0).
static void recoverTriple(int x) {
    int cnt[3] = {0, 0, 0};
    vector<int> L;
    for (int u : adj[x])
        if (jeList(u)) { L.push_back(u); ++cnt[tip[u]]; }
    bool xUV2 = cnt[1] > cnt[2] ||
                (cnt[1] == cnt[2] && ((cnt[0] == 0 && vel[1] == vel[2] + 1) ||
                                      (cnt[0] == 2 && vel[1] == vel[2] - 1)));
    int sx = xUV2 ? 2 : 1;       // skup za x
    int prisilni = drugi(sx);    // listovi tipa 0 i tipa sx moraju u suprotni skup
    stavi(x, sx);
    for (int u : L)
        if (tip[u] == 0 || tip[u] == sx) stavi(u, prisilni);
    // listovi tipa drugi(sx) vec imaju susjeda u skupu drugi(sx): slobodno ih
    // dijelimo tako da skupovi ostanu uravnotezeni (svaki u trenutno manji)
    for (int u : L)
        if (tip[u] == prisilni) stavi(u, manji());
    prune(x);
}

int main() {
    int t;
    if (scanf("%d", &t) != 1) return 0;
    while (t--) {
        scanf("%d %d", &n, &m);
        adj.assign(n + 1, {});
        for (int i = 0; i < m; ++i) {
            int a, b;
            scanf("%d %d", &a, &b);
            adj[a].push_back(b);
            adj[b].push_back(a);
        }
        deg.assign(n + 1, 0); side.assign(n + 1, 0); tip.assign(n + 1, 0);
        brojListova.assign(n + 1, 0); ziv.assign(n + 1, 1);
        listovi.clear(); trojke.clear();
        vel[1] = vel[2] = 0;
        for (int v = 1; v <= n; ++v) {
            deg[v] = adj[v].size();
            if (deg[v] == 1) { listovi.push_back(v); tip[v] = 0; }
        }
        for (int v = 1; v <= n; ++v)
            for (int u : adj[v])
                if (deg[u] == 1) ++brojListova[v];
        for (int v = 1; v <= n; ++v)
            if (brojListova[v] >= 3) trojke.push_back(v);

        int sljedeci = 1;  // za "proizvoljan" zivi vrh
        int zivih = n;
        while (zivih > 0) {
            while (!trojke.empty() && !jeTrojka(trojke.back())) trojke.pop_back();
            while (!listovi.empty() && !jeList(listovi.back())) listovi.pop_back();
            int prije = vel[1] + vel[2];
            if (!trojke.empty()) {
                recoverTriple(trojke.back());
            } else if (!listovi.empty()) {
                recoverEndvertex(listovi.back());
            } else {
                while (!ziv[sljedeci]) ++sljedeci;
                int x = sljedeci, y = susjedLista(x);  // bilo koji zivi susjed
                stavi(x, 1);
                stavi(y, 2);
                prune(x);
                prune(y);
            }
            zivih -= vel[1] + vel[2] - prije;
        }
        int s = (vel[1] == n / 2) ? 1 : 2;
        bool prvi = true;
        for (int v = 1; v <= n; ++v)
            if (side[v] == s) { printf(prvi ? "%d" : " %d", v); prvi = false; }
        printf("\n");
    }
    return 0;
}
