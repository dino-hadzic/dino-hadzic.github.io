// UCup 1, Stage 3 (AMPPZ 2022), H. Hyperloop
// 1) Dijkstra od vrha 1 -> DAG najkracih putova (brid (u,v,d) je u DAG-u ako dist[u]+d=dist[v]).
// 2) Usporedba silazno sortiranih nizova duljina (jednakog zbroja) = usporedba vektora brojaca
//    po tezinama od najvece tezine nadolje; multiskupovi se lijepo ponasaju na unije, pa vrijedi
//    DP: best[v] = max po DAG-bridovima (u,v) od best[u] + {d}.
// 3) Multiskupove cuvamo u perzistentnom segmentnom stablu po tezinama (1..50000) s 64-bitnim
//    hashevima; usporedba trazi najvecu tezinu na kojoj se brojaci razlikuju u O(log W).
//    Nove cvorove stvaramo samo za pobjednicki brid svakog vrha (n log W cvorova) zbog 64 MB.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

const int W = 50000;
struct Cvor { int l, r; ull h; };          // za list: l = brojac
static vector<Cvor> t;
static ull rnd[W + 1];

int umetni(int a, int nl, int nr, int w) {
    int c = t.size();
    t.push_back(t[a]);
    t[c].h += rnd[w];
    if (nl == nr) { t[c].l++; return c; }
    int mid = (nl + nr) / 2;
    if (w <= mid) { int x = umetni(t[a].l, nl, mid, w); t[c].l = x; }
    else { int x = umetni(t[a].r, mid + 1, nr, w); t[c].r = x; }
    return c;
}
int brojac(int a, int w) {
    int nl = 1, nr = W;
    while (nl < nr) {
        int mid = (nl + nr) / 2;
        if (w <= mid) { a = t[a].l; nr = mid; } else { a = t[a].r; nl = mid + 1; }
        if (a == 0) return 0;
    }
    return t[a].l;
}
// najveca tezina u [lo,hi] na kojoj se brojaci verzija a i b razlikuju; 0 ako je nema
int razlika(int a, int b, int nl, int nr, int lo, int hi) {
    if (hi < nl || nr < lo || a == b) return 0;
    if (t[a].h == t[b].h && lo <= nl && nr <= hi) return 0;
    if (nl == nr) return nl;
    int mid = (nl + nr) / 2;
    int r = razlika(t[a].r, t[b].r, mid + 1, nr, lo, hi);
    if (r) return r;
    return razlika(t[a].l, t[b].l, nl, mid, lo, hi);
}
int znak(int x) { return (x > 0) - (x < 0); }
// usporedi multiskup (a + {d1}) s (b + {d2}); >0 ako je prvi leksikografski veci
int usporedi(int a, int d1, int b, int d2) {
    if (d1 < d2) return -usporedi(b, d2, a, d1);
    if (d1 == d2) {
        int p = razlika(a, b, 1, W, 1, W);
        return p ? znak(brojac(a, p) - brojac(b, p)) : 0;
    }
    int p = razlika(a, b, 1, W, d1 + 1, W);
    if (p) return znak(brojac(a, p) - brojac(b, p));
    int s = znak(brojac(a, d1) + 1 - brojac(b, d1));
    if (s) return s;
    p = razlika(a, b, 1, W, d2 + 1, d1 - 1);
    if (p) return znak(brojac(a, p) - brojac(b, p));
    s = znak(brojac(a, d2) - brojac(b, d2) - 1);
    if (s) return s;
    p = razlika(a, b, 1, W, 1, d2 - 1);
    if (p) return znak(brojac(a, p) - brojac(b, p));
    return 0;
}

int main() {
    mt19937_64 gen(20230211);
    for (int i = 1; i <= W; ++i) rnd[i] = gen();
    t.reserve(100000 * 18 + 5);
    int z;
    scanf("%d", &z);
    while (z--) {
        int n, m;
        scanf("%d %d", &n, &m);
        vector<int> eu(m), ev(m), ed(m), deg(n + 2, 0);
        for (int i = 0; i < m; ++i) {
            scanf("%d %d %d", &eu[i], &ev[i], &ed[i]);
            ++deg[eu[i]]; ++deg[ev[i]];
        }
        vector<int> start(n + 2, 0);
        for (int v = 1; v <= n; ++v) start[v + 1] = start[v] + deg[v];
        vector<int> susjed(2 * m), tez(2 * m), pos(start.begin(), start.end());
        for (int i = 0; i < m; ++i) {
            susjed[pos[eu[i]]] = ev[i]; tez[pos[eu[i]]++] = ed[i];
            susjed[pos[ev[i]]] = eu[i]; tez[pos[ev[i]]++] = ed[i];
        }
        // Dijkstra
        const ll INF = LLONG_MAX / 4;
        vector<ll> dist(n + 1, INF);
        priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> pq;
        dist[1] = 0; pq.push({0, 1});
        while (!pq.empty()) {
            auto [d, v] = pq.top(); pq.pop();
            if (d != dist[v]) continue;
            for (int i = start[v]; i < start[v + 1]; ++i) {
                int w = susjed[i]; ll nd = d + tez[i];
                if (nd < dist[w]) { dist[w] = nd; pq.push({nd, w}); }
            }
        }
        // DP po rastucoj udaljenosti
        vector<int> red(n);
        iota(red.begin(), red.end(), 1);
        sort(red.begin(), red.end(), [&](int a, int b) { return dist[a] < dist[b]; });
        t.clear(); t.push_back({0, 0, 0});
        vector<int> ver(n + 1, 0), rod(n + 1, 0);
        for (int v : red) {
            if (v == 1 || dist[v] >= INF) continue;
            int bu = -1, bd = 0;
            for (int i = start[v]; i < start[v + 1]; ++i) {
                int u = susjed[i], d = tez[i];
                if (dist[u] + d != dist[v]) continue;
                if (bu == -1 || usporedi(ver[u], d, ver[bu], bd) > 0) { bu = u; bd = d; }
            }
            rod[v] = bu;
            ver[v] = umetni(ver[bu], 1, W, bd);
        }
        vector<int> put;
        for (int v = n; v != 0; v = rod[v]) put.push_back(v);
        reverse(put.begin(), put.end());
        printf("%d\n", (int)put.size());
        for (size_t i = 0; i < put.size(); ++i) printf("%d%c", put[i], i + 1 == put.size() ? '\n' : ' ');
    }
    return 0;
}
