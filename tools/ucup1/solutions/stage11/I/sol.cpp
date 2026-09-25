// UCup 1, Stage 11 (EC-Final 2022), I. Chase Game
// Dok Pang miruje u k, šteta pri ulasku u v je d - dist(k, v) -> Dijkstra iz vrha 1.
// Ulazak u vrh s dist(k, v) >= d izaziva teleport (šteta d); nakon toga je optimalno
// ići najkraćim putem do n, a cijena ostatka ovisi samo o duljini L = dist(v, n):
//   g(L) = q * d(d+1)/2 + r*d - r(r+1)/2,  gdje je L = q*d + r, 0 <= r < d.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, m, k;
ll d;
vector<vector<int>> adj;

vector<int> bfs(int src) {
    vector<int> dist(n + 1, -1);
    queue<int> q;
    dist[src] = 0; q.push(src);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) if (dist[v] < 0) { dist[v] = dist[u] + 1; q.push(v); }
    }
    return dist;
}

// Cijena puta duljine L najkraćim putem nakon što je Pang teleportiran u početni vrh puta.
ll g(ll L) {
    ll q = L / d, r = L % d;
    return q * (d * (d + 1) / 2) + r * d - r * (r + 1) / 2;
}

int main() {
    scanf("%d %d %d %lld", &n, &m, &k, &d);
    adj.assign(n + 1, {});
    for (int i = 0; i < m; i++) {
        int a, b; scanf("%d %d", &a, &b);
        adj[a].push_back(b); adj[b].push_back(a);
    }
    vector<int> dk = bfs(k), dn = bfs(n);

    const ll INF = LLONG_MAX / 4;
    vector<ll> D(n + 1, INF);
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<>> pq;
    D[1] = 0; pq.push({0, 1});
    ll ans = INF;
    while (!pq.empty()) {
        auto [du, u] = pq.top(); pq.pop();
        if (du != D[u]) continue;
        if (u == n) { ans = min(ans, du); continue; }   // stigli bez teleporta
        for (int v : adj[u]) {
            if (dk[v] >= d) {
                // teleport u v: šteta d, zatim najkraći put do n
                ans = min(ans, du + d + g(dn[v]));
            } else {
                ll nd = du + (d - dk[v]);
                if (nd < D[v]) { D[v] = nd; pq.push({nd, v}); }
            }
        }
    }
    printf("%lld\n", ans);
    return 0;
}
