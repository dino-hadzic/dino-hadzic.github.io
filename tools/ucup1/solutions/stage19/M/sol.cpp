// UCup 1, Stage 19 (NAC 2023), M. Who Watches the Watchmen?
// Tražena konfiguracija = pokrivanje ciklusima (duljine >= 2) u grafu vidljivosti:
// i -> j dopušteno ako na segmentu (i, j) nema drugog drona; cijena 0 ako i već gleda j
// (j je prvi dron na zraci i), inače 1 (okret). Premještanje (1000) > n okreta, pa se
// premješta samo kad pokrivanje ne postoji: n = 1 (nemoguće, -1) ili n neparan i svi
// dronovi kolinearni (graf vidljivosti je put). Inače: mađarski algoritam na bipartitnom
// grafu (lijevo "tko gleda", desno "koga gleda") s cijenama 0/1/INF, O(n^3).
// Kolinearan neparan slučaj: pomaknemo točno jedan dron M izvan pravca; preostalih n-1
// (paran broj) čini put Q_0..Q_{n-2}, M vidi sve. Ciklus s M = M + susjedni komad Q_i..Q_j
// (i paran, j neparan), ostatak upareni susjedi. Za M i njegova "gledača" W: 0 okreta ako se
// zraka W i zraka unazad od cilja M-a sijeku (3D presjek zraka, egzaktno u __int128),
// 1 ako je jedan od njihovih smjerova izvan pravca, 2 inače. Ukupno O(n^3 / 4).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef __int128 lll;
typedef array<ll, 3> V3;

int n;
vector<V3> P, D;

V3 oduzmi(const V3& a, const V3& b) { return {a[0] - b[0], a[1] - b[1], a[2] - b[2]}; }
V3 kriz(const V3& a, const V3& b) {
    return {a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]};
}
lll skal(const V3& a, const V3& b) { return (lll)a[0] * b[0] + (lll)a[1] * b[1] + (lll)a[2] * b[2]; }
bool nula(const V3& a) { return a[0] == 0 && a[1] == 0 && a[2] == 0; }
V3 smjer(V3 a) {  // normalizirani smjer (dijeljenje s gcd)
    ll g = __gcd(__gcd(llabs(a[0]), llabs(a[1])), llabs(a[2]));
    return {a[0] / g, a[1] / g, a[2] / g};
}

// Presjek zraka A + t*u (t > 0) i B + s*w (s > 0); pravci ne smiju biti isti.
bool sijekuSe(const V3& A, const V3& u, const V3& B, const V3& w) {
    V3 nrm = kriz(u, w);
    if (nula(nrm)) return false;                 // paralelni pravci (isti pravac = nevaljan)
    V3 Dd = oduzmi(B, A);
    if (skal(Dd, nrm) != 0) return false;         // nisu komplanarni
    lll t = skal(kriz(Dd, w), nrm);               // t * |nrm|^2
    lll s = skal(kriz(Dd, u), nrm);               // s * |nrm|^2
    return t > 0 && s > 0;
}

// Mađarski algoritam (minimalno uparivanje), cijene 0/1/INF.
ll madjarski(const vector<vector<ll>>& a) {
    const ll INF = (ll)4e18;
    int m = a.size();
    vector<ll> u(m + 1), v(m + 1), minv(m + 1);
    vector<int> p(m + 1), way(m + 1);
    for (int i = 1; i <= m; ++i) {
        p[0] = i;
        int j0 = 0;
        fill(minv.begin(), minv.end(), INF);
        vector<char> used(m + 1, 0);
        do {
            used[j0] = 1;
            int i0 = p[j0], j1 = 0;
            ll delta = INF;
            for (int j = 1; j <= m; ++j)
                if (!used[j]) {
                    ll cur = a[i0 - 1][j - 1] - u[i0] - v[j];
                    if (cur < minv[j]) { minv[j] = cur; way[j] = j0; }
                    if (minv[j] < delta) { delta = minv[j]; j1 = j; }
                }
            for (int j = 0; j <= m; ++j) {
                if (used[j]) { u[p[j]] += delta; v[j] -= delta; }
                else minv[j] -= delta;
            }
            j0 = j1;
        } while (p[j0] != 0);
        do { int j1 = way[j0]; p[j0] = p[j1]; j0 = j1; } while (j0);
    }
    ll ukupno = 0;
    for (int j = 1; j <= m; ++j) ukupno += a[p[j] - 1][j - 1];
    return ukupno;
}

int main() {
    if (scanf("%d", &n) != 1) return 0;
    P.resize(n); D.resize(n);
    for (int i = 0; i < n; ++i)
        if (scanf("%lld %lld %lld %lld %lld %lld", &P[i][0], &P[i][1], &P[i][2], &D[i][0], &D[i][1], &D[i][2]) != 6) return 0;
    if (n == 1) { puts("-1"); return 0; }

    bool kolinearni = true;
    V3 u = oduzmi(P[1], P[0]);
    for (int i = 2; i < n; ++i) if (!nula(kriz(oduzmi(P[i], P[0]), u))) kolinearni = false;

    if (!(kolinearni && n % 2 == 1)) {
        const ll INF = 1000000;
        // vidljivost: j je vidljiv iz i ako je najbliži među točkama u istom smjeru
        vector<vector<ll>> cijena(n, vector<ll>(n, INF));
        for (int i = 0; i < n; ++i) {
            map<V3, pair<ll, int>> najblizi;   // smjer -> (udaljenost^2, indeks)
            for (int j = 0; j < n; ++j) if (j != i) {
                V3 d = oduzmi(P[j], P[i]);
                ll dd = (ll)skal(d, d);
                V3 k = smjer(d);
                auto it = najblizi.find(k);
                if (it == najblizi.end() || dd < it->second.first) najblizi[k] = {dd, j};
            }
            for (auto& [k, par] : najblizi) cijena[i][par.second] = 1;
            auto it = najblizi.find(smjer(D[i]));
            if (it != najblizi.end()) cijena[i][it->second.second] = 0;   // već ga gleda
        }
        ll r = madjarski(cijena);
        printf("%lld\n", r >= INF ? -1LL : r);
        return 0;
    }

    // kolinearni, n neparan (n >= 3): pomicanje točno jednog drona
    V3 us = smjer(u);
    vector<int> red(n);
    iota(red.begin(), red.end(), 0);
    vector<ll> par(n);
    for (int i = 0; i < n; ++i) par[i] = (ll)skal(oduzmi(P[i], P[0]), us);
    sort(red.begin(), red.end(), [&](int a, int b) { return par[a] < par[b]; });
    // znak smjera duž pravca: +1 / -1 / 0 (nije paralelan)
    vector<int> znak(n, 0);
    for (int i = 0; i < n; ++i)
        if (nula(kriz(D[i], us))) znak[i] = skal(D[i], us) > 0 ? 1 : -1;

    ll najbolje = LLONG_MAX;
    for (int mi = 0; mi < n; ++mi) {
        int m = red[mi];
        vector<int> Q;
        for (int i = 0; i < n; ++i) if (i != mi) Q.push_back(red[i]);
        int k = Q.size();   // paran
        vector<ll> fwd(k, 0), bwd(k, 0);
        for (int a = 0; a < k; ++a) { fwd[a] = znak[Q[a]] != 1; bwd[a] = znak[Q[a]] != -1; }
        vector<ll> parC(k, 0);
        for (int a = 0; a + 1 < k; ++a) parC[a] = fwd[a] + bwd[a + 1];
        // L[i] = cijena uparivanja Q_0..Q_{i-1} (i paran); R[j] = cijena za Q_{j+1}..Q_{k-1} (j neparan)
        vector<ll> L(k + 1, 0), R(k + 1, 0);
        for (int i = 2; i <= k; i += 2) L[i] = L[i - 2] + parC[i - 2];
        R[k - 1] = 0;
        for (int j = k - 3; j >= 1; j -= 2) R[j] = R[j + 2] + parC[j + 1];
        vector<ll> pf(k + 1, 0), pb(k + 1, 0);
        for (int a = 0; a < k; ++a) { pf[a + 1] = pf[a] + fwd[a]; pb[a + 1] = pb[a] + bwd[a]; }
        bool canM = znak[m] == 0;
        V3 negD = {-D[m][0], -D[m][1], -D[m][2]};
        auto extra = [&](int T, int W) -> ll {
            bool canW = znak[W] == 0;
            if (canM && canW && sijekuSe(P[T], negD, P[W], D[W])) return 0;
            return (canM || canW) ? 1 : 2;
        };
        for (int i = 0; i < k; i += 2)
            for (int j = i + 1; j < k; j += 2) {
                ll c1 = pf[j] - pf[i] + extra(Q[i], Q[j]);          // M -> Q_i -> ... -> Q_j -> M
                ll c2 = pb[j + 1] - pb[i + 1] + extra(Q[j], Q[i]);  // M -> Q_j -> ... -> Q_i -> M
                najbolje = min(najbolje, 1000 + L[i] + R[j] + min(c1, c2));
            }
    }
    printf("%lld\n", najbolje);
    return 0;
}
