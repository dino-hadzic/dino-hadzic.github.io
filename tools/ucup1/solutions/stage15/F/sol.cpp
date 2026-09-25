// UCup 1, Stage 15 (ZJCPC 2023), F. Classic: Classical Problem
// Ako 0 nije u S, jedino c=0 daje mex 1. Inače za c≠0 i d=c^{-1}: mex ≥ W  <=>  d,2d,...,(W-1)d ∈ S.
// Preko primitivnog korijena g množenje postaje zbrajanje eksponenata mod (p-1), pa je uvjet
// „I(k)+x ∈ I(S) za sve k<W” ciklička korelacija indikatora (NTT). Binarno tražimo najveći W.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 998244353;

ll pw(ll b, ll e, ll m) { ll r = 1; b %= m; while (e) { if (e & 1) r = r * b % m; b = b * b % m; e >>= 1; } return r; }

void ntt(vector<ll>& a, bool inv) {
    int n = a.size();
    for (int i = 1, j = 0; i < n; ++i) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    for (int len = 2; len <= n; len <<= 1) {
        ll w = pw(3, (MOD - 1) / len, MOD);
        if (inv) w = pw(w, MOD - 2, MOD);
        for (int i = 0; i < n; i += len) {
            ll wn = 1;
            for (int j = 0; j < len / 2; ++j) {
                ll u = a[i + j], v = a[i + j + len / 2] * wn % MOD;
                a[i + j] = u + v < MOD ? u + v : u + v - MOD;
                a[i + j + len / 2] = u - v >= 0 ? u - v : u - v + MOD;
                wn = wn * w % MOD;
            }
        }
    }
    if (inv) { ll ni = pw(n, MOD - 2, MOD); for (ll& x : a) x = x * ni % MOD; }
}

int primitivniKorijen(int p) {
    if (p == 2) return 1;
    int phi = p - 1, t = phi;
    vector<int> fakt;
    for (int q = 2; (ll)q * q <= t; ++q) if (t % q == 0) { fakt.push_back(q); while (t % q == 0) t /= q; }
    if (t > 1) fakt.push_back(t);
    for (int g = 2; ; ++g) {
        bool ok = true;
        for (int q : fakt) if (pw(g, phi / q, p) == 1) { ok = false; break; }
        if (ok) return g;
    }
}

int main() {
    int T; scanf("%d", &T);
    while (T--) {
        int n, p; scanf("%d %d", &n, &p);
        vector<int> a(n); vector<char> uS(p, 0);
        for (int& x : a) { scanf("%d", &x); uS[x] = 1; }
        if (!uS[0]) { puts("1 1"); puts("0"); continue; }
        int L = p - 1, g = primitivniKorijen(p);
        vector<int> lg(p, -1), potg(L);          // lg[g^i]=i, potg[i]=g^i
        for (ll i = 0, cur = 1; i < L; ++i, cur = cur * g % p) { potg[i] = cur; lg[cur] = i; }
        int sz = 1; while (sz < 2 * L) sz <<= 1;
        vector<ll> A(sz, 0);                      // A[i]=1 ako g^i ∈ S
        for (int i = 0; i < L; ++i) A[i] = uS[potg[i]];
        ntt(A, false);
        // korel(W): C[x] = broj k∈[1,W-1] s I(k)+x ∈ I(S); vraća x-eve s C[x]=W-1
        auto korel = [&](int W) {
            vector<ll> B(sz, 0);                  // Brev[t] = 1 ako je t ≡ -I(k) za neki k<W
            for (int k = 1; k < W; ++k) B[(L - lg[k]) % L] = 1;
            ntt(B, false);
            for (int i = 0; i < sz; ++i) B[i] = B[i] * A[i] % MOD;
            ntt(B, true);
            vector<int> res;
            for (int x = 0; x < L; ++x) {
                ll c = B[x] + (x + L < sz ? B[x + L] : 0);   // ciklička konvolucija duljine L
                if (c == W - 1) res.push_back(x);
            }
            return res;
        };
        int lo = 1, hi = n;                       // W=1 uvijek moguć; mex ≤ n
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (!korel(mid).empty()) lo = mid; else hi = mid - 1;
        }
        vector<int> cs;
        if (lo == 1) { for (int c = 0; c < p; ++c) cs.push_back(c); }    // svi c daju mex 1
        else {
            for (int x : korel(lo)) cs.push_back(potg[(L - x) % L]);      // c = d^{-1} = g^{-x}
            sort(cs.begin(), cs.end());
        }
        printf("%d %d\n", (int)cs.size(), lo);
        for (size_t i = 0; i < cs.size(); ++i) printf("%d%c", cs[i], i + 1 == cs.size() ? '\n' : ' ');
    }
    return 0;
}
