// A. LaLa and Magic Circle (LiLi Version) - output-only
// Konstrukcija (Biedl, "Polygons Needing Many Flipturns"), N djeljiv s 4:
//   grupa 1: d_i = (i+1, (i+1)^2)         za 0 <= i <= N/2-2   (konveksni lanac)
//   grupa 2: d_i = (1, 0)                 za neparne i u [N/2-1, N-2]
//   grupa 3: d_i = (N/2, (N/2)^2)         za parne   i u [N/2-1, N-2]
//   zadnji brid zatvara poligon.
// Flipturn "džepa" od dva brida samo ZAMIJENI ta dva brida, pa svaki brid (1,0)
// polako "klizi" kroz cijeli lanac; strategija "uvijek prvi džep u poretku
// indeksa" daje točno N^2/8 - 1 = 124 999 koraka za N = 1000.
// Program SIMULIRA postupak (ljuska raste, stari vrhovi ljuske se ne miču),
// pa je svaki ispisani korak stvarno valjan.
// Za potrebe testiranja, ako na ulazu postoji broj, koristi se kao N.
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
struct P { ll x, y; };
ll cross(const P& o, const P& a, const P& b) { return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x); }
bool onSegment(const P& a, const P& b, const P& q) {
    return cross(a, b, q) == 0 && min(a.x, b.x) <= q.x && q.x <= max(a.x, b.x)
        && min(a.y, b.y) <= q.y && q.y <= max(a.y, b.y);
}

int main() {
    int N = 1000;
    { int t; if (scanf("%d", &t) == 1) N = t; }
    const ll OFF = 200000000;                       // pomak da sve koordinate ostanu u [0, 1e9]

    vector<P> d;
    for (int i = 0; i <= N / 2 - 2; i++) d.push_back({i + 1, (ll)(i + 1) * (i + 1)});
    for (int i = N / 2 - 1; i <= N - 2; i++)
        d.push_back(i % 2 == 1 ? P{1, 0} : P{N / 2, (ll)(N / 2) * (N / 2)});
    vector<P> p(N);
    p[0] = {OFF, OFF};
    for (int i = 1; i < N; i++) p[i] = {p[i - 1].x + d[i - 1].x, p[i - 1].y + d[i - 1].y};
    vector<P> init = p;

    // početna konveksna ljuska (monotoni lanac), CCW
    vector<P> h;
    {
        vector<P> pts = p;
        sort(pts.begin(), pts.end(), [](const P& a, const P& b) { return a.x != b.x ? a.x < b.x : a.y < b.y; });
        for (int pass = 0; pass < 2; pass++) {
            size_t start = h.size();
            for (auto& q : pts) {
                while (h.size() >= start + 2 && cross(h[h.size() - 2], h.back(), q) <= 0) h.pop_back();
                h.push_back(q);
            }
            h.pop_back();
            reverse(pts.begin(), pts.end());
        }
    }
    auto onHullFull = [&](const P& q) {
        for (size_t i = 0; i < h.size(); i++) if (onSegment(h[i], h[(i + 1) % h.size()], q)) return true;
        return false;
    };
    vector<char> on(N);
    for (int i = 0; i < N; i++) on[i] = onHullFull(p[i]);

    // umetanje nove točke q u ljusku (ljuska samo raste) + ažuriranje oznaka "na rubu"
    auto insertPoint = [&](int idx) {
        const P q = p[idx];
        int H = h.size();
        vector<ll> cr(H);
        int vis = 0;
        bool onEdge = false;
        for (int i = 0; i < H; i++) { cr[i] = cross(h[i], h[(i + 1) % H], q); if (cr[i] < 0) vis++; if (cr[i] == 0) onEdge = true; }
        if (vis == 0) { on[idx] = onEdge; return; }  // q unutar ljuske ili na njezinu rubu
        // vidljivi bridovi čine ciklički interval [i, j]
        int i = 0;
        while (!(cr[i] < 0 && cr[(i - 1 + H) % H] >= 0)) i++;
        int j = i;
        while (cr[(j + 1) % H] < 0) j = (j + 1) % H;
        // uklonjeni bridovi (h_k, h_{k+1}) za k u [i, j]; novi bridovi (h_i, q), (q, h_{j+1})
        vector<P> removedA, removedB;
        for (int k = i;; k = (k + 1) % H) {
            removedA.push_back(h[k]); removedB.push_back(h[(k + 1) % H]);
            if (k == j) break;
        }
        P hi = h[i], hj = h[(j + 1) % H];
        for (int t = 0; t < N; t++) {
            if (on[t]) {
                for (size_t k = 0; k < removedA.size() && on[t]; k++)
                    if (onSegment(removedA[k], removedB[k], p[t])) on[t] = 0;
            }
            if (!on[t] && (onSegment(hi, q, p[t]) || onSegment(q, hj, p[t]))) on[t] = 1;
        }
        // nova ljuska: h_0..h_i, q, h_{j+1}..
        vector<P> nh;
        for (int k = (j + 1) % H;; k = (k + 1) % H) { nh.push_back(h[k]); if (k == i) break; }
        nh.push_back(q);
        h = nh;
    };

    vector<array<ll, 4>> moves;
    while (true) {
        int u = -1, len = 0;
        for (int i = 0; i < N && u < 0; i++) {
            if (!on[i] || on[(i + 1) % N]) continue;
            int j = (i + 1) % N, l = 1;
            while (!on[j]) { j = (j + 1) % N; l++; }
            u = i; len = l;
        }
        if (u < 0) break;                           // svi vrhovi na ljusci: poligon je konveksan
        int v = (u + len) % N;
        moves.push_back({p[u].x, p[u].y, p[v].x, p[v].y});
        P s = {p[u].x + p[v].x, p[u].y + p[v].y};
        vector<P> mid(len - 1);
        for (int k = 1; k < len; k++) mid[k - 1] = p[(u + k) % N];
        for (int k = 1; k < len; k++) {
            P w = mid[len - 1 - k];                 // obrnuti redoslijed + točkasta refleksija
            p[(u + k) % N] = {s.x - w.x, s.y - w.y};
        }
        for (int k = 1; k < len; k++) insertPoint((u + k) % N);
    }

    string out;
    out.reserve(moves.size() * 40 + N * 24);
    char buf[64];
    out += to_string(N); out += '\n';
    for (int i = 0; i < N; i++) { int l = snprintf(buf, sizeof buf, "%lld %lld\n", init[i].x, init[i].y); out.append(buf, l); }
    out += to_string(moves.size()); out += '\n';
    for (auto& m : moves) { int l = snprintf(buf, sizeof buf, "%lld %lld %lld %lld\n", m[0], m[1], m[2], m[3]); out.append(buf, l); }
    fwrite(out.data(), 1, out.size(), stdout);
    return 0;
}
