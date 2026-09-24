// UCup 1, Stage 11 (EC-Final 2022), G. Rectangle
// Tri pravca: (3 iste orijentacije) + (2 okomita + 1 vodoravni) + simetrično sa zamjenom koordinata.
//  * 3 pravca iste orijentacije: 1D problem nad intervalima [l_i, r_i]. Enumeriramo srednji pravac b:
//    lijevi mora ležati u presjeku svih intervala s r_i < b, desni u presjeku svih s l_i > b.
//    Skupovi se mijenjaju samo u O(n) točkama, između njih je broj načina umnožak dviju afinih funkcija.
//  * 2 okomita (L < R) + 1 vodoravni h: sweep po h; pravokutnici koje h dodiruje "nestaju". Za preostale
//    intervale: L <= min r_i, R >= M = max l_i, a za fiksno L vrijedi R <= g(L) = min{ r_i : l_i > L }.
//    Broj načina = sum_L max(0, g(L) - M + 1) po L <= min(min r, M - 1)  (+ sum_{L=M}^{min r} (10^9 - L)).
//    g je sufiksni minimum po intervalima sortiranima po l; zbroj "duljina x sufiksni minimum" uz
//    umetanje/brisanje održava segmentno stablo tehnikom „rekonstrukcije zgrada” (O(log^2 n) po operaciji).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef __int128 lll;

const ll MOD = 998244353;
const ll C = 1000000000LL;   // koordinate pravaca su u [1, C]
const ll INF = 4e9;

ll md(lll x) { x %= MOD; if (x < 0) x += MOD; return (ll)x; }

// sum_{b=s}^{e} 1, b, b^2  (točno, pa mod)
ll S0(ll s, ll e) { return e < s ? 0 : md(e - s + 1); }
ll S1(ll s, ll e) { if (e < s) return 0; return md((lll)(s + e) * (e - s + 1) / 2); }
ll S2(ll s, ll e) {
    if (e < s) return 0;
    auto f = [](lll n) { return n * (n + 1) * (2 * n + 1) / 6; };   // sum_{b=1}^{n} b^2
    return md(f(e) - f(s - 1));
}
// sum_{b=s}^{e} (p0 + p1 b)(q0 + q1 b)
ll sumProd(ll s, ll e, ll p0, ll p1, ll q0, ll q1) {
    ll res = md((lll)md(p0) * md(q0) % MOD * S0(s, e));
    res = (res + md((lll)md(p0 * q1 + p1 * q0) * S1(s, e))) % MOD;
    res = (res + md((lll)md(p1 * q1) * S2(s, e))) % MOD;
    return res;
}

// ---------- tri pravca iste orijentacije ----------
ll threeSame(vector<pair<ll, ll>> iv) {
    int n = iv.size();
    vector<int> byR(n), byL(n);
    iota(byR.begin(), byR.end(), 0); iota(byL.begin(), byL.end(), 0);
    sort(byR.begin(), byR.end(), [&](int a, int b) { return iv[a].second < iv[b].second; });
    sort(byL.begin(), byL.end(), [&](int a, int b) { return iv[a].first < iv[b].first; });
    vector<ll> sufMinR(n + 1, INF);           // min r među intervalima byL[p..n-1]
    for (int p = n - 1; p >= 0; p--) sufMinR[p] = min(sufMinR[p + 1], iv[byL[p]].second);
    ll maxL = iv[byL[n - 1]].first;

    // događaji: b = r_i + 1 (i ulazi u lijevi skup), b = l_i (i izlazi iz desnog skupa)
    vector<ll> ev;
    for (auto& [l, r] : iv) { ev.push_back(r + 1); ev.push_back(l); }
    sort(ev.begin(), ev.end()); ev.erase(unique(ev.begin(), ev.end()), ev.end());

    ll ans = 0, start = 1;
    int pr = 0, pl = 0;                        // byR[0..pr-1] su lijevo (r < b), byL[pl..] su desno (l > b)
    ll lmaxL = 0, lminR = INF;                 // presjek lijevih intervala
    auto segment = [&](ll s, ll e) {           // b iz [s, e], skupovi konstantni
        if (s > e) return;
        ll p0, p1, q0, q1;
        if (pr == 0) { p0 = -1; p1 = 1; }                                  // a iz [1, b-1]
        else { p0 = max(0LL, lminR - lmaxL + 1); p1 = 0; }
        if (pl == n) { q0 = C; q1 = -1; }                                  // c iz [b+1, C]
        else { q0 = max(0LL, sufMinR[pl] - maxL + 1); q1 = 0; }
        ans = (ans + sumProd(s, e, p0, p1, q0, q1)) % MOD;
    };
    for (ll e : ev) {
        if (e > C) break;
        segment(start, e - 1);
        while (pr < n && iv[byR[pr]].second + 1 <= e) { lmaxL = max(lmaxL, iv[byR[pr]].first); lminR = min(lminR, iv[byR[pr]].second); pr++; }
        while (pl < n && iv[byL[pl]].first <= e) pl++;
        start = e;
    }
    segment(start, C);
    return ans;
}

// ---------- segmentno stablo: sum len_j * min(w[j..]) uz umetanje/brisanje ----------
struct SegTree {
    int n, sz;
    vector<ll> mn, sm, lenSum, len;
    void init(const vector<ll>& L) {
        n = L.size(); sz = 1; while (sz < n) sz <<= 1;
        mn.assign(2 * sz, INF); sm.assign(2 * sz, 0); lenSum.assign(2 * sz, 0); len = L;
        for (int i = 0; i < n; i++) lenSum[sz + i] = len[i] % MOD;
        for (int i = sz - 1; i >= 1; i--) lenSum[i] = (lenSum[2 * i] + lenSum[2 * i + 1]) % MOD;
        for (int i = 0; i < n; i++) sm[sz + i] = md((lll)len[i] * INF);
        for (int i = sz - 1; i >= 1; i--) pull(i);
    }
    // zbroj len_j * min(sufiksni minimum unutar čvora od j, bound) po svim j u čvoru
    ll calc(int node, ll bound) {
        if (mn[node] >= bound) return md((lll)lenSum[node] * (bound % MOD));
        if (node >= sz) return sm[node];
        int rc = 2 * node + 1, lc = 2 * node;
        if (mn[rc] <= bound) return (md(sm[node] - sm[rc]) + calc(rc, bound)) % MOD;
        return (calc(lc, bound) + md((lll)lenSum[rc] * (bound % MOD))) % MOD;
    }
    void pull(int node) {
        int lc = 2 * node, rc = 2 * node + 1;
        mn[node] = min(mn[lc], mn[rc]);
        sm[node] = (sm[rc] + calc(lc, mn[rc])) % MOD;
    }
    void set(int pos, ll v) {
        int i = sz + pos; mn[i] = v; sm[i] = md((lll)len[pos] * (v % MOD));
        for (i >>= 1; i >= 1; i >>= 1) pull(i);
    }
    ll rangeMin(int node, int nl, int nr, int a, int b) {
        if (b < nl || nr < a) return INF;
        if (a <= nl && nr <= b) return mn[node];
        int mid = (nl + nr) / 2;
        return min(rangeMin(2 * node, nl, mid, a, b), rangeMin(2 * node + 1, mid + 1, nr, a, b));
    }
    ll rangeMin(int a, int b) { return a > b ? INF : rangeMin(1, 0, sz - 1, a, b); }
    // zbroj len_j * min(w[j..n-1]) za j u [a, b]; bound = min w desno od trenutnog čvora
    ll query(int node, int nl, int nr, int a, int b, ll& bound) {
        if (b < nl || nr < a) return 0;
        if (a <= nl && nr <= b) { ll res = calc(node, bound); bound = min(bound, mn[node]); return res; }
        int mid = (nl + nr) / 2;
        ll res = query(2 * node + 1, mid + 1, nr, a, b, bound);
        res = (res + query(2 * node, nl, mid, a, b, bound)) % MOD;
        return res;
    }
    ll query(int a, int b) {
        if (a > b) return 0;
        ll bound = rangeMin(b + 1, n - 1);
        return query(1, 0, sz - 1, a, b, bound);
    }
    // najdesnija pozicija s w < v, ili -1
    int rightmostLess(int node, int nl, int nr, ll v) {
        if (mn[node] >= v) return -1;
        if (nl == nr) return nl;
        int mid = (nl + nr) / 2;
        int res = rightmostLess(2 * node + 1, mid + 1, nr, v);
        if (res < 0) res = rightmostLess(2 * node, nl, mid, v);
        return res;
    }
};

// ---------- 2 pravca u smjeru "iv" (intervali) + 1 pravac okomit na njih (intervali "sweep") ----------
ll twoPlusOne(const vector<pair<ll, ll>>& iv, const vector<pair<ll, ll>>& sw) {
    int n = iv.size();
    vector<int> ord(n); iota(ord.begin(), ord.end(), 0);
    sort(ord.begin(), ord.end(), [&](int a, int b) { return iv[a].first < iv[b].first; });
    vector<int> pos(n);                        // pos[i] = pozicija intervala i (1..n) u poretku po l
    vector<ll> L(n + 2), R(n + 2);             // L[0] = 1 (virtualno)
    L[0] = 1;
    for (int p = 0; p < n; p++) { pos[ord[p]] = p + 1; L[p + 1] = iv[ord[p]].first; R[p + 1] = iv[ord[p]].second; }
    // komad j (0..n-1): L iz [L[j], L[j+1]-1], duljina L[j+1]-L[j]; w[j] = R[j+1] ako je prisutan
    vector<ll> len(n);
    for (int j = 0; j < n; j++) len[j] = L[j + 1] - L[j];
    SegTree st; st.init(len);
    set<int> present;                          // prisutne pozicije (1..n)
    multiset<ll> minR;
    for (int p = 1; p <= n; p++) { st.set(p - 1, R[p]); present.insert(p); minR.insert(R[p]); }

    const ll pairsAll = md((lll)C * (C - 1) / 2);
    auto countPairs = [&]() -> ll {
        if (present.empty()) return pairsAll;
        int jmax = *present.rbegin();
        ll M = L[jmax], mr = *minR.begin();
        int j0 = st.rightmostLess(1, 0, st.sz - 1, M) + 1;         // od ovdje je sufiksni minimum >= M
        ll res = 0;
        if (mr >= M) {
            // svi komadi j0..jmax-1 cijeli, plus L iz [M, mr] s R iz (L, C]
            if (j0 <= jmax - 1) {
                ll s = st.query(j0, jmax - 1);
                ll lens = md(L[jmax] - L[j0]);
                res = md(s - (lll)md(M - 1) * lens);
            }
            res = (res + sumProd(M, mr, C, -1, 1, 0)) % MOD;
        } else {
            // komad c sadrži mr: cijeli komadi j0..c-1, komad c skraćen na [L[c], mr]
            int c = int(upper_bound(L.begin() + 1, L.begin() + n + 1, mr) - L.begin()) - 1;   // najveći j s L[j] <= mr
            if (j0 <= c - 1) {
                ll s = st.query(j0, c - 1);
                ll lens = md(L[c] - L[j0]);
                res = md(s - (lll)md(M - 1) * lens);
            }
            if (j0 <= c) {
                ll g = st.rangeMin(c, n - 1);
                if (g >= M) res = (res + md((lll)md(mr - L[c] + 1) * md(g - M + 1))) % MOD;
            }
        }
        return res;
    };

    // sweep: pravokutnik i nestaje za h u [sw_i.l, sw_i.r]
    vector<pair<ll, int>> ev;                  // (h, +i) = umetni, (h, -(i+1)) = izbriši
    for (int i = 0; i < n; i++) { ev.push_back({sw[i].first, -(i + 1)}); ev.push_back({sw[i].second + 1, i + 1}); }
    sort(ev.begin(), ev.end());
    ll ans = 0, start = 1;
    size_t k = 0;
    while (k < ev.size()) {
        ll h = ev[k].first;
        if (h > C) break;
        if (start <= h - 1) ans = (ans + md((lll)(h - start) * countPairs())) % MOD;
        while (k < ev.size() && ev[k].first == h) {
            int e = ev[k].second; k++;
            if (e < 0) { int i = -e - 1, p = pos[i]; present.erase(p); minR.erase(minR.find(R[p])); st.set(p - 1, INF); }
            else { int i = e - 1, p = pos[i]; present.insert(p); minR.insert(R[p]); st.set(p - 1, R[p]); }
        }
        start = h;
    }
    if (start <= C) ans = (ans + md((lll)(C - start + 1) * countPairs())) % MOD;
    return ans;
}

int main() {
    int T;
    if (scanf("%d", &T) != 1) return 0;
    while (T--) {
        int n; scanf("%d", &n);
        vector<pair<ll, ll>> X(n), Y(n);
        for (int i = 0; i < n; i++) { ll a, b, c, d; scanf("%lld %lld %lld %lld", &a, &b, &c, &d); X[i] = {a, c}; Y[i] = {b, d}; }
        ll ans = (threeSame(X) + threeSame(Y)) % MOD;
        ans = (ans + twoPlusOne(X, Y)) % MOD;   // 2 okomita (x = a) + 1 vodoravni (sweep po y)
        ans = (ans + twoPlusOne(Y, X)) % MOD;   // 2 vodoravna + 1 okomiti
        printf("%lld\n", ans);
    }
    return 0;
}
