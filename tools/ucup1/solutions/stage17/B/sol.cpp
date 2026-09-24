// UCup 1, Stage 17, B - Disjoint Set Union
// Činjenice o DSU-u s kompresijom puta:
//  * korijen stabla je uvijek jedan od početnih korijena; roditelj nekog vrha
//    može postati samo trenutni korijen (find) -> g[v] je ili f[v] ("zadržan"),
//    ili početni korijen ("cilj" od v);
//  * find prolazi kroz sve pretke, pa ako je v pomaknut, pomaknuti su i svi
//    njegovi f-preci dubine >= 2 (djeca korijena find ne mijenja);
//  * vrh v iz početnog stabla T_z s ciljem rx != rz zadnji se put pomiče dok je
//    rx korijen stabla koje sadrži T_z, dakle rz je prestao biti korijen prije
//    rx: t(rz) < t(rx). Ti uvjeti (brid rz -> rx) moraju biti acikličan graf.
// Konstrukcija po topološkom redu t: najprije find za sve pomaknute vrhove
// (postaju djeca svog početnog korijena). Zatim za korijene po redu t:
// invarijanta je da su svi "neriješeni" vrhovi u stablu korijena m na dubini
// <= 2; find ih podiže na dubinu 1 (oni s ciljem m time su gotovi), pa stablo
// spajamo (unite) pod neriješeni cilj s najmanjim t. Lanac spajanja tako
// posjeti sve potrebne ciljeve, a find nikada ne prolazi kroz gotov vrh
// (osim kroz dijete korijena, što ga ne mijenja). Operacija <= n^2 + 2n.
#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> f, g, cur;
vector<pair<int, pair<int, int>>> ops;  // (tip, (x, y))

int findOp(int x) {  // stvarni find s kompresijom puta na trenutnom polju cur
    if (cur[x] == x) return x;
    return cur[x] = findOp(cur[x]);
}
void emitFind(int x) { ops.push_back({1, {x, 0}}); findOp(x); }
void emitUnite(int x, int y) {
    ops.push_back({2, {x, y}});
    int a = findOp(x), b = findOp(y);
    if (a != b) cur[a] = b;
}

bool solve() {
    ops.clear();
    // korijeni i dubine u f (f je garantirano šuma)
    vector<int> froot(n + 1, 0), depth(n + 1, -1);
    function<void(int)> dfsF = [&](int v) {
        if (depth[v] >= 0) return;
        if (f[v] == v) { froot[v] = v; depth[v] = 0; return; }
        dfsF(f[v]);
        froot[v] = froot[f[v]];
        depth[v] = depth[f[v]] + 1;
    };
    for (int v = 1; v <= n; v++) dfsF(v);

    // g mora biti šuma; groot
    vector<int> groot(n + 1, 0), state(n + 1, 0);
    for (int v = 1; v <= n; v++) {
        if (state[v]) continue;
        vector<int> path;
        int x = v;
        while (state[x] == 0 && g[x] != x) { state[x] = 1; path.push_back(x); x = g[x]; }
        if (state[x] == 1) return false;  // ciklus
        int r = (g[x] == x) ? x : groot[x];
        if (g[x] == x) groot[x] = x, state[x] = 2;
        for (int y : path) { groot[y] = r; state[y] = 2; }
    }
    // komponente se samo spajaju
    for (int v = 1; v <= n; v++) if (groot[v] != groot[froot[v]]) return false;

    // cilj svakog vrha
    vector<int> target(n + 1, 0);  // 0 = nema (zadržan ili završni korijen)
    vector<char> moved(n + 1, 0);
    for (int v = 1; v <= n; v++) {
        if (f[v] == v) {
            if (g[v] == v) continue;
            if (f[g[v]] != g[v]) return false;
            target[v] = g[v];
        } else {
            if (g[v] == f[v]) continue;
            if (f[g[v]] != g[v]) return false;  // roditelj može postati samo početni korijen
            target[v] = g[v];
            moved[v] = 1;
        }
    }
    // pomaknut vrh povlači pomak svih f-predaka dubine >= 2
    for (int v = 1; v <= n; v++) if (moved[v]) {
        int p = f[v];
        if (depth[p] >= 2 && !moved[p]) return false;
    }
    // ograničenja rz -> rx među korijenima, topološki red
    vector<vector<int>> adj(n + 1);
    vector<int> indeg(n + 1, 0);
    for (int v = 1; v <= n; v++) if (target[v] && target[v] != froot[v]) {
        adj[froot[v]].push_back(target[v]);
        indeg[target[v]]++;
    }
    vector<int> order, t(n + 1, -1);
    queue<int> q;
    int roots = 0;
    for (int v = 1; v <= n; v++) if (f[v] == v) { roots++; if (indeg[v] == 0) q.push(v); }
    while (!q.empty()) {
        int v = q.front(); q.pop();
        t[v] = order.size(); order.push_back(v);
        for (int w : adj[v]) if (--indeg[w] == 0) q.push(w);
    }
    if ((int)order.size() != roots) return false;  // ciklus u ograničenjima

    // konstrukcija
    cur = f;
    for (int v = 1; v <= n; v++) if (moved[v]) emitFind(v);
    vector<vector<int>> members(n + 1);
    for (int v = 1; v <= n; v++) members[froot[v]].push_back(v);
    for (int m : order) {
        // neriješeni vrhovi na dubini 2 podižemo na dubinu 1
        for (int v : members[m]) {
            if (!target[v] || cur[v] == target[v] || v == m) continue;
            if (cur[v] != m) {
                assert(cur[cur[v]] == m);
                emitFind(v);
            }
        }
        // spoji pod neriješeni cilj s najmanjim t
        int best = 0;
        for (int v : members[m]) {
            if (!target[v] || cur[v] == target[v]) continue;
            if (!best || t[target[v]] < t[best]) best = target[v];
        }
        if (g[m] == m) { assert(best == 0); continue; }
        assert(best != 0 && t[best] > t[m]);
        emitUnite(m, best);
        for (int v : members[m]) members[best].push_back(v);
        members[m].clear();
    }
    for (int v = 1; v <= n; v++) assert(cur[v] == g[v]);
    return true;
}

int main() {
    int T;
    scanf("%d", &T);
    string out;
    char buf[64];
    while (T--) {
        scanf("%d", &n);
        f.assign(n + 1, 0); g.assign(n + 1, 0);
        for (int i = 1; i <= n; i++) scanf("%d", &f[i]);
        for (int i = 1; i <= n; i++) scanf("%d", &g[i]);
        if (!solve()) { out += "NO\n"; continue; }
        snprintf(buf, sizeof buf, "YES\n%d\n", (int)ops.size());
        out += buf;
        for (auto &o : ops) {
            if (o.first == 1) snprintf(buf, sizeof buf, "1 %d\n", o.second.first);
            else snprintf(buf, sizeof buf, "2 %d %d\n", o.second.first, o.second.second);
            out += buf;
        }
    }
    fputs(out.c_str(), stdout);
    return 0;
}
