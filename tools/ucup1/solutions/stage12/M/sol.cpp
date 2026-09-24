// M - Colorful Graph
// 1) Tarjan: sazmi jako povezane komponente (vrhovi iste SCC mogu dijeliti boju).
// 2) Na dobivenom DAG-u trazimo najmanji broj lanaca (skupova medusobno
//    usporedivih vrhova) = najmanje pokrivanje putevima u tranzitivnom zatvorenju
//    = N' - (najvece sparivanje u zatvorenju).
// 3) Sparivanje racunamo tokom bez eksplicitnog zatvorenja: src->V_i (1),
//    U_i->dst (1), V_a->U_b (inf) za bridove, U_i->V_i (inf) "prolaz kroz i".
// 4) Dekompozicijom toka na puteve dobijemo parove (i -> k), spojimo ih u lance.
#include <bits/stdc++.h>
using namespace std;

struct Edge { int to, cap; };
vector<Edge> E;
vector<vector<int>> adj;
void addEdge(int u, int v, int c) {
    adj[u].push_back(E.size()); E.push_back({v, c});
    adj[v].push_back(E.size()); E.push_back({u, 0});
}
vector<int> vis;
int stamp = 0;
// jedno prosirujuce trazenje (Ford-Fulkerson, DFS), tok je najvise N'
bool dfsAug(int u, int t) {
    if (u == t) return true;
    vis[u] = stamp;
    for (int id : adj[u]) {
        if (E[id].cap <= 0 || vis[E[id].to] == stamp) continue;
        if (dfsAug(E[id].to, t)) { E[id].cap--; E[id ^ 1].cap++; return true; }
    }
    return false;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> g(n + 1);
    vector<pair<int, int>> edges(m);
    for (auto &e : edges) { scanf("%d %d", &e.first, &e.second); g[e.first].push_back(e.second); }

    // Tarjanov algoritam (iterativno, radi dubine do 7000 i limita memorije)
    vector<int> idx(n + 1, 0), low(n + 1, 0), comp(n + 1, -1), st;
    vector<char> onSt(n + 1, 0);
    int timer = 0, ncomp = 0;
    for (int s = 1; s <= n; s++) {
        if (idx[s]) continue;
        vector<pair<int, size_t>> cs = {{s, 0}};
        idx[s] = low[s] = ++timer; st.push_back(s); onSt[s] = 1;
        while (!cs.empty()) {
            int v = cs.back().first;
            size_t &i = cs.back().second;
            if (i < g[v].size()) {
                int u = g[v][i++];
                if (!idx[u]) {
                    idx[u] = low[u] = ++timer; st.push_back(u); onSt[u] = 1;
                    cs.push_back({u, 0});
                } else if (onSt[u]) low[v] = min(low[v], idx[u]);
            } else {
                if (low[v] == idx[v]) {
                    while (true) {
                        int u = st.back(); st.pop_back(); onSt[u] = 0; comp[u] = ncomp;
                        if (u == v) break;
                    }
                    ncomp++;
                }
                cs.pop_back();
                if (!cs.empty()) low[cs.back().first] = min(low[cs.back().first], low[v]);
            }
        }
    }
    int K = ncomp;
    // mreza: src = 2K, dst = 2K+1, V_i = i, U_i = K + i
    int src = 2 * K, dst = 2 * K + 1;
    adj.assign(2 * K + 2, {});
    const int INF = 1e9;
    for (int i = 0; i < K; i++) {
        addEdge(src, i, 1);
        addEdge(K + i, dst, 1);
        addEdge(K + i, i, INF);  // U_i -> V_i: put moze "proci" kroz i
    }
    for (auto &e : edges) {
        int a = comp[e.first], b = comp[e.second];
        if (a != b) addEdge(a, K + b, INF);  // V_a -> U_b
    }
    vis.assign(2 * K + 2, 0);
    int flow = 0;
    while (true) { stamp++; if (!dfsAug(src, dst)) break; flow++; }

    // dekompozicija toka: za svaki V_i s tokom iz src prati jedinicu toka do U_k
    vector<int> nxt(K, -1), hasPred(K, 0), ptr(2 * K + 2, 0);
    for (int i = 0; i < K; i++) {
        // brid src->V_i je prvi dodan za i: pronadi ga
        int eid = -1;
        for (int id : adj[src]) if (E[id].to == i) { eid = id; break; }
        if (E[eid].cap != 0) continue;  // nema toka
        int u = i;
        while (u != dst) {
            // pronadi izlazni brid iz u s pozitivnim tokom (cap izvornog brida smanjen)
            bool moved = false;
            for (int &p = ptr[u]; p < (int)adj[u].size(); p++) {
                int id = adj[u][p];
                if (id & 1) continue;          // povratni brid
                if (E[id ^ 1].cap == 0) continue;  // tok na bridu = kapacitet povratnog
                E[id].cap++; E[id ^ 1].cap--;  // skini jedinicu toka
                if (E[id].to == dst) nxt[i] = u - K;
                u = E[id].to;
                moved = true;
                break;
            }
            if (!moved) break;  // ne bi se smjelo dogoditi
        }
        if (nxt[i] >= 0) hasPred[nxt[i]] = 1;
    }
    // lanci: krecemo od vrhova bez prethodnika, boja raste po lancu
    vector<int> color(K, 0);
    int c = 0;
    for (int i = 0; i < K; i++) {
        if (hasPred[i]) continue;
        c++;
        for (int u = i; u != -1; u = nxt[u]) color[u] = c;
    }
    for (int v = 1; v <= n; v++) printf("%d%c", color[comp[v]], v == n ? '\n' : ' ');
}
