// UCup 1, Stage 15 (ZJCPC 2023), I. MEXimum Spanning Tree
// Presjek grafovskog matroida (šuma) i particijskog matroida (najviše jedan brid svake težine).
// Težine dodajemo redom K = 0, 1, 2, ...; u svakom koraku tražimo jedan povećavajući put
// u grafu razmjene. Kad put ne postoji, odgovor je K.
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> eu, ev, ew;
vector<char> inS;           // je li brid u trenutnom zajedničkom nezavisnom skupu S
vector<vector<pair<int,int>>> adj;   // šuma S: (susjed, indeks brida)
vector<int> par, parEdge, dep, comp;

// Ukorijeni šumu S: roditelji, dubine, komponente.
void izgradiSumu() {
    adj.assign(n + 1, {});
    for (int e = 0; e < m; ++e)
        if (inS[e]) { adj[eu[e]].push_back({ev[e], e}); adj[ev[e]].push_back({eu[e], e}); }
    par.assign(n + 1, 0); parEdge.assign(n + 1, -1); dep.assign(n + 1, 0); comp.assign(n + 1, -1);
    for (int r = 1; r <= n; ++r) {
        if (comp[r] != -1) continue;
        comp[r] = r; par[r] = 0;
        vector<int> st = {r};
        while (!st.empty()) {
            int v = st.back(); st.pop_back();
            for (auto [to, e] : adj[v]) if (comp[to] == -1) {
                comp[to] = r; par[to] = v; parEdge[to] = e; dep[to] = dep[v] + 1;
                st.push_back(to);
            }
        }
    }
}

// Bridovi šume S na putu između a i b (a i b u istoj komponenti).
vector<int> putUSumi(int a, int b) {
    vector<int> res;
    while (a != b) {
        if (dep[a] < dep[b]) swap(a, b);
        res.push_back(parEdge[a]); a = par[a];
    }
    return res;
}

// Pokušaj povećati S bridom težine K (klasa K je još prazna). Vraća uspjeh.
bool augment(int K, const vector<int>& predstavnik) {
    izgradiSumu();
    // Graf razmjene nad bridovima težine <= K.
    //   X1 = {x ∉ S : S + x je šuma}          (izvori)
    //   X2 = {x ∉ S : težina(x) = K}          (ponori; klasa K je slobodna)
    //   y -> x (y ∈ S, x ∉ S) ako je S - y + x šuma  (y leži na putu krajeva x u šumi)
    //   x -> y (x ∉ S, y ∈ S) ako S - y + x poštuje težine (y je brid iste težine kao x)
    vector<vector<int>> odY(m);   // y -> lista x
    vector<int> dist(m, -1), prevv(m, -1);
    deque<int> q;
    for (int x = 0; x < m; ++x) {
        if (inS[x] || ew[x] > K) continue;
        if (comp[eu[x]] != comp[ev[x]]) { dist[x] = 0; q.push_back(x); }
        else for (int y : putUSumi(eu[x], ev[x])) odY[y].push_back(x);
    }
    int kraj = -1;
    while (!q.empty()) {
        int v = q.front(); q.pop_front();
        if (!inS[v]) {
            if (ew[v] == K) { kraj = v; break; }
            int y = predstavnik[ew[v]];        // jedini brid težine ew[v] u S
            if (dist[y] == -1) { dist[y] = dist[v] + 1; prevv[y] = v; q.push_back(y); }
        } else {
            for (int x : odY[v]) if (dist[x] == -1) { dist[x] = dist[v] + 1; prevv[x] = v; q.push_back(x); }
        }
    }
    if (kraj == -1) return false;
    for (int v = kraj; v != -1; v = prevv[v]) inS[v] ^= 1;   // simetrična razlika duž najkraćeg puta
    return true;
}

int main() {
    scanf("%d %d", &n, &m);
    eu.resize(m); ev.resize(m); ew.resize(m);
    for (int i = 0; i < m; ++i) scanf("%d %d %d", &eu[i], &ev[i], &ew[i]);
    inS.assign(m, 0);
    vector<int> predstavnik(n + 2, -1);   // predstavnik[c] = brid težine c u S
    int K = 0;
    while (true) {
        bool ima = false;
        for (int e = 0; e < m; ++e) if (ew[e] == K) ima = true;
        if (!ima || !augment(K, predstavnik)) break;
        for (int e = 0; e < m; ++e) if (inS[e]) predstavnik[ew[e]] = e;
        ++K;
    }
    printf("%d\n", K);
    return 0;
}
