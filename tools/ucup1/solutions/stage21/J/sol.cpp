// J. Triangle City – najkraći put + Eulerova staza, O(E log V)
// Svi vrhovi imaju paran stupanj. Staza od (1,1) do (n,n) ostavlja neiskorišten skup bridova
// u kojem su (1,1) i (n,n) neparni, a ostali parni – taj skup sadrži put (1,1)->(n,n), pa je
// neiskorištena duljina >= d = najkraći put. Obrnuto: uklonimo bridove najkraćeg puta; zbog
// nejednakosti trokuta put koristi najviše jedan brid svakog trokuta, pa ostatak ostaje povezan
// i ima Eulerovu stazu (1,1)->(n,n) duljine (ukupno - d), što je optimum.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int T; scanf("%d", &T);
    while (T--) {
        int n; scanf("%d", &n);
        auto id = [&](int i, int j) { return i * (i - 1) / 2 + (j - 1); };  // 0-based id čvora (i,j)
        int V = n * (n + 1) / 2;
        vector<int> eu, ev; vector<ll> ew;
        auto addEdge = [&](int a, int b, ll w) { eu.push_back(a); ev.push_back(b); ew.push_back(w); };
        for (int i = 1; i < n; i++) for (int j = 1; j <= i; j++) { ll w; scanf("%lld", &w); addEdge(id(i, j), id(i + 1, j), w); }
        for (int i = 1; i < n; i++) for (int j = 1; j <= i; j++) { ll w; scanf("%lld", &w); addEdge(id(i, j), id(i + 1, j + 1), w); }
        for (int i = 1; i < n; i++) for (int j = 1; j <= i; j++) { ll w; scanf("%lld", &w); addEdge(id(i + 1, j), id(i + 1, j + 1), w); }
        int E = eu.size();
        vector<vector<int>> adj(V);
        ll total = 0;
        for (int e = 0; e < E; e++) { adj[eu[e]].push_back(e); adj[ev[e]].push_back(e); total += ew[e]; }
        // Dijkstra od (1,1)
        int s = id(1, 1), t = id(n, n);
        vector<ll> dist(V, LLONG_MAX); vector<int> pe(V, -1);
        priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<>> pq;
        dist[s] = 0; pq.push({0, s});
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d != dist[u]) continue;
            for (int e : adj[u]) {
                int w = eu[e] ^ ev[e] ^ u;
                if (d + ew[e] < dist[w]) { dist[w] = d + ew[e]; pe[w] = e; pq.push({dist[w], w}); }
            }
        }
        vector<char> used(E, 0);
        for (int u = t; u != s; ) { int e = pe[u]; used[e] = 1; u = eu[e] ^ ev[e] ^ u; }
        // Hierholzer od s (iterativno)
        vector<int> ptr(V, 0), path;
        vector<int> st = {s};
        while (!st.empty()) {
            int u = st.back();
            while (ptr[u] < (int)adj[u].size() && used[adj[u][ptr[u]]]) ptr[u]++;
            if (ptr[u] == (int)adj[u].size()) { path.push_back(u); st.pop_back(); }
            else { int e = adj[u][ptr[u]]; used[e] = 1; st.push_back(eu[e] ^ ev[e] ^ u); }
        }
        reverse(path.begin(), path.end());
        printf("%lld\n%d\n", total - dist[t], (int)path.size());
        string out;
        for (int k = 0; k < (int)path.size(); k++) {
            // iz id-a natrag u (i,j)
            int i = (int)((sqrt(8.0L * path[k] + 1) - 1) / 2) + 1;
            while (i * (i - 1) / 2 > path[k]) i--;
            while ((i + 1) * i / 2 <= path[k]) i++;
            int j = path[k] - i * (i - 1) / 2 + 1;
            if (k) out += ' ';
            out += to_string(i) + ' ' + to_string(j);
        }
        puts(out.c_str());
    }
    return 0;
}
