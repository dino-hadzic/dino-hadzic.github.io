#include <bits/stdc++.h>
using namespace std;
using u64 = unsigned long long;
using ll = long long;

// Segmentno stablo: range add, broj pozicija s pokrivenoscu > 0.
struct Seg {
    int n; vector<int> mn, cnt, lazy;
    Seg(int n) : n(n), mn(4 * n, 0), cnt(4 * n, 0), lazy(4 * n, 0) { build(1, 0, n - 1); }
    void build(int v, int l, int r) {
        if (l == r) { cnt[v] = 1; return; }
        int m = (l + r) / 2; build(2 * v, l, m); build(2 * v + 1, m + 1, r);
        cnt[v] = cnt[2 * v] + cnt[2 * v + 1];
    }
    void apply(int v, int x) { mn[v] += x; lazy[v] += x; }
    void push(int v) {
        if (lazy[v]) { apply(2 * v, lazy[v]); apply(2 * v + 1, lazy[v]); lazy[v] = 0; }
    }
    void pull(int v) {
        mn[v] = min(mn[2 * v], mn[2 * v + 1]);
        cnt[v] = (mn[2 * v] == mn[v] ? cnt[2 * v] : 0) + (mn[2 * v + 1] == mn[v] ? cnt[2 * v + 1] : 0);
    }
    void add(int v, int l, int r, int ql, int qr, int x) {
        if (qr < l || r < ql) return;
        if (ql <= l && r <= qr) { apply(v, x); return; }
        push(v); int m = (l + r) / 2;
        add(2 * v, l, m, ql, qr, x); add(2 * v + 1, m + 1, r, ql, qr, x);
        pull(v);
    }
    void add(int l, int r, int x) { add(1, 0, n - 1, l, r, x); }
    int pokriveno() { return n - (mn[1] == 0 ? cnt[1] : 0); }
};

int main() {
    int n, S;
    if (scanf("%d %d", &n, &S) != 2) return 0;
    int z = 0, o = 0;
    vector<int> b;   // b_i = a_i - 1 za a_i >= 2
    for (int i = 0; i < n; ++i) {
        int x; if (scanf("%d", &x) != 1) return 0;
        if (x == 0) ++z; else if (x == 1) ++o; else b.push_back(x - 1);
    }
    int r = b.size();
    ll B = 0; for (int x : b) B += x;
    int theta = (r + 1) / 2;   // dovoljno pratiti brojeve elemenata c <= ceil(r/2)
    int W = theta / 64 + 1;    // rijeci po retku
    // T[d] = bitmaska po c: postoji podskup velikih elemenata s sum b = d i |podskup| = c (c <= theta)
    vector<u64> T((size_t)(B + 1) * W, 0);
    T[0] = 1;
    u64 maskZadnja = (theta % 64 == 63) ? ~0ULL : ((1ULL << (theta % 64 + 1)) - 1);
    sort(b.begin(), b.end());
    // ograniceni ruksak: binarno cijepanje brojnosti svake vrijednosti
    for (int i = 0; i < r;) {
        int j = i; while (j < r && b[j] == b[i]) ++j;
        int m = j - i, v = b[i];
        for (int t = 1; m > 0; t <<= 1) {
            int k = min(t, m); m -= k;               // komad od k kopija: sum b = k*v, broj = k
            if (k > theta) continue;                 // vise od theta elemenata nikad ne pratimo
            ll pomak = (ll)k * v;
            int ws = k / 64, bs = k % 64;
            for (ll d = B; d >= pomak; --d) {
                u64 *dst = &T[(size_t)d * W];
                const u64 *src = &T[(size_t)(d - pomak) * W];
                for (int w = W - 1; w >= ws; --w) {
                    u64 val = src[w - ws] << bs;
                    if (bs && w - ws - 1 >= 0) val |= src[w - ws - 1] >> (64 - bs);
                    dst[w] |= val;
                }
                dst[W - 1] &= maskZadnja;
            }
        }
        i = j;
    }
    // upiti po stupcu d: prvi/zadnji postavljeni bit, prvi >= alpha, zadnji <= alpha-1
    auto prvi = [&](ll d, int od) -> int {   // najmanji c >= od u T[d], ili -1
        if (od > theta) return -1;
        if (od < 0) od = 0;
        const u64 *row = &T[(size_t)d * W];
        int w = od / 64;
        u64 x = row[w] & (~0ULL << (od % 64));
        while (true) {
            if (x) return w * 64 + __builtin_ctzll(x);
            if (++w >= W) return -1;
            x = row[w];
        }
    };
    auto zadnji = [&](ll d, int doo) -> int {  // najveci c <= doo u T[d], ili -1
        if (doo < 0) return -1;
        if (doo > theta) doo = theta;
        const u64 *row = &T[(size_t)d * W];
        int w = doo / 64;
        u64 x = row[w] & (doo % 64 == 63 ? ~0ULL : ((1ULL << (doo % 64 + 1)) - 1));
        while (true) {
            if (x) return w * 64 + 63 - __builtin_clzll(x);
            if (--w < 0) return -1;
            x = row[w];
        }
    };
    const int INF = INT_MAX;
    // intervali po T (zbroj), aktivni za D = T - k u [d - z, d]; pomak D' = D + z
    // dogadaji: dodaj pri D' = d + z, ukloni nakon D' = d
    vector<vector<pair<int,int>>> dodaj(B + z + 2), ukloni(B + z + 2);
    int alpha = r - o;   // c >= alpha  <=>  r - c <= o
    for (ll d = 0; d <= B; ++d) {
        ll dk = B - d;   // komplementarni zbroj
        int cminD = prvi(d, 0), cmaxD = zadnji(d, theta);
        int cminK = prvi(dk, 0), cmaxK = zadnji(dk, theta);   // brojevi komplementa
        if (cminD < 0 && cminK < 0) continue;
        int cmin = INF, cmax = -1;
        if (cminD >= 0) { cmin = min(cmin, cminD); cmax = max(cmax, cmaxD); }
        if (cminK >= 0) { cmin = min(cmin, r - cmaxK); cmax = max(cmax, r - cminK); }
        // lo = max c <= o ; hi = min c >= o+1  (theta <= o, pa hi dolazi samo iz komplementa)
        int lo = -1, hi = INF;
        if (cmaxD >= 0) lo = cmaxD;                         // cmaxD <= theta <= o
        int p = prvi(dk, alpha);                            // komplement: c' >= r - o  =>  c = r - c' <= o
        if (p >= 0) lo = max(lo, r - p);
        int q = zadnji(dk, alpha - 1);                      // c' <= r - o - 1  =>  c >= o + 1
        if (q >= 0) hi = r - q;
        auto interval = [&](ll L, ll R) {
            dodaj[d + z].push_back({(int)L, (int)R});
            if (d >= 1) ukloni[d - 1].push_back({(int)L, (int)R});
        };
        if (lo >= 0 && hi != INF && hi - lo > o + 1) {
            interval(d + cmin, d + lo + o);
            interval(d + hi, d + cmax + o);
        } else {
            interval(d + cmin, d + cmax + o);
        }
    }
    Seg seg(S + 1);
    ll odgovor = 0;
    for (ll Dp = B + z; Dp >= 0; --Dp) {
        for (auto [L, R] : dodaj[Dp]) seg.add(L, R, 1);
        for (auto [L, R] : ukloni[Dp]) seg.add(L, R, -1);
        odgovor += seg.pokriveno();
    }
    printf("%lld\n", odgovor);
    return 0;
}
